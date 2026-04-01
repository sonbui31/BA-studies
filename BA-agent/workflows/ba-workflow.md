---
description: Business Analysis Workflow 3.0 - Multi-LLM Orchestrated with Actionable Gates
---

# BA Workflow Protocol 3.0

This workflow automates BA documentation using the full v3.0 skill suite with **mandatory gates** (Elicitation → As-Is → Pre-Flight → Traceability) to ensure "Right First Time" output.

// turbo-all

## Steps

### 🚪 MANDATORY GATES (Không bỏ qua)

0. **Stakeholder Elicitation Gate (MANDATORY)**
   - Nhận raw input (file PDF/DOC/text/transcript)
   - Sinh Interview Questionnaire theo stakeholder roles (sử dụng `../BA-document-rule/core/customer-intelligence-guide.md`)
   - Yêu cầu user trả lời hoặc cung cấp transcript phỏng vấn
   - Extract: Pain Points, Hidden Needs, Constraints, Assumptions
   - **Output:** Insight Cards + Pain Point Map
   - **Gate Rule:** Nếu user không cung cấp bất kỳ input nào → STOP, không tiếp tục
   - **LLM:** Claude 4.6 — sinh câu hỏi sắc bén, empathetic

1. **Strategic Vision & Risk Register**
   - Identify goals, stakeholders, OKRs
   - **Risk Scan (o4):** Phân tích input → phát hiện patterns rủi ro → sinh Risk Register skeleton
   - Template: `../BA-document-rule/templates/risk-register.md`
   - **LLM:** OpenAI o4 — reasoning edge cases, "What if" scenarios

2. **Customer Intelligence & Deep Elicitation**
   - Run `../BA-document-rule/core/customer-intelligence-guide.md` — deep probing
   - Extract hidden needs, analyze stakeholder psychology, build Insight Cards
   - **LLM:** Claude 4.6 — nuanced analysis, empathetic probing

### 📄 AS-IS DOCUMENTATION (Trước To-Be)

2.5. **As-Is Process Documentation (MANDATORY)**
    - Document quy trình hiện tại TRƯỚC khi viết To-Be
    - Template: `../BA-document-rule/templates/as-is-process.md`
    - **Output:** As-Is Swimlanes + Pain Point Analysis + Gap Analysis + Metrics Baseline
    - **Gate Rule:** Nếu không có thông tin As-Is, hỏi user: "Quy trình hiện tại vận hành thế nào?"
    - Nếu user xác nhận "không có quy trình" (greenfield) → ghi N/A + lý do → tiếp tục

### 📝 GENERATION (Có Pre-Flight)

3. **Initialize Workspace & Template Selection**
   - Chọn overlay: Product / Outsource / In-house / Startup-MVP
   - Map features → success metrics → tracking events
   - Tạo thư mục project nếu chưa có

4. **Screen Inventory (NEW v3.0)**
   - Liệt kê TẤT CẢ screens cần thiết cho dự án
   - Template: `../BA-document-rule/templates/screen-inventory.md`
   - Guide: `../BA-document-rule/core/screen-inventory-guide.md`
   - **Rule:** Mỗi Feature phải có ≥ 1 screen
   - Vẽ Navigation Map (Mermaid)

5. **Document Generation, Auto-Diagram & Visual Prototyping**
   - **⚡ PRE-FLIGHT:** Chạy `../BA-document-rule/core/pre-flight-checklist.md` TRƯỚC mỗi document
     - Nếu FAIL ≥ 5 items → STOP, yêu cầu user bổ sung
     - Nếu FAIL 1-4 items → Cảnh báo, tự fill nếu được
   - Generate BRD → SRS → Feature Spec → Story Map → UAT Plan
   - **Auto-Diagram:** Parse raw input → auto-select diagram type → generate Mermaid
   - **Wireframes:** Generate via `StitchMCP` hoặc Mermaid mockup cho screens trong Inventory
   - **LLM:** GPT-5 — technical SRS drafting | Claude 4.6 — User Stories & AC
   - **Inline Audit:** Sau mỗi major section, nhanh verify C-S-K-A (không chờ cuối)

### ✅ VALIDATION (Multi-Layer)

6. **AI Quality Gate & Traceability Audit**
   - Run C-S-K-A Matrix evaluation (`../BA-document-rule/core/evaluation-protocol.md`)
   - **LLM:** Gemini 3 Pro — full context scan | o4 — logic contradiction check
   - Requirement-to-Code Audit nếu project có source code (`../BA-document-rule/core/code-traceability-audit.md`)

6.5. **Pre-Flight Verification (Post-Gen)**
     - Re-run Pre-Flight Checklist cho mỗi document ĐÃ SINH
     - Verify tất cả items PASS sau khi viết (không phải chỉ trước khi viết)
     - Nếu vẫn FAIL → sửa inline → re-verify

6.7. **Cross-Document Traceability Validation (NEW v3.0)**
     - Run `../BA-document-rule/core/traceability-validator.md`
     - Scan: BRQ-ID → FR-ID → Feature-ID → US-ID → TC-ID
     - Output: Full Chain Report + Missing Items
     - **Gate Rule:** Nếu có ≥ 1 ORPHAN_BRQ hoặc MISSING_TC → agent PHẢI fix trước khi báo hoàn tất
     - **LLM:** Gemini 3 Pro — massive cross-doc scan

7. **Impact Analysis & Stakeholder Simulation**
   - Cross-file dependency scan (`../BA-document-rule/core/impact-analysis-guide.md`)
   - Persona roleplay stress-test (`../BA-document-rule/core/persona-simulation.md`)
   - Cập nhật Risk Register nếu phát hiện risks mới

### 📊 FINAL REPORT

8. **Final v3.0 Report**
   - Scorecard: C-S-K-A per document
   - Auto-Generated Diagrams summary
   - Wireframe Links (StitchMCP)
   - Screen Inventory summary
   - Risk Register summary
   - Traceability Validation Report (Full Chain + Gaps)
   - Insight Cards từ Elicitation
   - As-Is → To-Be Gap Analysis summary

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
```
