"""Regression tests for ID patterns found in real project bundles (QLTS, vClassio).

Before 3.8 the scripts were tuned on the sample bundles only; on real documents most findings were
false: matrix rows with a title column, sub-IDs (FR-TEA-003.1), overview lists, grouping tables and
project-specific IDs were all misread. tests/fixtures/real_world_patterns reproduces those patterns
without customer data.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
REAL = Path(__file__).resolve().parent / "fixtures" / "real_world_patterns"

import ba_id_utils  # noqa: E402
import id_migrate  # noqa: E402
import reindex_markdown  # noqa: E402
import traceability_scan  # noqa: E402


def gap_types(report):
    return [gap["type"] for gap in report["gaps"]]


class RealWorldPatternTests(unittest.TestCase):
    def tearDown(self):
        ba_id_utils.set_project_scheme(None)

    def copy_bundle(self, tmp):
        target = Path(tmp) / "bundle"
        shutil.copytree(REAL, target)
        return target

    def test_real_world_bundle_is_clean_under_project_scheme(self):
        report, critical = traceability_scan.build_report(REAL, scheme="project", strict=True)
        self.assertEqual(critical, 0, report["gaps"])
        self.assertEqual(report["metrics"]["full_chain_total"], report["metrics"]["business_total"])

    def test_same_bundle_fails_canonical_strict(self):
        report, critical = traceability_scan.build_report(REAL, scheme="canonical", strict=True)
        self.assertGreater(critical, 0)
        self.assertIn("OFF_SCHEME_ID", gap_types(report))

    def test_project_scheme_required_for_project_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = self.copy_bundle(tmp)
            (target / "ba-scheme.json").unlink()
            with self.assertRaises(ValueError):
                traceability_scan.build_report(target, scheme="project")

    def test_matrix_with_title_column_is_not_a_duplicate(self):
        text = (
            "### US01: Tra cứu\n\n## Bảng tổng hợp\n\n| US | Tên | BRQ | FR | TC |\n|---|---|---|---|---|\n"
            "| US01 | Tra cứu tài sản bằng QR | BRQ-01 | FR-QR-01 | TC-01-A |\n"
        )
        definitions = ba_id_utils.definition_ids(text, "story")
        self.assertEqual(ba_id_utils.duplicate_definitions(definitions), {})

    def test_matrix_with_business_column_first_is_not_a_duplicate(self):
        text = (
            "| Mã YC | Mô tả |\n|---|---|\n| BR-001 | Theo dõi học tập |\n\n"
            "| BR liên quan | Mã SR | Functional Requirement | User Story | Test Case |\n|---|---|---|---|---|\n"
            "| BR-001, BR-004 | SR-01 | (bổ sung sau) | (bổ sung sau) | (bổ sung sau) |\n"
        )
        definitions = ba_id_utils.definition_ids(text, "brd")
        self.assertEqual(ba_id_utils.duplicate_definitions(definitions), {})

    def test_sub_ids_are_children_not_duplicates(self):
        self.assertEqual(ba_id_utils.extract_ids_from_line("| FR-TEA-003.1 | Gửi duyệt |"), ["FR-TEA-003.1"])
        self.assertEqual(ba_id_utils.parent_id("FR-TEA-003.1"), "FR-TEA-003")
        text = "| ID | FR-TEA-003 |\n\n| Mã | Yêu cầu |\n|---|---|\n| FR-TEA-003.1 | A |\n| FR-TEA-003.2 | B |\n"
        definitions = ba_id_utils.definition_ids(text, "srs")
        self.assertEqual([item.meta.value for item in definitions], ["FR-TEA-003", "FR-TEA-003.1", "FR-TEA-003.2"])
        self.assertEqual(ba_id_utils.duplicate_definitions(definitions), {})

    def test_overview_list_plus_detail_heading_is_not_a_duplicate(self):
        text = "- F05. Quản lý tài sản\n- F06. Kiểm kê\n\n### 2.5 F05 — Quản lý tài sản\n"
        self.assertEqual(ba_id_utils.duplicate_definitions(ba_id_utils.definition_ids(text, "feature")), {})

    def test_grouping_table_is_not_a_duplicate(self):
        text = (
            "### F05 — Quản lý tài sản\n\n| Module | Exception ID | Mô tả |\n|---|---|---|\n"
            "| F05 | EX-1A | Trùng mã |\n| F05 | EX-1B | Thiếu trường |\n| F08 | EX-2A | Đang sửa |\n\n"
            "### F08 — Điều chuyển\n"
        )
        self.assertEqual(ba_id_utils.duplicate_definitions(ba_id_utils.definition_ids(text, "feature")), {})

    def test_real_duplicates_are_still_reported(self):
        two_headings = "### US-AUTH-001: Đăng nhập\n\n### US-AUTH-001: Đăng xuất\n"
        self.assertIn("US-AUTH-001", ba_id_utils.duplicate_definitions(ba_id_utils.definition_ids(two_headings, "story")))
        defining_table = "| Mã YC | Mô tả |\n|---|---|\n| FR-AUTH-001 | A |\n| FR-AUTH-001 | B |\n"
        self.assertIn("FR-AUTH-001", ba_id_utils.duplicate_definitions(ba_id_utils.definition_ids(defining_table, "srs")))

    def test_links_on_the_line_under_a_definition_count(self):
        text = "### US01: Tra cứu\n> **Related BRQ-ID:** `BRQ-01` | **FR-ID:** `FR-QR-01`\n\n## Khác\nBRQ-09\n"
        owners = ba_id_utils.definition_blocks(text, "story")
        self.assertEqual(owners.get(2), "US01")
        self.assertNotIn(5, owners)

    def test_orphan_brq_names_the_undefined_fr_it_points_to(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = self.copy_bundle(tmp)
            brd = target / "02-BRD.md"
            brd.write_text(
                brd.read_text(encoding="utf-8")
                + "\n## 4. Bổ sung\n\n| BRQ-ID | Tên | FR |\n|---|---|---|\n| **BRQ-03** | Báo cáo | FR-RPT-09 |\n",
                encoding="utf-8",
            )
            config = json.loads((target / "ba-scheme.json").read_text(encoding="utf-8"))
            report, _ = traceability_scan.build_report(target, scheme="project", strict=True)
            orphan = [gap for gap in report["gaps"] if gap["item"] == "BRQ-03"]
            self.assertTrue(orphan, report["gaps"])
            self.assertIn("FR-RPT-09", orphan[0]["detail"])
            self.assertTrue(config["ids"])

    def test_brq_listed_in_srs_matrix_does_not_hide_missing_brd_definition(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = self.copy_bundle(tmp)
            srs = target / "05-SRS.md"
            srs.write_text(
                srs.read_text(encoding="utf-8")
                + "\n## 3. Ma trận truy vết\n\n| BRQ | FR | TC |\n|---|---|---|\n| BRQ-07 | FR-QR-01 | TC-01-A |\n",
                encoding="utf-8",
            )
            report, _ = traceability_scan.build_report(target, scheme="project", strict=True)
            stale = [gap["item"] for gap in report["gaps"] if gap["type"] == "STALE_REF"]
            self.assertIn("BRQ-07", stale)

    def test_reindex_keeps_project_prefix_and_moves_children(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "ba-scheme.json").write_text(json.dumps({"ids": {"business": ["SR-\\d{2}"]}}), encoding="utf-8")
            brd = root / "02-BRD.md"
            brd.write_text("| Mã YC | Mô tả |\n|---|---|\n| SR-01 | A |\n| SR-03 | B |\n", encoding="utf-8")
            srs = root / "05-SRS.md"
            srs.write_text(
                "| Mã YC | Mô tả |\n|---|---|\n| FR-AUTH-001 | A (SR-03) |\n| FR-AUTH-003 | B |\n| FR-AUTH-003.1 | Con |\n",
                encoding="utf-8",
            )
            ba_id_utils.set_project_scheme(ba_id_utils.load_project_scheme(root / "ba-scheme.json"))
            plan = reindex_markdown.plan_renumbering([brd, srs])
            self.assertEqual(plan["replacements"].get("SR-03"), "SR-02")
            self.assertEqual(plan["replacements"].get("FR-AUTH-003"), "FR-AUTH-002")
            self.assertEqual(plan["replacements"].get("FR-AUTH-003.1"), "FR-AUTH-002.1")

    def test_id_migrate_blocks_targets_the_scripts_cannot_read(self):
        plan = id_migrate.plan_migration({"TC-01-A"}, [(__import__("re").compile(r"TC-(\d{2})-([A-Z])"), r"TC-QLTS-\1\2")])
        self.assertTrue(plan["conflicts"])

    def test_id_migrate_apply_writes_alias_table_and_keeps_chains(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = self.copy_bundle(tmp)
            config = json.loads((target / "ba-scheme.json").read_text(encoding="utf-8"))
            config["migrate"] = {"US(\\d{2})": "US-QR-0\\1"}
            (target / "ba-scheme.json").write_text(json.dumps(config), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT_DIR / "id_migrate.py"), str(target), "--apply"],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            alias = (target / "ID-MIGRATION.md").read_text(encoding="utf-8")
            self.assertIn("| US01 | US-QR-001 |", alias)
            self.assertIn("US-QR-001", (target / "06-User-Story-Map.md").read_text(encoding="utf-8"))
            report, critical = traceability_scan.build_report(target, scheme="project", strict=True)
            self.assertEqual(critical, 0, report["gaps"])

    def test_rubric_reads_description_under_a_title_line(self):
        import quality_rubric

        text = (
            "### FR-01.1 — Xem sổ liên lạc\n\n| Mô tả | Phụ huynh có thể xem sổ liên lạc của con theo thứ tự thời gian. |\n"
            "| --- | --- |\n| Actor | Parent |\n\n- **FR-QR-01: Quét mã QR**\n  - **Mô tả:** Nhân viên quét mã, hệ thống phải mở trang tài sản trong 2 giây.\n"
            "\n- Camera của giáo viên dùng cho điểm danh (FR-04.1)\n"
        )
        result = quality_rubric.evaluate_text(text, doc_role="srs")
        by_id = {item["req_id"]: item for item in result["requirements"]}
        self.assertEqual(sorted(by_id), ["FR-01.1", "FR-QR-01"])  # the mention of FR-04.1 is not a requirement
        self.assertNotIn("Missing Actor", by_id["FR-01.1"]["smells"])
        self.assertIn("Phụ huynh", by_id["FR-01.1"]["text"])
        self.assertIn("2 giây", by_id["FR-QR-01"]["text"])

    def test_project_actors_count_as_actors(self):
        import quality_rubric

        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / "ba-scheme.json"
            config.write_text(json.dumps({"ids": {}, "actors": ["ktts"]}), encoding="utf-8")
            line = "| FR-AST-001 | KTTS phải nhập mã tài sản trước khi lưu. |\n"
            self.assertIn("Missing Actor", quality_rubric.evaluate_text(line)["requirements"][0]["smells"])
            ba_id_utils.set_project_scheme(ba_id_utils.load_project_scheme(config))
            self.assertNotIn("Missing Actor", quality_rubric.evaluate_text(line)["requirements"][0]["smells"])

    def test_preflight_ignores_brackets_inside_inline_code(self):
        import preflight_check

        text = "Auth: `[ADMIN, KTTS]`. Regex `^ASSET-[0-9a-f]{8}$`. Còn thiếu [Tên khách hàng].\n"
        self.assertEqual(preflight_check.count_placeholders(text), 1)

    def test_preflight_uses_project_roles_for_brd_presence(self):
        import preflight_check

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "ba-scheme.json").write_text(json.dumps({"files": {"01-baccm.md": "brd"}}), encoding="utf-8")
            (root / "01-BACCM.md").write_text("# BACCM\n\n| BRQ-ID | Mô tả |\n|---|---|\n| BRQ-01 | A |\n", encoding="utf-8")
            (root / "05-SRS.md").write_text("# SRS\n\n| ID | Yêu cầu |\n|---|---|\n| FR-AST-001 | Hệ thống phải lưu. |\n", encoding="utf-8")
            report = preflight_check.evaluate_bundle(root)
            srs = next(doc for doc in report["documents"] if doc["file"] == "05-SRS.md")
            brd_check = next(check for check in srs["checks"] if check["item"] == "BRD Completed")
            self.assertEqual(brd_check["status_code"], preflight_check.PASS_CODE)

    def test_human_signoff_fails_when_approved_without_signatures(self):
        import preflight_check

        approved_unsigned = (
            "# BRD\n> **Trạng thái:** Draft\n\n## Lịch sử\n\n| Phiên bản | Ngày | Thay đổi | Người | Phê duyệt bởi |\n|---|---|---|---|---|\n"
            "| 1.0 | 26/02/2026 | **Đã phê duyệt — Chốt phạm vi** | BA | Giám đốc vận hành |\n\n"
            "## 11. Phê duyệt BRD\n\n| Vai trò | Họ tên | Chữ ký | Ngày |\n|---|---|---|---|\n| Sponsor | | | |\n"
        )
        result = preflight_check.human_signoff_check(approved_unsigned)
        self.assertEqual(result["status_code"], preflight_check.FAIL_CODE)
        signed = approved_unsigned.replace("| Sponsor | | | |", "| Sponsor | Trần Minh Đức | Đã ký | 26/02/2026 |")
        self.assertEqual(preflight_check.human_signoff_check(signed)["status_code"], preflight_check.PASS_CODE)
        still_open = signed + "\nHạn mức `[CẦN XÁC NHẬN: Giám đốc]`\n"
        self.assertEqual(preflight_check.human_signoff_check(still_open)["status_code"], preflight_check.FAIL_CODE)

    def test_human_signoff_is_na_for_drafts_and_policy_notes(self):
        import preflight_check

        draft = (
            "# BRD\n> **Trạng thái:** Trình duyệt\n> ⚠️ Tài liệu CHỐT PHẠM VI (Baseline) — mọi thay đổi sau khi phê duyệt phải qua CR\n\n"
            "| Tài liệu | Mô tả |\n|---|---|\n| BRD | Phải chính thống, chốt phạm vi (baseline) + phê duyệt |\n"
            "| 0.2 | 12/05/2026 | Trình duyệt | PM/BA |\n"
        )
        self.assertEqual(preflight_check.human_signoff_check(draft)["status_code"], preflight_check.NA_CODE)

    def test_bundle_audit_flags_rule_text_copied_between_rule_files(self):
        import ba_bundle_audit

        rule = "Không ghi Baseline khi bảng Phê duyệt chưa có họ tên và ngày của người có thẩm quyền, hoặc còn câu hỏi cần xác nhận chưa đóng."
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "agents").mkdir()
            (root / "SKILL.md").write_text(f"# Skill\n\n- {rule}\n", encoding="utf-8")
            (root / "agents" / "a.md").write_text(f"# Agent\n\n1. **{rule}**\n", encoding="utf-8")
            original = ba_bundle_audit.ROOT
            try:
                ba_bundle_audit.ROOT = root
                self.assertEqual(len(ba_bundle_audit.duplicated_rule_text()), 1)
                (root / "agents" / "a.md").write_text("# Agent\n\nXem `SKILL.md` mục 10.\n", encoding="utf-8")
                self.assertEqual(ba_bundle_audit.duplicated_rule_text(), [])
            finally:
                ba_bundle_audit.ROOT = original

    def test_id_migrate_conflict_when_two_ids_map_to_one(self):
        import re

        plan = id_migrate.plan_migration({"US01", "US-QR-001"}, [(re.compile(r"US(\d{2})"), r"US-QR-0\1")])
        self.assertTrue(any("US-QR-001" in item for item in plan["conflicts"]))


if __name__ == "__main__":
    unittest.main()
