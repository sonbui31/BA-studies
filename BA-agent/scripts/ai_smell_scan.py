#!/usr/bin/env python3
"""Scan Markdown files for AI-writing smells (Vietnamese and English patterns).

Rules come from Anti_ai_writing_rules.md (Dieu 1, 2, 3, 7, 8, 9, 15, 20) plus a Vietnamese appendix.
Fenced code blocks are skipped. Findings are warnings: exit code is 0 unless --strict is passed.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterator, List, Tuple


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# (category, rule, regex, suggestion)
RULES: List[Tuple[str, str, str, str]] = [
    ("vi-vague-praise", "Dieu 8-9", r"đóng vai trò (?:quan trọng|then chốt|cốt lõi|thiết yếu|chủ chốt)", "Nói cụ thể thành phần đó làm gì"),
    ("vi-contrast", "Dieu 3", r"không chỉ\b.{1,80}?\bmà còn", "Nói thẳng từng ý, bỏ cấu trúc đối lập"),
    ("vi-filler", "Dieu 7", r"nhằm mục đích|với mục đích", "Dùng 'để' hoặc bỏ"),
    ("vi-vague-praise", "Dieu 9", r"mang lại (?:giá trị|lợi ích|trải nghiệm|hiệu quả)", "Ghi lợi ích cụ thể có số"),
    ("vi-vague-praise", "Dieu 9", r"một cách (?:hiệu quả|toàn diện|tối ưu|mượt mà|liền mạch|nhanh chóng)", "Bỏ trạng từ, ghi metric nếu cần"),
    ("vi-vague-praise", "Dieu 1", r"(?:giải pháp|nền tảng|hệ thống|trải nghiệm)\s+(?:toàn diện|đột phá|tối ưu|mạnh mẽ|liền mạch)", "Bỏ tính từ, mô tả chức năng cụ thể"),
    ("vi-vague-praise", "Dieu 1", r"\b(?:nâng tầm|đột phá|hệ sinh thái|sợi dây liên kết|tối ưu hóa trải nghiệm)\b", "Thay bằng mô tả cụ thể"),
    ("vi-filler", "Dieu 7", r"đảm bảo rằng|góp phần (?:nâng cao|cải thiện|thúc đẩy|tạo)", "Nói thẳng hành động và kết quả"),
    ("vi-hedge", "Dieu 2", r"(?:cần lưu ý rằng|đáng chú ý là|đáng lưu ý|có thể nói rằng|không thể phủ nhận|điều quan trọng là)", "Bỏ phần dẫn, nói thẳng nội dung"),
    ("vi-opener", "Dieu 2", r"(?:^|[.!?]\s+)(?:Bên cạnh đó|Hơn nữa|Tóm lại|Nhìn chung|Nói tóm lại|Tổng kết lại)\s*,", "Nối thẳng vào câu trước hoặc xóa"),
    ("vi-cliche", "Dieu 11", r"trong bối cảnh .{0,60}(?:hiện nay|ngày càng)|ngày càng (?:phát triển|quan trọng|đa dạng)", "Bỏ câu mở đầu chung chung"),
    ("en-vocab", "Dieu 1", r"\b(?:crucial|delve|pivotal|robust|meticulous(?:ly)?|tapestry|showcas(?:e|ing)|underscor(?:e|es|ing)|testament|vibrant|groundbreaking|intricate|intricacies|seamless(?:ly)?)\b", "Thay bằng từ đơn giản hoặc xóa"),
    ("en-opener", "Dieu 2", r"(?:^|[.!?]\s+)(?:Additionally|Consequently|Notably|In summary|In conclusion|Overall)\s*,|it(?:'s| is) (?:important|crucial|worth) (?:to )?(?:note|noting)", "Nối thẳng vào câu trước"),
    ("assistant-voice", "Dieu 15", r"\b(?:Of course!|Certainly!|I hope this helps|Let me know if|Feel free to|Would you like me to)", "Xóa hoàn toàn"),
    ("tool-fingerprint", "Dieu 20", r"contentReference|oaicite|turn\d+search\d+|grok_card|:::writing\{", "Xóa dấu vết công cụ"),
]

COMPILED = [(cat, rule, re.compile(pattern, re.IGNORECASE), hint) for cat, rule, pattern, hint in RULES]
EXCLUDED_FILES = {"anti_ai_writing_rules.md"}


def iter_markdown(target: Path) -> Iterator[Path]:
    if not target.exists():
        raise FileNotFoundError(f"Target does not exist: {target}")
    if target.is_file():
        yield target
        return
    for path in sorted(target.rglob("*.md")):
        if path.name.lower() in EXCLUDED_FILES:
            continue
        yield path


def scan_text(text: str) -> List[Dict[str, object]]:
    findings: List[Dict[str, object]] = []
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for category, rule, regex, hint in COMPILED:
            for match in regex.finditer(line):
                findings.append(
                    {
                        "line": line_no,
                        "category": category,
                        "rule": rule,
                        "match": match.group(0).strip(),
                        "hint": hint,
                    }
                )
    return findings


def scan_path(target: Path) -> Dict[str, object]:
    files = []
    total = 0
    for path in iter_markdown(target):
        findings = scan_text(path.read_text(encoding="utf-8"))
        total += len(findings)
        files.append({"file": str(path), "findings": findings})
    return {"target": str(target), "total": total, "files": files}


def format_markdown(report: Dict[str, object]) -> str:
    lines = [f"# AI SMELL SCAN", f"> Target: `{report['target']}`", ""]
    flagged = [item for item in report["files"] if item["findings"]]
    if not flagged:
        lines.append("Không phát hiện mẫu AI nào.")
        return "\n".join(lines)
    for item in flagged:
        lines.append(f"## {Path(item['file']).name} ({len(item['findings'])})")
        lines.append("")
        lines.append("| Dòng | Điều | Mẫu | Gợi ý |")
        lines.append("|---:|---|---|---|")
        for f in item["findings"]:
            lines.append(f"| {f['line']} | {f['rule']} | `{f['match']}` | {f['hint']} |")
        lines.append("")
    lines.append(f"**Tổng:** {report['total']} mẫu trong {len(flagged)} file.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan Markdown files for AI-writing smells.")
    parser.add_argument("target", help="Markdown file or folder")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--strict", action="store_true", help="Exit 1 when any smell is found")
    args = parser.parse_args()

    try:
        report = scan_path(Path(args.target).resolve())
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(format_markdown(report))
    return 1 if args.strict and report["total"] else 0


if __name__ == "__main__":
    sys.exit(main())
