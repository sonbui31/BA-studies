#!/usr/bin/env python3
"""Markdown to DOCX exporter for BA documents (stdlib only).

Builds a Word package with zipfile so a BA can send the Markdown source to a customer as a
.docx, optionally on the customer's own template (styles, theme, fonts, headers/footers,
page setup). The Markdown file stays the source of truth; see docx_feedback.py for the way
back.

Usage:
    python md_to_docx.py <file.md|folder> [--out-dir DIR] [--template ref.docx] [--force]
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import io
import json
import os
import posixpath
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import urllib.parse
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
RT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/"
RT_CORE = "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties"

CT_MAIN = "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
CT_STYLES = "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"
CT_NUMBERING = "application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"
CT_SETTINGS = "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"
CT_CORE = "application/vnd.openxmlformats-package.core-properties+xml"
CT_APP = "application/vnd.openxmlformats-officedocument.extended-properties+xml"
CT_RELS = "application/vnd.openxmlformats-package.relationships+xml"

DOC_NAMESPACES = (
    'xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" '
    'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
    'xmlns:o="urn:schemas-microsoft-com:office:office" '
    f'xmlns:r="{R_NS}" '
    'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
    'xmlns:v="urn:schemas-microsoft-com:vml" '
    'xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" '
    'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
    'xmlns:w10="urn:schemas-microsoft-com:office:word" '
    f'xmlns:w="{W_NS}" '
    'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
    'xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" '
    'xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" '
    'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" '
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
    'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" '
    'mc:Ignorable="w14 w15 wp14"'
)

XML_DECL = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
MERMAID_NOTE = "[Sơ đồ Mermaid — xem bản Markdown hoặc ảnh xuất kèm]"
CODE_FONT = "Courier New"  # has Vietnamese glyphs, unlike several modern monospace fonts
BODY_FONT = "Times New Roman"
HEADING_FONT = "Arial"
TEXT_WIDTH_TWIPS = 9638  # A4 (11906) minus 2 x 2 cm margins
MAX_IMAGE_EMU = 16 * 360000  # 16 cm
EMU_PER_TWIP = 635
# A diagram this wide (BPMN with lanes, long flowcharts) is unreadable on a portrait page:
# it goes on a landscape page of its own.
WIDE_IMAGE_RATIO = 1.3
WIDE_IMAGE_MIN_PX = 1400
IMAGE_ONLY_PARA = re.compile(r"^!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)$")
IMAGE_WITH_CAPTION = re.compile(r"^(!\[[^\]]*\]\([^)\s]+(?:\s+\"[^\"]*\")?\))\s+(\S.*)$", re.S)
EMU_PER_PX = 9525  # 96 dpi

# Logical style -> canonical Word style name (used to find localized style ids in templates).
STYLE_NAMES = {
    "Title": "Title",
    "Heading1": "heading 1",
    "Heading2": "heading 2",
    "Heading3": "heading 3",
    "Heading4": "heading 4",
    "Heading5": "heading 5",
    "Heading6": "heading 6",
    "TableGrid": "Table Grid",
    "Code": "Code",
    "Quote": "Quote",
    "ListParagraph": "List Paragraph",
    "Hyperlink": "Hyperlink",
}
BASE_STYLE_NAMES = {"Normal": "Normal", "TableNormal": "Normal Table", "DefaultParagraphFont": "Default Paragraph Font"}


# --------------------------------------------------------------------------------------------
# XML helpers
# --------------------------------------------------------------------------------------------

_INVALID_XML = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\ufffe\uffff]")


def esc(text: str, quote: bool = False) -> str:
    """Escape text for XML content (or attribute values when quote=True)."""
    text = _INVALID_XML.sub("", text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if quote:
        text = text.replace('"', "&quot;")
    return text


def w_t(text: str) -> str:
    space = ' xml:space="preserve"' if text != text.strip() or "  " in text else ""
    return f"<w:t{space}>{esc(text)}</w:t>"


# --------------------------------------------------------------------------------------------
# Markdown block parsing
# --------------------------------------------------------------------------------------------

FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([^\s`]*)")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?[ \t]*$")
HR_RE = re.compile(r"^ {0,3}([-*_])(?:[ \t]*\1){2,}[ \t]*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d{1,9}[.)])[ \t]+(.*)$")
QUOTE_RE = re.compile(r"^ {0,3}>")
ALIGN_RE = re.compile(r"^\s*\|?\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)*\|?\s*$")
TASK_RE = re.compile(r"^\[([ xX])\]\s+")


@dataclass
class Block:
    kind: str  # heading | para | list | table | code | quote | hr
    text: str = ""
    level: int = 0
    lang: str = ""
    lines: List[str] = field(default_factory=list)
    items: List[Tuple[int, bool, int, str]] = field(default_factory=list)  # (level, ordered, start, text)
    rows: List[List[str]] = field(default_factory=list)


def _closes_fence(line: str, fence: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and set(stripped) == {fence[0]} and len(stripped) >= len(fence)


def strip_html_comments(text: str) -> str:
    """Drop <!-- ... --> comments (also multi-line) outside fenced code."""
    out: List[str] = []
    fence: Optional[str] = None
    in_comment = False
    for line in text.split("\n"):
        if not in_comment:
            if fence:
                out.append(line)
                if _closes_fence(line, fence):
                    fence = None
                continue
            match = FENCE_RE.match(line)
            if match:
                fence = match.group(2)
                out.append(line)
                continue
        if not in_comment and "<!--" not in line:
            out.append(line)
            continue
        result, rest = "", line
        while rest:
            if in_comment:
                end = rest.find("-->")
                if end < 0:
                    rest = ""
                    break
                rest, in_comment = rest[end + 3:], False
            else:
                start = rest.find("<!--")
                if start < 0:
                    result += rest
                    break
                result, rest, in_comment = result + rest[:start], rest[start + 4:], True
        if result.strip():
            out.append(result)
    return "\n".join(out)


def split_row(line: str) -> List[str]:
    """Split a GFM table row on unescaped pipes."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", s)]


def _is_table_start(lines: List[str], i: int) -> bool:
    return "|" in lines[i] and i + 1 < len(lines) and "|" in lines[i + 1] and bool(ALIGN_RE.match(lines[i + 1]))


def _starts_block(lines: List[str], i: int) -> bool:
    line = lines[i]
    return bool(
        FENCE_RE.match(line)
        or HEADING_RE.match(line)
        or HR_RE.match(line)
        or QUOTE_RE.match(line)
        or LIST_RE.match(line)
        or _is_table_start(lines, i)
    )


def _join_soft(lines: List[str]) -> str:
    """Join paragraph lines: soft breaks become spaces, hard breaks (two spaces / backslash) <br>."""
    parts: List[str] = []
    for index, line in enumerate(lines):
        last = index == len(lines) - 1
        if not last and (line.endswith("  ") or line.endswith("\\")):
            parts.append(line.rstrip(" \\") + "<br>")
        else:
            parts.append(line.strip() + ("" if last else " "))
    return "".join(parts).strip()


