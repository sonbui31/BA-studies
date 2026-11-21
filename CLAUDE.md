# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Vietnamese Business Analysis knowledge base whose core is `BA-agent/`, a Claude skill. Most "code" is Markdown rule documents that steer the AI. The Python scripts in `BA-agent/scripts/` audit BA documents and the bundle itself. Documents are written in Vietnamese with diacritics. Keep that language and read/write every file as UTF-8.

- `BA-agent/`: the skill (entrypoint `SKILL.md`), rules, templates, scripts, tests, and two sample bundles.
- `projects/`: real project deliverables produced with the skill. Several are gitignored.
- `learning/` and `.agent/` are gitignored. `.agent/skills/ba-agent/SKILL.md` and `.agent/agents/ba-specialist.md` are local copies of `BA-agent/SKILL.md` and `BA-agent/agents/ba-specialist.md`, with relative `../` paths rewritten to `BA-agent/`. After editing either source, re-sync these copies.

## Commands

Run from the repo root. Requires Python 3.11+ (CI uses 3.11) and only the standard library. The exception is the knowledge-index builders, which need `requirements-knowledge-index.txt` / `requirements-semantic-index.txt`.

```bash
python BA-agent/scripts/ba_bundle_audit.py                       # required files, version markers, SKILL.md paths exist
python -m unittest discover -s BA-agent/tests -v                 # all tests
python -m unittest discover -s BA-agent/tests -k one_to_one      # single test by name substring
python BA-agent/scripts/eval_golden_cases.py --format markdown   # golden cases in tests/golden/
python BA-agent/scripts/template_schema_check.py "BA-agent/Curated templates"
python BA-agent/scripts/media_audit.py "BA-agent/Curated templates"
python BA-agent/scripts/traceability_scan.py BA-agent/BA-Documents-Outsource --scheme canonical --strict
python BA-agent/scripts/traceability_scan.py projects/QLTS --scheme project --strict   # real bundle with its own IDs (ba-scheme.json)
python BA-agent/scripts/preflight_check.py BA-agent/BA-Documents-Product
python BA-agent/scripts/ai_smell_scan.py <file-or-dir>           # Vietnamese/English "AI-sounding" prose
```

CI (`.github/workflows/ba-agent-ci.yml`) runs all of the above and also runs strict traceability on `tests/fixtures/canonical_bundle`, `tests/fixtures/canonical_full_bundle`, both sample bundles, and `--scheme project` on `tests/fixtures/real_world_patterns`. Any change to scripts, sample documents, or rules must keep these passing. `BA-agent/scripts/README.md` lists every script with its exit codes.

## Architecture

**The skill layer is read on demand.**
- `SKILL.md` is the orchestrator. It covers:
  - intake triage (lanes L0–L4);
  - the 6-step process;
  - Hard Gates 1–7;
  - Rigor Tiers 1–3.

  It points to detail files and does not duplicate them.
- The detail lives in:
  - `BA-document-rule/core/` (process rules, gates, tiers, rubrics);
  - `BA-document-rule/templates/` and `Curated templates/` (document skeletons);
  - `BA-document-rule/overlays/<project-type>/` (outsource, product, fintech, healthcare, government, startup-mvp, inhouse);
  - `BA-document-rule/references/`.
- The agent persona (`agents/ba-specialist.md`) and the workflow (`workflows/ba-workflow.md`) restate the same rules from another angle.
- A rule change usually touches `SKILL.md`, the relevant core doc, the agent, the workflow, `USER-GUIDE.md`, `DOCUMENT-MAP.md`, and `CHANGELOG.md` together.

**The scripts share one ID and classification module, `scripts/ba_id_utils.py`.**
- The canonical ID scheme is `BRQ-01`, `BR-001`, `FR-<MOD>-001`, `NFR-<TYPE>-001`, `F01`, `US-<MOD>-001`, `AC-/TC-<MOD>-001`. The legacy scheme is `BRD-xxx`, `FR-001`, `US-001`, `UAT-001`.
- The traceability chain is BRQ/BR → FR/NFR → (Feature, only when a Feature Map exists) → US → AC/TC. Links are N:M by default.
- **The file name decides a document's role.** `brd` → BRD; `srs`/`prd`/`requirement`/`yeu-cau` → SRS; `story` → User Story; `uat`/`acceptance`/`test`/`beta` → UAT/AC; `feature` → Feature Map.
- An ID counts as a *definition* only when it appears in a file of the matching role and starts a table row, heading, list item, or line. Everywhere else it counts as a reference. IDs inside code fences are ignored.
- Renaming sample files or moving IDs out of first table cells changes scan results.

