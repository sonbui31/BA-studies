#!/usr/bin/env python3
import argparse
import json
import re
import sys
from collections import defaultdict, deque
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

from ba_id_utils import (
    MarkdownId,
    classify_file,
    collect_markdown_files,
    definition_blocks,
    definition_ids,
    detect_id_meta,
    duplicate_definitions,
    extract_headings,
    extract_ids,
    extract_ids_from_line,
    find_project_scheme,
    get_project_scheme,
    heading_gaps,
    id_kind,
    is_primary,
    iter_non_fenced_lines,
    load_project_scheme,
    matrix_lines,
    parent_id,
    read_text,
    sequence_gaps,
    set_project_scheme,
)


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def normalize_kind(raw: str) -> str:
    return id_kind(raw)


ROLE_DEFINITION_KINDS = {
    "brd": {"business"},
    "srs": {"functional", "nonfunctional"},
    "story": {"story"},
    "uat": {"test"},
    "feature": {"feature"},
}


CANONICAL_PATTERNS = {
    "business": re.compile(r"^(?:BRQ-\d+(?:\.\d+)?|BR-\d{3}(?:\.\d{1,2})?)$"),
    "functional": re.compile(r"^FR-[A-Z][A-Z0-9]{1,9}-\d{3,4}(?:\.\d{1,2})?$"),
    "nonfunctional": re.compile(r"^NFR-[A-Z][A-Z0-9]{1,9}-\d{3,4}(?:\.\d{1,2})?$"),
    "story": re.compile(r"^US-[A-Z][A-Z0-9]{1,9}-\d{3,4}(?:\.\d{1,2})?$"),
    "test": re.compile(r"^(?:AC|TC)-[A-Z][A-Z0-9]{1,9}-\d{3,4}(?:\.\d{1,2})?$"),
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
    if scheme == "project":
        project = get_project_scheme()
        if project and project.kind_of(token):
            return True
        pattern = CANONICAL_PATTERNS.get(kind)
        return bool(pattern and pattern.match(token))
    patterns = CANONICAL_PATTERNS if scheme == "canonical" else LEGACY_PATTERNS
    pattern = patterns.get(kind)
    return bool(pattern and pattern.match(token))


def build_report(
    target: Path,
    scheme: str = "auto",
    strict: bool = False,
    one_to_one: bool = False,
    config: Optional[Path] = None,
) -> Tuple[dict, int]:
    if not target.exists():
        raise FileNotFoundError(f"Target does not exist: {target}")
    scheme_path = config or find_project_scheme(target)
    set_project_scheme(load_project_scheme(scheme_path) if scheme_path else None)
    if scheme == "project" and not scheme_path:
        raise ValueError("--scheme project needs a ba-scheme.json in the bundle folder or --config PATH")
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
        """Definitions that create an ID: matrix rows only count in the family's own document."""
        return [item.meta for item in definition_ids(text, role) if not item.matrix_row or is_primary(item, role)]

    def minted_ids(text: str, role: str) -> List[MarkdownId]:
        """IDs minted by this document: numbering gaps are judged only here."""
        return [item.meta for item in definition_ids(text, role) if is_primary(item, role)]

    off_scheme: Dict[str, Set[str]] = defaultdict(set)
    unclassified: List[str] = []

    for path in files:
        role = normalize_role(path)
        file_roles[path] = role
        text = read_text(path)

        headings_report.extend(f"{path.name}: {gap}" for gap in heading_gaps(extract_headings(text)))
        duplicates = duplicate_definitions(definition_ids(text, role))
        _, skips = sequence_gaps(minted_ids(text, role))
        index_duplicates.extend(
            f"{path.name}: INDEX_DUPLICATE {value} at lines {', '.join(str(line) for line in lines)}"
            for value, lines in duplicates.items()
        )
        index_skips.extend(f"{path.name}: {item}" for item in skips)

        has_ids = False
        block_owner = definition_blocks(text, role)
        matrix_rows = set(matrix_lines(text))
        for line_no, line in iter_non_fenced_lines(text):
            raw_ids = extract_ids_from_line(line)
            has_ids = has_ids or bool(raw_ids)
            if scheme != "auto":
                for token in raw_ids:
                    if not token_allowed(token, scheme):
                        off_scheme[token].add(path.name)
            ids = [token for token in raw_ids if token_allowed(token, scheme)]
            if not ids:
                continue
            add_trace_edges(role, ids, feature_definition_row=line.lstrip().startswith("| F"))
            if line_no in matrix_rows:
                # A matrix row states the chain explicitly, whatever document it sits in.
                add_trace_edges("other", ids)
                # Column order is chain order: "BR | SR | FR" links business level to business level.
                business_columns = [
                    [token for token in extract_ids_from_line(cell) if token in ids and normalize_kind(token) == "business"]
                    for cell in line.strip().strip("|").split("|")
                ]
                business_columns = [column for column in business_columns if column]
                for index, left_column in enumerate(business_columns):
                    for right_column in business_columns[index + 1:]:
                        add_edges(left_column, right_column)
            owner = block_owner.get(line_no)
            if owner and owner not in ids and token_allowed(owner, scheme):
                # Links written under a definition belong to it (see definition_blocks).
                add_trace_edges(role, [owner] + ids)
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
        project = get_project_scheme()
        if role == "other" and has_ids and not (project and project.role_of(path)):
            unclassified.append(path.name)

    add_test_alias_edges(graph, set(graph.keys()) | {token for values in definitions.values() for token in values})

    # Sub-requirements (FR-TEA-003.1) belong to their parent. A child reaches what its parent
    # reaches, and a parent counts as defined when only its children are written out.
    known_tokens = set(graph.keys()) | set(reverse_graph.keys()) | {t for values in definitions.values() for t in values}
    for values in list(references.values()):
        known_tokens |= values
    parent_of: Dict[str, str] = {}
    for token in sorted(known_tokens):
        parent = parent_id(token)
        if not parent:
            continue
        parent_of[token] = parent
        graph[parent].add(token)
        if normalize_kind(token) != "business":
            graph[token].add(parent)
    for kind in list(definitions.keys()):
        for token in list(definitions[kind]):
            parent = parent_of.get(token)
            if parent and kind != "business":
                definitions[kind].add(parent)

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
            status = "ORPHAN_BR" if business_id.startswith("BR-") else "ORPHAN_BRQ"
            critical_count += 1
            detail = "Business rule not enforced by any FR/NFR" if status == "ORPHAN_BR" else "No FR/NFR linked"
            undefined = sorted(
                item
                for item in graph.get(business_id, set())
                if normalize_kind(item) in {"functional", "nonfunctional"}
                and item not in functional_ids
                and item not in nonfunctional_ids
            )
            if undefined:
                detail += "; links only to FR/NFR not defined in the SRS: " + ", ".join(undefined)
            gaps.append({"type": status, "item": business_id, "detail": detail})
        elif frs and not stories:
            status = "MISSING_STORY"
            critical_count += 1
            gaps.append({"type": "MISSING_STORY", "item": business_id, "detail": "FR exists but no story linked"})
        elif (stories or nfrs) and not tests:
            status = "MISSING_TC"
            critical_count += 1
            gaps.append({"type": "MISSING_TC", "item": business_id, "detail": "Story/NFR exists but no test linked"})
        elif feature_ids and frs and stories and not features:
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

    direct_mode = strict and scheme in ("canonical", "project")
    for fr_id in sorted(functional_ids):
        reverse = bfs(reverse_graph, fr_id)
        if not any(item in business_ids for item in reverse):
            critical_count += 1
            gaps.append({"type": "ORPHAN_FR", "item": fr_id, "detail": "No business requirement linked"})
        if direct_mode:
            linked_stories = sorted((graph.get(fr_id, set()) | graph.get(parent_of.get(fr_id, ""), set())) & story_ids)
            if not linked_stories:
                critical_count += 1
                gaps.append({"type": "MISSING_US_FOR_FR", "item": fr_id, "detail": "FR has no direct US link"})
            elif one_to_one and len(linked_stories) > 1:
                critical_count += 1
                gaps.append(
                    {
                        "type": "MULTIPLE_US_FOR_FR",
                        "item": fr_id,
                        "detail": "FR links to multiple US: " + ", ".join(linked_stories),
                    }
                )
        elif story_ids and not (bfs(graph, fr_id) & story_ids):
            critical_count += 1
            gaps.append({"type": "MISSING_US_FOR_FR", "item": fr_id, "detail": "FR does not reach any US"})

    for story_id in sorted(story_ids):
        if direct_mode:
            linked_tests = sorted((graph.get(story_id, set()) | graph.get(parent_of.get(story_id, ""), set())) & test_ids)
            if not linked_tests:
                critical_count += 1
                gaps.append({"type": "MISSING_AC_FOR_US", "item": story_id, "detail": "US has no direct AC/TC link"})
            elif one_to_one and len(linked_tests) > 1:
                critical_count += 1
                gaps.append(
                    {
                        "type": "MULTIPLE_AC_FOR_US",
                        "item": story_id,
                        "detail": "US links to multiple AC/TC: " + ", ".join(linked_tests),
                    }
                )
        elif test_ids and not (bfs(graph, story_id) & test_ids):
            critical_count += 1
            gaps.append({"type": "MISSING_AC_FOR_US", "item": story_id, "detail": "US does not reach any AC/TC"})

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

    if functional_ids:
        for ref in sorted(token for token in references["story"] if normalize_kind(token) == "functional"):
            if ref not in functional_ids:
                critical_count += 1
                gaps.append({"type": "STALE_REF", "item": ref, "detail": "Referenced in story docs but not defined in SRS"})
    if business_ids:
        for ref in sorted(references["srs"] - set(business_ids)):
            critical_count += 1
            gaps.append({"type": "STALE_REF", "item": ref, "detail": "Referenced in SRS but not defined in BRD"})

    if not files:
        critical_count += 1
        gaps.append({"type": "NO_FILES", "item": str(target), "detail": "No markdown files found"})
    elif not business_ids and not functional_ids:
        critical_count += 1
        gaps.append(
            {
                "type": "NO_DEFINITIONS",
                "item": str(target),
                "detail": "No BRQ/BR or FR/NFR definitions found; check file names (BRD/SRS/Story/UAT) and ID scheme",
            }
        )
    for token in sorted(off_scheme):
        if strict:
            critical_count += 1
        gaps.append(
            {
                "type": "OFF_SCHEME_ID",
                "item": token,
                "detail": f"Not a valid {scheme} ID (ignored for linking) in: " + ", ".join(sorted(off_scheme[token])),
            }
        )
    for name in unclassified:
        gaps.append(
            {
                "type": "UNCLASSIFIED_FILE",
                "item": name,
                "detail": "File name does not say BRD/SRS/Story/UAT/Feature; its IDs are treated as references only",
            }
        )

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
        "project_scheme": str(scheme_path.resolve()) if scheme_path else None,
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
    if report.get("project_scheme"):
        lines.append(f"> Project scheme: `{report['project_scheme']}`")
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
    parser.add_argument(
        "--scheme",
        choices=["auto", "legacy", "canonical", "project"],
        default="auto",
        help="ID scheme to validate; 'project' = canonical plus the formats declared in ba-scheme.json",
    )
    parser.add_argument("--config", help="Path to ba-scheme.json (default: looked up in the bundle folder)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Canonical/project: require direct FR->US and US->AC/TC links; any off-scheme ID is critical",
    )
    parser.add_argument(
        "--one-to-one",
        action="store_true",
        help="With --strict --scheme canonical, also reject an FR mapped to several US or a US mapped to several AC/TC",
    )
    args = parser.parse_args()

    target = Path(args.target).resolve()
    try:
        report, critical_count = build_report(
            target,
            scheme=args.scheme,
            strict=args.strict,
            one_to_one=args.one_to_one,
            config=Path(args.config).resolve() if args.config else None,
        )
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    markdown = render_markdown(report)
    print(markdown)

    if args.output_json:
        Path(args.output_json).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    if args.output_md:
        Path(args.output_md).write_text(markdown, encoding="utf-8")

    return 1 if critical_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
