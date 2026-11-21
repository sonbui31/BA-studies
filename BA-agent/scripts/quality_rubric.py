#!/usr/bin/env python3
import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from ba_id_utils import (
    classify_file,
    collect_markdown_files,
    find_project_scheme,
    get_project_scheme,
    iter_non_fenced_lines,
    load_project_scheme,
    read_text,
    set_project_scheme,
)


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


VAGUE_WORDS = (
    "nhanh",
    "thời gian ngắn",
    "ngưỡng chấp nhận",
    "mức cơ bản",
    "đẹp",
    "dễ dùng",
    "linh hoạt",
    "hiệu quả",
    "ổn định",
    "an toàn",
    "sẵn sàng",
    "nhiều",
    "lớn",
    "tối thiểu",
)
IMPLEMENTATION_WORDS = (
    "react",
    "postgresql",
    "mysql",
    "mongodb",
    "redis",
    "api gateway",
    "kafka",
)
ACTOR_WORDS = (
    "admin",
    "user",
    "manager",
    "pm",
    "product manager",
    "product team",
    "portal user",
    "end user",
    "nhân viên",
    "khách hàng",
    "subscriber",
    "founder",
    "growth",
    "hệ thống",
    "system",
    "người dùng",
    "vật tư",
    "phòng vật tư",
    "khoa",
    "bệnh viện",
    "trưởng khoa",
    "ban điều hành",
    "kỹ sư",
    "quản trị",
)
METRIC_PATTERNS = (
    # "%" is not a word character, so it cannot be followed by \b; match it on its own branch.
    re.compile(
        r"\b\d+(?:[.,]\d+)?\s*(?:(?:ms|s|giây|phút|giờ|ngày|tháng|năm|mb|gb|rps|rows|records|users?|bản ghi|người dùng|lần)\b|%)",
        re.IGNORECASE,
    ),
    re.compile(r"\b(p95|rto|rpo|wcag|owasp|tls)\b", re.IGNORECASE),
)
VERIFIABLE_CONTROL_PATTERNS = (
    re.compile(r"\b(mfa|jwt|rbac|sso|sonarqube|quality gate|audit log|encryption|aes|zap)\b", re.IGNORECASE),
    re.compile(r"\b(kiểm thử|kiểm tra|quét|báo cáo|rà soát|monitoring|review)\b", re.IGNORECASE),
)
TRACE_PATTERN = re.compile(r"\b(BRQ-\d+(?:\.\d+)?|BRD-\d{3}|BR-\d{3}).*(TC-[A-Z0-9-]+|UAT-[A-Z0-9-]+)\b", re.IGNORECASE)
REQ_ID_PATTERN = re.compile(
    r"\b(FR(?:-[A-Z][A-Z0-9]{1,9})*-\d{1,4}(?:\.\d{1,2})?|NFR(?:-[A-Z][A-Z0-9]{1,9})?-\d{1,4}(?:\.\d{1,2})?"
    r"|BRQ-\d+(?:\.\d+)?|BRD-\d{3,4}|BR-\d{3,4})\b"
)
# A title line ("- **FR-QR-01: Quét mã QR**", "### FR-01.1 — Xem sổ liên lạc") states no requirement;
# the requirement sits in the lines under it ("Mô tả: ...", "| Mô tả | ... |", "| Actor | Parent |").
# "cần" is left out on purpose: it is also part of nouns ("chuyên cần").
MODAL_PATTERN = re.compile(r"\b(phải|cho phép|có thể|được|không được|shall|must|should|allow|allows)\b", re.IGNORECASE)
TITLE_LINE = re.compile(r"^\s*(?:#{1,6}\s+|[-*+]\s+)")
DESCRIPTION_LABEL = re.compile(r"^(?:mô tả|description|yêu cầu|requirement|nội dung)$", re.IGNORECASE)
ACTOR_LABEL = re.compile(r"^(?:actor|tác nhân|vai trò|người dùng|role)$", re.IGNORECASE)


def contains_word(lowered: str, words) -> bool:
    """Whole-word match (Unicode aware), so "pm" does not match "development"."""
    return any(re.search(r"(?<![\w])" + re.escape(word) + r"(?![\w])", lowered) for word in words)


@dataclass
class RequirementAssessment:
    req_id: str
    text: str
    smells: List[str]
    score: int
    family: str


# No square brackets: should_skip_candidate treats [..] as a template placeholder.
EXPLICIT_ACTOR = "tác nhân » "


def has_actor(lowered: str) -> bool:
    """Generic actor words, actors the project declares in ba-scheme.json, or an explicit Actor field."""
    if EXPLICIT_ACTOR in lowered:
        return True
    project = get_project_scheme()
    words = ACTOR_WORDS + tuple(project.actors) if project else ACTOR_WORDS
    return contains_word(lowered, words)


