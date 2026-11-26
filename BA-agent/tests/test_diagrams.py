"""Diagram standard (so_do.md): lint, auto-fix, Word export of Mermaid, Hard Gate 1 check."""
import struct
import sys
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import diagram_check  # noqa: E402
import md_to_docx  # noqa: E402
import preflight_check  # noqa: E402


def tiny_png() -> bytes:
    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    header = struct.pack(">IIBBBBB", 2, 2, 8, 2, 0, 0, 0)
    pixels = zlib.compress(b"\x00" + b"\xff\xff\xff" * 2 + b"\x00" + b"\xff\xff\xff" * 2)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", pixels) + chunk(b"IEND", b"")


def lint(text: str, max_nodes: int = 12):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "doc.md"
        path.write_text(text, encoding="utf-8")
        diagrams = diagram_check.extract_diagrams(path)
        return [f for d in diagrams for f in diagram_check.check_diagram(d, max_nodes)]


def codes(findings, level=None):
    return sorted({f.code for f in findings if level is None or f.level == level})


THEME = diagram_check.THEME_LINE


class DiagramCheckTests(unittest.TestCase):
    def test_placeholder_in_identifier_breaks_but_in_label_only_warns(self):
        broken = "```mermaid\nerDiagram\n    {{ENTITY_1}} ||--o{ {{ENTITY_2}} : \"quan hệ\"\n```\n"
        self.assertIn("PLACEHOLDER", codes(lint(broken), "error"))
        label = f"```mermaid\n{THEME}\nflowchart LR\n    A[\"{{{{Tên bước}}}}\"] --> B[\"Kết thúc\"]\n```\n"
        found = lint(label)
        self.assertNotIn("PLACEHOLDER", codes(found, "error"))
        self.assertIn("PLACEHOLDER_TEXT", codes(found, "warning"))
        gantt = f"```mermaid\n{THEME}\ngantt\n    dateFormat YYYY-MM-DD\n    section A\n        Ký :milestone, m0, {{{{date}}}}, 0d\n```\n"
        self.assertIn("PLACEHOLDER", codes(lint(gantt), "error"))

    def test_stereotype_tag_only_flagged_in_flowcharts(self):
        flow = f"```mermaid\n{THEME}\nflowchart LR\n    A([\"Đặt hàng\"]) -.->|\"<<include>>\"| B([\"Thanh toán\"])\n```\n"
        self.assertIn("STEREOTYPE_TAG", codes(lint(flow), "error"))
        klass = f"```mermaid\n{THEME}\nclassDiagram\n    class Kho {{\n        <<interface>>\n    }}\n```\n"
        self.assertNotIn("STEREOTYPE_TAG", codes(lint(klass)))

    def test_unlabeled_branch_of_exclusive_gateway_is_an_error(self):
        text = (
            f"```mermaid\n{THEME}\nflowchart LR\n    S((\"Bắt đầu\")) --> G{{\"Đủ điều kiện?\"}}\n"
            "    G -->|\"Có\"| A[\"Duyệt\"]\n    G --> B[\"Từ chối\"]\n```\n"
        )
        errors = [f for f in lint(text) if f.code == "UNLABELED_BRANCH"]
        self.assertEqual(len(errors), 1)
        self.assertIn("G -> B", errors[0].detail)

    def test_parallel_gateway_needs_no_labels_but_needs_a_join(self):
        paired = (
            f"```mermaid\n{THEME}\nflowchart LR\n    P1{{\"+\"}} --> A[\"Hoàn tiền\"]\n    P1 --> B[\"Gửi thư\"]\n"
            "    A --> P2{\"+\"}\n    B --> P2\n```\n"
        )
        self.assertEqual(codes(lint(paired)), [])
        unpaired = paired.replace("    A --> P2{\"+\"}\n    B --> P2\n", "")
        self.assertIn("PARALLEL_UNPAIRED", codes(lint(unpaired), "warning"))

    def test_style_warnings(self):
        text = "```mermaid\nflowchart LR\n    A[\"👤 Khách\\nhàng\"] --> B[\"Đơn\"]\n```\n"
        self.assertEqual(codes(lint(text), "warning"), ["EMOJI", "NEWLINE_ESCAPE", "NO_THEME"])
        many = f"```mermaid\n{THEME}\nflowchart LR\n" + "".join(f"    N{i}[\"Bước {i}\"] --> N{i + 1}[\"Bước {i + 1}\"]\n" for i in range(14)) + "```\n"
        self.assertIn("TOO_MANY_NODES", codes(lint(many), "warning"))

    def test_fix_rewrites_mechanical_issues_and_keeps_crlf(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "doc.md"
            original = "# Tài liệu\r\n\r\n```mermaid\r\nflowchart LR\r\n    A[\"👤 Khách\\nhàng\"] -.->|\"<<include>>\"| B([\"Thanh toán\"])\r\n```\r\n"
            path.write_bytes(original.encode("utf-8"))
            self.assertGreater(diagram_check.fix_file(path), 0)
            data = path.read_bytes().decode("utf-8")
            self.assertIn("%%{init:", data)
            self.assertIn("Khách<br/>hàng", data)
            self.assertIn("≪include≫", data)
            self.assertNotIn("👤", data)
            self.assertNotIn("\n", data.replace("\r\n", ""))
            self.assertEqual(codes(lint(data)), [])

    def test_shipped_diagrams_meet_the_standard(self):
        targets = [ROOT / "so_do.md", ROOT / "BA-Documents-Outsource", ROOT / "BA-Documents-Product", ROOT / "Curated templates"]
        for target in targets:
            paths = [target] if target.is_file() else sorted(target.rglob("*.md"))
            findings = [f for p in paths for d in diagram_check.extract_diagrams(p) for f in diagram_check.check_diagram(d, 12)]
            self.assertEqual(findings, [], f"{target}: {[(f.code, f.file, f.line) for f in findings]}")
        rules = sorted((ROOT / "BA-document-rule").rglob("*.md"))
        errors = [f for p in rules for d in diagram_check.extract_diagrams(p) for f in diagram_check.check_diagram(d, 15) if f.level == "error"]
        self.assertEqual(errors, [])


class WordDiagramTests(unittest.TestCase):
    def test_mermaid_becomes_picture_when_a_renderer_is_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "doc.md"
            md.write_text(f"# Quy trình\n\n```mermaid\n{THEME}\nflowchart LR\n    A[\"Bắt đầu\"] --> B[\"Kết thúc\"]\n```\n", encoding="utf-8")
            seen = []
            counts = md_to_docx.convert(md, Path(tmp) / "with.docx", None, lambda code: seen.append(code) or tiny_png())
            self.assertEqual((counts["diagrams"], counts["diagrams_as_code"]), (1, 0))
            self.assertTrue(seen[0].startswith("%%{init"))
            with zipfile.ZipFile(Path(tmp) / "with.docx") as zf:
                self.assertTrue(any(name.startswith("word/media/") for name in zf.namelist()))
                self.assertNotIn("flowchart LR", zf.read("word/document.xml").decode("utf-8"))
            counts = md_to_docx.convert(md, Path(tmp) / "without.docx")
            self.assertEqual((counts["diagrams"], counts["diagrams_as_code"]), (0, 1))
            failing = md_to_docx.convert(md, Path(tmp) / "failing.docx", None, lambda code: None)
            self.assertEqual(failing["diagrams_as_code"], 1)

    def test_cli_refuses_image_mode_without_mermaid_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "doc.md"
            md.write_text("# A\n", encoding="utf-8")
            code = md_to_docx.main([str(md), "--diagrams", "image", "--mmdc", str(Path(tmp) / "khong-co-mmdc.cmd")])
            self.assertEqual(code, 2)


class ProcessDiagramGateTests(unittest.TestCase):
    def test_brd_needs_a_drawn_process(self):
        flow = f"```mermaid\n{THEME}\nflowchart LR\n    A[\"Nhận\"] --> B[\"Duyệt\"]\n```\n"
        bare = "# BRD\n\n## Quy trình\n\nKhoa gửi phiếu -> Vật tư duyệt\n"
        self.assertEqual(preflight_check.process_diagram_check(bare, {"02-BRD.md": bare})["status_code"], preflight_check.FAIL_CODE)
        self.assertEqual(preflight_check.process_diagram_check(bare + flow, {})["status_code"], preflight_check.PASS_CODE)
        ctx = {"02-BRD.md": bare, "04-Process-Flow.md": flow}
        self.assertEqual(preflight_check.process_diagram_check(bare, ctx)["status_code"], preflight_check.PASS_CODE)
        ascii_flow = {"02-BRD.md": bare, "04-Process-Flow.md": "```\nKhoa ──▶ Vật tư\n```\n"}
        self.assertEqual(preflight_check.process_diagram_check(bare, ascii_flow)["status_code"], preflight_check.FAIL_CODE)
        sequence_only = f"```mermaid\n{THEME}\nsequenceDiagram\n    A->>B: gọi\n```\n"
        self.assertEqual(preflight_check.process_diagram_check(bare + sequence_only, {})["status_code"], preflight_check.FAIL_CODE)
        self.assertEqual(preflight_check.process_diagram_check(bare + "![Quy trình](diagrams/p1.png)", {})["status_code"], preflight_check.PASS_CODE)
        self.assertEqual(preflight_check.process_diagram_check("[LỐI AGILE LITE]\n" + bare, {})["status_code"], preflight_check.NA_CODE)

    def test_process_gate_is_not_fooled(self):
        bare = "# BRD\n\n## Quy trình\n\nKhoa gửi phiếu -> Vật tư duyệt\n"
        fail, ok, na = preflight_check.FAIL_CODE, preflight_check.PASS_CODE, preflight_check.NA_CODE

        def status(text):
            return preflight_check.process_diagram_check(text, {})["status_code"]

        self.assertEqual(status(bare + "![Logo](assets/logo.png)\n"), fail)  # any picture is not a process
        self.assertEqual(status(bare + "File gốc là quy-trinh.bpmn trong thư mục chung.\n"), fail)  # plain mention
        self.assertEqual(status(bare + "```text\n[x](diagrams/p1.bpmn)\n```\n"), fail)  # inside a code fence
        self.assertEqual(status(bare + "Bản chuẩn: [p1](diagrams/p1.bpmn)\n"), ok)
        self.assertEqual(status(bare + "Không áp dụng lối Agile Lite cho dự án này.\n"), fail)
        front = f"```mermaid\n---\ntitle: Duyệt\n---\n{THEME}\nflowchart LR\n    A[\"Nhận\"] --> B[\"Duyệt\"]\n```\n"
        self.assertEqual(status(bare + front), ok)
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "02-BRD.md").write_text(bare + "Bản chuẩn: [p1](diagrams/khong-co.bpmn)\n", encoding="utf-8")
            report = preflight_check.evaluate_bundle(Path(tmp))
            gate = [c for d in report["documents"] for c in d["checks"] if c["item"] == "Process Diagram"][0]
            self.assertEqual(gate["status_code"], fail)  # link to a file that does not exist
        self.assertEqual(status(bare + "![Quy trình](diagrams/p1.png)"), ok)  # no bundle folder: not checked on disk
        self.assertEqual(na, preflight_check.NA_CODE)


