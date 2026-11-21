#!/usr/bin/env python3
import fnmatch
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Tuple


# Module codes: 2-10 chars, start with a letter, may contain digits (FR-M01-001).
_MOD = r"[A-Z][A-Z0-9]{1,9}"
_SEQ = r"\d{3,4}"
# Sub-requirements: FR-TEA-003.1 is a child of FR-TEA-003 (same for BR, NFR, US, AC, TC).
_SUB = r"(?:\.\d{1,2})?"
_LOOKBEHIND = r"(?<![A-Za-z0-9-])"

# Lookbehind instead of a leading word boundary: an ID must not be the tail of a longer ID
# ("TC-NFR-001" must not also yield "NFR-001").
ID_PATTERNS = {
    "business": re.compile(rf"{_LOOKBEHIND}(?:BRQ-\d+(?:\.\d+)?|BRD-\d{{3,4}}{_SUB}|BR-\d{{3,4}}{_SUB})\b"),
    "functional": re.compile(rf"{_LOOKBEHIND}FR(?:-{_MOD})?-\d{{1,4}}{_SUB}\b"),
    "nonfunctional": re.compile(rf"{_LOOKBEHIND}NFR(?:-{_MOD})?-\d{{1,4}}{_SUB}\b"),
    "story": re.compile(rf"{_LOOKBEHIND}(?:US(?:-{_MOD})?-{_SEQ}{_SUB}|US\d{{2,3}})\b"),
    "test": re.compile(
        rf"{_LOOKBEHIND}(?:AC(?:-{_MOD})?-\d{{2,4}}{_SUB}|TC(?:-{_MOD})?-{_SEQ}{_SUB}|TC-\d{{2}}-[A-Z]|UAT(?:-[A-Z]+)?-\d{{2,4}})\b"
    ),
    "feature": re.compile(rf"{_LOOKBEHIND}(?:F\d{{2}}|F-\d{{3}})\b"),
}

KINDS = ("business", "functional", "nonfunctional", "story", "test", "feature")
KIND_FAMILY = {
    "business": "BR",
    "functional": "FR",
    "nonfunctional": "NFR",
    "story": "US",
    "test": "TC",
    "feature": "F",
}

# Section numbering is "1.", "1.2" or "1.2." followed by a space. A bare number without a dot
# ("## 2024 Roadmap", "### 3 bước đăng nhập") belongs to the title and is never renumbered.
HEADING_PATTERN = re.compile(
    r"^(?P<hashes>#{1,6})\s+(?P<num>\d+(?:\.\d+)+|\d+(?=\.))(?P<dot>\.?)\s+(?P<title>.+?)\s*$"
)
TOP_LEVEL_BRQ_PATTERN = re.compile(r"^BRQ-(\d+)$")
SUB_BRQ_PATTERN = re.compile(r"^BRQ-(\d+)\.(\d+)$")
MODULED_PATTERN = re.compile(rf"^(FR|NFR|US|AC|TC)-({_MOD})-(\d{{1,4}})$")
SIMPLE_HUNDREDS_PATTERN = re.compile(r"^(BRD|BR|FR|NFR|US|AC|TC|UAT)-(\d{2,4})$")
SIMPLE_AC_PATTERN = re.compile(r"^AC-(\d{2})$")
LEGACY_US_PATTERN = re.compile(r"^US(\d{2,3})$")
LEGACY_TC_ALPHA_PATTERN = re.compile(r"^TC-(\d{2})-([A-Z])$")
UAT_MODULED_PATTERN = re.compile(r"^UAT-([A-Z]{2,10})-(\d{2,4})$")
FEATURE_PATTERN = re.compile(r"^F(\d{2})$")
LEGACY_FEATURE_PATTERN = re.compile(r"^F-(\d{3})$")
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})")

# Legacy convention: BRD/BR/FR/NFR use the hundreds digit as a module bucket (FR-101..FR-199).
HUNDRED_BUCKET_FAMILIES = {"BRD", "BR", "FR", "NFR"}


