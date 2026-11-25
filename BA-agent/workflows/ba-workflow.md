---
description: Business Analysis Workflow 3.10.0 - các bước lối L4, định tuyến theo ngành, rollback và ước lượng công
---

# BA Workflow Protocol 3.10.0

Các bước chi tiết của lối L4: định tuyến theo loại dự án và ngành (Government / Healthcare / Fintech), tài liệu phụ theo tín hiệu nghiệp vụ, rollback và ước lượng công.

> **File này không chép lại luật.** Nguyên tắc viết (tiếng Việt có dấu, chỉ dùng curated template, độc giả từng tài liệu, văn phong chống "mùi AI"): `../SKILL.md` mục 1–2. Hard Gate 1–8 và checkpoint: `../SKILL.md` mục 10. Việc người phải làm (H1–H6): `../BA-document-rule/core/human-accountability.md`. Khi file này và SKILL.md nói khác nhau, SKILL.md đúng.

// turbo-all

## Steps

> **Workflow này dành cho lối L4 (dự án/epic mới)** và phần thay đổi của lối L3. Trước Step 0, phân loại yêu cầu theo `../BA-document-rule/core/intake-triage.md`: hỏi đáp (L0), review một artifact (L1) hay viết một artifact lẻ (L2) thì xử lý ngay, không chạy các step dưới đây.

### 🚪 MANDATORY GATES (Không bỏ qua)

0. **Project Classification & Stakeholder Elicitation Gate (MANDATORY)**
   - Run `../BA-document-rule/core/project-classification-gate.md` before recommending a document set
   - Classify initiative: Product / In-house / Outsource / Startup-MVP / Government / Healthcare / Fintech, plus add-ons such as AI/ML, reporting, RBAC, data governance
   - Detect commercialization signals: product, platform, SaaS, app, B2B, sell to external companies, paid offering, subscription, marketplace
   - **Non-negotiable Vision Rule:** If the initiative is a new product, platform, SaaS/app, commercializable MVP, or B2B offering, list **Product Vision Document** before Project Charter and BRD. BRD/Charter must not replace Vision.
   - **Output:** Project Classification Summary + Required Document Layers + Assumptions to Validate
   - Nhận raw input (file PDF/DOC/text/transcript)
   - Sinh Interview Questionnaire theo stakeholder roles (sử dụng `../BA-document-rule/core/customer-intelligence-guide.md`)
   - Yêu cầu user trả lời hoặc cung cấp transcript phỏng vấn
   - Extract: Pain Points, Hidden Needs, Constraints, Assumptions
   - **Sổ nguồn và kế hoạch elicitation** (`../BA-document-rule/core/evidence-source-gate.md`): mỗi insight ghi nguồn (`SRC-xx`, trực tiếp/gián tiếp) và mức E1–E4; thông tin từ người chat ghi `SRC-CHAT`. Liệt kê nhận định trọng yếu và người là nguồn trực tiếp cho từng nhận định
   - **Người chịu trách nhiệm tài liệu (H1):** hỏi tên và vai trò ngay từ đầu
   - **Output:** Insight Cards + Pain Point Map + Sổ nguồn + Kế hoạch elicitation
   - **Gate Rule:** Nếu user không cung cấp bất kỳ input nào → STOP, không tiếp tục
   - **Trọng tâm:** câu hỏi sắc, đồng cảm với người được hỏi

1. **Strategic Vision & Risk Register**
   - Create or update the strategic vision layer before BRD/SRS planning
   - For Product/B2B/commercializable MVP: draft or request Product Vision inputs (target users, differentiator, product goals, positioning, future direction)
   - For non-product internal delivery: capture Vision & Scope at project level
   - Identify goals, stakeholders, OKRs
   - **Risk Scan (o4):** Phân tích input → phát hiện patterns rủi ro → sinh Risk Register skeleton
   - Template: `../BA-document-rule/templates/risk-register.md`
   - **Trọng tâm:** edge case và kịch bản "nếu... thì"; có thể giao một lượt review độc lập (`../agents/ba-specialist.md` mục Review độc lập)

2. **Customer Intelligence & Deep Elicitation**
   - Run `../BA-document-rule/core/customer-intelligence-guide.md` — deep probing
   - Extract hidden needs, analyze stakeholder psychology, build Insight Cards
   - **Trọng tâm:** phân tích tinh tế, hỏi sâu có đồng cảm