def parse_blocks(text: str) -> List[Block]:
    """Parse the Markdown subset used in BA documents into blocks."""
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    lines = strip_html_comments(text).split("\n")
    blocks: List[Block] = []
    para: List[str] = []
    n = len(lines)
    i = 0

    def flush_para() -> None:
        if para:
            blocks.append(Block("para", text=_join_soft(para)))
            para.clear()

    while i < n:
        line = lines[i]
        if not line.strip():
            flush_para()
            i += 1
            continue

        fence = FENCE_RE.match(line)
        if fence:
            flush_para()
            indent, marker, lang = len(fence.group(1)), fence.group(2), fence.group(3).lower()
            body: List[str] = []
            i += 1
            while i < n and not _closes_fence(lines[i], marker):
                raw = lines[i]
                strip = min(indent, len(raw) - len(raw.lstrip(" ")))
                body.append(raw[strip:].expandtabs(4))
                i += 1
            i += 1  # closing fence (or EOF)
            blocks.append(Block("code", lang=lang, lines=body))
            continue

        heading = HEADING_RE.match(line)
        if heading:
            flush_para()
            title = re.sub(r"[ \t]+#+[ \t]*$", "", heading.group(2) or "").strip()
            blocks.append(Block("heading", level=len(heading.group(1)), text=title))
            i += 1
            continue

        if HR_RE.match(line):
            flush_para()
            blocks.append(Block("hr"))
            i += 1
            continue

        if _is_table_start(lines, i):
            flush_para()
            rows = [split_row(line)]
            i += 2
            while i < n and lines[i].strip() and "|" in lines[i]:
                rows.append(split_row(lines[i]))
                i += 1
            width = max(len(row) for row in rows)
            blocks.append(Block("table", rows=[row + [""] * (width - len(row)) for row in rows]))
            continue

        if QUOTE_RE.match(line):
            flush_para()
            paragraphs: List[List[str]] = [[]]
            while i < n and QUOTE_RE.match(lines[i]):
                inner = re.sub(r"^(\s*>[ \t]?)+", "", lines[i])
                if inner.strip():
                    paragraphs[-1].append(inner.strip())
                elif paragraphs[-1]:
                    paragraphs.append([])
                i += 1
            # Quote lines keep their own line (BA metadata blocks like "> **Trạng thái:** Draft").
            blocks.append(Block("quote", lines=["<br>".join(p) for p in paragraphs if p]))
            continue

        if LIST_RE.match(line):
            flush_para()
            raw_items: List[List] = []
            while i < n:
                cur = lines[i]
                match = LIST_RE.match(cur)
                if match and not HR_RE.match(cur):
                    marker = match.group(2)
                    ordered = marker[0].isdigit()
                    item_text = TASK_RE.sub(lambda m: "☐ " if m.group(1) == " " else "☒ ", match.group(3))
                    raw_items.append([len(match.group(1).expandtabs(4)), ordered, int(marker[:-1]) if ordered else 1, item_text])
                    i += 1
                    continue
                if not cur.strip():
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and (LIST_RE.match(lines[j]) or (lines[j][:1] in (" ", "\t") and not _starts_block(lines, j))):
                        if not LIST_RE.match(lines[j]):
                            raw_items[-1][3] += "<br>"
                        i = j
                        continue
                    break
                if _starts_block(lines, i):
                    break
                last = raw_items[-1][3]
                raw_items[-1][3] = last + ("" if last.endswith("<br>") else " ") + cur.strip()
                i += 1
            stack: List[int] = []
            items: List[Tuple[int, bool, int, str]] = []
            for indent, ordered, start, item_text in raw_items:
                while stack and indent < stack[-1]:
                    stack.pop()
                if not stack or indent > stack[-1]:
                    stack.append(indent)
                items.append((min(len(stack) - 1, 8), ordered, start, item_text.strip()))
            blocks.append(Block("list", items=items))
            continue

        para.append(line)
        i += 1

    flush_para()
    return blocks


# --------------------------------------------------------------------------------------------
# Inline parsing
# --------------------------------------------------------------------------------------------

@dataclass
class Run:
    kind: str  # text | br | image
    text: str = ""
    bold: bool = False
    italic: bool = False
    code: bool = False
    href: Optional[str] = None
    src: str = ""


ESCAPABLE = set("\\`*_{}[]()#+-.!|<>~\"'")
BR_RE = re.compile(r"<br\s*/?>", re.I)
AUTOLINK_RE = re.compile(r"<((?:https?|mailto):[^>\s]+)>", re.I)
# Only well-known inline HTML tags are dropped; "<Tên dự án>"-style placeholders stay visible.
HTML_TAG_RE = re.compile(
    r"</?(?:b|i|u|s|em|strong|span|sup|sub|small|mark|kbd|del|ins|font|center|div|p|a)(?:\s[^<>]*)?/?>", re.I
)
IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(\s*(<[^>]*>|[^)\s]*)(?:\s+"[^"]*")?\s*\)')
LINK_RE = re.compile(r'\[((?:[^\[\]]|\[[^\]]*\])*)\]\(\s*(<[^>]*>|[^)\s]*)(?:\s+"[^"]*")?\s*\)')
CODE_SPAN_RE = re.compile(r"(`+)(.+?)(?<!`)\1(?!`)", re.S)


def _emphasis(text: str, i: int) -> Optional[Tuple[int, int, bool, bool]]:
    """Match emphasis at i. Returns (inner_start, inner_end_exclusive, bold, italic) and the
    caller resumes after the closing delimiter (inner_end + len(delimiter))."""
    ch = text[i]
    prev = text[i - 1] if i > 0 else " "
    if ch == "_" and prev.isalnum():
        return None  # snake_case stays literal
    for size, bold, italic in ((3, True, True), (2, True, False), (1, False, True)):
        delim = ch * size
        if not text.startswith(delim, i):
            continue
        start = i + size
        if start >= len(text) or text[start].isspace() or text[start] == ch and size == 1:
            continue
        pos = start + 1
        while True:
            pos = text.find(delim, pos)
            if pos < 0:
                break
            before = text[pos - 1]
            after = text[pos + size] if pos + size < len(text) else " "
            if not before.isspace() and before != ch and after != ch:
                if ch == "_" and after.isalnum():
                    pos += 1
                    continue
                return start, pos, bold, italic
            pos += 1
    return None


def parse_inline(text: str, bold: bool = False, italic: bool = False, href: Optional[str] = None) -> List[Run]:
    """Turn inline Markdown into a flat list of styled runs."""
    runs: List[Run] = []
    buf: List[str] = []

    def flush() -> None:
        if buf:
            runs.append(Run("text", "".join(buf), bold, italic, False, href))
            buf.clear()

    i = 0
    while i < len(text):
        c = text[i]
        if c == "\\" and i + 1 < len(text) and text[i + 1] in ESCAPABLE:
            buf.append(text[i + 1])
            i += 2
            continue
        if c == "`":
            match = CODE_SPAN_RE.match(text, i)
            if match:
                flush()
                code = match.group(2)
                if code.startswith(" ") and code.endswith(" ") and code.strip():
                    code = code[1:-1]
                runs.append(Run("text", code, bold, italic, True, href))
                i = match.end()
                continue
        if c == "<":
            match = BR_RE.match(text, i)
            if match:
                flush()
                runs.append(Run("br"))
                i = match.end()
                continue
            match = AUTOLINK_RE.match(text, i)
            if match:
                flush()
                url = match.group(1)
                runs.append(Run("text", url, bold, italic, False, href or url))
                i = match.end()
                continue
            match = HTML_TAG_RE.match(text, i)
            if match:
                i = match.end()  # other inline HTML tags are dropped, their content kept
                continue
        if c == "!" and text.startswith("![", i):
            match = IMAGE_RE.match(text, i)
            if match:
                flush()
                runs.append(Run("image", match.group(1), src=match.group(2).strip("<>")))
                i = match.end()
                continue
        if c == "[":
            match = LINK_RE.match(text, i)
            if match:
                flush()
                url = match.group(2).strip("<>")
                is_external = re.match(r"(?i)(https?|mailto):", url) is not None
                runs.extend(parse_inline(match.group(1), bold, italic, (url if is_external else None) or href))
                i = match.end()
                continue
        if c in "*_":
            match = _emphasis(text, i)
            if match:
                start, end, b, it = match
                flush()
                runs.extend(parse_inline(text[start:end], bold or b, italic or it, href))
                i = end + (start - i)
                continue
            # Skip the whole delimiter run so "**" without a partner stays literal.
            j = i
            while j < len(text) and text[j] == c:
                j += 1
            buf.append(text[i:j])
            i = j
            continue
        buf.append(c)
        i += 1
    flush()
    return runs