@dataclass(frozen=True)
class MarkdownHeading:
    level: int
    text: str
    number: str
    line_no: int
    trailing_dot: bool = True


@dataclass(frozen=True)
class MarkdownId:
    value: str
    family: str
    group: str
    sequence: int
    line_no: int


def read_text(path: Path) -> str:
    """Read UTF-8 text keeping the original line endings (needed to write files back unchanged)."""
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def write_text(path: Path, text: str) -> None:
    """Write text without translating line endings (no LF -> CRLF conversion on Windows)."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def collect_markdown_files(target: Path) -> List[Path]:
    if not target.exists():
        raise FileNotFoundError(f"Target does not exist: {target}")
    if target.is_file():
        return [target]
    # ID-MIGRATION.md is the old -> new alias table written by id_migrate.py: old IDs on purpose.
    return sorted(path for path in target.rglob("*.md") if path.is_file() and path.name != "ID-MIGRATION.md")


@dataclass
class ProjectScheme:
    """ID formats and file roles a project declares in ba-scheme.json.

    Real projects keep their own IDs (F14, US20, Rule-4, SR-01, BRULE-001, BRQ-TEA-005).
    Declaring them lets the scripts read the bundle as it is instead of forcing a migration.
    """

    patterns: Dict[str, List["re.Pattern[str]"]] = field(default_factory=dict)
    roles: Dict[str, str] = field(default_factory=dict)
    actors: List[str] = field(default_factory=list)
    source: Optional[Path] = None

    def kind_of(self, token: str) -> Optional[str]:
        for kind, patterns in self.patterns.items():
            if any(pattern.fullmatch(token) for pattern in patterns):
                return kind
        return None

    def role_of(self, path: Path) -> Optional[str]:
        name = path.name.lower()
        for glob, role in self.roles.items():
            if fnmatch.fnmatch(name, glob.lower()):
                return role
        return None


SCHEME_FILE = "ba-scheme.json"
VALID_ROLES = {"brd", "srs", "story", "uat", "feature", "other"}
_PROJECT_SCHEME: Optional[ProjectScheme] = None
_PROJECT_LINE_PATTERNS: List["re.Pattern[str]"] = []


def load_project_scheme(path: Path) -> ProjectScheme:
    """Parse ba-scheme.json: {"ids": {kind: [regex]}, "files": {glob: role}, "actors": [name]}."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    scheme = ProjectScheme(source=Path(path))
    for kind, raw_patterns in (data.get("ids") or {}).items():
        if kind not in KINDS:
            raise ValueError(f"{path}: unknown ID kind '{kind}' (use one of {', '.join(KINDS)})")
        if isinstance(raw_patterns, str):
            raw_patterns = [raw_patterns]
        scheme.patterns[kind] = [re.compile(item) for item in raw_patterns]
    for glob, role in (data.get("files") or {}).items():
        if role not in VALID_ROLES:
            raise ValueError(f"{path}: unknown role '{role}' for '{glob}' (use one of {', '.join(sorted(VALID_ROLES))})")
        scheme.roles[glob] = role
    scheme.actors = [str(item).lower() for item in (data.get("actors") or [])]
    return scheme


def find_project_scheme(target: Path) -> Optional[Path]:
    """ba-scheme.json in the target folder (or the folder of a target file), or one level up."""
    folder = target if target.is_dir() else target.parent
    for candidate in (folder / SCHEME_FILE, folder.parent / SCHEME_FILE):
        if candidate.is_file():
            return candidate
    return None


def set_project_scheme(scheme: Optional[ProjectScheme]) -> None:
    global _PROJECT_SCHEME, _PROJECT_LINE_PATTERNS
    _PROJECT_SCHEME = scheme
    _PROJECT_LINE_PATTERNS = []
    if scheme:
        for patterns in scheme.patterns.values():
            for pattern in patterns:
                _PROJECT_LINE_PATTERNS.append(re.compile(rf"{_LOOKBEHIND}(?:{pattern.pattern})(?![A-Za-z0-9]|\.\d)"))


