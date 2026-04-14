# PRE-FLIGHT CHECKLIST ENGINE (v3.0)

> **Mục đích:** Agent PHẢI pass checklist trước khi sinh tài liệu. Không pass = Không viết.
> **Trigger:** Tự động kích hoạt TRƯỚC mỗi bước sinh document trong `ba-workflow`.
> **Triết lý:** "Right First Time" — giảm iteration từ 4+ vòng xuống ≤ 2 vòng.

---

## 1. Nguyên tắc Hoạt động

```
INPUT nhận được → Chọn document type → Chạy Pre-Flight Checklist tương ứng
  → PASS ✅ → Tiến hành sinh tài liệu
  → FAIL ❌ → Thông báo user thiếu gì → Yêu cầu bổ sung → Re-check
```

**Quy tắc:**
- Agent KHÔNG ĐƯỢC bỏ qua bất kỳ item nào trong checklist
- Nếu item không áp dụng (N/A), agent phải ghi lý do
- Mỗi item có 3 status: `✅ PASS`, `❌ FAIL`, `⚠️ N/A (lý do)`

---

## 2. Checklist theo Loại Tài liệu

### 📋 PFC-BRD: Pre-Flight cho Business Requirements Document

| # | Check Item | Điều kiện PASS | Nếu FAIL |
|---|------------|----------------|----------|
| 1 | **Glossary/Thuật ngữ** | Có bảng thuật ngữ nghiệp vụ + kỹ thuật + pháp lý (nếu có) | Sinh glossary từ input trước khi viết BRD |
| 2 | **Problem Statement** | Có ≥ 2 vấn đề cụ thể, lượng hóa được | Hỏi user: "Vấn đề cụ thể là gì? Mất bao nhiêu thời gian/tiền?" |
| 3 | **Stakeholder Map** | Có ≥ 3 roles + Pain Points + Expectations | Hỏi user: "Ai sẽ dùng hệ thống? Họ gặp khó khăn gì?" |
| 4 | **OKRs / Success Metrics** | Mỗi OKR có Baseline + Target + Method | Hỏi user: "Hiện tại chỉ số X là bao nhiêu? Mục tiêu?" |
| 5 | **MoSCoW Priority** | Mỗi BRQ phải gán Must/Should/Could/Won't | Tự gán draft MoSCoW → yêu cầu user confirm |
| 6 | **Business Rules** | Có ≥ 1 constraint rule hoặc data validation rule | Hỏi user: "Có ràng buộc nghiệp vụ nào bắt buộc?" |
| 7 | **Assumptions & Constraints** | Có ≥ 3 assumptions + ≥ 2 constraints | Tự suy luận từ context → yêu cầu user confirm |
| 8 | **Traceability Matrix** | Mỗi BRQ có mapping → FR/Feature (dù là placeholder) | Tạo skeleton traceability matrix |
| 9 | **As-Is Process** | Có mô tả quy trình hiện tại HOẶC user xác nhận không có | Hỏi user: "Quy trình hiện tại vận hành thế nào?" |
| 10 | **Elicitation Record** | Có ≥ 1 nguồn input (transcript, file, meeting notes) | Hỏi user câu hỏi elicitation trước khi viết |
| 11 | **Business Rule Architecture** | Nếu có ≥ 5 rules tương tác: có Execution Order + Override Matrix | Hỏi user: "Các quy tắc này có thứ tự ưu tiên? Rule nào ghi đè rule nào?" |
| 12 | **Output Severity Design** | Nếu hệ thống có validation/audit: có bảng severity levels | Tự sinh draft severity table → yêu cầu user confirm |
| 13 | **System Memory Check** | Nếu rules phụ thuộc lịch sử: có bảng System Memory Req | Hỏi: "Quyết định này có phụ thuộc vào dữ liệu đợt trước không?" |
| 14 | **AI Feature Spec** | Nếu có AI/ML features: có `ai-feature-spec.md` hoặc reference | Hướng dẫn user tạo `ai-feature-spec.md` theo template |
| 15 | **Assumption Validation** ⭐ v3.3 | Assumptions có Impact=High phải có Owner + Validate method | Chuyển sang Assumption Register (`writing-guide.md` §13) |
| 16 | **Sequential Numbering** ⭐ v3.4 | BRQ-ID tuần tự không nhảy cóc, không lặp. Sub-ID (BRQ-XX.Y) tuần tự trong nhóm cha. Heading numbering (§1, §2...) liên tục. | Quét toàn bộ → re-index theo `writing-guide.md` §1.1 rule 3 |