def plain_text(markdown_inline: str) -> str:
    """Visible text of inline Markdown as it will appear in Word (images carry no text)."""
    parts: List[str] = []
    for run in parse_inline(markdown_inline):
        if run.kind == "text":
            parts.append(run.text)
        elif run.kind == "br":
            parts.append("\n")
    return "".join(parts)


# --------------------------------------------------------------------------------------------
# Images
# --------------------------------------------------------------------------------------------

def image_info(data: bytes) -> Optional[Tuple[str, int, int]]:
    """Return (extension, width_px, height_px) for PNG/JPEG data, else None."""
    if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR":
        width, height = struct.unpack(">II", data[16:24])
        return "png", width, height
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker == 0xFF:
                i += 1
                continue
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                height, width = struct.unpack(">HH", data[i + 5:i + 9])
                return "jpeg", width, height
            if marker in (0x01,) or 0xD0 <= marker <= 0xD9:
                i += 2
                continue
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return None


# --------------------------------------------------------------------------------------------
# Styles and numbering
# --------------------------------------------------------------------------------------------

class MermaidRenderer:
    """Render Mermaid code to PNG with mermaid-cli (mmdc). Optional: without mmdc, diagrams stay code.

    mmdc is a Node tool (npm i -g @mermaid-js/mermaid-cli). It drives a headless browser; when its
    bundled Chromium is not installed, pass an installed Chrome/Edge with --browser.
    """

    def __init__(self, mmdc: str, browser: Optional[str] = None, scale: float = 2.0) -> None:
        self.mmdc = mmdc
        self.browser = browser
        self.scale = scale
        self.cache: Dict[str, Optional[bytes]] = {}
        self.errors: List[str] = []

    @staticmethod
    def find(explicit: Optional[str] = None) -> Optional[str]:
        local = Path(__file__).resolve().parent / "node_modules" / ".bin" / ("mmdc.cmd" if os.name == "nt" else "mmdc")
        # A path the user names is the only one tried: falling back would hide a typo.
        candidates = (explicit,) if explicit else (os.environ.get("BA_MMDC"), "mmdc", str(local))
        for candidate in candidates:
            if not candidate:
                continue
            found = shutil.which(candidate) or (candidate if Path(candidate).is_file() else None)
            if found:
                return found
        return None

    def __call__(self, code: str) -> Optional[bytes]:
        key = hashlib.sha1(code.encode("utf-8")).hexdigest()
        if key in self.cache:
            return self.cache[key]
        png: Optional[bytes] = None
        with tempfile.TemporaryDirectory() as tmp:
            src, out = Path(tmp) / "d.mmd", Path(tmp) / "d.png"
            src.write_text(code, encoding="utf-8")
            cmd = [self.mmdc, "-i", str(src), "-o", str(out), "-b", "white", "-s", str(self.scale), "-q"]
            if self.browser:
                config = Path(tmp) / "puppeteer.json"
                config.write_text(json.dumps({"executablePath": self.browser, "args": ["--no-sandbox"]}), encoding="utf-8")
                cmd += ["-p", str(config)]
            try:
                proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
                if proc.returncode == 0 and out.is_file():
                    png = out.read_bytes()
                else:
                    message = (proc.stderr or proc.stdout or "").strip().splitlines()
                    self.errors.append(message[0] if message else f"mmdc exit {proc.returncode}")
            except (OSError, subprocess.TimeoutExpired) as exc:
                self.errors.append(str(exc))
        self.cache[key] = png
        return png


def _style(sid: str, kind: str, name: str, based: Optional[str], body: str, extra: str = "") -> str:
    based_xml = f'<w:basedOn w:val="{esc(based, True)}"/>' if based else ""
    return (
        f'<w:style w:type="{kind}"{extra} w:styleId="{esc(sid, True)}"><w:name w:val="{esc(name, True)}"/>'
        f"{based_xml}{body}</w:style>"
    )


def default_style_xml(logical: str, ids: Dict[str, Optional[str]]) -> str:
    """Default definition of a logical style; ids maps logical/base names to style ids."""
    normal, table_normal, dpf = ids.get("Normal"), ids.get("TableNormal"), ids.get("DefaultParagraphFont")
    sid = ids.get(logical) or logical
    nxt = f'<w:next w:val="{esc(normal, True)}"/>' if normal else ""
    if logical == "Title":
        return _style(sid, "paragraph", "Title", normal, f'{nxt}<w:uiPriority w:val="10"/><w:qFormat/>'
                      '<w:pPr><w:spacing w:before="240" w:after="240"/><w:jc w:val="center"/></w:pPr>'
                      f'<w:rPr><w:rFonts w:ascii="{HEADING_FONT}" w:hAnsi="{HEADING_FONT}" w:cs="{HEADING_FONT}"/>'
                      '<w:b/><w:bCs/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr>')
    if logical.startswith("Heading"):
        level = int(logical[-1])
        size = {1: 32, 2: 28, 3: 26, 4: 26, 5: 26, 6: 26}[level]
        italic = "<w:i/><w:iCs/>" if level >= 5 else ""
        return _style(sid, "paragraph", f"heading {level}", normal, f'{nxt}<w:uiPriority w:val="9"/><w:qFormat/>'
                      f'<w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="{240 if level == 1 else 180}" w:after="120"/>'
                      f'<w:outlineLvl w:val="{level - 1}"/></w:pPr>'
                      f'<w:rPr><w:rFonts w:ascii="{HEADING_FONT}" w:hAnsi="{HEADING_FONT}" w:cs="{HEADING_FONT}"/>'
                      f'<w:b/><w:bCs/>{italic}<w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>')
    if logical == "ListParagraph":
        return _style(sid, "paragraph", "List Paragraph", normal, '<w:uiPriority w:val="34"/><w:qFormat/>'
                      '<w:pPr><w:spacing w:after="60"/><w:ind w:left="720"/><w:contextualSpacing/></w:pPr>')
    if logical == "Code":
        return _style(sid, "paragraph", "Code", normal, '<w:qFormat/>'
                      '<w:pPr><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
                      f'<w:rPr><w:rFonts w:ascii="{CODE_FONT}" w:hAnsi="{CODE_FONT}" w:cs="{CODE_FONT}" w:eastAsia="{CODE_FONT}"/>'
                      '<w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>')
    if logical == "Quote":
        return _style(sid, "paragraph", "Quote", normal, f'{nxt}<w:uiPriority w:val="29"/><w:qFormat/>'
                      '<w:pPr><w:pBdr><w:left w:val="single" w:sz="12" w:space="8" w:color="A6A6A6"/></w:pBdr>'
                      '<w:spacing w:before="60" w:after="120"/><w:ind w:left="284"/></w:pPr>'
                      '<w:rPr><w:i/><w:iCs/><w:color w:val="404040"/></w:rPr>')
    if logical == "Hyperlink":
        return _style(sid, "character", "Hyperlink", dpf, '<w:uiPriority w:val="99"/><w:unhideWhenUsed/>'
                      '<w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr>')
    if logical == "TableGrid":
        border = '<w:{0} w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
        borders = "".join(border.format(side) for side in ("top", "left", "bottom", "right", "insideH", "insideV"))
        return _style(sid, "table", "Table Grid", table_normal, '<w:uiPriority w:val="39"/>'
                      '<w:pPr><w:spacing w:before="40" w:after="40" w:line="240" w:lineRule="auto"/></w:pPr>'
                      f'<w:tblPr><w:tblBorders>{borders}</w:tblBorders></w:tblPr>')
    raise KeyError(logical)