**Real bundles keep their own IDs.** A `ba-scheme.json` in a bundle folder declares extra ID formats per kind, file roles and domain actors; every script loads it through `find_project_scheme`/`set_project_scheme` (a module-level global in `ba_id_utils`, so tests reset it in `tearDown`). Beyond same-line links, the scanner reads links on the lines under a definition (`definition_blocks`), attribute tables (`| ID | FR-X-001 |`), and matrix rows in any file (`matrix_lines`). Sub-IDs (`FR-TEA-003.1`) belong to their parent (`parent_id`). Numbering gaps and cross-file duplicates are judged only in the family's own document (`FAMILY_PRIMARY_ROLE`). `tests/fixtures/real_world_patterns/` reproduces the patterns found in `projects/`; when a script raises a false alarm on a real document, add the pattern there first (`BA-document-rule/core/pilot-protocol.md`).

**Document headers drive the checks.**
- `preflight_check.py` and `persona_review_check.py` read `Tier:` near the top of a document.
- For preflight, no Tier means the Evidence Sources check is N/A. For persona review, no Tier is checked as Tier 3.
- `preflight_check.py` Human Sign-off: a document whose `Trạng thái:` or version history claims approval must have a dated row in its sign-off table and no `[CẦN XÁC NHẬN]` (Hard Gate 8, `core/human-accountability.md`).
- `reindex_markdown.py` freezes ID groups defined in signed documents. A document counts as signed when its first 40 lines contain "Đã phê duyệt", "Chốt phạm vi", or "Trạng thái: Baseline". Never renumber IDs in signed baselines by hand either.

**Sample bundles are test inputs.**
- `BA-Documents-Outsource/` and `BA-Documents-Product/` are labelled `[TÀI LIỆU MẪU]` and use fictional data.
- They must pass strict canonical traceability and preflight. Their content (Source Register `SRC-xx`, "Nguồn · Mức" columns, Tier lines) exists partly to exercise those checks.

## Conventions

- **Versioning:**
  - The release is the top `## [x.y.z]` entry in `BA-agent/CHANGELOG.md`.
  - `ba_bundle_audit.py` fails when any file listed in `HEADER_VERSIONED_FILES` has a title or `Phiên bản:` line naming a different MAJOR.MINOR. It also fails when a versioned file mentions a future version.
  - When bumping, update all of those headers. Bump rules are in `BA-agent/CONTRIBUTING.md` §7: a new template or guide is MINOR, a fix is PATCH.
- **New core or required files** must be added to `REQUIRED_FILES` in `scripts/ba_bundle_audit.py` and listed in `DOCUMENT-MAP.md`.
- **One owner file per rule.** `agents/ba-specialist.md` and `workflows/ba-workflow.md` point to `SKILL.md` instead of restating rules; `ba_bundle_audit.py` fails when a rule line of 120+ characters appears in more than one of `SKILL.md`, `agents/`, `workflows/`, `BA-document-rule/core/`.
- **Every file path in backticks in `SKILL.md` must exist.** The bundle audit checks this, resolving each path against `BA-agent/` and several subfolders.
- **Prose in rule files and generated BA documents follows `BA-agent/Anti_ai_writing_rules.md`.** Run `ai_smell_scan.py` on new Markdown.
- **Commit message format** (from `CONTRIBUTING.md`): `[ADD|FIX|UPDATE|REMOVE] short description`.
- **Windows encoding:**
  - The console is cp1252, so scripts that print Vietnamese call `sys.stdout.reconfigure(encoding="utf-8")`.
  - Do not pass Vietnamese text or `'''` blocks through Bash heredocs, which mangles them. Write patch scripts with the Write tool and run them as files.
  - Read and write text with `newline=""` where line endings must be preserved.
