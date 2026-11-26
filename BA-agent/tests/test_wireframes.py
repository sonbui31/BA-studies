"""Wireframes and mockups (so_do.md section 13): HTML -> PNG rendering and the screen-set check."""
import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import wireframe_tool  # noqa: E402


def tiny_png() -> bytes:
    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    header = struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(b"\x00\xff\xff\xff")) + chunk(b"IEND", b"")


INVENTORY = (
    "# Screen Inventory\n\n| Mã màn hình | Tên | Ảnh |\n|---|---|---|\n"
    "| SCR-01 | Danh sách tài sản | `wireframes/SCR-01-danh-sach.png` |\n"
    "| SCR-02 | Phiếu kiểm kê | `wireframes/SCR-02-kiem-ke.png` |\n"
)
SRS = (
    "# SRS\n\n![SCR-01: Danh sách tài sản](wireframes/SCR-01-danh-sach.png)\n"
    "*Nguồn thiết kế: [wireframes/SCR-01-danh-sach.html](wireframes/SCR-01-danh-sach.html) | Cấp trực quan: Wireframe*\n\n"
    "![SCR-02: Phiếu kiểm kê](wireframes/SCR-02-kiem-ke.png)\n"
    "*Nguồn thiết kế: Figma — SCR-02 | Cấp trực quan: Mockup*\n"
)


def bundle(tmp: str, srs: str = SRS, inventory: str = INVENTORY, images=("SCR-01-danh-sach.png", "SCR-02-kiem-ke.png")) -> Path:
    root = Path(tmp)
    (root / "wireframes").mkdir()
    for name in images:
        (root / "wireframes" / name).write_bytes(tiny_png())
    (root / "05-SRS.md").write_text(srs, encoding="utf-8")
    (root / "06-Screen-Inventory.md").write_text(inventory, encoding="utf-8")
    return root


def problems(root: Path, level: str):
    return [f.detail for f in wireframe_tool.check_bundle(root) if f.level == level]


class WireframeCheckTests(unittest.TestCase):
    def test_consistent_bundle_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = bundle(tmp)
            self.assertEqual(wireframe_tool.check_bundle(root), [])
            self.assertEqual(wireframe_tool.main(["check", str(root), "--strict"]), 0)

    def test_missing_image_and_unknown_screen_are_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            srs = SRS + "\n![SCR-09: Lạ](wireframes/SCR-09-la.png)\n*Nguồn thiết kế: Figma*\n"
            root = bundle(tmp, srs=srs)
            errors = problems(root, "error")
            self.assertTrue(any("SCR-09-la.png" in e and "không tồn tại" in e for e in errors))
            self.assertTrue(any("SCR-09 không có trong bảng" in e for e in errors))
            self.assertEqual(wireframe_tool.main(["check", str(root)]), 1)

    def test_image_must_be_named_after_its_screen(self):
        with tempfile.TemporaryDirectory() as tmp:
            srs = SRS + "\n![Màn hình](wireframes/man-hinh.png)\n*Nguồn thiết kế: Figma*\n"
            root = bundle(tmp, srs=srs, images=("SCR-01-danh-sach.png", "SCR-02-kiem-ke.png", "man-hinh.png"))
            self.assertTrue(any("phải bắt đầu bằng mã màn hình" in e for e in problems(root, "error")))
            wrong_row = INVENTORY.replace("`wireframes/SCR-02-kiem-ke.png`", "`wireframes/SCR-01-danh-sach.png`")
        with tempfile.TemporaryDirectory() as tmp:
            root = bundle(tmp, inventory=wrong_row)
            self.assertTrue(any("SCR-02 trỏ tới ảnh của SCR-01" in e for e in problems(root, "error")))

    def test_source_line_and_orphans_are_warnings(self):
        with tempfile.TemporaryDirectory() as tmp:
            srs = SRS.replace("*Nguồn thiết kế: Figma — SCR-02 | Cấp trực quan: Mockup*\n", "")
            root = bundle(tmp, srs=srs, images=("SCR-01-danh-sach.png", "SCR-02-kiem-ke.png", "SCR-03-cu.png"))
            warnings = problems(root, "warning")
            self.assertTrue(any("thiếu dòng" in w and "SCR-02" in w for w in warnings))
            self.assertTrue(any("không được tài liệu nào dùng" in w for w in warnings))
            self.assertEqual(problems(root, "error"), [])
            self.assertEqual(wireframe_tool.main(["check", str(root)]), 0)
            self.assertEqual(wireframe_tool.main(["check", str(root), "--strict"]), 1)

    def test_screen_code_mentioned_without_a_row_is_a_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            srs = SRS + "\n| FR-AST-001 | Tạo hồ sơ | ... | SCR-12 |\n"
            root = bundle(tmp, srs=srs)
            self.assertTrue(any("SCR-12 được nhắc tới" in w for w in problems(root, "warning")))

    def test_examples_inside_code_fences_are_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            srs = SRS + "\n```markdown\n![SCR-77: Ví dụ](wireframes/SCR-77-vi-du.png)\n```\n"
            root = bundle(tmp, srs=srs)
            self.assertEqual(wireframe_tool.check_bundle(root), [])

    def test_bad_arguments_exit_2(self):
        self.assertEqual(wireframe_tool.main(["check", str(ROOT / "khong-co-thu-muc")]), 2)
        self.assertEqual(wireframe_tool.main(["render", str(ROOT / "khong-co.html")]), 2)
        with self.assertRaises(ValueError):
            wireframe_tool.page_size("", "1280")

    def test_page_size_from_meta(self):
        self.assertEqual(wireframe_tool.page_size('<meta name="wireframe-size" content="390x844">', None), (390, 844))
        self.assertEqual(wireframe_tool.page_size("", None), (1280, 800))
        self.assertEqual(wireframe_tool.page_size("", "1440x900"), (1440, 900))

    def test_shipped_bundles_pass(self):
        for folder in ("BA-Documents-Outsource", "BA-Documents-Product"):
            self.assertEqual(wireframe_tool.main(["check", str(ROOT / folder), "--strict"]), 0, folder)

    @unittest.skipUnless(wireframe_tool.find_browser(), "render needs an installed Chrome or Edge")
    def test_render_html_to_png(self):
        with tempfile.TemporaryDirectory() as tmp:
            html = Path(tmp) / "SCR-01-thu.html"
            html.write_text('<!doctype html><meta charset="utf-8"><meta name="wireframe-size" content="400x300"><p>Danh sách tài sản</p>', encoding="utf-8")
            self.assertEqual(wireframe_tool.main(["render", str(html), "--scale", "1"]), 0)
            data = (Path(tmp) / "SCR-01-thu.png").read_bytes()
            self.assertEqual(struct.unpack(">II", data[16:24]), (400, 300))


if __name__ == "__main__":
    unittest.main()
