#!/usr/bin/env python3
import argparse
import json
import re
import sys
from collections import defaultdict, deque
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

from ba_id_utils import (
    MarkdownId,
    classify_file,
    collect_markdown_files,
    detect_id_meta,
    extract_headings,
    extract_ids,
    extract_ids_from_line,
    heading_gaps,
    iter_non_fenced_lines,
    read_text,
    sequence_gaps,
)


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def normalize_kind(raw: str) -> str:
    if raw.startswith(("BRQ-", "BRD-", "BR-")):
        return "business"
    if raw.startswith("FR-"):
        return "functional"
    if raw.startswith("NFR-"):
        return "nonfunctional"
    if raw.startswith("US"):
        return "story"
    if raw.startswith(("AC-", "TC-", "UAT-")):
        return "test"
    if (raw.startswith("F") and raw[1:].isdigit()) or re.match(r"^F-\d{3}$", raw):
        return "feature"
    return "other"


ROLE_DEFINITION_KINDS = {
    "brd": {"business"},
    "srs": {"functional", "nonfunctional"},
    "story": {"story"},
    "uat": {"test"},
    "feature": {"feature"},
}


CANONICAL_PATTERNS = {
    "business": re.compile(r"^(?:BRQ-\d+(?:\.\d+)?|BR-\d{3})$"),
    "functional": re.compile(r"^FR-[A-Z]{2,10}-\d{3}$"),
    "nonfunctional": re.compile(r"^NFR-[A-Z]{2,10}-\d{3}$"),
    "story": re.compile(r"^US-[A-Z]{2,10}-\d{3}$"),
    "test": re.compile(r"^(?:AC|TC)-[A-Z]{2,10}-\d{3}$"),
    "feature": re.compile(r"^(?:F\d{2}|F-\d{3})$"),
}

LEGACY_PATTERNS = {
    "business": re.compile(r"^(?:BRD-\d{3}|BR-\d{3})$"),
    "functional": re.compile(r"^FR-\d{3}$"),
    "nonfunctional": re.compile(r"^NFR-\d{2,3}$"),
    "story": re.compile(r"^(?:US-\d{3}|US\d{2,3})$"),
    "test": re.compile(r"^(?:AC-\d{2,3}|UAT(?:-[A-Z]+)?-\d{2,3}|TC-\d{3}|TC-\d{2}-[A-Z])$"),
    "feature": re.compile(r"^(?:F\d{2}|F-\d{3})$"),
}


def bfs(graph: Dict[str, Set[str]], start: str) -> Set[str]:
    visited: Set[str] = set()
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        queue.extend(neighbor for neighbor in graph.get(current, set()) if neighbor not in visited)
    return visited


def tokens_by_kind(tokens: Iterable[str]) -> Dict[str, Set[str]]:
    grouped: Dict[str, Set[str]] = defaultdict(set)
    for token in tokens:
        grouped[normalize_kind(token)].add(token)
    return grouped


def add_test_alias_edges(graph: Dict[str, Set[str]], tokens: Set[str]) -> None:
    simple_ac = re.compile(r"^AC-(\d{2,3})$")
    simple_tc = re.compile(r"^TC-(\d{3})$")
    simple_uat = re.compile(r"^UAT-(\d{3})$")
    suffixes = set()
    for token in tokens:
        if match := simple_ac.match(token):
            suffixes.add(match.group(1).zfill(3))
        if match := simple_tc.match(token):
            suffixes.add(match.group(1))
        if match := simple_uat.match(token):
            suffixes.add(match.group(1))
    for suffix in suffixes:
        ac_token = f"AC-{suffix}"
        short_ac_token = f"AC-{int(suffix):02d}"
        tc_token = f"TC-{suffix}"
        uat_token = f"UAT-{suffix}"
        aliases = [token for token in (ac_token, short_ac_token, tc_token, uat_token) if token in tokens]
        for left in aliases:
            for right in aliases:
                if left != right:
                    graph[left].add(right)


def token_allowed(token: str, scheme: str) -> bool:
    if scheme == "auto":
        return True
    kind = normalize_kind(token)
    if kind == "other":
        return False
    patterns = CANONICAL_PATTERNS if scheme == "canonical" else LEGACY_PATTERNS
    pattern = patterns.get(kind)
    return bool(pattern and pattern.match(token))