def get_project_scheme() -> Optional[ProjectScheme]:
    return _PROJECT_SCHEME


def id_kind(token: str) -> str:
    """business / functional / nonfunctional / story / test / feature / other.

    A project-declared format wins over the built-in reading (in QLTS "F14" is a functional ID).
    """
    if _PROJECT_SCHEME:
        kind = _PROJECT_SCHEME.kind_of(token)
        if kind:
            return kind
    if token.startswith(("BRQ-", "BRD-", "BR-")):
        return "business"
    if token.startswith("FR-"):
        return "functional"
    if token.startswith("NFR-"):
        return "nonfunctional"
    if token.startswith("US"):
        return "story"
    if token.startswith(("AC-", "TC-", "UAT-")):
        return "test"
    if re.fullmatch(r"F\d{2}|F-\d{3}", token):
        return "feature"
    return "other"


def parent_id(token: str) -> Optional[str]:
    """FR-TEA-003.1 -> FR-TEA-003; BRQ-02.1 -> BRQ-02; None when the token has no sub-number."""
    match = re.fullmatch(r"(.*\d)\.(\d{1,2})", token)
    if not match:
        return None
    base = match.group(1)
    if id_kind(base) == "other" or id_kind(base) != id_kind(token):
        return None
    return base


def classify_file(path: Path) -> str:
    if _PROJECT_SCHEME:
        role = _PROJECT_SCHEME.role_of(path)
        if role:
            return role
    name = path.name.lower()
    if "brd" in name:
        return "brd"
    if "srs" in name or "prd" in name or "requirement" in name or "yeu-cau" in name:
        return "srs"
    if "uat" in name or "acceptance" in name or "criteria" in name or "test" in name or "beta" in name:
        return "uat"
    if "story" in name or "stories" in name:
        return "story"
    if "feature" in name:
        return "feature"
    return "other"


def extract_ids_from_line(line: str) -> List[str]:
    """IDs in reading order. A match nested inside a longer match at the same place is dropped."""
    spans: List[Tuple[int, int, str]] = []
    for pattern in list(ID_PATTERNS.values()) + _PROJECT_LINE_PATTERNS:
        for match in pattern.finditer(line):
            spans.append((match.start(), match.end(), match.group(0)))
    kept: List[Tuple[int, int, str]] = []
    for start, end, value in sorted(spans, key=lambda item: (item[0], -(item[1] - item[0]))):
        if any(k_start <= start and end <= k_end and (k_start, k_end) != (start, end) for k_start, k_end, _ in kept):
            continue
        kept.append((start, end, value))
    ordered: List[str] = []
    for _, _, value in sorted(kept):
        if value not in ordered:
            ordered.append(value)
    return ordered


def iter_fence_state(text: str, keepends: bool = False) -> Iterator[Tuple[int, str, bool]]:
    """Yield (line_no, line, inside_or_on_fence) handling both ``` and ~~~ fences."""
    fence: Optional[str] = None
    for index, line in enumerate(text.splitlines(keepends=keepends), start=1):
        match = FENCE_PATTERN.match(line)
        if fence is None:
            if match:
                fence = match.group(1)
                yield index, line, True
                continue
            yield index, line, False
        else:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence):
                fence = None
            yield index, line, True


def iter_non_fenced_lines(text: str) -> Iterator[Tuple[int, str]]:
    for index, line, fenced in iter_fence_state(text):
        if not fenced:
            yield index, line


