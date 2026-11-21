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
        definition_ids,
        duplicate_definitions,
        find_project_scheme,
        is_primary,
        load_project_scheme,
        set_project_scheme,
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
        definition_ids,
        duplicate_definitions,
        find_project_scheme,
        is_primary,
        load_project_scheme,
        set_project_scheme,
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


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


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


NEGATION_PATTERN = re.compile(
    r"(không có|chưa có|không cần|chưa cần|chưa xác định|chưa làm rõ|không áp dụng|\bn/a\b|\btbd\b|\bnone\b|\bno\b|\bnot\b|\bwithout\b)",
    re.IGNORECASE,
)


def _token_pattern(token: str, case_sensitive: bool = False) -> "re.Pattern[str]":
    flags = 0 if case_sensitive else re.IGNORECASE
    return re.compile(r"(?<![\w])" + re.escape(token) + r"(?![\w])", flags)


def has_any(text: str, *tokens: str, case_sensitive: bool = False) -> bool:
    """True when a token appears as a whole word on a line that does not negate it.

    "Không có glossary" or "Chưa có hiện trạng" do not count as evidence. Fenced code is ignored.
    """
    patterns = [_token_pattern(token, case_sensitive) for token in tokens]
    for _, line in iter_non_fenced_lines(text):
        for pattern in patterns:
            match = pattern.search(line)
            if not match:
                continue
            before = line[: match.start()]
            if NEGATION_PATTERN.search(before[-40:]):
                continue
            return True
    return False


def has_heading(text: str, *tokens: str) -> bool:
    """True when a markdown heading names the section (stronger evidence than a word in prose)."""
    patterns = [_token_pattern(token) for token in tokens]
    for _, line in iter_non_fenced_lines(text):
        if line.lstrip().startswith("#") and any(pattern.search(line) for pattern in patterns):
            return True
    return False


def count_in_table_rows(text: str, tokens: tuple, case_sensitive: bool = True) -> int:
    patterns = [_token_pattern(token, case_sensitive) for token in tokens]
    total = 0
    for _, line in iter_non_fenced_lines(text):
        if line.lstrip().startswith("|"):
            total += sum(len(pattern.findall(line)) for pattern in patterns)
    return total


AI_MARKERS = ("AI", "ML", "LLM", "OCR", "NLP", "GenAI")
AI_MARKERS_CI = ("machine learning", "trí tuệ nhân tạo", "học máy", "recommendation engine", "mô hình dự đoán")


OUT_OF_SCOPE_HEADING = re.compile(r"(ngoài phạm vi|out of scope|chưa làm|won't|không làm|không thuộc phạm vi)", re.IGNORECASE)


def in_scope_text(text: str) -> str:
    """Drop sections whose heading marks them as out of scope."""
    kept = []
    skipping_level = 0
    for _, line in iter_non_fenced_lines(text):
        heading = re.match(r"^(#{1,6})\s", line)
        if heading:
            level = len(heading.group(1))
            if skipping_level and level <= skipping_level:
                skipping_level = 0
            if not skipping_level and OUT_OF_SCOPE_HEADING.search(line):
                skipping_level = level
                continue
        if not skipping_level:
            kept.append(line)
    return "\n".join(kept)


def mentions_ai(text: str) -> bool:
    # Case-sensitive: the Vietnamese pronoun "ai" (who) must not trigger the AI checklist.
    scoped = in_scope_text(text)
    return has_any(scoped, *AI_MARKERS, case_sensitive=True) or has_any(scoped, *AI_MARKERS_CI)


# Labels the skill requires authors to write; they are status markers, not unfilled placeholders.
ALLOWED_LABELS = (
    "ai-drafted", "cần xác nhận", "giả định", "chưa có thông tin", "dự thảo", "chưa duyệt",
    "lối agile lite", "đã bỏ qua theo yêu cầu user", "tài liệu mẫu", "chưa có baseline", "ví dụ giả định",
)


INLINE_CODE = re.compile(r"`[^`\n]*`")


def count_placeholders(text: str) -> int:
    ignored = {"[x]", "[ ]", "[*]"}
    count = 0
    for _, line in iter_non_fenced_lines(text):
        if line.lstrip().startswith(("- [ ]", "- [x]", "- [X]")):
            continue
        # Inline code is literal: "Auth: `[ADMIN, KTTS]`", a regex "`[0-9a-f]{8}`", a URL "`{domain}`".
        line = INLINE_CODE.sub("", line)
        for match in PLACEHOLDER_PATTERN.finditer(line):
            token = match.group(0)
            if token.lower() in ignored:
                continue
            if line[match.end():match.end() + 1] in ("(", "["):
                continue  # markdown link text
            inner = token.strip("[]{}$_ ").lower()
            if any(inner.startswith(label) for label in ALLOWED_LABELS):
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


