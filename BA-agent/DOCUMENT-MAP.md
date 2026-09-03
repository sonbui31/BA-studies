# HƯỚNG DẪN BỘ TÀI LIỆU BA (Document Map v3.4)

> **Mục đích:** Giải thích chức năng và nội dung từng file trong hệ thống BA-agent
> **Cập nhật:** 12/05/2026 — v3.4 (đóng gói skill + đồng bộ numbering/validation)

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
| 4A | `04A-Feature-Map.md` | Feature layer map `BR -> FR -> Feature -> US -> Test`, dùng cho strict traceability | Khi cần sign-off traceability đầy đủ |
| 5 | `05-SRS-Lite.md` | **Tùy chọn** — chỉ cho feature phức tạp: API Spec, NFR, Integration, RBAC | Khi cần spec kỹ thuật |
| 6 | `06-User-Story-Map.md` | Stories + AC kèm **OKR mapping**, Traceability Matrix, Release Mapping | Khi viết stories |
| 7 | `07-Data-Model.md` | SaaS schema (Accounts, Subscriptions, multi-tenancy) + **Analytics Data Model** | Khi thiết kế database |
| 8 | `08-Beta-Testing-Plan.md` | Gradual Rollout (5%→100%), **A/B Testing**, Feature Flags, Post-Release Monitoring | Khi chuẩn bị release |
| 9 | `09-Release-Notes.md` | Release Notes hướng user + CR tracking nội bộ | Sau mỗi release |
| 10 | `10-Standup-Notes.md` | Daily Standup, Sprint Review, Retrospective templates | Hàng ngày / mỗi Sprint |

---

## 2. BA-agent/BA-Documents-Outsource — Dự án Thuê ngoài

> **Đặc thù:** Tài liệu formal, sign-off bắt buộc, ràng buộc hợp đồng, giao tiếp từ xa.

> **📌 Lưu ý:** Bộ Outsource đánh số từ `00-` (Process Framework là hướng dẫn quy trình), sau đó `01-` là Vision & Scope (tài liệu đầu tiên cần viết). Thứ tự đánh số phản ánh đúng thứ tự viết tài liệu.

| # | File | Mô tả | Khi nào dùng |
|---|------|-------|-------------|
| 0 | `00-BA-Process-Framework.md` | Quy trình **6 phase** (thêm Phase 0: Hợp đồng). 5 Quy tắc vàng, Mốc thanh toán, Communication Protocol | Đọc đầu tiên — hiểu quy trình OS |
| 1 | `01-Vision-Scope.md` | Vision & Scope với **KH phê duyệt**, chốt phạm vi cho scope tracking | Phase 0-1: Khởi động |
| 2 | `02-BRD.md` | BRD formal — cơ sở cho **hợp đồng + ước lượng**, KH phê duyệt bắt buộc | Phase 0-1: Tiền dự án |
| 3 | `03-Stakeholder-Map.md` | Stakeholder **cả 2 bên** (KH + NCC), Communication Protocol, múi giờ, SLA phản hồi | Phase 1: Khởi động |
| 4 | `04-Process-Flow.md` | As-Is / To-Be, workshop từ xa **(ghi hình bắt buộc)** | Phase 2: Khám phá |
| 4A | `04A-Feature-Map.md` | Feature layer map `BRD/BR -> FR -> Feature -> US -> UAT`, dùng cho sign-off traceability | Phase 3: Chi tiết hóa |
| 5 | `05-SRS.md` | SRS **đầy đủ** (15-25 trang) — Dev không ngồi cạnh nên phải rõ ràng tuyệt đối | Phase 3: Chi tiết hóa |
| 6 | `06-User-Story-Map.md` | Stories + AC, **chốt phạm vi signed bởi KH** = scope agreement | Phase 3: Chi tiết hóa |
| 7 | `07-Data-Model.md` | ERD + Data Dictionary + **Swagger/OpenAPI** formal | Phase 3: Chi tiết hóa |
| 8 | `08-UAT-Plan.md` | **UAT formal** + Biên bản nghiệm thu (gắn với thanh toán milestone) | Phase 5: Kết thúc |
| 9 | `09-Change-Log.md` | CR Process — **mọi thay đổi = ảnh hưởng chi phí**, bắt buộc email/văn bản | Phase 4: Phát triển |
| 10 | `10-Meeting-Minutes.md` | MoM formal, **ghi hình bắt buộc**, gửi KH xác nhận trong 24h | Mỗi cuộc họp |
| 11 | `11-Handover-Checklist.md` | Bàn giao: mã nguồn, tài liệu, Knowledge Transfer, **bảo hành 30-90 ngày** | Phase 5: Kết thúc |