def _generic_meta(value: str, family: str, line_no: int) -> MarkdownId:
    """Group/sequence for a project-declared ID: trailing number (or letter) is the sequence."""
    if match := re.fullmatch(r"(.*?)(\d+)", value):
        return MarkdownId(value=value, family=family, group=match.group(1) or family, sequence=int(match.group(2)), line_no=line_no)
    if match := re.fullmatch(r"(.*?)([A-Z])", value):
        return MarkdownId(value=value, family=family, group=match.group(1), sequence=ord(match.group(2)) - 64, line_no=line_no)
    return MarkdownId(value=value, family=family, group=value, sequence=0, line_no=line_no)


def detect_id_meta(value: str, line_no: int) -> Optional[MarkdownId]:
    if _PROJECT_SCHEME:
        kind = _PROJECT_SCHEME.kind_of(value)
        if kind:
            return _generic_meta(value, KIND_FAMILY[kind], line_no)
    parent = parent_id(value)
    if parent and not value.startswith("BRQ-"):
        base = detect_id_meta(parent, line_no)
        family = base.family if base else KIND_FAMILY[id_kind(parent)]
        return MarkdownId(value=value, family=family, group=parent, sequence=int(value.rsplit(".", 1)[1]), line_no=line_no)
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
        if family in HUNDRED_BUCKET_FAMILIES:
            group = f"{family}-{numeric // 100}"
        else:
            group = family
        return MarkdownId(value=value, family=family, group=group, sequence=numeric, line_no=line_no)
    if match := SIMPLE_AC_PATTERN.match(value):
        return MarkdownId(value=value, family="AC", group="AC", sequence=int(match.group(1)), line_no=line_no)
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
        headings.append(
            MarkdownHeading(
                level=len(match.group("hashes")),
                number=match.group("num"),
                text=match.group("title"),
                line_no=index,
                trailing_dot=bool(match.group("dot")),
            )
        )
    return headings


def extract_ids(text: str) -> List[MarkdownId]:
    ids: List[MarkdownId] = []
    for index, line in iter_non_fenced_lines(text):
        for raw in extract_ids_from_line(line):
            meta = detect_id_meta(raw, index)
            if meta:
                ids.append(meta)
    return ids


def expected_heading_numbers(headings: Iterable[MarkdownHeading]) -> List[Tuple[MarkdownHeading, List[int]]]:
    """Compute the expected section number for each numbered heading.

    Numbering depth comes from the number itself ("1.2" is depth 2), not from the count of '#'.
    The parent prefix is taken from the closest preceding heading one level shallower, so a
    template that starts at "2.0" or uses "1.1" for every H2 keeps its own scheme. Only the last
    component is renumbered to make siblings contiguous. A first sibling may start at 0 or 1.
    """
    last: Dict[int, List[int]] = {}
    result: List[Tuple[MarkdownHeading, List[int]]] = []
    for heading in headings:
        parts = [int(part) for part in heading.number.split(".")]
        depth = len(parts)
        prefix = last[depth - 1] if depth > 1 and (depth - 1) in last else parts[:-1]
        previous = last.get(depth)
        if previous is not None and previous[:-1] == prefix:
            value = previous[-1] + 1
        else:
            value = parts[-1] if parts[-1] in (0, 1) else 1
        expected = prefix + [value]
        result.append((heading, expected))
        last[depth] = expected
        for deeper in [key for key in last if key > depth]:
            last.pop(deeper)
    return result


def heading_gaps(headings: Iterable[MarkdownHeading]) -> List[str]:
    gaps: List[str] = []
    for heading, expected in expected_heading_numbers(headings):
        expected_text = ".".join(str(part) for part in expected)
        if heading.number != expected_text:
            gaps.append(
                f"HEADING_SKIP line {heading.line_no}: expected {expected_text}, found {heading.number}"
            )
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
        unique_sequences = sorted({item.sequence for item in items})
        if not unique_sequences:
            continue
        start = unique_sequences[0]
        expected = list(range(start, start + len(unique_sequences)))
        if unique_sequences != expected:
            skips.append(
                f"INDEX_SKIP {group}: observed {unique_sequences}, expected contiguous {expected}"
            )
    return duplicates, skips


