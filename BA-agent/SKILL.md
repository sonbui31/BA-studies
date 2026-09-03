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
| Classify project before recommending documents | `BA-document-rule/core/project-classification-gate.md` |
| Use the distilled BA knowledge base | `BA-document-rule/references/ba-knowledge-base.md` |
| Retrieve specific BA knowledge cards | `BA-document-rule/references/ba-knowledge-cards.json` via `scripts/knowledge_search.py` |
| Search the built self-contained BA source index | `knowledge-index/chunks.jsonl` via hybrid search in `scripts/knowledge_index_search.py` |
| Build/search optional semantic embeddings | `scripts/build_semantic_index.py`, `scripts/semantic_index_search.py` |
| Check source/rebuild metadata | `knowledge-source/source-manifest.json` |
| Build investment/adoption/data/reporting artifacts | `BA-document-rule/templates/business-case.md`, `raid-log.md`, `rbac-matrix.md`, `reporting-specification.md`, `operational-readiness-checklist.md`, `test-strategy.md`, `data-governance-plan.md` |
| Run product discovery and analytics planning | `BA-document-rule/templates/user-research-plan.md`, `product-analytics-spec.md` |
| Standardize process modeling | `BA-document-rule/templates/bpmn-modeling-standard.md`, `BA-document-rule/core/process-decomposition-guide.md` |
| Run document gates before drafting | `BA-document-rule/core/pre-flight-checklist.md` |
| Check traceability and numbering | `BA-document-rule/core/traceability-validator.md` |
| Improve requirement quality and NFRs | `BA-document-rule/core/requirement-quality-rubric.md`, `BA-document-rule/core/nfr-discovery-guide.md` |
| Evaluate scenario coverage in a BA answer/artifact | `scripts/ba_response_eval.py` |
| Run golden BA behavior checks | `scripts/eval_golden_cases.py` |
| Resolve stakeholder conflicts before sign-off | `BA-document-rule/core/stakeholder-conflict-resolution.md`, `BA-document-rule/core/persona-simulation.md` |
| Select domain-specific overlays | Choose one actual overlay config under `BA-document-rule/overlays/` |
| Generate BRD/SRS/User Story/AC with curated layout and examples | `Curated templates/Template-tai-lieu-BA-BRD-SRS-UserStory-AC.docx`; use alongside `BA-document-rule/templates/brd.md`, `srs.md`, and `user-story-map.md` |
| Generate or review full SRS structure | `Curated templates/SRS.pdf`; use as SRS reference alongside `BA-document-rule/templates/srs.md` |
| Generate from markdown templates | `BA-document-rule/templates/` and `BA-document-rule/templates/industry/` |
| Generate Vietnamese Docusaurus user manual for an app | `user-manual-generator/SKILL.md`; references in `user-manual-generator/references/`; audit with `user-manual-generator/scripts/audit-docs.js` |

## Execution rules

1. Start from `workflows/ba-workflow.md` unless the user asks for one narrow artifact only.
2. Before recommending a document set or drafting anything broad, run `BA-document-rule/core/project-classification-gate.md` and state the classification assumptions.
3. If the project is a new product, platform, SaaS/app, commercializable MVP, or B2B offering, Product Vision Document is mandatory and must be listed before Project Charter and BRD. Do not treat BRD or Project Charter as a substitute for Product Vision.
4. Run elicitation and As-Is gates before writing BRD or SRS, unless the user explicitly confirms a greenfield project.
5. Pick one overlay before drafting:
   `inhouse`, `outsource`, `product`, `startup-mvp`, `government`, `healthcare`, or `fintech`.
6. Before drafting BRD, SRS, User Story Map, or Acceptance Criteria, consult the matching curated template first:
   - `Curated templates/Template-tai-lieu-BA-BRD-SRS-UserStory-AC.docx` for structure, wording style, examples, and expected level of detail.
   - `Curated templates/SRS.pdf` when generating/reviewing SRS completeness.
   Then normalize the final output into repository markdown conventions and the selected overlay.
7. Add supporting artifacts when risk signals appear:
   - Investment or Go/No-Go decision → `business-case.md`.
   - Open assumptions/issues/dependencies → `raid-log.md`.
   - Role-sensitive access → `rbac-matrix.md`.
   - Dashboards/KPIs/exports → `reporting-specification.md`.
   - Go-live/support/training → `operational-readiness-checklist.md`.
   - SIT/regression/NFR coverage → `test-strategy.md`.
   - Data ownership/retention/quality → `data-governance-plan.md`.
   - Product discovery or event tracking → `user-research-plan.md`, `product-analytics-spec.md`.
   - Formal process notation → `bpmn-modeling-standard.md`.