def detect_smells(text: str, family: str = "SRS") -> List[str]:
    lowered = text.lower()
    smells: List[str] = []

    has_metric = any(pattern.search(text) for pattern in METRIC_PATTERNS)
    has_verifiable_control = any(pattern.search(text) for pattern in VERIFIABLE_CONTROL_PATTERNS)

    if contains_word(lowered, VAGUE_WORDS) and not has_metric:
        smells.append("Vague Adjective")
    if re.search(r"\b(được|is|are)\b", lowered) and re.search(r"\b(gửi|xử lý|lưu|hiển thị|validated?|sent|processed)\b", lowered):
        smells.append("Passive Voice")
    if family not in {"NFR", "BRD", "BR"} and not has_actor(lowered):
        smells.append("Missing Actor")
    if family not in {"NFR", "BRD", "BR"} and (
        len(re.findall(r"\b(và|and)\b", lowered)) >= 2 or len(re.findall(r"\b(phải|shall|must)\b", lowered)) >= 2
    ):
        smells.append("Compound Requirement")
    if contains_word(lowered, IMPLEMENTATION_WORDS):
        smells.append("Implementation Bias")
    if contains_word(lowered, ("nhiều", "lớn", "tối đa", "minimum", "maximum", "hỗ trợ")) and not any(
        pattern.search(text) for pattern in METRIC_PATTERNS
    ):
        smells.append("Missing Boundary")
    if contains_word(lowered, ("an toàn", "sẵn sàng", "mở rộng", "bảo mật")) and not (
        has_metric or has_verifiable_control
    ):
        smells.append("Untestable NFR")
    if "trace" in lowered and not TRACE_PATTERN.search(text):
        smells.append("Orphan Requirement")

    return list(dict.fromkeys(smells))


def score_requirement(text: str, smells: List[str], family: str = "SRS") -> int:
    lowered = text.lower()
    score = 5

    if family not in {"NFR", "BRD", "BR"} and not has_actor(lowered):
        score -= 1
    obligation_words = ("phải", "shall", "must", "có thể", "cần", "cho phép", "i want", "so that")
    if not any(word in lowered for word in obligation_words):
        score -= 1
    if family not in {"BRD", "BR"} and not (
        any(pattern.search(text) for pattern in METRIC_PATTERNS)
        or any(pattern.search(text) for pattern in VERIFIABLE_CONTROL_PATTERNS)
    ):
        score -= 1
    condition_words = ("if", "khi", "nếu", "trước khi", "then", "sau khi", "precondition", "để", "so that", "giảm")
    if family not in {"BRD", "BR"} and not any(token in lowered for token in condition_words):
        score -= 1
    score -= min(2, len(smells))

    return max(1, min(5, score))


def normalize_candidate_line(req_id: str, line: str) -> str:
    if "|" not in line:
        return line.strip()
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    meaningful = []
    for cell in cells:
        if not cell:
            continue
        if REQ_ID_PATTERN.fullmatch(cell):
            continue
        if re.fullmatch(r"(S-\d{3}|SCOPE-\d{2,3}|Màn hình\s+\d+(?:\.\d+)?)", cell, re.IGNORECASE):
            continue
        if re.fullmatch(r"(P\d|Must|Should|Could|Won't|Bắt buộc|Nên có|Có thể|Chưa làm|☐|✅|❌)", cell, re.IGNORECASE):
            continue
        if re.fullmatch(r"(FR|NFR|US|TC|UAT|BRD|BR)(-[A-Z0-9]+)+", cell, re.IGNORECASE):
            continue
        meaningful.append(cell)
    if req_id.startswith(("BRQ-", "BRD-", "BR-", "NFR-")) and len(meaningful) >= 2:
        return ". ".join(meaningful)
    preferred = [cell for cell in meaningful if len(cell.split()) >= 3]
    preferred.sort(key=len, reverse=True)
    meaningful.sort(key=len, reverse=True)
    return (preferred[0] if preferred else (meaningful[0] if meaningful else line.strip()))


def should_skip_candidate(req_id: str, text: str) -> bool:
    lowered = text.lower()
    if "[tên" in lowered or "{{" in lowered or "[mô tả" in lowered or "[x]" in lowered:
        return True
    if "[" in text and "]" in text:
        return True
    if lowered in {"—", "-"}:
        return True
    if lowered.startswith("[") and lowered.endswith("]"):
        return True
    if "traceability" in lowered or "ma trận truy vết" in lowered:
        return True
    if "tiêu chí chấp nhận" in lowered:
        return True
    if req_id.startswith(("BRD-", "BR-")) and ("fr-" in lowered or "us-" in lowered or "tc-" in lowered or "uat-" in lowered):
        return True
    if req_id.startswith("BR-") and lowered.startswith("- br-"):
        return True
    if re.fullmatch(r"(us|fr|nfr|tc|uat|brd|br)(-[a-z0-9]+)+", lowered):
        return True
    if re.fullmatch(r"hđ\s+\d+(?:\.\d+)?", lowered, re.IGNORECASE):
        return True
    if re.fullmatch(r"màn hình\s+\d+(?:\.\d+)?", lowered):
        return True
    return False


