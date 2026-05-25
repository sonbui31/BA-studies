#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parents[0]
DEFAULT_CASES = ROOT / "tests" / "golden" / "ba_response_cases.jsonl"

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import ba_response_eval  # noqa: E402


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def load_cases(path: Path) -> List[Dict[str, object]]:
    cases = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            cases.append(json.loads(line))
    return cases


def evaluate_case(case: Dict[str, object]) -> Dict[str, object]:
    case_type = case.get("type")
    if case_type != "response_eval":
        return {
            "id": case.get("id"),
            "passed": False,
            "error": f"Unsupported case type: {case_type}",
        }
    payload = ba_response_eval.evaluate_text(str(case.get("text", "")), str(case.get("scenario")))
    expected = bool(case.get("expected_pass"))
    actual = bool(payload["passed"])
    return {
        "id": case.get("id"),
        "type": case_type,
        "scenario": case.get("scenario"),
        "expected_pass": expected,
        "actual_pass": actual,
        "score": payload["score"],
        "passed": expected == actual,
        "failed_checks": [item["id"] for item in payload["checks"] if item["status"] != "PASS"],
    }


def evaluate_cases(path: Path) -> Dict[str, object]:
    results = [evaluate_case(case) for case in load_cases(path)]
    failed = [item for item in results if not item["passed"]]
    return {
        "cases_file": str(path),
        "total": len(results),
        "passed": len(results) - len(failed),
        "failed": len(failed),
        "results": results,
    }


def format_markdown(payload: Dict[str, object]) -> str:
    lines = [
        "# BA Golden Evaluation",
        "",
        f"Total: {payload['total']}",
        f"Passed: {payload['passed']}",
        f"Failed: {payload['failed']}",
        "",
        "| Case | Scenario | Expected | Actual | Score | Result |",
        "|---|---|---:|---:|---:|---|",
    ]
    for item in payload["results"]:
        status = "PASS" if item["passed"] else "FAIL"
        lines.append(
            f"| {item['id']} | {item.get('scenario', '-')} | {item.get('expected_pass')} | "
            f"{item.get('actual_pass')} | {item.get('score', '-')} | {status} |"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run golden BA evaluation cases.")
    parser.add_argument("--cases", default=str(DEFAULT_CASES))
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    path = Path(args.cases).resolve()
    if not path.exists():
        print(f"ERROR: Golden cases not found: {path}", file=sys.stderr)
        return 2
    payload = evaluate_cases(path)
    if args.format == "markdown":
        print(format_markdown(payload))
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
