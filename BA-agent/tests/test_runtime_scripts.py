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
import ba_response_eval
import ai_smell_scan
import build_knowledge_index
import eval_golden_cases
import ba_id_utils
import media_audit
import persona_review_check
import quality_rubric
import reindex_markdown
import template_schema_check
import traceability_scan


class RuntimeScriptTests(unittest.TestCase):
    def test_persona_review_requires_all_21_roles_with_evidence(self):
        roles = persona_review_check.canonical_roles(
            persona_review_check.PROTOCOL.read_text(encoding="utf-8")
        )
        self.assertEqual(len(roles), 21)
        rows = "\n".join(f"| {role} | PASS | Kiểm tra mục 2 của tài liệu | — |" for role in roles)
        report = f"Tài liệu: docs/BRD.md v1.0 | Tier: 3\nLoại rà soát: Review độc lập (người thật: Lê An, QA Lead)\n## Độ phủ 21 vai trò\n{rows}\n"
        self.assertEqual(persona_review_check.validate_report(report, roles), [])
        self_review = report.replace("Review độc lập (người thật: Lê An, QA Lead)", "Tự rà soát (AI)")
        self.assertTrue(any("H4" in error for error in persona_review_check.validate_report(self_review, roles)))
        self.assertIn(
            "R-BA: thiếu vai trò (bắt buộc ở Tier 3)",
            persona_review_check.validate_report(report.replace(rows.splitlines()[-1], ""), roles),
        )

    def test_persona_review_rejects_unjustified_na_and_unlinked_issue(self):
        roles = persona_review_check.canonical_roles(
            persona_review_check.PROTOCOL.read_text(encoding="utf-8")
        )
        rows = [f"| {role} | PASS | Kiểm tra mục 2 của tài liệu | — |" for role in roles]
        rows[0] = f"| {roles[0]} | N/A | — | — |"
        rows[1] = f"| {roles[1]} | ISSUE | Thiếu ngoại lệ ở mục 3 | RV-01 |"
        report = "Tài liệu: docs/BRD.md v1.0\n## Độ phủ 21 vai trò\n" + "\n".join(rows)
        errors = persona_review_check.validate_report(report, roles)
        self.assertTrue(any("thiếu căn cứ" in error for error in errors))
        self.assertTrue(any("RV-01 không có trong mục Phát hiện" in error for error in errors))

    def test_persona_review_rejects_duplicate_and_generic_na(self):
        roles = persona_review_check.canonical_roles(
            persona_review_check.PROTOCOL.read_text(encoding="utf-8")
        )
        rows = [f"| {role} | PASS | Kiểm tra mục 2 của tài liệu | — |" for role in roles]
        rows[0] = f"| {roles[0]} | N/A | Không áp dụng | — |"
        report = "Tài liệu: docs/BRD.md v1.0\n## Độ phủ 21 vai trò\n" + "\n".join(rows + [rows[0]])
        errors = persona_review_check.validate_report(report, roles)
        self.assertTrue(any("vai trò bị lặp" in error for error in errors))
        self.assertTrue(any("N/A phải nêu lý do" in error for error in errors))

    def _roles(self):
        return persona_review_check.canonical_roles(persona_review_check.PROTOCOL.read_text(encoding="utf-8"))

    def test_persona_review_tier1_requires_only_core_roles_for_document_type(self):
        roles = self._roles()
        needed = ["R-BA", "R-CFO", "R-PO", "R-MANAGER", "R-CUSTOMER"]
        rows = "\n".join(f"| {role} | PASS | Đối chiếu mục 1.6, bảng BRQ | — |" for role in needed)
        report = f"Tài liệu: docs/BRD.md v1.0 | Loại tài liệu: BRD | Tier: 1\n## Độ phủ vai trò\n{rows}\n"
        self.assertEqual(persona_review_check.validate_report(report, roles), [])
        errors = persona_review_check.validate_report(report.replace("| R-CFO |", "| R-XYZ |"), roles)
        self.assertTrue(any("R-CFO: thiếu vai trò" in error for error in errors))

    def test_persona_review_tier2_adds_roles_and_needs_document_type(self):
        roles = self._roles()
        report = "Tài liệu: docs/SRS.md v1.0 | Tier: 2 | Dữ liệu nhạy cảm: Có\n## Độ phủ vai trò\n"
        errors = persona_review_check.validate_report(report, roles)
        self.assertTrue(any("Loại tài liệu" in error for error in errors))
        required = persona_review_check.required_roles(roles, 2, "srs", True)
        for role in ("R-BA", "R-TECH", "R-SPONSOR", "R-QA", "R-PRIVACY"):
            self.assertIn(role, required)
        self.assertNotIn("R-CFO", required)
        self.assertEqual(len(persona_review_check.required_roles(roles, 3, None, False)), 21)

    def test_persona_review_rejects_evidence_without_location_and_unreferenced_findings(self):
        roles = self._roles()
        rows = [f"| {role} | PASS | Kiểm tra mục 2 của tài liệu | — |" for role in roles]
        rows[0] = f"| {roles[0]} | PASS | x | — |"
        report = (
            "Tài liệu: docs/BRD.md v1.0 | Tier: 3\n## Độ phủ vai trò\n" + "\n".join(rows)
            + "\n## Phát hiện\n| ID | Vai trò |\n|---|---|\n| RV-07 | R-QA |\n"
        )
        errors = persona_review_check.validate_report(report, roles)
        self.assertTrue(any(f"{roles[0]}: căn cứ PASS phải trỏ tới vị trí" in error for error in errors))
        self.assertTrue(any("RV-07: phát hiện không được vai trò nào" in error for error in errors))

    def test_persona_review_cli_survives_cp1252_console(self):
        roles = self._roles()
        rows = "\n".join(f"| {role} | PASS | Kiểm tra mục 2 của tài liệu | — |" for role in roles)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "review.md"
            path.write_text(f"Tài liệu: docs/BRD.md v1.0 | Tier: 3\nLoại rà soát: Review độc lập (người thật: Lê An, QA Lead)\n## Độ phủ 21 vai trò\n{rows}\n", encoding="utf-8")
            env = dict(__import__("os").environ, PYTHONIOENCODING="cp1252", PYTHONUTF8="0")
            result = subprocess.run(
                [sys.executable, str(SCRIPT_DIR / "persona_review_check.py"), str(path)],
                capture_output=True,
                env=env,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

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

    def test_knowledge_index_hybrid_expands_vietnamese_ba_terms(self):
        chunks = [
            {
                "id": "1",
                "source_path": "sample/uat.md",
                "source_name": "uat.md",
                "chunk_index": 0,
                "text": "UAT acceptance sign-off evidence must map to contractor handover and traceability.",
                "tags": ["uat", "rtm"],
            },
            {
                "id": "2",
                "source_path": "sample/ui.md",
                "source_name": "ui.md",
                "chunk_index": 0,
                "text": "Prototype layout defines empty state and responsive UI behavior.",
                "tags": ["ux"],
            },
        ]
        results = knowledge_index_search.search("nghiệm thu nhà thầu", chunks, limit=1, mode="hybrid")
        self.assertEqual(results[0]["id"], "1")
        self.assertEqual(results[0]["retrieval_mode"], "hybrid")

    def test_knowledge_index_compact_includes_citation_fields(self):
        record = {
            "id": "1",
            "score": 0.9,
            "source_path": "docs/brd.pdf",
            "source_name": "brd.pdf",
            "chunk_index": 7,
            "text": "A " * 500,
            "tags": ["brd"],
            "extraction": "pdf-pypdf",
        }
        payload = knowledge_index_search.compact(record, max_chars=40)
        self.assertEqual(payload["source_ref"], "docs/brd.pdf#chunk-7")
        self.assertIn("excerpt", payload)
        self.assertLessEqual(len(payload["excerpt"]), 40)

    def test_knowledge_index_cli_missing_index(self):
        script = SCRIPT_DIR / "knowledge_index_search.py"
        result = subprocess.run(
            [sys.executable, str(script), "anything", "--index", str(FIXTURE_DIR / "missing-index.jsonl")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)

    def test_ba_response_eval_passes_outsource_control_coverage(self):
        text = (
            "Stakeholder/RACI owner and approver are named. Scope includes in scope and out of scope. "
            "Assumption and constraint are listed. Change Request and change control are defined. "
            "UAT acceptance sign-off maps to RTM traceability from BRQ to FR to US to TC. "
            "Handover includes KT and warranty."
        )
        payload = ba_response_eval.evaluate_text(text, "outsource")
        self.assertTrue(payload["passed"])

    def test_ba_response_eval_fails_missing_product_metrics(self):
        text = "The product has user stories and a backlog."
        payload = ba_response_eval.evaluate_text(text, "product")
        self.assertFalse(payload["passed"])

    def test_ba_response_eval_short_tokens_match_on_word_boundaries(self):
        self.assertFalse(ba_response_eval.term_in_text("cr", "the descriptions were discussed"))
        self.assertTrue(ba_response_eval.term_in_text("cr", "a cr was raised"))
        self.assertTrue(ba_response_eval.term_in_text("fr-", "maps to fr-auth-001"))
        self.assertTrue(ba_response_eval.term_in_text("phạm vi", "xác định phạm vi dự án"))

    def test_ba_response_eval_supports_domain_scenarios(self):
        for scenario in ("healthcare", "government", "startup-mvp", "inhouse"):
            payload = ba_response_eval.evaluate_text("Nothing relevant here.", scenario)
            self.assertFalse(payload["passed"], scenario)

    def test_ai_smell_scan_flags_vietnamese_and_english_patterns(self):
        text = "\n".join(
            [
                "Hệ thống đóng vai trò quan trọng trong việc quản lý.",
                "Nó không chỉ lưu dữ liệu mà còn gửi thông báo.",
                "Additionally, this is a robust design.",
                "Hệ thống gửi thông báo trong 30 giây.",
            ]
        )
        findings = ai_smell_scan.scan_text(text)
        self.assertEqual({item["line"] for item in findings}, {1, 2, 3})

    def test_ai_smell_scan_skips_fenced_code(self):
        text = "\n".join(["```", "đóng vai trò quan trọng", "```", "Hệ thống lưu đơn nghỉ."])
        self.assertEqual(ai_smell_scan.scan_text(text), [])

    def test_senior_judgement_cases_have_required_structure(self):
        path = Path(__file__).resolve().parent / "golden" / "senior_judgement_cases.jsonl"
        cases = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertGreaterEqual(len(cases), 8)
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            for key in ("situation", "ask"):
                self.assertTrue(str(case.get(key, "")).strip(), f"{case['id']} missing {key}")
            for key in ("senior_signals", "middle_signals", "red_flags"):
                self.assertTrue(case.get(key), f"{case['id']} missing {key}")
            self.assertGreaterEqual(len(case["senior_signals"]), 3, case["id"])

    def test_golden_cases_pass(self):
        payload = eval_golden_cases.evaluate_cases(Path(__file__).resolve().parent / "golden" / "ba_response_cases.jsonl")
        self.assertEqual(payload["failed"], 0)

    def test_build_index_chunks_pages_with_page_metadata(self):
        pages = [
            " ".join(["first"] * 40),
            " ".join(["second"] * 40),
        ]
        chunks = build_knowledge_index.chunk_pages(pages, max_words=30, overlap=5)
        self.assertGreaterEqual(len(chunks), 2)
        self.assertEqual(chunks[0]["page_start"], 1)
        self.assertEqual(chunks[-1]["page_start"], 2)

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
            (root / "04A-Feature-Map.md").write_text("| F-002 | Other feature |\n", encoding="utf-8")
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

    def test_traceability_scan_canonical_full_fixture_passes_strict(self):
        report, critical_count = traceability_scan.build_report(
            FIXTURE_DIR / "canonical_full_bundle", scheme="canonical", strict=True
        )
        self.assertEqual(critical_count, 0)
        self.assertEqual(report["metrics"]["business_total"], 3)
        self.assertEqual(report["metrics"]["full_chain_total"], 3)
        self.assertEqual(report["gaps"], [])

    def test_template_schema_check_passes_curated_core_templates(self):
        report = template_schema_check.evaluate_templates(Path(__file__).resolve().parents[1] / "Curated templates")
        self.assertEqual(report["summary"]["fail"], 0)
        self.assertEqual(report["summary"]["pass"], 4)

    def test_media_audit_passes_curated_media_inventory(self):
        report = media_audit.evaluate_media(Path(__file__).resolve().parents[1] / "Curated templates")
        self.assertEqual(report["metrics"]["gap_total"], 0)
        self.assertEqual(report["metrics"]["media_total"], 11)
        self.assertEqual(report["metrics"]["embedded_total"], 6)

    def test_acceptance_criteria_file_is_treated_as_uat_artifact(self):
        self.assertEqual(ba_id_utils.classify_file(Path("07-Acceptance-Criteria.md")), "uat")
        meta = ba_id_utils.detect_id_meta("AC-AST-001", 1)
        self.assertIsNotNone(meta)
        self.assertEqual(meta.family, "AC")

    def test_traceability_scan_accepts_canonical_ac_chain(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("| BRQ-01 | Need |\n", encoding="utf-8")
            (root / "03-Feature-Map.md").write_text("| F01 | Feature | BRQ-01, FR-AST-001, US-AST-001, AC-AST-001 |\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("| FR-AST-001 | Requirement | BRQ-01, F01 |\n", encoding="utf-8")
            (root / "06-User-Story.md").write_text("| US-AST-001 | Story | FR-AST-001, F01 |\n", encoding="utf-8")
            (root / "07-Acceptance-Criteria.md").write_text(
                "| AC-AST-001 | Given valid input, when saved, then success. | US-AST-001, FR-AST-001 |\n",
                encoding="utf-8",
            )
            report, critical_count = traceability_scan.build_report(root, scheme="canonical", strict=True)
            self.assertEqual(critical_count, 0)
            self.assertEqual(report["metrics"]["full_chain_total"], 1)

    def test_traceability_scan_one_to_one_flag_rejects_multiple_us_per_fr(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "02-BRD.md").write_text("| BRQ-01 | Need |\n", encoding="utf-8")
            (root / "03-Feature-Map.md").write_text(
                "| F01 | Feature | BRQ-01, FR-AST-001, US-AST-001, US-AST-002, AC-AST-001 |\n",
                encoding="utf-8",
            )
            (root / "05-SRS.md").write_text("| FR-AST-001 | Requirement | BRQ-01, F01 |\n", encoding="utf-8")
            (root / "06-User-Story.md").write_text(
                "| US-AST-001 | Story | FR-AST-001, F01 |\n"
                "| US-AST-002 | Story | FR-AST-001, F01 |\n",
                encoding="utf-8",
            )
            (root / "07-Acceptance-Criteria.md").write_text(
                "| AC-AST-001 | Given valid input, when saved, then success. | US-AST-001 |\n",
                encoding="utf-8",
            )
            report, critical_count = traceability_scan.build_report(root, scheme="canonical", strict=True)
            self.assertNotIn("MULTIPLE_US_FOR_FR", {gap["type"] for gap in report["gaps"]})
            report, critical_count = traceability_scan.build_report(
                root, scheme="canonical", strict=True, one_to_one=True
            )
            gap_types = {gap["type"] for gap in report["gaps"]}
            self.assertIn("MULTIPLE_US_FOR_FR", gap_types)
            self.assertGreater(critical_count, 0)

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
                [sys.executable, str(script), str(root), "--scheme", "canonical", "--strict"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(failed.returncode, 1)

    # --- traceability: false-PASS regressions -------------------------------------------------

    def _bundle(self, root: Path, files: dict) -> None:
        for name, text in files.items():
            (root / name).write_text(text, encoding="utf-8")

    def test_traceability_scan_reads_definitions_from_headings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "### BRQ-01: Đăng nhập\nMô tả.\n",
                "05-SRS.md": "### FR-AUTH-001 — Đăng nhập bằng mật khẩu\nNguồn: BRQ-01\n",
            })
            report, _ = traceability_scan.build_report(root, scheme="canonical")
            self.assertEqual(report["metrics"]["business_total"], 1)
            self.assertEqual(report["metrics"]["functional_total"], 1)

    def test_traceability_scan_fails_empty_or_unrecognised_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _, critical = traceability_scan.build_report(root)
            self.assertGreater(critical, 0)
            (root / "ghi-chu.md").write_text("Không có ID nào.\n", encoding="utf-8")
            report, critical = traceability_scan.build_report(root)
            self.assertIn("NO_DEFINITIONS", {gap["type"] for gap in report["gaps"]})
            self.assertGreater(critical, 0)

    def test_traceability_scan_canonical_strict_rejects_legacy_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "| BRD-101 | Need |\n",
                "05-SRS.md": "| FR-101 | BRD-101 | Requirement |\n",
            })
            report, critical = traceability_scan.build_report(root, scheme="canonical", strict=True)
            self.assertIn("OFF_SCHEME_ID", {gap["type"] for gap in report["gaps"]})
            self.assertGreater(critical, 0)

    def test_traceability_scan_default_mode_checks_every_fr(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "| BRD-101 | Need |\n",
                "05-SRS.md": "| FR-101 | BRD-101 | A |\n| FR-102 | BRD-101 | B |\n",
                "06-User-Story-Map.md": "| US-001 | FR-101 | Story |\n",
                "08-UAT-Plan.md": "| UAT-001 | US-001 | Test |\n",
            })
            report, critical = traceability_scan.build_report(root, scheme="legacy")
            missing = [gap["item"] for gap in report["gaps"] if gap["type"] == "MISSING_US_FOR_FR"]
            self.assertEqual(missing, ["FR-102"])
            self.assertGreater(critical, 0)

    def test_traceability_scan_supports_four_digit_and_alnum_module_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "| BRQ-01 | Need |\n",
                "05-SRS.md": "| FR-M01-001 | BRQ-01 | A |\n| FR-1001 | BRQ-01 | B |\n",
            })
            report, _ = traceability_scan.build_report(root)
            self.assertEqual(report["metrics"]["functional_total"], 2)

    def test_traceability_scan_four_column_nfr_table_is_definition(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "| BRQ-01 | Need |\n",
                "05-SRS.md": "| NFR-PERF-001 | BRQ-01 | Phản hồi tìm kiếm dưới 300 ms | Load test |\n",
            })
            report, _ = traceability_scan.build_report(root, scheme="canonical")
            self.assertIn("ORPHAN_NFR", {gap["type"] for gap in report["gaps"]})

    def test_traceability_scan_flags_story_reference_to_undefined_fr(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "| BRQ-01 | Need |\n",
                "05-SRS.md": "| FR-AUTH-001 | BRQ-01 | A |\n",
                "06-User-Story.md": "| US-AUTH-001 | FR-AUTH-001, FR-AUTH-009 | Story |\n",
            })
            report, _ = traceability_scan.build_report(root, scheme="canonical")
            stale = [gap["item"] for gap in report["gaps"] if gap["type"] == "STALE_REF"]
            self.assertEqual(stale, ["FR-AUTH-009"])

    def test_traceability_scan_labels_unenforced_business_rule(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "| BRQ-01 | Need |\n| BR-001 | Rule |\n",
                "05-SRS.md": "| FR-AUTH-001 | BRQ-01 | A |\n",
            })
            report, _ = traceability_scan.build_report(root, scheme="canonical")
            self.assertIn("ORPHAN_BR", {gap["type"] for gap in report["gaps"]})

    def test_id_patterns_do_not_match_tail_of_longer_id(self):
        self.assertEqual(ba_id_utils.extract_ids_from_line("| TC-NFR-001 | NFR-PERF-001 |"), ["TC-NFR-001", "NFR-PERF-001"])
        self.assertNotIn("NFR-001", ba_id_utils.extract_ids_from_line("TC-NFR-001"))

    def test_sample_bundles_pass_canonical_strict(self):
        root = Path(__file__).resolve().parents[1]
        for name in ("BA-Documents-Outsource", "BA-Documents-Product"):
            report, critical = traceability_scan.build_report(root / name, scheme="canonical", strict=True)
            self.assertEqual(critical, 0, [gap for gap in report["gaps"] if gap["type"] != "UNCLASSIFIED_FILE"])

    def test_traceability_scan_ignores_ids_in_tilde_fences(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._bundle(root, {
                "02-BRD.md": "| BRQ-01 | Need |\n~~~\n| BRQ-02 | Ví dụ |\n~~~\n",
                "05-SRS.md": "| FR-AUTH-001 | BRQ-01 | A |\n",
            })
            report, _ = traceability_scan.build_report(root, scheme="canonical")
            self.assertEqual(report["metrics"]["business_total"], 1)

    # --- reindex: data-safety regressions ------------------------------------------------------

    def test_reindex_heading_numbers_inside_titles_are_not_numbering(self):
        text = "## 1. Giới thiệu\n## 2024 Roadmap\n### 3 bước đăng nhập\n## 2. Phạm vi\n"
        rewritten, updates = reindex_markdown.build_heading_replacements(text)
        self.assertEqual(rewritten, text)
        self.assertEqual(updates, [])

    def test_reindex_keeps_template_heading_scheme(self):
        text = "## 2.0 Thông tin chung\n## 2.1 Giới thiệu\n## 2.3 Yêu cầu\n### 2.3.1 Module\n"
        rewritten, _ = reindex_markdown.build_heading_replacements(text)
        self.assertIn("## 2.2 Yêu cầu", rewritten)
        self.assertIn("### 2.2.1 Module", rewritten)
        self.assertIn("## 2.0 Thông tin chung", rewritten)

    def test_reindex_leaves_contiguous_sequences_alone(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            story = root / "06-User-Story.md"
            story.write_text("".join(f"| US-{i:03d} | Story |\n" for i in range(1, 13)), encoding="utf-8")
            uat = root / "08-UAT.md"
            uat.write_text("| TC-01-A | x |\n| TC-01-B | y |\n| AC-01 | z |\n", encoding="utf-8")
            self.assertEqual(reindex_markdown.build_id_replacements([story, uat]), {})

    def test_reindex_freezes_groups_defined_in_signed_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            brd = root / "02-BRD.md"
            srs = root / "05-SRS.md"
            brd.write_text("# BRD\n> **Trạng thái:** Đã phê duyệt\n| BRQ-01 | A |\n| BRQ-03 | B |\n", encoding="utf-8")
            srs.write_text("| FR-AUTH-001 | BRQ-03 |\n", encoding="utf-8")
            plan = reindex_markdown.plan_renumbering([brd, srs])
            self.assertNotIn("BRQ-03", plan["replacements"])
            self.assertTrue(plan["frozen"])

    def test_reindex_kpi_baseline_column_is_not_a_signature(self):
        text = "# BRD\n> Trạng thái: Draft\n" + "\n" * 50 + "| KPI | Baseline | Mục tiêu |\n"
        self.assertFalse(reindex_markdown.is_signed_baseline(text))

    def test_reindex_renames_sub_requirements_with_parent_and_keeps_crlf(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            brd = root / "02-BRD.md"
            brd.write_bytes("| BRQ-01 | A |\r\n| BRQ-03 | B |\r\n| BRQ-03.1 | Con |\r\n".encode("utf-8"))
            srs = root / "05-SRS.md"
            srs.write_text("| FR-AUTH-001 | BRQ-03.1 |\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT_DIR / "reindex_markdown.py"), str(root), "--apply"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            data = brd.read_bytes().decode("utf-8")
            self.assertIn("| BRQ-02 | B |\r\n", data)
            self.assertIn("| BRQ-02.1 | Con |\r\n", data)
            self.assertIn("BRQ-02.1", srs.read_text(encoding="utf-8"))

    def test_reindex_does_not_merge_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            srs = root / "05-SRS.md"
            srs.write_text("| FR-AUTH-001 | A |\n| FR-AUTH-003 | B |\n| FR-AUTH-003 | C |\n", encoding="utf-8")
            plan = reindex_markdown.plan_renumbering([srs])
            self.assertEqual(plan["replacements"], {})
            self.assertTrue(plan["duplicates"])

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

    def test_preflight_ignores_negated_markers(self):
        text = "# BRD\nHiện chưa có glossary.\nChưa có hiện trạng.\nKhông có traceability.\n"
        checks = {item["item"]: item["status_code"] for item in preflight_check.brd_checks(text, {})}
        self.assertEqual(checks["Glossary"], "FAIL")
        self.assertEqual(checks["As-Is Process"], "FAIL")
        self.assertEqual(checks["Traceability Matrix"], "FAIL")

    def test_preflight_vietnamese_pronoun_ai_is_not_an_ai_feature(self):
        text = "# BRD\nAi phê duyệt đơn? Trưởng phòng là người duyệt; ai cũng xem được trạng thái.\n"
        checks = {item["item"]: item["status_code"] for item in preflight_check.brd_checks(text, {})}
        self.assertEqual(checks["AI Feature Spec"], "N/A")
        self.assertTrue(preflight_check.mentions_ai("Tính năng gợi ý dùng mô hình AI để xếp hạng."))

    def test_preflight_moscow_needs_priority_values_in_tables(self):
        prose = "Người dùng có thể xem. Có thể lọc. Có thể xuất. Có thể in.\n"
        checks = {item["item"]: item["status_code"] for item in preflight_check.brd_checks(prose, {})}
        self.assertEqual(checks["MoSCoW Priority"], "FAIL")
        table = "".join(f"| BRQ-0{i} | Nhu cầu | {p} |\n" for i, p in enumerate(["Must", "Must", "Should", "Could"], 1))
        checks = {item["item"]: item["status_code"] for item in preflight_check.brd_checks(table, {})}
        self.assertEqual(checks["MoSCoW Priority"], "PASS")

    def test_preflight_required_labels_and_links_are_not_placeholders(self):
        text = "> [AI-Drafted] [TÀI LIỆU MẪU]\nGateway [CẦN XÁC NHẬN]; ngưỡng [Giả định] 5 phút.\nXem [SRS](05-SRS.md).\n"
        self.assertEqual(preflight_check.count_placeholders(text), 0)
        self.assertEqual(preflight_check.count_placeholders("Tên dự án: [Tên dự án]\n"), 1)

    def test_preflight_accepts_moscow_as_headings_and_ignores_out_of_scope_ai(self):
        text = (
            "## 6. Phạm vi\n### BẮT BUỘC (Must)\n- A\n### NÊN CÓ (Should)\n- B\n### CÓ THỂ (Could)\n- C\n"
            "## 7. Ngoài phạm vi\n| Nhận dạng tài sản bằng AI | Chưa có dữ liệu |\n## 8. Rủi ro\n"
        )
        checks = {item["item"]: item["status_code"] for item in preflight_check.brd_checks(text, {})}
        self.assertEqual(checks["MoSCoW Priority"], "PASS")
        self.assertEqual(checks["AI Feature Spec"], "N/A")

    def test_preflight_srs_finds_data_dictionary_in_data_model_document(self):
        ctx = {"02-BRD.md": "BRD", "07-Data-Model.md": "| Field | Kiểu dữ liệu | Null |\n"}
        checks = {item["item"]: item["status_code"] for item in preflight_check.srs_checks("# SRS\n", ctx)}
        self.assertEqual(checks["Data Dictionary"], "PASS")

    def test_bundle_audit_flags_stale_headers_and_missing_skills(self):
        import ba_bundle_audit

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            guide = root / "GUIDE.md"
            guide.write_text("# Hướng dẫn BA 3.4\n", encoding="utf-8")
            original = ba_bundle_audit.HEADER_VERSIONED_FILES
            original_root = ba_bundle_audit.ROOT
            try:
                ba_bundle_audit.HEADER_VERSIONED_FILES = [guide]
                ba_bundle_audit.ROOT = root
                self.assertTrue(ba_bundle_audit.stale_header_versions((3, 6, 0), "3.6.0"))
                self.assertFalse(ba_bundle_audit.stale_header_versions((3, 4, 0), "3.4.0"))
                (root / "agents").mkdir()
                (root / "agents" / "x.md").write_text("---\nskills: [no-such-skill]\n---\n", encoding="utf-8")
                self.assertTrue(ba_bundle_audit.missing_agent_skills())
            finally:
                ba_bundle_audit.HEADER_VERSIONED_FILES = original
                ba_bundle_audit.ROOT = original_root

    def test_preflight_evidence_sources_follow_tier(self):
        no_tier = "# BRD\nKhông ghi Tier.\n"
        self.assertEqual(preflight_check.evidence_sources_check(no_tier)["status_code"], "N/A")
        tier2_missing = "# BRD\n> **Tier:** 2 — hợp đồng\n| BR-001 | Quy tắc |\n"
        self.assertEqual(preflight_check.evidence_sources_check(tier2_missing)["status_code"], "FAIL")
        tier2_ok = (
            "# BRD\n> **Tier:** 2 — hợp đồng\n"
            "| Mã BR | Quy tắc | Nguồn · Mức |\n|---|---|---|\n| BR-001 | Quy tắc | SRC-01 · E2 |\n"
            "### Sổ nguồn\n| Mã nguồn | Loại |\n|---|---|\n| SRC-01 | Workshop |\n"
        )
        self.assertEqual(preflight_check.evidence_sources_check(tier2_ok)["status_code"], "PASS")
        tier1_column = "# Mini-Brief\nTier: 1\n| Fact | Nguồn |\n|---|---|\n| A | PO |\n"
        self.assertEqual(preflight_check.evidence_sources_check(tier1_column)["status_code"], "PASS")

    def test_senior_cases_cover_triage_sources_and_slices(self):
        path = Path(__file__).resolve().parent / "golden" / "senior_judgement_cases.jsonl"
        ids = {json.loads(line)["id"] for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}
        for case_id in ("quick_ac_request_no_bundle", "single_indirect_source_business_rule", "slice_baselining_partial_clarity"):
            self.assertIn(case_id, ids)

    def test_preflight_fails_folder_without_recognised_documents(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "ghi-chu.md").write_text("# Ghi chú\n", encoding="utf-8")
            report = preflight_check.evaluate_bundle(Path(tmp))
            self.assertGreater(report["summary"]["fail"], 0)
            self.assertTrue(report["errors"])

    def test_quality_rubric_accepts_percentage_metrics(self):
        text = "| NFR-AVL-001 | Availability | Hệ thống phải sẵn sàng 99.9% thời gian mỗi tháng | Uptime report | Monitoring |\n"
        result = quality_rubric.evaluate_text(text)
        self.assertNotIn("Untestable NFR", result["requirements"][0]["smells"])
        self.assertNotIn("Vague Adjective", result["requirements"][0]["smells"])

    def test_quality_rubric_actor_words_match_whole_words(self):
        self.assertFalse(quality_rubric.contains_word("the development team saves data", ("pm",)))
        self.assertTrue(quality_rubric.contains_word("pm duyệt yêu cầu", ("pm",)))

    def test_ba_response_eval_acronyms_do_not_match_ordinary_words(self):
        text = "Tài liệu mô tả yêu cầu phi chức năng. He saved his notes."
        payload = ba_response_eval.evaluate_text(text, "healthcare")
        checks = {item["id"]: item["status"] == "PASS" for item in payload["checks"]}
        self.assertFalse(checks["privacy_consent"])
        self.assertFalse(checks["integration"])
        payload = ba_response_eval.evaluate_text("Dữ liệu PHI được mã hóa; tích hợp HIS qua HL7.", "healthcare")
        checks = {item["id"]: item["status"] == "PASS" for item in payload["checks"]}
        self.assertTrue(checks["privacy_consent"])
        self.assertTrue(checks["integration"])

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

    def test_preflight_flags_unaccented_vietnamese_body_text(self):
        text = (
            "He thong phai hien thi danh sach don hang va cho phep nguoi dung kiem tra thong tin khach hang. "
            "Tai lieu yeu cau chuc nang quan ly du lieu dau vao dau ra."
        )
        passed, detail = preflight_check.vietnamese_diacritics_status(text)
        self.assertFalse(passed, detail)

    def test_preflight_allows_accented_vietnamese_body_text(self):
        text = (
            "Hệ thống phải hiển thị danh sách đơn hàng và cho phép người dùng kiểm tra thông tin khách hàng. "
            "Tài liệu yêu cầu chức năng quản lý dữ liệu đầu vào đầu ra."
        )
        passed, detail = preflight_check.vietnamese_diacritics_status(text)
        self.assertTrue(passed, detail)

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