ROLE_FAMILIES = {
    "brd": {"BRQ", "BRD", "BR"},
    # Business rules are often written in the SRS next to the FR that enforces them.
    "srs": {"FR", "NFR", "BR"},
    "story": {"US"},
    "uat": {"AC", "TC", "UAT"},
    "feature": {"F"},
}

# The document where an ID family is minted. Numbering continuity and cross-file duplicates are
# judged only there; a BR restated in the SRS or a BRQ listed in an SRS matrix is a reference.
FAMILY_PRIMARY_ROLE = {
    "BRQ": "brd",
    "BRD": "brd",
    "BR": "brd",
    "FR": "srs",
    "NFR": "srs",
    "US": "story",
    "AC": "uat",
    "TC": "uat",
    "UAT": "uat",
    "F": "feature",
}


def is_primary(definition: "IdDefinition", role: str) -> bool:
    return FAMILY_PRIMARY_ROLE.get(definition.meta.family) == role


_ID_LIST_CELL = re.compile(r"^[\sA-Z0-9.,;:/→>\-–—()&+✅☐✓x]*$")

# A heading that announces a traceability matrix: every row under it is a cross-reference.
TRACE_HEADING = re.compile(r"truy\s*vết|traceability|ma\s*trận|\bRTM\b|matrix|liên kết yêu cầu", re.IGNORECASE)
# Header cells naming an ID family. A table whose header names 3+ families is a matrix.
HEADER_FAMILY_PATTERNS = {
    "business": re.compile(r"\b(?:brq|brd|br|brule|business|nghiệp vụ|rule)\b", re.IGNORECASE),
    "functional": re.compile(r"\b(?:fr|sr|srs|functional|chức năng|use case|uc)\b", re.IGNORECASE),
    "story": re.compile(r"\b(?:us|user story|story|stories)\b", re.IGNORECASE),
    "test": re.compile(r"\b(?:tc|ac|uat|test|tests|kiểm thử|acceptance|nghiệm thu)\b", re.IGNORECASE),
    "feature": re.compile(r"\b(?:feature|tính năng|f)\b", re.IGNORECASE),
}
# Attribute tables: "| ID | FR-TEA-003 |" or "| Mã yêu cầu | US-AUTH-001 |".
ATTRIBUTE_KEY = re.compile(r"^(?:id|mã|mã id|mã yc|mã yêu cầu|requirement id|story id|req id)$", re.IGNORECASE)
# Header of a defining ID column ("ID", "Mã YC", "FR", "US ID"). Under any other first-column
# header ("Module", "Phân hệ") repeated IDs only group rows.
ID_COLUMN_HEADER = re.compile(r"\b(?:id|mã|fr|nfr|us|br|brq|brd|ac|tc|uat|story|yêu cầu|requirement)\b", re.IGNORECASE)
_ALIGN_ROW = re.compile(r"^\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)*\|?\s*$")


def _split_cells(stripped: str) -> List[str]:
    cells = re.split(r"(?<!\\)\|", stripped.strip().strip("|"))
    return [cell.strip() for cell in cells]


def _header_is_matrix(cells: List[str]) -> bool:
    families = set()
    for cell in cells:
        for family, pattern in HEADER_FAMILY_PATTERNS.items():
            if pattern.search(cell):
                families.add(family)
                break
    return len(families) >= 3


def _is_matrix_row(cells: List[str]) -> bool:
    """A traceability-matrix row: every cell after the first is empty, an ID list or a short mark."""
    rest = cells[1:]
    if not rest:
        return False
    has_id = False
    for cell in rest:
        if extract_ids_from_line(cell):
            has_id = True
            stripped = cell
            for token in extract_ids_from_line(cell):
                stripped = stripped.replace(token, "")
            if not _ID_LIST_CELL.match(stripped):
                return False
        elif len(cell) > 12:
            return False
    return has_id