SOURCE_ID = re.compile(r"\bSRC-(?:\d{2,3}|CHAT)\b")


def document_tier(text: str):
    """Tier written in the document header ("Tier: 2 ..."), or None."""
    for _, line in list(iter_non_fenced_lines(text))[:25]:
        match = re.search(r"Tier\W{0,4}\s*([123])\b", line)
        if match:
            return int(match.group(1))
    return None


def evidence_sources_check(text: str) -> Dict[str, str]:
    """BRD facts must name their sources (core/evidence-source-gate.md).

    Tier 1: a "Nguồn" column or SRC references. Tier 2-3: a Source Register (table rows starting
    with SRC-xx) and facts that cite those sources outside the register.
    """
    tier = document_tier(text)
    if tier is None:
        return make_na("Evidence Sources", "no Tier in document header")
    register_rows = 0
    citations = 0
    has_source_column = False
    for _, line in iter_non_fenced_lines(text):
        stripped = line.strip()
        if stripped.startswith("|"):
            first = stripped.strip("|").split("|")[0].strip()
            if SOURCE_ID.fullmatch(first):
                register_rows += 1
                continue
            if re.search(r"\|\s*Nguồn\b|\|\s*Source\b", stripped, re.IGNORECASE):
                has_source_column = True
        citations += len(SOURCE_ID.findall(stripped))
    if tier == 1:
        ok = has_source_column or citations > 0
        return make_check("Evidence Sources", ok, f"Tier 1: source column={has_source_column}, {citations} citation(s)")
    ok = register_rows >= 1 and citations >= register_rows
    return make_check(
        "Evidence Sources",
        ok,
        f"Tier {tier}: {register_rows} source register row(s), {citations} citation(s) outside the register",
    )


BASELINE_STATUS = re.compile(r"Trạng thái\W{0,6}\s*(?:baseline|approved|đã phê duyệt|đã chốt|đã ký)", re.IGNORECASE)
VERSION_ROW_APPROVED = re.compile(r"^\|\s*v?\d+(?:\.\d+)+\s*\|.*(?:đã phê duyệt|chốt phạm vi|approved|baseline)", re.IGNORECASE)
SIGNOFF_HEADING = re.compile(r"^#{1,6}\s.*(?:phê duyệt|ký duyệt|sign-?off|chữ ký|xác nhận nghiệm thu)", re.IGNORECASE)
DATE_PATTERN = re.compile(r"\b\d{1,2}/\d{1,2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b")


def claims_baseline(text: str) -> bool:
    """The document says it is approved: a status line in the header, or a version-history row
    recording approval with someone in the approver column."""
    lines = [line for _, line in iter_non_fenced_lines(text)]
    if any(BASELINE_STATUS.search(line) for line in lines[:25]):
        return True
    for line in lines:
        if VERSION_ROW_APPROVED.match(line.strip()):
            cells = [cell.strip(" *") for cell in line.strip().strip("|").split("|")]
            if cells and cells[-1] not in {"", "—", "-", "–"}:
                return True
    return False


def signed_rows(text: str) -> int:
    """Rows of a sign-off table (under a Phê duyệt / Sign-off heading) that carry a date."""
    count = 0
    in_signoff = False
    for _, line in iter_non_fenced_lines(text):
        stripped = line.strip()
        if stripped.startswith("#"):
            in_signoff = bool(SIGNOFF_HEADING.match(stripped))
            continue
        if in_signoff and stripped.startswith("|") and DATE_PATTERN.search(stripped):
            count += 1
    return count


def human_signoff_check(text: str) -> Dict[str, str]:
    """core/human-accountability.md H5: a document that claims baseline needs a filled sign-off."""
    if not claims_baseline(text):
        return make_na("Human Sign-off", "document does not claim baseline/approval")
    rows = signed_rows(text)
    open_items = text.count("[CẦN XÁC NHẬN")
    problems = []
    if rows == 0:
        problems.append("claims baseline but the sign-off table has no row with a name and date")
    if open_items:
        problems.append(f"{open_items} [CẦN XÁC NHẬN] still open")
    return make_check("Human Sign-off", not problems, "; ".join(problems) or f"{rows} signed row(s)")


