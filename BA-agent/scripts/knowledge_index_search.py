#!/usr/bin/env python3
import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "knowledge-index" / "chunks.jsonl"
_CORPUS_CACHE: Dict[int, Tuple[List[List[str]], Dict[str, int], float]] = {}


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def tokenize(text: str) -> List[str]:
    return re.findall(r"[\wÀ-ỹ]+", text.lower(), flags=re.UNICODE)


QUERY_EXPANSIONS = {
    "nghiệm thu": ["uat", "acceptance", "sign", "off", "evidence", "handover"],
    "nghiem thu": ["uat", "acceptance", "sign", "off", "evidence", "handover"],
    "nhà thầu": ["vendor", "outsource", "contractor", "handover"],
    "nha thau": ["vendor", "outsource", "contractor", "handover"],
    "truy vết": ["traceability", "rtm", "matrix", "mapping"],
    "truy vet": ["traceability", "rtm", "matrix", "mapping"],
    "yêu cầu": ["requirement", "requirements", "brd", "srs"],
    "yeu cau": ["requirement", "requirements", "brd", "srs"],
    "quy trình": ["process", "workflow", "bpmn"],
    "quy trinh": ["process", "workflow", "bpmn"],
    "báo cáo": ["report", "reporting", "dashboard", "kpi"],
    "bao cao": ["report", "reporting", "dashboard", "kpi"],
    "phân quyền": ["rbac", "role", "permission", "access"],
    "phan quyen": ["rbac", "role", "permission", "access"],
    "rủi ro": ["risk", "raid", "assumption", "issue", "dependency"],
    "rui ro": ["risk", "raid", "assumption", "issue", "dependency"],
    "kiểm thử": ["test", "testing", "uat", "testcase"],
    "kiem thu": ["test", "testing", "uat", "testcase"],
    "signoff": ["sign", "off", "acceptance", "approval", "uat"],
    "sign-off": ["sign", "off", "acceptance", "approval", "uat"],
    "acceptance": ["uat", "test", "sign", "off", "criteria"],
    "vendor": ["outsource", "contractor", "handover", "acceptance"],
    "outsource": ["vendor", "contractor", "change", "request", "handover"],
    "stakeholder": ["elicitation", "interview", "workshop", "raci"],
}


def expand_query_terms(query: str) -> List[str]:
    terms = tokenize(query)
    expanded = list(terms)
    lowered = query.lower()
    for phrase, synonyms in QUERY_EXPANSIONS.items():
        if phrase in lowered or any(token in terms for token in tokenize(phrase)):
            expanded.extend(synonyms)
    return expanded


def load_chunks(index_path: Path = DEFAULT_INDEX) -> List[Dict[str, object]]:
    if not index_path.exists():
        raise FileNotFoundError(f"Knowledge index not found: {index_path}")
    chunks = []
    for line in index_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            chunks.append(json.loads(line))
    return chunks


def chunk_search_text(chunk: Dict[str, object]) -> str:
    tags = chunk.get("tags", [])
    if not isinstance(tags, list):
        tags = []
    return str(chunk.get("text", "")) + " " + " ".join(str(tag) for tag in tags)


def corpus_stats(chunks: List[Dict[str, object]]) -> Tuple[List[List[str]], Dict[str, int], float]:
    cache_key = id(chunks)
    if cache_key in _CORPUS_CACHE:
        return _CORPUS_CACHE[cache_key]
    tokenized = [tokenize(chunk_search_text(chunk)) for chunk in chunks]
    doc_freq = defaultdict(int)
    for terms in tokenized:
        for term in set(terms):
            doc_freq[term] += 1
    avg_len = sum(len(terms) for terms in tokenized) / max(1, len(tokenized))
    stats = (tokenized, doc_freq, avg_len)
    _CORPUS_CACHE[cache_key] = stats
    return stats


def bm25_search(
    query: str,
    chunks: List[Dict[str, object]],
    limit: int = 8,
    expanded: bool = False,
) -> List[Dict[str, object]]:
    query_terms = expand_query_terms(query) if expanded else tokenize(query)
    if not query_terms:
        return []
    tokenized, doc_freq, avg_len = corpus_stats(chunks)
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
            record["bm25_score"] = round(score, 4)
            record["score"] = round(score, 4)
            record["retrieval_mode"] = "bm25"
            scores.append(record)
    scores.sort(key=lambda item: (-item["score"], str(item.get("source_path", "")), int(item.get("chunk_index", 0))))
    return scores[:limit]


def vector_search(query: str, chunks: List[Dict[str, object]], limit: int = 8) -> List[Dict[str, object]]:
    query_terms = expand_query_terms(query)
    if not query_terms:
        return []
    tokenized, doc_freq, _ = corpus_stats(chunks)
    total_docs = max(1, len(chunks))
    query_counts = Counter(query_terms)
    query_weights = {
        term: count * math.log(1 + total_docs / (1 + doc_freq.get(term, 0)))
        for term, count in query_counts.items()
    }
    query_norm = math.sqrt(sum(weight * weight for weight in query_weights.values()))
    if query_norm == 0:
        return []

    scores = []
    query_vocab = set(query_weights)
    for idx, terms in enumerate(tokenized):
        if not terms:
            continue
        counts = Counter(term for term in terms if term in query_vocab)
        if not counts:
            continue
        dot = 0.0
        doc_norm = 0.0
        for term, count in counts.items():
            weight = (1 + math.log(count)) * math.log(1 + total_docs / (1 + doc_freq.get(term, 0)))
            dot += weight * query_weights[term]
            doc_norm += weight * weight
        if doc_norm == 0:
            continue
        score = dot / (math.sqrt(doc_norm) * query_norm)
        if score > 0:
            record = dict(chunks[idx])
            record["vector_score"] = round(score, 4)
            record["score"] = round(score, 4)
            record["retrieval_mode"] = "vector"
            scores.append(record)
    scores.sort(key=lambda item: (-item["score"], str(item.get("source_path", "")), int(item.get("chunk_index", 0))))
    return scores[:limit]


