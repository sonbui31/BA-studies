#!/usr/bin/env python3
"""Pull customer feedback (tracked changes and comments) out of a returned Word file.

Every change and comment is anchored to a requirement ID (same paragraph, else same table
row, else the nearest preceding heading) so the BA can turn it into a Change Request and
update the Markdown source. With --baseline the accepted Word text is also compared with the
Markdown source by ID, which catches edits made without Track Changes.

Usage:
    python docx_feedback.py <returned.docx> [--baseline source.md] [--out report.md]
"""

from __future__ import annotations

import argparse
import os
import sys
import unicodedata
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ba_id_utils import extract_ids_from_line, find_project_scheme, load_project_scheme, set_project_scheme  # noqa: E402
from docx_to_md import NS, attr, load_styles, qn  # noqa: E402
import md_to_docx  # noqa: E402


W = lambda name: qn("w", name)  # noqa: E731
CHANGE_TAGS = {W("ins"): "ins", W("del"): "del", W("moveFrom"): "moveFrom", W("moveTo"): "moveTo"}
KIND_LABEL = {"ins": "Thêm", "del": "Xóa", "moveFrom": "Di chuyển", "moveTo": "Di chuyển", "fmt": "Định dạng", "comment": "Bình luận"}
ORIGINAL_KINDS = {None, "del", "moveFrom"}
ACCEPTED_KINDS = {None, "ins", "moveTo"}
NO_FEEDBACK = "Không có thay đổi theo dõi hoặc bình luận."
MAX_CELL = 300


# --------------------------------------------------------------------------------------------
# Text helpers
# --------------------------------------------------------------------------------------------

def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text.replace(" ", " "))
    return re.sub(r"\s+", " ", text).strip()


def first_id(text: str) -> Optional[str]:
    """First BA ID by position in the text."""
    ids = extract_ids_from_line(text)
    return min(ids, key=lambda token: text.find(token)) if ids else None


def element_texts(el: ET.Element) -> Tuple[str, str]:
    """(original, accepted) text of a paragraph/cell/row: original keeps deletions and drops
    insertions, accepted is the text with every tracked change accepted."""
    original: List[str] = []
    accepted: List[str] = []

    def add(text: str, kind: Optional[str]) -> None:
        if kind in ORIGINAL_KINDS:
            original.append(text)
        if kind in ACCEPTED_KINDS:
            accepted.append(text)

    def visit(node: ET.Element, kind: Optional[str]) -> None:
        for child in node:
            tag = child.tag
            if tag in CHANGE_TAGS:
                visit(child, CHANGE_TAGS[tag])
            elif tag in (W("pPr"), W("rPr")):
                continue
            elif tag in (W("t"), W("delText")):
                add(child.text or "", kind)
            elif tag in (W("tab"), W("br"), W("cr")):
                add(" ", kind)
            else:
                visit(child, kind)
                if tag == W("p"):
                    add(" ", None)

    visit(el, None)
    return normalize("".join(original)), normalize("".join(accepted))


def short(text: str, limit: int = MAX_CELL) -> str:
    text = normalize(text)
    return text if len(text) <= limit else text[: limit - 1] + "…"


def cell(text: str) -> str:
    return short(text).replace("|", "\\|")


def fmt_date(value: str) -> str:
    return value[:16].replace("T", " ") if value else ""


def diff_snippet(old: str, new: str, context: int = 30) -> Tuple[str, str]:
    """Trim the common prefix/suffix so the changed part is visible."""
    prefix = len(os.path.commonprefix([old, new]))
    suffix = len(os.path.commonprefix([old[prefix:][::-1], new[prefix:][::-1]]))
    start = max(0, prefix - context)
    if start > 0:  # begin at a word boundary so IDs are not cut in half
        start = old.rfind(" ", 0, start) + 1
    lead = "…" if start > 0 else ""

    def piece(text: str) -> str:
        end = len(text) - suffix
        tail_end = min(len(text), end + context)
        return lead + text[start:tail_end] + ("…" if tail_end < len(text) else "")

    return piece(old), piece(new)


