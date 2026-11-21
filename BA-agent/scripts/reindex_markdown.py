#!/usr/bin/env python3
"""Renumber markdown section headings and BA IDs so sequences are contiguous.

Safety rules:
- Dry run by default. ``--apply`` writes files, keeping each file's line endings.
- Only groups that actually have gaps are renumbered; a clean US-001..US-012 is left alone.
  Relative order is kept (sorted by current number) and the first number of a group is kept.
- An ID group defined in a signed/baseline document is frozen: none of its IDs are renamed in
  any file, because the signed document itself will not be edited.
- Sub-requirements follow their parent: BRQ-03 -> BRQ-02 also renames BRQ-03.1 -> BRQ-02.1.
- Duplicate definitions cannot be resolved automatically; they are reported for a manual fix.
- Headings: only "1.", "1.2", "1.2." numbering is touched, and only the last component.

Exit codes: 0 = nothing to do (or changes applied cleanly); 1 = dry run found renumbering to do,
or duplicates need a manual fix; 2 = bad target.
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from ba_id_utils import (
    HEADING_PATTERN,
    HUNDRED_BUCKET_FAMILIES,
    MarkdownHeading,
    classify_file,
    definition_ids,
    duplicate_definitions,
    collect_markdown_files,
    detect_id_meta,
    expected_heading_numbers,
    extract_ids_from_line,
    find_project_scheme,
    get_project_scheme,
    iter_fence_state,
    is_primary,
    iter_non_fenced_lines,
    load_project_scheme,
    parent_id,
    read_text,
    replace_exact_tokens,
    set_project_scheme,
    write_text,
)


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# Signed status is read from the document header only, so a KPI table with a "Baseline" column
# deep in the body does not freeze the document.
HEADER_LINES = 40
SIGNED_PATTERNS = (
    re.compile(r"đã phê duyệt", re.IGNORECASE),
    re.compile(r"chốt phạm vi", re.IGNORECASE),
    re.compile(r"nghiệm thu đạt", re.IGNORECASE),
    re.compile(r"(trạng thái|status)\W*\s*(baseline|approved|signed|đã ký)", re.IGNORECASE),
)


def is_signed_baseline(text: str) -> bool:
    for line_no, line in iter_non_fenced_lines(text):
        if line_no > HEADER_LINES:
            break
        if any(pattern.search(line) for pattern in SIGNED_PATTERNS):
            return True
    return False


def build_heading_replacements(text: str) -> Tuple[str, List[str]]:
    headings: List[MarkdownHeading] = []
    for line_no, line, fenced in iter_fence_state(text, keepends=True):
        if fenced:
            continue
        body = line.rstrip("\r\n")
        match = HEADING_PATTERN.match(body)
        if match:
            headings.append(
                MarkdownHeading(
                    level=len(match.group("hashes")),
                    number=match.group("num"),
                    text=match.group("title"),
                    line_no=line_no,
                    trailing_dot=bool(match.group("dot")),
                )
            )
    planned: Dict[int, str] = {}
    for heading, expected in expected_heading_numbers(headings):
        expected_text = ".".join(str(part) for part in expected)
        if expected_text != heading.number:
            planned[heading.line_no] = expected_text

    updates: List[str] = []
    output: List[str] = []
    for line_no, line, fenced in iter_fence_state(text, keepends=True):
        if fenced or line_no not in planned:
            output.append(line)
            continue
        body = line.rstrip("\r\n")
        ending = line[len(body):]
        match = HEADING_PATTERN.match(body)
        dot = "." if match.group("dot") else ""
        rebuilt = f"{match.group('hashes')} {planned[line_no]}{dot} {match.group('title')}"
        updates.append(f"line {line_no}: {body.strip()} -> {rebuilt}")
        output.append(rebuilt + ending)
    return "".join(output), updates


def file_role(path: Path) -> str:
    return classify_file(path)


def definition_ids_for_role(text: str, role: str) -> List[str]:
    """Unique IDs minted (not merely referenced or restated) in a document of this role."""
    ids: List[str] = []
    for item in definition_ids(text, role):
        if not is_primary(item, role):
            continue
        if item.meta.value not in ids:
            ids.append(item.meta.value)
    return ids


def _format_like(old: str, family: str, group: str, sequence: int) -> str:
    project = get_project_scheme()
    rest = old[len(group):] if old.startswith(group) else ""
    if project and project.kind_of(old) and rest.isdigit():
        # Project-declared IDs ("SR-07", "BRULE-012"): keep the prefix and the digit width.
        return f"{group}{sequence:0{len(rest)}d}"
    if family == "BRQ":
        return f"BRQ-{sequence:02d}"
    if group.startswith(f"{family}-") and not group[len(family) + 1:].isdigit():
        width = len(old.rsplit("-", 1)[1])
        return f"{group}-{sequence:0{width}d}"
    width = max(3, len(old.rsplit("-", 1)[1]))
    return f"{family}-{sequence:0{width}d}"


def plan_renumbering(files: List[Path], include_baseline: bool = False) -> dict:
    """Return {'replacements', 'duplicates', 'frozen'} for the whole bundle."""
    grouped: Dict[Tuple[str, str], List[Tuple[int, str]]] = defaultdict(list)
    definers: Dict[str, Set[Path]] = defaultdict(set)
    signed_files: Set[Path] = set()
    sub_ids: Set[str] = set()

    for path in files:
        text = read_text(path)
        if not include_baseline and is_signed_baseline(text):
            signed_files.add(path)
        for _, line in iter_non_fenced_lines(text):
            for token in extract_ids_from_line(line):
                if parent_id(token):
                    sub_ids.add(token)
        for value in definition_ids_for_role(text, file_role(path)):
            meta = detect_id_meta(value, 0)
            if not meta or parent_id(value):
                continue
            definers[value].add(path)
            key = (meta.family, meta.group)
            if all(existing != value for _, existing in grouped[key]):
                grouped[key].append((meta.sequence, value))

    duplicate_values: Set[str] = {value for value, paths in definers.items() if len(paths) > 1}
    duplicates = sorted(
        f"{value} được định nghĩa ở nhiều file: {', '.join(sorted(p.name for p in paths))}"
        for value, paths in definers.items()
        if len(paths) > 1
    )
    # Duplicates inside one file.
    for path in files:
        role = file_role(path)
        minted = [item for item in definition_ids(read_text(path), role) if is_primary(item, role)]
        for value, lines in duplicate_definitions(minted).items():
            duplicate_values.add(value)
            duplicates.append(f"{path.name}: {value} định nghĩa lặp ở dòng {', '.join(str(line) for line in lines)}")

    replacements: Dict[str, str] = {}
    frozen: List[str] = []
    for (family, group), entries in grouped.items():
        entries.sort()
        sequences = [sequence for sequence, _ in entries]
        start = sequences[0]
        target = list(range(start, start + len(sequences)))
        if sequences == target:
            continue
        if any(value in duplicate_values for _, value in entries):
            frozen.append(f"{group}: có ID trùng, không tự đánh lại số; sửa ID trùng trước")
            continue
        project = get_project_scheme()
        if project and any(project.kind_of(value) and not value[len(group):].isdigit() for _, value in entries):
            frozen.append(f"{group}: định dạng ID riêng của dự án không có số cuối để đánh lại; không đổi")
            continue
        locked_by = sorted({p.name for _, value in entries for p in definers[value] if p in signed_files})
        if locked_by:
            frozen.append(f"{group}: có lỗ hổng {sequences} nhưng được định nghĩa trong tài liệu đã ký ({', '.join(locked_by)}); không đổi")
            continue
        for (old_seq, old), new_seq in zip(entries, target):
            if old_seq == new_seq:
                continue
            new = _format_like(old, family, group, new_seq)
            replacements[old] = new
            for sub in sub_ids:
                if parent_id(sub) == old:
                    replacements[sub] = f"{new}.{sub.rsplit('.', 1)[1]}"
    return {"replacements": replacements, "duplicates": duplicates, "frozen": frozen, "signed": signed_files}


def build_id_replacements(files: List[Path], include_baseline: bool = False) -> Dict[str, str]:
    return plan_renumbering(files, include_baseline)["replacements"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Renumber markdown headings and BA IDs (dry run by default).")
    parser.add_argument("target", nargs="?", default=".", help="File or folder to process")
    parser.add_argument("--apply", action="store_true", help="Write changes back to disk")
    parser.add_argument("--headings-only", action="store_true", help="Only renumber markdown headings")
    parser.add_argument("--include-baseline", action="store_true", help="Allow edits on signed/baseline documents")
    parser.add_argument("--config", help="Path to ba-scheme.json (default: looked up in the target folder)")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    try:
        files = collect_markdown_files(target)
        scheme_path = Path(args.config).resolve() if args.config else find_project_scheme(target)
        set_project_scheme(load_project_scheme(scheme_path) if scheme_path else None)
    except (FileNotFoundError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 2
    plan = {"replacements": {}, "duplicates": [], "frozen": [], "signed": set()}
    if not args.headings_only:
        plan = plan_renumbering(files, args.include_baseline)
    replacements: Dict[str, str] = plan["replacements"]

    changed_files = 0
    for path in files:
        original = read_text(path)
        print(f"\n[{file_role(path)}] {path}")
        if path in plan["signed"] or (not args.include_baseline and is_signed_baseline(original)):
            print("- Bỏ qua tài liệu đã ký/baseline. Chạy lại với --include-baseline nếu thật sự cần sửa.")
            continue
        rewritten, heading_updates = build_heading_replacements(original)
        rewritten = replace_exact_tokens(rewritten, replacements)
        touched = sorted({f"{old} -> {new}" for old, new in replacements.items() if re.search(rf"(?<![\w.-]){re.escape(old)}(?![\w-]|\.\d)", original)})
        if heading_updates:
            print("Heading updates:")
            for item in heading_updates[:20]:
                print(f"- {item}")
            if len(heading_updates) > 20:
                print(f"- ... {len(heading_updates) - 20} more")
        if touched:
            print("ID updates:")
            for item in touched[:20]:
                print(f"- {item}")
            if len(touched) > 20:
                print(f"- ... {len(touched) - 20} more")
        if rewritten == original:
            print("- Không cần đánh lại số")
            continue
        changed_files += 1
        if args.apply:
            write_text(path, rewritten)

    for item in plan["frozen"]:
        print(f"\nFROZEN: {item}")
    for item in plan["duplicates"]:
        print(f"\nDUPLICATE (sửa tay): {item}")

    print(f"\nProcessed {len(files)} markdown file(s); {'changed' if args.apply else 'would change'} {changed_files}.")
    if not args.apply and changed_files:
        print("Dry run only. Re-run with --apply to write changes.")
    if plan["duplicates"]:
        return 1
    if changed_files and not args.apply:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
