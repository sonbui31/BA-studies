#!/usr/bin/env python3
import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "knowledge-index" / "chunks.jsonl"


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def tokenize(text: str) -> List[str]:
    return re.findall(r"[\wÀ-ỹ]+", text.lower(), flags=re.UNICODE)


def load_chunks(index_path: Path = DEFAULT_INDEX) -> List[Dict[str, object]]:
    if not index_path.exists():
        raise FileNotFoundError(f"Knowledge index not found: {index_path}")
    chunks = []
    for line in index_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            chunks.append(json.loads(line))
    return chunks


def bm25_search(query: str, chunks: List[Dict[str, object]], limit: int = 8) -> List[Dict[str, object]]:
    query_terms = tokenize(query)
    if not query_terms:
        return []
    tokenized = [tokenize(str(chunk.get("text", "")) + " " + " ".join(chunk.get("tags", []))) for chunk in chunks]
    doc_freq = defaultdict(int)
    for terms in tokenized:
        for term in set(terms):
            doc_freq[term] += 1
    avg_len = sum(len(terms) for terms in tokenized) / max(1, len(tokenized))
    k1 = 1.5
    b = 0.75
    scores = []
    for idx, terms in enumerate(tokenized):
        if not terms:
            continue
        counts = Counter(terms)
        score = 0.0
        for term in query_terms:
            if term not in counts:
                continue
            df = doc_freq.get(term, 0)
            idf = math.log(1 + (len(chunks) - df + 0.5) / (df + 0.5))
            tf = counts[term]
            denom = tf + k1 * (1 - b + b * len(terms) / max(1, avg_len))
            score += idf * (tf * (k1 + 1) / denom)
        if score > 0:
            record = dict(chunks[idx])
            record["score"] = round(score, 4)
            scores.append(record)
    scores.sort(key=lambda item: (-item["score"], str(item.get("source_path", "")), int(item.get("chunk_index", 0))))
    return scores[:limit]


def compact(record: Dict[str, object], max_chars: int = 650) -> Dict[str, object]:
    text = str(record.get("text", ""))
    if len(text) > max_chars:
        text = text[: max_chars - 3].rstrip() + "..."
    return {
        "id": record.get("id"),
        "score": record.get("score"),
        "source_path": record.get("source_path"),
        "area": record.get("area"),
        "tags": record.get("tags"),
        "extraction": record.get("extraction"),
        "chunk_index": record.get("chunk_index"),
        "text": text,
    }


def format_markdown(results: List[Dict[str, object]]) -> str:
    if not results:
        return "No matching indexed BA knowledge chunks found."
    lines = []
    for item in results:
        lines.append(f"## {item.get('source_path')}#chunk-{item.get('chunk_index')} (score {item.get('score')})")
        tags = ", ".join(item.get("tags", []))
        if tags:
            lines.append(f"Tags: {tags}")
        lines.append(str(item.get("text", "")).strip())
        lines.append("")
    return "\n".join(lines).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="BM25 search over the self-contained BA knowledge index.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--index", default=str(DEFAULT_INDEX), help="Path to chunks.jsonl")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    try:
        chunks = load_chunks(Path(args.index).resolve())
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    results = bm25_search(args.query, chunks, limit=args.limit)
    if args.format == "markdown":
        print(format_markdown(results))
    else:
        print(json.dumps({"query": args.query, "results": [compact(item) for item in results]}, indent=2, ensure_ascii=False))
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
