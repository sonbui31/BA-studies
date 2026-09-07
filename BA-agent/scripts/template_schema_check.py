#!/usr/bin/env python3
"""Validate core curated BA templates against the canonical schema contract."""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "Curated templates"


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


TEMPLATE_SCHEMAS: Dict[str, Dict[str, object]] = {
    "01-BRD-Template.md": {
        "sections": [
            "## 1.1 Thông tin chung",
            "## 1.2 Bối cảnh & Mục tiêu kinh doanh",
            "## 1.3 Phạm vi",
            "## 1.4 Stakeholders",
            "## 1.5 Mục tiêu nghiệp vụ",
            "## 1.6 Yêu cầu nghiệp vụ chi tiết",
            "## 1.7 Luật nghiệp vụ",
            "## 1.8 Quy trình nghiệp vụ",
            "## 1.9 Ràng buộc & Giả định",
            "## 1.10 Rủi ro & Giải pháp",
            "## 1.11 Tiêu chí thành công",
            "## 1.12 Ma trận truy vết",
            "## 1.13 Từ điển thuật ngữ",
        ],
        "must_include": ["BRQ-01", "BR-001", "FR-MOD-001", "AC-MOD-001"],
        "must_not_include": [r"\bBRULE-\d+", r"\bSR-\d+"],
    },
    "02-SRS-Template.md": {
        "sections": [
            "## 2.0 Thông tin chung",
            "## 2.1 Giới thiệu",
            "## 2.2 Mô tả tổng quan",
            "## 2.3 Yêu cầu chức năng",
            "## 2.4 Yêu cầu chức năng xuyên suốt",
            "## 2.5 Yêu cầu phi chức năng",
            "## 2.6 Mô hình dữ liệu",
            "## 2.7 Đặc tả giao diện ngoài",
            "## 2.8 Đặc tả API",
            "## 2.9 Giao diện người dùng",
            "## 2.10 Ma trận truy xuất",
        ],
        "must_include": ["FR-MODA-001", "NFR", "BRQ-01", "AC-MODA-001"],
        "must_not_include": [r"\bBRULE-\d+", r"\bSR-\d+", r"\bFR-[A-Z]\d{2}\b"],
    },
    "03-User-Story-Template.md": {
        "sections": [
            "## 3.0 Thông tin chung",
            "## 3.1 Sprint Roadmap",
            "## 3.2 Bảng tổng hợp User Stories",
            "## 3.3 Template User Story Chuẩn",
            "## 3.4 Ví dụ thực chiến",
        ],
        "must_include": ["US-AUTH-001", "FR-AUTH-001", "AC-MODULE-001", "Definition of Done"],
        "must_not_include": [r"\bBRULE-\d+", r"\bUS-\d{2,3}\b"],
    },
    "04-Acceptance-Criteria-Template.md": {
        "sections": [
            "## 4.0 Thông tin chung",
            "## 4.1 Ma trận truy xuất",
            "## 4.2 Template Chuẩn",
            "## 4.3 Kịch bản bổ sung",
            "## 4.4 Checklist nghiệm thu nhanh",
            "## 4.5 Ví dụ thực chiến",
        ],
        "must_include": ["AC-AUTH-001", "US-AUTH-001", "FR-AUTH-001", "BR-004"],
        "must_not_include": [r"\bBRULE-\d+", r"\bAC-\d{2,3}\b"],
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def table_separator_errors(text: str) -> List[str]:
    errors: List[str] = []
    lines = text.splitlines()
    for index, line in enumerate(lines[:-1], start=1):
        if not line.lstrip().startswith("|"):
            continue
        separator = lines[index].strip()
        if not separator.startswith("|") or "---" not in separator:
            continue
        header_cols = len([cell for cell in line.strip().strip("|").split("|")])
        separator_cols = len([cell for cell in separator.strip().strip("|").split("|")])
        if header_cols != separator_cols:
            errors.append(
                f"line {index}: table header has {header_cols} columns but separator has {separator_cols}"
            )
    return errors


def evaluate_template(path: Path, schema: Dict[str, object]) -> Dict[str, object]:
    errors: List[str] = []
    text = read_text(path)

    for section in schema.get("sections", []):
        if section not in text:
            errors.append(f"Missing section: {section}")
    for token in schema.get("must_include", []):
        if str(token) not in text:
            errors.append(f"Missing required marker: {token}")
    for pattern in schema.get("must_not_include", []):
        if re.search(str(pattern), text):
            errors.append(f"Forbidden legacy marker found: {pattern}")
    errors.extend(table_separator_errors(text))

    return {
        "file": str(path),
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
    }


def evaluate_templates(root: Path = CURATED) -> Dict[str, object]:
    reports = []
    for name, schema in TEMPLATE_SCHEMAS.items():
        path = root / name
        if not path.exists():
            reports.append({"file": str(path), "status": "FAIL", "errors": ["Missing template file"]})
            continue
        reports.append(evaluate_template(path, schema))
    return {
        "target": str(root),
        "summary": {
            "pass": sum(1 for report in reports if report["status"] == "PASS"),
            "fail": sum(1 for report in reports if report["status"] == "FAIL"),
        },
        "templates": reports,
    }


def print_markdown(report: Dict[str, object]) -> None:
    print("# TEMPLATE SCHEMA CHECK")
    print(f"> Target: `{report['target']}`\n")
    print("| Template | Status | Errors |")
    print("|---|---|---|")
    for item in report["templates"]:
        errors = "<br>".join(item["errors"]) if item["errors"] else "---"
        print(f"| {Path(str(item['file'])).name} | {item['status']} | {errors} |")
    summary = report["summary"]
    print(f"\nTOTAL: {summary['pass']} PASS | {summary['fail']} FAIL")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate core BA curated template schema.")
    parser.add_argument("target", nargs="?", default=str(CURATED), help="Curated templates folder")
    parser.add_argument("--output-json", help="Write JSON report")
    args = parser.parse_args()

    report = evaluate_templates(Path(args.target).resolve())
    print_markdown(report)
    if args.output_json:
        Path(args.output_json).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return 1 if report["summary"]["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