def default_styles_xml() -> str:
    ids: Dict[str, Optional[str]] = {key: key for key in list(STYLE_NAMES) + list(BASE_STYLE_NAMES)}
    base = (
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
        '<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont"><w:name w:val="Default Paragraph Font"/>'
        '<w:uiPriority w:val="1"/><w:semiHidden/><w:unhideWhenUsed/></w:style>'
        '<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/><w:uiPriority w:val="99"/>'
        '<w:semiHidden/><w:unhideWhenUsed/><w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar>'
        '<w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/>'
        '<w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>'
        '<w:style w:type="numbering" w:default="1" w:styleId="NoList"><w:name w:val="No List"/><w:uiPriority w:val="99"/>'
        '<w:semiHidden/><w:unhideWhenUsed/></w:style>'
    )
    styles = "".join(default_style_xml(logical, ids) for logical in STYLE_NAMES)
    return (
        f'{XML_DECL}<w:styles xmlns:w="{W_NS}" xmlns:r="{R_NS}">'
        "<w:docDefaults><w:rPrDefault><w:rPr>"
        f'<w:rFonts w:ascii="{BODY_FONT}" w:eastAsia="{BODY_FONT}" w:hAnsi="{BODY_FONT}" w:cs="{BODY_FONT}"/>'
        '<w:sz w:val="26"/><w:szCs w:val="26"/><w:lang w:val="vi-VN" w:eastAsia="en-US" w:bidi="ar-SA"/>'
        "</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>"
        '<w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
        f"{base}{styles}</w:styles>"
    )


BULLET_CHARS = ["•", "◦", "▪"]


def numbering_fragments(abs_base: int, num_base: int, ordered: List[Tuple[int, int, int]]) -> Tuple[str, str]:
    """Return (abstractNum xml, num xml). ordered = [(numId, level, start)] for each ordered list run."""
    bullet_levels, decimal_levels = [], []
    for lvl in range(9):
        ind = f'<w:pPr><w:ind w:left="{720 + 360 * lvl}" w:hanging="360"/></w:pPr>'
        char = BULLET_CHARS[lvl % 3]
        bullet_levels.append(
            f'<w:lvl w:ilvl="{lvl}"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="{char}"/>'
            f'<w:lvlJc w:val="left"/>{ind}<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:hint="default"/></w:rPr></w:lvl>'
        )
        decimal_levels.append(
            f'<w:lvl w:ilvl="{lvl}"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%{lvl + 1}."/>'
            f'<w:lvlJc w:val="left"/>{ind}</w:lvl>'
        )
    abstract = (
        f'<w:abstractNum w:abstractNumId="{abs_base}"><w:multiLevelType w:val="hybridMultilevel"/>{"".join(bullet_levels)}</w:abstractNum>'
        f'<w:abstractNum w:abstractNumId="{abs_base + 1}"><w:multiLevelType w:val="hybridMultilevel"/>{"".join(decimal_levels)}</w:abstractNum>'
    )
    nums = [f'<w:num w:numId="{num_base + 1}"><w:abstractNumId w:val="{abs_base}"/></w:num>']
    for num_id, level, start in ordered:
        nums.append(
            f'<w:num w:numId="{num_id}"><w:abstractNumId w:val="{abs_base + 1}"/>'
            f'<w:lvlOverride w:ilvl="{level}"><w:startOverride w:val="{start}"/></w:lvlOverride></w:num>'
        )
    return abstract, "".join(nums)


DEFAULT_SECT_PR = (
    '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
    '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="709" w:footer="709" w:gutter="0"/>'
    '<w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr>'
)

DEFAULT_SETTINGS = (
    f'{XML_DECL}<w:settings xmlns:w="{W_NS}"><w:zoom w:percent="100"/><w:defaultTabStop w:val="720"/>'
    '<w:characterSpacingControl w:val="doNotCompress"/><w:compat>'
    '<w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/>'
    "</w:compat></w:settings>"
)


# --------------------------------------------------------------------------------------------
# Template support
# --------------------------------------------------------------------------------------------

def _rels_name(part: str) -> str:
    folder, base = posixpath.split(part)
    return posixpath.join(folder, "_rels", base + ".rels")


def _resolve(part: str, target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join(posixpath.dirname(part), target))


def text_width(sect_pr: str) -> int:
    """Usable text width (twips) from a sectPr; falls back to A4 with 2 cm margins."""
    def num(tag: str, name: str) -> Optional[float]:
        match = re.search(rf'<w:{tag}\b[^>]*\bw:{name}="([\d.]+)"', sect_pr)
        return float(match.group(1)) if match else None

    width, left, right = num("pgSz", "w"), num("pgMar", "left"), num("pgMar", "right")
    if width and left is not None and right is not None and width - left - right > 1000:
        return int(width - left - right)
    return TEXT_WIDTH_TWIPS


def text_height(sect_pr: str) -> Optional[int]:
    """Usable text height (twips) from a sectPr, or None when the sectPr does not say."""
    def num(tag: str, name: str) -> Optional[float]:
        match = re.search(rf'<w:{tag}\b[^>]*\bw:{name}="([\d.]+)"', sect_pr)
        return float(match.group(1)) if match else None

    height, top, bottom = num("pgSz", "h"), num("pgMar", "top"), num("pgMar", "bottom")
    if height and top is not None and bottom is not None and height - top - bottom > 1000:
        return int(height - abs(top) - abs(bottom))
    return None


def continued_section(sect_pr: str) -> str:
    """Section properties for a section after the first: no own first-page header, numbering continues."""
    sect = re.sub(r"<w:titlePg\b[^>]*/>", "", sect_pr)
    return re.sub(r'(<w:pgNumType\b[^>]*?)\s+w:start="\d+"', r"\1", sect)


# Markers left in the body by _wide_picture_xml and resolved by _resolve_sections.
BREAK_BEFORE, LANDSCAPE_SLOT, WIDE_END = "\x00P\x00", "\x00L\x00", "\x00E\x00"


class Template:
    """Read-only view of a customer's reference .docx/.dotx."""

    def __init__(self, path: Path) -> None:
        self.zf = zipfile.ZipFile(path)
        self.names = set(self.zf.namelist())
        ct = ET.fromstring(self.zf.read("[Content_Types].xml"))
        self.defaults = {el.get("Extension", "").lower(): el.get("ContentType", "") for el in ct if el.tag.endswith("Default")}
        self.overrides = {el.get("PartName", ""): el.get("ContentType", "") for el in ct if el.tag.endswith("Override")}
        root_rels = self.rels("")
        main = next((t for _, (ty, t, _) in root_rels.items() if ty == RT + "officeDocument"), "word/document.xml")
        self.main = main.lstrip("/")
        if self.main not in self.names:
            raise ValueError("template has no main document part")
        self.doc_rels = self.rels(self.main)
        self.document = self.zf.read(self.main).decode("utf-8")

    def rels(self, part: str) -> Dict[str, Tuple[str, str, str]]:
        """Relationships of a part: id -> (type, target, target_mode). part='' is the package."""
        name = "_rels/.rels" if not part else _rels_name(part)
        if name not in self.names:
            return {}
        root = ET.fromstring(self.zf.read(name))
        return {
            el.get("Id", ""): (el.get("Type", ""), el.get("Target", ""), el.get("TargetMode", "Internal"))
            for el in root
        }

    def content_type(self, part: str) -> str:
        return self.overrides.get("/" + part) or self.defaults.get(posixpath.splitext(part)[1][1:].lower(), "application/octet-stream")

    def part_by_type(self, rel_type: str) -> Optional[str]:
        for ty, target, mode in self.doc_rels.values():
            if ty == RT + rel_type and mode != "External":
                part = _resolve(self.main, target)
                if part in self.names:
                    return part
        return None

    def text(self, part: str) -> str:
        return self.zf.read(part).decode("utf-8")

    def sect_pr(self) -> Optional[str]:
        starts = [m.start() for m in re.finditer(r"<w:sectPr[\s>/]", self.document)]
        if not starts:
            return None
        idx = starts[-1]
        close = self.document.find(">", idx)
        if self.document[close - 1] == "/":
            return self.document[idx:close + 1]
        end = self.document.find("</w:sectPr>", idx)
        return self.document[idx:end + len("</w:sectPr>")] if end > 0 else None

    def style_index(self) -> Tuple[Dict[str, str], Dict[str, str]]:
        """Return (styleId -> type, lowercase name -> styleId) of the template's styles."""
        by_id: Dict[str, str] = {}
        by_name: Dict[str, str] = {}
        if "word/styles.xml" not in self.names:
            return by_id, by_name
        root = ET.fromstring(self.zf.read("word/styles.xml"))
        for style in root.findall(f"{{{W_NS}}}style"):
            sid = style.get(f"{{{W_NS}}}styleId")
            if not sid:
                continue
            by_id[sid] = style.get(f"{{{W_NS}}}type", "paragraph")
            name = style.find(f"{{{W_NS}}}name")
            if name is not None and name.get(f"{{{W_NS}}}val"):
                by_name.setdefault(name.get(f"{{{W_NS}}}val", "").lower(), sid)
        return by_id, by_name


