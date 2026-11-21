import re
import struct
import subprocess
import sys
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path
from xml.etree import ElementTree as ET


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import ba_id_utils
import docx_feedback
import md_to_docx

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"

SAMPLE_MD = """# Đặc tả yêu cầu phần mềm — Hệ thống đặt lịch khám

> **Trạng thái:** Draft
> **Phiên bản:** 1.0

## 1. Yêu cầu chức năng

Tài liệu mô tả yêu cầu **bắt buộc** và *tùy chọn* cho `module-auth`. Xem [Cổng dịch vụ công](https://dichvucong.gov.vn) và [SRS](05-SRS.md).<br>Dòng thứ hai.

| Mã | Mô tả | Nguồn |
|:---|---|---:|
| FR-AUTH-001 | Khóa tài khoản sau 5 lần đăng nhập sai | BRQ-01 |
| FR-AUTH-002 | Đặt lại mật khẩu qua SMS \\| email | BRQ-01, US-AUTH-001 |
| NFR-PERF-001 | Phản hồi dưới 2 giây |

### 1.1 Danh sách

- Bệnh nhân đăng ký
  - Nhập số CCCD
    - Xác thực OTP
- Bác sĩ duyệt lịch

1. Mở ứng dụng
2. Chọn khoa khám
3. Xác nhận

```python
def kiem_tra(): return "Đã khóa"
```

```mermaid
flowchart TD
  A[Bệnh nhân] --> B[Đặt lịch]
```

---

![Sơ đồ ngữ cảnh](media/so-do.png)

![Ảnh thiếu](media/khong-co.png)

<!-- ghi chú nội bộ, không xuất ra Word -->

#### Ghi chú cấp 4

##### Cấp 5

###### Cấp 6
"""

REQUIRED_PARTS = [
    "[Content_Types].xml",
    "_rels/.rels",
    "word/document.xml",
    "word/_rels/document.xml.rels",
    "word/styles.xml",
    "word/numbering.xml",
    "docProps/core.xml",
    "docProps/app.xml",
]


def tiny_png(width: int = 4, height: int = 3) -> bytes:
    raw = b"".join(b"\x00" + b"\xff\x00\x00" * width for _ in range(height))

    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


def run_script(name: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT_DIR / name), *args], capture_output=True, encoding="utf-8", errors="replace"
    )


def write_sample(root: Path) -> Path:
    (root / "media").mkdir()
    (root / "media" / "so-do.png").write_bytes(tiny_png())
    md = root / "srs-mau.md"
    md.write_text(SAMPLE_MD, encoding="utf-8")
    return md


def doc_text(zf: zipfile.ZipFile) -> str:
    root = ET.fromstring(zf.read("word/document.xml"))
    return "".join(t.text or "" for t in root.iter(f"{{{W_NS}}}t"))


def all_ids(text: str) -> set:
    found = set()
    for line in text.splitlines():
        found.update(ba_id_utils.extract_ids_from_line(line))
    return found


