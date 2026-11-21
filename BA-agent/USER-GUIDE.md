# HƯỚNG DẪN SỬ DỤNG BỘ KIT BA 3.10 (ADVANCED ANALYSIS & WRITING QUALITY ENGINE)

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
     ↳ [NEW] Quality Engine: Decomposition + NFR Discovery + Quality Rubric + Anti-AI Writing Rules

✅ VALIDATION (multi-layer)
  6. AI Quality Gate — Inline audit (Rubric + Smells + Conflicts + Anti-AI Checklist)
  6.5 Pre-Flight Verify — Re-check sau khi viết
  6.6 Sequential Index Validation — Heading/ID numbering không nhảy/lặp
  6.7 Traceability Validation — BRQ→FR/NFR→Feature→US→AC/TC chain check
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

## 🆕 Có gì mới trong v3.10?

- **Quy trình nghiệp vụ vẽ bằng BPMN 2.0 thật** (định dạng bpmn.io): pool, lane, loại task, cổng loại trừ và song song, sự kiện hẹn giờ gắn biên. File `.bpmn` mở và sửa được bằng bpmn.io, Camunda Modeler; nhập được vào Bizagi, Signavio. Xem `so_do.md` mục 4.
- **`bpmn_tool.py`:** viết bản mô tả JSON ngắn (lane, bước, luồng), script sinh `.bpmn` có bố cục, kiểm tra lỗi mô hình (luồng cụt, nhánh thiếu điều kiện, phần tử lơ lửng) và vẽ ảnh PNG/SVG bằng bpmn-js.
- **Tài liệu mẫu:** 13 sơ đồ BPMN: bộ Outsource 7 (tổng quan vòng đời tài sản; điều chuyển, kiểm kê, bảo trì), bộ Product 5 (BRD, vòng phản hồi, gộp feedback trùng, cập nhật trạng thái), 1 ví dụ trong `so_do.md`; ô viền đỏ đánh dấu bước gây điểm đau trong As-Is. User flow của một người dùng trên màn hình vẫn vẽ bằng Mermaid.
- **Xuất Word:** ảnh sơ đồ rộng tự nằm trên trang ngang riêng để chữ còn đọc được.
- Mermaid BPMN-lite chỉ còn dùng để phác thảo trong lúc trao đổi.

## Có gì mới trong v3.9

- **Một chuẩn vẽ sơ đồ duy nhất:** `so_do.md` (viết lại). Khối khai báo giao diện chung thay theme mặc định của Mermaid; mười quy tắc; BPMN-lite cho quy trình (sự kiện bắt đầu/kết thúc, cổng loại trừ và song song, vai trò theo màu); khi nào phải vẽ BPMN 2.0 thật. Sửa các ví dụ sai nghiệp vụ cũ (Sequence thiếu `else`, State hoàn tiền về sai trạng thái).
- **Tài liệu mẫu có sơ đồ quy trình thật:** `BA-Documents-Outsource/04-Process-Flow.md` (điều chuyển, kiểm kê, bảo trì; As-Is và To-Be), BRD và User Flow của bộ Product chuyển từ sơ đồ ký tự sang Mermaid.
- **`diagram_check.py`:** bắt sơ đồ không vẽ được, nhánh không nhãn, `<<include>>` hiện thành `<>`; `--fix` sửa phần máy móc; `--render` vẽ thử bằng mermaid-cli.
- **Xuất Word có hình:** `md_to_docx.py` vẽ sơ đồ Mermaid thành ảnh khi có mermaid-cli.
- **Preflight `Process Diagram`:** BRD phải dựa trên sơ đồ quy trình vẽ được (Hard Gate 1).

## Có gì mới trong v3.8