### 📄 AS-IS DOCUMENTATION (Trước To-Be)

2.5. **As-Is Process Documentation (MANDATORY)**
    - Document quy trình hiện tại TRƯỚC khi viết To-Be
    - Template: `../BA-document-rule/templates/as-is-process.md`
    - **Output:** sơ đồ As-Is BPMN 2.0 (`../so_do.md` mục 4) + Pain Point Analysis + Gap Analysis + Metrics Baseline
    - **Gate Rule:** Nếu không có thông tin As-Is, hỏi user: "Quy trình hiện tại vận hành thế nào?"
    - Nếu user xác nhận "không có quy trình" (greenfield) → ghi N/A + lý do → tiếp tục

### 📝 GENERATION (Có Pre-Flight)

3. **Initialize Workspace & Project Type Routing**
   - Xác định loại dự án → Chọn overlay → Load industry templates (nếu có)
   - Template cho 4 tài liệu cốt lõi theo `../SKILL.md` mục 1 (nguyên tắc 4) và mục 3; template trong `BA-document-rule/templates/` chỉ dùng cho tài liệu phụ chọn ở danh sách dưới
   - Dự án đang dở dùng ID riêng: tạo `ba-scheme.json` ở thư mục bộ tài liệu (`../scripts/README.md`), không ép đổi ID khách đã đọc
   - Reconfirm the Project Classification Summary before choosing templates:
     ```text
     Project classification: <type> + <add-ons>
     Commercialization signal: <yes/no/unknown>
     Required first artifact: <Product Vision Document | Vision & Scope | Project Charter>
     Selected overlay: <overlay>
     Supporting add-ons: <AI/RBAC/Reporting/Data Governance/etc.>
     Assumptions to validate: <list>
     ```
   - Map features → success metrics → tracking events
   - Tạo thư mục project nếu chưa có
   - Chọn supporting templates theo tín hiệu nghiệp vụ:
     - Cần quyết định đầu tư / Go-No-Go → `../BA-document-rule/templates/business-case.md`
     - Có assumption, issue, dependency mở → `../BA-document-rule/templates/raid-log.md`
     - Có phân quyền theo vai trò / phạm vi dữ liệu → `../BA-document-rule/templates/rbac-matrix.md`
     - Có báo cáo, dashboard, KPI, export → `../BA-document-rule/templates/reporting-specification.md`
     - Có go-live, training, support, rollback → `../BA-document-rule/templates/operational-readiness-checklist.md`
     - Cần SIT/regression/NFR coverage → `../BA-document-rule/templates/test-strategy.md`
     - Có data owner, retention, data quality, CDE → `../BA-document-rule/templates/data-governance-plan.md`
     - Product discovery / analytics → `../BA-document-rule/templates/user-research-plan.md`, `../BA-document-rule/templates/product-analytics-spec.md`
     - Quy trình phức tạp cần chuẩn BPMN → `../BA-document-rule/templates/bpmn-modeling-standard.md`
     - New product/platform/SaaS/app/B2B/commercializable MVP → `../BA-document-rule/templates/vision-scope.md` as Product Vision Document, before BRD/Charter/SRS planning

   **📋 Project Type Routing Table:**

   | Loại | Overlay | Industry Templates | Flow bổ sung |
   |------|---------|:------------------:|-------------|
   | **In-house** | `../BA-document-rule/overlays/inhouse/` | ❌ Không | Standard flow (Step 4→8) |
   | **Outsource** | `../BA-document-rule/overlays/outsource/` | ❌ Không | Standard + Phase 0 (Hợp đồng) |
   | **Product** | `../BA-document-rule/overlays/product/` | ❌ Không | Standard + OKR/A-B test |
   | **Startup/MVP** | `../BA-document-rule/overlays/startup-mvp/` | ❌ Không | Lean flow (skip SRS, chỉ 2-4 docs) |
   | 🏛️ **Government** | `../BA-document-rule/overlays/government/` | ✅ 5 templates | **→ Step 3.5G** (HSMT, ATTT, nghiệm thu) |
   | 🏥 **Healthcare** | `../BA-document-rule/overlays/healthcare/` | ✅ 6 templates | **→ Step 3.5H** (Clinical, PHI, consent) |
   | 💰 **Fintech** | `../BA-document-rule/overlays/fintech/` | ✅ 6 templates | **→ Step 3.5F** (Transaction, AML, recon) |

   **Routing Logic:**
   ```
   IF product/platform/SaaS/app/B2B/commercializable MVP signal exists
     → Product Vision Document is mandatory
     → Prefer Product overlay unless user explicitly chooses Lean Canvas-only validation
   END

   IF loại dự án ∈ {Government, Healthcare, Fintech}
     → Load overlay-config.md
     → Load industry templates (templates/industry/)
     → Execute Step 3.5 (Industry Preparation) TRƯỚC Step 4
   ELSE
     → Load overlay-config.md
     → Skip Step 3.5 → Tiến thẳng Step 4
   END
   ```

