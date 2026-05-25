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
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def evaluate_text(text: str, scenario: str) -> Dict[str, object]:
    if scenario not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario}")
    profile = SCENARIOS[scenario]
    lowered = normalize(text)
    checks: List[Dict[str, object]] = []
    passed_count = 0
    for check_id, needles in profile["checks"].items():
        matched = [needle for needle in needles if needle.lower() in lowered]
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
