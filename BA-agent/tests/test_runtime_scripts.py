import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures"

import preflight_check
import knowledge_search
import knowledge_index_search
import quality_rubric
import reindex_markdown
import traceability_scan


class RuntimeScriptTests(unittest.TestCase):
    def test_knowledge_search_returns_relevant_uat_card(self):
        results = knowledge_search.search_cards("UAT traceability sign-off", limit=2)
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "KB-UAT-RTM-001")

    def test_knowledge_search_returns_ai_card(self):
        results = knowledge_search.search_cards("AI prediction model confidence fallback", limit=3)
        ids = {item["id"] for item in results}
        self.assertIn("KB-AI-ML-001", ids)

    def test_knowledge_search_cli_markdown(self):
        script = SCRIPT_DIR / "knowledge_search.py"
        result = subprocess.run(
            [sys.executable, str(script), "process modeling BPMN exception", "--format", "markdown"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("KB-MODELING-001", result.stdout)

    def test_knowledge_index_bm25_search(self):
        chunks = [
            {"id": "1", "text": "UAT scenario must map to traceability matrix and sign-off evidence.", "tags": ["uat"]},
            {"id": "2", "text": "Wireframe prototype includes loading empty and error states.", "tags": ["ux"]},
        ]
        results = knowledge_index_search.bm25_search("UAT traceability sign-off", chunks, limit=1)
        self.assertEqual(results[0]["id"], "1")

    def test_knowledge_index_cli_missing_index(self):
        script = SCRIPT_DIR / "knowledge_index_search.py"
        result = subprocess.run(
            [sys.executable, str(script), "anything", "--index", str(FIXTURE_DIR / "missing-index.jsonl")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)

    def test_quality_rubric_detects_weak_requirement(self):
        text = "FR-001 | Hệ thống quản lý tài sản nhanh và linh hoạt"
        result = quality_rubric.evaluate_text(text)
        self.assertFalse(result["passed"])
        self.assertGreaterEqual(len(result["requirements"][0]["smells"]), 1)

    def test_quality_rubric_skips_traceability_rows(self):
        text = "BRD-101 | FR-101 | US-001 | TC-001 | ☐"
        result = quality_rubric.evaluate_text(text)
        self.assertEqual(result["requirements"], [])

    def test_quality_rubric_scores_nfr_with_metric_columns(self):
        text = "| NFR-001 | Performance | API phải phản hồi trong thời gian ngắn | ≤ 500ms p95 | Load test |\n"
        result = quality_rubric.evaluate_text(text)
        self.assertTrue(result["passed"])
        self.assertIn("≤ 500ms p95", result["requirements"][0]["text"])

    def test_traceability_scan_reports_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("BRD-101\nBRD-101\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("FR-101\n", encoding="utf-8")
            report, _ = traceability_scan.build_report(root)
            gap_types = {gap["type"] for gap in report["gaps"]}
            self.assertIn("INDEX_DUPLICATE", gap_types)

    def test_traceability_scan_treats_strict_feature_gap_as_critical(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("| BRD-101 | Need |\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("| FR-101 | BRD-101 | Requirement |\n", encoding="utf-8")
            (root / "06-User-Story-Map.md").write_text("| US-001 | FR-101 | Story |\n", encoding="utf-8")
            (root / "08-UAT-Plan.md").write_text("| UAT-001 | US-001 | Test |\n", encoding="utf-8")
            report, critical_count = traceability_scan.build_report(root, scheme="legacy", strict=True)
            gap_types = {gap["type"] for gap in report["gaps"]}
            self.assertIn("BROKEN_CHAIN", gap_types)
            self.assertGreater(critical_count, 0)

    def test_traceability_scan_reports_orphan_nfr_without_dedicated_test(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("| BRD-101 | Need |\n", encoding="utf-8")
            (root / "05-SRS.md").write_text(
                "| FR-101 | BRD-101 | Requirement |\n"
                "| NFR-001 | BRD-101 | Availability | 99.9% uptime | Monthly report |\n",
                encoding="utf-8",
            )
            (root / "06-User-Story-Map.md").write_text("| US-001 | FR-101 | Story |\n", encoding="utf-8")
            (root / "08-UAT-Plan.md").write_text("| UAT-001 | US-001 | Test |\n", encoding="utf-8")
            report, critical_count = traceability_scan.build_report(root, scheme="legacy")
            gap_types = {gap["type"] for gap in report["gaps"]}
            self.assertIn("ORPHAN_NFR", gap_types)
            self.assertGreater(critical_count, 0)

    def test_traceability_scan_does_not_overconnect_business_ids_in_same_matrix_row(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("| BR-001 | A |\n| BR-002 | B |\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("| FR-101 | BR-001 | Requirement |\n", encoding="utf-8")
            (root / "04A-Feature-Map.md").write_text(
                "| BR-001, BR-002 | FR-101 | F-001 | US-001 | UAT-001 |\n",
                encoding="utf-8",
            )
            (root / "06-User-Story-Map.md").write_text("| US-001 | FR-101 | Story |\n", encoding="utf-8")
            (root / "08-UAT-Plan.md").write_text("| UAT-001 | US-001 | Test |\n", encoding="utf-8")
            report, _ = traceability_scan.build_report(root, scheme="legacy")
            br2 = next(chain for chain in report["chains"] if chain["business_id"] == "BR-002")
            self.assertEqual(br2["functional_ids"], [])

    def test_traceability_scan_detects_canonical_brq_definitions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("| BRQ-01 | Need |\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("| FR-INV-001 | BRQ-01 | Requirement |\n", encoding="utf-8")
            report, _ = traceability_scan.build_report(root, scheme="canonical")
            self.assertEqual(report["metrics"]["business_total"], 1)
            self.assertEqual(report["chains"][0]["business_id"], "BRQ-01")

    def test_traceability_scan_canonical_fixture_passes_strict(self):
        report, critical_count = traceability_scan.build_report(
            FIXTURE_DIR / "canonical_bundle", scheme="canonical", strict=True
        )
        self.assertEqual(critical_count, 0)
        self.assertEqual(report["metrics"]["business_total"], 1)
        self.assertEqual(report["metrics"]["full_chain_total"], 1)
        self.assertEqual(report["gaps"], [])

    def test_traceability_scan_cli_exit_codes_for_strict_mode(self):
        script = SCRIPT_DIR / "traceability_scan.py"
        passed = subprocess.run(
            [sys.executable, str(script), str(FIXTURE_DIR / "canonical_bundle"), "--scheme", "canonical", "--strict"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("| BRD-101 | Need |\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("| FR-101 | BRD-101 | Requirement |\n", encoding="utf-8")
            (root / "06-User-Story-Map.md").write_text("| US-001 | FR-101 | Story |\n", encoding="utf-8")
            (root / "08-UAT-Plan.md").write_text("| UAT-001 | US-001 | Test |\n", encoding="utf-8")
            failed = subprocess.run(
                [sys.executable, str(script), str(root), "--scheme", "legacy", "--strict"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(failed.returncode, 1)

    def test_reindex_skips_baseline_docs_by_default(self):
        text = "## 1. Scope\n> **Trạng thái:** Draft\n> **Đã phê duyệt — Chốt phạm vi**\n"
        self.assertTrue(reindex_markdown.is_signed_baseline(text))

    def test_reindex_skips_headings_inside_fenced_blocks(self):
        text = "## 1. Scope\n```markdown\n## 9. Example\n```\n## 2. Next\n"
        rewritten, updates = reindex_markdown.build_heading_replacements(text)
        self.assertIn("## 9. Example", rewritten)
        self.assertEqual(updates, [])

    def test_reindex_uses_definition_ids_not_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            brd = root / "02-BRD.md"
            srs = root / "05-SRS.md"
            brd.write_text("| BR-001 | Need | FR-101 |\n", encoding="utf-8")
            srs.write_text("| FR-101 | BR-001 | Requirement |\n| FR-103 | BR-001 | Requirement |\n", encoding="utf-8")
            replacements = reindex_markdown.build_id_replacements([brd, srs])
            self.assertEqual(replacements, {"FR-103": "FR-102"})

    def test_preflight_raises_for_missing_target(self):
        with self.assertRaises(FileNotFoundError):
            preflight_check.evaluate_path(Path("missing-target-for-preflight"))

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

    def test_preflight_quality_gate_uses_rubric_pass_flag(self):
        text = "\n".join(
            [
                "| FR-001 | Hệ thống quản lý tài sản nhanh và linh hoạt |",
                "| FR-002 | Precondition: người dùng có quyền. Khi lưu, hệ thống phải lưu hồ sơ trong 2 giây. |",
                "| FR-003 | Precondition: người dùng có quyền. Khi sửa, hệ thống phải lưu hồ sơ trong 2 giây. |",
            ]
        )
        checks = preflight_check.srs_checks(text, {"02-BRD.md": "BRD content"})
        gate = next(item for item in checks if item["item"] == "Requirement Quality Gate")
        self.assertEqual(gate["status_code"], "FAIL")


if __name__ == "__main__":
    unittest.main()