# --------------------------------------------------------------------------------------------
# Reading the returned docx
# --------------------------------------------------------------------------------------------

def main_part(zf: zipfile.ZipFile) -> str:
    """Main document part from _rels/.rels (Office Online may save it as word/document2.xml)."""
    if "_rels/.rels" in zf.namelist():
        for rel in ET.fromstring(zf.read("_rels/.rels")):
            if rel.get("Type", "").endswith("/officeDocument"):
                return (rel.get("Target") or "word/document.xml").lstrip("/")
    return "word/document.xml"


def part_target(zf: zipfile.ZipFile, part: str, rel_suffix: str) -> Optional[str]:
    """Resolve the first internal relationship of `part` whose type ends with rel_suffix."""
    rels = md_to_docx._rels_name(part)
    if rels in zf.namelist():
        for rel in ET.fromstring(zf.read(rels)):
            if rel.get("Type", "").endswith("/" + rel_suffix) and rel.get("TargetMode") != "External":
                return md_to_docx._resolve(part, rel.get("Target", ""))
    return None

@dataclass
class Item:
    seq: int
    kind: str
    anchor: str
    content: str
    author: str
    date: str


@dataclass
class Para:
    anchor: str
    original: str
    accepted: str


class FeedbackReader:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.items: List[Item] = []
        self.pairs: List[Tuple[str, str, str, str]] = []  # (anchor, old, new, authors)
        self.paras: List[Para] = []
        self.units: List[str] = []  # accepted text per paragraph (outside tables) or table row
        self.heading: Optional[str] = None
        self.seq = 0
        self.open_comments: Dict[str, List[str]] = {}
        self.comment_text: Dict[str, List[str]] = {}
        self.comment_pos: Dict[str, Tuple[int, int]] = {}  # id -> (paragraph index, seq)
        with zipfile.ZipFile(path) as zf:
            self.styles = load_styles(zf)
            main = main_part(zf)
            root = ET.fromstring(zf.read(main))
            self.comments = self._load_comments(zf, part_target(zf, main, "comments"))
        body = root.find("w:body", NS)
        if body is not None:
            self.walk(body, None)
        self._add_comment_items()

    def next_seq(self) -> int:
        self.seq += 1
        return self.seq

    @staticmethod
    def _load_comments(zf: zipfile.ZipFile, part: Optional[str]) -> Dict[str, Tuple[str, str, str]]:
        if not part or part not in zf.namelist():
            return {}
        root = ET.fromstring(zf.read(part))
        comments: Dict[str, Tuple[str, str, str]] = {}
        for comment in root.findall("w:comment", NS):
            paragraphs = [normalize("".join(t.text or "" for t in p.iter(W("t")))) for p in comment.iter(W("p"))]
            comments[attr(comment, "w", "id") or ""] = (
                attr(comment, "w", "author") or "",
                attr(comment, "w", "date") or "",
                " / ".join(p for p in paragraphs if p),
            )
        return comments

    # -- traversal ----------------------------------------------------------------------------

    def walk(self, el: ET.Element, row_id: Optional[str]) -> None:
        for child in el:
            if child.tag == W("p"):
                self.paragraph(child, row_id)
            elif child.tag == W("tr"):
                self.row(child)
            elif child.tag in (W("commentRangeStart"), W("commentRangeEnd")):
                self.comment_marker(child)
            else:
                self.walk(child, row_id)

    def row(self, tr: ET.Element) -> None:
        original, accepted = element_texts(tr)
        row_id = first_id(original) or first_id(accepted)
        cells = tr.findall("w:tc", NS) + tr.findall("w:sdt/w:sdtContent/w:tc", NS)
        self.units.append(" | ".join(element_texts(tc)[1] for tc in cells))
        self.walk(tr, row_id)

    def comment_marker(self, node: ET.Element) -> None:
        cid = attr(node, "w", "id") or ""
        if node.tag == W("commentRangeStart"):
            self.open_comments[cid] = []
            self.comment_pos.setdefault(cid, (len(self.paras), self.next_seq()))
        elif node.tag == W("commentRangeEnd") and cid in self.open_comments:
            self.comment_text[cid] = self.open_comments.pop(cid)
        elif node.tag == W("commentReference"):
            self.comment_pos.setdefault(cid, (len(self.paras), self.next_seq()))

    def is_heading(self, p: ET.Element) -> bool:
        style = p.find("w:pPr/w:pStyle", NS)
        name = self.styles.get(attr(style, "w", "val") or "", attr(style, "w", "val") or "") if style is not None else ""
        name = name.lower().replace(" ", "")
        outline = p.find("w:pPr/w:outlineLvl", NS)
        level = attr(outline, "w", "val") if outline is not None else None
        return name.startswith("heading") or name == "title" or (level is not None and level.isdigit() and int(level) < 9)

    def paragraph(self, p: ET.Element, row_id: Optional[str]) -> None:
        segments: List[Tuple[str, Optional[Tuple[str, str, str]], int]] = []
        formats: List[Tuple[str, str, str, int]] = []

        def visit(node: ET.Element, change: Optional[Tuple[str, str, str]]) -> None:
            for child in node:
                tag = child.tag
                if tag in CHANGE_TAGS:
                    visit(child, (CHANGE_TAGS[tag], attr(child, "w", "author") or "", attr(child, "w", "date") or ""))
                elif tag == W("pPr"):
                    change_el = child.find("w:pPrChange", NS)
                    if change_el is not None:
                        formats.append(("(định dạng đoạn)", attr(change_el, "w", "author") or "", attr(change_el, "w", "date") or "", self.next_seq()))
                elif tag == W("rPr"):
                    continue
                elif tag == W("r"):
                    change_el = child.find("w:rPr/w:rPrChange", NS)
                    if change_el is not None:
                        text = "".join(t.text or "" for t in child.iter() if t.tag in (W("t"), W("delText")))
                        if text.strip():
                            formats.append((text, attr(change_el, "w", "author") or "", attr(change_el, "w", "date") or "", self.next_seq()))
                    visit(child, change)
                elif tag in (W("t"), W("delText"), W("tab"), W("br"), W("cr")):
                    text = (child.text or "") if tag in (W("t"), W("delText")) else " "
                    segments.append((text, change, self.next_seq()))
                    if change is None or change[0] in ("ins", "moveTo"):
                        for buffer in self.open_comments.values():
                            buffer.append(text)
                elif tag in (W("commentRangeStart"), W("commentRangeEnd"), W("commentReference")):
                    self.comment_marker(child)
                else:
                    visit(child, change)

        visit(p, None)
        original, accepted = element_texts(p)
        if self.is_heading(p) and accepted:
            self.heading = accepted
        anchor = first_id(original) or first_id(accepted) or row_id
        if not anchor:
            anchor = f"Mục: {self.heading}" if self.heading else "(đầu tài liệu)"
        self.paras.append(Para(anchor, original, accepted))
        if row_id is None:
            self.units.append(accepted)

        # Group consecutive segments of the same change kind and author into one item.
        groups: List[List] = []
        for text, change, seq in segments:
            if change is None:
                groups.append([])
                continue
            if groups and groups[-1] and groups[-1][0] == change[0] and groups[-1][1] == change[1]:
                groups[-1][3] += text
            else:
                groups.append([change[0], change[1], change[2], text, seq])
        kinds = set()
        authors: List[str] = []
        for group in groups:
            if not group or not group[3].strip():
                continue
            kind, author, date, text, seq = group
            kinds.add(kind)
            if author not in authors:
                authors.append(author)
            prefix = {"moveFrom": "(chuyển đi) ", "moveTo": "(chuyển đến) "}.get(kind, "")
            self.items.append(Item(seq, KIND_LABEL[kind], anchor, prefix + normalize(text), author, date))
        if kinds & {"del", "moveFrom"} and kinds & {"ins", "moveTo"}:
            self.pairs.append((anchor, original, accepted, ", ".join(a for a in authors if a)))

        merged: Dict[str, List] = {}
        for text, author, date, seq in formats:
            entry = merged.setdefault(author, [[], date, seq])
            entry[0].append(text)
        for author, (texts, date, seq) in merged.items():
            self.items.append(Item(seq, KIND_LABEL["fmt"], anchor, normalize(" ".join(texts)), author, date))

    def _add_comment_items(self) -> None:
        for cid, (author, date, text) in self.comments.items():
            index, seq = self.comment_pos.get(cid, (len(self.paras), self.next_seq()))
            if index < len(self.paras):
                anchor = self.paras[index].anchor
            else:
                anchor = f"Mục: {self.heading}" if self.heading else "(cuối tài liệu)"
            anchored = normalize("".join(self.comment_text.get(cid, self.open_comments.get(cid, []))))
            content = text + (f' — trên đoạn: "{short(anchored, 120)}"' if anchored else "")
            self.items.append(Item(seq, KIND_LABEL["comment"], anchor, content, author, date))
        self.items.sort(key=lambda item: item.seq)


