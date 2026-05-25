#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "knowledge-index" / "semantic"


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def require_search_dependencies():
    missing = []
    try:
        import numpy as np  # type: ignore
    except Exception:
        np = None
        missing.append("numpy")
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
    except Exception:
        SentenceTransformer = None
        missing.append("sentence-transformers")
    if missing:
        raise RuntimeError(
            "Missing semantic search dependencies: "
            + ", ".join(missing)
            + ". Install with: pip install -r BA-agent/requirements-semantic-index.txt"
        )
    return np, SentenceTransformer


def load_json(path: Path) -> Dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_records(path: Path) -> List[Dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def source_ref(record: Dict[str, object]) -> str:
    ref = f"{record.get('source_path')}#chunk-{record.get('chunk_index')}"
    if record.get("page_start"):
        ref += f":page-{record.get('page_start')}"
    return ref


def clean_excerpt(text: str, max_chars: int = 650) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_chars:
        text = text[: max_chars - 3].rstrip() + "..."
    return text


def semantic_search(query: str, index_dir: Path, limit: int = 8) -> List[Dict[str, object]]:
    np, SentenceTransformer = require_search_dependencies()
    manifest = load_json(index_dir / "manifest.json")
    records = load_records(index_dir / str(manifest["records_file"]))
    model = SentenceTransformer(str(manifest["model"]))
    query_vector = model.encode([query], convert_to_numpy=True, normalize_embeddings=True).astype("float32")

    faiss_file = manifest.get("faiss_index_file")
    if faiss_file and (index_dir / str(faiss_file)).exists():
        try:
            import faiss  # type: ignore

            index = faiss.read_index(str(index_dir / str(faiss_file)))
            scores, indexes = index.search(query_vector, limit)
            hits = []
            for score, idx in zip(scores[0], indexes[0]):
                if idx < 0:
                    continue
                record = dict(records[int(idx)])
                record["score"] = round(float(score), 4)
                record["retrieval_mode"] = "semantic-faiss"
                hits.append(record)
            return hits
        except Exception:
            pass

    embeddings = np.load(str(index_dir / str(manifest["embeddings_file"])))
    scores = embeddings @ query_vector[0]
    top_indexes = np.argsort(-scores)[:limit]
    hits = []
    for idx in top_indexes:
        record = dict(records[int(idx)])
        record["score"] = round(float(scores[int(idx)]), 4)
        record["retrieval_mode"] = "semantic-numpy"
        hits.append(record)
    return hits


def compact(record: Dict[str, object], max_chars: int = 650) -> Dict[str, object]:
    return {
        "id": record.get("id"),
        "score": record.get("score"),
        "retrieval_mode": record.get("retrieval_mode"),
        "source_ref": source_ref(record),
        "source_path": record.get("source_path"),
        "source_name": record.get("source_name"),
        "page_start": record.get("page_start"),
        "page_end": record.get("page_end"),
        "tags": record.get("tags"),
        "excerpt": clean_excerpt(str(record.get("text", "")), max_chars=max_chars),
    }


def format_markdown(results: List[Dict[str, object]], max_chars: int = 900) -> str:
    if not results:
        return "No semantic BA knowledge chunks found."
    lines = []
    for item in results:
        lines.append(f"## {source_ref(item)}")
        lines.append(f"Source: {item.get('source_name') or item.get('source_path')} (score {item.get('score')}, mode {item.get('retrieval_mode')})")
        tags = ", ".join(item.get("tags", []))
        if tags:
            lines.append(f"Tags: {tags}")
        lines.append(clean_excerpt(str(item.get("text", "")), max_chars=max_chars))
        lines.append("")
    return "\n".join(lines).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the optional semantic embedding index for BA-agent.")
    parser.add_argument("query")
    parser.add_argument("--index", default=str(DEFAULT_INDEX))
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--max-chars", type=int, default=900)
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    index_dir = Path(args.index).resolve()
    if not (index_dir / "manifest.json").exists():
        print(f"ERROR: Semantic index not found: {index_dir}", file=sys.stderr)
        return 2
    try:
        results = semantic_search(args.query, index_dir=index_dir, limit=args.limit)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.format == "markdown":
        print(format_markdown(results, max_chars=args.max_chars))
    else:
        print(json.dumps({"query": args.query, "results": [compact(item, args.max_chars) for item in results]}, indent=2, ensure_ascii=False))
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
