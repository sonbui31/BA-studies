# HƯỚNG DẪN SỬ DỤNG BỘ KIT BA 3.4 (ADVANCED ANALYSIS & WRITING QUALITY ENGINE)

> **Chào mừng bạn đến với BA-Agent 3.4!**
> Bộ kit "Layered OS" v3.4 — **"Think Deeper, Write Better"**: Advanced Analysis + Requirement Quality Engine.
> Multi-LLM là protocol phân vai reviewer/drafter khuyến nghị; repo này cung cấp tài liệu và runtime scripts, không tự gọi các model thay người dùng.

---

## 🚀 Khởi động nhanh

**Lệnh chính:** `/ba-workflow [tên_dự_án] [mô_tả_ngắn]`

**Quy trình 3.4 (gates + generation + validation):**

```
🚪 GATES (bắt buộc)
  0. Elicitation Gate — Phỏng vấn / Extract insight từ KH
  1. Risk Scan — Phát hiện rủi ro + sinh Risk Register
  2. Customer Intelligence — Deep probing, hidden needs
  2.5 As-Is Process — Document quy trình hiện tại + Gap Analysis

📝 GENERATION (có Pre-Flight)
  3. Template Selection — Chọn overlay + plan metrics
  3.5 Industry Preparation — Gov/Healthcare/Fintech templates nếu cần
  4. Screen Inventory — Liệt kê screens + Navigation Map
  5. Document + Diagram + Wireframe — PRE-FLIGHT trước mỗi doc
     ↳ [NEW] Quality Engine: Decomposition + NFR Discovery + Quality Rubric

✅ VALIDATION (multi-layer)
  6. AI Quality Gate — Inline audit (Rubric + Smells + Conflicts)
  6.5 Pre-Flight Verify — Re-check sau khi viết
  6.6 Sequential Index Validation — Heading/ID numbering không nhảy/lặp
  6.7 Traceability Validation — BRQ→FR→US→TC chain check (incl. NFR→TC)
  7. Impact + Persona Sim + Decision Analysis — Scan, stress-test, evaluate
  7.5 [NEW] Communication Packaging — Đóng gói theo audience (CEO/Dev)
  7.6 [NEW] Operational/Data/Adoption Readiness — RBAC, RAID, Ops, Data Governance
  8. Final Report — Scorecard + Risk + Traceability + Diagrams
```


**⚡ Rollback path (nếu step fail):**

```
Step 6.7 FAIL (traceability gaps)  → Quay lại Step 5 (bổ sung docs thiếu)
Step 6.5 FAIL (pre-flight items)   → Quay lại Step 5 (sửa inline)
Step 6 FAIL (C-S-K-A < 7.5)       → Quay lại Step 5 (rewrite sections)
Step 5 FAIL (pre-flight trước doc) → Quay lại Step 0/2 (bổ sung input)
```

---

## 🆕 Có gì mới trong v3.4?

| Feature | v3.3 | v3.4 |
|---------|------|------|
| **Requirement Decomposition** | BA tự tách ad-hoc | ⭐ 4 patterns: CRUD/Lifecycle/Actor/Integration |
| **AC Coverage** | 2 scenarios (Happy + Unhappy) | ⭐ 8 loại (thêm Boundary, Permission, Concurrency, Data Volume...) |
| **Requirement Quality** | Chấm điểm mức document | ⭐ Chấm mức **từng câu** (5-point rubric + 8 Smell Detector) |
| **Conflict Detection** | Phát hiện thủ công | ⭐ 6 patterns auto-scan: Contradictory, Overlapping, Boundary... |
| **Decision Analysis** | Không có | ⭐ 4 tools: Weighted Scoring, Pugh, CBA, Decision Tree |
| **NFR Discovery** | Fill template sẵn | ⭐ 7 câu hỏi + 5 kỹ thuật phát hiện NFR specific |
| **Process Decomposition** | 1 level swimlane | ⭐ L0→L1→L2→L3 hierarchy + rules khi nào dừng |
| **Impact Analysis** | 39 dòng basic | ⭐ 180+ dòng: Scoring Matrix + Ripple Effect + Regression Map |
| **Communication Packaging** | 1 bản cho tất cả | ⭐ 4 package types: CEO/Dev/QC/End-User |
| **Assumption Validation** | Ghi nhận, không validate | ⭐ Lifecycle + Validation Methods + Register |
| **Writing Examples** | Không có | ⭐ Mẫu viết: Precondition/Exception/BR/NFR/Integration/TC |