def _label_and_value(line: str) -> Tuple[str, str]:
    """('mô tả', 'text') from "| Mô tả | text |", "- **Mô tả:** text" or "Mô tả: text"."""
    stripped = line.strip()
    if stripped.startswith("|"):
        cells = [cell.strip(" *`") for cell in stripped.strip("|").split("|")]
        if len(cells) >= 2:
            return cells[0], cells[1]
        return "", ""
    match = re.match(r"^[-*+]?\s*\**([^:*]{2,30}?)\**\s*:\s*\**\s*(.+)$", stripped)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return "", ""


def block_requirement_text(lines: List[str], start: int) -> str:
    """Description and actor written under a title line, up to the next heading or requirement ID."""
    description = actor = ""
    for line in lines[start + 1:start + 30]:
        stripped = line.strip()
        if stripped.startswith("#") or REQ_ID_PATTERN.match(stripped.lstrip("-*+| `")):
            break
        label, value = _label_and_value(stripped)
        if not value:
            continue
        if not description and DESCRIPTION_LABEL.match(label):
            description = value
        elif not actor and ACTOR_LABEL.match(label):
            actor = value
    if not description:
        return ""
    # An explicit Actor field names who acts, even when the role is domain-specific ("KTTS", "Parent").
    return f"{EXPLICIT_ACTOR}{actor}: {description}" if actor else description


def extract_requirement_candidates(text: str, doc_role: str = "srs") -> List[Tuple[str, str, str]]:
    if doc_role not in {"brd", "srs", "story"}:
        return []
    candidates: List[Tuple[str, str, str]] = []
    lines = [line for _, line in iter_non_fenced_lines(text)]
    for index, line in enumerate(lines):
        match = REQ_ID_PATTERN.search(line)
        if not match:
            continue
        req_id = match.group(1)
        stripped = line.strip()
        if not stripped.startswith("|") and not stripped.lstrip("#-*+> `").startswith(req_id):
            # "- Camera ... (FR-04.1)": a mention inside prose or a list, not the requirement itself.
            continue
        if req_id.startswith(("FR-", "NFR-")) and stripped.startswith("|") and not stripped.startswith(f"| {req_id}"):
            continue
        if req_id.startswith("NFR-") and line.strip().startswith("| NFR-") and line.count("|") <= 4:
            continue
        if req_id.startswith("NFR-") and "UAT-NFR-" in line:
            continue
        if req_id.startswith(("BRQ-", "BRD-", "BR-")) and doc_role not in {"brd", "story"}:
            continue
        if req_id.startswith(("BRD-", "BR-")) and "UAT-" in line and "US-" in line:
            continue
        family = "BR" if req_id.startswith("BR-") else ("BRD" if req_id.startswith(("BRQ-", "BRD-")) else ("NFR" if req_id.startswith("NFR-") else "SRS"))
        clean = normalize_candidate_line(req_id, line).replace("  ", " ")
        if TITLE_LINE.match(line) and not MODAL_PATTERN.search(clean):
            body = block_requirement_text(lines, index)
            if body:
                clean = f"{clean.strip('#-*+ ')} — {body}"
        if should_skip_candidate(req_id, clean):
            continue
        candidates.append((req_id, clean, family))
    return candidates


def evaluate_text(text: str, doc_role: str = "srs") -> Dict[str, object]:
    assessments: List[RequirementAssessment] = []
    for req_id, candidate, family in extract_requirement_candidates(text, doc_role=doc_role):
        smells = detect_smells(candidate, family=family)
        score = score_requirement(candidate, smells, family=family)
        assessments.append(
            RequirementAssessment(req_id=req_id, text=candidate, smells=smells, score=score, family=family)
        )

    if not assessments:
        return {"requirements": [], "avg_score": 0.0, "passed": False, "message": "No requirement-like lines found"}

    avg_score = round(sum(item.score for item in assessments) / len(assessments), 2)
    passed = avg_score >= 3.0 and all(item.score >= 3 for item in assessments)
    return {
        "requirements": [
            {
                "req_id": item.req_id,
                "score": item.score,
                "smells": item.smells,
                "text": item.text,
                "family": item.family,
            }
            for item in assessments
        ],
        "avg_score": avg_score,
        "passed": passed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit BA requirement quality using the bundle rubric.")
    parser.add_argument("target", help="Markdown file or folder")
    parser.add_argument("--output-json", help="Write JSON report")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    scheme_path = find_project_scheme(target)
    set_project_scheme(load_project_scheme(scheme_path) if scheme_path else None)
    reports = []
    for path in collect_markdown_files(target):
        result = evaluate_text(read_text(path), doc_role=classify_file(path))
        if result.get("requirements"):
            reports.append({"file": str(path), **result})

    payload = {"target": str(target), "reports": reports}
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    if args.output_json:
        Path(args.output_json).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    passed = all(report["passed"] for report in reports) if reports else False
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
