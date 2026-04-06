# BA-DOCUMENT-RULE
## Bộ quy tắc & Template tài liệu Business Analysis

> **Phiên bản:** 3.3 | **Ngày:** 06/04/2026
> **Kiến trúc:** Layered OS (Core + Templates + Overlays)
> **Áp dụng:** Mọi loại dự án

---

## 🎯 Mục đích

Bộ **BA-document-rule** cung cấp:
- **Quy tắc chung** cho mọi tài liệu BA (chuẩn viết, quality check, models)
- **Template** cho từng loại tài liệu (Vision & Scope, BRD, SRS, Story Map...)
- **Overlay** tùy chỉnh theo loại dự án (In-house, Outsource, Product, Startup)

---

## 📐 Models & Frameworks tích hợp

| Model | Mục đích | File tham chiếu |
|-------|---------|----------------|
| **BACCM** | 6 khái niệm lõi BA (Change, Need, Solution, Stakeholder, Value, Context) | `core/principles.md` |
| **BABOK® v3** | 7 Knowledge Areas chuẩn quốc tế | `core/principles.md` |
| **MoSCoW** | Phân loại ưu tiên (Must/Should/Could/Won't) | `core/principles.md` |
| **Kano Model** | Phân tích mức hài lòng (Basic/Performance/Excitement) | `core/principles.md` |
| **INVEST** | Tiêu chí viết User Story | `core/principles.md` |
| **Given-When-Then** | Viết Acceptance Criteria chuẩn BDD | `core/principles.md` |
| **SWOT** | Phân tích chiến lược | `templates/brd.md` |
| **Impact Mapping** | Goal → Actors → Impacts → Features | `templates/vision-scope.md` |
| **5W1H** | Khung thu thập yêu cầu | `core/principles.md` |
| **RACI** | Ma trận phân công trách nhiệm | `references/raci-matrix.md` |
| **Lean Canvas** | 1-page business model (Startup) | `overlays/startup-mvp/` |

---

## 📁 Cấu trúc thư mục

```
BA-document-rule/
│
├── README.md                          ← Bạn đang đọc file này
├── QUICK-START.md                     ← 5 phút bắt đầu dự án mới
│
├── core/                              ← CORE LAYER — Quy tắc bất biến (19 files)
│   ├── 00-ba-process-framework.md     Quy trình BA 5 pha + BABOK mapping
│   ├── principles.md                  BACCM, MoSCoW, Kano, INVEST, GWT, SWOT, 5W1H
│   ├── writing-guide.md              Chuẩn viết, format, versioning, SMART req
│   ├── diagram-guide.md              Hướng dẫn vẽ sơ đồ (Mermaid)
│   ├── quality-checklist.md          DoR, DoD, BACCM check, review checklist
│   ├── glossary.md                   Thuật ngữ BA
│   ├── evaluation-protocol.md        C-S-K-A Matrix 3.3: inline audit + Multi-LLM phases
│   ├── impact-analysis-guide.md      Phân tích ảnh hưởng: Scoring + Ripple Effect + Regression Map
│   ├── persona-simulation.md         Mô phỏng stakeholder persona
│   ├── code-traceability-audit.md    Đối soát Requirement vs Code
│   ├── predictive-ba-guide.md        Risk Management: pattern-based detection
│   ├── customer-intelligence-guide.md Khai thác & phân tích thông tin KH
│   ├── pre-flight-checklist.md       ⭐ Pre-Flight Engine: checklist per document type (v3.0)
│   ├── traceability-validator.md     ⭐ Auto-scan cross-doc: BRQ→FR→US→TC + NFR chain (v3.2)
│   ├── screen-inventory-guide.md     ⭐ Screen Inventory & Wireframe enforcement (v3.0)
│   ├── requirement-quality-rubric.md ⭐ 5-point rubric + 8 Smell Detector (v3.3)
│   ├── decision-analysis-framework.md ⭐ Weighted Scoring, Pugh, CBA, Decision Tree (v3.3)
│   ├── nfr-discovery-guide.md        ⭐ 7 câu hỏi + 5 kỹ thuật phát hiện NFR (v3.3)
│   └── process-decomposition-guide.md ⭐ Phân rã quy trình L0→L3 (v3.3)
│
├── templates/                         ← TEMPLATES — Mẫu tài liệu (18 files)
│   ├── vision-scope.md               + Impact Mapping, Context Diagram
│   ├── brd.md                        + SWOT, 5W1H, MoSCoW, Kano
│   ├── stakeholder-map.md            + Power/Interest Grid, RACI
│   ├── process-flow.md               + As-Is/To-Be, Gap Analysis, Swimlane
│   ├── srs.md                        + NFR categories, State/Sequence Diagram
│   ├── user-story-map.md             + INVEST, GWT, MoSCoW, Kano, Release Plan
│   ├── data-model.md                 + ERD, Data Dictionary, Index Strategy
│   ├── uat-plan.md                   + Entry/Exit Criteria, Traceability
│   ├── change-log.md                 + CR workflow, Impact Analysis
│   ├── meeting-minutes.md            + Decision Log, Risk Escalation, Open Items (v3.2)
│   ├── handover-checklist.md         + Knowledge Transfer, Warranty
│   ├── api-specification.md          + REST conventions, Auth flow
│   ├── as-is-process.md              ⭐ As-Is: Current State + Pain Points + Gap Analysis (v3.0)
│   ├── risk-register.md              ⭐ Risk Register + Response Strategies + Heatmap (v3.2)
│   ├── data-migration-plan.md        ⭐ Migration: Source→Target + Rollback (v3.0)
│   ├── screen-inventory.md           ⭐ Screen list + Navigation Map + Responsive (v3.0)
│   ├── post-implementation-review.md ⭐ PIR: Benefits + Lessons + Tech Debt (v3.2)
│   └── ai-feature-spec.md            ⭐ AI Behavior + Confidence Matrix + Fallbacks (v3.1)
│
├── overlays/                          ← OVERLAYS — Tùy chỉnh theo loại dự án
│   ├── inhouse/overlay-config.md      In-house: SRS Lite, flexible
│   ├── outsource/overlay-config.md    Outsource: formal, sign-off, NDA, payment
│   ├── product/overlay-config.md      Product: BRD, OKR, A/B test
│   └── startup-mvp/overlay-config.md  Startup: Lean Canvas, 2-4 docs only
│
└── references/                        ← REFERENCES — Tài liệu tham khảo (7 files)
    ├── elicitation-techniques.md      Kỹ thuật thu thập yêu cầu
    ├── estimation-guide.md            Ước lượng: T-Shirt, Planning Poker, 3-Point
    ├── raci-matrix.md                 Hướng dẫn RACI
    ├── tools-recommendation.md        Công cụ khuyến nghị
    ├── anti-patterns.md               ⭐ 15 sai lầm BA + Root Cause + Self-check (v3.2)
    ├── writing-examples.md            ⭐ Mẫu viết: Precondition/Exception/BR/NFR/TC (v3.3)
    └── communication-packaging.md     ⭐ 4 package types: CEO/Dev/QC/End-User (v3.3)
```

---

## 🚀 Bắt đầu nhanh

1. Đọc **`QUICK-START.md`** — hướng dẫn 5 phút
2. Chọn **overlay** phù hợp → biết cần tạo tài liệu nào
3. Copy **templates** cần thiết → điền thông tin dự án
4. Dùng **`core/quality-checklist.md`** để review trước sign-off

---

## 📖 Đọc theo vai trò

| Vai trò | Bắt đầu từ đâu |
|---------|----------------|
| **BA mới** | `core/principles.md` → `core/writing-guide.md` → `QUICK-START.md` |
| **BA có kinh nghiệm** | `QUICK-START.md` → Chọn overlay → Copy templates |
| **PM** | `core/00-ba-process-framework.md` → `references/raci-matrix.md` |
| **Dev Lead** | `templates/srs.md` → `templates/data-model.md` → `templates/api-specification.md` |
| **Trainer** | `core/principles.md` (BACCM, models) → `core/quality-checklist.md` (DoR/DoD) |