def definition_ids_for_role(text: str, role: str):
    """IDs minted by this document (skip checks): matrix rows only count in the family's own document."""
    return [item.meta for item in definition_ids(text, role) if is_primary(item, role)]


def numbering_status(text: str, role: str) -> Tuple[bool, str]:
    heading_issues = heading_gaps(extract_headings(text))
    duplicates = duplicate_definitions(item for item in definition_ids(text, role) if is_primary(item, role))
    _, skips = sequence_gaps(definition_ids_for_role(text, role))
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
    success_rows = count_table_rows(
        text, ("tiêu chí thành công", "success metrics", "mục tiêu dự án", "chỉ tiêu", "okr", "kpi")
    )
    rule_rows = max(
        count_table_rows(text, ("quy tắc nghiệp vụ", "business rules")),
        len(re.findall(r"\b(QT|BR)-\d+", text)),
    )

    checks.append(make_check("Open Placeholders", placeholder_count == 0, f"{placeholder_count} placeholder marker(s)"))
    ok, detail = vietnamese_diacritics_status(text)
    checks.append(make_check("Vietnamese Diacritics", ok, detail))
    checks.append(make_check("Glossary", has_heading(text, "thuật ngữ", "glossary", "từ điển thuật ngữ"), "glossary section heading"))
    checks.append(make_check("Problem Statement", pain_rows >= 2 or text.count("Rủi ro #") >= 2, f"{pain_rows} problem rows"))
    checks.append(make_check("Stakeholder Map", stakeholder_rows >= 3, f"{stakeholder_rows} stakeholder rows"))
    kpi_lines = sum(
        1
        for _, line in iter_non_fenced_lines(text)
        if re.search(r"(?<![\w])(okrs?|kpis?|chỉ số)(?![\w])", line, re.IGNORECASE) and re.search(r"\d", line)
    )
    checks.append(make_check("OKRs / Success Metrics", success_rows >= 2 or kpi_lines >= 2, f"{success_rows} metric rows / {kpi_lines} KPI lines with numbers"))
    priority_markers = count_in_table_rows(
        text, ("Must", "Should", "Could", "Won't", "Must have", "Bắt buộc", "Nên có", "Có thể có", "Chưa làm")
    )
    moscow_headings = sum(
        1
        for token in ("Must", "Should", "Could", "Won't")
        if any(line.lstrip().startswith("#") and _token_pattern(token, True).search(line) for _, line in iter_non_fenced_lines(text))
    )
    checks.append(
        make_check(
            "MoSCoW Priority",
            priority_markers >= 4 or moscow_headings >= 3,
            f"{priority_markers} priority value(s) in tables / {moscow_headings} MoSCoW heading(s)",
        )
    )
    checks.append(make_check("Business Rules", rule_rows >= 1, f"{rule_rows} rule markers"))
    checks.append(make_check("Assumptions & Constraints", assumption_rows >= 1 and constraint_rows >= 1, f"{assumption_rows} assumptions / {constraint_rows} constraints"))
    checks.append(make_check("Traceability Matrix", has_heading(text, "ma trận truy vết", "traceability", "rtm", "truy xuất"), "traceability section heading"))
    checks.append(make_check("As-Is Process", has_heading(text, "as-is", "hiện trạng", "quy trình hiện tại"), "current-state section heading"))
    checks.append(make_check("Elicitation Record", has_any(text, "phỏng vấn", "interview", "workshop", "khảo sát", "quan sát"), "elicitation evidence"))
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
    if mentions_ai(text):
        checks.append(make_check("AI Feature Spec", has_any(text, "accuracy", "confidence", "false positive", "human-in-the-loop"), "AI control markers"))
    else:
        checks.append(make_na("AI Feature Spec", "no AI/ML markers"))
    checks.append(evidence_sources_check(text))
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
    checks.append(make_check("BRD Completed", any(classify_file(Path(name)) == "brd" for name in ctx), "BRD file present in bundle"))
    checks.append(make_check("Architecture Diagram", mermaid_count >= 1 and has_any(text, "kiến trúc", "architecture"), f"{mermaid_count} mermaid block(s)"))
    checks.append(make_check("ER Diagram / Data Model", "erDiagram" in text or has_any(text, "erd", "data model", "mô hình dữ liệu"), "data model markers"))
    checks.append(make_check("Use Case / Actor Coverage", actor_rows >= 2 or has_any(text, "use case", "actor"), f"{actor_rows} actor rows"))
    checks.append(make_check("State Machine", "stateDiagram" in text or has_any(text, "state machine", "máy trạng thái", "chuyển trạng thái"), "state-machine markers"))
    dictionary_terms = ("data dictionary", "từ điển dữ liệu", "kiểu dữ liệu", "data type")
    data_model_docs = [content for name, content in ctx.items() if re.search(r"data[-_ ]?model|mô-hình-dữ-liệu", name, re.IGNORECASE)]
    has_dictionary = has_any(text, *dictionary_terms) or any(has_any(doc, *dictionary_terms) for doc in data_model_docs)
    checks.append(make_check("Data Dictionary", has_dictionary, "dictionary markers in SRS or Data Model document"))
    checks.append(make_check("API Conventions", has_any(text, "API", "endpoint", "base url", case_sensitive=False), "API markers"))
    checks.append(
        make_check(
            "Validation Rules",
            has_any(text, "validation", "regex", "enum", "VR", "kiểm tra hợp lệ", "quy tắc kiểm tra", "bắt buộc nhập", "định dạng", "độ dài tối đa", "không hợp lệ"),
            "validation markers",
        )
    )
    checks.append(make_check("NFR Coverage", nfr_count >= 5, f"{nfr_count} NFR IDs"))
    checks.append(make_check("Sequence Diagram", "sequenceDiagram" in text or has_any(text, "sequence diagram", "sơ đồ tuần tự"), "sequence markers"))
    checks.append(make_check("Decomposition Pattern", has_any(text, "module", "tính năng", "feature"), f"{fr_count} FR IDs"))
    checks.append(make_check("Requirement Quality Gate", bool(rubric.get("passed")), f"avg score {rubric.get('avg_score', 0)}"))
    compound_hits = sum(1 for req in rubric.get("requirements", []) if "Compound Requirement" in req["smells"])
    checks.append(make_check("Compound Requirement Scan", compound_hits == 0, f"{compound_hits} compound requirement(s)"))
    ok, detail = numbering_status(text, "srs")
    checks.append(make_check("Sequential Numbering", ok, detail))
    return checks


