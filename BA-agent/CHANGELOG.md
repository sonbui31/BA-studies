# CHANGELOG — BA-Agent Framework

> Tất cả thay đổi đáng chú ý của framework sẽ được ghi nhận tại đây.
> Format: [Semantic Versioning](https://semver.org/) — MAJOR.MINOR.PATCH

---

## [3.3] — 2026-04-03

### ⭐ Added — "Viết tốt hơn" (Writing Quality Engine)
- **Requirement Decomposition Patterns** — 4 patterns (CRUD/Lifecycle/Actor/Integration) + Decision Table (`writing-guide.md` §10)
- **AC Pattern Library** — 8 loại scenario: Happy/Negative/Boundary/Permission/State/Concurrency/Integration/Data Volume (`writing-guide.md` §11)
- **Conflict Detection Patterns** — 6 loại mâu thuẫn requirement + Resolution Strategies (`writing-guide.md` §12)
- **Assumption Validation Process** — Lifecycle: Identified→Documented→Validated→Confirmed/Rejected (`writing-guide.md` §13)
- **Requirement Quality Rubric** — 5-point scale + 8 Smell Detector patterns (`core/requirement-quality-rubric.md`) [NEW]
- **Writing Examples Library** — Mẫu viết cho Precondition/Exception/BR/NFR/Integration/TC (`references/writing-examples.md`) [NEW]

### ⭐ Added — "Nghĩ sâu hơn" (Advanced Analysis Engine)
- **Decision Analysis Framework** — 4 tools: Weighted Scoring, Pugh Matrix, CBA/ROI, Decision Tree (`core/decision-analysis-framework.md`) [NEW]
- **NFR Discovery Guide** — 7 câu hỏi + 5 kỹ thuật phát hiện NFR specific (`core/nfr-discovery-guide.md`) [NEW]
- **Process Decomposition Guide** — L0→L1→L2→L3 hierarchy + decomposition rules (`core/process-decomposition-guide.md`) [NEW]
- **Communication Packaging** — 4 package types: Executive Summary/Technical Brief/Test Strategy/Quick Start (`references/communication-packaging.md`) [NEW]

### 🔧 Changed
- **Impact Analysis Guide** — Rewrite toàn bộ (39→180+ dòng): Impact Scoring Matrix + Ripple Effect Tree + Regression Mapping + Decision Flowchart
- **As-Is Process template** — Gap Analysis §5 mở rộng: 5 Gap Types + Prioritization Matrix + Closure Tracking
- **ba-specialist.md** — Skills 12→15; thêm Skill 13 (Decision Analysis), 14 (NFR & Quality), 15 (Packaging & Process)
- **DOCUMENT-MAP.md** — Cập nhật core/ (15→19 files), references/ (5→7 files)
- **Version đồng bộ → v3.3** trên ba-specialist, DOCUMENT-MAP

### 📊 Stats
- Files mới: 6 (`requirement-quality-rubric`, `decision-analysis-framework`, `nfr-discovery-guide`, `process-decomposition-guide`, `writing-examples`, `communication-packaging`)
- Files major update: 3 (`writing-guide`, `impact-analysis-guide`, `as-is-process`)
- Total content added: ~2,500 dòng nội dung mới

---

## [3.2] — 2026-04-03

### ⭐ Added
- **Post-Implementation Review (PIR)** template — Cover BABOK KA#6 (Solution Evaluation)
  - Benefits Realization tracking (OKR Planned vs Actual)
  - Lessons Learned (Keep/Improve/Stop)
  - Technical Debt Assessment
  - User Adoption metrics (DAU, Feature Usage Rate)
- **Anti-Patterns Guide** — 15 sai lầm BA thường gặp + cách tránh (`references/anti-patterns.md`)
- **NFR Traceability** — Mở rộng chain: `NFR-ID → NFR-TC-ID` cho Performance/Security test
- **Bi-Directional Tracing** — Trace ngược TC→US→FR→BRQ, phát hiện Stale References
- **Impact Chain** — Khi BRQ thay đổi → auto-flag tất cả downstream items
- **Risk Response Strategies** — 4 chiến lược Accept/Mitigate/Transfer/Avoid + Decision Flowchart
- **LLM Triage Matrix** — Chọn 1/2/4 LLM theo kích thước dự án (S/M/L)
- **Workflow Rollback Path** — Rõ ràng: step fail → quay lại step nào
- **Effort Estimation per Step** — Bảng S/M/L giờ/ngày per workflow step
- **CHANGELOG.md** — File này, theo dõi thay đổi framework
- **CONTRIBUTING.md** — Quy trình đóng góp + Template PR checklist

### 🔧 Changed
- **Version đồng bộ toàn bộ → v3.2** — README, principles, ba-specialist, workflow, evaluation-protocol, DOCUMENT-MAP
- **USER-GUIDE.md** — "11 Skills" → "12 Skills", thêm Skill 12 (AI/ML Feature Spec)
- **Meeting Minutes template** — Thêm Decision Log + Risk Escalation + Open Items tracking
- **Traceability Validator** — v3.0 → v3.2: thêm ORPHAN_NFR + STALE_REF gap types
- **ba-specialist.md** — v3.1 → v3.2: Updated Primary Objective + Skills Suite header

### 🐛 Fixed
- Version mismatch giữa README.md (v2.6.1) và ba-specialist.md (v3.1) — nay đồng bộ v3.2
- USER-GUIDE thiếu Skill 12 (AI/ML Feature Spec) — đã bổ sung

---

## [3.1] — 2026-03-27

### Added
- **AI/ML Feature Specification** template + Pre-Flight (PFC-AI)
- **Narrative Storytelling** cho Pain Points trong BRD (writing-guide.md Section 9)
- **Business Rule Architecture** với Execution Order + Override Matrix
- **Output Severity Design** cho validation/audit systems
- **System Memory Requirements** cho cross-temporal logic
- **UX Metrics** (Time-to-Decision, Scan-to-Action) trong writing-guide.md
- **Configurable Intelligence** Pattern trong AI Feature Spec
- **Auto-Diagram Engine** — Keyword-to-Diagram routing (10 loại)

---

## [3.0] — 2026-03-20

### Added
- **Elicitation Gate** — MANDATORY Step 0, không bỏ qua
- **Pre-Flight Checklist Engine** — Check trước khi sinh document (PFC-BRD, PFC-SRS, PFC-USM, PFC-UAT)
- **Traceability Validator** — Auto-scan cross-doc gaps
- **As-Is Process** — Bắt buộc trước To-Be
- **Screen Inventory + Wireframe** — Mỗi feature ≥ 1 screen
- **Risk Register** — Thay thế Predictive BA lý thuyết bằng actionable register
- **Multi-LLM → Actionable** — Gắn vai trò cụ thể vào từng bước

### Changed
- Evaluation Protocol → Inline Audit (không chỉ cuối cùng)
- Code Traceability Audit → Actionable output format

---

## [2.6.1] — 2026-03-27

### Added
- Auto-Diagram Engine integration (10 types)
- `so_do.md` — Thư viện Mermaid examples

---

## [2.6] — 2026-03-25

### Added
- Customer Intelligence Guide (elicitation + stakeholder psychology)
- Code-to-Requirement Traceability Audit
- Predictive BA Guide (scope creep forecasting)
- Persona Simulation skill
- Impact Analysis guide

---

## [2.5] — 2026-03-20

### Added
- Multi-LLM Orchestration (Gemini 3, Claude 4.6, GPT-5, o4)
- C-S-K-A Evaluation Matrix
- Overlay system (product/outsource/inhouse/startup)

---

## [2.2] — 2026-03-15

### Added
- Initial BA-document-rule framework
- Core principles (BACCM, BABOK, MoSCoW, INVEST, GWT)
- 12 templates (Vision Scope, BRD, SRS, Story Map, etc.)
- Writing Guide
- Quality Checklist (DoR, DoD)
- Glossary
