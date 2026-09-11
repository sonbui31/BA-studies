# BA Studies

Hệ thống kiến thức và công cụ Business Analysis, được tổ chức thành 3 phần chính.

---

## Cấu trúc repo

```
BA studies/
├── BA-agent/              ← Lõi hệ thống BA Agent (AI trợ lý phân tích nghiệp vụ)
├── projects/              ← Các dự án thực tế / dự án mẫu
├── learning/              ← Tài liệu học tập BA (sách, khóa học, bài tập)
└── BA-WORKFLOW-GUIDE.md   ← Hướng dẫn quy trình xây dựng BA Agent
```

### 📦 [BA-agent/](BA-agent/)

Hệ thống AI Agent đóng vai Business Analyst — thu thập yêu cầu, phân tích nghiệp vụ, sinh tài liệu BRD/SRS/User Story, review và audit chất lượng.

| Thành phần | Mô tả |
|---|---|
| [SKILL.md](BA-agent/SKILL.md) | Entrypoint cho skill system |
| [USER-GUIDE.md](BA-agent/USER-GUIDE.md) | Hướng dẫn sử dụng |
| [DOCUMENT-MAP.md](BA-agent/DOCUMENT-MAP.md) | Bản đồ toàn bộ tài liệu BA |
| [Anti_ai_writing_rules.md](BA-agent/Anti_ai_writing_rules.md) | Bộ quy tắc viết văn chống "mùi AI" (24 Điều cấm & Checklist) |
| [so_do.md](BA-agent/so_do.md) | Quy chuẩn vẽ sơ đồ Mermaid Level 0→3 |
| `agents/` | Agent persona (ba-specialist) |
| `workflows/` | Quy trình BA workflow |
| `scripts/` | 14 scripts tự động: preflight, quality rubric, traceability, knowledge search... |
| `BA-document-rule/` | Bộ rule, template, overlay theo loại dự án |
| `Curated templates/` | Template thực chiến BRD/SRS/User Story |
| `BA-Documents-Outsource/` | Bộ tài liệu mẫu dự án outsource |
| `BA-Documents-Product/` | Bộ tài liệu mẫu dự án product/SaaS |

### 📁 [projects/](projects/)

Dự án thực tế sử dụng BA-agent. Xem [projects/README.md](projects/README.md) để biết chi tiết.

| Dự án | Loại | Mô tả |
|---|---|---|
| QLTS | In-house | Hệ thống Quản lý Tài sản |
| vClassio_app | Product | Ứng dụng VClassio (parent app, teacher app) |
| SaaS-HRM-Platform | Product/SaaS | Nền tảng quản lý nhân sự SaaS |

### 📚 learning/

Thư viện tài liệu học tập BA — sách, khóa học, bài tập, template gốc. *Không được git track (gitignored).*

---

---

# BA-agent: Hướng Dẫn Chat 1-1 Để Làm Business Analysis

Tài liệu này dành cho cách dùng đơn giản nhất: **bạn chat trực tiếp với BA-agent**, không cần nhớ lệnh, không cần chạy code, không cần tự đọc hết template.

Bạn chỉ cần nói rõ mục tiêu, cung cấp thông tin đang có, rồi để BA-agent hỏi tiếp, phân tích, tạo tài liệu, review và chỉ ra gap.

Ba quy tắc mặc định hiện tại:

- **Tài liệu tiếng Việt phải có dấu**. BA-agent không được sinh nội dung kiểu `tieng Viet khong dau`, trừ ID, tên file, code, API path, database field, command, URL.
- Khi viết **BRD, SRS, User Story, Acceptance Criteria**, BA-agent phải tham chiếu `BA-agent/Curated templates/` trước để bám format/ví dụ thực chiến, rồi chuẩn hóa output theo markdown templates và overlay của repo.
- **Văn phong chuẩn xác, cấm "mùi AI"**: Tuân thủ nghiêm ngặt Bộ 24 Điều cấm và Checklist 10 bước trong [Anti_ai_writing_rules.md](BA-agent/Anti_ai_writing_rules.md), cấm từ vựng sáo rỗng, cấu trúc câu dập khuôn, phân tích rỗng và giọng chatbot phục vụ.

Khi bạn muốn BA-agent tự kiểm tra bằng terminal, hãy nói rõ:

```text
Nếu cần kiểm tra bằng script, hãy tự chạy lệnh phù hợp và báo kết quả dễ hiểu cho tôi.
```

Như vậy bạn vẫn chat 1-1, còn các lệnh như search knowledge, preflight, quality rubric, traceability scan sẽ do agent chọn và chạy khi phù hợp.

---

## 1. BA-agent Dùng Để Làm Gì?

`BA-agent` giúp bạn làm các việc BA sau:

- Khai thác yêu cầu từ ý tưởng mơ hồ.
- Xác định stakeholder, pain point, scope, assumption, constraint.
- Viết hoặc review Vision & Scope, BRD, SRS, User Story, UAT, RTM.
- Áp dụng curated templates dạng DOCX/PDF cho BRD, SRS, User Story và Acceptance Criteria.
- Vẽ/đề xuất process flow, BPMN, use case, ERD, user flow.
- Kiểm tra requirement có rõ, testable, traceable không.
- Phân tích impact khi đổi yêu cầu.
- Phân loại dự án trước khi chọn tài liệu, để không bỏ qua Product Vision với product/SaaS/B2B/MVP thương mại hóa.
- Tra cứu kiến thức BA đã được index sẵn từ folder tài liệu cũ.
- Tạo user manual / hướng dẫn sử dụng tiếng Việt dạng Docusaurus 3.10.

Bạn có thể dùng BA-agent như một **BA senior ngồi cùng bàn**, hỏi gì trả lời đó, nhưng vẫn đi theo quy trình chuẩn.

---

## 2. Một Câu Lệnh Duy Nhất — AI Tự Làm Theo Đúng Quy Trình

> Copy prompt dưới đây, thay `[...]`, dán vào chat. AI sẽ tự chạy lần lượt 6 bước theo đúng quy trình trong [BA-WORKFLOW-GUIDE.md](BA-WORKFLOW-GUIDE.md).

```text
Dùng BA-agent cho dự án: [tên dự án].
Mô tả ngắn: [mô tả bạn đang có].

Hãy làm việc với tôi theo kiểu hỏi đáp 1-1, đi theo ĐÚNG 6 bước sau, KHÔNG bỏ bước, KHÔNG viết tài liệu khi chưa đủ input.

═══ BƯỚC 1 — TIẾP NHẬN & LÀM RÕ (Elicitation) ═══
1.1. Hỏi tôi để hiểu: vấn đề hiện tại, mục tiêu, stakeholder, quy trình hiện tại, phạm vi in/out, ràng buộc.
     Nếu thiếu actor, mục tiêu, hoặc điều kiện quan trọng → hỏi lại, KHÔNG đoán.
     Phân loại yêu cầu: tính năng mới / thay đổi quy trình / báo lỗi / tối ưu.

1.2. Lập Stakeholder Map (bắt buộc đủ 6 cột):
     | Stakeholder | Vai trò trong quy trình | Ảnh hưởng (H/M/L) | Quan tâm (H/M/L) | Nhu cầu/kỳ vọng chính | Kênh liên lạc |
     - Liệt kê MỌI bên liên quan, kể cả gián tiếp (compliance, vận hành, support, vendor).
     - Xếp loại theo ma trận Power-Interest (Manage Closely / Keep Satisfied / Keep Informed / Monitor).
     - Nếu thiếu dữ kiện để xếp loại → hỏi lại, KHÔNG tự gán.

1.3. Vẽ BPMN (as-is rồi to-be):
     - Mỗi Lane = 1 stakeholder trong Stakeholder Map (KHÔNG thêm actor lạ).
     - Dùng đúng ký hiệu: Pool, Lane, Start/End Event, Task, Exclusive/Parallel/Inclusive Gateway, Sequence Flow, Message Flow.
     - Nhánh nghiệp vụ chưa rõ → đánh dấu [CẦN XÁC NHẬN] trên Gateway, KHÔNG tự chọn.
     - Đối chiếu ngược: số actor trong BPMN = số stakeholder có vai trò "thực hiện hành động".

═══ BƯỚC 2 — PHÂN TÍCH NGHIỆP VỤ (Analysis) ═══
- Xác định Actor, Trigger, Flow chính, Flow ngoại lệ — đối chiếu trực tiếp với BPMN.
- Mỗi Gateway trong BPMN → ít nhất 1 business rule bằng văn bản.
- Đối chiếu với hệ thống/tài liệu hiện có nếu tôi cung cấp.

═══ BƯỚC 3 — CẤU TRÚC HÓA (Structuring) ═══
- Chuyển thành User Story: "Là [vai trò], tôi muốn [hành động], để [giá trị]."
- Viết Acceptance Criteria theo Given–When–Then.
- Mỗi nhánh Gateway trong BPMN → ít nhất 1 AC.

═══ BƯỚC 4 — KIỂM TRA & ĐỐI CHIẾU CHÉO (Validation) ═══
- Actor trong Stakeholder Map ↔ Lane trong BPMN ↔ vai trò trong User Story PHẢI khớp nhau.
- Liệt kê rõ mọi giả định (assumption) đã tự suy ra, yêu cầu tôi xác nhận.
- Checklist: có actor rõ? có edge case? có mâu thuẫn với rule khác?

═══ BƯỚC 5 — TÀI LIỆU HÓA (Documentation) ═══
- Xuất output theo đúng format: Stakeholder Map (bảng 6 cột), BPMN (text hoặc Mermaid), User Story + AC.
- Gắn version/ngày cập nhật.

═══ BƯỚC 6 — BÀN GIAO & PHẢN HỒI (Handoff) ═══
- Tóm tắt lại toàn bộ để tôi xác nhận trước khi "chốt".
- Nếu tôi chỉnh sửa → cập nhật và ghi nhận thay đổi.

═══ GATE ĐIỀU KIỆN TÀI LIỆU ═══
- KHÔNG viết BRD nếu chưa có Stakeholder Map + BPMN tổng quan + mục tiêu kinh doanh được xác nhận.
- KHÔNG viết SRS nếu BRD chưa được tôi xác nhận "đã chốt".
- KHÔNG viết User Story nếu đoạn BPMN liên quan còn mục [CẦN XÁC NHẬN] chưa xử lý.
- KHÔNG viết AC nếu chưa xác định được nhánh Gateway tương ứng trong BPMN.
- Nếu dự án theo agile, có thể bỏ qua BRD/SRS nhưng vẫn PHẢI có Stakeholder Map + BPMN trước khi viết User Story.

═══ RÀNG BUỘC ═══
- KHÔNG bịa số liệu, KHÔNG tự thêm nghiệp vụ chưa được xác nhận.
- KHÔNG tạo actor/Lane không có trong Stakeholder Map.
- Nếu thông tin mâu thuẫn → nêu rõ mâu thuẫn, KHÔNG tự chọn.
- Tất cả nội dung tiếng Việt phải viết có dấu đầy đủ.
- Khi viết BRD/SRS/User Story/AC → áp dụng Curated templates trước, rồi chuẩn hóa theo markdown templates và overlay.
- Nếu cần tra kiến thức hoặc kiểm tra chất lượng → tự chạy script phù hợp.

Bắt đầu từ Bước 1.1 — hỏi tôi từng nhóm câu hỏi (tối đa 5 câu mỗi lần).
Sau mỗi câu trả lời, tóm tắt hiểu biết hiện tại và nói rõ đang ở bước nào, bước tiếp theo là gì.
```