def build_report(target: Path, scheme: str = "auto", strict: bool = False) -> Tuple[dict, int]:
    if not target.exists():
        raise FileNotFoundError(f"Target does not exist: {target}")
    files = collect_markdown_files(target)
    graph: Dict[str, Set[str]] = defaultdict(set)
    reverse_graph: Dict[str, Set[str]] = defaultdict(set)
    definitions: Dict[str, Set[str]] = defaultdict(set)
    references: Dict[str, Set[str]] = defaultdict(set)
    file_roles: Dict[Path, str] = {}
    gaps: List[dict] = []
    headings_report: List[str] = []
    index_duplicates: List[str] = []
    index_skips: List[str] = []

    def add_edge(left: str, right: str) -> None:
        if left == right:
            return
        graph[left].add(right)
        reverse_graph[right].add(left)

    def add_edges(lefts: Iterable[str], rights: Iterable[str]) -> None:
        for left in lefts:
            for right in rights:
                add_edge(left, right)

    def add_trace_edges(role: str, tokens: List[str], feature_definition_row: bool = False) -> None:
        grouped = tokens_by_kind(tokens)
        business = grouped["business"]
        functional = grouped["functional"]
        nonfunctional = grouped["nonfunctional"]
        requirements = functional | nonfunctional
        features = grouped["feature"]
        stories = grouped["story"]
        tests = grouped["test"]

        if role == "srs":
            add_edges(business, requirements)
            add_edges(requirements, features | tests)
            return
        if role == "feature":
            feature_map_row = feature_definition_row or bool(tokens and normalize_kind(tokens[0]) == "feature")
            if len(business) <= 1 or feature_map_row:
                add_edges(business, requirements)
            add_edges(business, features)
            add_edges(requirements, features | stories | tests)
            add_edges(features, stories | tests)
            add_edges(stories, tests)
            return
        if role == "story":
            add_edges(business | requirements | features, stories)
            add_edges(requirements, features)
            add_edges(stories, tests)
            return
        if role == "uat":
            add_edges(business | requirements | features | stories, tests)
            return
        if role == "brd":
            if len(business) <= 1:
                add_edges(business, requirements)
            add_edges(business, features | stories | tests)
            add_edges(requirements, features | stories | tests)
            add_edges(features, stories | tests)
            add_edges(stories, tests)
            return
        add_edges(business, requirements | features)
        add_edges(requirements, features | stories | tests)
        add_edges(features, stories | tests)
        add_edges(stories, tests)

    def normalize_role(path: Path) -> str:
        name = path.name.lower()
        if "beta" in name:
            return "uat"
        return classify_file(path)

    def definition_ids_for_role(text: str, role: str) -> List[MarkdownId]:
        ids: List[MarkdownId] = []
        def ids_from_cell(cell: str, line_no: int) -> List[MarkdownId]:
            found: List[MarkdownId] = []
            for token in extract_ids_from_line(cell):
                meta = detect_id_meta(token, line_no)
                if meta:
                    found.append(meta)
            return found

        for line_no, line in iter_non_fenced_lines(text):
            stripped = line.lstrip()
            if role == "brd":
                if stripped.startswith("| BRQ-") or stripped.startswith("| BRD-") or stripped.startswith("| BR-"):
                    first_cell = stripped.strip().strip("|").split("|")[0].strip()
                    ids.extend(ids_from_cell(first_cell, line_no))
                elif stripped.startswith("- BRQ-") or stripped.startswith("- BR-"):
                    ids.extend(ids_from_cell(line, line_no))
                elif re.match(r"^(BRQ-\d+(?:\.\d+)?|BRD-\d{3}|BR-\d{3})\b", stripped):
                    first_token = stripped.split()[0]
                    ids.extend(ids_from_cell(first_token, line_no))
            elif role == "srs":
                if stripped.startswith("| FR-") or stripped.startswith("| NFR-"):
                    cells = [cell.strip() for cell in stripped.strip().strip("|").split("|")]
                    first_cell = cells[0] if cells else ""
                    if first_cell.startswith("NFR-") and any("UAT-NFR-" in cell for cell in cells):
                        continue
                    if first_cell.startswith("NFR-") and len(cells) < 5:
                        continue
                    ids.extend(ids_from_cell(first_cell, line_no))
                elif re.match(r"^(FR-\d{3}|NFR-\d{2,3})\b", stripped):
                    first_token = stripped.split()[0]
                    ids.extend(ids_from_cell(first_token, line_no))
            elif role == "story":
                if stripped.startswith("| US-") or stripped.startswith("| US"):
                    first_cell = stripped.strip().strip("|").split("|")[0].strip()
                    ids.extend(ids_from_cell(first_cell, line_no))
                elif re.match(r"^(US-\d{3}|US\d{2,3})\b", stripped):
                    first_token = stripped.split()[0]
                    ids.extend(ids_from_cell(first_token, line_no))
            elif role == "uat":
                if stripped.startswith("| AC-") or stripped.startswith("| UAT-") or stripped.startswith("| TC-") or stripped.startswith("| IT-"):
                    first_cell = stripped.strip().strip("|").split("|")[0].strip()
                    ids.extend(ids_from_cell(first_cell, line_no))
                elif re.match(r"^(AC-\d{2,3}|UAT-\d{3}|TC-\d{3}|TC-\d{2}-[A-Z])\b", stripped):
                    first_token = stripped.split()[0]
                    ids.extend(ids_from_cell(first_token, line_no))
            elif role == "feature":
                if stripped.startswith("| F"):
                    first_cell = stripped.strip().strip("|").split("|")[0].strip()
                    ids.extend(ids_from_cell(first_cell, line_no))
                elif re.match(r"^(?:F\d{2}|F-\d{3})\b", stripped):
                    first_token = stripped.split()[0]
                    ids.extend(ids_from_cell(first_token, line_no))
        return ids

    for path in files:
        role = normalize_role(path)
        file_roles[path] = role
        text = read_text(path)

        headings_report.extend(f"{path.name}: {gap}" for gap in heading_gaps(extract_headings(text)))
        duplicates, skips = sequence_gaps(definition_ids_for_role(text, role))
        index_duplicates.extend(f"{path.name}: {item}" for item in duplicates)
        index_skips.extend(f"{path.name}: {item}" for item in skips)

        for _, line in iter_non_fenced_lines(text):
            ids = [token for token in extract_ids_from_line(line) if token_allowed(token, scheme)]
            if not ids:
                continue
            add_trace_edges(role, ids, feature_definition_row=line.lstrip().startswith("| F"))
            if role == "uat":
                for token in ids:
                    if normalize_kind(token) in {"story", "functional", "nonfunctional", "business"}:
                        references["uat"].add(token)
            if role == "story":
                for token in ids:
                    if normalize_kind(token) in {"business", "functional"}:
                        references["story"].add(token)
            if role == "srs":
                for token in ids:
                    if normalize_kind(token) == "business":
                        references["srs"].add(token)
        for token in [item for item in definition_ids_for_role(text, role) if token_allowed(item.value, scheme)]:
            definitions[normalize_kind(token.value)].add(token.value)

    add_test_alias_edges(graph, set(graph.keys()) | {token for values in definitions.values() for token in values})
    for left, rights in graph.items():
        for right in rights:
            reverse_graph[right].add(left)

    business_ids = sorted(definitions["business"])
    story_ids = definitions["story"]
    test_ids = definitions["test"]
    feature_ids = definitions["feature"]
    functional_ids = definitions["functional"]
    nonfunctional_ids = definitions["nonfunctional"]

    chains: List[dict] = []
    critical_count = 0

    for business_id in business_ids:
        component = bfs(graph, business_id)
        frs = sorted(item for item in component if item in functional_ids)
        nfrs = sorted(item for item in component if item in nonfunctional_ids)
        stories = sorted(item for item in component if item in story_ids)
        tests = sorted(item for item in component if item in test_ids)
        features = sorted(item for item in component if item in feature_ids)

        status = "FULL"
        if not frs and not nfrs:
            status = "ORPHAN_BRQ"
            critical_count += 1
            gaps.append({"type": "ORPHAN_BRQ", "item": business_id, "detail": "No FR/NFR linked"})
        elif frs and not stories:
            status = "MISSING_STORY"
            critical_count += 1
            gaps.append({"type": "MISSING_STORY", "item": business_id, "detail": "FR exists but no story linked"})
        elif (stories or nfrs) and not tests:
            status = "MISSING_TC"
            critical_count += 1
            gaps.append({"type": "MISSING_TC", "item": business_id, "detail": "Story/NFR exists but no test linked"})
        elif (strict or feature_ids) and frs and stories and not features:
            status = "BROKEN_CHAIN"
            critical_count += 1
            gaps.append({"type": "BROKEN_CHAIN", "item": business_id, "detail": "Feature link missing"})

        chains.append(
            {
                "business_id": business_id,
                "functional_ids": frs,
                "nonfunctional_ids": nfrs,
                "feature_ids": features,
                "story_ids": stories,
                "test_ids": tests,
                "status": status,
            }
        )

    for fr_id in sorted(functional_ids):
        reverse = bfs(reverse_graph, fr_id)
        if not any(item in business_ids for item in reverse):
            critical_count += 1
            gaps.append({"type": "ORPHAN_FR", "item": fr_id, "detail": "No business requirement linked"})
        if strict and scheme == "canonical":
            linked_stories = sorted(graph.get(fr_id, set()) & story_ids)
            if not linked_stories:
                critical_count += 1
                gaps.append({"type": "MISSING_US_FOR_FR", "item": fr_id, "detail": "FR has no direct US link"})
            elif len(linked_stories) > 1:
                critical_count += 1
                gaps.append(
                    {
                        "type": "MULTIPLE_US_FOR_FR",
                        "item": fr_id,
                        "detail": "FR links to multiple US: " + ", ".join(linked_stories),
                    }
                )

    if strict and scheme == "canonical":
        for story_id in sorted(story_ids):
            linked_tests = sorted(graph.get(story_id, set()) & test_ids)
            if not linked_tests:
                critical_count += 1
                gaps.append({"type": "MISSING_AC_FOR_US", "item": story_id, "detail": "US has no direct AC/TC link"})
            elif len(linked_tests) > 1:
                critical_count += 1
                gaps.append(
                    {
                        "type": "MULTIPLE_AC_FOR_US",
                        "item": story_id,
                        "detail": "US links to multiple AC/TC: " + ", ".join(linked_tests),
                    }
                )

    for nfr_id in sorted(nonfunctional_ids):
        forward = bfs(graph, nfr_id)
        if not any(item in test_ids for item in forward):
            critical_count += 1
            gaps.append({"type": "ORPHAN_NFR", "item": nfr_id, "detail": "No NFR test linked"})

    if story_ids:
        stale_story_refs = sorted(references["uat"] & {token for token in references["uat"] if normalize_kind(token) == "story"} - story_ids)
        for story_ref in stale_story_refs:
            critical_count += 1
            gaps.append({"type": "STALE_REF", "item": story_ref, "detail": "Referenced in UAT but not defined in story docs"})

    for item in index_duplicates:
        critical_count += 1
        gaps.append({"type": "INDEX_DUPLICATE", "item": item, "detail": "Duplicate ID detected"})
    for item in index_skips:
        critical_count += 1
        gaps.append({"type": "INDEX_SKIP", "item": item, "detail": "Non-contiguous numbering detected"})
    for item in headings_report:
        gaps.append({"type": "HEADING_SKIP", "item": item, "detail": "Heading numbering drift detected"})

    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "target": str(target.resolve()),
        "files_scanned": [str(path.resolve()) for path in files],
        "metrics": {
            "business_total": len(business_ids),
            "functional_total": len(functional_ids),
            "story_total": len(story_ids),
            "test_total": len(test_ids),
            "full_chain_total": sum(1 for chain in chains if chain["status"] == "FULL"),
            "gap_total": len(gaps),
        },
        "chains": chains,
        "gaps": gaps,
    }
    return report, critical_count