# --------------------------------------------------------------------------------------------
# Baseline comparison
# --------------------------------------------------------------------------------------------

IMAGE_PLACEHOLDER = re.compile(r"\[Ảnh: [^\]]*\]")


def markdown_units(text: str) -> List[str]:
    """Visible text per paragraph / list item / table row, as md_to_docx renders it."""
    units: List[str] = []
    for block in md_to_docx.parse_blocks(text):
        if block.kind in ("heading", "para"):
            units.append(md_to_docx.plain_text(block.text))
        elif block.kind == "list":
            units.extend(md_to_docx.plain_text(item[3]) for item in block.items)
        elif block.kind == "table":
            units.extend(" | ".join(normalize(md_to_docx.plain_text(c)) for c in row) for row in block.rows)
        elif block.kind == "quote":
            units.extend(md_to_docx.plain_text(line) for line in block.lines)
        elif block.kind == "code":
            units.extend(block.lines)
    return [normalize(unit) for unit in units]


def index_units(units: List[str]) -> Tuple[Dict[str, List[str]], set]:
    by_id: Dict[str, List[str]] = {}
    mentioned: set = set()
    for unit in units:
        unit = normalize(IMAGE_PLACEHOLDER.sub("", unit))
        ids = extract_ids_from_line(unit)
        mentioned.update(ids)
        key = first_id(unit)
        if key:
            by_id.setdefault(key, []).append(unit)
    return by_id, mentioned


