#!/usr/bin/env python3
"""Check that a BA document's role-review report covers the roles its Tier requires.

Required roles (see BA-document-rule/core/persona-simulation.md, section 3):
- Tier 1: R-BA + the deep-read roles of the document type.
- Tier 2: Tier 1 + R-SPONSOR, R-STAFF, R-TIME, R-QA, R-SEC, R-PM.
- Tier 3: all 21 roles.
- Sensitive data ("Dữ liệu nhạy cảm: Có") adds R-PRIVACY and R-SEC at any Tier.
A report without a Tier is checked as Tier 3. Optional roles may be listed; if listed they are
validated like required ones.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "BA-document-rule" / "core" / "persona-simulation.md"
ROLE_RE = re.compile(r"^\|\s*`(R-[A-Z]+)`\s*\|", re.MULTILINE)
FINDING_RE = re.compile(r"\bRV-\d+\b")
# Evidence must point somewhere: a section mark, an ID, a heading/table/line reference.
LOCATION_RE = re.compile(
    r"(§|\bmục\b|\bbảng\b|\bdòng\b|\bbước\b|\bphần\b|\bsection\b|\bline\b|\bheading\b|"
    r"\b[A-Z]{2,5}(?:-[A-Z0-9]{2,10})?-\d{2,4}\b|\b\d+(?:\.\d+)+\b)",
    re.IGNORECASE,
)
MIN_REASON_CHARS = 15
GENERIC_NA = {"không áp dụng", "không liên quan", "n/a", "na", "không có", "không cần"}

DOC_TYPE_ROLES: Dict[str, List[str]] = {
    "brd": ["R-CFO", "R-PO", "R-MANAGER", "R-CUSTOMER"],
    "process": ["R-MANAGER", "R-SME", "R-TRAINER"],
    "srs": ["R-TECH", "R-DATA", "R-SEC", "R-PARTNER"],
    "story": ["R-PO", "R-QA", "R-SME", "R-ACCESS"],
    "golive": ["R-OPS", "R-SUPPORT", "R-TRAINER", "R-ACCESS"],
}
DOC_TYPE_ALIASES = {
    "brd": "brd", "vision": "brd", "business case": "brd", "vision & scope": "brd",
    "bpmn": "process", "process": "process", "quy trình": "process", "sop": "process",
    "srs": "srs", "api": "srs", "data model": "srs", "srs-lite": "srs",
    "user story": "story", "story": "story", "ac": "story", "acceptance criteria": "story", "uat": "story",
    "go-live": "golive", "golive": "golive", "handover": "golive", "manual": "golive", "bàn giao": "golive",
}
TIER2_EXTRA = ["R-SPONSOR", "R-STAFF", "R-TIME", "R-QA", "R-SEC", "R-PM"]
SENSITIVE_EXTRA = ["R-PRIVACY", "R-SEC"]


def canonical_roles(protocol_text: str) -> List[str]:
    catalog = protocol_text.split("## 3. Quy tắc bắt buộc cho từng tài liệu", 1)[0]
    roles = ROLE_RE.findall(catalog)
    if len(roles) != 21 or len(set(roles)) != 21:
        raise ValueError("Giao thức phải định nghĩa đúng 21 mã vai trò duy nhất ở mục 1–2")
    return roles


def _filled(value: str) -> bool:
    value = value.strip()
    return bool(value and value not in {"—", "-", "…"} and not value.startswith("["))


def _header_field(report_text: str, name: str) -> Optional[str]:
    for line in report_text.splitlines()[:15]:
        for part in line.split("|"):
            match = re.match(rf"^\s*\**{name}\**\s*:\s*\**\s*(.+?)\s*$", part, re.IGNORECASE)
            if match:
                return match.group(1).strip("* ")
    return None


HUMAN_REVIEW_RE = re.compile(r"người thật\s*:\s*[^)\]\s][^)\]]{2,}", re.IGNORECASE)


def has_human_reviewer(report_text: str) -> bool:
    """A named human reviewer in the 'Loại rà soát' header (self-review by the AI does not count)."""
    value = _header_field(report_text, "Loại rà soát") or ""
    match = HUMAN_REVIEW_RE.search(value)
    return bool(match) and "<" not in match.group(0) and "[" not in match.group(0)


def report_scope(report_text: str) -> Tuple[int, Optional[str], bool, List[str]]:
    """Return (tier, doc_type, sensitive, notes) parsed from the report header."""
    notes: List[str] = []
    tier_raw = _header_field(report_text, "Tier")
    tier = 3
    if tier_raw and re.match(r"^[123]\b", tier_raw):
        tier = int(tier_raw[0])
    else:
        notes.append("Không đọc được Tier (1/2/3) ở đầu báo cáo; kiểm tra theo Tier 3")
    type_raw = (_header_field(report_text, "Loại tài liệu") or "").lower()
    doc_type = None
    for alias, key in sorted(DOC_TYPE_ALIASES.items(), key=lambda item: -len(item[0])):
        if alias in type_raw:
            doc_type = key
            break
    sensitive_raw = (_header_field(report_text, "Dữ liệu nhạy cảm") or "").lower()
    sensitive = sensitive_raw.startswith(("có", "yes", "co"))
    return tier, doc_type, sensitive, notes


def required_roles(all_roles: List[str], tier: int, doc_type: Optional[str], sensitive: bool) -> List[str]:
    if tier >= 3:
        return list(all_roles)
    required: List[str] = ["R-BA"] + DOC_TYPE_ROLES.get(doc_type or "", [])
    if tier == 2:
        required += TIER2_EXTRA
    if sensitive:
        required += SENSITIVE_EXTRA
    ordered = [role for role in all_roles if role in set(required)]
    return ordered


def validate_report(report_text: str, roles: List[str]) -> List[str]:
    errors: List[str] = []
    metadata = re.search(r"^Tài liệu:\s*([^\n]+)", report_text, re.MULTILINE)
    if not metadata or not _filled(metadata.group(1).split("|", 1)[0]):
        errors.append("Thiếu đường dẫn/tên tài liệu và phiên bản trong dòng 'Tài liệu:'")

    tier, doc_type, sensitive, _ = report_scope(report_text)
    if tier < 3 and doc_type is None:
        errors.append(
            "Tier 1/2 cần ghi 'Loại tài liệu:' (BRD/Vision, BPMN/quy trình, SRS/API/Data, "
            "User Story/AC/UAT, Go-live/bàn giao) để xác định vai trò bắt buộc"
        )
    required = required_roles(roles, tier, doc_type, sensitive)
    if tier >= 3 and not has_human_reviewer(report_text):
        errors.append(
            "Tier 3 cần ít nhất một người thật review độc lập (core/human-accountability.md, H4): "
            "ghi 'Loại rà soát: Review độc lập (người thật: <tên, vai trò>)' ở đầu báo cáo"
        )

    section = re.search(
        r"^## Độ phủ(?: \d+)? vai trò\s*$([\s\S]*?)(?=^## |\Z)",
        report_text,
        re.MULTILINE,
    )
    if not section:
        return errors + ["Thiếu mục '## Độ phủ vai trò'"]

    seen: Dict[str, Tuple[str, str, str]] = {}
    for line in section.group(1).splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or not re.fullmatch(r"`?R-[A-Z]+`?", cells[0]):
            continue
        role = cells[0].strip("`")
        if len(cells) != 4:
            errors.append(f"{role}: dòng ma trận phải có đúng 4 cột")
            continue
        if role in seen:
            errors.append(f"{role}: vai trò bị lặp")
        seen[role] = (cells[1].upper(), cells[2], cells[3])

    for role in required:
        if role not in seen:
            errors.append(f"{role}: thiếu vai trò (bắt buộc ở Tier {tier})")
    for role in sorted(set(seen) - set(roles)):
        errors.append(f"{role}: mã vai trò ngoài danh mục")

    findings_section = re.search(r"^## Phát hiện\s*$([\s\S]*?)(?=^## |\Z)", report_text, re.MULTILINE)
    finding_ids: Set[str] = set()
    if findings_section:
        finding_ids = set(re.findall(r"^\|\s*(RV-\d+)\s*\|", findings_section.group(1), re.MULTILINE))
    referenced: Set[str] = set()

    for role in [role for role in roles if role in seen]:
        status, reason, refs = seen[role]
        if status not in {"PASS", "ISSUE", "N/A"}:
            errors.append(f"{role}: kết quả phải là PASS, ISSUE hoặc N/A (đang là {status})")
        if not _filled(reason):
            errors.append(f"{role}: thiếu căn cứ hoặc lý do cụ thể")
        elif status == "N/A":
            if reason.strip().lower().rstrip(".") in GENERIC_NA or len(reason.strip()) < MIN_REASON_CHARS:
                errors.append(f"{role}: N/A phải nêu lý do gắn với phạm vi tài liệu (tối thiểu {MIN_REASON_CHARS} ký tự)")
        elif len(reason.strip()) < MIN_REASON_CHARS or not LOCATION_RE.search(reason):
            errors.append(f"{role}: căn cứ {status} phải trỏ tới vị trí cụ thể (mục, bảng, dòng hoặc ID)")
        ids = set(FINDING_RE.findall(refs))
        referenced |= ids
        if status == "ISSUE":
            if not ids:
                errors.append(f"{role}: ISSUE phải trỏ tới ID phát hiện RV-xx")
            for finding_id in sorted(ids - finding_ids):
                errors.append(f"{role}: {finding_id} không có trong mục Phát hiện")
    for finding_id in sorted(finding_ids - referenced):
        errors.append(f"{finding_id}: phát hiện không được vai trò nào trong ma trận trỏ tới")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("report", type=Path, help="Báo cáo review Markdown của một tài liệu")
    args = parser.parse_args()
    try:
        roles = canonical_roles(PROTOCOL.read_text(encoding="utf-8"))
        report_text = args.report.read_text(encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 2
    tier, doc_type, sensitive, notes = report_scope(report_text)
    for note in notes:
        print(f"NOTE: {note}")
    errors = validate_report(report_text, roles)
    required = required_roles(roles, tier, doc_type, sensitive)
    if errors:
        print(f"FAIL: {args.report} — {len(errors)} lỗi độ phủ")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"PASS: {args.report} — Tier {tier}, đủ {len(required)} vai trò bắt buộc, "
        "mỗi vai trò có kết quả và căn cứ"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