def build_docx(path: Path, document: str, comments: str = "") -> None:
    """Minimal hand-written package used for the feedback tests."""
    overrides = '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    rels = ""
    if comments:
        overrides += '<Override PartName="/word/comments.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>'
        rels = f'<Relationship Id="rId9" Type="{R_NS}/comments" Target="comments.xml"/>'
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr(
            "[Content_Types].xml",
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            f'<Default Extension="xml" ContentType="application/xml"/>{overrides}</Types>',
        )
        zf.writestr(
            "_rels/.rels",
            f'<Relationships xmlns="{REL_NS}"><Relationship Id="rId1" Type="{R_NS}/officeDocument" Target="word/document.xml"/></Relationships>',
        )
        zf.writestr("word/_rels/document.xml.rels", f'<Relationships xmlns="{REL_NS}">{rels}</Relationships>')
        zf.writestr("word/document.xml", f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:body>{document}<w:sectPr/></w:body></w:document>')
        if comments:
            zf.writestr("word/comments.xml", f'<w:comments xmlns:w="{W_NS}">{comments}</w:comments>')


TRACKED_DOCUMENT = (
    '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Yêu cầu chức năng</w:t></w:r></w:p>'
    "<w:tbl><w:tr>"
    "<w:tc><w:p><w:r><w:t>FR-AUTH-001</w:t></w:r></w:p></w:tc>"
    '<w:tc><w:p><w:r><w:t xml:space="preserve">Khóa tài khoản sau </w:t></w:r>'
    '<w:del w:id="1" w:author="Khách hàng" w:date="2026-11-20T09:00:00Z"><w:r><w:delText>5 lần</w:delText></w:r></w:del>'
    '<w:ins w:id="2" w:author="Khách hàng" w:date="2026-11-20T09:00:00Z"><w:r><w:t>3 lần</w:t></w:r></w:ins>'
    '<w:r><w:t xml:space="preserve"> đăng nhập sai</w:t></w:r></w:p></w:tc>'
    "</w:tr></w:tbl>"
    '<w:p><w:commentRangeStart w:id="0"/><w:r><w:t>US-AUTH-001: Là bệnh nhân, tôi muốn đăng nhập bằng mật khẩu</w:t></w:r>'
    '<w:commentRangeEnd w:id="0"/><w:r><w:commentReference w:id="0"/></w:r></w:p>'
)
TRACKED_COMMENTS = (
    '<w:comment w:id="0" w:author="Trưởng khoa" w:date="2026-11-20T10:00:00Z">'
    "<w:p><w:r><w:t>Cần thêm đăng nhập bằng VNeID</w:t></w:r></w:p></w:comment>"
)


class MarkdownToDocxTests(unittest.TestCase):
    def test_sample_converts_to_valid_package_with_embedded_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            md = write_sample(Path(tmp))
            out = Path(tmp) / "srs-mau.docx"
            counts = md_to_docx.convert(md, out)
            self.assertEqual(counts["images"], 1)
            self.assertEqual(counts["tables"], 1)
            with zipfile.ZipFile(out) as zf:
                names = zf.namelist()
                for part in REQUIRED_PARTS:
                    self.assertIn(part, names)
                for name in names:
                    if name.endswith((".xml", ".rels")):
                        ET.fromstring(zf.read(name))  # raises on malformed XML
                self.assertIn("word/media/md_image1.png", names)
                self.assertEqual(zf.read("word/media/md_image1.png"), tiny_png())
                document = zf.read("word/document.xml").decode("utf-8")
                rels = zf.read("word/_rels/document.xml.rels").decode("utf-8")
                text = doc_text(zf)
                numbering = zf.read("word/numbering.xml").decode("utf-8")

            self.assertIn("r:embed=", document)
            self.assertIn('Target="https://dichvucong.gov.vn" TargetMode="External"', rels)
            self.assertIn("<w:hyperlink", document)
            for style in ("Title", "Heading2", "Heading3", "Heading4", "Heading5", "Heading6", "Code", "Quote", "ListParagraph", "TableGrid"):
                self.assertIn(f'w:val="{style}"', document, style)
            self.assertIn("<w:tblHeader/>", document)
            self.assertIn("<w:br/>", document)
            self.assertIn(md_to_docx.MERMAID_NOTE, text)
            self.assertIn("[Ảnh: Ảnh thiếu]", text)
            self.assertNotIn("ghi chú nội bộ", text)
            self.assertIn("Khóa tài khoản sau 5 lần đăng nhập sai", text)
            self.assertIn("Đặt lại mật khẩu qua SMS | email", text)
            self.assertIn('def kiem_tra(): return "Đã khóa"', text)
            self.assertNotIn("**", text)
            for num_id in set(re.findall(r'<w:numId w:val="(\d+)"/>', document)):
                self.assertIn(f'<w:num w:numId="{num_id}">', numbering)
            self.assertIn('<w:ilvl w:val="2"/>', document)  # third nesting level

    def test_round_trip_keeps_headings_ids_and_table_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            md = write_sample(Path(tmp))
            result = run_script("md_to_docx.py", str(md), "--out-dir", str(Path(tmp) / "out"))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("bảng: 1", result.stdout)
            back_dir = Path(tmp) / "back"
            result = run_script("docx_to_md.py", str(Path(tmp) / "out" / "srs-mau.docx"), "--out-dir", str(back_dir))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            back = (back_dir / "srs-mau.md").read_text(encoding="utf-8")

        lines = {line.lstrip("#").strip() for line in back.splitlines()}
        for heading in re.findall(r"^#{1,6} (.+)$", SAMPLE_MD, flags=re.M):
            self.assertIn(heading, lines, heading)
        self.assertEqual(all_ids(back), all_ids(SAMPLE_MD))
        self.assertIn("| FR-AUTH-001 | Khóa tài khoản sau 5 lần đăng nhập sai | BRQ-01 |", back)
        self.assertIn("| FR-AUTH-002 | Đặt lại mật khẩu qua SMS \\| email | BRQ-01, US-AUTH-001 |", back)
        self.assertIn("| NFR-PERF-001 | Phản hồi dưới 2 giây |  |", back)

    def test_template_keeps_header_page_setup_and_adds_missing_styles(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template = root / "mau-benh-vien.docx"
            styles = (
                f'<w:styles xmlns:w="{W_NS}">'
                '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
                '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>'
                '<w:rPr><w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:color w:val="C00000"/></w:rPr></w:style>'
                '<w:style w:type="paragraph" w:styleId="TieuDe2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/></w:style>'
                '<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/></w:style>'
                "</w:styles>"
            )
            sect = (
                '<w:sectPr><w:headerReference w:type="default" r:id="rId7"/><w:pgSz w:w="11906" w:h="16838"/>'
                '<w:pgMar w:top="1418" w:right="1134" w:bottom="1134" w:left="1701" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'
            )
            with zipfile.ZipFile(template, "w") as zf:
                zf.writestr(
                    "[Content_Types].xml",
                    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                    '<Default Extension="xml" ContentType="application/xml"/>'
                    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
                    '<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
                    "</Types>",
                )
                zf.writestr("_rels/.rels", f'<Relationships xmlns="{REL_NS}"><Relationship Id="rId1" Type="{R_NS}/officeDocument" Target="word/document.xml"/></Relationships>')
                zf.writestr(
                    "word/_rels/document.xml.rels",
                    f'<Relationships xmlns="{REL_NS}"><Relationship Id="rId1" Type="{R_NS}/styles" Target="styles.xml"/>'
                    f'<Relationship Id="rId7" Type="{R_NS}/header" Target="header1.xml"/></Relationships>',
                )
                zf.writestr("word/document.xml", f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:body><w:p><w:r><w:t>Trang bìa</w:t></w:r></w:p>{sect}</w:body></w:document>')
                zf.writestr("word/styles.xml", styles)
                zf.writestr("word/header1.xml", f'<w:hdr xmlns:w="{W_NS}"><w:p><w:r><w:t>BỆNH VIỆN ĐA KHOA TỈNH</w:t></w:r></w:p></w:hdr>')

            md = write_sample(root)
            result = run_script("md_to_docx.py", str(md), "--template", str(template))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with zipfile.ZipFile(root / "srs-mau.docx") as zf:
                for name in zf.namelist():
                    if name.endswith((".xml", ".rels")):
                        ET.fromstring(zf.read(name))
                self.assertIn("BỆNH VIỆN ĐA KHOA TỈNH", zf.read("word/header1.xml").decode("utf-8"))
                document = zf.read("word/document.xml").decode("utf-8")
                rels = ET.fromstring(zf.read("word/_rels/document.xml.rels"))
                styles_out = zf.read("word/styles.xml").decode("utf-8")
                content_types = zf.read("[Content_Types].xml").decode("utf-8")

            header_rid = re.search(r'<w:headerReference w:type="default" r:id="([^"]+)"/>', document).group(1)
            targets = {rel.get("Id"): rel.get("Target") for rel in rels}
            self.assertEqual(targets[header_rid], "header1.xml")
            self.assertIn('w:left="1701"', document)
            self.assertIn('PartName="/word/header1.xml"', content_types)
            self.assertIn("Cambria", styles_out)  # template's own Heading1 is kept
            defined = set(re.findall(r'w:styleId="([^"]+)"', styles_out))
            for needed in ("Heading1", "Heading3", "Heading6", "Title", "TableGrid", "Code", "Quote", "ListParagraph", "Hyperlink"):
                self.assertIn(needed, defined)
            used = set(re.findall(r'<w:(?:pStyle|rStyle|tblStyle) w:val="([^"]+)"', document))
            self.assertTrue(used <= defined, used - defined)
            self.assertIn('w:val="TieuDe2"', document)  # localized "heading 2" id is reused
            self.assertNotIn('w:styleId="Heading2"', styles_out)

    def test_refuses_to_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            md = write_sample(Path(tmp))
            self.assertEqual(run_script("md_to_docx.py", str(md)).returncode, 0)
            out = Path(tmp) / "srs-mau.docx"
            out.write_bytes(b"ban cu")
            refused = run_script("md_to_docx.py", str(md))
            self.assertEqual(refused.returncode, 1)
            self.assertIn("--force", refused.stdout)
            self.assertEqual(out.read_bytes(), b"ban cu")
            self.assertEqual(run_script("md_to_docx.py", str(Path(tmp)), "--force").returncode, 0)
            self.assertTrue(zipfile.is_zipfile(out))
            self.assertEqual(run_script("md_to_docx.py", str(Path(tmp) / "khong-co.md")).returncode, 2)


class DocxFeedbackTests(unittest.TestCase):
    def test_tracked_changes_and_comment_are_anchored_to_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "srs-tra-ve.docx"
            build_docx(path, TRACKED_DOCUMENT, TRACKED_COMMENTS)
            report = docx_feedback.build_report(docx_feedback.FeedbackReader(path))

        rows = [line for line in report.splitlines() if line.startswith("| ") and not line.startswith("| #")]
        deleted = next(line for line in rows if "| Xóa |" in line)
        inserted = next(line for line in rows if "| Thêm |" in line)
        comment = next(line for line in rows if "| Bình luận |" in line)
        self.assertIn("FR-AUTH-001", deleted)
        self.assertIn("5 lần", deleted)
        self.assertIn("FR-AUTH-001", inserted)
        self.assertIn("3 lần", inserted)
        self.assertIn("Khách hàng", inserted)
        self.assertIn("2026-11-20 09:00", inserted)
        self.assertIn("US-AUTH-001", comment)
        self.assertIn("VNeID", comment)
        self.assertIn("Trưởng khoa", comment)
        pair = next(line for line in report.splitlines() if line.startswith("- **FR-AUTH-001**"))
        self.assertRegex(pair, r"5 lần.*→.*3 lần")
        self.assertIn("Việc cần làm", report)
        self.assertIn("L3", report)

    def test_no_feedback_message_and_bad_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sach.docx"
            build_docx(path, "<w:p><w:r><w:t>FR-AUTH-001 Không đổi</w:t></w:r></w:p>")
            result = run_script("docx_feedback.py", str(path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(docx_feedback.NO_FEEDBACK, result.stdout)
            not_docx = Path(tmp) / "khong-phai.docx"
            not_docx.write_text("không phải zip", encoding="utf-8")
            self.assertEqual(run_script("docx_feedback.py", str(not_docx)).returncode, 2)
            self.assertEqual(run_script("docx_feedback.py", str(Path(tmp) / "thieu.docx")).returncode, 2)

    def test_baseline_detects_changed_and_added_ids(self):
        baseline = (
            "# SRS\n\n| Mã | Mô tả |\n|---|---|\n"
            "| FR-AUTH-001 | Khóa tài khoản sau **5 lần** đăng nhập sai |\n"
            "| FR-AUTH-002 | Đặt lại mật khẩu qua SMS |\n"
        )
        edited = baseline.replace("**5 lần**", "3 lần") + "| FR-AUTH-003 | Đăng nhập bằng VNeID |\n"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "goc.md").write_text(baseline, encoding="utf-8")
            (root / "khach-sua.md").write_text(edited, encoding="utf-8")
            md_to_docx.convert(root / "khach-sua.md", root / "khach-sua.docx")
            out = root / "phan-hoi.md"
            result = run_script("docx_feedback.py", str(root / "khach-sua.docx"), "--baseline", str(root / "goc.md"), "--out", str(out))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(docx_feedback.NO_FEEDBACK, result.stdout)
            report = out.read_text(encoding="utf-8")

            tracked = root / "tracked.docx"
            build_docx(tracked, TRACKED_DOCUMENT, TRACKED_COMMENTS)
            tracked_report = docx_feedback.build_report(docx_feedback.FeedbackReader(tracked), root / "goc.md")

        self.assertIn("## So với bản Markdown gốc", report)
        self.assertIn("ID mới xuất hiện trong Word: FR-AUTH-003", report)
        self.assertIn("ID có nội dung thay đổi: FR-AUTH-001", report)
        self.assertNotIn("FR-AUTH-002 |", report)
        self.assertRegex(report, r"\| FR-AUTH-001 \| .*5 lần.* \| .*3 lần.* \|")
        # With tracked changes the comparison uses the accepted text ("3 lần").
        self.assertIn("ID có nội dung thay đổi: FR-AUTH-001", tracked_report)
        self.assertIn("FR-AUTH-002", tracked_report.split("không còn trong Word:")[1].splitlines()[0])


if __name__ == "__main__":
    unittest.main()