- **Scripts đọc đúng tài liệu thật.** Chạy lên ba bộ tài liệu thật (QLTS, vClassio) cho thấy phần lớn cảnh báo của bản 3.7 là sai: ma trận có cột tên, ID con `FR-TEA-003.1`, liên kết viết ở dòng dưới định nghĩa, bảng nhóm, bảng thuộc tính. Đã sửa 15 mẫu viết; bản ghi: `tests/golden/real_project_tool_run_2026-11-21.md`.
- **Dự án đang dở giữ ID riêng:** khai báo định dạng ID, vai trò file và tác nhân trong `ba-scheme.json`, chạy `traceability_scan.py --scheme project`. Muốn chuyển sang ID canonical: `id_migrate.py` (có bảng đổi ID).
- **Bản Word cho khách và nhận góp ý:** `md_to_docx.py --template <mẫu của khách>` xuất Word theo mẫu; `docx_feedback.py` gom Track Changes và comment của khách về đúng ID.
- **Việc người phải làm (H1–H6) và Hard Gate 8:** người chịu trách nhiệm tài liệu, xác nhận bằng văn bản cho nhận định trọng yếu, review độc lập theo Tier, chỉ người ký mới chuyển tài liệu sang Baseline. Preflight có check `Human Sign-off`. Xem `BA-document-rule/core/human-accountability.md`.
- **Mỗi luật một file chủ:** agent và workflow trỏ về `SKILL.md` thay vì chép lại; `ba_bundle_audit.py` báo lỗi khi một câu luật bị chép sang file khác.
- **Giao thức chạy thử trên dự án thật:** `BA-document-rule/core/pilot-protocol.md`.

## Có gì mới trong v3.7

- **Phân loại yêu cầu (lối L0–L4):** câu hỏi nhanh, review hay viết một artifact lẻ được xử lý ngay; chỉ dự án/epic mới mới chạy đủ 6 bước và Hard Gate. Xem `BA-document-rule/core/intake-triage.md`.
- **Nguồn yêu cầu và Hard Gate 7:** mỗi Fact ghi nguồn và mức E1–E4; thông tin từ người chat ghi `SRC-CHAT`; không chốt khi nhận định trọng yếu chỉ có nguồn gián tiếp. BRD Tier 2+ có Sổ nguồn và kế hoạch elicitation; preflight có check `Evidence Sources`. Xem `BA-document-rule/core/evidence-source-gate.md`.
- **Chốt theo lát cắt:** chốt nền chung của BRD rồi đưa từng luồng/module (đủ BRQ → FR → US → AC) qua gate độc lập, theo dõi trong Sổ lát cắt. Xem `BA-document-rule/core/slice-baselining.md`.
- **Kiểm tra theo Tier:** Tier 1 chỉ chạy checklist Anti-AI, preflight, ai_smell_scan; Tier 2–3 thêm rubric, traceability, review vai trò (`rigor-tiers.md` mục 2).

## Có gì mới trong v3.6

- **Script audit tin cậy hơn:** `traceability_scan.py` không còn PASS giả (đọc định nghĩa ở heading, báo thư mục rỗng, báo ID sai scheme ở strict, kiểm tra từng FR); `reindex_markdown.py` không còn sửa hỏng tài liệu đã ký, heading kiểu `## 2024 Roadmap` hay dãy số đang đúng. Chi tiết từng script: `scripts/README.md`.
- **Truy vết N:M:** mỗi FR cần ≥ 1 US, mỗi US cần ≥ 1 AC/TC; ánh xạ 1:1 chỉ kiểm khi bật `--one-to-one`. Feature chỉ bắt buộc khi bộ tài liệu có Feature Map.
- **Review vai trò theo Tier:** Tier 1 gồm R-BA và vai trò theo loại tài liệu, Tier 2 thêm 6 vai trò, Tier 3 đủ 21.
- **Tài liệu mẫu chuyển sang scheme canonical** và đạt `--scheme canonical --strict`.
- **SKILL.md gọn hơn:** quy chuẩn từng loại tài liệu chuyển sang `BA-document-rule/core/document-rulebook.md`.

## Có gì mới trong v3.4

