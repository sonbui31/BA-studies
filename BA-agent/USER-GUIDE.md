# HƯỚNG DẪN SỬ DỤNG BỘ KIT BA 3.3 (ADVANCED ANALYSIS & WRITING QUALITY ENGINE)

> **Chào mừng bạn đến với BA-Agent 3.3!**
> Bộ kit "Layered OS" v3.3 — **"Think Deeper, Write Better"**: Advanced Analysis + Requirement Quality Engine.
> Giữ Multi-LLM orchestration (Claude 4.6, o4, GPT-5, Gemini 3) với vai trò CỤ THỂ tại từng bước.

---

## 🚀 Khởi động nhanh

**Lệnh chính:** `/ba-workflow [tên_dự_án] [mô_tả_ngắn]`

**Quy trình 3.3 (13 bước):**

```
🚪 GATES (bắt buộc)
  0. Elicitation Gate — Phỏng vấn / Extract insight từ KH
  1. Risk Scan — Phát hiện rủi ro + sinh Risk Register
  2. Customer Intelligence — Deep probing, hidden needs
  2.5 As-Is Process — Document quy trình hiện tại + Gap Analysis

📝 GENERATION (có Pre-Flight)
  3. Template Selection — Chọn overlay + plan metrics
  4. Screen Inventory — Liệt kê screens + Navigation Map
  5. Document + Diagram + Wireframe — PRE-FLIGHT trước mỗi doc
     ↳ [NEW] Quality Engine: Decomposition + NFR Discovery + Quality Rubric

✅ VALIDATION (multi-layer)
  6. AI Quality Gate — Inline audit (Rubric + Smells + Conflicts)
  6.5 Pre-Flight Verify — Re-check sau khi viết
  6.7 Traceability Validation — BRQ→FR→US→TC chain check (incl. NFR→TC)
  7. Impact + Persona Sim + Decision Analysis — Scan, stress-test, evaluate
  7.5 [NEW] Communication Packaging — Đóng gói theo audience (CEO/Dev)
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

## 🆕 Có gì mới trong v3.3?

| Feature | v3.2 | v3.3 |
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

## 🤖 Các kỹ năng (15 Skills)

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

---

## 📂 Cấu trúc thư mục

```
BA-agent/
├── agents/ba-specialist.md     ← Agent persona & 15 Skills (v3.3)
├── workflows/ba-workflow.md    ← Slash command logic (12 bước với gates + rollback)
├── BA-document-rule/           ← "Hệ điều hành" (Core + Templates + Overlays)
│   ├── core/                   ← 19 files: Principles, Guides, Pre-Flight, Validator...
│   │   ├── pre-flight-checklist.md    ⭐ Check trước khi viết
│   │   ├── traceability-validator.md  ⭐ Auto-scan gaps (incl. NFR)
│   │   ├── screen-inventory-guide.md  ⭐ Screen & Wireframe guide
│   │   ├── requirement-quality-rubric.md ⭐ 5-point rubric + 8 Smells (v3.3)
│   │   ├── decision-analysis-framework.md ⭐ Weighted Scoring, Pugh, CBA (v3.3)
│   │   ├── nfr-discovery-guide.md     ⭐ 7 câu hỏi + 5 kỹ thuật NFR (v3.3)
│   │   ├── process-decomposition-guide.md ⭐ L0→L3 hierarchy (v3.3)
│   │   └── ... (12 existing files)
│   ├── templates/              ← 18 templates generic
│   │   ├── post-implementation-review.md  ⭐ NEW v3.2: PIR + Benefits Realization
│   │   ├── as-is-process.md           ⭐ As-Is documentation
│   │   ├── risk-register.md           ⭐ Risk Register + Response Strategies
│   │   ├── data-migration-plan.md     ⭐ Migration with rollback
│   │   ├── screen-inventory.md        ⭐ Screen tracking
│   │   ├── industry/                  ⭐ 9 templates ngành (Gov/HC/FT) — v3.3.1
│   │   └── ... (12 existing templates)
│   ├── overlays/               ← Config theo loại dự án (7 loại: 4 generic + 3 industry)
│   └── references/             ← RACI, Estimation, Elicitation, Anti-Patterns (7 files)
│       ├── anti-patterns.md           ⭐ Top 15 sai lầm BA (v3.2)
│       ├── writing-examples.md        ⭐ Mẫu viết: Precondition/Exception/BR (v3.3)
│       └── communication-packaging.md ⭐ 4 package types CEO/Dev/QC (v3.3)
├── BA-Documents-Product/       ← 11 files mẫu cho Sản phẩm
├── BA-Documents-Outsource/     ← 12 files mẫu cho Thuê ngoài
├── DOCUMENT-MAP.md             ← Bản đồ chỉ đường cho mọi file
├── USER-GUIDE.md               ← Hướng dẫn sử dụng (file này)
├── CHANGELOG.md                ← Lịch sử thay đổi
├── CONTRIBUTING.md             ← ⭐ NEW v3.2: Quy trình đóng góp
└── so_do.md                    ← Thư viện Mermaid (10 loại sơ đồ)
```

---

## 📈 5 Nguyên tắc cốt lõi v3.3

1. **Right First Time** — Pre-Flight + Inline Audit = giảm iterations từ 4+ → ≤ 2
2. **Facts, not Theory** — Risk Register từ patterns thực tế, không predict từ "hàng ngàn mẫu"
3. **Visual First** — Screen Inventory + Wireframe TRƯỚC khi code. Diagram tốt hơn 1000 chữ
4. **Multi-LLM Precision** — Claude viết, o4 nghĩ, Gemini đọc, GPT-5 draft specs
5. **Complete Traceability** — BRQ→FR→US→TC + NFR→NFR-TC — không gì bị orphan

---

## 🛠 Tùy chỉnh

- **Sửa nguyên tắc:** `BA-document-rule/core/principles.md`
- **Sửa template:** `BA-document-rule/templates/*.md`
- **Sửa Pre-Flight items:** `BA-document-rule/core/pre-flight-checklist.md`
- **Sửa traceability rules:** `BA-document-rule/core/traceability-validator.md`
- **Thêm overlay mới:** Tạo folder trong `BA-document-rule/overlays/`
- **Xem anti-patterns:** `BA-document-rule/references/anti-patterns.md`
- **Xem changelog:** `CHANGELOG.md`

---

## 🎯 LLM Triage Matrix — Khi nào dùng bao nhiêu LLM?

| Kích thước dự án | Timeline | Số LLM | Vai trò |
|---|---|:---:|---|
| **S** (< 3 sprints, MVP) | < 2 tháng | **1** | Gemini 3 hoặc Claude — đa năng |
| **M** (3-8 sprints, standard) | 2-5 tháng | **2** | Primary (Gemini/Claude) + Reviewer (o4) |
| **L** (> 8 sprints, regulated) | > 5 tháng | **4** | Full orchestration: Claude + o4 + Gemini + GPT-5 |

> **Quy tắc:** Không phải dự án nào cũng cần 4 LLM. Chọn fit-for-purpose.
