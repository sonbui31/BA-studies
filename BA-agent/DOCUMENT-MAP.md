# HƯỚNG DẪN BỘ TÀI LIỆU BA (Document Map v3.0)

> **Mục đích:** Giải thích chức năng và nội dung từng file trong hệ thống BA-agent
> **Cập nhật:** 01/04/2026 — v3.0 (thêm 3 core + 4 templates mới)

---

## 1. BA-agent/BA-Documents-Product — Dự án Sản phẩm (SaaS / Platform / App)

> **Đặc thù:** Data-driven, user research, metrics-focused, continuous improvement.

| # | File | Mô tả | Khi nào dùng |
|---|------|-------|-------------|
| 0 | `00-BA-Process-Framework.md` | Quy trình **Product Cycle**: Discover → Define → Build → Measure. Lặp lại liên tục, không có "kết thúc". | Đọc đầu tiên — hiểu vòng đời Product |
| 1 | `01-Vision-Scope.md` | Product Vision Board, **OKRs**, AARRR Metrics (Acquisition → Referral), Revenue Model, Competitive Landscape | Khi bắt đầu sản phẩm mới |
| 2 | `02-BRD.md` | BRD cho Product: Problem Statement, Success Metrics, **MoSCoW + Kano**, Rollout Plan, RTM | Khi define feature/epic |
| 3 | `03-User-Personas.md` | User Personas (journey, pain points, quotes), Persona Priority Matrix, Interview Plan | Khi research user |
| 4 | `04-User-Flow.md` | Onboarding Flow, Core User Flow, Error/Edge Cases, Notification Flows, **Analytics tracking points** | Khi thiết kế luồng |
| 5 | `05-SRS-Lite.md` | **Tùy chọn** — chỉ cho feature phức tạp: API Spec, NFR, Integration, RBAC | Khi cần spec kỹ thuật |
| 6 | `06-User-Story-Map.md` | Stories + AC kèm **OKR mapping**, Traceability Matrix, Release Mapping | Khi viết stories |
| 7 | `07-Data-Model.md` | SaaS schema (Accounts, Subscriptions, multi-tenancy) + **Analytics Data Model** | Khi thiết kế database |
| 8 | `08-Beta-Testing-Plan.md` | Gradual Rollout (5%→100%), **A/B Testing**, Feature Flags, Post-Release Monitoring | Khi chuẩn bị release |
| 9 | `09-Release-Notes.md` | Release Notes hướng user + CR tracking nội bộ | Sau mỗi release |
| 10 | `10-Standup-Notes.md` | Daily Standup, Sprint Review, Retrospective templates | Hàng ngày / mỗi Sprint |

---

## 2. BA-agent/BA-Documents-Outsource — Dự án Thuê ngoài

> **Đặc thù:** Tài liệu formal, sign-off bắt buộc, ràng buộc hợp đồng, giao tiếp từ xa.

| # | File | Mô tả | Khi nào dùng |
|---|------|-------|-------------|
| 1 | `01-BA-Process-Framework.md` | Quy trình **6 phase** (thêm Phase 0: Hợp đồng). 5 Quy tắc vàng, Payment Milestone, Communication Protocol | Đọc đầu tiên — hiểu quy trình OS |
| 2 | `02-BRD.md` | BRD formal — cơ sở cho **hợp đồng + ước lượng**, KH sign-off bắt buộc | Phase 0: Tiền dự án |
| 3 | `03-Vision-Scope.md` | Vision & Scope với **KH sign-off**, baseline cho scope tracking | Phase 1: Khởi động |
| 4 | `04-Stakeholder-Map.md` | Stakeholder **cả 2 bên** (KH + NCC), Communication Protocol, múi giờ, SLA phản hồi | Phase 1: Khởi động |
| 5 | `05-Process-Flow.md` | As-Is / To-Be, workshop từ xa **(ghi hình bắt buộc)** | Phase 2: Khám phá |
| 6 | `06-SRS.md` | SRS **đầy đủ** (15-25 trang) — Dev không ngồi cạnh nên phải rõ ràng tuyệt đối | Phase 3: Chi tiết hóa |
| 7 | `07-User-Story-Map.md` | Stories + AC, **baseline signed bởi KH** = scope agreement | Phase 3: Chi tiết hóa |
| 8 | `08-Data-Model.md` | ERD + Data Dictionary + **Swagger/OpenAPI** formal | Phase 3: Chi tiết hóa |
| 9 | `09-UAT-Plan.md` | **UAT formal** + Biên bản nghiệm thu (gắn với thanh toán milestone) | Phase 5: Kết thúc |
| 10 | `10-Change-Log.md` | CR Process — **mọi thay đổi = ảnh hưởng chi phí**, bắt buộc email/văn bản | Phase 4: Phát triển |
| 11 | `11-Meeting-Minutes.md` | MoM formal, **ghi hình bắt buộc**, gửi KH xác nhận trong 24h | Mỗi cuộc họp |
| 12 | `12-Handover-Checklist.md` | Bàn giao: mã nguồn, tài liệu, Knowledge Transfer, **bảo hành 30-90 ngày** | Phase 5: Kết thúc |

---

## 3. BA-agent/BA-document-rule — Bộ Rule & Template gốc

> **Đặc thù:** Không dùng trực tiếp — đây là "hệ điều hành" sinh ra 2 bộ tài liệu trên.
> **Cách dùng:** Chọn overlay (product/outsource/inhouse/startup) → áp lên template → tạo ra bộ tài liệu phù hợp.