3.5. **Industry-Specific Preparation (CHỈ cho Government / Healthcare / Fintech)** ⭐ NEW v3.3.1

    > ⚠️ **Skip step này** nếu dự án là In-house / Outsource / Product / Startup.

    **🏛️ Step 3.5G — Government Preparation:**
    | Thứ tự | Hành động | Template | Output |
    |:------:|----------|---------|--------|
    | G1 | Lập Regulatory Compliance Matrix | `../BA-document-rule/templates/industry/regulatory-compliance-matrix.md` | Feature → Luật ĐT / NĐ 85 / ATTT |
    | G2 | Chuẩn bị HSMT (nếu đấu thầu) | `../BA-document-rule/templates/industry/procurement-bidding-spec.md` | HSMT + ROM + Kế hoạch đào tạo |
    | G3 | Spec tích hợp LGSP/NGSP | `../BA-document-rule/templates/industry/industry-integration-spec.md` | Integration spec cho CSDL QG |
    | G4 | Lập Security & BCP Plan | `../BA-document-rule/templates/industry/security-continuity-plan.md` | ATTT assessment + DR/BCP |
    | G5 | Lập Multi-level Acceptance Plan | `../BA-document-rule/templates/industry/multi-level-acceptance.md` | Nghiệm thu sơ bộ → vận hành thử → nghiệm thu chính thức |
    - **Gate Rule:** HSMT phải hoàn thành TRƯỚC khi bắt đầu Step 5 (vì SRS là phụ lục HSMT)

    **🏥 Step 3.5H — Healthcare Preparation:**
    | Thứ tự | Hành động | Template | Output |
    |:------:|----------|---------|--------|
    | H1 | Document Clinical Workflow Maps | `../BA-document-rule/templates/industry/clinical-workflow-map.md` | Pathway OPD/IPD/ER + DDI rules |
    | H2 | Lập Data Classification Matrix | `../BA-document-rule/templates/industry/data-privacy-consent.md` | PHI 5-level + Consent lifecycle |
    | H3 | Spec tích hợp HL7 FHIR | `../BA-document-rule/templates/industry/industry-integration-spec.md` | FHIR Resources mapping |
    | H4 | Lập Regulatory Matrix | `../BA-document-rule/templates/industry/regulatory-compliance-matrix.md` | Feature → NĐ 13/2023, TT BYT |
    | H5 | Lập Multi-level Acceptance / Clinical Validation | `../BA-document-rule/templates/industry/multi-level-acceptance.md` | Clinical validation + nghiệm thu nhiều cấp |
    | H6 | Lập Security & BCP Plan | `../BA-document-rule/templates/industry/security-continuity-plan.md` | STRIDE + DR/BCP + drill evidence |
    - **Gate Rule:** Clinical Workflow Map phải được BS review TRƯỚC khi viết SRS

    **💰 Step 3.5F — Fintech Preparation:**
    | Thứ tự | Hành động | Template | Output |
    |:------:|----------|---------|--------|
    | F1 | Design Transaction State Machine | `../BA-document-rule/templates/industry/transaction-recon-spec.md` | State diagram + Ledger + Recon |
    | F2 | Spec AML/KYC Process | `../BA-document-rule/templates/industry/aml-kyc-process.md` | eKYC flow + AML rules + SAR |
    | F3 | Lập Data Privacy & Consent | `../BA-document-rule/templates/industry/data-privacy-consent.md` | PII classification + KYC consent |
    | F4 | Spec tích hợp Open Banking / Payment Partner | `../BA-document-rule/templates/industry/industry-integration-spec.md` | Open Banking/payment API + error handling + retry |
    | F5 | Lập Regulatory Matrix | `../BA-document-rule/templates/industry/regulatory-compliance-matrix.md` | Feature → PCI-DSS, NHNN, AML |
    | F6 | Lập Security & BCP Plan | `../BA-document-rule/templates/industry/security-continuity-plan.md` | STRIDE + DR/BCP |
    - **Gate Rule:** Transaction State Machine + AML rules phải được Compliance approve TRƯỚC Step 5