Ví dụ sử dụng:

```text
Dùng BA-agent cho dự án: Hệ thống quản lý tài sản.
Mô tả ngắn: Công ty muốn quản lý tài sản, cấp phát, thu hồi, kiểm kê và báo cáo.

[... dán toàn bộ prompt trên ...]
```

> **Tip:** Sau khi AI hoàn thành 6 bước, bạn có thể nói thêm: *"Giờ hãy viết BRD"* hoặc *"Giờ hãy viết SRS"* — AI sẽ tự kiểm tra gate điều kiện trước khi viết.

---

## 3. Cách Bắt Đầu Nhanh Nhất

Copy prompt này và thay phần trong ngoặc:

```text
Dùng BA-agent cho dự án: [tên dự án].
Mô tả ngắn: [mô tả bạn đang có].

Hãy làm việc với tôi theo kiểu hỏi đáp 1-1.
Đầu tiên hãy hỏi tôi các câu cần thiết để hiểu problem, stakeholder, scope, quy trình hiện tại và mục tiêu.
Sau khi đủ thông tin, hãy đề xuất bộ tài liệu BA cần tạo.
Nếu cần tra cứu kiến thức hoặc kiểm tra tài liệu bằng script, hãy tự chạy lệnh phù hợp và tóm tắt kết quả cho tôi.
Khi viết BRD/SRS/User Story/AC, hãy áp dụng Curated templates trước rồi mới chuẩn hóa theo markdown templates.
Tất cả nội dung tiếng Việt phải viết có dấu.
```

Ví dụ:

```text
Dùng BA-agent cho dự án: Hệ thống quản lý tài sản.
Mô tả ngắn: Công ty muốn quản lý tài sản, cấp phát, thu hồi, kiểm kê và báo cáo.

Hãy làm việc với tôi theo kiểu hỏi đáp 1-1.
Đầu tiên hãy hỏi tôi các câu cần thiết để hiểu problem, stakeholder, scope, quy trình hiện tại và mục tiêu.
Sau khi đủ thông tin, hãy đề xuất bộ tài liệu BA cần tạo.
Nếu cần tra cứu kiến thức hoặc kiểm tra tài liệu bằng script, hãy tự chạy lệnh phù hợp và tóm tắt kết quả cho tôi.
Khi viết BRD/SRS/User Story/AC, hãy áp dụng Curated templates trước rồi mới chuẩn hóa theo markdown templates.
Tất cả nội dung tiếng Việt phải viết có dấu.
```