def render_markdown(report: dict) -> str:
    lines = []
    lines.append("# TRACEABILITY SCAN REPORT")
    lines.append(f"> Target: `{report['target']}`")
    lines.append(f"> Generated: `{report['generated_at']}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    for key, value in report["metrics"].items():
        lines.append(f"| {key} | {value} |")
    lines.append("")
    lines.append("## Chains")
    lines.append("")
    lines.append("| Business | FR/NFR | Feature | Story | Test | Status |")
    lines.append("|---|---|---|---|---|---|")
    for chain in report["chains"]:
        frs = chain["functional_ids"] + chain["nonfunctional_ids"]
        lines.append(
            f"| {chain['business_id']} | {', '.join(frs) or '---'} | {', '.join(chain['feature_ids']) or '---'} | "
            f"{', '.join(chain['story_ids']) or '---'} | {', '.join(chain['test_ids']) or '---'} | {chain['status']} |"
        )
    lines.append("")
    lines.append("## Gaps")
    lines.append("")
    if not report["gaps"]:
        lines.append("No gaps detected.")
        return "\n".join(lines)
    lines.append("| Type | Item | Detail |")
    lines.append("|---|---|---|")
    for gap in report["gaps"]:
        lines.append(f"| {gap['type']} | {gap['item']} | {gap['detail']} |")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan BA markdown documents for traceability gaps.")
    parser.add_argument("target", nargs="?", default=".", help="Project folder or markdown file")
    parser.add_argument("--output-json", help="Write JSON report to this file")
    parser.add_argument("--output-md", help="Write markdown report to this file")
    parser.add_argument("--scheme", choices=["auto", "legacy", "canonical"], default="auto", help="ID scheme to validate")
    parser.add_argument("--strict", action="store_true", help="Require full feature links where the chain model expects them")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    report, critical_count = build_report(target, scheme=args.scheme, strict=args.strict)
    markdown = render_markdown(report)
    print(markdown)

    if args.output_json:
        Path(args.output_json).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    if args.output_md:
        Path(args.output_md).write_text(markdown, encoding="utf-8")

    return 1 if critical_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
