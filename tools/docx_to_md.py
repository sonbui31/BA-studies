#!/usr/bin/env python3
"""Small DOCX to Markdown converter for local BA documents.

It preserves the document order for paragraphs, tables, and embedded images.
The converter intentionally avoids external dependencies so it can run in a
plain Python environment.
"""

from __future__ import annotations

import argparse
import html
import os
import posixpath
import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "v": "urn:schemas-microsoft-com:vml",
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
}


def qn(prefix: str, name: str) -> str:
    return f"{{{NS[prefix]}}}{name}"


def attr(el: ET.Element, prefix: str, name: str) -> str | None:
    return el.attrib.get(qn(prefix, name))


def read_xml(zf: zipfile.ZipFile, name: str) -> ET.Element:
    return ET.fromstring(zf.read(name))


def load_relationships(zf: zipfile.ZipFile) -> dict[str, str]:
    rels_path = "word/_rels/document.xml.rels"
    if rels_path not in zf.namelist():
        return {}
    root = read_xml(zf, rels_path)
    rels: dict[str, str] = {}
    for rel in root.findall("rel:Relationship", NS):
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rid and target:
            rels[rid] = target
    return rels


def load_styles(zf: zipfile.ZipFile) -> dict[str, str]:
    if "word/styles.xml" not in zf.namelist():
        return {}
    root = read_xml(zf, "word/styles.xml")
    styles: dict[str, str] = {}
    for style in root.findall("w:style", NS):
        sid = attr(style, "w", "styleId")
        name = style.find("w:name", NS)
        if sid and name is not None:
            styles[sid] = attr(name, "w", "val") or sid
    return styles


def sanitize_filename(name: str) -> str:
    base = Path(name).stem
    base = re.sub(r"[^\w.-]+", "_", base, flags=re.UNICODE).strip("_")
    return base or "document"


def md_escape_cell(text: str) -> str:
    text = text.replace("\n", "<br>")
    return text.replace("|", "\\|").strip()


def normalize_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def image_label(doc_name: str, rel_id: str, target: str, index: int) -> str:
    ext = Path(target).suffix or ".png"
    return f"{doc_name}_image_{index:02d}{ext}"