---

## 4. Quy Trình Chat Chuẩn

Bạn không cần tự chạy workflow. Chỉ cần yêu cầu BA-agent đi theo các bước này:

```text
1. Hỏi để hiểu bài toán
2. Tóm tắt lại context
3. Xác định loại dự án và add-ons: product/in-house/outsource/startup MVP/AI/reporting/RBAC/data governance
4. Nếu là product/platform/SaaS/app/B2B/commercializable MVP, chốt Product Vision trước Project Charter/BRD
5. Chọn overlay và curated/markdown templates phù hợp
6. Đề xuất bộ tài liệu cần làm theo từng lớp: Product, Business, Process, Requirement, UX, AI/Data, Technical, QA/UAT, Delivery
7. Làm từng tài liệu một
8. Review gap sau mỗi tài liệu
9. Kiểm tra traceability giữa các tài liệu
10. Chốt bản hoàn chỉnh
```

Prompt:

```text
Hãy dẫn tôi đi theo quy trình BA từng bước.
Mỗi lần chỉ hỏi tối đa 5 câu.
Sau mỗi câu trả lời của tôi, hãy cập nhật lại phần hiểu biết của bạn và nói bước tiếp theo.
Khi cần search knowledge, review chất lượng hoặc kiểm tra traceability, hãy tự chạy script phù hợp.
```

Các script BA-agent có thể tự chọn:

| Khi nào | Script phù hợp |
|---|---|
| Cần tra cứu nhanh kiến thức BA | `knowledge_search.py` |
| Cần tra cứu sâu trong knowledge index | `knowledge_index_search.py` |
| Cần kiểm tra tài liệu đủ input chưa | `preflight_check.py` |
| Cần chấm requirement rõ/testable không | `quality_rubric.py` |
| Cần kiểm tra traceability | `traceability_scan.py` |
| Cần kiểm tra/sửa numbering, ID | `reindex_markdown.py` |
| Cần đánh giá câu trả lời/tài liệu đã đủ control theo loại dự án chưa | `ba_response_eval.py` |
| Cần chạy bộ test hành vi BA chuẩn | `eval_golden_cases.py` |
| Cần semantic search bằng embedding thật | `build_semantic_index.py`, `semantic_index_search.py` |
| Cần kiểm tra toàn bộ BA-agent | `ba_bundle_audit.py` |

---

## 5. Chọn Loại Dự Án Bằng Chat

Nếu bạn chưa biết dự án thuộc loại nào, hỏi:

```text
Dựa trên mô tả dự án của tôi, hãy xác định dự án thuộc loại nào: in-house, outsource, product, startup MVP, fintech, healthcare hay government.
Đồng thời xác định các add-ons nếu có: AI/ML, reporting/dashboard, RBAC/phân quyền, data governance/audit.
Nếu có tín hiệu product/platform/SaaS/app/B2B/commercialization, hãy đưa Product Vision Document lên trước Project Charter và BRD.
Giải thích ngắn vì sao và đề xuất bộ tài liệu phù hợp theo từng lớp.
```

Bảng tham khảo:

| Loại | Khi dùng |
|---|---|
| `in-house` | Dự án nội bộ công ty |
| `outsource` | Làm cho client, cần sign-off, hợp đồng, nghiệm thu |
| `product` | SaaS/app/platform, có roadmap, metric, release |
| `startup-mvp` | Cần ra MVP nhanh |
| `fintech` | Ví điện tử, payment, banking, reconciliation |
| `healthcare` | HIS/EMR/LIS, bệnh viện, clinical workflow |
| `government` | Dự án nhà nước, đấu thầu, nghiệm thu nhiều cấp |

Rule quan trọng:

```text
Product Vision không được thay bằng BRD hoặc Project Charter.
Nếu dự án là product/platform/SaaS/app/B2B hoặc MVP có khả năng thương mại hóa,
tài liệu đầu tiên phải là Product Vision Document.
```

---

## 6. Curated Templates Được Dùng Thế Nào?

Folder `BA-agent/Curated templates/` là lớp template thực chiến cho các tài liệu BA lõi:

| File | Vai trò |
|---|---|
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC.docx` | Baseline format, bảng, wording style và ví dụ cho BRD, SRS, User Story, Acceptance Criteria |
| `SRS.pdf` | Reference để đối chiếu độ đầy đủ khi sinh hoặc review SRS |

Khi bạn muốn BA-agent dùng đúng folder này, nói rõ:

```text
Hãy viết tài liệu theo BA-agent và áp dụng Curated templates trước.
Output cuối cùng vẫn là markdown, tuân thủ overlay, numbering, traceability và quality gates của repo.
Tất cả nội dung tiếng Việt phải có dấu.
```

Curated templates không thay thế `BA-document-rule/templates/`. Cách dùng đúng là:

```text
Curated templates         → lấy format/ví dụ/mức chi tiết
BA-document-rule/templates → chuẩn hóa cấu trúc markdown và checklist
BA-document-rule/overlays  → điều chỉnh theo loại dự án
scripts/*                  → kiểm tra chất lượng, numbering, traceability
```

---

## 7. Nếu Bạn Chỉ Có Ý Tưởng Mơ Hồ

Dùng prompt:

```text
Tôi chỉ có ý tưởng sơ bộ sau:
[ghi ý tưởng]

Hãy đóng vai BA và khai thác yêu cầu từ đầu.
Đừng viết tài liệu ngay.
Nếu cần, hãy tự chạy knowledge_search.py hoặc knowledge_index_search.py để lấy checklist/tri thức liên quan trước khi hỏi.
Hãy hỏi tôi từng nhóm câu hỏi về:
1. Vấn đề hiện tại
2. Người dùng/stakeholder
3. Quy trình hiện tại
4. Mục tiêu kinh doanh
5. Phạm vi in/out
6. Dữ liệu và báo cáo
7. Ràng buộc kỹ thuật/thời gian/ngân sách
```

BA-agent nên trả về:

- Pain points.
- Needs.
- Stakeholders.
- Scope.
- Assumptions.
- Constraints.
- Open questions.
- Risks.
- Candidate requirements.

---

## 8. Nếu Bạn Muốn Viết BRD

Prompt:

```text
Dùng BA-agent để viết BRD cho dự án sau:
[mô tả dự án]

Trước khi viết BRD, hãy kiểm tra thông tin đã đủ chưa.
Nếu thiếu, hãy hỏi tôi trước.
Nếu cần, hãy tự chạy knowledge_search.py hoặc knowledge_index_search.py với chủ đề BRD/scope/stakeholder/assumption.
Hãy áp dụng Curated templates cho BRD trước, sau đó chuẩn hóa theo template markdown và overlay phù hợp.
Viết tiếng Việt có dấu đầy đủ.
Khi đủ rồi, hãy viết BRD theo cấu trúc:
1. Executive Summary
2. Background / Problem
3. Business Objectives
4. Stakeholders
5. Scope In / Out
6. Business Requirements
7. Assumptions
8. Constraints
9. Risks
10. Success Metrics
11. Approval / Sign-off
```

Nếu đã có draft BRD:

```text
Đây là BRD draft của tôi:
[dán nội dung]

Hãy review theo vai trò BA senior.
Nếu nội dung nằm trong file/folder, hãy tự chạy preflight_check.py và quality_rubric.py nếu phù hợp.
Chỉ ra:
1. Thiếu thông tin gì
2. Requirement nào mơ hồ
3. Scope nào chưa rõ
4. Assumption/risk nào cần bổ sung
5. Cách sửa cụ thể
```

---

## 9. Nếu Bạn Muốn Viết SRS

Prompt:

```text
Dùng BA-agent để viết SRS cho module:
[tên module]

Input hiện có:
[BRD hoặc mô tả]

Nếu cần, hãy tự chạy knowledge_search.py hoặc knowledge_index_search.py về SRS/FR/NFR/API/data/error handling trước khi viết.
Hãy đối chiếu Curated templates/SRS.pdf và template SRS markdown trước khi viết.
Viết tiếng Việt có dấu đầy đủ.
Hãy hỏi thêm nếu thiếu, sau đó viết SRS gồm:
1. Scope
2. Actors / Roles
3. Functional Requirements
4. Non-functional Requirements
5. Business Rules
6. Data Requirements
7. UI / Screen Behavior
8. API / Integration nếu có
9. Error / Exception Handling
10. Traceability về BRD
```

Yêu cầu thêm:

```text
Mỗi requirement phải có ID, actor, trigger, expected result và acceptance hint.
Không dùng từ mơ hồ như "nhanh", "dễ dùng", "linh hoạt" nếu không có metric.
```

---

## 10. Nếu Bạn Muốn Viết User Story

Prompt:

```text
Dựa trên feature sau:
[mô tả feature]

Nếu cần, hãy tự tra knowledge về User Story/Acceptance Criteria/INVEST trước khi viết.
Hãy áp dụng Curated templates cho User Story/Acceptance Criteria trước khi sinh output.
Viết tiếng Việt có dấu đầy đủ.
Hãy tạo User Story Map gồm:
1. Activities
2. Tasks
3. User Stories
4. Acceptance Criteria theo Given-When-Then
5. Priority MoSCoW
6. Mapping về requirement ID nếu có
```

Yêu cầu chất lượng:

```text
Mỗi story phải đạt INVEST.
Acceptance Criteria phải có happy path, negative path, boundary case và permission case nếu phù hợp.
```

---

## 11. Nếu Bạn Muốn Làm UAT Và RTM

Prompt:

```text
Dựa trên các requirement/user stories sau:
[dán nội dung]

Nếu cần, hãy tự tra knowledge về UAT/RTM và chạy traceability_scan.py nếu có folder tài liệu.
Hãy tạo UAT Plan và RTM.
UAT cần có:
1. Entry Criteria
2. Exit Criteria
3. Test Scenarios
4. Test Data
5. Expected Result
6. Evidence cần thu thập
7. Defect handling
8. Sign-off

RTM cần trace:
BRQ -> FR/NFR -> Feature -> User Story -> Test Case
```

Nếu muốn review traceability:

```text
Hãy kiểm tra traceability trong nội dung sau.
Chỉ ra requirement nào chưa có FR, story nào chưa có test case, NFR nào chưa có cách kiểm thử.
```

---

## 12. Nếu Bạn Muốn Vẽ Quy Trình / Diagram

Prompt:

```text
Dựa trên quy trình sau:
[mô tả quy trình]

Nếu cần, hãy tự tra knowledge về BPMN/UML/DFD/ERD để chọn đúng loại diagram.
Hãy đề xuất loại diagram phù hợp nhất.
Sau đó tạo:
1. As-Is process
2. Pain points / gaps
3. To-Be process
4. Business rules tại các decision points
5. Exception flows
```

Nếu muốn Mermaid:

```text
Hãy vẽ quy trình trên bằng Mermaid.
Dùng swimlane nếu có nhiều actor/phòng ban.
```

Chọn diagram:

| Cần hiểu gì | Diagram phù hợp |
|---|---|
| Ai dùng hệ thống | Use Case / Context Diagram |
| Quy trình chạy thế nào | BPMN / Activity / Swimlane |
| Dữ liệu đi đâu | DFD |
| Dữ liệu lưu thế nào | ERD |
| Thành phần gọi nhau thế nào | Sequence Diagram |
| Trạng thái thay đổi thế nào | State Diagram |
| Màn hình đi như nào | User Flow / Screen Inventory |

---

## 13. Nếu Dự Án Có AI / ML

Prompt:

```text
Dùng BA-agent để đặc tả AI/ML feature sau:
[mô tả tính năng]

Nếu cần, hãy tự tra knowledge về AI/ML feature spec, confidence, fallback và monitoring trước khi viết.
Hãy tạo AI Feature Spec gồm:
1. Business Objective
2. Input Data / Source
3. Output
4. Model behavior
5. Confidence threshold
6. Acceptable error
7. Human review
8. Fallback khi AI không chắc
9. Monitoring
10. UAT scenarios
11. Risks: bias, privacy, hallucination, wrong prediction
```

Ví dụ:

```text
Tính năng: AI tự tạo bài học, quiz và bài thi từ tài liệu nội bộ công ty.
```

---

## 14. Nếu Dự Án Có Data / Report / Dashboard

Prompt:

```text
Dự án có báo cáo/dashboard sau:
[mô tả]

Nếu cần, hãy tự tra knowledge về reporting spec, KPI, data governance và data dictionary.
Hãy tạo Reporting Specification gồm:
1. Danh sách report/dashboard
2. KPI/metric definition
3. Formula
4. Data source
5. Filter
6. Refresh frequency
7. Permission
8. Export
9. Data quality checks
```

Nếu có data model:

```text
Hãy tạo Data Dictionary cho các entity sau:
[danh sách entity hoặc mô tả dữ liệu]

Mỗi field cần có:
field name, type, required, validation rule, source, owner, sensitivity.
```

---

## 15. Nếu Dự Án Là Outsource

Prompt:

```text
Dự án này là outsource/client-vendor.
Hãy áp dụng quy tắc BA cho outsource.
Tôi cần bộ tài liệu có thể sign-off và quản lý scope.

Nếu cần, hãy tự tra knowledge về outsource, sign-off, UAT, Change Request và handover.
Hãy đề xuất:
1. Tài liệu cần tạo
2. Thứ tự tạo
3. Điểm cần sign-off
4. Cách quản lý Change Request
5. Cách chuẩn bị UAT và handover
```

Bộ tài liệu thường dùng:

```text
Vision & Scope
BRD
Stakeholder Map
Process Flow
Feature Map
SRS
User Story Map
Data Model
UAT Plan
Change Log
Meeting Minutes
Handover Checklist
```

---

## 16. Nếu Dự Án Là Product / SaaS

Prompt:

```text
Dự án này là product/SaaS.
Hãy áp dụng tư duy Product BA.

Nếu cần, hãy tự tra knowledge về product discovery, persona, user flow, analytics và beta testing.
Hãy giúp tôi xác định:
1. Product Vision
2. Target users và buyer nếu khác nhau
3. Persona
4. Pain points
5. Product hypothesis
6. Differentiator / value proposition
7. Success metrics
8. User flow
9. Analytics events
10. MVP scope
11. Release plan
12. Feedback loop
```

Bộ tài liệu thường dùng:

```text
Product Vision Document / Vision & Scope
BRD nhẹ
User Personas
User Flow
Feature Map
SRS Lite nếu cần
User Story Map
Data Model
Beta Testing Plan
Release Notes
```

Nếu product/SaaS có hướng bán B2B hoặc thương mại hóa, thứ tự tối thiểu nên là:

```text
1. Product Vision Document
2. Product Strategy/Roadmap nếu cần
3. Project Charter
4. BRD nhẹ
5. Scope In/Out
6. User Story Map + Product Backlog
```

---

## 17. Nếu Dự Án Thuộc Domain Đặc Thù

### Fintech / Banking / Payment

```text
Dự án thuộc fintech/payment.
Hãy kiểm tra thêm các khía cạnh:
transaction state, reconciliation, AML/KYC, audit trail, fraud/risk, privacy, role approval.
```

### Healthcare

```text
Dự án thuộc healthcare.
Hãy kiểm tra thêm:
clinical workflow, PHI/PII, consent, HL7/FHIR nếu có, clinical validation, multi-level acceptance.
```

### Government

```text
Dự án thuộc government/public sector.
Hãy kiểm tra thêm:
procurement, regulatory compliance, multi-level acceptance, security classification, audit evidence.
```

---

## 18. Cách Yêu Cầu BA-agent Review

Prompt review chung:

```text
Hãy review nội dung sau như BA senior.
Ưu tiên phát hiện bug/gap/risk hơn là khen.
Nếu nội dung nằm trong file/folder, hãy tự chạy preflight_check.py, quality_rubric.py hoặc traceability_scan.py khi phù hợp.

Hãy trả lời theo format:
1. Critical gaps
2. Major gaps
3. Minor gaps
4. Missing questions
5. Suggested fixes
6. Revised version nếu cần

Nội dung:
[dán tài liệu]
```

Prompt review requirement:

```text
Hãy chấm các requirement sau theo tiêu chí:
atomic, unambiguous, testable, traceable, feasible, valuable.
Chỉ ra requirement nào mơ hồ, thiếu actor, thiếu condition, thiếu metric, hoặc không test được.
```

Prompt review traceability:

```text
Hãy kiểm tra traceability:
BRQ -> FR/NFR -> Feature -> US -> TC.
Chỉ ra orphan, missing link và cách sửa.
```

---

## 19. Cách Làm Việc Từng Bước Với BA-agent

Nếu muốn BA-agent không viết quá nhanh, dùng prompt:

```text
Làm từng bước với tôi.
Không viết tài liệu hoàn chỉnh ngay.
Mỗi lần chỉ:
1. Tóm tắt hiểu biết hiện tại
2. Hỏi tối đa 5 câu tiếp theo
3. Nói rõ sau câu trả lời của tôi sẽ làm gì
```

Nếu muốn BA-agent tự đề xuất bước tiếp theo:

```text
Dựa trên thông tin hiện tại, hãy nói tôi đang ở phase nào của BA workflow,
thiếu gì, và bước tiếp theo nên làm gì.
```

---

## 20. Khi Nào Mới Cần Chạy Script?

Bạn **không bắt buộc tự chạy script** nếu chỉ muốn chat 1-1.

Script chỉ cần khi:

- Muốn audit tự động cả thư mục tài liệu.
- Muốn scan traceability bằng máy.
- Muốn chấm requirement hàng loạt.
- Muốn rebuild knowledge index.

Nếu cần, bạn có thể bảo BA-agent tự chạy:

```text
Hãy tự chạy các script kiểm tra cần thiết cho folder này và báo kết quả dễ hiểu.
```

Ví dụ prompt hybrid:

```text
Dùng BA-agent review folder BA-Documents-Outsource.
Hãy tự chạy các lệnh phù hợp để:
1. Kiểm tra preflight
2. Chấm quality rubric
3. Scan traceability
4. Báo lỗi theo Critical/Major/Minor

Tôi không cần xem raw terminal log, chỉ cần kết luận và cách sửa.
```

```text
Dùng BA-agent viết SRS cho module Quản lý tài sản.
Trước khi viết, hãy tự tra knowledge liên quan bằng script nếu cần.
Sau khi viết xong, hãy tự chạy quality_rubric.py trên file/tài liệu nếu có thể.
```

```text
Dùng BA-agent kiểm tra traceability cho bộ tài liệu này.
Hãy tự chạy traceability_scan.py nếu có folder tài liệu.
Nếu không chạy được, hãy kiểm tra thủ công từ nội dung tôi dán.
```

Các script chính mà BA-agent có thể tự chạy:

```powershell
python .\scripts\knowledge_search.py "topic" --format markdown
python .\scripts\knowledge_index_search.py "deep query" --format markdown --limit 5
python .\scripts\preflight_check.py <project-folder>
python .\scripts\quality_rubric.py <project-folder-or-file>
python .\scripts\traceability_scan.py <project-folder>
```

Quy tắc trao đổi:

- Bạn chỉ cần yêu cầu mục tiêu.
- BA-agent tự chọn script nếu có lợi.
- BA-agent không cần show toàn bộ output terminal.
- BA-agent phải tóm tắt kết quả bằng ngôn ngữ BA dễ hiểu.
- Nếu script fail, BA-agent phải nói rõ fail ở đâu và chuyển sang kiểm tra thủ công nếu có thể.

---

## 21. Câu Lệnh Chat Mẫu Hay Dùng Nhất

### Bắt đầu dự án

```text
Dùng BA-agent cho dự án [tên].
Hãy hỏi tôi để khai thác yêu cầu từ đầu.
```

### Đề xuất tài liệu cần tạo

```text
Dựa trên mô tả này, hãy đề xuất bộ tài liệu BA cần tạo, thứ tự tạo và lý do.
```

### Viết tài liệu

```text
Hãy viết [BRD/SRS/UAT/User Story Map] cho nội dung sau.
Nếu thiếu thông tin, hỏi tôi trước.
Nếu là BRD/SRS/User Story/AC, hãy áp dụng Curated templates và viết tiếng Việt có dấu.
```

### Review tài liệu

```text
Hãy review tài liệu sau như BA senior, chỉ ra gap và cách sửa.
```

### Kiểm tra yêu cầu

```text
Hãy kiểm tra các requirement sau có rõ, testable và traceable không.
```

### Tạo câu hỏi phỏng vấn

```text
Hãy tạo bộ câu hỏi phỏng vấn stakeholder cho dự án này.
Chia theo từng vai trò.
```

### Tóm tắt và bước tiếp theo

```text
Hãy tóm tắt những gì đã biết, những gì còn thiếu, và đề xuất bước tiếp theo.
```

---

## 22. Tạo User Manual / Hướng Dẫn Sử Dụng

BA-agent có thể tạo bộ tài liệu hướng dẫn sử dụng tiếng Việt cho ứng dụng thật, xuất ra Docusaurus 3.10 site có screenshot, phân quyền, trang Home giới thiệu sản phẩm và audit chất lượng trước bàn giao.

### Bắt đầu tạo manual

```text
Dùng BA-agent để tạo user manual tiếng Việt cho ứng dụng sau:
[tên app, URL hoặc mô tả]

Hãy khám phá app, chụp screenshot, map role/permission,
rồi tạo Docusaurus site có sidebar, search và trang Home giới thiệu sản phẩm.
Tất cả nội dung tiếng Việt phải có dấu.
```

### Chuyển tài liệu cũ sang Docusaurus

```text
Tôi có tài liệu hướng dẫn sử dụng cũ ở:
[đường dẫn hoặc dán nội dung]

Hãy chuyển sang Docusaurus 3.10 với sidebar, screenshot, phân quyền và trang Home.
Deploy lên GitHub Pages repo: [owner/repo].
```

### Audit manual trước bàn giao

```text
Hãy chạy audit cho bộ manual ở folder [đường dẫn].
Kiểm tra link hỏng, ảnh thiếu, placeholder chưa thay, dữ liệu nhạy cảm, cú pháp admonition và baseUrl.
```

---

## 23. Ghi Nhớ Ngắn Gọn

Bạn có thể dùng BA-agent chỉ bằng một câu:

```text
Dùng BA-agent để dẫn tôi làm BA cho dự án này từ đầu đến cuối, hỏi từng bước và chỉ tạo tài liệu khi đủ thông tin.
```

Quy trình nhớ nhanh:

```text
Hỏi → Hiểu problem → Phân loại dự án → Chọn overlay/template → Chốt Vision nếu là product → Chốt scope → Viết tài liệu có dấu → Review gap → Traceability → Sign-off
```

Nguyên tắc quan trọng nhất:

```text
Đừng để BA-agent viết tài liệu ngay khi input còn mơ hồ.
Hãy bắt nó hỏi, tóm tắt, xác nhận rồi mới viết.
```