@dataclass(frozen=True)
class IdDefinition:
    meta: MarkdownId
    matrix_row: bool
    site: str = "line"  # heading | table | line (list items and plain lines)


def definition_ids(text: str, role: str) -> List[IdDefinition]:
    """IDs a document of this role defines, with line numbers.

    A definition is an ID that opens a table row (first cell), a heading ("### US-AUTH-001: ..."),
    a list item or a line. Only ID families owned by the role count (BRD -> BRQ/BR, SRS -> FR/NFR,
    story -> US, UAT/AC -> AC/TC/UAT, feature map -> F).

    Rows that only cross-reference are marked ``matrix_row`` so duplicate checks ignore them while
    coverage still sees them: rows of a traceability matrix (a table under a "Truy vết / Ma trận"
    heading, or whose header names 3+ ID families), rows passing the _is_matrix_row heuristic, and
    rows of a table that groups by its first column: the column header is not an ID column
    ("Module", "Kịch bản") and some ID repeats in it ("| F05 | EX-1A |", "| F05 | EX-1B |").
    Attribute tables ("| ID | FR-TEA-003 |") define the ID in the second cell.
    """
    families = ROLE_FAMILIES.get(role, set())
    found: List[IdDefinition] = []
    if not families:
        return found
    in_table = False
    table_is_matrix = False
    trace_section = False
    first_column_groups = False
    table_rows: List[int] = []  # indexes into found for first-column definitions of the current table

    def close_table() -> None:
        values = [found[index].meta.value for index in table_rows]
        if first_column_groups and len(values) != len(set(values)):
            for index in table_rows:
                item = found[index]
                found[index] = IdDefinition(meta=item.meta, matrix_row=True, site=item.site)
        table_rows.clear()
    for line_no, line in iter_non_fenced_lines(text):
        stripped = line.strip()
        if not stripped:
            if in_table:
                close_table()
            in_table = False
            continue
        matrix = False
        site = "line"
        grouping_row = False
        if stripped.startswith("|"):
            site = "table"
            cells = _split_cells(stripped)
            if not in_table:
                # First row of a table is its header: decide once whether the table is a matrix.
                in_table = True
                table_is_matrix = trace_section or _header_is_matrix(cells)
                header_first = cells[0].strip("*` ") if cells else ""
                first_column_groups = not (extract_ids_from_line(header_first) or ID_COLUMN_HEADER.search(header_first))
            if _ALIGN_ROW.match(stripped):
                continue
            if len(cells) >= 2 and ATTRIBUTE_KEY.match(cells[0].strip("*` ")):
                candidate = cells[1].strip("*` ")
            else:
                candidate = cells[0].strip("*` ") if cells else ""
                matrix = table_is_matrix or _is_matrix_row(cells)
                grouping_row = True
        else:
            if in_table:
                close_table()
            in_table = False
            if stripped.startswith("#"):
                trace_section = bool(TRACE_HEADING.search(stripped))
                site = "heading"
            heading = re.match(r"^#{1,6}\s+(?:\d+(?:\.\d+)*\.?\s+)?(.*)$", stripped)
            candidate = heading.group(1) if heading else re.sub(r"^(?:[-*+]|\d+\.)\s+", "", stripped)
            candidate = candidate.lstrip("*`[ ")
        tokens = extract_ids_from_line(candidate)
        if not tokens:
            continue
        first = min(tokens, key=lambda token: candidate.find(token))
        if not candidate.startswith(first):
            continue
        meta = detect_id_meta(first, line_no)
        if meta and meta.family in families:
            if grouping_row:
                table_rows.append(len(found))
            found.append(IdDefinition(meta=meta, matrix_row=matrix, site=site))
    if in_table:
        close_table()
    return found