class Converter:
    def __init__(self, docx_path: Path, output_path: Path, media_dir: Path) -> None:
        self.docx_path = docx_path
        self.output_path = output_path
        self.media_dir = media_dir
        self.doc_stem = sanitize_filename(docx_path.name)
        self.image_count = 0
        self.copied_by_rid: dict[str, str] = {}
        self.lines: list[str] = []

    def convert(self) -> None:
        with zipfile.ZipFile(self.docx_path) as zf:
            self.rels = load_relationships(zf)
            self.styles = load_styles(zf)
            root = read_xml(zf, "word/document.xml")
            body = root.find("w:body", NS)
            if body is None:
                raise ValueError(f"No document body found in {self.docx_path}")

            self.lines.append(f"# {Path(self.docx_path).stem}")
            self.lines.append("")
            for child in body:
                if child.tag == qn("w", "p"):
                    block = self.paragraph_to_md(child, zf)
                    if block:
                        self.append_block(block)
                elif child.tag == qn("w", "tbl"):
                    table = self.table_to_md(child, zf)
                    if table:
                        self.append_block(table)

        self.output_path.write_text("\n".join(self.lines).rstrip() + "\n", encoding="utf-8")

    def append_block(self, block: str) -> None:
        block = block.rstrip()
        if not block:
            return
        if self.lines and self.lines[-1] != "":
            self.lines.append("")
        self.lines.extend(block.splitlines())
        self.lines.append("")

    def paragraph_style(self, p: ET.Element) -> str:
        pstyle = p.find("w:pPr/w:pStyle", NS)
        if pstyle is None:
            return ""
        sid = attr(pstyle, "w", "val") or ""
        return self.styles.get(sid, sid)

    def paragraph_prefix(self, p: ET.Element) -> str:
        style = self.paragraph_style(p).lower().replace(" ", "")
        if "heading1" in style or style in {"title"}:
            return "# "
        if "heading2" in style:
            return "## "
        if "heading3" in style:
            return "### "
        if "heading4" in style:
            return "#### "
        if p.find("w:pPr/w:numPr", NS) is not None:
            return "- "
        return ""

    def paragraph_to_md(self, p: ET.Element, zf: zipfile.ZipFile) -> str:
        chunks: list[str] = []
        for node in p.iter():
            if node.tag == qn("w", "t"):
                chunks.append(node.text or "")
            elif node.tag == qn("w", "tab"):
                chunks.append("\t")
            elif node.tag == qn("w", "br"):
                chunks.append("\n")
            elif node.tag == qn("a", "blip"):
                rid = attr(node, "r", "embed") or attr(node, "r", "link")
                if rid:
                    chunks.append(self.image_markdown(rid, zf))
            elif node.tag == qn("v", "imagedata"):
                rid = attr(node, "r", "id")
                if rid:
                    chunks.append(self.image_markdown(rid, zf))

        text = normalize_text("".join(chunks))
        if not text:
            return ""

        prefix = self.paragraph_prefix(p)
        if prefix.startswith("#"):
            level = prefix.count("#")
            if level == 1 and self.lines and self.lines[0] == f"# {Path(self.docx_path).stem}":
                prefix = "## "
            return f"{prefix}{text}"
        if prefix:
            return "\n".join(f"{prefix}{line}" if line else "" for line in text.splitlines())
        return text

    def image_markdown(self, rid: str, zf: zipfile.ZipFile) -> str:
        target = self.rels.get(rid)
        if not target:
            return f"[missing image: {rid}]"
        if target.startswith("http://") or target.startswith("https://"):
            return f"![{rid}]({target})"

        source = posixpath.normpath(posixpath.join("word", target))
        if source not in zf.namelist():
            return f"[missing image file: {html.escape(target)}]"

        if rid not in self.copied_by_rid:
            self.image_count += 1
            output_name = image_label(self.doc_stem, rid, target, self.image_count)
            self.media_dir.mkdir(parents=True, exist_ok=True)
            out_path = self.media_dir / output_name
            with zf.open(source) as src, out_path.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            self.copied_by_rid[rid] = os.path.relpath(out_path, self.output_path.parent)

        rel_path = self.copied_by_rid[rid].replace(os.sep, "/")
        return f"\n\n![Sơ đồ/Hình {self.image_count}]({rel_path})\n\n"

    def cell_to_text(self, cell: ET.Element, zf: zipfile.ZipFile) -> str:
        parts: list[str] = []
        for p in cell.findall("w:p", NS):
            text = self.paragraph_to_md(p, zf)
            if text:
                parts.append(text)
        return normalize_text("\n".join(parts))

    def table_to_md(self, tbl: ET.Element, zf: zipfile.ZipFile) -> str:
        rows: list[list[str]] = []
        for tr in tbl.findall("w:tr", NS):
            row: list[str] = []
            for tc in tr.findall("w:tc", NS):
                row.append(md_escape_cell(self.cell_to_text(tc, zf)))
            if any(row):
                rows.append(row)
        if not rows:
            return ""

        width = max(len(row) for row in rows)
        rows = [row + [""] * (width - len(row)) for row in rows]
        header = rows[0]
        sep = ["---"] * width
        md_rows = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(sep) + " |",
        ]
        for row in rows[1:]:
            md_rows.append("| " + " | ".join(row) + " |")
        return "\n".join(md_rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", nargs="+", type=Path)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--media-dir-name", default="media")
    args = parser.parse_args()

    for docx_path in args.docx:
        out_dir = args.out_dir or docx_path.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        output_path = out_dir / f"{Path(docx_path).stem}.md"
        media_dir = out_dir / args.media_dir_name
        Converter(docx_path, output_path, media_dir).convert()
        print(output_path)


if __name__ == "__main__":
    main()
