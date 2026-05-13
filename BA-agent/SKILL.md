---
name: ba-agent
description: Business analysis skill for elicitation, BRD/SRS generation, user story mapping, UAT planning, traceability validation, impact analysis, and regulated-domain BA work. Use when Codex needs to create, review, restructure, or audit BA artifacts for product, in-house, outsource, government, healthcare, or fintech projects.
---

# BA Agent

Use this skill as the entrypoint for BA work in this repository.

## Read selectively

Read only the files needed for the task.

| Need | Read |
|---|---|
| Route the overall BA process | `workflows/ba-workflow.md` |
| Apply the BA persona and execution rules | `agents/ba-specialist.md` |
| Understand repository structure | `BA-document-rule/README.md` |
| Pick required artifacts by project type | `DOCUMENT-MAP.md` |
| Build investment/adoption/data/reporting artifacts | `BA-document-rule/templates/business-case.md`, `raid-log.md`, `rbac-matrix.md`, `reporting-specification.md`, `operational-readiness-checklist.md`, `test-strategy.md`, `data-governance-plan.md` |
| Run product discovery and analytics planning | `BA-document-rule/templates/user-research-plan.md`, `product-analytics-spec.md` |
| Standardize process modeling | `BA-document-rule/templates/bpmn-modeling-standard.md`, `BA-document-rule/core/process-decomposition-guide.md` |
| Run document gates before drafting | `BA-document-rule/core/pre-flight-checklist.md` |
| Check traceability and numbering | `BA-document-rule/core/traceability-validator.md` |
| Improve requirement quality and NFRs | `BA-document-rule/core/requirement-quality-rubric.md`, `BA-document-rule/core/nfr-discovery-guide.md` |
| Resolve stakeholder conflicts before sign-off | `BA-document-rule/core/stakeholder-conflict-resolution.md`, `BA-document-rule/core/persona-simulation.md` |
| Select domain-specific overlays | Choose one actual overlay config under `BA-document-rule/overlays/` |
| Generate from templates | `BA-document-rule/templates/` and `BA-document-rule/templates/industry/` |

## Execution rules

1. Start from `workflows/ba-workflow.md` unless the user asks for one narrow artifact only.
2. Run elicitation and As-Is gates before writing BRD or SRS, unless the user explicitly confirms a greenfield project.
3. Pick one overlay before drafting:
   `inhouse`, `outsource`, `product`, `startup-mvp`, `government`, `healthcare`, or `fintech`.
4. Add supporting artifacts when risk signals appear:
   - Investment or Go/No-Go decision → `business-case.md`.
   - Open assumptions/issues/dependencies → `raid-log.md`.
   - Role-sensitive access → `rbac-matrix.md`.
   - Dashboards/KPIs/exports → `reporting-specification.md`.
   - Go-live/support/training → `operational-readiness-checklist.md`.
   - SIT/regression/NFR coverage → `test-strategy.md`.
   - Data ownership/retention/quality → `data-governance-plan.md`.
   - Product discovery or event tracking → `user-research-plan.md`, `product-analytics-spec.md`.
   - Formal process notation → `bpmn-modeling-standard.md`.
5. Keep traceability explicit:
   `BRQ-* -> FR-* -> Feature -> US-* -> TC-*`.
6. If stakeholders disagree on scope, controls, workflow, budget, or ownership, stop drafting and run the conflict-resolution protocol before freezing BRD/SRS/UAT wording.
7. Use the bundle validator before claiming the skill package is internally consistent.

## Validation

Run:

```powershell
python .\scripts\ba_bundle_audit.py
```

The validator checks release-version alignment, missing skill entry files, future-version drift, and legacy story ID examples in the main bundle docs.

## Runtime automation

Use the scripts before doing manual traceability cleanup.

```powershell
python .\scripts\preflight_check.py <project-folder>
python .\scripts\quality_rubric.py <project-folder-or-file>
python .\scripts\traceability_scan.py <project-folder>
python .\scripts\traceability_scan.py <project-folder> --output-md traceability-report.md --output-json traceability-report.json
python .\scripts\traceability_scan.py <project-folder> --scheme legacy
python .\scripts\traceability_scan.py <project-folder> --scheme canonical --strict
python .\scripts\reindex_markdown.py <project-folder>
python .\scripts\reindex_markdown.py <project-folder> --apply
python .\scripts\reindex_markdown.py <project-folder> --include-baseline --apply
```

Rules:
- Run `preflight_check.py` before drafting or approving BRD, SRS, Story Map, and UAT artifacts.
- Run `quality_rubric.py` on SRS or BRD files before claiming requirement quality is acceptable.
- Run `traceability_scan.py` after drafting BRD, SRS, Story Map, or UAT artifacts.
- Use `reindex_markdown.py` in dry-run mode first.
- Only use `--apply` after reviewing the proposed renumbering, especially on outsource projects with signed baselines.
- Use `--scheme legacy` for bundles using `BRD-101 / FR-101 / US-001 / UAT-001`.
- Use `--scheme canonical --strict` for bundles using `BRQ-01 / FR-MOD-001 / US-MOD-001 / TC-MOD-001`.
