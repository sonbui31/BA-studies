#!/usr/bin/env python3
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Tuple


ID_PATTERNS = {
    "business": re.compile(r"\b(?:BRQ-\d+(?:\.\d+)?|BRD-\d{3}|BR-\d{3})\b"),
    "functional": re.compile(r"\bFR(?:-[A-Z]{2,10})?-\d{1,3}\b"),
    "nonfunctional": re.compile(r"\bNFR(?:-[A-Z]{2,10})?-\d{1,3}\b"),
    "story": re.compile(r"\b(?:US(?:-[A-Z]{2,10})?-\d{3}|US\d{2,3})\b"),
    "test": re.compile(r"\b(?:TC(?:-[A-Z]{2,10})?-\d{3}|TC-\d{2}-[A-Z]|UAT(?:-[A-Z]+)?-\d{2,3})\b"),
    "feature": re.compile(r"\b(?:F\d{2}|F-\d{3})\b"),
}

HEADING_PATTERN = re.compile(r"^(#{1,6})\s+((\d+(?:\.\d+)*)\.?\s+)(.+?)\s*$")
TOP_LEVEL_BRQ_PATTERN = re.compile(r"^BRQ-(\d+)$")
SUB_BRQ_PATTERN = re.compile(r"^BRQ-(\d+)\.(\d+)$")
MODULED_PATTERN = re.compile(r"^(FR|NFR|US|TC)-([A-Z]{2,10})-(\d{3})$")
SIMPLE_HUNDREDS_PATTERN = re.compile(r"^(BRD|BR|FR|NFR|US|TC|UAT)-(\d{3})$")
LEGACY_US_PATTERN = re.compile(r"^US(\d{2,3})$")
LEGACY_TC_ALPHA_PATTERN = re.compile(r"^TC-(\d{2})-([A-Z])$")
UAT_MODULED_PATTERN = re.compile(r"^UAT-([A-Z]{2,10})-(\d{2,3})$")
FEATURE_PATTERN = re.compile(r"^F(\d{2})$")
LEGACY_FEATURE_PATTERN = re.compile(r"^F-(\d{3})$")


@dataclass(frozen=True)
class MarkdownHeading:
    level: int
    text: str
    number: str
    line_no: int


@dataclass(frozen=True)
class MarkdownId:
    value: str
    family: str
    group: str
    sequence: int
    line_no: int


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def collect_markdown_files(target: Path) -> List[Path]:
    if not target.exists():
        raise FileNotFoundError(f"Target does not exist: {target}")
    if target.is_file():
        return [target]
    return sorted(path for path in target.rglob("*.md") if path.is_file())


def classify_file(path: Path) -> str:
    name = path.name.lower()
    if "brd" in name:
        return "brd"
    if "srs" in name:
        return "srs"
    if "uat" in name:
        return "uat"
    if "story" in name:
        return "story"
    if "feature" in name:
        return "feature"
    return "other"


def extract_ids_from_line(line: str) -> List[str]:
    found: List[str] = []
    for pattern in ID_PATTERNS.values():
        found.extend(pattern.findall(line))
    return sorted(set(found), key=found.index)


def iter_non_fenced_lines(text: str) -> Iterator[Tuple[int, str]]:
    in_fence = False
    for index, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield index, line


