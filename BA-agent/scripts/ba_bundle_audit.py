#!/usr/bin/env python3
import re
import sys
from pathlib import Path


try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"

VERSIONED_FILES = [
    ROOT / "SKILL.md",
    ROOT / "Anti_ai_writing_rules.md",
    ROOT / "so_do.md",
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
    ROOT / "Anti_ai_writing_rules.md",
    ROOT / "so_do.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "agents" / "ba-specialist.md",
    ROOT / "workflows" / "ba-workflow.md",
    ROOT / "scripts" / "preflight_check.py",
    ROOT / "scripts" / "quality_rubric.py",
    ROOT / "scripts" / "traceability_scan.py",
    ROOT / "scripts" / "reindex_markdown.py",
    ROOT / "scripts" / "template_schema_check.py",
    ROOT / "scripts" / "media_audit.py",
    ROOT / "scripts" / "knowledge_search.py",
    ROOT / "scripts" / "build_knowledge_index.py",
    ROOT / "scripts" / "knowledge_index_search.py",
    ROOT / "scripts" / "build_semantic_index.py",
    ROOT / "scripts" / "semantic_index_search.py",
    ROOT / "scripts" / "ba_response_eval.py",
    ROOT / "scripts" / "eval_golden_cases.py",
    ROOT / "scripts" / "ai_smell_scan.py",
    ROOT / "scripts" / "persona_review_check.py",
    ROOT / "knowledge-source" / "babok-v3-framework.md",
    ROOT / "knowledge-source" / "ba-update-2026-11-14.md",
    ROOT / "knowledge-source" / "ba-update-2026-11-21.md",
    ROOT / "BA-document-rule" / "core" / "rigor-tiers.md",
    ROOT / "BA-document-rule" / "core" / "strategy-analysis-guide.md",
    ROOT / "BA-document-rule" / "core" / "solution-evaluation-guide.md",
    ROOT / "BA-document-rule" / "core" / "senior-ba-rubric.md",
    ROOT / "BA-document-rule" / "core" / "persona-simulation.md",
    ROOT / "BA-document-rule" / "core" / "document-rulebook.md",
    ROOT / "BA-document-rule" / "core" / "intake-triage.md",
    ROOT / "BA-document-rule" / "core" / "evidence-source-gate.md",
    ROOT / "BA-document-rule" / "core" / "slice-baselining.md",
    ROOT / "BA-document-rule" / "core" / "human-accountability.md",
    ROOT / "BA-document-rule" / "core" / "pilot-protocol.md",
    ROOT / "scripts" / "id_migrate.py",
    ROOT / "scripts" / "diagram_check.py",
    ROOT / "scripts" / "bpmn_tool.py",
    ROOT / "scripts" / "bpmn_render.mjs",
    ROOT / "scripts" / "wireframe_tool.py",
    ROOT / "tests" / "test_wireframes.py",
    ROOT / "scripts" / "package.json",
    ROOT / "tests" / "test_bpmn.py",
    ROOT / "diagrams" / "vi-du-hoan-tien.bpmn",
    ROOT / "BA-Documents-Outsource" / "diagrams" / "p1-dieu-chuyen-tobe.bpmn",
    ROOT / "tests" / "test_diagrams.py",
    ROOT / "scripts" / "md_to_docx.py",
    ROOT / "scripts" / "docx_feedback.py",
    ROOT / "tests" / "fixtures" / "real_world_patterns" / "ba-scheme.json",
    ROOT / "tests" / "golden" / "real_project_tool_run_2026-11-21.md",
    ROOT / "scripts" / "README.md",
    ROOT / "BA-document-rule" / "references" / "elicitation-playbook.md",
    ROOT / "BA-document-rule" / "references" / "senior-ba-soft-skills.md",
    ROOT / "BA-document-rule" / "references" / "case-study-parent-app.md",
    ROOT / "BA-document-rule" / "references" / "vn-regulatory-watchlist.md",
    ROOT / "tests" / "golden" / "senior_judgement_cases.jsonl",
    ROOT / "BA-document-rule" / "references" / "ba-knowledge-base.md",
    ROOT / "BA-document-rule" / "references" / "ba-knowledge-cards.json",
    ROOT / "knowledge-index" / "manifest.json",
    ROOT / "knowledge-source" / "source-manifest.json",
    ROOT / "knowledge-source" / "download-instructions.md",
    ROOT / "requirements-knowledge-index.txt",
    ROOT / "requirements-semantic-index.txt",
    ROOT / "tests" / "golden" / "ba_response_cases.jsonl",
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


HEADER_VERSIONED_FILES = [
    ROOT / "USER-GUIDE.md",
    ROOT / "DOCUMENT-MAP.md",
    ROOT / "agents" / "ba-specialist.md",
    ROOT / "workflows" / "ba-workflow.md",
    ROOT / "BA-document-rule" / "README.md",
    ROOT / "BA-document-rule" / "core" / "principles.md",
    ROOT / "BA-document-rule" / "core" / "traceability-validator.md",
]
HEADER_VERSION_PATTERN = re.compile(r"\b(\d+)\.(\d+)(?:\.\d+)?\b")


def stale_header_versions(release_tuple, release_text):
    """The title / 'Phiên bản:' line of a current-state document must name the current MAJOR.MINOR."""
    errors = []
    for path in HEADER_VERSIONED_FILES:
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()[:8]
        header_lines = [line for line in lines if line.startswith("# ") or "Phiên bản:" in line]
        for line in header_lines:
            for match in HEADER_VERSION_PATTERN.finditer(line):
                major, minor = int(match.group(1)), int(match.group(2))
                if major == release_tuple[0] and minor != release_tuple[1]:
                    errors.append(
                        f"{path.relative_to(ROOT)} header says {match.group(0)} but the release is {release_text}: {line.strip()}"
                    )
    return errors


def missing_agent_skills():
    """Agent frontmatter must not reference skills that do not exist."""
    errors = []
    for path in (ROOT / "agents").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^skills:\s*\[([^\]]*)\]", text, re.MULTILINE)
        if not match:
            continue
        for name in [item.strip() for item in match.group(1).split(",") if item.strip()]:
            candidates = list(ROOT.parent.glob(f"**/skills/{name}/SKILL.md")) + list(ROOT.glob(f"**/{name}/SKILL.md"))
            if not candidates:
                errors.append(f"{path.relative_to(ROOT)} references missing skill '{name}'")
    return errors


