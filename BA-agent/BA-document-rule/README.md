# BA-DOCUMENT-RULE
## Bộ quy tắc & Template tài liệu Business Analysis

> **Phiên bản:** 2.6 | **Ngày:** 27/03/2026
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
├── core/                              ← CORE LAYER — Quy tắc bất biến
│   ├── 00-ba-process-framework.md     Quy trình BA 5 pha + BABOK mapping
│   ├── principles.md                  BACCM, MoSCoW, Kano, INVEST, GWT, SWOT, 5W1H
│   ├── writing-guide.md              Chuẩn viết, format, versioning, SMART req
│   ├── diagram-guide.md              Hướng dẫn vẽ sơ đồ (Mermaid)
│   ├── quality-checklist.md          DoR, DoD, BACCM check, review checklist
│   ├── glossary.md                   Thuật ngữ BA
│   ├── evaluation-protocol.md        C-S-K-A Matrix chấm điểm tài liệu (v2.2)
│   ├── impact-analysis-guide.md      Phân tích ảnh hưởng cross-file (v2.5)
│   ├── persona-simulation.md         Mô phỏng stakeholder persona (v2.5)
│   ├── code-traceability-audit.md    Đối soát Requirement vs Code (v2.6)
│   ├── predictive-ba-guide.md        Dự báo rủi ro Scope Creep (v2.6)
│   └── customer-intelligence-guide.md Khai thác & phân tích thông tin KH (v2.6)
│
├── templates/                         ← TEMPLATES — Mẫu tài liệu
│   ├── vision-scope.md               + Impact Mapping, Context Diagram
│   ├── brd.md                        + SWOT, 5W1H, MoSCoW, Kano
│   ├── stakeholder-map.md            + Power/Interest Grid, RACI
│   ├── process-flow.md               + As-Is/To-Be, Gap Analysis, Swimlane
│   ├── srs.md                        + NFR categories, State/Sequence Diagram
│   ├── user-story-map.md             + INVEST, GWT, MoSCoW, Kano, Release Plan
│   ├── data-model.md                 + ERD, Data Dictionary, Index Strategy
│   ├── uat-plan.md                   + Entry/Exit Criteria, Traceability
│   ├── change-log.md                 + CR workflow, Impact Analysis
│   ├── meeting-minutes.md            + Action Item tracking
│   ├── handover-checklist.md         + Knowledge Transfer, Warranty
│   └── api-specification.md          + REST conventions, Auth flow
│
├── overlays/                          ← OVERLAYS — Tùy chỉnh theo loại dự án
│   ├── inhouse/overlay-config.md      In-house: SRS Lite, flexible
│   ├── outsource/overlay-config.md    Outsource: formal, sign-off, NDA, payment
│   ├── product/overlay-config.md      Product: BRD, OKR, A/B test
│   └── startup-mvp/overlay-config.md  Startup: Lean Canvas, 2-4 docs only
│
└── references/                        ← REFERENCES — Tài liệu tham khảo
    ├── raci-matrix.md                 Hướng dẫn RACI
    ├── elicitation-techniques.md      Kỹ thuật thu thập yêu cầu
    ├── estimation-guide.md            Ước lượng: T-Shirt, Planning Poker, 3-Point
    └── tools-recommendation.md        Công cụ khuyến nghị
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