---

## 3. BA-agent/BA-document-rule — Bộ Rule & Template gốc

> **Đặc thù:** Không dùng trực tiếp — đây là "hệ điều hành" sinh ra 2 bộ tài liệu trên.
> **Cách dùng:** Chọn overlay (product/outsource/inhouse/startup) → áp lên template → tạo ra bộ tài liệu phù hợp.
> **Bắt buộc:** Trước khi đề xuất bộ tài liệu, chạy `core/project-classification-gate.md`. Nếu dự án là product/platform/SaaS/app/B2B/commercializable MVP, Product Vision Document phải đứng trước Project Charter và BRD.

### 📄 Root

| File | Mô tả |
|------|-------|
| `README.md` | Tổng quan: cách hoạt động, cấu trúc thư mục, flow sử dụng |
| `QUICK-START.md` | Hướng dẫn 5 phút: chọn overlay → copy template → viết tài liệu |

### 📁 Curated templates/ — NGUỒN TEMPLATE DUY NHẤT cho BRD, SRS, User Story, AC

> **🔴 Quy tắc Exclusive:** Đây là thư mục template **DUY NHẤT** cho 4 tài liệu cốt lõi (BRD, SRS, User Story, Acceptance Criteria). AI **BẮT BUỘC CHỈ SỬ DỤNG** các template trong folder này. **TUYỆT ĐỐI KHÔNG** dùng `BA-document-rule/templates/brd.md`, `srs.md`, `user-story-map.md` cho mục đích sinh tài liệu cốt lõi.

| File | Mô tả | Khi nào dùng |
|------|-------|-------------|
| `01-BRD-Template.md` | Template BRD chuẩn 11 phần — 100% ngôn ngữ nghiệp vụ, cấm thuật ngữ IT | Khi sinh BRD dự án |
| `02-SRS-Template.md` | Template SRS chuẩn 9 phần kỹ thuật — FR Decomposition, NFR, ERD, API, Traceability | Khi sinh SRS dự án |
| `03-User-Story-Template.md` | Template User Story chuẩn INVEST + DoD 5 tiêu chí | Khi sinh User Story dự án |
| `04-Acceptance-Criteria-Template.md` | Template AC chuẩn Given-When-Then — 4 Scenarios bắt buộc | Khi sinh Acceptance Criteria dự án |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.docx` | File gốc Word tổng hợp — có ví dụ thực chiến Đặt lịch khám bệnh | Reference kiểm tra format, bảng biểu |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.md` | Bản Markdown extraction của file Word trên | AI đọc trực tiếp khi cần tra cứu nhanh |
| `SRS.pdf` | Mẫu/reference SRS đầy đủ chuẩn IEEE dạng PDF | Khi audit SRS để đối chiếu completeness |

### 📁 core/ — Nguyên tắc cốt lõi (21 files — áp dụng mọi dự án)