---

## 🤖 Các kỹ năng (21 Skills)

> Cột LLM bên dưới là vai trò/model khuyến nghị khi người vận hành có môi trường multi-model; nếu không, dùng cùng một assistant và chạy scripts validation ở cuối.

| Kỹ năng | Lệnh tiêu biểu | Kết quả | LLM |
|---|---|---|---|
| **Elicitation Gate** | `@ba-specialist phỏng vấn KH cho dự án X` | Interview questions + Insight Cards | Claude 4.6 |
| **Risk Management** | `@ba-specialist tạo risk register dựa trên BRD` | Risk Register + Heatmap + Response Strategies | o4 |
| **As-Is Documentation** | `@ba-specialist document As-Is cho quy trình [X]` | As-Is Swimlane + Gap Analysis | — |
| **Pre-Flight Engine** | (Tự động chạy trước mỗi doc) | Checklist PASS/FAIL | — |
| **Traceability Validator** | `@ba-specialist kiểm tra truy vết dự án` | Full Chain Report + Gaps (incl. NFR→TC) | Gemini 3 |
| **Screen Inventory** | `@ba-specialist liệt kê screens cho dự án X` | Screen list + Nav map + Wireframes | — |
| **Auto-Diagram Engine** | `@ba-specialist vẽ [loại] cho [quy trình]` | Mermaid diagram tự động | — |
| **Code-to-Req Audit** | `@ba-specialist đối soát SRS với code` | Audit Report + Match/Mismatch | Claude + o4 |
| **Impact Analysis** | `@ba-specialist phân tích ảnh hưởng thay đổi X` | Dependency scan | Gemini 3 |
| **Persona Simulation** | `@ba-specialist đóng vai CFO phản biện` | Stress-test report | o4 |
| **AI Prototyping** | `@ba-specialist tạo wireframe cho feature X` | StitchMCP wireframe | — |
| **AI/ML Feature Spec** | `@ba-specialist tạo AI spec cho feature [X]` | AI Behavior + Confidence Matrix + Fallbacks | Claude + o4 |
| **Decision Analysis** ⭐ | `@ba-specialist phân tích quyết định: A vs B` | Weighted Scoring / CBA / Decision Tree | — |
| **NFR Discovery & Quality** ⭐ | `@ba-specialist khám phá NFR + chấm rubric` | NFR specifics + Quality Report (5-point) | o4 |
| **Communication Packaging** ⭐ | `@ba-specialist tạo Executive Summary từ BRD` | 4 package types cho 4 audiences | Claude 4.6 |
| **Business Case & Investment** ⭐ | `@ba-specialist tạo Business Case cho dự án X` | Options, ROI/NPV, feasibility, Go/No-Go | — |
| **RAID/RBAC Governance** ⭐ | `@ba-specialist tạo RAID Log và RBAC Matrix` | RAID owner/escalation + Role/Permission/Data Scope | — |
| **Reporting/Analytics/Data Governance** ⭐ | `@ba-specialist tạo Reporting Spec và Data Governance Plan` | KPI, event taxonomy, CDE, DQ rules, retention | — |
| **Research & Product Discovery** ⭐ | `@ba-specialist lập User Research Plan` | Research objective, script, participant plan, synthesis | — |
| **Test/BPMN/Ops Readiness** ⭐ | `@ba-specialist tạo Test Strategy và Operational Readiness` | SIT/regression/NFR coverage, BPMN, go-live checklist | — |
| **Curated Template Application** ⭐ | `@ba-specialist tạo BRD/SRS theo curated template` | BRD/SRS/User Story/AC **CHỈ DÙNG DUY NHẤT** 4 template trong `Curated templates/` (`01-BRD`, `02-SRS`, `03-User-Story`, `04-AC`) | — |

---

## 📂 Cấu trúc thư mục

