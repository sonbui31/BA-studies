#!/usr/bin/env python3
"""Audit curated template media declarations and markdown image links."""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set


ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "Curated templates"
MEDIA = CURATED / "media"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
IMAGE_LINK_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def image_files(media_dir: Path = MEDIA) -> List[Path]:
    if not media_dir.exists():
        raise FileNotFoundError(f"Media folder does not exist: {media_dir}")
    return sorted(path for path in media_dir.iterdir() if path.is_file() and path.suffix.lower() in IMAGE_EXTS)


def markdown_files(root: Path = CURATED) -> List[Path]:
    if not root.exists():
        raise FileNotFoundError(f"Curated templates folder does not exist: {root}")
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def extract_image_links(root: Path = CURATED) -> List[Dict[str, object]]:
    links: List[Dict[str, object]] = []
    for path in markdown_files(root):
        for line_no, line in enumerate(read_text(path).splitlines(), start=1):
            for match in IMAGE_LINK_PATTERN.finditer(line):
                ref = match.group(1).strip()
                resolved = (path.parent / ref).resolve()
                links.append(
                    {
                        "file": str(path),
                        "line": line_no,
                        "ref": ref,
                        "resolved": str(resolved),
                        "exists": resolved.exists(),
                    }
                )
    return links


def declared_media_names(media_readme: Path) -> Set[str]:
    if not media_readme.exists():
        return set()
    text = read_text(media_readme)
    return set(re.findall(r"`([^`]+\.(?:png|jpg|jpeg|gif|webp|svg))`", text, flags=re.IGNORECASE))


def evaluate_media(curated_root: Path = CURATED) -> Dict[str, object]:
    media_dir = curated_root / "media"
    media_readme = media_dir / "README.md"
    files = image_files(media_dir)
    links = extract_image_links(curated_root)
    declared = declared_media_names(media_readme)
    embedded_names = {Path(str(link["resolved"])).name for link in links if Path(str(link["resolved"])).parent == media_dir.resolve()}
    media_names = {path.name for path in files}

    gaps: List[Dict[str, str]] = []
    for link in links:
        if not link["exists"]:
            gaps.append({"type": "BROKEN_IMAGE_LINK", "item": f"{link['file']}:{link['line']}", "detail": str(link["ref"])})
    for name in sorted(media_names - declared):
        gaps.append({"type": "UNDECLARED_MEDIA", "item": name, "detail": "Image exists but is not listed in media/README.md"})
    for name in sorted(declared - media_names):
        gaps.append({"type": "STALE_MEDIA_DECLARATION", "item": name, "detail": "media/README.md lists a missing image"})

    return {
        "target": str(media_dir),
        "metrics": {
            "media_total": len(media_names),
            "embedded_total": len(embedded_names),
            "declared_total": len(declared),
            "reference_only_total": len(media_names - embedded_names),
            "gap_total": len(gaps),
        },
        "embedded_media": sorted(embedded_names),
        "reference_only_media": sorted(media_names - embedded_names),
        "links": links,
        "gaps": gaps,
    }


def print_markdown(report: Dict[str, object]) -> None:
    print("# MEDIA AUDIT REPORT")
    print(f"> Target: `{report['target']}`\n")
    print("## Summary\n")
    print("| Metric | Value |")
    print("|---|---|")
    for key, value in report["metrics"].items():
        print(f"| {key} | {value} |")
    print("\n## Gaps\n")
    if not report["gaps"]:
        print("No media gaps detected.")
        return
    print("| Type | Item | Detail |")
    print("|---|---|---|")
    for gap in report["gaps"]:
        print(f"| {gap['type']} | {gap['item']} | {gap['detail']} |")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit curated template media links and declarations.")
    parser.add_argument("target", nargs="?", default=str(CURATED), help="Curated templates folder")
    parser.add_argument("--output-json", help="Write JSON report")
    args = parser.parse_args()

    report = evaluate_media(Path(args.target).resolve())
    print_markdown(report)
    if args.output_json:
        Path(args.output_json).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return 1 if report["metrics"]["gap_total"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