class HumanSignoffTests(unittest.TestCase):
    HEAD = "# SRS\n\n> Trạng thái: Baseline\n\n"

    def code(self, text):
        return preflight_check.human_signoff_check(self.HEAD + text)["status_code"]

    def test_signoff_table_under_a_subheading_counts(self):
        text = "## 9. Phê duyệt\n\n### 9.1 Bên khách hàng\n\n| Vai trò | Họ tên | Ngày |\n|---|---|---|\n| Sponsor | Nguyễn Văn A | 05/03/2026 |\n"
        self.assertEqual(self.code(text), preflight_check.PASS_CODE)

    def test_rows_without_a_name_or_with_a_placeholder_date_do_not_count(self):
        no_name = "## Phê duyệt\n\n| Vai trò | Họ tên | Ngày |\n|---|---|---|\n| Sponsor | [Tên] | 05/03/2026 |\n"
        self.assertEqual(self.code(no_name), preflight_check.FAIL_CODE)
        fake_date = "## Phê duyệt\n\n| Vai trò | Họ tên | Ngày |\n|---|---|---|\n| Sponsor | Nguyễn Văn A | 00/00/0000 |\n"
        self.assertEqual(self.code(fake_date), preflight_check.FAIL_CODE)

    def test_open_items_ignore_code_and_checklist_sentences(self):
        signed = "## Phê duyệt\n\n| Vai trò | Họ tên | Ngày |\n|---|---|---|\n| Sponsor | Nguyễn Văn A | 05/03/2026 |\n"
        quiet = "- [x] Không còn mục [CẦN XÁC NHẬN] nào\n\nGhi `[CẦN XÁC NHẬN]` khi chưa rõ.\n\n```\n[CẦN XÁC NHẬN]\n```\n"
        self.assertEqual(self.code(quiet + signed), preflight_check.PASS_CODE)
        self.assertEqual(self.code("Ngưỡng duyệt 50 triệu [CẦN XÁC NHẬN]\n" + signed), preflight_check.FAIL_CODE)


if __name__ == "__main__":
    unittest.main()