def detect_id_meta(value: str, line_no: int) -> Optional[MarkdownId]:
    if match := TOP_LEVEL_BRQ_PATTERN.match(value):
        return MarkdownId(value=value, family="BRQ", group="BRQ", sequence=int(match.group(1)), line_no=line_no)
    if match := SUB_BRQ_PATTERN.match(value):
        return MarkdownId(value=value, family="BRQ", group=f"BRQ-{int(match.group(1)):02d}", sequence=int(match.group(2)), line_no=line_no)
    if match := MODULED_PATTERN.match(value):
        family, module, seq = match.groups()
        return MarkdownId(value=value, family=family, group=f"{family}-{module}", sequence=int(seq), line_no=line_no)
    if match := SIMPLE_HUNDREDS_PATTERN.match(value):
        family, seq = match.groups()
        numeric = int(seq)
        if family in {"BRD", "BR", "FR", "NFR"}:
            group = f"{family}-{numeric // 100}"
        else:
            group = f"{family}-{numeric // 10}"
        return MarkdownId(value=value, family=family, group=group, sequence=numeric, line_no=line_no)
    if match := LEGACY_US_PATTERN.match(value):
        return MarkdownId(value=value, family="US", group="US", sequence=int(match.group(1)), line_no=line_no)
    if match := LEGACY_TC_ALPHA_PATTERN.match(value):
        base, suffix = match.groups()
        return MarkdownId(value=value, family="TC", group=f"TC-{base}", sequence=ord(suffix) - 64, line_no=line_no)
    if match := UAT_MODULED_PATTERN.match(value):
        module, seq = match.groups()
        return MarkdownId(value=value, family="UAT", group=f"UAT-{module}", sequence=int(seq), line_no=line_no)
    if match := FEATURE_PATTERN.match(value):
        return MarkdownId(value=value, family="F", group="F", sequence=int(match.group(1)), line_no=line_no)
    if match := LEGACY_FEATURE_PATTERN.match(value):
        numeric = int(match.group(1))
        return MarkdownId(value=value, family="F", group=f"F-{numeric // 100}", sequence=numeric, line_no=line_no)
    return None


def extract_headings(text: str) -> List[MarkdownHeading]:
    headings: List[MarkdownHeading] = []
    for index, line in iter_non_fenced_lines(text):
        match = HEADING_PATTERN.match(line)
        if not match:
            continue
        level = len(match.group(1))
        headings.append(MarkdownHeading(level=level, number=match.group(3), text=match.group(4), line_no=index))
    return headings


def extract_ids(text: str) -> List[MarkdownId]:
    ids: List[MarkdownId] = []
    for index, line in iter_non_fenced_lines(text):
        for raw in extract_ids_from_line(line):
            meta = detect_id_meta(raw, index)
            if meta:
                ids.append(meta)
    return ids


def heading_gaps(headings: Iterable[MarkdownHeading]) -> List[str]:
    counters: Dict[int, int] = {}
    gaps: List[str] = []
    for heading in headings:
        expected = counters.get(heading.level, 0) + 1
        parts = [int(part) for part in heading.number.split(".")]
        current = parts[-1]
        if current != expected:
            gaps.append(
                f"HEADING_SKIP line {heading.line_no}: expected {expected} at level {heading.level}, found {heading.number}"
            )
        counters[heading.level] = current
        for deeper in list(counters):
            if deeper > heading.level:
                counters.pop(deeper, None)
    return gaps


def sequence_gaps(ids: Iterable[MarkdownId]) -> Tuple[List[str], List[str]]:
    duplicates: List[str] = []
    skips: List[str] = []
    grouped: Dict[Tuple[str, str], List[MarkdownId]] = {}
    seen_values: Dict[str, List[int]] = {}

    for item in ids:
        grouped.setdefault((item.family, item.group), []).append(item)
        seen_values.setdefault(item.value, []).append(item.line_no)

    for value, lines in seen_values.items():
        if len(lines) > 1:
            duplicates.append(f"INDEX_DUPLICATE {value} at lines {', '.join(str(line) for line in lines)}")

    for (_, group), items in grouped.items():
        sorted_items = sorted(items, key=lambda item: (item.sequence, item.line_no))
        unique_sequences = sorted({item.sequence for item in sorted_items})
        if not unique_sequences:
            continue
        start = unique_sequences[0]
        expected = list(range(start, start + len(unique_sequences)))
        if unique_sequences != expected:
            skips.append(
                f"INDEX_SKIP {group}: observed {unique_sequences}, expected contiguous {expected}"
            )
    return duplicates, skips


def replace_exact_tokens(text: str, replacements: Dict[str, str]) -> str:
    if not replacements:
        return text
    ordered = sorted(replacements, key=len, reverse=True)
    pattern = re.compile(r"\b(" + "|".join(re.escape(token) for token in ordered) + r")\b")
    output: List[str] = []
    in_fence = False
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue
        if in_fence:
            output.append(line)
            continue
        output.append(pattern.sub(lambda match: replacements.get(match.group(0), match.group(0)), line))
    return "".join(output)