| File | Mô tả | v3.0? |
|------|-------|:---:|
| `00-ba-process-framework.md` | Quy trình BA generic 5 phase: Inception → Discovery → Elaboration → Delivery → Closure | |
| `principles.md` | Nguyên tắc BA: BACCM, stakeholder-centric, traceability, iterative | |
| `writing-guide.md` | Chuẩn viết tài liệu: naming, format bảng, viết AC, ngôn ngữ, tone | |
| `diagram-guide.md` | Quy ước sơ đồ: Mermaid syntax, hình dạng, khi nào dùng loại nào | |
| `quality-checklist.md` | Checklist chất lượng: completeness, consistency, traceability check | |
| `glossary.md` | Thuật ngữ BA A-Z (AC, BABOK, BRD, CR, DoD, Epic, SRS, UAT...) | |
| `evaluation-protocol.md` | C-S-K-A Matrix 3.2: **inline audit** + Multi-LLM phases + Pre-Flight cross-check | ⬆ Updated |
| `impact-analysis-guide.md` | Phân tích ảnh hưởng: cross-file dependency scan, downstream risk | |
| `persona-simulation.md` | Mô phỏng stakeholder persona: đóng vai CFO, Architect, End-User để stress-test | |
| `stakeholder-conflict-resolution.md` | ⭐ Protocol xử lý conflict requirement: decision owner, conflict log, update rules | ⭐ NEW v3.4 |
| `code-traceability-audit.md` | Đối soát Requirement vs Code 3.0: **actionable output format** + full chain | ⬆ Updated |
| `predictive-ba-guide.md` | Risk Management 3.0: **pattern-based detection** từ tài liệu thực tế | ⬆ Updated |
| `customer-intelligence-guide.md` | Kỹ thuật khai thác & phân tích thông tin KH: probing, hidden needs, tâm lý stakeholder | |
| `project-classification-gate.md` | ⭐ Gate phân loại dự án trước khi chọn tài liệu; bắt buộc Product Vision cho product/B2B/commercializable MVP | ⭐ NEW |
| `pre-flight-checklist.md` | ⭐ Pre-Flight Engine: checklist per document type — PASS mới được viết | ⭐ NEW |
| `traceability-validator.md` | ⭐ Auto-scan cross-doc traceability: BRQ→FR→Feature→US→TC + **NFR→NFR-TC chain** + Bi-directional + Impact Chain | ⬆ v3.2 |
| `screen-inventory-guide.md` | ⭐ Screen Inventory & Wireframe enforcement: mỗi Feature ≥ 1 screen | v3.0 |
| `requirement-quality-rubric.md` | ⭐ Rubric 5 bậc chấm điểm từng câu requirement + 8 Smell Detector patterns | ⭐ NEW v3.3 |
| `decision-analysis-framework.md` | ⭐ 4 công cụ ra quyết định: Weighted Scoring, Pugh, CBA, Decision Tree | ⭐ NEW v3.3 |
| `nfr-discovery-guide.md` | ⭐ 7 câu hỏi + 5 kỹ thuật phát hiện NFR specific cho từng dự án | ⭐ NEW v3.3 |
| `process-decomposition-guide.md` | ⭐ Phân rã quy trình L0→L1→L2→L3 + rules khi nào dừng | ⭐ NEW v3.3 |

### 📁 templates/ — 28 templates generic

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
| `meeting-minutes.md` | Template Meeting Minutes + **Decision Log** + **Risk Escalation** + **Open Items tracking** | ⬆ v3.2 |
| `handover-checklist.md` | Template Bàn giao | |
| `api-specification.md` | Template API Specification | |
| `as-is-process.md` | ⭐ Template As-Is Process: Current State + Pain Points + Gap Analysis + Metrics Baseline | ⭐ NEW |
| `risk-register.md` | ⭐ Template Risk Register: Impact×Probability + Heatmap + Auto-detect + **Risk Response Strategies** | ⬆ v3.2 |
| `data-migration-plan.md` | ⭐ Template Data Migration: Source→Target mapping + Cleansing + Rollback | ⭐ NEW |
| `screen-inventory.md` | ⭐ Template Screen Inventory: Master screen list + Navigation Map + Responsive Matrix | ⭐ NEW |
| `post-implementation-review.md` | ⭐ Template PIR: Benefits Realization + Lessons Learned + Tech Debt + User Adoption | ⭐ NEW v3.2 |
| `ai-feature-spec.md` | ⭐ Template AI/ML Feature: AI Behavior + Confidence Matrix + Human-in-the-Loop + Fallbacks | ⭐ NEW v3.1 |
| `business-case.md` | ⭐ Business Case: options, cost-benefit, ROI/NPV, feasibility, Go/No-Go | ⭐ NEW |
| `raid-log.md` | ⭐ RAID Log: Risks, Assumptions, Issues, Dependencies + escalation | ⭐ NEW |
| `rbac-matrix.md` | ⭐ RBAC Matrix: roles, permissions, data scope, segregation of duties | ⭐ NEW |
| `reporting-specification.md` | ⭐ Reporting/BI Spec: KPI, report catalog, source mapping, DQ checks | ⭐ NEW |
| `operational-readiness-checklist.md` | ⭐ Operational Readiness: go-live, cutover, support, monitoring, rollback | ⭐ NEW |
| `test-strategy.md` | ⭐ Test Strategy: SIT/UAT/regression/NFR coverage + defect triage | ⭐ NEW |
| `user-research-plan.md` | ⭐ User Research Plan: objective, script, participant plan, synthesis | ⭐ NEW |
| `product-analytics-spec.md` | ⭐ Product Analytics: metrics, funnel, event taxonomy, experiments | ⭐ NEW |
| `bpmn-modeling-standard.md` | ⭐ BPMN Modeling Standard: notation, gateway, exception, handoff rules | ⭐ NEW |
| `data-governance-plan.md` | ⭐ Data Governance: owner, classification, CDE, data quality, retention | ⭐ NEW |

