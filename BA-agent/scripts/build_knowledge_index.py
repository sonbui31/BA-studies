#!/usr/bin/env python3
import argparse
import hashlib
import json
import logging
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "knowledge-index"
SUPPORTED_TEXT_EXTENSIONS = {".md", ".txt"}
PANDOC_EXTENSIONS = {".docx", ".pptx"}
PDF_EXTENSIONS = {".pdf"}


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


logging.getLogger("pypdf").setLevel(logging.ERROR)
logging.getLogger("pdfminer").setLevel(logging.ERROR)


def stable_id(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8", errors="ignore")).hexdigest()[:16]


def read_text_file(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "cp1258", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except Exception:
            continue
    return ""


def run_pandoc(path: Path) -> str:
    try:
        completed = subprocess.run(
            ["pandoc", "-t", "plain", str(path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=90,
        )
    except Exception:
        return ""
    if completed.returncode != 0:
        return ""
    return completed.stdout


def extract_pdf_pages_pypdf(path: Path, max_pages: int = 0) -> List[str]:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return []
    try:
        reader = PdfReader(str(path))
        pages = reader.pages[:max_pages] if max_pages else reader.pages
        texts = []
        for page in pages:
            texts.append(page.extract_text() or "")
        return texts
    except Exception:
        return []


def extract_pdf_text_pypdf(path: Path, max_pages: int = 0) -> str:
    return "\n".join(extract_pdf_pages_pypdf(path, max_pages=max_pages))


def extract_pdf_text_pdfminer(path: Path, max_pages: int = 0) -> str:
    try:
        from pdfminer.high_level import extract_text  # type: ignore
    except Exception:
        return ""
    try:
        page_numbers = list(range(max_pages)) if max_pages else None
        return extract_text(str(path), page_numbers=page_numbers) or ""
    except Exception:
        return ""


def extract_pdf_text(path: Path, max_pages: int = 0) -> tuple[str, str, List[str]]:
    # Optional dependency support. If unavailable, caller will fall back to metadata.
    pages = extract_pdf_pages_pypdf(path, max_pages=max_pages)
    text = "\n".join(pages)
    if text.strip():
        return text, "pdf-pypdf", pages
    text = extract_pdf_text_pdfminer(path, max_pages=max_pages)
    if text.strip():
        return text, "pdf-pdfminer", []
    return "", "pdf-metadata", []


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def source_area(path: Path, source_root: Path) -> str:
    try:
        rel = path.relative_to(source_root)
    except ValueError:
        return ""
    return rel.parts[0] if rel.parts else ""


def infer_tags(path: Path, text: str) -> List[str]:
    haystack = f"{path.as_posix()} {text[:2000]}".lower()
    rules = {
        "brd": ["brd", "business requirement"],
        "srs": ["srs", "software requirement", "functional requirement"],
        "uat": ["uat", "acceptance test", "test case"],
        "rtm": ["rtm", "traceability", "truy vết"],
        "elicitation": ["elicitation", "interview", "workshop", "stakeholder", "khơi gợi"],
        "modeling": ["bpmn", "uml", "dfd", "erd", "sequence diagram", "activity diagram"],
        "agile": ["scrum", "agile", "user story", "backlog", "sprint"],
        "product": ["product", "roadmap", "prioritization", "launch"],
        "ux": ["ux", "ui", "wireframe", "prototype", "figma"],
        "data": ["data", "sql", "dashboard", "reporting", "dictionary", "analytics"],
        "api": ["api", "microservice", "rest", "integration"],
        "ai": ["artificial intelligence", "machine learning", "prediction", "predictive", "model confidence", "chatgpt", "quiz generation", "trí tuệ nhân tạo"],
        "domain-finance": ["banking", "finance", "payment", "insurance", "claim", "policy"],
        "healthcare": ["healthcare", "hospital", "clinical", "hl7", "fhir"],
        "government": ["government", "procurement", "public sector"],
    }
    tags = []
    for tag, needles in rules.items():
        if any(needle in haystack for needle in needles):
            tags.append(tag)
    return tags


def chunk_text(text: str, max_words: int = 280, overlap: int = 45) -> List[str]:
    words = text.split()
    if not words:
        return []
    chunks = []
    step = max(1, max_words - overlap)
    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + max_words]).strip()
        if len(chunk.split()) >= 25:
            chunks.append(chunk)
        if start + max_words >= len(words):
            break
    return chunks


def chunk_pages(pages: List[str], max_words: int = 280, overlap: int = 45) -> List[Dict[str, object]]:
    chunks = []
    for page_number, page_text in enumerate(pages, start=1):
        normalized = normalize_text(page_text)
        if not normalized:
            continue
        for chunk in chunk_text(normalized, max_words=max_words, overlap=overlap):
            chunks.append({"text": chunk, "page_start": page_number, "page_end": page_number})
    return chunks


def extract_document(path: Path, source_root: Path, include_pdf_metadata: bool, pdf_max_pages: int = 0) -> Optional[Dict[str, object]]:
    ext = path.suffix.lower()
    text = ""
    extraction = "none"
    if ext in SUPPORTED_TEXT_EXTENSIONS:
        text = read_text_file(path)
        extraction = "text"
    elif ext in PANDOC_EXTENSIONS:
        text = run_pandoc(path)
        extraction = "pandoc"
    elif ext in PDF_EXTENSIONS:
        text, extraction, pages = extract_pdf_text(path, max_pages=pdf_max_pages)
        if not text and include_pdf_metadata:
            try:
                rel_path = path.relative_to(source_root).as_posix()
            except ValueError:
                rel_path = path.name
            text = f"{path.stem}. Source file: {rel_path}"
            pages = []
    else:
        return None

    text = normalize_text(text)
    if not text:
        return None
    rel = path.relative_to(source_root).as_posix()
    return {
        "source_path": rel,
        "source_name": path.name,
        "area": source_area(path, source_root),
        "extension": ext,
        "extraction": extraction,
        "text": text,
        "pages": [normalize_text(page) for page in pages] if ext in PDF_EXTENSIONS else [],
        "tags": infer_tags(path, text),
    }


def iter_source_files(source_root: Path) -> Iterable[Path]:
    allowed = SUPPORTED_TEXT_EXTENSIONS | PANDOC_EXTENSIONS | PDF_EXTENSIONS
    for path in source_root.rglob("*"):
        if path.is_file() and path.suffix.lower() in allowed:
            yield path


def build_index(
    source_root: Path,
    output_dir: Path,
    max_docs: int = 0,
    include_pdf_metadata: bool = True,
    pdf_max_pages: int = 0,
) -> Dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    chunks_path = output_dir / "chunks.jsonl"
    manifest_path = output_dir / "manifest.json"
    stats = {
        "documents_seen": 0,
        "documents_indexed": 0,
        "chunks": 0,
        "by_extension": {},
        "by_extraction": {},
    }
    with chunks_path.open("w", encoding="utf-8", newline="\n") as out:
        for path in iter_source_files(source_root):
            stats["documents_seen"] += 1
            if max_docs and stats["documents_indexed"] >= max_docs:
                break
            doc = extract_document(
                path,
                source_root,
                include_pdf_metadata=include_pdf_metadata,
                pdf_max_pages=pdf_max_pages,
            )
            if not doc:
                continue
            stats["documents_indexed"] += 1
            ext = str(doc["extension"])
            extraction = str(doc["extraction"])
            stats["by_extension"][ext] = stats["by_extension"].get(ext, 0) + 1
            stats["by_extraction"][extraction] = stats["by_extraction"].get(extraction, 0) + 1
            page_chunks = chunk_pages(doc.get("pages", [])) if doc.get("pages") else []
            chunk_records = page_chunks or [{"text": chunk} for chunk in chunk_text(str(doc["text"]))]
            for idx, chunk_record in enumerate(chunk_records):
                chunk = str(chunk_record["text"])
                chunk_id = stable_id(f"{doc['source_path']}:{idx}:{chunk[:80]}")
                record = {
                    "id": chunk_id,
                    "source_path": doc["source_path"],
                    "source_name": doc["source_name"],
                    "area": doc["area"],
                    "extension": doc["extension"],
                    "extraction": doc["extraction"],
                    "chunk_index": idx,
                    "page_start": chunk_record.get("page_start"),
                    "page_end": chunk_record.get("page_end"),
                    "tags": doc["tags"],
                    "text": chunk,
                }
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                stats["chunks"] += 1

    manifest = {
        "version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_root_name": source_root.name,
        "self_contained": True,
        "runtime_source_dependency": False,
        "chunks_file": "chunks.jsonl",
        "citation_granularity": "page-level for PDF documents extracted by pypdf during rebuild",
        "stats": stats,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a self-contained BA knowledge index from source learning documents.")
    parser.add_argument("--source", default=str(ROOT.parent / "BA"), help="Source BA folder")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output index folder")
    parser.add_argument("--max-docs", type=int, default=0, help="Limit indexed documents for testing")
    parser.add_argument("--pdf-max-pages", type=int, default=0, help="Limit PDF pages per file; 0 means all pages")
    parser.add_argument("--no-pdf-metadata", action="store_true", help="Skip PDF metadata fallback chunks when PDF text extraction is unavailable")
    args = parser.parse_args()

    source_root = Path(args.source).resolve()
    if not source_root.exists():
        print(f"ERROR: Source folder not found: {source_root}", file=sys.stderr)
        return 2
    manifest = build_index(
        source_root=source_root,
        output_dir=Path(args.output).resolve(),
        max_docs=args.max_docs,
        include_pdf_metadata=not args.no_pdf_metadata,
        pdf_max_pages=args.pdf_max_pages,
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