SKILL_PATH_PATTERN = re.compile(r"`((?:BA-agent/)?[\w\-./ ]+?\.(?:md|py|json|jsonl|pdf|docx))`")


def broken_skill_paths():
    """Every file path written in backticks in SKILL.md must exist."""
    errors = []
    skill = ROOT / "SKILL.md"
    if not skill.exists():
        return errors
    bases = [ROOT, ROOT / "BA-document-rule", ROOT / "scripts", ROOT / "Curated templates", ROOT / "knowledge-source"]
    for match in SKILL_PATH_PATTERN.finditer(skill.read_text(encoding="utf-8")):
        raw = match.group(1)
        rel = raw[len("BA-agent/"):] if raw.startswith("BA-agent/") else raw
        if any(token in rel for token in ("<", "*")) or "/" not in rel and not rel.endswith(".py"):
            # bare file names like `02-BRD.md` are output names, not references
            if not rel.endswith(".py"):
                continue
        if not any((base / rel).exists() for base in bases):
            errors.append(f"SKILL.md references a file that does not exist: {raw}")
    return sorted(set(errors))


RULE_FILES_GLOBS = ["SKILL.md", "agents/*.md", "workflows/*.md", "BA-document-rule/core/*.md"]
MIN_DUPLICATE_CHARS = 120


def _normalize_rule_line(line: str) -> str:
    text = re.sub(r"[`*_>#|]", " ", line)
    text = re.sub(r"^\s*(?:[-+]|\d+[.)]|[A-Z]\d+\.)\s+", "", text)
    text = re.sub(r"\(?(?:\.\./)*[\w\-./]+\.(?:md|py|json)\)?", " ", text)  # paths differ by ../ prefix
    return re.sub(r"\s+", " ", text).strip().lower()


def duplicated_rule_text():
    """A rule sentence copied into several rule files drifts apart over time (one owner per rule).

    Flags any normalized line of at least MIN_DUPLICATE_CHARS characters that appears in more than
    one of SKILL.md, agents/, workflows/ and BA-document-rule/core/. Point to the owner instead.
    """
    seen = {}
    for pattern in RULE_FILES_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            in_fence = False
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.lstrip().startswith(("```", "~~~")):
                    in_fence = not in_fence
                    continue
                if in_fence or re.fullmatch(r"\s*\|?[\s:|-]+\|?\s*", line):
                    continue
                key = _normalize_rule_line(line)
                if len(key) < MIN_DUPLICATE_CHARS:
                    continue
                seen.setdefault(key, set()).add(str(path.relative_to(ROOT)))
    return sorted(
        f"Rule text copied in {', '.join(sorted(paths))}: \"{key[:90]}...\" (keep it in one owner file and point to it)"
        for key, paths in seen.items()
        if len(paths) > 1
    )


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

    errors.extend(stale_header_versions(release_tuple, release_text))
    errors.extend(missing_agent_skills())
    errors.extend(broken_skill_paths())
    errors.extend(duplicated_rule_text())

    legacy_story_refs = []
    legacy_story_pattern = re.compile(r"\bUS\d{2,3}\b")
    fixtures = ROOT / "tests"
    for path in ROOT.rglob("*.md"):
        if fixtures in path.parents:
            continue  # fixtures and pilot records quote real projects' legacy IDs on purpose
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