# --------------------------------------------------------------------------------------------
# Document writer
# --------------------------------------------------------------------------------------------

class DocxWriter:
    def __init__(
        self,
        md_path: Path,
        template: Optional[Template] = None,
        diagram_renderer: Optional[Callable[[str], Optional[bytes]]] = None,
    ) -> None:
        self.diagram_renderer = diagram_renderer
        self.md_path = md_path
        self.base_dir = md_path.parent
        self.template = template
        self.parts: Dict[str, bytes] = {}
        self.overrides: Dict[str, str] = {}
        self.defaults: Dict[str, str] = {"rels": CT_RELS, "xml": "application/xml"}
        self.rels: List[Tuple[str, str, str, bool]] = []  # (id, type, target, external)
        self.copied: Dict[str, str] = {}
        self.link_rids: Dict[str, str] = {}
        self.image_rids: Dict[str, Tuple[str, int, int]] = {}
        self.counts = {"headings": 0, "tables": 0, "images": 0, "diagrams": 0, "diagrams_as_code": 0, "landscape_pages": 0}
        self.max_image_emu = MAX_IMAGE_EMU
        self.page_sect: Optional[str] = None  # section a picture is being drawn for, when not the main one
        self.title: Optional[str] = None
        self.drawing_id = 0
        self.ordered_nums: List[Tuple[int, int, int]] = []
        self.styles_xml = default_styles_xml()
        self.numbering_xml_template: Optional[str] = None
        self.abs_base, self.num_base = 0, 0
        self.style_ids: Dict[str, str] = {key: key for key in STYLE_NAMES}
        self.sect_pr = DEFAULT_SECT_PR
        self.text_width = TEXT_WIDTH_TWIPS
        self.settings_xml = DEFAULT_SETTINGS
        if template:
            self._apply_template(template)

    # -- relationships and parts ---------------------------------------------------------------

    def add_rel(self, rel_type: str, target: str, external: bool = False) -> str:
        rid = f"rId{len(self.rels) + 1}"
        self.rels.append((rid, rel_type, target, external))
        return rid

    def copy_part(self, part: str, data: Optional[bytes] = None) -> None:
        """Copy a template part plus its relationships and internal targets (recursively)."""
        assert self.template is not None
        if part in self.copied:
            return
        self.copied[part] = part
        self.parts[part] = data if data is not None else self.template.zf.read(part)
        self.overrides["/" + part] = self.template.content_type(part)
        rels_name = _rels_name(part)
        if rels_name in self.template.names:
            self.parts[rels_name] = self.template.zf.read(rels_name)
            for _, (_, target, mode) in self.template.rels(part).items():
                child = _resolve(part, target)
                if mode != "External" and child in self.template.names:
                    self.copy_part(child)

    def _apply_template(self, tpl: Template) -> None:
        # Styles: keep the template's, map logical styles to its ids, append what is missing.
        if "word/styles.xml" in tpl.names:
            by_id, by_name = tpl.style_index()
            ids: Dict[str, Optional[str]] = {}
            for logical, name in {**BASE_STYLE_NAMES, **STYLE_NAMES}.items():
                ids[logical] = logical if logical in by_id else by_name.get(name.lower())
            missing = [logical for logical in STYLE_NAMES if not ids.get(logical)]
            for logical in STYLE_NAMES:
                self.style_ids[logical] = ids.get(logical) or logical
            styles = tpl.text("word/styles.xml")
            if missing:
                ids.update({logical: logical for logical in missing})
                extra = "".join(default_style_xml(logical, ids) for logical in missing)
                if f'xmlns:w="{W_NS}"' not in styles[:2000]:
                    extra = extra.replace("<w:style ", f'<w:style xmlns:w="{W_NS}" ')
                close = styles.rfind("</w:styles>")
                styles = styles[:close] + extra + styles[close:]
            self.styles_xml = styles

        for rel_type in ("theme", "fontTable", "settings"):
            part = tpl.part_by_type(rel_type)
            if not part:
                continue
            if rel_type == "settings":
                settings = tpl.text(part)
                # Drop references to parts we do not carry over and any editing restriction.
                for tag in ("attachedTemplate", "documentProtection", "writeProtection", "mailMerge",
                            "footnotePr", "endnotePr", "rsids"):
                    settings = re.sub(rf"<w:{tag}\b[^>]*/>|<w:{tag}\b[^>]*>.*?</w:{tag}>", "", settings, flags=re.S)
                self.settings_xml = settings
                continue
            self.copy_part(part)
            self.add_rel(RT + rel_type, posixpath.relpath(part, "word"))

        numbering = tpl.part_by_type("numbering")
        if numbering:
            text = tpl.text(numbering)
            abs_ids = [int(v) for v in re.findall(r'w:abstractNumId="(\d+)"', text)]
            num_ids = [int(v) for v in re.findall(r'<w:num\b[^>]*w:numId="(\d+)"', text)]
            self.abs_base = max(abs_ids, default=-1) + 1
            self.num_base = max(num_ids, default=0)
            self.numbering_xml_template = text
            rels_name = _rels_name(numbering)
            if rels_name in tpl.names:  # picture bullets
                for _, (_, target, mode) in tpl.rels(numbering).items():
                    child = _resolve(numbering, target)
                    if mode != "External" and child in tpl.names:
                        self.copy_part(child)
                self.parts["word/_rels/numbering.xml.rels"] = tpl.zf.read(rels_name)

        sect = tpl.sect_pr()
        if sect:
            dropped: List[str] = []

            def remap(match: "re.Match[str]") -> str:
                old = match.group(1)
                rel = tpl.doc_rels.get(old)
                if not rel or rel[2] == "External":
                    dropped.append(old)
                    return match.group(0)
                part = _resolve(tpl.main, rel[1])
                if part not in tpl.names:
                    dropped.append(old)
                    return match.group(0)
                self.copy_part(part)
                return f'r:id="{self.add_rel(rel[0], posixpath.relpath(part, "word"))}"'

            sect = re.sub(r'r:id="([^"]+)"', remap, sect)
            for old in dropped:
                sect = re.sub(rf'<w:\w+\b[^>]*r:id="{re.escape(old)}"[^>]*/>', "", sect)
            self.sect_pr = sect
            self.text_width = text_width(sect)

    # -- runs ---------------------------------------------------------------------------------

    def _text_run(self, run: Run, force_bold: bool = False, char_style: Optional[str] = None) -> str:
        rpr: List[str] = []
        if char_style:
            rpr.append(f'<w:rStyle w:val="{esc(char_style, True)}"/>')
        if run.code:
            rpr.append(f'<w:rFonts w:ascii="{CODE_FONT}" w:hAnsi="{CODE_FONT}" w:cs="{CODE_FONT}" w:eastAsia="{CODE_FONT}"/>')
        if run.bold or force_bold:
            rpr.append("<w:b/><w:bCs/>")
        if run.italic:
            rpr.append("<w:i/><w:iCs/>")
        if run.code:
            rpr.append('<w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>')
        rpr_xml = f"<w:rPr>{''.join(rpr)}</w:rPr>" if rpr else ""
        pieces = run.text.split("\t")
        content = "<w:tab/>".join(w_t(piece) if piece else "" for piece in pieces)
        return f"<w:r>{rpr_xml}{content}</w:r>"

    def _image_run(self, run: Run) -> str:
        alt = run.text or Path(urllib.parse.unquote(run.src)).name
        placeholder = Run("text", f"[Ảnh: {alt}]", italic=True)
        src = urllib.parse.unquote(run.src)
        if not src or re.match(r"(?i)^(https?|data|ftp):", src):
            return self._text_run(placeholder)
        try:
            path = (self.base_dir / src).resolve()
            if path.suffix.lower() not in (".png", ".jpg", ".jpeg") or not path.is_file():
                return self._text_run(placeholder)
        except (OSError, ValueError):
            return self._text_run(placeholder)
        drawing = self._drawing_run(str(path), path.read_bytes, alt, path.name)
        return drawing if drawing else self._text_run(placeholder)

    def _image_paragraph(self, text: str, caption: Optional[str] = None) -> Optional[str]:
        """A paragraph holding only a local PNG/JPEG: centred, landscape page when wide."""
        match = IMAGE_ONLY_PARA.match(text)
        if not match:
            return None
        alt, src = match.group(1), urllib.parse.unquote(match.group(2))
        if re.match(r"(?i)^(https?|data|ftp):", src):
            return None
        try:
            path = (self.base_dir / src).resolve()
            if path.suffix.lower() not in (".png", ".jpg", ".jpeg") or not path.is_file():
                return None
            info = image_info(path.read_bytes())
        except (OSError, ValueError):
            return None
        if not info:
            return None
        _, width, height = info
        return self._wide_picture_xml(lambda: self._drawing_run(str(path), path.read_bytes, alt or path.name, path.name), width, height, caption)

    def _landscape_sect(self) -> str:
        """The current section properties turned to landscape (headers, footers, margins kept)."""
        sect = re.sub(r"\s+w:rsid\w*=\"[^\"]*\"", "", self.sect_pr)
        match = re.search(r'<w:pgSz\b[^>]*/>', sect)
        if not match:
            return sect
        width = re.search(r'w:w="(\d+)"', match.group(0))
        height = re.search(r'w:h="(\d+)"', match.group(0))
        if not (width and height):
            return sect
        w, h = int(width.group(1)), int(height.group(1))
        size = f'<w:pgSz w:w="{max(w, h)}" w:h="{min(w, h)}" w:orient="landscape"/>'
        return sect[: match.start()] + size + sect[match.end():]

    def _wide_picture_xml(self, drawing: Callable[[], Optional[str]], width_px: int, height_px: int, caption: Optional[str] = None) -> Optional[str]:
        """Picture paragraph (and its caption); wide pictures get a landscape page between two section breaks."""
        center = '<w:jc w:val="center"/>'
        keep = "<w:keepNext/>" if caption else ""  # picture and caption stay on one page
        if width_px < WIDE_IMAGE_MIN_PX or width_px / max(height_px, 1) < WIDE_IMAGE_RATIO:
            run = drawing()
            if not run:
                return None
            under = self.paragraph(caption, extra_ppr=center) if caption else ""
            return f"<w:p><w:pPr>{keep}{center}</w:pPr>{run}</w:p>{under}"
        landscape = self._landscape_sect()
        previous = self.max_image_emu
        self.max_image_emu = text_width(landscape) * EMU_PER_TWIP
        self.page_sect = landscape
        try:
            run = drawing()
        finally:
            self.max_image_emu = previous
            self.page_sect = None
        if not run:
            return None
        self.counts["landscape_pages"] += 1
        # The landscape section ends on the picture's own paragraph (no empty paragraph that could
        # spill onto a page of its own); _resolve_sections decides which breaks are really needed.
        if caption:  # the section ends on the caption, so it shares the landscape page
            under = self.paragraph(caption, extra_ppr=center + LANDSCAPE_SLOT)
            return f"{BREAK_BEFORE}<w:p><w:pPr>{keep}{center}</w:pPr>{run}</w:p>{under}{WIDE_END}"
        return f'{BREAK_BEFORE}<w:p><w:pPr>{center}{LANDSCAPE_SLOT}</w:pPr>{run}</w:p>{WIDE_END}'

    def _resolve_sections(self, body: str) -> Tuple[str, str]:
        """Turn the wide-picture markers into section breaks; return (body, final sectPr).

        - no portrait break at the very start or right after another wide picture (no blank page);
        - a wide picture at the very end makes the last section landscape (no blank last page);
        - only the first section keeps a separate first-page header and a numbering restart.
        """
        portrait = re.sub(r"\s+w:rsid\w*=\"[^\"]*\"", "", self.sect_pr)
        landscape = self._landscape_sect()
        pieces = re.split("(\x00[PLE]\x00)", body)
        out: List[str] = []
        sections = 0
        content = False
        final = None
        for index, piece in enumerate(pieces):
            if piece == BREAK_BEFORE:
                if content:
                    out.append(f"<w:p><w:pPr>{portrait if sections == 0 else continued_section(portrait)}</w:pPr></w:p>")
                    sections += 1
                    content = False
            elif piece == LANDSCAPE_SLOT:
                rest = "".join(p for p in pieces[index + 1:] if p not in (BREAK_BEFORE, LANDSCAPE_SLOT, WIDE_END))
                own = landscape if sections == 0 else continued_section(landscape)
                tail = rest.split("</w:p>", 1)[1] if "</w:p>" in rest else ""
                if not tail.strip():
                    final = own
                else:
                    out.append(own)
                    sections += 1
            elif piece == WIDE_END:
                content = False
            elif piece:
                out.append(piece)
                content = True
        if final is None:
            final = self.sect_pr if sections == 0 else continued_section(self.sect_pr)
        return "".join(out), final

    def _drawing_run(self, key: str, load: Callable[[], bytes], alt: str, file_name: str) -> Optional[str]:
        """Inline picture run for PNG/JPEG bytes (embedded once per key), or None if not an image."""
        if key not in self.image_rids:
            data = load()
            info = image_info(data)
            if not info:
                return None
            ext, width, height = info
            name = f"media/md_image{len(self.image_rids) + 1}.{ext}"
            self.parts["word/" + name] = data
            self.defaults[ext] = "image/png" if ext == "png" else "image/jpeg"
            self.image_rids[key] = (self.add_rel(RT + "image", name), max(width, 1), max(height, 1))
            self.counts["images"] += 1
        rid, width, height = self.image_rids[key]
        cx, cy = width * EMU_PER_PX, height * EMU_PER_PX
        if cx > self.max_image_emu:
            cy = int(cy * self.max_image_emu / cx)
            cx = self.max_image_emu
        # 90 % of the text height leaves room for the caption line on the same page.
        page_h = text_height(self.page_sect or self.sect_pr)
        if page_h and cy > page_h * EMU_PER_TWIP * 0.9:
            limit = int(page_h * EMU_PER_TWIP * 0.9)
            cx, cy = int(cx * limit / cy), limit
        self.drawing_id += 1
        did = self.drawing_id
        alt_attr = esc(alt, True)
        return (
            "<w:r><w:drawing>"
            f'<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
            '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
            f'<wp:docPr id="{did}" name="Picture {did}" descr="{alt_attr}"/>'
            '<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic><pic:nvPicPr><pic:cNvPr id="{did}" name="{esc(file_name, True)}" descr="{alt_attr}"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
            "</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>"
        )

    def runs_xml(self, text: str, force_bold: bool = False) -> str:
        runs = parse_inline(text)
        out: List[str] = []
        i = 0
        while i < len(runs):
            run = runs[i]
            if run.kind == "br":
                out.append('<w:r><w:br/></w:r>')
            elif run.kind == "image":
                out.append(self._image_run(run))
            elif run.href:
                group: List[Run] = []
                while i < len(runs) and runs[i].kind == "text" and runs[i].href == run.href:
                    group.append(runs[i])
                    i += 1
                if run.href not in self.link_rids:
                    target = urllib.parse.quote(run.href, safe=":/?#[]@!$&'()*+,;=%~")
                    self.link_rids[run.href] = self.add_rel(RT + "hyperlink", target, external=True)
                inner = "".join(self._text_run(r, force_bold, self.style_ids["Hyperlink"]) for r in group)
                out.append(f'<w:hyperlink r:id="{self.link_rids[run.href]}" w:history="1">{inner}</w:hyperlink>')
                continue
            else:
                out.append(self._text_run(run, force_bold))
            i += 1
        return "".join(out)

    # -- blocks -------------------------------------------------------------------------------

    def paragraph(self, text: str, style: Optional[str] = None, extra_ppr: str = "", force_bold: bool = False) -> str:
        ppr = (f'<w:pStyle w:val="{esc(style, True)}"/>' if style else "") + extra_ppr
        ppr_xml = f"<w:pPr>{ppr}</w:pPr>" if ppr else ""
        return f"<w:p>{ppr_xml}{self.runs_xml(text, force_bold)}</w:p>"

    def literal_paragraph(self, text: str, style: str, italic: bool = False) -> str:
        run = self._text_run(Run("text", text, italic=italic)) if text else ""
        return f'<w:p><w:pPr><w:pStyle w:val="{esc(style, True)}"/></w:pPr>{run}</w:p>'

    def list_xml(self, block: Block) -> str:
        out: List[str] = []
        active: Dict[int, int] = {}  # level -> numId of the ordered run at that level
        bullet_id = self.num_base + 1
        for level, ordered, start, text in block.items:
            for deeper in [lvl for lvl in active if lvl > level]:
                active.pop(deeper)
            if ordered:
                if level not in active:
                    num_id = self.num_base + 2 + len(self.ordered_nums)
                    self.ordered_nums.append((num_id, level, start))
                    active[level] = num_id
                num_id = active[level]
            else:
                active.pop(level, None)
                num_id = bullet_id
            numpr = f'<w:numPr><w:ilvl w:val="{level}"/><w:numId w:val="{num_id}"/></w:numPr>'
            out.append(self.paragraph(text, self.style_ids["ListParagraph"], numpr))
        return "".join(out)

    def table_xml(self, block: Block) -> str:
        ncols = len(block.rows[0])
        col_w = self.text_width // max(ncols, 1)
        grid = "".join(f'<w:gridCol w:w="{col_w}"/>' for _ in range(ncols))
        out = [
            f'<w:tbl><w:tblPr><w:tblStyle w:val="{esc(self.style_ids["TableGrid"], True)}"/><w:tblW w:w="5000" w:type="pct"/>'
            '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
            f"</w:tblPr><w:tblGrid>{grid}</w:tblGrid>"
        ]
        for index, row in enumerate(block.rows):
            header = index == 0
            out.append("<w:tr>" + ("<w:trPr><w:tblHeader/></w:trPr>" if header else ""))
            for cell in row:
                shade = '<w:shd w:val="clear" w:color="auto" w:fill="D9E2F3"/>' if header else ""
                out.append(f'<w:tc><w:tcPr><w:tcW w:w="{col_w}" w:type="dxa"/>{shade}</w:tcPr>{self.paragraph(cell, force_bold=header)}</w:tc>')
            out.append("</w:tr>")
        out.append("</w:tbl>")
        return "".join(out)

    def body_xml(self, blocks: List[Block]) -> str:
        out: List[str] = []
        previous = ""
        for block in blocks:
            if block.kind == "table" and previous == "table":
                out.append("<w:p/>")  # keep adjacent tables from merging
            if block.kind == "heading":
                self.counts["headings"] += 1
                style = f"Heading{block.level}"
                if block.level == 1 and self.title is None:
                    self.title = plain_text(block.text)
                    style = "Title"
                out.append(self.paragraph(block.text, self.style_ids[style]))
            elif block.kind == "para":
                text = block.text.strip()
                picture = self._image_paragraph(text)
                if not picture:
                    # An image followed by its caption line ("Nguồn thiết kế: ...") in the same paragraph:
                    # picture on its own (landscape page when wide), caption as a normal paragraph after it.
                    lead = IMAGE_WITH_CAPTION.match(text)
                    picture = self._image_paragraph(lead.group(1), lead.group(2)) if lead else None
                out.append(picture if picture else self.paragraph(block.text))
            elif block.kind == "list":
                out.append(self.list_xml(block))
            elif block.kind == "table":
                self.counts["tables"] += 1
                out.append(self.table_xml(block))
            elif block.kind == "code":
                code_style = self.style_ids["Code"]
                if block.lang == "mermaid":
                    code = "\n".join(block.lines or [])
                    png = self.diagram_renderer(code) if self.diagram_renderer else None
                    picture = None
                    info = image_info(png) if png else None
                    if png and info:
                        key = "mermaid:" + hashlib.sha1(code.encode("utf-8")).hexdigest()
                        picture = self._wide_picture_xml(lambda: self._drawing_run(key, lambda: png, "Sơ đồ", "diagram.png"), info[1], info[2])
                    if picture:
                        self.counts["diagrams"] += 1
                        out.append(picture)
                        previous = block.kind
                        continue
                    self.counts["diagrams_as_code"] += 1
                    out.append(f'<w:p>{self._text_run(Run("text", MERMAID_NOTE, italic=True))}</w:p>')
                out.extend(self.literal_paragraph(line, code_style) for line in block.lines or [""])
            elif block.kind == "quote":
                out.extend(self.paragraph(text, self.style_ids["Quote"]) for text in block.lines)
            elif block.kind == "hr":
                out.append('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="auto"/></w:pBdr></w:pPr></w:p>')
            previous = block.kind
        if previous == "table":
            out.append("<w:p/>")
        return "".join(out)

    # -- package ------------------------------------------------------------------------------

    def numbering_xml(self) -> str:
        abstract, nums = numbering_fragments(self.abs_base, self.num_base, self.ordered_nums)
        if not self.numbering_xml_template:
            return f'{XML_DECL}<w:numbering xmlns:w="{W_NS}" xmlns:r="{R_NS}">{abstract}{nums}</w:numbering>'
        text = self.numbering_xml_template
        first_num = re.search(r"<w:num[\s>]", text)
        cleanup = re.search(r"<w:numIdMacAtCleanup\b", text)
        close = text.rfind("</w:numbering>")
        if close < 0:  # self-closing <w:numbering .../>
            text = re.sub(r"/>\s*$", "></w:numbering>", text.rstrip())
            close = text.rfind("</w:numbering>")
        nums_at = cleanup.start() if cleanup else close
        abs_at = first_num.start() if first_num else nums_at
        return text[:abs_at] + abstract + text[abs_at:nums_at] + nums + text[nums_at:]

    def build(self, markdown: str) -> bytes:
        blocks = parse_blocks(markdown)
        body, final_sect = self._resolve_sections(self.body_xml(blocks))
        document = f"{XML_DECL}<w:document {DOC_NAMESPACES}><w:body>{body}{final_sect}</w:body></w:document>"

        self.add_rel(RT + "styles", "styles.xml")
        self.add_rel(RT + "numbering", "numbering.xml")
        self.add_rel(RT + "settings", "settings.xml")
        self.parts["word/document.xml"] = document.encode("utf-8")
        self.parts["word/styles.xml"] = self.styles_xml.encode("utf-8")
        self.parts["word/numbering.xml"] = self.numbering_xml().encode("utf-8")
        self.parts["word/settings.xml"] = self.settings_xml.encode("utf-8")
        self.overrides.update({
            "/word/document.xml": CT_MAIN,
            "/word/styles.xml": CT_STYLES,
            "/word/numbering.xml": CT_NUMBERING,
            "/word/settings.xml": CT_SETTINGS,
            "/docProps/core.xml": CT_CORE,
            "/docProps/app.xml": CT_APP,
        })

        rel_xml = []
        for rid, rel_type, target, external in self.rels:
            mode = ' TargetMode="External"' if external else ""
            rel_xml.append(f'<Relationship Id="{rid}" Type="{rel_type}" Target="{esc(target, True)}"{mode}/>')
        self.parts["word/_rels/document.xml.rels"] = (
            f'{XML_DECL}<Relationships xmlns="{PKG_REL_NS}">{"".join(rel_xml)}</Relationships>'
        ).encode("utf-8")

        now = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        title = esc(self.title or self.md_path.stem)
        self.parts["docProps/core.xml"] = (
            f'{XML_DECL}<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f"<dc:title>{title}</dc:title><dc:creator>BA-agent</dc:creator><cp:lastModifiedBy>BA-agent</cp:lastModifiedBy>"
            f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
            f'<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>'
        ).encode("utf-8")
        self.parts["docProps/app.xml"] = (
            f'{XML_DECL}<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
            'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
            "<Application>BA-agent md_to_docx</Application></Properties>"
        ).encode("utf-8")
        self.parts["_rels/.rels"] = (
            f'{XML_DECL}<Relationships xmlns="{PKG_REL_NS}">'
            f'<Relationship Id="rId1" Type="{RT}officeDocument" Target="word/document.xml"/>'
            f'<Relationship Id="rId2" Type="{RT_CORE}" Target="docProps/core.xml"/>'
            f'<Relationship Id="rId3" Type="{RT}extended-properties" Target="docProps/app.xml"/>'
            "</Relationships>"
        ).encode("utf-8")

        defaults = "".join(f'<Default Extension="{ext}" ContentType="{ct}"/>' for ext, ct in sorted(self.defaults.items()))
        overrides = "".join(
            f'<Override PartName="{esc(name, True)}" ContentType="{ct}"/>' for name, ct in sorted(self.overrides.items())
        )
        content_types = f'{XML_DECL}<Types xmlns="{CT_NS}">{defaults}{overrides}</Types>'

        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("[Content_Types].xml", content_types.encode("utf-8"))
            for name in ["_rels/.rels", "word/document.xml"] + sorted(set(self.parts) - {"_rels/.rels", "word/document.xml"}):
                zf.writestr(name, self.parts[name])
        return buffer.getvalue()


