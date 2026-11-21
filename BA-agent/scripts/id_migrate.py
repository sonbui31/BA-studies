#!/usr/bin/env python3
"""Migrate a bundle's own ID formats to canonical IDs, with an alias table.

Rules live in the bundle's ba-scheme.json under "migrate": each key is a regex that must match a
whole ID, each value the replacement (re.sub syntax, e.g. "US-QLTS-0\\1"):

    "migrate": {
        "US(\\d{2})": "US-QLTS-0\\1",
        "TC-(\\d{2})-([A-Z])": "TC-QLTS-\\1\\2"
    }

Dry run by default: prints the mapping and the conflicts. --apply rewrites the Markdown files
(signed/baseline documents are skipped unless --include-baseline) and writes ID-MIGRATION.md,
the old -> new alias table people need to follow old references in email, Jira or Word copies.
Sub-IDs follow their parent (US20.1 -> US-QLTS-020.1) unless a rule maps them directly.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

from ba_id_utils import (
    collect_markdown_files,
    extract_ids_from_line,
    find_project_scheme,
    id_kind,
    iter_non_fenced_lines,
    load_project_scheme,
    parent_id,
    read_text,
    replace_exact_tokens,
    set_project_scheme,
    write_text,
)
from reindex_markdown import is_signed_baseline
from traceability_scan import CANONICAL_PATTERNS

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ALIAS_FILE = "ID-MIGRATION.md"


def load_rules(scheme_path: Path) -> List[Tuple["re.Pattern[str]", str]]:
    data = json.loads(scheme_path.read_text(encoding="utf-8"))
    rules = data.get("migrate") or {}
    if not rules:
        raise ValueError(f"{scheme_path}: no \"migrate\" rules")
    return [(re.compile(pattern), template) for pattern, template in rules.items()]


def collect_tokens(files: List[Path]) -> Dict[str, Dict[str, int]]:
    """token -> {file name: occurrences}."""
    usage: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for path in files:
        for _, line in iter_non_fenced_lines(read_text(path)):
            for token in extract_ids_from_line(line):
                usage[token][path.name] += 1
    return usage


def plan_migration(tokens: Set[str], rules: List[Tuple["re.Pattern[str]", str]]) -> dict:
    """Return {'mapping', 'conflicts', 'warnings'}."""
    mapping: Dict[str, str] = {}
    for token in sorted(tokens):
        for pattern, template in rules:
            if pattern.fullmatch(token):
                mapping[token] = pattern.sub(template, token)
                break
    for token in sorted(tokens):
        if token in mapping:
            continue
        parent = parent_id(token)
        if parent and parent in mapping:
            mapping[token] = f"{mapping[parent]}.{token.rsplit('.', 1)[1]}"

    conflicts: List[str] = []
    warnings: List[str] = []
    targets: Dict[str, List[str]] = defaultdict(list)
    for old, new in mapping.items():
        targets[new].append(old)
    for new, olds in sorted(targets.items()):
        if len(olds) > 1:
            conflicts.append(f"{', '.join(sorted(olds))} cùng đổi thành {new}")
        if new in tokens and new not in mapping:
            conflicts.append(f"{new} đã có trong bộ tài liệu với nghĩa khác; không thể đổi {', '.join(olds)} thành {new}")
    for old, new in sorted(mapping.items()):
        kind = id_kind(old)
        if extract_ids_from_line(new) != [new] or id_kind(new) != kind:
            # The scripts could no longer see this ID: traceability would silently lose it.
            conflicts.append(f"{old} -> {new}: script không nhận ra {new} là ID loại {kind}")
            continue
        pattern = CANONICAL_PATTERNS.get(kind)
        if pattern and not pattern.match(new):
            warnings.append(f"{old} -> {new}: chưa đúng định dạng canonical của loại {kind}")
    return {"mapping": mapping, "conflicts": conflicts, "warnings": warnings}


def render_alias_table(mapping: Dict[str, str], usage: Dict[str, Dict[str, int]], scheme_path: Path) -> str:
    lines = [
        "# Bảng đổi ID (ID-MIGRATION)",
        "",
        f"> Sinh bởi `id_migrate.py` theo quy tắc trong `{scheme_path.name}`. Giữ file này cùng bộ tài liệu:",
        "> email, ticket, bản Word cũ vẫn dùng ID cũ, cần tra ngược ở đây.",
        "",
        "| ID cũ | ID mới | Số lần xuất hiện | File |",
        "|---|---|---|---|",
    ]
    for old, new in sorted(mapping.items(), key=lambda item: item[1]):
        files = usage.get(old, {})
        lines.append(f"| {old} | {new} | {sum(files.values())} | {', '.join(sorted(files))} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate project-specific BA IDs to canonical IDs (dry run by default).")
    parser.add_argument("target", help="Bundle folder")
    parser.add_argument("--config", help="ba-scheme.json with \"migrate\" rules (default: looked up in the folder)")
    parser.add_argument("--apply", action="store_true", help="Rewrite the files and write ID-MIGRATION.md")
    parser.add_argument("--include-baseline", action="store_true", help="Also rewrite signed/baseline documents")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    try:
        if not target.is_dir():
            raise FileNotFoundError(f"Not a folder: {target}")
        scheme_path = Path(args.config).resolve() if args.config else find_project_scheme(target)
        if not scheme_path:
            raise FileNotFoundError(f"No ba-scheme.json in {target}; pass --config")
        set_project_scheme(load_project_scheme(scheme_path))
        rules = load_rules(scheme_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 2

    files = [path for path in collect_markdown_files(target) if path.name != ALIAS_FILE]
    usage = collect_tokens(files)
    plan = plan_migration(set(usage), rules)
    mapping: Dict[str, str] = plan["mapping"]

    print(f"Quy tắc: {scheme_path}")
    print(f"{len(mapping)} ID sẽ đổi trong {len(files)} file.")
    for old, new in sorted(mapping.items(), key=lambda item: item[1])[:40]:
        print(f"- {old} -> {new}")
    if len(mapping) > 40:
        print(f"- ... {len(mapping) - 40} ID khác (xem {ALIAS_FILE} sau khi --apply)")
    for item in plan["warnings"]:
        print(f"CẢNH BÁO: {item}")
    for item in plan["conflicts"]:
        print(f"XUNG ĐỘT: {item}")
    if plan["conflicts"]:
        print("Không đổi gì. Sửa quy tắc migrate cho hết xung đột rồi chạy lại.")
        return 1
    if not mapping:
        print("Không có ID nào khớp quy tắc.")
        return 0
    if not args.apply:
        print("Dry run. Chạy lại với --apply để ghi.")
        return 1

    skipped = []
    for path in files:
        original = read_text(path)
        if not args.include_baseline and is_signed_baseline(original):
            skipped.append(path.name)
            continue
        rewritten = replace_exact_tokens(original, mapping)
        if rewritten != original:
            write_text(path, rewritten)
    (target / ALIAS_FILE).write_text(render_alias_table(mapping, usage, scheme_path), encoding="utf-8")
    for name in skipped:
        print(f"Bỏ qua tài liệu đã ký/baseline: {name} (ID cũ vẫn còn trong file này; tra {ALIAS_FILE})")
    print(f"Đã ghi. Bảng đổi ID: {target / ALIAS_FILE}")
    print("Cập nhật ba-scheme.json: bỏ các định dạng cũ khỏi \"ids\" khi không còn tài liệu nào dùng.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
