import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import preflight_check
import quality_rubric
import reindex_markdown
import traceability_scan


class RuntimeScriptTests(unittest.TestCase):
    def test_quality_rubric_detects_weak_requirement(self):
        text = "FR-001 | Hệ thống quản lý tài sản nhanh và linh hoạt"
        result = quality_rubric.evaluate_text(text)
        self.assertFalse(result["passed"])
        self.assertGreaterEqual(len(result["requirements"][0]["smells"]), 1)

    def test_quality_rubric_skips_traceability_rows(self):
        text = "BRD-101 | FR-101 | US-001 | TC-001 | ☐"
        result = quality_rubric.evaluate_text(text)
        self.assertEqual(result["requirements"], [])

    def test_traceability_scan_reports_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("BRD-101\nBRD-101\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("FR-101\n", encoding="utf-8")
            report, _ = traceability_scan.build_report(root)
            gap_types = {gap["type"] for gap in report["gaps"]}
            self.assertIn("INDEX_DUPLICATE", gap_types)

    def test_reindex_skips_baseline_docs_by_default(self):
        text = "## 1. Scope\n> **Trạng thái:** Draft\n> **Đã phê duyệt — Chốt phạm vi**\n"
        self.assertTrue(reindex_markdown.is_signed_baseline(text))

    def test_preflight_flags_missing_stakeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text(
                "# BRD\n## 1. Vấn đề hiện tại\n| # | Vấn đề |\n|---|---|\n|1|A|\n|2|B|\n"
                "## 2. Đối tượng đọc\n| Đối tượng | Mục đích đọc |\n|---|---|\n|Sponsor|X|\n"
                "## 3. Giả định\n|#|Giả định|\n|---|---|\n|1|A|\n## 4. Ràng buộc\n|#|Ràng buộc|\n|---|---|\n|1|B|\n",
                encoding="utf-8",
            )
            payload = preflight_check.evaluate_path(root)
            brd = payload["documents"][0]
            stakeholder = next(item for item in brd["checks"] if item["item"] == "Stakeholder Map")
            self.assertEqual(stakeholder["status_code"], "FAIL")


if __name__ == "__main__":
    unittest.main()