| Feature | v3.3 | v3.4 |
|---------|------|------|
| **Requirement Decomposition** | BA tự tách ad-hoc | ⭐ 4 patterns: CRUD/Lifecycle/Actor/Integration |
| **AC Coverage** | 2 scenarios (Happy + Unhappy) | ⭐ 8 loại (thêm Boundary, Permission, Concurrency, Data Volume...) |
| **Requirement Quality** | Chấm điểm mức document | ⭐ Chấm mức **từng câu** (5-point rubric + 8 Smell Detector) |
| **Conflict Detection** | Phát hiện thủ công | ⭐ 6 mẫu rà mâu thuẫn (Contradictory, Overlapping, Boundary...) trong `writing-guide.md` §12; rà bằng đọc hiểu |
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
| **Review theo vai trò** | `@ba-specialist review BRD bằng vai trò sếp, nhân viên và người dùng ít thời gian` | Báo cáo phát hiện theo ID, bằng chứng, tác động và người cần quyết định; có thể thêm CFO, QA, Ops, bảo mật... theo rủi ro | — |
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
│   ├── 01-BRD-Template.md      ← Template BRD chuẩn 14 phần (BRQ, RACI, BR→FR)
│   ├── 02-SRS-Template.md      ← Template SRS chuẩn 11 phần (FR-CC, External Interface)
│   ├── 03-User-Story-Template.md ← Template US (Sprint Roadmap, SP, BR)
│   ├── 04-Acceptance-Criteria-Template.md ← Template AC 4+4 Scenarios + Traceability
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
├── Anti_ai_writing_rules.md      ← ⭐ Bộ quy tắc viết văn chống "mùi AI" (27 Điều)
└── so_do.md                    ← Thư viện Mermaid (10 loại sơ đồ)
```

---

## 📈 5 Nguyên tắc cốt lõi

1. **Right First Time** — Pre-Flight + Inline Audit = giảm iterations từ 4+ → ≤ 2
2. **Facts, not Theory** — Risk Register từ patterns thực tế, không predict từ "hàng ngàn mẫu"
3. **Visual First** — Screen Inventory + Wireframe TRƯỚC khi code. Diagram tốt hơn 1000 chữ
4. **Review độc lập** — lượt review chạy với bối cảnh sạch, nhận tài liệu và tiêu chí chứ không nhận kết luận của lượt viết
5. **Complete Traceability** — BRQ→FR/NFR→(Feature)→US→AC/TC; canonical strict bắt mỗi FR nối trực tiếp ≥ 1 US và mỗi US ≥ 1 AC/TC

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
python .\scripts\persona_review_check.py <bao-cao-review-cua-mot-tai-lieu.md>
python .\scripts\traceability_scan.py <project-folder> --scheme legacy
python .\scripts\traceability_scan.py <project-folder> --scheme canonical --strict
python .\scripts\reindex_markdown.py <project-folder>
python .\scripts\template_schema_check.py ".\Curated templates"
python .\scripts\media_audit.py ".\Curated templates"
```

Mỗi tài liệu BA được tạo hoặc sửa đáng kể cần báo cáo review riêng theo `BA-document-rule/core/persona-simulation.md`. Ghi `Loại tài liệu`, `Tier`, `Dữ liệu nhạy cảm` ở đầu báo cáo; điền các vai trò bắt buộc của Tier (Tier 3: đủ 21) với `PASS`, `ISSUE` hoặc `N/A` và căn cứ trỏ tới vị trí; chạy `persona_review_check.py` trên từng báo cáo trước khi bàn giao. `N/A` là kết quả sau khi đã xét phạm vi, không phải bỏ qua vai trò.

**Legacy bundle** dùng ID như `BRD-101 / FR-101 / US-001 / UAT-001`. Với dạng này, chạy `--scheme legacy`.

**Canonical bundle** dùng ID như `BRQ-01 / FR-MOD-001 / US-MOD-001 / AC-MOD-001` hoặc `TC-MOD-001`. Với dạng này, chạy `--scheme canonical --strict`; strict mode yêu cầu FR nối trực tiếp tới ≥ 1 US, US tới ≥ 1 AC/TC, và coi mọi ID sai scheme là lỗi. Thêm `--one-to-one` khi dự án yêu cầu ánh xạ 1:1.

`BROKEN_CHAIN` chỉ xuất hiện khi bộ tài liệu có Feature Map nhưng một chuỗi BRQ không đi qua Feature nào: bổ sung mapping Feature cho chuỗi đó, hoặc bỏ Feature Map nếu dự án không dùng tầng Feature.

---

## 🎯 LLM Triage Matrix — Khi nào dùng bao nhiêu LLM?

| Kích thước dự án | Timeline | Số LLM | Vai trò |
|---|---|:---:|---|
| **S** (< 3 sprints, MVP) | < 2 tháng | **1** | Gemini 3 hoặc Claude — đa năng |
| **M** (3-8 sprints, standard) | 2-5 tháng | **2** | Primary (Gemini/Claude) + Reviewer (o4) |
| **L** (> 8 sprints, regulated) | > 5 tháng | **4** | Full orchestration: Claude + o4 + Gemini + GPT-5 |

> **Quy tắc:** Không phải dự án nào cũng cần 4 LLM. Chọn fit-for-purpose.