### 📄 Root

| File | Mô tả |
|------|-------|
| `README.md` | Tổng quan: cách hoạt động, cấu trúc thư mục, flow sử dụng |
| `QUICK-START.md` | Hướng dẫn 5 phút: chọn overlay → copy template → viết tài liệu |

### 📁 core/ — Nguyên tắc cốt lõi (15 files — áp dụng mọi dự án)

| File | Mô tả | v3.0? |
|------|-------|:---:|
| `00-ba-process-framework.md` | Quy trình BA generic 5 phase: Inception → Discovery → Elaboration → Delivery → Closure | |
| `principles.md` | Nguyên tắc BA: BACCM, stakeholder-centric, traceability, iterative | |
| `writing-guide.md` | Chuẩn viết tài liệu: naming, format bảng, viết AC, ngôn ngữ, tone | |
| `diagram-guide.md` | Quy ước sơ đồ: Mermaid syntax, hình dạng, khi nào dùng loại nào | |
| `quality-checklist.md` | Checklist chất lượng: completeness, consistency, traceability check | |
| `glossary.md` | Thuật ngữ BA A-Z (AC, BABOK, BRD, CR, DoD, Epic, SRS, UAT...) | |
| `evaluation-protocol.md` | C-S-K-A Matrix 3.0: **inline audit** + Multi-LLM phases + Pre-Flight cross-check | ⬆ Updated |
| `impact-analysis-guide.md` | Phân tích ảnh hưởng: cross-file dependency scan, downstream risk | |
| `persona-simulation.md` | Mô phỏng stakeholder persona: đóng vai CFO, Architect, End-User để stress-test | |
| `code-traceability-audit.md` | Đối soát Requirement vs Code 3.0: **actionable output format** + full chain | ⬆ Updated |
| `predictive-ba-guide.md` | Risk Management 3.0: **pattern-based detection** từ tài liệu thực tế | ⬆ Updated |
| `customer-intelligence-guide.md` | Kỹ thuật khai thác & phân tích thông tin KH: probing, hidden needs, tâm lý stakeholder | |
| `pre-flight-checklist.md` | ⭐ Pre-Flight Engine: checklist per document type — PASS mới được viết | ⭐ NEW |
| `traceability-validator.md` | ⭐ Auto-scan cross-doc traceability: BRQ→FR→Feature→US→TC chain | ⭐ NEW |
| `screen-inventory-guide.md` | ⭐ Screen Inventory & Wireframe enforcement: mỗi Feature ≥ 1 screen | ⭐ NEW |

### 📁 templates/ — 16 templates generic

| File | Mô tả | v3.0? |
|------|-------|:---:|
| `vision-scope.md` | Template Vision & Scope | |
| `brd.md` | Template BRD (Business Requirements) | |
| `stakeholder-map.md` | Template Stakeholder Map + RACI | |
| `process-flow.md` | Template Process Flow (As-Is / To-Be) | |
| `srs.md` | Template SRS (Functional + Non-functional) | |
| `user-story-map.md` | Template User Story Map (Epic → Feature → Story) | |
| `data-model.md` | Template Data Model (ERD + Data Dictionary) | |
| `uat-plan.md` | Template UAT Plan | |
| `change-log.md` | Template Change Log + CR Process | |
| `meeting-minutes.md` | Template Meeting Minutes | |
| `handover-checklist.md` | Template Bàn giao | |
| `api-specification.md` | Template API Specification | |
| `as-is-process.md` | ⭐ Template As-Is Process: Current State + Pain Points + Gap Analysis + Metrics Baseline | ⭐ NEW |
| `risk-register.md` | ⭐ Template Risk Register: Impact×Probability + Heatmap + Auto-detect rules | ⭐ NEW |
| `data-migration-plan.md` | ⭐ Template Data Migration: Source→Target mapping + Cleansing + Rollback | ⭐ NEW |
| `screen-inventory.md` | ⭐ Template Screen Inventory: Master screen list + Navigation Map + Responsive Matrix | ⭐ NEW |

### 📁 overlays/ — Tùy chỉnh theo loại dự án

| File | Khi nào dùng | Thay đổi chính |
|------|-------------|---------------|
| `inhouse/overlay-config.md` | Dự án nội bộ | SRS Lite, linh hoạt, ít sign-off |
| `outsource/overlay-config.md` | Dự án thuê ngoài | Phase 0, SRS đầy đủ, sign-off, NDA, Payment Milestone |
| `product/overlay-config.md` | Sản phẩm SaaS/App | BRD nhẹ + OKR, User Flow, Beta Test, A/B Test |
| `startup-mvp/overlay-config.md` | Startup cần MVP nhanh | Lean Canvas, chỉ 2-4 docs, tốc độ > chất lượng tài liệu |

### 📁 references/ — Tài liệu tham khảo

| File | Mô tả |
|------|-------|
| `elicitation-techniques.md` | Kỹ thuật thu thập yêu cầu: interview, workshop, observation, survey |
| `estimation-guide.md` | Ước lượng: story points, T-shirt sizing, ROM, function points |
| `raci-matrix.md` | Hướng dẫn xây dựng RACI + ví dụ + sai lầm thường gặp |
| `tools-recommendation.md` | Khuyến nghị công cụ: Jira, Confluence, Figma, Draw.io |