4. **Screen Inventory (NEW v3.0)**
   - Liệt kê TẤT CẢ screens cần thiết cho dự án
   - Template: `../BA-document-rule/templates/screen-inventory.md`
   - Guide: `../BA-document-rule/core/screen-inventory-guide.md`
   - **Rule:** Mỗi Feature phải có ≥ 1 screen
   - Vẽ Navigation Map (Mermaid)

5. **Document Generation, Auto-Diagram & Visual Prototyping**
   - **⚡ PRE-FLIGHT:** Chạy `../BA-document-rule/core/pre-flight-checklist.md` TRƯỚC mỗi document
   - **Luật viết:** `../SKILL.md` mục 1–2 (mở trước tài liệu đầu tiên của phiên)
   - **Automation:** Chạy `../scripts/preflight_check.py <project-folder>` trước khi draft hoặc approve artifact
     - Nếu FAIL ≥ 5 items → STOP, yêu cầu user bổ sung
     - Nếu FAIL 1-4 items → Cảnh báo, tự fill nếu được
   - Generate theo thứ tự BRD → SRS → User Story → Acceptance Criteria (4 tài liệu cốt lõi, `../SKILL.md` mục 3); Feature Map và UAT Plan là tài liệu bổ sung khi dự án cần
   - **Chốt theo tài liệu hoặc theo lát cắt** (`../BA-document-rule/core/slice-baselining.md`): với Tier 2–3 có thể chốt nền chung của BRD trước, rồi đưa từng lát cắt dọc (một luồng/module, đủ BRQ → FR → US → AC) qua gate độc lập; ghi trạng thái trong Sổ lát cắt
   - **Gate nguồn và ký (Hard Gate 7–8):** xem `../SKILL.md` mục 10; AI ghi `Trình duyệt`, chỉ người ký mới chuyển sang `Baseline`
   - Generate supporting artifacts đã chọn ở Step 3, không ép mọi dự án phải có đủ 10 tài liệu mới
   - **Industry Documents (nếu Step 3.5 đã chạy):**
     - 🏛️ Gov → Tích hợp HSMT specs vào SRS phụ lục + Nghiệm thu protocol → UAT
     - 🏥 HC → Tích hợp Clinical Workflow vào Process Flow + PHI NFRs vào SRS + DDI specs
     - 💰 FT → Tích hợp Transaction State Machine vào SRS + AML rules vào Feature Spec
   - **Auto-Diagram:** chọn loại sơ đồ theo `../so_do.md` mục 2. Quy trình nghiệp vụ: BPMN 2.0 (`../so_do.md` mục 4) bằng `../scripts/bpmn_tool.py build diagrams/<tên>.json --png diagrams/<tên>.png`, chèn ảnh kèm liên kết `.bpmn`, chạy `bpmn_tool.py check`. Sơ đồ khác: Mermaid theo khối khai báo chuẩn, chạy `../scripts/diagram_check.py --strict`
   - **Wireframes:** Mermaid mockup cho screens trong Inventory; dùng công cụ thiết kế nếu môi trường có
   - **Requirement Quality Engine (NEW v3.3):**
     - Áp dụng 4 Decomposition Patterns (`../BA-document-rule/core/writing-guide.md` §10)
     - Khám phá NFR qua 7 câu hỏi (`../BA-document-rule/core/nfr-discovery-guide.md`)
     - Phân rã quy trình L0→L3 (`../BA-document-rule/core/process-decomposition-guide.md`)
     - **Automation:** Chạy `../scripts/quality_rubric.py <file-or-project-folder>` để score requirement thực tế
   - **Trọng tâm:** SRS chính xác kỹ thuật; User Story và AC theo góc nhìn người dùng
   - **Inline Audit:** Sau mỗi section, tính điểm 5-point rubric + bắt 8 Smells (`quality_rubric.py`) + rà tay 6 mẫu mâu thuẫn (`writing-guide.md` §12, script không tự phát hiện)