```
BA-agent/
├── agents/ba-specialist.md     ← Agent persona & 21 Skills (v3.4)
├── workflows/ba-workflow.md    ← Slash command logic với gates + rollback
├── Curated templates/          ← NGUỒN DUY NHẤT cho BRD/SRS/User Story/AC
│   ├── 01-BRD-Template.md      ← Template BRD chuẩn 11 phần
│   ├── 02-SRS-Template.md      ← Template SRS chuẩn 9 phần kỹ thuật
│   ├── 03-User-Story-Template.md ← Template User Story chuẩn INVEST
│   ├── 04-Acceptance-Criteria-Template.md ← Template AC chuẩn 4 Scenarios
│   ├── Template-tai-lieu-BA-*.docx ← File gốc Word (reference)
│   └── SRS.pdf                 ← Reference SRS chuẩn IEEE
├── BA-document-rule/           ← "Hệ điều hành" (Core + Templates phụ trợ + Overlays)
│   ├── core/                   ← 20 files: Principles, Guides, Pre-Flight, Validator...
│   │   ├── pre-flight-checklist.md    ⭐ Check trước khi viết
│   │   ├── traceability-validator.md  ⭐ Auto-scan gaps (incl. NFR)
│   │   ├── screen-inventory-guide.md  ⭐ Screen & Wireframe guide
│   │   ├── requirement-quality-rubric.md ⭐ 5-point rubric + 8 Smells (v3.3)
│   │   ├── decision-analysis-framework.md ⭐ Weighted Scoring, Pugh, CBA (v3.3)
│   │   ├── nfr-discovery-guide.md     ⭐ 7 câu hỏi + 5 kỹ thuật NFR (v3.3)
│   │   ├── process-decomposition-guide.md ⭐ L0→L3 hierarchy (v3.3)
│   │   └── ... (13 existing files)
│   ├── templates/              ← 28 templates generic
│   │   ├── post-implementation-review.md  ⭐ NEW v3.2: PIR + Benefits Realization
│   │   ├── as-is-process.md           ⭐ As-Is documentation
│   │   ├── risk-register.md           ⭐ Risk Register + Response Strategies
│   │   ├── data-migration-plan.md     ⭐ Migration with rollback
│   │   ├── screen-inventory.md        ⭐ Screen tracking
│   │   ├── business-case.md           ⭐ ROI, options, Go/No-Go
│   │   ├── raid-log.md                ⭐ Risks, Assumptions, Issues, Dependencies
│   │   ├── rbac-matrix.md             ⭐ Role, Permission, Data Scope
│   │   ├── reporting-specification.md ⭐ KPI/report/dashboard spec
│   │   ├── operational-readiness-checklist.md ⭐ Go-live readiness
│   │   ├── test-strategy.md           ⭐ SIT/UAT/regression/NFR strategy
│   │   ├── user-research-plan.md      ⭐ Discovery and research planning
│   │   ├── product-analytics-spec.md  ⭐ Funnel and event taxonomy
│   │   ├── bpmn-modeling-standard.md  ⭐ BPMN/process modeling rules
│   │   ├── data-governance-plan.md    ⭐ Data ownership, quality, retention
│   │   ├── industry/                  ⭐ 9 templates ngành (Gov/HC/FT) — v3.3.1
│   │   └── ... (generic templates khác)
│   ├── overlays/               ← Config theo loại dự án (7 loại: 4 generic + 3 industry)
│   └── references/             ← RACI, Estimation, Elicitation, Anti-Patterns (7 files)
│       ├── anti-patterns.md           ⭐ Top 15 sai lầm BA (v3.2)
│       ├── writing-examples.md        ⭐ Mẫu viết: Precondition/Exception/BR (v3.3)
│       └── communication-packaging.md ⭐ 4 package types CEO/Dev/QC (v3.3)
├── BA-Documents-Product/       ← 12 files mẫu cho Sản phẩm
├── BA-Documents-Outsource/     ← 13 files mẫu cho Thuê ngoài
├── DOCUMENT-MAP.md             ← Bản đồ chỉ đường cho mọi file
├── USER-GUIDE.md               ← Hướng dẫn sử dụng (file này)
├── CHANGELOG.md                ← Lịch sử thay đổi
├── CONTRIBUTING.md             ← ⭐ NEW v3.2: Quy trình đóng góp
└── so_do.md                    ← Thư viện Mermaid (10 loại sơ đồ)
```