### 📁 overlays/ — Tùy chỉnh theo loại dự án

| File | Khi nào dùng | Thay đổi chính |
|------|-------------|---------------|
| `BA-document-rule/overlays/inhouse/overlay-config.md` | Dự án nội bộ | SRS Lite, linh hoạt, ít sign-off |
| `BA-document-rule/overlays/outsource/overlay-config.md` | Dự án thuê ngoài | Phase 0, SRS đầy đủ, sign-off, NDA, Payment Milestone |
| `BA-document-rule/overlays/product/overlay-config.md` | Sản phẩm SaaS/App | BRD nhẹ + OKR, User Flow, Beta Test, A/B Test |
| `BA-document-rule/overlays/startup-mvp/overlay-config.md` | Startup cần MVP nhanh | Lean Canvas, chỉ 2-4 docs, tốc độ > chất lượng tài liệu |
| `BA-document-rule/overlays/government/overlay-config.md` | ⭐ Dự án CNTT Chính phủ/Khu vực công | Đấu thầu (Luật 22/2023), nghiệm thu nhiều cấp, ATTT, LGSP/NGSP |
| `BA-document-rule/overlays/healthcare/overlay-config.md` | ⭐ Dự án Y tế: HIS/EMR/LIS | PHI protection (NĐ 13/2023), HL7 FHIR, Clinical Workflow, DDI check |
| `BA-document-rule/overlays/fintech/overlay-config.md` | ⭐ Dự án Tài chính/Thanh toán | PCI-DSS, AML/KYC, Transaction Integrity, Reconciliation, NHNN compliance |

### 📁 templates/industry/ — Template đặc thù ngành (Chỉ dùng cho 🏛️ Gov / 🏥 HC / 💰 FT)

| File | Ngành | Mô tả |
|------|:-----:|-------|
| `regulatory-compliance-matrix.md` | 🏛️🏥💰 | Feature → Regulation mapping + Gap Analysis + Audit Readiness + Evidence ownership |
| `procurement-bidding-spec.md` | 🏛️ | Hồ sơ mời thầu (HSMT) + Ước lượng ngân sách (ROM) + Đào tạo CBCC |
| `multi-level-acceptance.md` | 🏛️🏥 | Nghiệm thu sơ bộ → Vận hành thử → Nghiệm thu chính thức + Clinical Validation |
| `clinical-workflow-map.md` | 🏥 | Clinical Pathway Maps (OPD/IPD/ER) + DDI Rules + HL7 FHIR Data Flow |
| `data-privacy-consent.md` | 🏥💰 | Data Classification Matrix + Consent Lifecycle + Break-the-Glass Protocol + rights evidence |
| `industry-integration-spec.md` | 🏛️🏥💰 | Tích hợp ngành: LGSP/NGSP, HL7 FHIR, Open Banking + Error handling + Retry |
| `transaction-recon-spec.md` | 💰 | Transaction State Machine + Double-entry Ledger + Idempotency + Reconciliation |
| `aml-kyc-process.md` | 💰 | eKYC 4-tier + CDD Risk Scoring + AML Rules + SAR Filing |
| `security-continuity-plan.md` | 🏛️🏥💰 | STRIDE Threat Model + DR/BCP + ATTT Assessment (NĐ 85/2016) + drill evidence |

### 📁 references/ — Tài liệu tham khảo

| File | Mô tả |
|------|-------|
| `elicitation-techniques.md` | Kỹ thuật thu thập yêu cầu: interview, workshop, observation, survey |
| `estimation-guide.md` | Ước lượng: story points, T-shirt sizing, ROM, function points |
| `raci-matrix.md` | Hướng dẫn xây dựng RACI + ví dụ + sai lầm thường gặp |
| `tools-recommendation.md` | Khuyến nghị công cụ: Jira, Confluence, Figma, Draw.io |
| `anti-patterns.md` | ⭐ **15 sai lầm BA thường gặp** + Root Cause + Cách tránh + Self-check | v3.2 |
| `writing-examples.md` | ⭐ Bộ mẫu viết: Precondition, Exception, Business Rule, NFR, Integration Spec, Test Case | ⭐ NEW v3.3 |
| `communication-packaging.md` | ⭐ 4 package types đóng gói thông tin: Executive Summary, Technical Brief, Test Strategy, Quick Start | ⭐ NEW v3.3 |
| `ba-knowledge-base.md` | Knowledge base BA tự chứa, chắt lọc từ kho `BA/`, dùng được ngay cả khi xoá folder nguồn | ⭐ NEW |
| `ba-knowledge-cards.json` | Retrieval cards có cấu trúc cho các chủ đề BRD/SRS/UAT/RTM/modeling/data/product/AI/domain | ⭐ NEW |