def compare_baseline(reader: FeedbackReader, baseline: Path) -> List[str]:
    md_by_id, md_ids = index_units(markdown_units(baseline.read_text(encoding="utf-8")))
    doc_by_id, doc_ids = index_units(reader.units)
    added = sorted(doc_ids - md_ids)
    removed = sorted(md_ids - doc_ids)
    changed = [key for key in md_by_id if key in doc_by_id and md_by_id[key] != doc_by_id[key]]

    lines = ["## So với bản Markdown gốc", "", f"Bản gốc: `{baseline.name}` (so trên văn bản Word đã chấp nhận mọi thay đổi).", ""]
    lines.append(f"- ID mới xuất hiện trong Word: {', '.join(added) if added else 'không có'}")
    lines.append(f"- ID có trong Markdown nhưng không còn trong Word: {', '.join(removed) if removed else 'không có'}")
    lines.append(f"- ID có nội dung thay đổi: {', '.join(changed) if changed else 'không có'}")
    if changed:
        lines += ["", "| ID | Markdown | Word |", "|---|---|---|"]
        for key in changed:
            old, new = diff_snippet(" ¶ ".join(md_by_id[key]), " ¶ ".join(doc_by_id[key]))
            lines.append(f"| {key} | {cell(old)} | {cell(new)} |")
    lines.append("")
    return lines