### ✅ VALIDATION (Multi-Layer)

6. **AI Quality Gate & Traceability Audit**
   - Run C-S-K-A Matrix evaluation (`../BA-document-rule/core/evaluation-protocol.md`)
   - **Review độc lập:** đọc toàn bộ ngữ cảnh và rà mâu thuẫn logic trong một lượt riêng
   - Requirement-to-Code Audit nếu project có source code (`../BA-document-rule/core/code-traceability-audit.md`)

6.5. **Pre-Flight Verification (Post-Gen)**
     - Re-run Pre-Flight Checklist cho mỗi document ĐÃ SINH
     - Verify tất cả items PASS sau khi viết (không phải chỉ trước khi viết)
     - **Anti-AI Writing Audit:** Tự rà soát 13 bước Checklist trong `../Anti_ai_writing_rules.md`, bảo đảm output sạch hoàn toàn "mùi AI"
     - Nếu vẫn FAIL → sửa inline → re-verify

6.6. **Sequential Index Validation (NEW v3.4)** ⭐
     - Quét toàn bộ documents ĐÃ SINH để kiểm tra chỉ mục tuần tự:
       - **Heading scan:** §1 → §2 → §3... không nhảy cóc, không lặp, không đảo
       - **Requirement ID scan:** BRQ-ID, FR-ID, NFR-ID, US-ID, AC-ID, TC-ID tuần tự trong cùng prefix
       - **Sub-ID scan:** BRQ-XX.Y tuần tự trong nhóm cha (VD: BRQ-06.1 → .2 → .3)
       - **Test Group scan:** Test Group 2.1 → 2.2 → 2.3... tuần tự
       - **Cross-doc ID consistency:** ID cùng entity phải khớp giữa BRD ↔ SRS ↔ Feature Spec ↔ Story Map ↔ UAT Plan
     - **Gap Types:** `INDEX_SKIP` (nhảy cóc) | `INDEX_DUPLICATE` (lặp) | `HEADING_SKIP` (heading nhảy)
     - Nếu phát hiện gap → chạy `reindex_markdown.py` ở chế độ xem trước. Script chỉ đổi nhóm có lỗ hổng, cập nhật tham chiếu ở mọi file, **bỏ qua tài liệu đã ký** và nhóm có ID trùng (ID trùng sửa tay). Không đánh lại số trong tài liệu khách đã ký: ghi lỗ hổng vào Change Log thay vì đổi ID
     - **Gate Rule:** 0 INDEX_SKIP + 0 INDEX_DUPLICATE + 0 HEADING_SKIP trước khi sang Step 6.7
     - Áp dụng quy tắc chi tiết: `../BA-document-rule/core/writing-guide.md` §1.1 rule 3
     - **Automation:** Ưu tiên chạy `../scripts/reindex_markdown.py <project-folder>` ở chế độ dry-run trước. Nếu kết quả hợp lý mới chạy `--apply`.

6.7. **Cross-Document Traceability Validation (NEW v3.0)**
     - Run `../BA-document-rule/core/traceability-validator.md`
     - **Automation:** Chạy `../scripts/traceability_scan.py <project-folder>` để sinh report markdown/json trước khi kết luận thủ công
     - Scan: BRQ-ID → FR/NFR-ID → Feature-ID → US-ID → AC/TC-ID
     - Với dự án mới, chạy `../scripts/traceability_scan.py <project-folder> --scheme canonical --strict`; strict mode bắt mỗi FR nối trực tiếp tới ≥ 1 US, mỗi US tới ≥ 1 AC/TC, và coi ID sai scheme là lỗi. Thêm `--one-to-one` khi hợp đồng yêu cầu ánh xạ 1:1.
     - Dự án có `ba-scheme.json` (ID riêng): `--scheme project --strict`. Liên kết viết ở dòng dưới định nghĩa (`> Related BRQ-ID: ...`) và ma trận truy vết có cột tên đều được đọc.
     - **Industry Traceability (nếu Gov/HC/FT):**
       - 🏛️ Gov: FR → Regulation (Luật/NĐ/TT) mapping validated
       - 🏥 HC: FR → Clinical Pathway → DDI rule traceability
       - 💰 FT: FR → Transaction State → AML Rule → Recon flow traceability
     - Output: Full Chain Report + Missing Items + Regulatory Gaps (nếu industry)
     - **Gate Rule:** Scanner trả mã 1 (có `ORPHAN_BRQ`, `ORPHAN_BR`, `MISSING_TC`, `MISSING_US_FOR_FR`, `MISSING_AC_FOR_US`, `ORPHAN_NFR`, `STALE_REF`, `OFF_SCHEME_ID` ở strict, ...) → agent PHẢI fix trước khi báo hoàn tất
     - **Gate Rule (Industry):** Nếu có FR chưa map → Regulation → BLOCK until mapped
     - **Review độc lập:** đối chiếu nghĩa giữa các tài liệu (phần scanner không kiểm được)

