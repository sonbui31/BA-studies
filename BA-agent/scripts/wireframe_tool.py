#!/usr/bin/env python3
"""Wireframes and mockups for BA documents: render HTML wireframes to PNG, check the screen set.

    python wireframe_tool.py render <SCR-01-ten.html> [-o out.png] [--size 1280x800] [--scale 2] [--browser PATH]
    python wireframe_tool.py check <bundle-folder> [--strict]

render: takes a screenshot of a local HTML wireframe with an installed Chrome or Edge (headless), so
a wireframe can be drawn offline when Figma or Stitch cannot be used. The page size comes from
--size, else from <meta name="wireframe-size" content="1280x800"> in the HTML, else 1280x800.

check (so_do.md section 13, core/screen-inventory-guide.md):
  - every image link to wireframes/ points to a file that exists;
  - every wireframe image is named after a screen code (SCR-01-...) defined in a table first cell
    (Screen Inventory, SRS) of the bundle;
  - a table row of screen SCR-xx that names a wireframe file names one of SCR-xx, not another screen;
  - every embedded wireframe has a source line ("Nguồn thiết kế: ...") right below it;
  - every PNG/JPEG in wireframes/ is used by some document (warning);
  - every screen code mentioned (an FR's Ref Wireframe column, a navigation note) has a row (warning).

Exit codes: 0 ok; 1 problems found (warnings too with --strict) or render failure;
2 bad arguments, missing file or folder, no browser found.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SCREEN_ID = re.compile(r"\bSCR-\d{2,3}\b")
ROW_SCREEN = re.compile(r"^\|\s*`?(SCR-\d{2,3})`?\s*\|")
IMAGE_LINK = re.compile(r"!\[[^\]]*\]\(([^)\s]*wireframes/[^)\s]+)\)")
FILE_MENTION = re.compile(r"wireframes/([\w.-]+\.(?:png|jpe?g))", re.IGNORECASE)
SOURCE_LINE = re.compile(r"ngu[ồo]n(?:\s+thi[ếe]t\s+k[ếe])?\s*:|source\s*:", re.IGNORECASE)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
SIZE_META = re.compile(r'<meta\s+name="wireframe-size"\s+content="(\d+)x(\d+)"', re.IGNORECASE)
IMAGE_EXTS = {".png", ".jpg", ".jpeg"}

BROWSER_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]
BROWSER_NAMES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge", "microsoft-edge"]


@dataclass
class Finding:
    level: str
    file: str
    line: int
    detail: str


# ---------------------------------------------------------------- render


def find_browser(explicit: Optional[str] = None) -> Optional[str]:
    """--browser, then BA_MERMAID_BROWSER / PUPPETEER_EXECUTABLE_PATH, then usual install places."""
    if explicit:
        return explicit if Path(explicit).is_file() else shutil.which(explicit)
    for env in ("BA_MERMAID_BROWSER", "PUPPETEER_EXECUTABLE_PATH"):
        value = os.environ.get(env)
        if value and Path(value).is_file():
            return value
    for path in BROWSER_PATHS:
        if Path(path).is_file():
            return path
    for name in BROWSER_NAMES:
        found = shutil.which(name)
        if found:
            return found
    return None


def page_size(html: str, size: Optional[str]) -> Tuple[int, int]:
    if size:
        match = re.fullmatch(r"(\d+)x(\d+)", size.strip())
        if not match:
            raise ValueError(f"--size cần dạng RỘNGxCAO, ví dụ 1280x800 (nhận được {size})")
        return int(match.group(1)), int(match.group(2))
    match = SIZE_META.search(html)
    return (int(match.group(1)), int(match.group(2))) if match else (1280, 800)


def render(html_path: Path, out_path: Path, browser: str, size: Tuple[int, int], scale: float = 2.0) -> Tuple[int, str]:
    width, height = size
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
            "--no-default-browser-check", f"--user-data-dir={profile}",
            f"--window-size={width},{height}", f"--force-device-scale-factor={scale}",
            f"--screenshot={out_path.resolve()}", html_path.resolve().as_uri(),
        ]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        except (OSError, subprocess.TimeoutExpired) as exc:
            return 1, f"không chạy được trình duyệt: {exc}"
    if not out_path.is_file() or out_path.stat().st_size == 0:
        return 1, "trình duyệt không tạo ảnh: " + (proc.stderr or proc.stdout).strip()[-300:]
    return 0, f"OK: {out_path} ({width}x{height} @{scale}x)"


# ---------------------------------------------------------------- check


def _visible_lines(text: str):
    """(line number, line) outside fenced code."""
    marker: Optional[str] = None
    for number, line in enumerate(text.splitlines(), start=1):
        match = FENCE.match(line)
        if marker is None:
            if match:
                marker = match.group(1)
                continue
            yield number, line
        elif match and match.group(1)[0] == marker[0] and len(match.group(1)) >= len(marker):
            marker = None


def screen_of(file_name: str) -> Optional[str]:
    match = re.match(r"(SCR-\d{2,3})(?:[-_.]|$)", file_name)
    return match.group(1) if match else None


def check_bundle(root: Path) -> List[Finding]:
    findings: List[Finding] = []
    docs = sorted(p for p in root.rglob("*.md") if "node_modules" not in p.parts)
    defined: Set[str] = set()
    used_files: Set[Path] = set()
    embeds: List[Tuple[Path, int, str]] = []
    rows: List[Tuple[Path, int, str, List[str]]] = []
    texts: Dict[Path, List[Tuple[int, str]]] = {}

    for doc in docs:
        lines = list(_visible_lines(doc.read_text(encoding="utf-8")))
        texts[doc] = lines
        for number, line in lines:
            row = ROW_SCREEN.match(line.strip())
            if row:
                defined.add(row.group(1))
                rows.append((doc, number, row.group(1), FILE_MENTION.findall(line)))
            for link in IMAGE_LINK.findall(line):
                embeds.append((doc, number, link))
            for name in FILE_MENTION.findall(line):
                used_files.add((doc.parent / "wireframes" / name).resolve())

    for doc, number, link in embeds:
        target = (doc.parent / link).resolve()
        used_files.add(target)
        rel = str(doc.relative_to(root))
        if not target.is_file():
            findings.append(Finding("error", rel, number, f"ảnh {link} không tồn tại"))
        screen = screen_of(Path(link).name)
        if not screen:
            findings.append(Finding("error", rel, number, f"tên ảnh {Path(link).name} phải bắt đầu bằng mã màn hình (SCR-01-...)"))
        elif screen not in defined:
            findings.append(Finding("error", rel, number, f"{screen} không có trong bảng Screen Inventory/SRS của bộ tài liệu"))
        following = [line for n, line in texts[doc] if number < n <= number + 3 and line.strip()]
        if not any(SOURCE_LINE.search(line) for line in following[:2]):
            findings.append(Finding("warning", rel, number, f"thiếu dòng \"Nguồn thiết kế: ...\" ngay dưới ảnh {Path(link).name}"))

    reported: Set[str] = set()
    for doc, lines in texts.items():
        for number, line in lines:
            for screen in SCREEN_ID.findall(line):
                if screen not in defined and screen not in reported:
                    reported.add(screen)
                    findings.append(Finding("warning", str(doc.relative_to(root)), number, f"{screen} được nhắc tới nhưng không có dòng nào trong bảng Screen Inventory/SRS"))

    for doc, number, screen, names in rows:
        for name in names:
            owner = screen_of(name)
            if owner and owner != screen:
                findings.append(Finding("error", str(doc.relative_to(root)), number, f"dòng {screen} trỏ tới ảnh của {owner} ({name})"))

    folders = {p.resolve() for p in root.rglob("wireframes") if p.is_dir() and "node_modules" not in p.parts}
    for folder in sorted(folders):
        for image in sorted(folder.iterdir()):
            if image.suffix.lower() in IMAGE_EXTS and image.resolve() not in used_files:
                findings.append(Finding("warning", str(image.relative_to(root.resolve())), 0, "ảnh không được tài liệu nào dùng"))
    return findings


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Vẽ wireframe HTML thành PNG và kiểm tra bộ màn hình (SCR-xx).")
    sub = parser.add_subparsers(dest="command", required=True)
    rend = sub.add_parser("render", help="Chụp file HTML wireframe thành PNG bằng Chrome/Edge headless")
    rend.add_argument("html", type=Path)
    rend.add_argument("-o", "--output", type=Path, default=None, help="Ảnh PNG (mặc định: cạnh file HTML, cùng tên)")
    rend.add_argument("--size", default=None, help="RỘNGxCAO, ví dụ 1280x800 hoặc 390x844")
    rend.add_argument("--scale", type=float, default=2.0, help="Hệ số điểm ảnh (mặc định 2)")
    rend.add_argument("--browser", default=None, help="Đường dẫn Chrome/Edge")
    chk = sub.add_parser("check", help="Kiểm tra ảnh wireframe/mockup và mã SCR-xx trong một bộ tài liệu")
    chk.add_argument("target", type=Path)
    chk.add_argument("--strict", action="store_true", help="Cảnh báo cũng làm mã thoát 1")
    args = parser.parse_args(argv)

    if args.command == "render":
        if not args.html.is_file():
            print(f"LỖI: không tìm thấy {args.html}")
            return 2
        browser = find_browser(args.browser)
        if not browser:
            print("LỖI: không tìm thấy Chrome hoặc Edge; truyền --browser <đường dẫn> hoặc đặt BA_MERMAID_BROWSER")
            return 2
        try:
            size = page_size(args.html.read_text(encoding="utf-8"), args.size)
        except ValueError as exc:
            print(f"LỖI: {exc}")
            return 2
        code, message = render(args.html, args.output or args.html.with_suffix(".png"), browser, size, args.scale)
        print(message)
        return code

    if not args.target.is_dir():
        print(f"LỖI: {args.target} không phải thư mục")
        return 2
    findings = check_bundle(args.target)
    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]
    print(f"# Kiểm tra wireframe: {len(errors)} lỗi, {len(warnings)} cảnh báo\n")
    if findings:
        print("| Mức | Vị trí | Chi tiết |")
        print("|---|---|---|")
        for f in findings:
            where = f"{f.file}:{f.line}" if f.line else f.file
            print(f"| {f.level} | {where} | {f.detail} |")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