# --------------------------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------------------------

def build_report(reader: FeedbackReader, baseline: Optional[Path] = None) -> str:
    items = reader.items
    changes = [item for item in items if item.kind != KIND_LABEL["comment"]]
    comments = [item for item in items if item.kind == KIND_LABEL["comment"]]
    authors = sorted({item.author for item in items if item.author})
    lines = [f"# Phản hồi từ file Word: {reader.path.name}", ""]
    if not items:
        lines += [NO_FEEDBACK, ""]
    else:
        lines.append(f"- Tổng: {len(changes)} thay đổi theo dõi, {len(comments)} bình luận.")
        lines.append(f"- Người góp ý: {', '.join(authors) if authors else 'không ghi tên'}")
        lines += ["", "| # | Loại | ID / Mục | Nội dung | Tác giả | Ngày |", "|---|---|---|---|---|---|"]
        for number, item in enumerate(items, start=1):
            lines.append(
                f"| {number} | {item.kind} | {cell(item.anchor)} | {cell(item.content)} | {cell(item.author)} | {fmt_date(item.date)} |"
            )
        lines.append("")
    if reader.pairs:
        lines += ["## Đoạn vừa xóa vừa thêm (cũ → mới)", ""]
        for anchor, old, new, who in reader.pairs:
            by = f" ({who})" if who else ""
            lines.append(f'- **{anchor}**{by}: "{short(old)}" → "{short(new)}"')
        lines.append("")
    if baseline is not None:
        lines += compare_baseline(reader, baseline)
    lines += [
        "## Việc cần làm",
        "",
        "1. Thay đổi về nội dung (phạm vi, quy tắc nghiệp vụ, con số, tiêu chí chấp nhận) xử lý như "
        "Change Request theo lối L3: ghi Change Log, phân tích tác động lên các ID liên quan, xin xác nhận trước khi sửa.",
        "2. Sửa file Markdown gốc (nguồn chuẩn), rồi xuất lại Word bằng `md_to_docx.py`. Không sửa tiếp trên file Word này.",
        "3. Trả lời từng bình luận của khách hàng và ghi quyết định vào biên bản hoặc Change Log.",
        "4. Thay đổi chỉ về định dạng không cần Change Request; nếu cần thì cập nhật template.",
        "",
    ]
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="Trích thay đổi theo dõi và bình luận từ file Word khách hàng gửi lại.")
    parser.add_argument("docx", type=Path, help="File .docx khách hàng gửi lại")
    parser.add_argument("--baseline", type=Path, default=None, help="File Markdown gốc để so theo ID")
    parser.add_argument("--out", type=Path, default=None, help="Ghi báo cáo Markdown ra file")
    args = parser.parse_args(argv)

    if not args.docx.is_file():
        print(f"LỖI: không tìm thấy file {args.docx}")
        return 2
    if args.baseline is not None and not args.baseline.is_file():
        print(f"LỖI: không tìm thấy file Markdown gốc {args.baseline}")
        return 2
    try:
        reader = FeedbackReader(args.docx)
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
        print(f"LỖI: {args.docx} không phải file .docx hợp lệ ({exc})")
        return 2

    # Project-specific IDs (ba-scheme.json next to the Markdown source or the returned file).
    scheme_path = find_project_scheme(args.baseline if args.baseline is not None else args.docx)
    set_project_scheme(load_project_scheme(scheme_path) if scheme_path else None)
    report = build_report(reader, args.baseline)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
        if not reader.items:
            print(NO_FEEDBACK)
        print(f"Đã ghi báo cáo: {args.out} ({len(reader.items)} mục phản hồi)")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