7. **Impact Analysis & Stakeholder Simulation**
   - Cross-file dependency scan (`../BA-document-rule/core/impact-analysis-guide.md`)
     - Dùng Impact Scoring Matrix + định tuyến Decision Flowchart
   - Tự rà soát từng tài liệu theo vai trò bắt buộc của Tier (`../SKILL.md` mục 6, ý 8; `../BA-document-rule/core/persona-simulation.md`), chạy `persona_review_check.py` cho từng báo cáo
   - Review độc lập theo Tier (H4): Tier 2 một lượt người thật hoặc phiên AI riêng; Tier 3 có ít nhất một người thật ghi tên vào báo cáo
   - Nếu có stakeholder conflict, chạy `../BA-document-rule/core/stakeholder-conflict-resolution.md` để chốt decision owner, conflict log, và artifacts phải cập nhật
   - Cập nhật Risk Register nếu phát hiện risks mới
   - **Decision Analysis (NEW v3.3):** Dùng Weighted Scoring/Decision Tree nếu có 2+ options

7.5 **Communication Packaging (NEW v3.3)**
   - Đóng gói nội dung thành: Executive Summary / Tech Brief / Test Strategy
   - Template: `../BA-document-rule/references/communication-packaging.md`

7.6 **Operational, Data, and Adoption Readiness (NEW)**
   - Nếu có go-live hoặc bàn giao vận hành: verify `operational-readiness-checklist.md`
   - Nếu có báo cáo/KPI/data migration: verify `reporting-specification.md` và `data-governance-plan.md`
   - Nếu có role-sensitive workflow: verify `rbac-matrix.md` khớp SRS/API/UAT
   - Nếu có scope lớn hoặc nhiều assumption: verify `raid-log.md` và đồng bộ Risk Register

### 📊 FINAL REPORT

8. **Final Report**
   - Trạng thái từng tài liệu: Nháp AI / BA đã rà / Trình duyệt / Baseline (ai ký, ngày); bước H1–H6 còn thiếu
   - Scorecard: Điểm Rubric trung bình + C-S-K-A
   - Auto-Generated Diagrams summary
   - Wireframe links (nếu có)
   - Bản Word đã xuất (`md_to_docx.py --template <mẫu khách>`) và cách gửi góp ý (`docx_feedback.py`)
   - Screen Inventory summary
   - Risk Register summary (incl. Response Strategies)
   - Traceability Validation Report (Full Chain + NFR Chain + Gaps)
   - Insight Cards từ Elicitation
   - As-Is → To-Be Gap Analysis summary
   - Supporting Artifacts summary: Business Case / RAID / RBAC / Reporting / Ops / Test / Data Governance nếu có
   - **Communication Packages:** Links tới các bản đóng gói (CEO/Dev)
   - **Industry-Specific Section (nếu Gov/HC/FT):**
     - 🏛️ Gov: Regulatory Compliance Status + HSMT Readiness + ATTT Assessment + Nghiệm thu Plan
     - 🏥 HC: Clinical Validation Status + PHI Compliance + Integration Readiness (HL7/FHIR)
     - 💰 FT: Transaction Integrity Report + AML/KYC Coverage + Reconciliation Readiness + PCI-DSS Status

---

## ⚡ Rollback Paths (Nếu step fail) ⭐ NEW v3.3

> **Nguyên tắc:** Khi step fail → không tiến tiếp. Quay lại step thích hợp để fix.

