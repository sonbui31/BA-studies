#!/usr/bin/env python3
"""Executable BA pre-flight checks for markdown artifact bundles."""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from ba_id_utils import (
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
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from ba_id_utils import (
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
    from quality_rubric import evaluate_text
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from quality_rubric import evaluate_text


PASS = "✅ PASS"
FAIL = "❌ FAIL"
NA = "⚠️ N/A"
PASS_CODE = "PASS"
FAIL_CODE = "FAIL"
NA_CODE = "N/A"
PLACEHOLDER_PATTERN = re.compile(r"(\[[^\]\n]{1,80}\]|\{\{[^}\n]{0,80}\}\}|\$\[_+\])")
VIETNAMESE_DIACRITIC_PATTERN = re.compile(r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]", re.IGNORECASE)
UNACCENTED_VIETNAMESE_HINT_PATTERN = re.compile(
    r"\b("
    r"nguoi|khach|hang|yeu|cau|chuc|nang|thong|tin|he|thong|phai|khong|duoc|"
    r"quy|trinh|du|lieu|bao|cao|quan|ly|dang|nhap|hien|thi|danh|sach|don|"
    r"hang|kiem|tra|nghiem|thu|tai|lieu|nguon|vao|dau|ra|xu|ly|luu|tru"
    r")\b",
    re.IGNORECASE,
)


def has_any(text: str, *tokens: str) -> bool:
    lowered = text.lower()
    return any(token.lower() in lowered for token in tokens)


def count_placeholders(text: str) -> int:
    ignored = {"[x]", "[ ]"}
    count = 0
    for _, line in iter_non_fenced_lines(text):
        if line.lstrip().startswith(("- [ ]", "- [x]", "- [X]")):
            continue
        for match in PLACEHOLDER_PATTERN.findall(line):
            if match.lower() in ignored:
                continue
            count += 1
    return count


def vietnamese_diacritics_status(text: str) -> Tuple[bool, str]:
    prose_lines = []
    for _, line in iter_non_fenced_lines(text):
        stripped = line.strip()
        if not stripped or stripped.startswith("|---"):
            continue
        if re.search(r"`[^`]+`|https?://|/[A-Za-z0-9_/-]+|[A-Z]{2,10}-[A-Z0-9-]*\d+", stripped):
            stripped = re.sub(r"`[^`]+`|https?://\S+|/[A-Za-z0-9_/-]+|[A-Z]{2,10}-[A-Z0-9-]*\d+", " ", stripped)
        prose_lines.append(stripped)

    prose = "\n".join(prose_lines)
    hint_count = len(UNACCENTED_VIETNAMESE_HINT_PATTERN.findall(prose))
    diacritic_count = len(VIETNAMESE_DIACRITIC_PATTERN.findall(prose))
    if hint_count >= 12 and diacritic_count < max(8, hint_count // 3):
        return False, f"likely unaccented Vietnamese ({hint_count} unaccented hints / {diacritic_count} diacritic chars)"
    return True, f"diacritics aligned ({hint_count} unaccented hints / {diacritic_count} diacritic chars)"


def count_table_rows(text: str, anchors: Tuple[str, ...]) -> int:
    lines = text.splitlines()
    capture = False
    count = 0
    for line in lines:
        lowered = line.lower()
        if any(anchor.lower() in lowered for anchor in anchors):
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture and line.strip().startswith("|") and "---" not in line:
            count += 1
    return max(0, count - 1)


def count_ids(text: str, prefixes: Tuple[str, ...]) -> int:
    ids = extract_ids(text)
    return sum(1 for item in ids if item.value.startswith(prefixes))


def definition_ids_for_role(text: str, role: str):
    ids = []

    def ids_from_text(value: str, line_no: int):
        found = []
        for token in extract_ids_from_line(value):
            meta = detect_id_meta(token, line_no)
            if meta:
                found.append(meta)
        return found

    for line_no, line in iter_non_fenced_lines(text):
        stripped = line.lstrip()
        if role == "brd":
            if stripped.startswith("| BRQ-") or stripped.startswith("| BRD-") or stripped.startswith("| BR-"):
                first_cell = stripped.strip().strip("|").split("|")[0].strip()
                ids.extend(item for item in ids_from_text(first_cell, line_no) if item.family in {"BRQ", "BRD", "BR"})
            elif stripped.startswith("- BRQ-"):
                ids.extend(item for item in ids_from_text(line, line_no) if item.family == "BRQ")
            elif stripped.startswith("- BR-"):
                ids.extend(item for item in extract_ids(line) if item.family == "BR")
        elif role == "srs":
            if stripped.startswith("| FR-") or stripped.startswith("| NFR-"):
                cells = [cell.strip() for cell in stripped.strip().strip("|").split("|")]
                first_cell = cells[0] if cells else ""
                if first_cell.startswith("NFR-") and len(cells) < 5:
                    continue
                if first_cell.startswith("NFR-") and any("UAT-NFR-" in cell for cell in cells):
                    continue
                ids.extend(item for item in extract_ids(first_cell) if item.family in {"FR", "NFR"})
        elif role == "story":
            if stripped.startswith("| US-") or stripped.startswith("| US"):
                first_cell = stripped.strip().strip("|").split("|")[0].strip()
                ids.extend(item for item in extract_ids(first_cell) if item.family == "US")
        elif role == "uat":
            if stripped.startswith("| AC-") or stripped.startswith("| UAT-") or stripped.startswith("| TC-"):
                first_cell = stripped.strip().strip("|").split("|")[0].strip()
                ids.extend(item for item in extract_ids(first_cell) if item.family in {"AC", "UAT", "TC"})
    return ids


def numbering_status(text: str, role: str) -> Tuple[bool, str]:
    heading_issues = heading_gaps(extract_headings(text))
    duplicates, skips = sequence_gaps(definition_ids_for_role(text, role))
    problems = []
    if heading_issues:
        problems.append(f"{len(heading_issues)} heading gap(s)")
    if duplicates:
        problems.append(f"{len(duplicates)} duplicate ID(s)")
    if skips:
        problems.append(f"{len(skips)} numbering skip(s)")
    return (not problems, ", ".join(problems) if problems else "numbering aligned")


def make_check(name: str, passed: bool, detail: str) -> Dict[str, str]:
    return {
        "item": name,
        "status": PASS if passed else FAIL,
        "status_code": PASS_CODE if passed else FAIL_CODE,
        "detail": detail,
    }


def make_na(name: str, detail: str) -> Dict[str, str]:
    return {"item": name, "status": NA, "status_code": NA_CODE, "detail": detail}


def brd_checks(text: str, ctx: Dict[str, str]) -> List[Dict[str, str]]:
    checks: List[Dict[str, str]] = []
    placeholder_count = count_placeholders(text)
    stakeholder_rows = max(
        count_table_rows(text, ("stakeholder", "bên liên quan")),
        count_table_rows(text, ("đối tượng đọc",)),
    )
    assumption_rows = count_table_rows(text, ("giả định",))
    constraint_rows = count_table_rows(text, ("ràng buộc",))
    pain_rows = count_table_rows(text, ("vấn đề hiện tại", "pain point"))
    success_rows = count_table_rows(text, ("tiêu chí thành công", "success metrics", "mục tiêu dự án"))
    rule_rows = max(
        count_table_rows(text, ("quy tắc nghiệp vụ", "business rules")),
        len(re.findall(r"\b(QT|BR)-\d+", text)),
    )

    checks.append(make_check("Open Placeholders", placeholder_count == 0, f"{placeholder_count} placeholder marker(s)"))
    ok, detail = vietnamese_diacritics_status(text)
    checks.append(make_check("Vietnamese Diacritics", ok, detail))
    checks.append(make_check("Glossary", has_any(text, "thuật ngữ", "glossary"), "glossary markers"))
    checks.append(make_check("Problem Statement", pain_rows >= 2 or text.count("Rủi ro #") >= 2, f"{pain_rows} problem rows"))
    checks.append(make_check("Stakeholder Map", stakeholder_rows >= 3, f"{stakeholder_rows} stakeholder rows"))
    checks.append(make_check("OKRs / Success Metrics", success_rows >= 2 or has_any(text, "okr", "baseline", "target"), f"{success_rows} metric rows"))
    checks.append(make_check("MoSCoW Priority", sum(text.count(token) for token in ("Must", "Should", "Could", "Won't", "Bắt buộc", "Nên có", "Có thể", "Chưa làm")) >= 4, "priority markers"))
    checks.append(make_check("Business Rules", rule_rows >= 1, f"{rule_rows} rule markers"))
    checks.append(make_check("Assumptions & Constraints", assumption_rows >= 1 and constraint_rows >= 1, f"{assumption_rows} assumptions / {constraint_rows} constraints"))
    checks.append(make_check("Traceability Matrix", has_any(text, "ma trận truy vết", "traceability", "rtm"), "traceability section"))
    checks.append(make_check("As-Is Process", has_any(text, "as-is", "hiện trạng", "quy trình hiện tại"), "current-state markers"))
    checks.append(make_check("Elicitation Record", has_any(text, "phỏng vấn", "interview", "workshop", "meeting"), "elicitation evidence"))
    if rule_rows >= 5:
        checks.append(make_check("Business Rule Architecture", has_any(text, "execution order", "override matrix", "ma trận ghi đè"), "rule architecture markers"))
    else:
        checks.append(make_na("Business Rule Architecture", "<5 rules detected"))
    if has_any(text, "audit", "severity", "nghiêm trọng", "cảnh báo"):
        checks.append(make_check("Output Severity Design", has_any(text, "mức độ", "severity", "critical", "warning"), "severity markers"))
    else:
        checks.append(make_na("Output Severity Design", "no audit/validation-heavy flow detected"))
    if has_any(text, "lịch sử", "đợt trước", "retention", "memory"):
        checks.append(make_check("System Memory Check", has_any(text, "system memory", "dữ liệu lịch sử", "cần nhớ gì"), "history-dependent markers"))
    else:
        checks.append(make_na("System Memory Check", "no historical-dependency markers"))
    if has_any(text, " ai ", " ml ", "ocr", "nlp", "classification", "recommendation"):
        checks.append(make_check("AI Feature Spec", has_any(text, "accuracy", "confidence", "false positive", "human-in-the-loop"), "AI control markers"))
    else:
        checks.append(make_na("AI Feature Spec", "no AI/ML markers"))
    ok, detail = numbering_status(text, "brd")
    checks.append(make_check("Sequential Numbering", ok, detail))
    return checks


def srs_checks(text: str, ctx: Dict[str, str]) -> List[Dict[str, str]]:
    checks: List[Dict[str, str]] = []
    placeholder_count = count_placeholders(text)
    nfr_count = count_ids(text, ("NFR",))
    fr_count = count_ids(text, ("FR",))
    actor_rows = count_table_rows(text, ("actors", "đối tượng đọc", "actor"))
    mermaid_count = text.count("```mermaid")
    rubric = evaluate_text(text)

    checks.append(make_check("Open Placeholders", placeholder_count == 0, f"{placeholder_count} placeholder marker(s)"))
    ok, detail = vietnamese_diacritics_status(text)
    checks.append(make_check("Vietnamese Diacritics", ok, detail))
    checks.append(make_check("BRD Completed", any("brd" in name.lower() for name in ctx), "BRD file present in bundle"))
    checks.append(make_check("Architecture Diagram", mermaid_count >= 1 and has_any(text, "kiến trúc", "architecture"), f"{mermaid_count} mermaid block(s)"))
    checks.append(make_check("ER Diagram / Data Model", has_any(text, "erd", "entity", "data dictionary", "data model"), "data model markers"))
    checks.append(make_check("Use Case / Actor Coverage", actor_rows >= 2 or has_any(text, "use case", "actor"), f"{actor_rows} actor rows"))
    checks.append(make_check("State Machine", has_any(text, "state", "trạng thái", "stateDiagram"), "state-machine markers"))
    checks.append(make_check("Data Dictionary", has_any(text, "field", "type", "data dictionary", "entity"), "dictionary markers"))
    checks.append(make_check("API Conventions", has_any(text, "api", "endpoint", "base url", "auth"), "API markers"))
    checks.append(make_check("Validation Rules", has_any(text, "validation", "regex", "enum", "VR-"), "validation markers"))
    checks.append(make_check("NFR Coverage", nfr_count >= 5, f"{nfr_count} NFR IDs"))
    checks.append(make_check("Sequence Diagram", has_any(text, "sequence", "sequenceDiagram", "luồng chính"), "sequence markers"))
    checks.append(make_check("Decomposition Pattern", has_any(text, "module", "tính năng", "feature"), f"{fr_count} FR IDs"))
    checks.append(make_check("Requirement Quality Gate", bool(rubric.get("passed")), f"avg score {rubric.get('avg_score', 0)}"))
    conflict_hits = sum(1 for req in rubric.get("requirements", []) if "Compound Requirement" in req["smells"])
    checks.append(make_check("Conflict Scan", conflict_hits == 0, f"{conflict_hits} compound/conflict smell(s)"))
    ok, detail = numbering_status(text, "srs")
    checks.append(make_check("Sequential Numbering", ok, detail))
    return checks


def story_checks(text: str, ctx: Dict[str, str]) -> List[Dict[str, str]]:
    checks: List[Dict[str, str]] = []
    placeholder_count = count_placeholders(text)
    story_count = count_ids(text, ("US",))
    br_count = sum(count_ids(content, ("BRQ", "BRD", "BR-")) for name, content in ctx.items() if "brd" in name.lower())
    gwt_count = len(re.findall(r"\b(Given|When|Then)\b", text, re.IGNORECASE))

    checks.append(make_check("Open Placeholders", placeholder_count == 0, f"{placeholder_count} placeholder marker(s)"))
    ok, detail = vietnamese_diacritics_status(text)
    checks.append(make_check("Vietnamese Diacritics", ok, detail))
    checks.append(make_check("BRQ Coverage", story_count >= 1 and br_count >= 1, f"{story_count} stories vs {br_count} business IDs"))
    checks.append(make_check("INVEST Format", has_any(text, "As a", "I want", "So that"), "story sentence markers"))
    checks.append(make_check("BDD Acceptance Criteria", gwt_count >= 3, f"{gwt_count} GWT marker(s)"))
    checks.append(make_check("Happy Path + Edge Case", has_any(text, "happy", "negative", "exception", "boundary"), "coverage markers"))
    checks.append(make_check("Sprint Assignment", has_any(text, "Sprint", "S1", "release"), "sprint/release markers"))
    checks.append(make_check("Traceability Table", has_any(text, "traceability", "mapping", "brd", "fr-", "tc-"), "traceability markers"))
    checks.append(make_check("AC Coverage Types", sum(has_any(text, token) for token in ("happy", "negative", "boundary", "permission", "concurrency")) >= 3, "multi-type AC markers"))
    ok, detail = numbering_status(text, "story")
    checks.append(make_check("Sequential Numbering", ok, detail))
    return checks


def uat_checks(text: str, ctx: Dict[str, str]) -> List[Dict[str, str]]:
    checks: List[Dict[str, str]] = []
    placeholder_count = count_placeholders(text)
    tc_count = count_ids(text, ("AC", "TC", "UAT"))
    business_refs = len(re.findall(r"\b(BR-|BRD-\d{3}|FR-\d{3}|FR-[A-Z]{2,10}-\d{3})\b", text))
    signoff_rows = count_table_rows(text, ("điều kiện kết thúc", "sign-off", "biên bản nghiệm thu"))

    checks.append(make_check("Open Placeholders", placeholder_count == 0, f"{placeholder_count} placeholder marker(s)"))
    ok, detail = vietnamese_diacritics_status(text)
    checks.append(make_check("Vietnamese Diacritics", ok, detail))
    checks.append(make_check("Story Coverage", tc_count >= 1 and any("story" in name.lower() for name in ctx), f"{tc_count} AC/test-case IDs"))
    checks.append(make_check("Test Data Spec", has_any(text, "test data", "dữ liệu kiểm thử", "test accounts"), "test-data markers"))
    checks.append(make_check("Pre-requisites", has_any(text, "điều kiện bắt đầu", "pre-requisite", "môi trường", "environment"), "pre-req markers"))
    checks.append(make_check("Sign-off Criteria", signoff_rows >= 1 or has_any(text, "nghiệm thu", "sign-off"), f"{signoff_rows} sign-off table block(s)"))
    checks.append(make_check("Business Rule TCs", business_refs >= 3, f"{business_refs} business/FR reference(s)"))
    ok, detail = numbering_status(text, "uat")
    checks.append(make_check("Sequential Numbering", ok, detail))
    return checks


CHECKERS = {
    "brd": ("PFC-BRD", brd_checks),
    "srs": ("PFC-SRS", srs_checks),
    "story": ("PFC-USM", story_checks),
    "uat": ("PFC-UAT", uat_checks),
}


def evaluate_bundle(target: Path) -> Dict[str, object]:
    docs = {path.name: read_text(path) for path in collect_markdown_files(target)}
    results = []
    total_pass = total_fail = total_na = 0
    for name, text in docs.items():
        role = classify_file(Path(name))
        if role not in CHECKERS:
            continue
        label, checker = CHECKERS[role]
        checks = checker(text, docs)
        pass_count = sum(1 for item in checks if item["status_code"] == PASS_CODE)
        fail_count = sum(1 for item in checks if item["status_code"] == FAIL_CODE)
        na_count = sum(1 for item in checks if item["status_code"] == NA_CODE)
        total_pass += pass_count
        total_fail += fail_count
        total_na += na_count
        status = "PASS" if fail_count == 0 else ("WARN" if fail_count <= 2 else "FAIL")
        results.append(
            {
                "file": name,
                "checklist": label,
                "doc_type": role,
                "status": status,
                "summary": {"pass": pass_count, "fail": fail_count, "na": na_count},
                "checks": checks,
            }
        )
    return {
        "target": str(target),
        "summary": {"pass": total_pass, "fail": total_fail, "na": total_na},
        "documents": results,
    }


def evaluate_path(target: Path) -> Dict[str, object]:
    """Backward-compatible alias for earlier tests and scripts."""
    return evaluate_bundle(target)


def print_markdown(report: Dict[str, object]) -> None:
    for doc in report["documents"]:
        print(f"\n### 🛫 Pre-Flight: {doc['file']} ({doc['checklist']})\n")
        print("| Item | Status | Detail |")
        print("|---|---|---|")
        for item in doc["checks"]:
            print(f"| {item['item']} | {item['status']} | {item['detail']} |")
        s = doc["summary"]
        print(f"\n**Result:** {s['pass']} PASS / {s['fail']} FAIL / {s['na']} N/A | **Status:** {doc['status']}")
    summary = report["summary"]
    print(f"\n{'=' * 60}\nTOTAL: {summary['pass']} PASS | {summary['fail']} FAIL | {summary['na']} N/A\n{'=' * 60}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run BA pre-flight checks on markdown artifact bundles.")
    parser.add_argument("target", help="Folder containing markdown docs")
    parser.add_argument("--output-json", help="Write JSON report")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.is_dir():
        print(f"ERROR: {target} is not a folder")
        return 1

    report = evaluate_bundle(target)
    print_markdown(report)

    if args.output_json:
        Path(args.output_json).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    return 1 if report["summary"]["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