---

## 📈 5 Nguyên tắc cốt lõi v3.4

1. **Right First Time** — Pre-Flight + Inline Audit = giảm iterations từ 4+ → ≤ 2
2. **Facts, not Theory** — Risk Register từ patterns thực tế, không predict từ "hàng ngàn mẫu"
3. **Visual First** — Screen Inventory + Wireframe TRƯỚC khi code. Diagram tốt hơn 1000 chữ
4. **Reviewer-role Precision** — phân vai drafter/reviewer theo loại việc; chỉ dùng nhiều LLM khi workflow thực tế có công cụ/model tương ứng
5. **Complete Traceability** — BRQ→FR→US→TC + NFR→NFR-TC — không gì bị orphan

---

## 🛠 Tùy chỉnh

- **Sửa nguyên tắc:** `BA-document-rule/core/principles.md`
- **Sửa template phụ trợ (Risk, RBAC, RAID, v.v.):** `BA-document-rule/templates/*.md`
- **Sửa template cốt lõi (BRD/SRS/Story/AC):** `Curated templates/01-BRD-Template.md`, `02-SRS-Template.md`, `03-User-Story-Template.md`, `04-Acceptance-Criteria-Template.md` — **NGUỒN DUY NHẤT** cho 4 tài liệu cốt lõi
- **Sửa Pre-Flight items:** `BA-document-rule/core/pre-flight-checklist.md`
- **Sửa traceability rules:** `BA-document-rule/core/traceability-validator.md`
- **Thêm overlay mới:** Tạo folder trong `BA-document-rule/overlays/`
- **Xem anti-patterns:** `BA-document-rule/references/anti-patterns.md`
- **Xem changelog:** `CHANGELOG.md`

---

## ✅ Runtime validation scripts

Chạy các script này trước khi kết luận bundle đã đạt chất lượng:

```powershell
python .\scripts\preflight_check.py <project-folder>
python .\scripts\quality_rubric.py <project-folder-or-file>
python .\scripts\traceability_scan.py <project-folder> --scheme legacy
python .\scripts\traceability_scan.py <project-folder> --scheme canonical --strict
python .\scripts\reindex_markdown.py <project-folder>
```

**Legacy bundle** dùng ID như `BRD-101 / FR-101 / US-001 / UAT-001`. Với dạng này, chạy `--scheme legacy` là mặc định an toàn. Chỉ thêm `--strict` nếu tài liệu cũng có Feature ID và mapping Feature.

**Canonical bundle** dùng ID như `BRQ-01 / FR-MOD-001 / US-MOD-001 / TC-MOD-001`. Với dạng này, chạy `--scheme canonical --strict`; strict mode yêu cầu chain đầy đủ `BRQ -> FR -> Feature -> US -> TC`.

Nếu `--strict` báo `BROKEN_CHAIN`, có hai hướng xử lý:
- Bổ sung Feature ID và mapping vào BRD/SRS/Story/UAT nếu dự án yêu cầu traceability đầy đủ.
- Bỏ `--strict` nếu đang kiểm tra legacy/outsource bundle mà Feature traceability được chủ đích loại khỏi phạm vi.

---

## 🎯 LLM Triage Matrix — Khi nào dùng bao nhiêu LLM?

| Kích thước dự án | Timeline | Số LLM | Vai trò |
|---|---|:---:|---|
| **S** (< 3 sprints, MVP) | < 2 tháng | **1** | Gemini 3 hoặc Claude — đa năng |
| **M** (3-8 sprints, standard) | 2-5 tháng | **2** | Primary (Gemini/Claude) + Reviewer (o4) |
| **L** (> 8 sprints, regulated) | > 5 tháng | **4** | Full orchestration: Claude + o4 + Gemini + GPT-5 |

> **Quy tắc:** Không phải dự án nào cũng cần 4 LLM. Chọn fit-for-purpose.