def convert(
    md_path: Path,
    out_path: Path,
    template_path: Optional[Path] = None,
    diagram_renderer: Optional[Callable[[str], Optional[bytes]]] = None,
) -> Dict[str, int]:
    """Convert one Markdown file; returns the heading/table/image/diagram counts."""
    template = Template(template_path) if template_path else None
    try:
        writer = DocxWriter(md_path, template, diagram_renderer)
        data = writer.build(md_path.read_text(encoding="utf-8"))
    finally:
        if template:
            template.zf.close()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    return writer.counts


def main(argv: Optional[List[str]] = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="Xuất Markdown sang Word (.docx), có thể dùng template của khách hàng.")
    parser.add_argument("target", type=Path, help="File .md hoặc thư mục chứa các file .md")
    parser.add_argument("--out-dir", type=Path, default=None, help="Thư mục ghi .docx (mặc định: cạnh file nguồn)")
    parser.add_argument("--template", type=Path, default=None, help="File .docx/.dotx mẫu của khách hàng")
    parser.add_argument("--force", action="store_true", help="Ghi đè file .docx đã có")
    parser.add_argument(
        "--diagrams",
        choices=["auto", "image", "code"],
        default="auto",
        help="Sơ đồ Mermaid: image = vẽ thành ảnh (cần mermaid-cli), code = giữ mã, auto = ảnh nếu có mermaid-cli",
    )
    parser.add_argument("--mmdc", default=None, help="Đường dẫn mmdc (mặc định: biến BA_MMDC hoặc mmdc trong PATH)")
    parser.add_argument("--browser", default=None, help="Chrome/Edge đã cài, khi mmdc không có Chromium riêng (hoặc biến BA_MERMAID_BROWSER)")
    args = parser.parse_args(argv)

    renderer: Optional[MermaidRenderer] = None
    if args.diagrams != "code":
        mmdc = MermaidRenderer.find(args.mmdc)
        if mmdc:
            from wireframe_tool import find_browser  # an installed Chrome/Edge when mmdc has no Chromium of its own

            renderer = MermaidRenderer(mmdc, args.browser or find_browser())
        elif args.diagrams == "image":
            print("LỖI: --diagrams image cần mermaid-cli (npm i -g @mermaid-js/mermaid-cli) hoặc --mmdc <đường dẫn>")
            return 2

    target: Path = args.target
    if target.is_dir():
        sources = sorted(p for p in target.glob("*.md") if p.is_file())
    elif target.is_file() and target.suffix.lower() == ".md":
        sources = [target]
    else:
        sources = []
    if not sources:
        print(f"LỖI: không tìm thấy file Markdown tại {target}")
        return 2
    if args.template:
        try:
            Template(args.template).zf.close()
        except (OSError, KeyError, ValueError, zipfile.BadZipFile, ET.ParseError) as exc:
            print(f"LỖI: template không hợp lệ ({args.template}): {exc}")
            return 2

    status = 0
    for source in sources:
        out_path = (args.out_dir or source.parent) / f"{source.stem}.docx"
        if out_path.exists() and not args.force:
            print(f"SKIP: {out_path} đã tồn tại; dùng --force để ghi đè")
            status = 1
            continue
        try:
            counts = convert(source, out_path, args.template, renderer)
        except Exception as exc:  # report and continue with the other files
            print(f"LỖI: {source}: {exc}")
            status = 1
            continue
        print(
            f"OK: {out_path} (heading: {counts['headings']}, bảng: {counts['tables']}, ảnh: {counts['images']}, "
            f"sơ đồ thành ảnh: {counts['diagrams']}, sơ đồ giữ mã: {counts['diagrams_as_code']}, "
            f"trang ngang: {counts['landscape_pages']})"
        )
        if counts["diagrams_as_code"]:
            if args.diagrams == "code":
                reason = "đã chọn --diagrams code"
            elif renderer is None:
                reason = "không tìm thấy mermaid-cli"
            else:
                reason = "mermaid-cli báo lỗi: " + "; ".join(renderer.errors[-2:])
            print(f"  CẢNH BÁO: {counts['diagrams_as_code']} sơ đồ xuất dạng mã ({reason}). Khách sẽ thấy mã, không thấy hình.")
    return status


if __name__ == "__main__":
    sys.exit(main())
