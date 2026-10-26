#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


SCENARIOS = {
    "outsource": {
        "threshold": 0.82,
        "checks": {
            "stakeholders": ["stakeholder", "raci", "owner", "approver", "người phê duyệt"],
            "scope": ["scope", "in scope", "out of scope", "phạm vi"],
            "assumptions_constraints": ["assumption", "constraint", "giả định", "ràng buộc"],
            "change_control": ["change request", "cr", "change control", "quản lý thay đổi"],
            "uat_acceptance": ["uat", "acceptance", "sign-off", "nghiệm thu", "tiêu chí chấp nhận"],
            "traceability": ["traceability", "rtm", "brq", "fr-", "us-", "tc-", "truy vết"],
            "handover": ["handover", "knowledge transfer", "kt", "warranty", "bàn giao"],
        },
    },
    "product": {
        "threshold": 0.78,
        "checks": {
            "problem_users": ["problem", "user", "persona", "pain point", "người dùng"],
            "outcomes_metrics": ["metric", "kpi", "okr", "success measure", "chỉ số"],
            "scope_mvp": ["mvp", "scope", "release", "roadmap", "phạm vi"],
            "backlog": ["backlog", "user story", "acceptance criteria", "ưu tiên"],
            "analytics": ["event", "tracking", "analytics", "funnel", "dashboard"],
            "experiment_risk": ["hypothesis", "experiment", "risk", "assumption", "giả định"],
        },
    },
    "fintech": {
        "threshold": 0.84,
        "checks": {
            "regulatory": ["regulatory", "compliance", "aml", "kyc", "quy định"],
            "money_movement": ["payment", "settlement", "reconciliation", "transaction", "giao dịch"],
            "security": ["security", "authentication", "authorization", "fraud", "bảo mật"],
            "audit": ["audit", "log", "evidence", "trace", "kiểm toán"],
            "nfr": ["nfr", "availability", "latency", "sla", "performance"],
            "exception_handling": ["exception", "rollback", "timeout", "retry", "ngoại lệ"],
            "uat_traceability": ["uat", "traceability", "rtm", "acceptance", "nghiệm thu"],
        },
    },
    "healthcare": {
        "threshold": 0.84,
        "checks": {
            "clinical_workflow": ["clinical workflow", "quy trình lâm sàng", "clinician", "bác sĩ", "điều dưỡng"],
            "privacy_consent": ["phi", "pii", "consent", "đồng ý", "privacy", "quyền riêng tư"],
            "standards": ["hl7", "fhir", "icd", "dicom"],
            "access_audit": ["audit", "access control", "phân quyền", "encryption", "mã hóa"],
            "clinical_validation": ["clinical validation", "patient safety", "an toàn người bệnh", "thẩm định lâm sàng"],
            "integration": ["his", "emr", "ehr", "lis", "pacs", "integration", "tích hợp"],
            "uat_traceability": ["uat", "traceability", "rtm", "acceptance", "nghiệm thu"],
        },
    },
    "government": {
        "threshold": 0.84,
        "checks": {
            "procurement": ["procurement", "bidding", "đấu thầu", "hồ sơ mời thầu", "mua sắm"],
            "regulatory": ["regulatory", "compliance", "nghị định", "thông tư", "quy định"],
            "multi_level_acceptance": ["multi-level", "nhiều cấp", "hội đồng nghiệm thu", "acceptance", "nghiệm thu"],
            "security_classification": ["security classification", "phân loại bảo mật", "cấp độ", "an toàn thông tin", "security"],
            "approval_chain": ["approval", "phê duyệt", "sign-off", "ký duyệt", "văn bản"],
            "traceability": ["traceability", "rtm", "brq", "fr-", "truy vết"],
            "data_retention": ["retention", "lưu trữ", "archive", "audit", "kiểm toán"],
        },
    },
    "startup-mvp": {
        "threshold": 0.75,
        "checks": {
            "problem": ["problem", "pain point", "vấn đề", "người dùng"],
            "hypothesis": ["hypothesis", "assumption", "giả thuyết", "giả định"],
            "mvp_scope": ["mvp", "in scope", "out of scope", "phạm vi"],
            "metrics": ["metric", "kpi", "okr", "retention", "conversion", "chỉ số"],
            "constraints": ["budget", "timeline", "deadline", "ngân sách", "thời hạn"],
            "backlog_ac": ["backlog", "user story", "acceptance criteria", "tiêu chí chấp nhận"],
        },
    },
    "inhouse": {
        "threshold": 0.78,
        "checks": {
            "stakeholders": ["stakeholder", "phòng ban", "department", "owner", "raci"],
            "process": ["as-is", "to-be", "quy trình", "process"],
            "adoption_training": ["adoption", "training", "đào tạo", "change management"],
            "operational_readiness": ["operational readiness", "go-live", "support", "vận hành", "rollback"],
            "governance": ["governance", "approval", "phê duyệt", "change request"],
            "acceptance": ["uat", "acceptance", "nghiệm thu", "tiêu chí chấp nhận"],
        },
    },
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def term_in_text(needle: str, lowered: str) -> bool:
    """Match short tokens (cr, kt, kyc, aml, sla, his...) on word boundaries so that "description" does not satisfy "cr"."""
    needle = needle.lower()
    if len(needle) > 4 and not needle.endswith("-"):
        return needle in lowered
    pattern = r"(?<![0-9a-zà-ỹ])" + re.escape(needle)
    if not needle.endswith("-"):
        pattern += r"(?![0-9a-zà-ỹ])"
    return re.search(pattern, lowered) is not None


def evaluate_text(text: str, scenario: str) -> Dict[str, object]:
    if scenario not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario}")
    profile = SCENARIOS[scenario]
    lowered = normalize(text)
    checks: List[Dict[str, object]] = []
    passed_count = 0
    for check_id, needles in profile["checks"].items():
        matched = [needle for needle in needles if term_in_text(needle, lowered)]
        passed = bool(matched)
        passed_count += 1 if passed else 0
        checks.append(
            {
                "id": check_id,
                "status": "PASS" if passed else "FAIL",
                "matched_terms": matched,
                "expected_terms": needles,
            }
        )
    score = passed_count / max(1, len(checks))
    threshold = float(profile["threshold"])
    return {
        "scenario": scenario,
        "score": round(score, 4),
        "threshold": threshold,
        "passed": score >= threshold,
        "checks": checks,
    }


def format_markdown(payload: Dict[str, object]) -> str:
    status = "PASS" if payload["passed"] else "FAIL"
    lines = [
        f"# BA Response Evaluation: {payload['scenario']}",
        "",
        f"Status: {status}",
        f"Score: {payload['score']} / threshold {payload['threshold']}",
        "",
        "| Check | Status | Matched terms |",
        "|---|---|---|",
    ]
    for item in payload["checks"]:
        matched = ", ".join(item["matched_terms"]) if item["matched_terms"] else "-"
        lines.append(f"| {item['id']} | {item['status']} | {matched} |")
    return "\n".join(lines)


def read_input(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate whether a BA answer/artifact covers scenario-specific controls.")
    parser.add_argument("target", help="Markdown/text file to evaluate, or '-' for stdin")
    parser.add_argument("--scenario", choices=sorted(SCENARIOS), required=True)
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    try:
        payload = evaluate_text(read_input(args.target), args.scenario)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.format == "markdown":
        print(format_markdown(payload))
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