### 📋 PFC-SRS: Pre-Flight cho Software Requirements Specification

| # | Check Item | Điều kiện PASS | Nếu FAIL |
|---|------------|----------------|----------|
| 1 | **BRD đã hoàn tất** | BRD đã viết và có traceability matrix | Yêu cầu hoàn tất BRD trước |
| 2 | **Architecture Diagram** | Có sơ đồ kiến trúc tầng (≥ 2 layers) | Sinh Mermaid architecture diagram |
| 3 | **ER Diagram** | Có ERD với ≥ 3 entities + quan hệ | Sinh Mermaid ERD từ BRD requirements |
| 4 | **Use Case Diagram** | Có diagram với ≥ 3 actors + ≥ 5 use cases | Sinh Mermaid Use Case |
| 5 | **State Machine** | Entity có ≥ 3 trạng thái phải có State Diagram | Sinh stateDiagram-v2 |
| 6 | **Data Dictionary** | Mỗi entity chính có table definition (Field, Type, Constraint) | Sinh Data Dictionary skeleton |
| 7 | **API Conventions** | Có Base URL, Auth method, Naming, Pagination standards | Sinh API Conventions section |
| 8 | **Validation Rules** | Mỗi Data Rule trong BRD có regex/range/enum definition | Map DR-xx → validation spec |
| 9 | **NFR Coverage** | Có ≥ 5 NFRs: Performance, Security, Availability, Backup, Accessibility | Check NFR list, bổ sung thiếu — **dùng NFR Discovery 7 câu hỏi** (`nfr-discovery-guide.md`) |
| 10 | **Sequence Diagram** | ≥ 2 luồng phức tạp có Sequence Diagram | Sinh Sequence cho top 2 complex flows |
| 11 | **Decomposition Pattern** ⭐ v3.3 | Mỗi BRQ "Quản lý [X]" đã decompose theo CRUD/Lifecycle/Actor/Integration | Áp dụng `writing-guide.md` §10 → decompose |
| 12 | **Requirement Quality Gate** ⭐ v3.3 | Mọi FR/NFR đạt Rubric ≥ 3/5 (Smell Detector PASS) | Chạy `requirement-quality-rubric.md` → fix smells |
| 13 | **Conflict Scan** ⭐ v3.3 | 0 Contradictory + 0 Overlapping conflicts detected | Chạy 6 Conflict Detection patterns (`writing-guide.md` §12) |
| 14 | **Sequential Numbering** ⭐ v3.4 | FR-ID tuần tự trong mỗi phân hệ. Heading numbering (§1, §2, §2.1...) liên tục. NFR-ID tuần tự. | Quét toàn bộ FR/NFR/heading → re-index |

### 📋 PFC-USM: Pre-Flight cho User Story Map

| # | Check Item | Điều kiện PASS | Nếu FAIL |
|---|------------|----------------|----------|
| 1 | **BRQ Coverage** | 100% BRQ-IDs trong BRD có ≥ 1 User Story | Scan BRD → list missing BRQs → sinh stories |
| 2 | **INVEST Format** | Mỗi story: As a [role], I want [goal], So that [benefit] | Rewrite stories đúng format |
| 3 | **BDD Acceptance Criteria** | Mỗi story có ≥ 1 AC dạng Given/When/Then | Sinh AC cho stories thiếu |
| 4 | **Happy Path + Edge Case** | ≥ 50% stories có cả Happy Path và Edge Case AC | Bổ sung Edge Case AC |
| 5 | **Sprint Assignment** | Mỗi story gán Sprint (S1, S2, S3...) | Tự phân Sprint theo dependency |
| 6 | **Traceability Table** | US → BRQ → FR → TC mapping table | Sinh traceability table |
| 7 | **AC Coverage ≥ 4 Types** ⭐ v3.3 | Must stories có ≥ 4 loại AC (Happy/Negative/Boundary/Permission) | Áp dụng AC Pattern Library (`writing-guide.md` §11) |
| 8 | **Sequential Numbering** ⭐ v3.4 | US-ID tuần tự (US01→US02→US03), EPIC numbering liên tục, AC numbering tuần tự trong mỗi US | Quét toàn bộ US/EPIC → re-index |

