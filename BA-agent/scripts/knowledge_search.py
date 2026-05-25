#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List


ROOT = Path(__file__).resolve().parents[1]
CARDS_PATH = ROOT / "BA-document-rule" / "references" / "ba-knowledge-cards.json"


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def tokenize(text: str) -> List[str]:
    return re.findall(r"[\wÀ-ỹ]+", text.lower(), flags=re.UNICODE)


def load_cards(path: Path = CARDS_PATH) -> List[Dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("cards", [])


def flatten_values(value: object) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from flatten_values(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from flatten_values(item)


def card_text(card: Dict[str, object]) -> str:
    return " ".join(flatten_values(card))


def score_card(card: Dict[str, object], query_tokens: List[str]) -> int:
    if not query_tokens:
        return 0
    weighted_parts = {
        "title": 5,
        "aliases": 4,
        "tags": 3,
        "summary": 2,
    }
    score = 0
    for field, weight in weighted_parts.items():
        field_text = " ".join(flatten_values(card.get(field, ""))).lower()
        for token in query_tokens:
            if token in field_text:
                score += weight
    all_tokens = set(tokenize(card_text(card)))
    score += sum(1 for token in query_tokens if token in all_tokens)
    return score


def search_cards(query: str, limit: int = 5, cards: List[Dict[str, object]] = None) -> List[Dict[str, object]]:
    cards = cards if cards is not None else load_cards()
    query_tokens = tokenize(query)
    ranked = []
    for card in cards:
        score = score_card(card, query_tokens)
        if score > 0:
            ranked.append({"score": score, **card})
    ranked.sort(key=lambda item: (-item["score"], item["id"]))
    return ranked[:limit]


def compact_card(card: Dict[str, object]) -> Dict[str, object]:
    keys = ["id", "score", "title", "summary", "tags", "use_when", "quality_checks", "traceability"]
    return {key: card[key] for key in keys if key in card}


def format_markdown(results: List[Dict[str, object]]) -> str:
    if not results:
        return "No matching BA knowledge cards found."
    lines = []
    for card in results:
        lines.append(f"## {card['id']} — {card['title']} (score {card['score']})")
        lines.append(str(card.get("summary", "")))
        if card.get("quality_checks"):
            lines.append("")
            lines.append("Quality checks:")
            for item in card["quality_checks"]:
                lines.append(f"- {item}")
        if card.get("traceability"):
            lines.append("")
            lines.append(f"Traceability: {card['traceability']}")
        lines.append("")
    return "\n".join(lines).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the self-contained BA knowledge cards.")
    parser.add_argument("query", help="Search query, e.g. 'UAT traceability' or 'AI prediction feature'")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of cards to return")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    results = search_cards(args.query, limit=args.limit)
    if args.format == "markdown":
        print(format_markdown(results))
    else:
        print(json.dumps({"query": args.query, "results": [compact_card(card) for card in results]}, indent=2, ensure_ascii=False))
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
