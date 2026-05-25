#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHUNKS = ROOT / "knowledge-index" / "chunks.jsonl"
DEFAULT_OUTPUT = ROOT / "knowledge-index" / "semantic"
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def require_semantic_dependencies():
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
        joined = ", ".join(missing)
        raise RuntimeError(
            f"Missing semantic index dependencies: {joined}. "
            "Install with: pip install -r BA-agent/requirements-semantic-index.txt"
        )
    return np, SentenceTransformer


def load_chunks(path: Path, limit: int = 0) -> List[Dict[str, object]]:
    chunks = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            chunks.append(json.loads(line))
        if limit and len(chunks) >= limit:
            break
    return chunks


def chunk_text(record: Dict[str, object]) -> str:
    tags = record.get("tags", [])
    if not isinstance(tags, list):
        tags = []
    fields = [
        str(record.get("source_name", "")),
        str(record.get("area", "")),
        " ".join(str(tag) for tag in tags),
        str(record.get("text", "")),
    ]
    return "\n".join(part for part in fields if part.strip())


def write_records(records: Iterable[Dict[str, object]], path: Path) -> int:
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as out:
        for record in records:
            slim = {
                "id": record.get("id"),
                "source_path": record.get("source_path"),
                "source_name": record.get("source_name"),
                "area": record.get("area"),
                "extension": record.get("extension"),
                "extraction": record.get("extraction"),
                "chunk_index": record.get("chunk_index"),
                "page_start": record.get("page_start"),
                "page_end": record.get("page_end"),
                "tags": record.get("tags"),
                "text": record.get("text"),
            }
            out.write(json.dumps(slim, ensure_ascii=False) + "\n")
            count += 1
    return count


def build_semantic_index(chunks_path: Path, output_dir: Path, model_name: str, batch_size: int, limit: int = 0) -> Dict[str, object]:
    np, SentenceTransformer = require_semantic_dependencies()
    chunks = load_chunks(chunks_path, limit=limit)
    if not chunks:
        raise RuntimeError(f"No chunks found in {chunks_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    model = SentenceTransformer(model_name)
    texts = [chunk_text(record) for record in chunks]
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    embeddings = embeddings.astype("float32")

    embeddings_path = output_dir / "embeddings.npy"
    records_path = output_dir / "records.jsonl"
    manifest_path = output_dir / "manifest.json"
    np.save(str(embeddings_path), embeddings)
    record_count = write_records(chunks, records_path)

    faiss_index_file = None
    faiss_available = False
    try:
        import faiss  # type: ignore

        faiss_available = True
        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        faiss_index_file = "index.faiss"
        faiss.write_index(index, str(output_dir / faiss_index_file))
    except Exception:
        faiss_available = False

    manifest = {
        "version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "type": "semantic-vector-index",
        "model": model_name,
        "source_chunks": str(chunks_path),
        "records_file": "records.jsonl",
        "embeddings_file": "embeddings.npy",
        "faiss_available": faiss_available,
        "faiss_index_file": faiss_index_file,
        "records": record_count,
        "dimensions": int(embeddings.shape[1]),
        "normalized": True,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an optional semantic embedding index for BA-agent.")
    parser.add_argument("--chunks", default=str(DEFAULT_CHUNKS), help="Path to chunks.jsonl")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Semantic index output folder")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="SentenceTransformers model name")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--limit", type=int, default=0, help="Limit chunks for smoke tests")
    args = parser.parse_args()

    try:
        manifest = build_semantic_index(
            chunks_path=Path(args.chunks).resolve(),
            output_dir=Path(args.output).resolve(),
            model_name=args.model,
            batch_size=args.batch_size,
            limit=args.limit,
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