### 📋 PFC-UAT: Pre-Flight cho UAT Plan

| # | Check Item | Điều kiện PASS | Nếu FAIL |
|---|------------|----------------|----------|
| 1 | **Story Coverage** | 100% User Stories có ≥ 1 Test Case | Scan Story Map → list missing → sinh TCs |
| 2 | **Test Data Spec** | Có bảng Test Data specification | Sinh test data spec từ Data Dictionary |
| 3 | **Pre-requisites** | Có environment setup + test accounts | Liệt kê pre-requisites |
| 4 | **Sign-off Criteria** | Có ≥ 5 sign-off criteria cụ thể | Sinh sign-off criteria |
| 5 | **Business Rule TCs** | Mỗi Business Rule (Rule-1, Rule-2...) có ≥ 1 TC | Map Rules → TCs |
| 6 | **Sequential Numbering** ⭐ v3.4 | Test Group numbering tuần tự (2.1→2.2→2.3). TC-ID tuần tự trong mỗi group (TC-01-A→TC-01-B). Bảng Sign-off criteria đánh số liên tục. | Quét toàn bộ TG/TC → re-index |

### 📋 PFC-AI: Pre-Flight cho AI/ML Feature Specification ⭐ NEW v3.1

> **Trigger:** Khi dự án có ≥ 1 tính năng AI/ML.
> **Template:** `templates/ai-feature-spec.md`

| # | Check Item | Điều kiện PASS | Nếu FAIL |
|---|------------|----------------|----------|
| 1 | **AI Behavior List** | Mọi AI behavior có ID + Input + Output rõ ràng | Liệt kê behaviors từ BRD requirements |
| 2 | **Accuracy Targets** | Mọi behavior có Precision/Recall/Accuracy target đo được | Hỏi user: "AI sai bao nhiêu % là chấp nhận được?" |
| 3 | **False Pos/Neg Impact** | Đã đánh giá cái nào nguy hiểm hơn: FP hay FN | Phân tích impact và chọn model bias |
| 4 | **Human-in-the-Loop** | Có Confidence matrix + Override flow | Sinh draft confidence matrix |
| 5 | **Training Data** | Đã xác định data source + volume + quality | Hỏi user: "Dữ liệu huấn luyện lấy từ đâu?" |
| 6 | **Knowledge Base** | Nếu có configurable AI: có KB spec (format, CRUD, scope) | Sinh KB template |
| 7 | **Fallback Behaviors** | Mọi failure scenario có fallback action | Liệt kê failure scenarios + fallbacks |
| 8 | **Explainability** | User hiểu được TẠI SAO AI ra kết quả | Thiết kế explanation UI |
| 9 | **Monitoring** | Có production accuracy metrics + degradation alert | Sinh monitoring spec |

---

## 3. Cách Agent Sử Dụng

Khi chuẩn bị sinh tài liệu, agent thực hiện:

```markdown
### 🛫 Pre-Flight Check: [Tên Document]

| # | Item | Status | Ghi chú |
|---|------|--------|---------|
| 1 | Glossary | ✅ PASS | Có trong input PDF |
| 2 | Problem Statement | ✅ PASS | 5 vấn đề đã xác định |
| 3 | Stakeholder Map | ❌ FAIL | Chỉ có 2 roles, cần ≥ 3 |
| ... | ... | ... | ... |

**Kết quả:** 8/10 PASS — Cần bổ sung: Stakeholder Map, As-Is Process
**Hành động:** Hỏi user trước khi tiến hành viết BRD.
```

---

## 4. Escalation Rules

| Số item FAIL | Hành động |
|---|---|
| **0** | ✅ Tiến hành sinh tài liệu ngay |
| **1-2** | ⚠️ Hỏi user bổ sung → tự fill nếu được → tiến hành |
| **3-4** | 🟡 Cảnh báo: "Thiếu nhiều input, output có thể không chính xác" → hỏi user có muốn tiếp? |
| **≥ 5** | 🔴 STOP: "Không đủ input để sinh tài liệu chất lượng. Cần bổ sung X, Y, Z trước." |