8. Keep traceability explicit:
   `BRQ-* -> FR-* -> Feature -> US-* -> TC-*`.
9. Generate Vietnamese-facing BA content in **Vietnamese with full diacritics**. Do not write body text as "tieng Viet khong dau". Keep ASCII/no-diacritic text only for filenames, IDs, code identifiers, API paths, database fields, commands, URLs, and source-controlled technical tokens.
10. If stakeholders disagree on scope, controls, workflow, budget, or ownership, stop drafting and run the conflict-resolution protocol before freezing BRD/SRS/UAT wording.
11. Use the bundle validator before claiming the skill package is internally consistent.
12. When the user asks to apply general BA knowledge gathered from the old `BA/` folder, read `BA-document-rule/references/ba-knowledge-base.md`; it is self-contained and must not require the original `BA/` folder to exist.
13. Before drafting a complex artifact, run or consult `scripts/knowledge_search.py "<topic>"` to retrieve the closest BA knowledge cards, especially for product vision, UAT/RTM, AI/ML, data/API/reporting, process modeling, and regulated domains.
14. If deeper source-derived recall is needed, search `knowledge-index/chunks.jsonl` with `scripts/knowledge_index_search.py "<query>"`; this index is self-contained and must not read the original `BA/` folder at runtime.

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
python .\scripts\ba_response_eval.py <file-or-> --scenario outsource --format markdown
python .\scripts\eval_golden_cases.py --format markdown
python .\scripts\knowledge_search.py "UAT traceability" --format markdown
python .\scripts\knowledge_index_search.py "BRD stakeholder assumptions" --format markdown
python .\scripts\knowledge_index_search.py "nghiệm thu nhà thầu" --mode hybrid --format markdown
python .\scripts\knowledge_index_search.py "UAT sign-off evidence" --mode vector --format json
python .\scripts\build_semantic_index.py --chunks .\knowledge-index\chunks.jsonl --output .\knowledge-index\semantic
python .\scripts\semantic_index_search.py "how to control vendor acceptance sign-off" --format markdown
```

Rules:
- Run `preflight_check.py` before drafting or approving BRD, SRS, Story Map, and UAT artifacts.
- Run `quality_rubric.py` on SRS or BRD files before claiming requirement quality is acceptable.
- Run `traceability_scan.py` after drafting BRD, SRS, Story Map, or UAT artifacts.
- Run `ba_response_eval.py` for important outsource, product, or fintech outputs before claiming the answer covers the scenario-specific BA controls.
- Run `eval_golden_cases.py` before releases to catch regressions in BA control coverage.
- Use `reindex_markdown.py` in dry-run mode first.
- Only use `--apply` after reviewing the proposed renumbering, especially on outsource projects with signed baselines.
- Use `--scheme legacy` for bundles using `BRD-101 / FR-101 / US-001 / UAT-001`; do not add `--strict` unless the bundle also defines Feature links.
- Use `--scheme canonical --strict` for bundles using `BRQ-01 / FR-MOD-001 / US-MOD-001 / TC-MOD-001`; strict mode requires the full `BRQ-* -> FR-* -> Feature -> US-* -> TC-*` chain.
- If `--strict` reports `BROKEN_CHAIN`, either add Feature IDs/links or rerun without `--strict` for legacy bundles where Feature traceability is intentionally out of scope.
- Use `knowledge_search.py` as the first retrieval layer for self-contained BA knowledge; do not require the old source folder for normal BA work.
- Use `knowledge_index_search.py` in default hybrid mode for deeper recall. It combines lexical BM25-style scoring, query expansion for BA Vietnamese/English terms, vector-style cosine scoring, and source citation fields.
- Use `--mode bm25` only when exact keyword matching is preferred; use `--mode vector` when the query is conceptual or phrased differently from the source documents.
- Use `build_semantic_index.py` only when optional dependencies in `requirements-semantic-index.txt` are installed. `semantic_index_search.py` uses real sentence-transformer embeddings and FAISS when available; it is an enhancement layer, not required for normal runtime.
- Use `build_knowledge_index.py --source <BA-folder>` only when rebuilding the self-contained index from source documents. Runtime BA work should use `knowledge_index_search.py`, not the old source folder.
- Rebuilding the PDF full-text index requires `requirements-knowledge-index.txt`; PDF chunks rebuilt through `pypdf` include `page_start/page_end` citation fields. Runtime search over an already-built `knowledge-index/` uses only the Python standard library.