def normalize_scores(items: Iterable[Dict[str, object]], score_key: str) -> Dict[str, float]:
    materialized = list(items)
    max_score = max((float(item.get(score_key, 0) or 0) for item in materialized), default=0.0)
    if max_score <= 0:
        return {}
    return {str(item.get("id")): float(item.get(score_key, 0) or 0) / max_score for item in materialized}


def hybrid_search(query: str, chunks: List[Dict[str, object]], limit: int = 8) -> List[Dict[str, object]]:
    candidate_limit = max(limit * 6, 40)
    bm25_results = bm25_search(query, chunks, limit=candidate_limit, expanded=True)
    vector_results = vector_search(query, chunks, limit=candidate_limit)
    by_id: Dict[str, Dict[str, object]] = {}
    for item in bm25_results + vector_results:
        by_id.setdefault(str(item.get("id")), dict(item))

    bm25_norm = normalize_scores(bm25_results, "bm25_score")
    vector_norm = normalize_scores(vector_results, "vector_score")
    for chunk_id, item in by_id.items():
        bm25_component = bm25_norm.get(chunk_id, 0.0)
        vector_component = vector_norm.get(chunk_id, 0.0)
        hybrid_score = 0.62 * bm25_component + 0.38 * vector_component
        item["bm25_score"] = next((r.get("bm25_score") for r in bm25_results if str(r.get("id")) == chunk_id), 0)
        item["vector_score"] = next((r.get("vector_score") for r in vector_results if str(r.get("id")) == chunk_id), 0)
        item["score"] = round(hybrid_score, 4)
        item["retrieval_mode"] = "hybrid"
    scores = [item for item in by_id.values() if float(item.get("score", 0) or 0) > 0]
    scores.sort(key=lambda item: (-float(item["score"]), str(item.get("source_path", "")), int(item.get("chunk_index", 0))))
    return scores[:limit]


def search(query: str, chunks: List[Dict[str, object]], limit: int = 8, mode: str = "hybrid") -> List[Dict[str, object]]:
    if mode == "bm25":
        return bm25_search(query, chunks, limit=limit, expanded=False)
    if mode == "vector":
        return vector_search(query, chunks, limit=limit)
    return hybrid_search(query, chunks, limit=limit)


def source_ref(record: Dict[str, object]) -> str:
    ref = f"{record.get('source_path')}#chunk-{record.get('chunk_index')}"
    if record.get("page_start"):
        ref += f":page-{record.get('page_start')}"
    return ref


def clean_excerpt(text: str, max_chars: int = 650) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\b(read|page)\b(?:\s+\1\b){2,}", r"\1", text, flags=re.IGNORECASE)
    if len(text) > max_chars:
        text = text[: max_chars - 3].rstrip() + "..."
    return text


def compact(record: Dict[str, object], max_chars: int = 650) -> Dict[str, object]:
    return {
        "id": record.get("id"),
        "score": record.get("score"),
        "bm25_score": record.get("bm25_score"),
        "vector_score": record.get("vector_score"),
        "retrieval_mode": record.get("retrieval_mode"),
        "source_ref": source_ref(record),
        "source_path": record.get("source_path"),
        "source_name": record.get("source_name"),
        "area": record.get("area"),
        "tags": record.get("tags"),
        "extraction": record.get("extraction"),
        "chunk_index": record.get("chunk_index"),
        "excerpt": clean_excerpt(str(record.get("text", "")), max_chars=max_chars),
    }


def format_markdown(results: List[Dict[str, object]], max_chars: int = 900) -> str:
    if not results:
        return "No matching indexed BA knowledge chunks found."
    lines = []
    for item in results:
        lines.append(f"## {source_ref(item)}")
        score_bits = [f"score {item.get('score')}"]
        if item.get("bm25_score"):
            score_bits.append(f"bm25 {item.get('bm25_score')}")
        if item.get("vector_score"):
            score_bits.append(f"vector {item.get('vector_score')}")
        if item.get("retrieval_mode"):
            score_bits.append(f"mode {item.get('retrieval_mode')}")
        lines.append(f"Source: {item.get('source_name') or item.get('source_path')} ({', '.join(score_bits)})")
        if item.get("extraction"):
            lines.append(f"Extraction: {item.get('extraction')}")
        tags = ", ".join(item.get("tags", []))
        if tags:
            lines.append(f"Tags: {tags}")
        lines.append(clean_excerpt(str(item.get("text", "")), max_chars=max_chars))
        lines.append("")
    return "\n".join(lines).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Hybrid search over the self-contained BA knowledge index.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--index", default=str(DEFAULT_INDEX), help="Path to chunks.jsonl")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--mode", choices=["hybrid", "bm25", "vector"], default="hybrid")
    parser.add_argument("--max-chars", type=int, default=900, help="Maximum excerpt length per result")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    try:
        chunks = load_chunks(Path(args.index).resolve())
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    results = search(args.query, chunks, limit=args.limit, mode=args.mode)
    if args.format == "markdown":
        print(format_markdown(results, max_chars=args.max_chars))
    else:
        print(json.dumps(
            {
                "query": args.query,
                "mode": args.mode,
                "expanded_terms": expand_query_terms(args.query),
                "results": [compact(item, max_chars=args.max_chars) for item in results],
            },
            indent=2,
            ensure_ascii=False,
        ))
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
