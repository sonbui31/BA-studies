#!/usr/bin/env python3
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"

VERSIONED_FILES = [
    ROOT / "SKILL.md",
    ROOT / "USER-GUIDE.md",
    ROOT / "DOCUMENT-MAP.md",
    ROOT / "agents" / "ba-specialist.md",
    ROOT / "workflows" / "ba-workflow.md",
    ROOT / "BA-document-rule" / "README.md",
    ROOT / "BA-document-rule" / "core" / "principles.md",
    ROOT / "BA-document-rule" / "core" / "traceability-validator.md",
]

REQUIRED_FILES = [
    ROOT / "SKILL.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "agents" / "ba-specialist.md",
    ROOT / "workflows" / "ba-workflow.md",
    ROOT / "scripts" / "preflight_check.py",
    ROOT / "scripts" / "quality_rubric.py",
    ROOT / "scripts" / "traceability_scan.py",
    ROOT / "scripts" / "reindex_markdown.py",
]


def parse_version(text: str):
    match = re.search(r"## \[(\d+\.\d+\.\d+)\]", text)
    if not match:
        raise ValueError("Cannot find release version in CHANGELOG.md")
    return tuple(int(part) for part in match.group(1).split(".")), match.group(1)


def scan_versions(text: str):
    matches = set(re.findall(r"\b(?:v|Version[: ]+|Phiên bản:\s*)(\d+\.\d+(?:\.\d+)?)", text, re.IGNORECASE))
    versions = []
    for match in matches:
        parts = tuple(int(part) for part in match.split("."))
        versions.append((parts, match))
    return sorted(versions)


def main():
    errors = []
    warnings = []

    try:
        changelog_text = CHANGELOG.read_text(encoding="utf-8")
        release_tuple, release_text = parse_version(changelog_text)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required bundle file: {path.relative_to(ROOT)}")

    for path in VERSIONED_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        versions = scan_versions(text)
        future_versions = [raw for parsed, raw in versions if parsed > release_tuple]
        if future_versions:
            errors.append(
                f"{path.relative_to(ROOT)} contains future version markers beyond {release_text}: {', '.join(sorted(future_versions))}"
            )

    legacy_story_refs = []
    legacy_story_pattern = re.compile(r"\bUS\d{2,3}\b")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if legacy_story_pattern.search(text):
            legacy_story_refs.append(path.relative_to(ROOT))

    if legacy_story_refs:
        warnings.append(
            "Legacy story ID examples still exist in: "
            + ", ".join(str(path) for path in sorted(legacy_story_refs))
        )

    print(f"BA bundle audit for release {release_text}")
    if not errors and not warnings:
        print("PASS: bundle metadata and version markers are aligned.")
        return 0

    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"- {error}")

    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"- {warning}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