def story_checks(text: str, ctx: Dict[str, str]) -> List[Dict[str, str]]:
    checks: List[Dict[str, str]] = []
    placeholder_count = count_placeholders(text)
    story_count = count_ids(text, ("US",))
    br_count = sum(count_ids(content, ("BRQ", "BRD", "BR-")) for name, content in ctx.items() if classify_file(Path(name)) == "brd")
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
    checks.append(make_check("Test Data Spec", has_any(text, "test data", "dữ liệu kiểm thử", "dữ liệu thử", "test accounts", "tài khoản thử"), "test-data markers"))
    checks.append(make_check("Pre-requisites", has_any(text, "điều kiện bắt đầu", "pre-requisite", "môi trường", "environment", "entry criteria", "điều kiện vào"), "pre-req markers"))
    checks.append(make_check("Sign-off Criteria", signoff_rows >= 1 or has_any(text, "nghiệm thu", "sign-off", "exit criteria", "điều kiện kết thúc"), f"{signoff_rows} sign-off table block(s)"))
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


def evaluate_bundle(target: Path, config: Path = None) -> Dict[str, object]:
    scheme_path = config or find_project_scheme(target)
    set_project_scheme(load_project_scheme(scheme_path) if scheme_path else None)
    docs = {path.name: read_text(path) for path in collect_markdown_files(target)}
    results = []
    total_pass = total_fail = total_na = 0
    for name, text in docs.items():
        role = classify_file(Path(name))
        if role not in CHECKERS:
            continue
        label, checker = CHECKERS[role]
        checks = checker(text, docs)
        checks.append(human_signoff_check(text))
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
    errors = []
    if not results:
        total_fail += 1
        errors.append(
            "Không tìm thấy tài liệu BRD/SRS/Story/UAT nào (tên file cần chứa brd, srs, story, uat, acceptance...)."
        )
    return {
        "target": str(target),
        "summary": {"pass": total_pass, "fail": total_fail, "na": total_na},
        "documents": results,
        "errors": errors,
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
    for error in report.get("errors", []):
        print(f"\n❌ {error}")
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
