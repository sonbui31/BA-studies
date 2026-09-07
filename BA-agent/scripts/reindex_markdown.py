#!/usr/bin/env python3
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

from ba_id_utils import (
    HEADING_PATTERN,
    classify_file,
    collect_markdown_files,
    detect_id_meta,
    extract_ids_from_line,
    iter_non_fenced_lines,
    replace_exact_tokens,
    read_text,
)


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


SIGNED_MARKERS = (
    "Đã phê duyệt",
    "CHỐT PHẠM VI",
    "Baseline",
    "Nghiệm thu đạt",
)


def is_signed_baseline(text: str) -> bool:
    return any(marker.lower() in text.lower() for marker in SIGNED_MARKERS)


def build_heading_replacements(text: str) -> Tuple[str, List[str]]:
    counters: Dict[int, int] = {}
    updates: List[str] = []
    new_lines: List[str] = []
    in_fence = False

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            new_lines.append(line)
            continue
        if in_fence:
            new_lines.append(line)
            continue

        match = HEADING_PATTERN.match(line)
        if not match:
            new_lines.append(line)
            continue

        level = len(match.group(1))
        counters[level] = counters.get(level, 0) + 1
        for deeper in list(counters):
            if deeper > level:
                counters.pop(deeper, None)
        number = ".".join(str(counters[current]) for current in sorted(counters) if current <= level)
        rebuilt = f"{match.group(1)} {number}. {match.group(4)}"
        if rebuilt != line:
            updates.append(f"line {line_no}: {line.strip()} -> {rebuilt}")
        new_lines.append(rebuilt)

    return "\n".join(new_lines) + ("\n" if text.endswith("\n") else ""), updates


def definition_ids_for_role(text: str, role: str) -> List[str]:
    ids: List[str] = []

    def first_cell(line: str) -> str:
        return line.strip().strip("|").split("|")[0].strip()

    def add_tokens(value: str) -> None:
        for token in extract_ids_from_line(value):
            meta = detect_id_meta(token, 0)
            if not meta:
                continue
            if role == "brd" and meta.family not in {"BRQ", "BRD", "BR"}:
                continue
            if role == "srs" and meta.family not in {"FR", "NFR"}:
                continue
            if role == "story" and meta.family != "US":
                continue
            if role == "uat" and meta.family not in {"AC", "TC", "UAT"}:
                continue
            if role == "feature" and meta.family != "F":
                continue
            if token not in ids:
                ids.append(token)

    for _, line in iter_non_fenced_lines(text):
        stripped = line.lstrip()
        if role == "brd":
            if stripped.startswith("| BRQ-") or stripped.startswith("| BRD-") or stripped.startswith("| BR-"):
                add_tokens(first_cell(stripped))
            elif stripped.startswith("- BRQ-") or stripped.startswith("- BR-"):
                add_tokens(stripped)
        elif role == "srs":
            if stripped.startswith("| FR-") or stripped.startswith("| NFR-"):
                cells = [cell.strip() for cell in stripped.strip().strip("|").split("|")]
                if cells and cells[0].startswith("NFR-") and len(cells) < 5:
                    continue
                add_tokens(cells[0] if cells else "")
        elif role == "story":
            if stripped.startswith("| US-") or stripped.startswith("| US"):
                add_tokens(first_cell(stripped))
        elif role == "uat":
            if stripped.startswith("| AC-") or stripped.startswith("| UAT-") or stripped.startswith("| TC-"):
                add_tokens(first_cell(stripped))
        elif role == "feature":
            if stripped.startswith("| F"):
                add_tokens(first_cell(stripped))

    return ids


def build_id_replacements(files: List[Path]) -> Dict[str, str]:
    grouped: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    token_order: List[str] = []

    for path in files:
        text = read_text(path)
        role = "uat" if "beta" in path.name.lower() else classify_file(path)
        for value in definition_ids_for_role(text, role):
            item = detect_id_meta(value, 0)
            if not item:
                continue
            if "." in item.value and item.family == "BRQ":
                continue
            key = (item.family, item.group)
            if item.value not in grouped[key]:
                grouped[key].append(item.value)
                token_order.append(item.value)

    replacements: Dict[str, str] = {}
    for (_, group), values in grouped.items():
        for index, old in enumerate(values, start=1):
            meta = detect_id_meta(old, 0)
            if not meta:
                continue
            if meta.family == "BRQ":
                new = f"BRQ-{index:02d}"
            elif meta.family in {"BRD", "BR", "FR", "NFR", "US", "AC", "TC", "UAT"}:
                if "-" in group and group != meta.family:
                    prefix, bucket = group.rsplit("-", 1)
                    if not bucket.isdigit():
                        new = old
                        if new != old:
                            replacements[old] = new
                        continue
                    bucket_value = int(bucket)
                    if meta.family in {"BRD", "BR", "FR", "NFR"}:
                        sequence = bucket_value * 100 + index
                    else:
                        sequence = bucket_value * 10 + index
                    new = f"{prefix}-{sequence:03d}"
                else:
                    if meta.family in {"BRD", "BR", "FR", "NFR", "US", "AC", "TC", "UAT"}:
                        new = f"{meta.family}-{index:03d}"
                    else:
                        new = old
            else:
                new = old
            if new != old:
                replacements[old] = new
    return replacements


def main() -> int:
    parser = argparse.ArgumentParser(description="Renumber markdown headings and BA IDs.")
    parser.add_argument("target", nargs="?", default=".", help="File or folder to process")
    parser.add_argument("--apply", action="store_true", help="Write changes back to disk")
    parser.add_argument("--headings-only", action="store_true", help="Only renumber markdown headings")
    parser.add_argument("--include-baseline", action="store_true", help="Allow edits on signed/baseline documents")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    files = collect_markdown_files(target)
    replacements = {} if args.headings_only else build_id_replacements(files)

    total_updates = 0
    for path in files:
        original = read_text(path)
        if not args.include_baseline and is_signed_baseline(original):
            print(f"\n[{classify_file(path)}] {path}")
            print("- Skipped signed/baseline document. Re-run with --include-baseline to allow edits.")
            continue
        rewritten, heading_updates = build_heading_replacements(original)
        rewritten = replace_exact_tokens(rewritten, replacements)
        changed = rewritten != original
        if changed:
            total_updates += 1
        print(f"\n[{classify_file(path)}] {path}")
        if heading_updates:
            print("Heading updates:")
            for item in heading_updates[:20]:
                print(f"- {item}")
            if len(heading_updates) > 20:
                print(f"- ... {len(heading_updates) - 20} more")
        touched = [f"{old} -> {new}" for old, new in replacements.items() if old in original]
        if touched:
            print("ID updates:")
            for item in touched[:20]:
                print(f"- {item}")
            if len(touched) > 20:
                print(f"- ... {len(touched) - 20} more")
        if not heading_updates and not touched:
            print("- No renumbering needed")
        if args.apply and changed:
            path.write_text(rewritten, encoding="utf-8")

    print(f"\nProcessed {len(files)} markdown file(s); changed {total_updates}.")
    if not args.apply:
        print("Dry run only. Re-run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