```
Step 6.7 FAIL (traceability gaps)     → Quay lại Step 5 (bổ sung docs/stories/TCs thiếu)
Step 6.7 FAIL (regulatory gaps)       → Quay lại Step 3.5 (bổ sung Regulatory Mapping) [INDUSTRY]
Step 6.6 FAIL (index gaps)            → Auto-fix re-index → Re-scan. Nếu vẫn FAIL → Quay lại Step 5 (sửa cấu trúc tài liệu)
Step 6.5 FAIL (pre-flight items fail) → Quay lại Step 5 (sửa inline sections)
Step 6 FAIL (C-S-K-A < 7.5)          → Quay lại Step 5 (rewrite sections chất lượng kém)
Step 5 FAIL (pre-flight TRƯỚC doc)    → Quay lại Step 0/2 (bổ sung input từ KH)
Step 4 FAIL (screens không map)       → Quay lại Step 3 (review feature → screen mapping)
Step 3.5 FAIL (industry gate)         → Quay lại Step 0/2 (bổ sung domain expertise) [INDUSTRY]
Step 2.5 FAIL (không có As-Is info)   → Quay lại Step 0 (hỏi KH về quy trình hiện tại)
Gate 8 FAIL (ghi Baseline chưa có ký) → Đổi trạng thái về Trình duyệt; chờ người có thẩm quyền ký
```

**Quy tắc rollback:**
1. **Tối đa 2 lần rollback** cho cùng 1 step — nếu fail lần 3 → escalate cho PM/PO
2. **Ghi nhận mỗi rollback** vào Final Report (số iterations thực tế)
3. **KHÔNG skip step sau khi rollback** — phải re-run từ step quay lại

---

## ⏱ Effort Estimation per Step ⭐ NEW v3.3

> **Hướng dẫn:** Thời gian ước lượng theo kích thước dự án. Dùng để planning sprint BA.

| Step | Tên | S (< 3 sprints) | M (3-8 sprints) | L (> 8 sprints) |
|:---:|---|:---:|:---:|:---:|
| 0 | Elicitation Gate | 2-4 giờ | 1-2 ngày | 2-3 ngày |
| 1 | Risk Scan + Register | 1-2 giờ | 4 giờ | 1 ngày |
| 2 | Customer Intelligence | 2-4 giờ | 1-2 ngày | 2-4 ngày |
| 2.5 | As-Is Process | 1-2 giờ (hoặc N/A) | 4-8 giờ | 1-2 ngày |
| 3 | Project Type Routing | 30 phút | 1 giờ | 2 giờ |
| **3.5** | **Industry Preparation** 🏛️🏥💰 | **2-4 giờ** | **1-2 ngày** | **2-3 ngày** |
| 4 | Screen Inventory | 1-2 giờ | 4-8 giờ | 1-2 ngày |
| 5 | Document Generation | 4-8 giờ | 2-4 ngày | 5-10 ngày |
| 6 | AI Quality Gate | 1-2 giờ | 4 giờ | 1 ngày |
| 6.5 | Pre-Flight Verify | 30 phút | 1-2 giờ | 4 giờ |
| 6.7 | Traceability Validation | 30 phút | 1-2 giờ | 4-8 giờ |
| 7 | Impact & Persona Sim | 1-2 giờ | 4 giờ | 1 ngày |
| 8 | Final Report | 1 giờ | 2-4 giờ | 4-8 giờ |
| | **TỔNG (Generic)** | **~2-3 ngày** | **~1-2 tuần** | **~3-4 tuần** |
| | **TỔNG (Industry +3.5)** | **~3-4 ngày** | **~2-3 tuần** | **~4-5 tuần** |

> **Lưu ý:** Effort Step 5 chiếm 40-50% tổng. Đây là step cần plan kỹ nhất.

---

## Command Usage

```
/ba-workflow [topic] [yêu cầu]
```

### Examples:
```
/ba-workflow QLTS "Xây dựng hệ thống quản lý tài sản bệnh viện"
/ba-workflow HRM-SaaS "Thiết kế nền tảng quản lý nhân sự SaaS"
/ba-workflow "audit" "Chạy traceability validator cho bộ tài liệu hiện tại"

# Industry Examples:
/ba-workflow HIS-BV "Xây dựng HIS cho bệnh viện đa khoa"           → Auto-route: Healthcare
/ba-workflow eWallet "Phát triển ví điện tử thanh toán"              → Auto-route: Fintech
/ba-workflow DVC-TinhX "Cổng dịch vụ công trực tuyến tỉnh X"       → Auto-route: Government
```