### 📁 scripts/ — Audit Scripts & Công cụ Tự động hóa (14 files)

| File | Mô tả | Khi nào dùng |
|------|-------|-------------|
| `preflight_check.py` | Kiểm tra tính đầy đủ tài liệu: placeholder `{{...}}`, tiếng Việt có dấu, Glossary, Stakeholder Map, Business Rules, numbering | Sau khi draft xong BRD/SRS/Story/UAT |
| `quality_rubric.py` | Chấm điểm chất lượng yêu cầu 1-5, bắt 8 Smells + 6 Conflict patterns | Sau khi viết FR/NFR hoặc User Story |
| `traceability_scan.py` | Quét chuỗi `BRQ→FR→Feature→US→TC`, phát hiện Orphan Requirements & gãy ID | Bước 4 (Validation) và trước bàn giao |
| `reindex_markdown.py` | Audit & tự sửa thứ tự heading §1→§2→§3 và ID tuần tự | Khi tài liệu có nhiều lần sửa |
| `ba_response_eval.py` | Đánh giá bao phủ controls theo loại dự án (Outsource/Product/Fintech) | Trước khi nghiệm thu |
| `ba_bundle_audit.py` | Audit toàn vẹn phiên bản hệ thống BA-agent | Khi bảo trì/nâng cấp skill |
| `knowledge_search.py` | Tìm kiếm tri thức BA từ knowledge cards | Khi cần tra cứu kiến thức |
| `knowledge_index_search.py` | BM25 + Hybrid search trên knowledge index | Khi cần search sâu |
| `build_knowledge_index.py` | Rebuild knowledge index từ sources | Khi cập nhật knowledge |
| `build_semantic_index.py` | Build semantic search index | Khi cập nhật knowledge |
| `semantic_index_search.py` | Semantic search trên index | Khi cần search ngữ nghĩa |
| `ba_id_utils.py` | Tiện ích xử lý BA ID (parse, validate, generate) | Dùng nội bộ bởi scripts khác |
| `eval_golden_cases.py` | Chạy golden test cases cho quality assurance | Khi kiểm tra regression |
| `docx_to_md.py` | Chuyển đổi file DOCX sang Markdown | Khi cần convert tài liệu |

### 📁 knowledge-index/ — Self-contained source index

| File | Mô tả |
|------|-------|
| `manifest.json` | Metadata build index, số docs/chunks, xác nhận không phụ thuộc folder nguồn lúc runtime |
| `chunks.jsonl` | Chunk nội dung/metadata đã extract từ tài liệu BA, search bằng `scripts/knowledge_index_search.py` |

### 📄 Index rebuild dependencies

| File | Mô tả |
|------|-------|
| `requirements-knowledge-index.txt` | Optional dependencies để rebuild PDF full-text index bằng `pypdf` và `pdfminer.six` |

### 📁 user-manual-generator/ — Tạo User Manual tiếng Việt (Docusaurus 3.10)

> **Đặc thù:** Tạo tài liệu hướng dẫn sử dụng tiếng Việt cho web app, desktop app, mobile app hoặc hệ thống nội bộ. Output là Docusaurus site có screenshot, phân quyền, và trang Home giới thiệu sản phẩm.

| File | Mô tả | Khi nào dùng |
|------|-------|-------------|
| `SKILL.md` | Rule chính để agent tạo manual: workflow, evidence rules, structure, quality bar | Khi cần tạo/cập nhật user manual |
| `README.md` | Hướng dẫn tổng quan, nguyên tắc, cách chạy audit | Đọc overview |
| `references/writing-guide.md` | Quy chuẩn viết tiếng Việt: tone, format, thuật ngữ | Khi viết nội dung manual |
| `references/docusaurus.md` | Hướng dẫn tạo và deploy Docusaurus 3.10 + GitHub Pages | Khi setup/deploy site |
| `references/capture-guide.md` | Hướng dẫn chụp screenshot và log bằng chứng | Khi thu thập hình ảnh |
| `references/handoff-template.md` | Template cho thông tin chưa xác minh (handoff-notes.md) | Khi có assumptions/open questions |
| `scripts/audit-docs.js` | Kiểm tra link, image, placeholder, privacy, cú pháp trước khi bàn giao | Trước khi delivery manual |