def matrix_lines(text: str) -> List[int]:
    """Line numbers of traceability-matrix rows: tables under a "Truy vết / Ma trận" heading or
    whose header names 3+ ID families. Each such row links the whole chain it lists."""
    rows: List[int] = []
    in_table = False
    is_matrix = False
    trace_section = False
    for line_no, line in iter_non_fenced_lines(text):
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = _split_cells(stripped)
            if not in_table:
                in_table = True
                is_matrix = trace_section or _header_is_matrix(cells)
                continue
            if is_matrix and not _ALIGN_ROW.match(stripped):
                rows.append(line_no)
            continue
        in_table = False
        if stripped.startswith("#"):
            trace_section = bool(TRACE_HEADING.search(stripped))
    return rows


def definition_blocks(text: str, role: str) -> Dict[int, str]:
    """Map each line inside a definition block to the ID that owns the block.

    Real documents put links on the lines under a definition, not on the same line:

        ### US20: Ghi vết biến động tài chính
        > **Related BRQ-ID:** `BRQ-02.1` | **FR-ID:** `F14`

        - **FR-QR-01: Quét mã QR**
          - **Nguồn:** BRQ-03

    A heading definition owns the lines up to the next heading of the same or a higher level.
    A list/line definition owns the lines up to the next definition or the next heading.
    An attribute table row ("| ID | FR-TEA-003 |") starts a block when no heading owns one.
    Rows of a definition list table own only themselves (row-level links cover them).
    """
    defs = {item.meta.line_no: item for item in definition_ids(text, role) if not item.matrix_row}
    owners: Dict[int, str] = {}
    owner: Optional[str] = None
    owner_level = 7  # heading level of the owner; 7 = list/line owner
    for line_no, line in iter_non_fenced_lines(text):
        stripped = line.strip()
        item = defs.get(line_no)
        heading = re.match(r"^(#{1,6})\s", stripped)
        if heading:
            level = len(heading.group(1))
            if item and item.site == "heading":
                owner, owner_level = item.meta.value, level
            elif owner and (owner_level == 7 or level <= owner_level):
                owner = None
            continue
        if item and item.site == "line":
            owner, owner_level = item.meta.value, 7
            continue
        if item and item.site == "table":
            cells = _split_cells(stripped)
            if cells and ATTRIBUTE_KEY.match(cells[0].strip("*` ")):
                if owner is None:
                    owner_level = 7
                owner = item.meta.value
            continue
        if owner:
            owners[line_no] = owner
    return owners


def duplicate_definitions(definitions: Iterable[IdDefinition]) -> Dict[str, List[int]]:
    """IDs defined twice in the same way (two headings, two defining table rows, two list lines).

    An overview list ("F05. Quản lý tài sản") followed by a detail heading ("### F05 — ...") is an
    outline plus its section, not a duplicate; matrix rows never count.
    """
    seen: Dict[Tuple[str, str], List[int]] = {}
    for item in definitions:
        if item.matrix_row:
            continue
        seen.setdefault((item.meta.value, item.site), []).append(item.meta.line_no)
    duplicates: Dict[str, List[int]] = {}
    for (value, _), lines in seen.items():
        if len(lines) > 1:
            duplicates.setdefault(value, []).extend(lines)
    return {value: sorted(lines) for value, lines in duplicates.items()}


def replace_exact_tokens(text: str, replacements: Dict[str, str]) -> str:
    """Replace whole-token IDs simultaneously (so A->B, B->C never chains) outside code fences."""
    if not replacements:
        return text
    ordered = sorted(replacements, key=len, reverse=True)
    pattern = re.compile(r"(?<![\w.-])(" + "|".join(re.escape(token) for token in ordered) + r")(?![\w-]|\.\d)")
    output: List[str] = []
    for _, line, fenced in iter_fence_state(text, keepends=True):
        if fenced:
            output.append(line)
            continue
        output.append(pattern.sub(lambda match: replacements.get(match.group(0), match.group(0)), line))
    return "".join(output)
