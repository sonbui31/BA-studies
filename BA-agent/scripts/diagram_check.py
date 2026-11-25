#!/usr/bin/env python3
"""Lint Mermaid diagrams in Markdown against so_do.md (the diagram standard).

Static checks (no Node needed):
  errors   PLACEHOLDER        {{...}} inside a diagram: Mermaid fails to render it
           STEREOTYPE_TAG     <<include>> in a flowchart renders as "<>"; write ≪include≫
           UNLABELED_BRANCH   a decision (rhombus) with several exits has an exit without a label
  warnings PLACEHOLDER_TEXT   {{...}} inside a label: renders, but must not remain in a delivered document
           NO_THEME           missing the standard %%{init ...}%% line (so_do.md 1.1)
           EMOJI              emoji inside a diagram
           NEWLINE_ESCAPE     "\\n" inside a label; use <br/>
           TOO_MANY_NODES     more steps than --max-nodes (events and gateways not counted)
           PARALLEL_UNPAIRED  an odd number of {"+"} gateways: a parallel split without a join

--render also draws every diagram with mermaid-cli (mmdc) and reports diagrams that fail.
--fix rewrites what is mechanical: inserts the standard init line, turns "\\n" into <br/>,
<<x>> into ≪x≫ in flowcharts, and removes emoji. Branch labels and placeholders stay manual.
Exit code: 1 when there are errors (with --strict, also warnings); 0 otherwise; 2 bad target.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

FENCE_OPEN = re.compile(r"^\s*```mermaid\s*$")
FENCE_CLOSE = re.compile(r"^\s*```\s*$")
PLACEHOLDER = re.compile(r"(?<![A-Za-z0-9_])\{\{")
STEREOTYPE = re.compile(r"<<\s*\w+\s*>>")
QUOTED = re.compile(r'"[^"]*"')
EDGE_LABEL = re.compile(r"\|[^|]*\|")
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF]")
ARROW = re.compile(r"(<-->|<?-\.+->|<?=+=>|<?-{2,}>|-{3,}|-\.+-)\s*(\|[^|]*\|)?")
NODE_ID = re.compile(r"^\s*([A-Za-z_][\w]*)")
RHOMBUS_DEF = re.compile(r"(?<![\w])([A-Za-z_]\w*)\s*\{(?!\{)([^{}]*)\}")
SHAPE_DEF = re.compile(r"(?<![\w])([A-Za-z_]\w*)\s*(\(\(\(|\(\(|\(\[|\[\[|\[\(|\[/|\[\\|\[|\(|\{\{|\{|>)")
EVENT_SHAPES = {"(((", "(("}
THEME_LINE = (
    '%%{init: {"theme": "base", "fontFamily": "Arial, Helvetica, sans-serif", "themeVariables": {"fontSize": "15px", '
    '"primaryColor": "#FFFFFF", "primaryBorderColor": "#4A5568", "primaryTextColor": "#1A202C", "lineColor": "#4A5568", '
    '"secondaryColor": "#F7FAFC", "tertiaryColor": "#F7FAFC", "clusterBkg": "#F7FAFC", "clusterBorder": "#A0AEC0", '
    '"edgeLabelBackground": "#FFFFFF", "actorBkg": "#EBF8FF", "actorBorder": "#2B6CB0", "noteBkgColor": "#FFF8E1", '
    '"noteBorderColor": "#B7791F"}}}%%'
)
EMOJI_WITH_SPACE = re.compile("(?:[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF]\uFE0F?\u200D?)+ ?")
# Mermaid also writes a label inside the arrow: A -- Có --> B, A -. Có .-> B, A == Có ==> B.
TEXT_ON_ARROW = [
    (re.compile(r"(?<![-.=<])--\s+([^\s>|-][^>|]*?)\s+(-->|---)"), lambda m: f"{m.group(2)}|{m.group(1)}|"),
    (re.compile(r"(?<![-.=<])==\s+([^\s>|=][^>|]*?)\s+(==>|===)"), lambda m: f"{m.group(2)}|{m.group(1)}|"),
    (re.compile(r"(?<![-.=<])-\.\s+([^\s>|.][^>|]*?)\s+(\.->|\.-)"), lambda m: f"-{m.group(2)}|{m.group(1)}|"),
]
OTHER_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
EMPTY_LABEL = re.compile(r"\[\s*\]|\(\s*\)|\{\s*\}|\|\s*\||\"\s*\"")
SKIP_LINE = re.compile(r"^\s*(%%|classDef\b|class\b|style\b|linkStyle\b|subgraph\b|end\b|direction\b|click\b)")


@dataclass
class Finding:
    level: str
    code: str
    file: str
    line: int
    detail: str


@dataclass
class Diagram:
    file: Path
    line: int  # line of the first diagram line in the Markdown file
    lines: List[str] = field(default_factory=list)

    @property
    def kind(self) -> str:
        for line in self.lines[front_matter_end(self.lines):]:
            stripped = line.strip()
            if not stripped or stripped.startswith("%%"):
                continue
            return stripped.split()[0]
        return ""

    @property
    def is_flowchart(self) -> bool:
        return self.kind in {"flowchart", "graph"}


def front_matter_end(lines: List[str]) -> int:
    """Index of the first line after a leading `---` ... `---` front-matter block (0 when none)."""
    first = next((i for i, line in enumerate(lines) if line.strip()), None)
    if first is None or lines[first].strip() != "---":
        return 0
    close = next((i for i in range(first + 1, len(lines)) if lines[i].strip() == "---"), None)
    return close + 1 if close is not None else 0


class _OuterFence:
    """Tracks non-Mermaid fences (```text, ````markdown examples...) so Mermaid shown inside them is skipped."""

    def __init__(self) -> None:
        self.marker: Optional[str] = None

    def inside(self, line: str) -> bool:
        match = OTHER_FENCE.match(line)
        if self.marker is None:
            if match and not FENCE_OPEN.match(line):
                self.marker = match.group(1)
                return True
            return False
        if match and match.group(1)[0] == self.marker[0] and len(match.group(1)) >= len(self.marker) and not line.strip()[len(match.group(1)):].strip():
            self.marker = None
        return True


def extract_diagrams(path: Path) -> List[Diagram]:
    diagrams: List[Diagram] = []
    current: Optional[Diagram] = None
    outer = _OuterFence()
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if current is None:
            if outer.inside(line):
                continue
            if FENCE_OPEN.match(line):
                current = Diagram(file=path, line=number + 1)
            continue
        if FENCE_CLOSE.match(line):
            diagrams.append(current)
            current = None
            continue
        current.lines.append(line)
    return diagrams


def _edges(lines: List[str]):
    """(source, target, labelled, line offset) for every arrow in a flowchart."""
    for offset, raw in enumerate(lines):
        for pattern, label in TEXT_ON_ARROW:
            raw = pattern.sub(label, raw)
        if SKIP_LINE.match(raw) or not ARROW.search(raw):
            continue
        parts = ARROW.split(raw)
        # parts = [segment, arrow, label, segment, arrow, label, segment, ...]
        segments = parts[0::3]
        labels = parts[2::3]
        for index in range(len(segments) - 1):
            left = NODE_ID.match(segments[index].split("&")[-1]) if index else NODE_ID.match(segments[index])
            right = NODE_ID.match(segments[index + 1])
            if left and right:
                yield left.group(1), right.group(1), bool(labels[index]), offset


def check_diagram(diagram: Diagram, max_nodes: int) -> List[Finding]:
    findings: List[Finding] = []
    name = str(diagram.file)
    text = "\n".join(diagram.lines)

    def add(level: str, code: str, offset: int, detail: str) -> None:
        findings.append(Finding(level, code, name, diagram.line + offset, detail))

    label_after_colon = diagram.kind in {"stateDiagram-v2", "stateDiagram", "sequenceDiagram", "journey"}
    for offset, line in enumerate(diagram.lines):
        structural = QUOTED.sub("", EDGE_LABEL.sub("", line))
        if label_after_colon:
            structural = structural.split(":", 1)[0]
        if PLACEHOLDER.search(structural):
            add("error", "PLACEHOLDER", offset, "{{...}} ở tên nút, tên trạng thái hoặc ngày làm Mermaid báo lỗi; dùng tên mẫu như ENTITY_A")
        elif PLACEHOLDER.search(line):
            add("warning", "PLACEHOLDER_TEXT", offset, "{{...}} trong nhãn: vẽ được nhưng tài liệu giao khách không được còn")
        if diagram.is_flowchart and STEREOTYPE.search(line):
            add("error", "STEREOTYPE_TAG", offset, "<<...>> hiện thành \"<>\"; viết ≪include≫ / ≪extend≫")
        if EMOJI.search(line):
            add("warning", "EMOJI", offset, "emoji trong sơ đồ hiển thị khác nhau giữa các máy và trong Word")
        if "\\n" in line and not line.strip().startswith("%%"):
            add("warning", "NEWLINE_ESCAPE", offset, "dùng <br/> thay cho \\n để xuống dòng")
    if not any(line.strip().startswith("%%{init") for line in diagram.lines):
        add("warning", "NO_THEME", 0, "thiếu dòng khai báo chuẩn %%{init ...}%% (so_do.md mục 1.1)")

    if not diagram.is_flowchart:
        return findings

    gateways: Dict[str, str] = {}
    shapes: Dict[str, str] = {}
    for line in diagram.lines:
        if SKIP_LINE.match(line):
            continue
        for match in RHOMBUS_DEF.finditer(line):
            gateways[match.group(1)] = match.group(2)
        for match in SHAPE_DEF.finditer(line):
            shapes.setdefault(match.group(1), match.group(2))

    outgoing: Dict[str, List[tuple]] = {}
    for source, target, labelled, offset in _edges(diagram.lines):
        outgoing.setdefault(source, []).append((target, labelled, offset))
    for gateway, label in gateways.items():
        exits = outgoing.get(gateway, [])
        is_parallel = label.strip().strip('"').strip() == "+"
        if len(exits) >= 2 and not is_parallel:
            for target, labelled, offset in exits:
                if not labelled:
                    add("error", "UNLABELED_BRANCH", offset, f"nhánh {gateway} -> {target} không có nhãn điều kiện")

    parallel = [g for g, label in gateways.items() if label.strip().strip('"').strip() == "+"]
    if len(parallel) % 2:
        add("warning", "PARALLEL_UNPAIRED", 0, "số cổng song song {\"+\"} lẻ: thiếu điểm hợp cho nhánh song song")

    steps = [node for node, shape in shapes.items() if shape not in EVENT_SHAPES and node not in gateways]
    if len(steps) > max_nodes:
        add("warning", "TOO_MANY_NODES", 0, f"{len(steps)} bước (tối đa {max_nodes}); tách thành quy trình con [[...]]")
    return findings


def fix_file(path: Path) -> int:
    """Apply the mechanical fixes to every Mermaid block of a file; return the number of changed lines."""
    with open(path, encoding="utf-8", newline="") as handle:
        original = handle.read()
    newline = "\r\n" if "\r\n" in original else "\n"
    lines = original.split(newline)
    out: List[str] = []
    changed = 0
    inside = False
    block_start = 0
    kind = ""
    front: Optional[str] = None
    outer = _OuterFence()
    for line in lines:
        if not inside:
            out.append(line)
            if outer.inside(line):
                continue
            if FENCE_OPEN.match(line):
                inside, block_start, kind, front = True, len(out), "", None
            continue
        if FENCE_CLOSE.match(line):
            body = out[block_start:]
            if not any(item.strip().startswith("%%{init") for item in body):
                at = block_start + front_matter_end(body)  # the init line goes after front-matter
                indent = re.match(r"\s*", body[0]).group(0) if body else ""
                out.insert(at, indent + THEME_LINE)
                changed += 1
            out.append(line)
            inside = False
            continue
        new = line
        stripped = line.strip()
        if front is None and stripped:
            front = "in" if stripped == "---" else "done"
        elif front == "in" and stripped == "---":
            front = "done"
            out.append(line)
            continue
        if front == "in":  # front-matter (title, config): left as written
            out.append(line)
            continue
        if not kind and stripped and not stripped.startswith("%%"):
            kind = stripped.split()[0]
        if not stripped.startswith("%%"):
            new = new.replace("\\n", "<br/>")
            if kind in {"flowchart", "graph"}:
                new = STEREOTYPE.sub(lambda m: "≪" + m.group(0)[2:-2].strip() + "≫", new)
            without_emoji = EMOJI_WITH_SPACE.sub("", new)
            # A label made only of emoji would become empty; leave that line for a person to reword.
            if len(EMPTY_LABEL.findall(without_emoji)) <= len(EMPTY_LABEL.findall(new)):
                new = without_emoji
        if new != line:
            changed += 1
        out.append(new)
    if changed:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(newline.join(out))
    return changed


def render_check(diagrams: List[Diagram], mmdc: str, browser: Optional[str]) -> List[Finding]:
    findings: List[Finding] = []
    with tempfile.TemporaryDirectory() as tmp:
        config: Optional[Path] = None
        if browser:
            config = Path(tmp) / "puppeteer.json"
            config.write_text(json.dumps({"executablePath": browser, "args": ["--no-sandbox"]}), encoding="utf-8")
        for index, diagram in enumerate(diagrams):
            src, out = Path(tmp) / f"d{index}.mmd", Path(tmp) / f"d{index}.svg"
            src.write_text("\n".join(diagram.lines), encoding="utf-8")
            cmd = [mmdc, "-i", str(src), "-o", str(out), "-q"] + (["-p", str(config)] if config else [])
            try:
                proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
                ok = proc.returncode == 0 and out.is_file()
                message = (proc.stderr or proc.stdout or "").strip().splitlines()
            except (OSError, subprocess.TimeoutExpired) as exc:
                ok, message = False, [str(exc)]
            if not ok:
                findings.append(
                    Finding("error", "RENDER_FAILED", str(diagram.file), diagram.line, message[0] if message else "mmdc failed")
                )
    return findings


def collect(target: Path) -> List[Path]:
    if target.is_file():
        return [target]
    return sorted(p for p in target.rglob("*.md") if "node_modules" not in p.parts)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Kiểm tra sơ đồ Mermaid theo chuẩn so_do.md.")
    parser.add_argument("target", type=Path, help="File .md hoặc thư mục")
    parser.add_argument("--strict", action="store_true", help="Cảnh báo cũng làm mã thoát 1")
    parser.add_argument("--max-nodes", type=int, default=12, help="Số bước tối đa của một flowchart (mặc định 12)")
    parser.add_argument("--render", action="store_true", help="Vẽ thử từng sơ đồ bằng mermaid-cli (mmdc)")
    parser.add_argument("--mmdc", default=None, help="Đường dẫn mmdc (mặc định: mmdc trong PATH)")
    parser.add_argument("--browser", default=None, help="Chrome/Edge đã cài, khi mmdc không có Chromium riêng")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--fix", action="store_true", help="Sửa phần máy móc (khai báo chuẩn, <br/>, ≪≫, emoji) rồi kiểm tra lại")
    args = parser.parse_args(argv)

    if not args.target.exists():
        print(f"LỖI: không tìm thấy {args.target}")
        return 2
    if args.fix:
        for path in collect(args.target):
            count = fix_file(path)
            if count:
                print(f"Đã sửa {count} dòng: {path}")
    diagrams = [diagram for path in collect(args.target) for diagram in extract_diagrams(path)]
    findings = [finding for diagram in diagrams for finding in check_diagram(diagram, args.max_nodes)]
    if args.render:
        local = Path(__file__).resolve().parent / "node_modules" / ".bin" / ("mmdc.cmd" if sys.platform == "win32" else "mmdc")
        mmdc = shutil.which(args.mmdc or "mmdc") or (args.mmdc if args.mmdc and Path(args.mmdc).is_file() else None)
        mmdc = mmdc or (str(local) if not args.mmdc and local.is_file() else None)
        if not mmdc:
            print("LỖI: --render cần mermaid-cli (npm i -g @mermaid-js/mermaid-cli) hoặc --mmdc <đường dẫn>")
            return 2
        findings += render_check(diagrams, mmdc, args.browser)

    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]
    if args.format == "json":
        print(json.dumps({"diagrams": len(diagrams), "findings": [f.__dict__ for f in findings]}, ensure_ascii=False, indent=2))
    else:
        print(f"# Kiểm tra sơ đồ: {len(diagrams)} sơ đồ, {len(errors)} lỗi, {len(warnings)} cảnh báo")
        if findings:
            print()
            print("| Mức | Mã | Vị trí | Chi tiết |")
            print("|---|---|---|---|")
            for f in findings:
                print(f"| {f.level} | {f.code} | {f.file}:{f.line} | {f.detail} |")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
