# 50 KỸ THUẬT PHÂN TÍCH NGHIỆP VỤ TRONG BABOK GUIDE V3

> **Nguồn:** IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK Guide) v3*, chương 10 "Techniques". Tên kỹ thuật theo bản gốc; mô tả và cột "Artifact trong BA-agent" do dự án viết.
> **Cách nhóm:** IIBA liệt kê 50 kỹ thuật theo thứ tự chữ cái và không chia nhóm. Bốn nhóm dưới đây (9 / 17 / 8 / 16) là cách sắp xếp của dự án để tra cứu theo mục đích, không phải cấu trúc chính thức của IIBA.
> **Khung tổng thể** (6 Knowledge Area, BACCM, Underlying Competencies, Perspectives): xem [babok-v3-framework.md](babok-v3-framework.md).
> **Lưu ý khi ôn CCBA/CBAP:** đối chiếu lại với bản BABOK v3 chính thức; bảng này là tóm tắt thực hành, không thay thế sách gốc.

---

## 1. Danh mục 50 kỹ thuật theo nhóm mục đích

### Nhóm A: Khơi gợi và cộng tác (9 kỹ thuật)

| # | Kỹ thuật | Mục đích | Khi nào dùng | Artifact trong BA-agent |
|:-:|---|---|---|---|
| 1 | Brainstorming | Sinh nhiều ý tưởng trong thời gian ngắn, chưa đánh giá | Tìm giải pháp, phá điểm nghẽn | Danh sách ý tưởng đã gom nhóm |
| 2 | Collaborative Games | Dùng trò chơi có luật (Product Box, Speed Boat) để khơi gợi | Stakeholder ngại nói trong họp thường | Danh sách pain/gain ưu tiên |
| 3 | Document Analysis | Đọc tài liệu, quy trình, chính sách, hợp đồng hiện có | Đầu dự án, trước khi phỏng vấn | `templates/as-is-process.md` |
| 4 | Focus Groups | Lấy ý kiến một nhóm đại diện về sản phẩm hoặc tính năng | Khám phá nhu cầu thị trường | `templates/user-research-plan.md` |
| 5 | Interviews | Hỏi trực tiếp 1-1 hoặc nhóm nhỏ | Cần hiểu sâu nhu cầu, quy tắc ngầm | `templates/meeting-minutes.md` |
| 6 | Mind Mapping | Vẽ sơ đồ tư duy để gom ý và quan hệ giữa các chủ đề | Làm rõ phạm vi ban đầu, ghi chú buổi họp | Sơ đồ tư duy |
| 7 | Observation | Quan sát người làm việc thật (chủ động hoặc thụ động) | Quy trình thủ công có luật ngầm | Ghi chú quan sát cho As-Is |
| 8 | Survey or Questionnaire | Thu thập dữ liệu có cấu trúc từ nhiều người | Cần số liệu từ nhóm đông, không họp được | Kết quả khảo sát |
| 9 | Workshops | Họp có điều phối để thống nhất yêu cầu giữa nhiều bên | Stakeholder xung đột, cần chốt phạm vi nhanh | Biên bản workshop, decision log |

### Nhóm B: Mô hình hóa và đặc tả (17 kỹ thuật)

| # | Kỹ thuật | Mục đích | Khi nào dùng | Artifact trong BA-agent |
|:-:|---|---|---|---|
| 10 | Business Rules Analysis | Xác định, diễn đạt và quản lý quy tắc nghiệp vụ | Chính sách, điều kiện duyệt, công thức tính | Danh mục `BR-*` |
| 11 | Concept Modelling | Định nghĩa khái niệm nghiệp vụ và quan hệ giữa chúng | Thống nhất thuật ngữ trước khi làm ERD | Mô hình khái niệm, Glossary |
| 12 | Data Dictionary | Mô tả từng phần tử dữ liệu: kiểu, độ dài, quy tắc | Bàn giao cho dev và DBA | `templates/data-model.md` |
| 13 | Data Flow Diagrams | Dữ liệu đi qua tiến trình và kho lưu trữ nào | Phân tích điểm vào/ra, tích hợp | DFD cấp 0, cấp 1 |
| 14 | Data Modelling | Thực thể, thuộc tính, quan hệ (ERD) | Thiết kế dữ liệu | ERD trong SRS |
| 15 | Decision Modelling | Biểu diễn logic ra quyết định phức tạp (decision table, decision tree) | Quy tắc nhiều điều kiện chồng nhau | Decision table trong SRS |
| 16 | Glossary | Danh sách thuật ngữ và định nghĩa dùng chung | Mọi dự án có thuật ngữ ngành | `core/glossary.md`, mục Từ điển trong BRD |
| 17 | Interface Analysis | Xác định điểm giao tiếp giữa hệ thống, người, thiết bị | Tích hợp cổng thanh toán, ERP, CRM | `templates/api-specification.md` |
| 18 | Organizational Modelling | Cơ cấu tổ chức, vai trò, tuyến báo cáo | Xác định ai chịu ảnh hưởng | Org chart, Stakeholder Map |
| 19 | Process Modelling | Biểu diễn quy trình bằng BPMN hoặc flowchart | As-Is, To-Be | `templates/process-flow.md`, `bpmn-modeling-standard.md` |
| 20 | Prototyping | Bản mẫu để người dùng thử và góp ý | Người dùng khó mô tả mong muốn | Wireframe, clickable prototype |
| 21 | Roles and Permissions Matrix | Ai được làm gì trên chức năng và dữ liệu nào | Hệ thống có phân quyền | `templates/rbac-matrix.md` |
| 22 | Scope Modelling | Vẽ ranh giới phạm vi (context diagram, use case diagram, feature tree) | Chốt In/Out Scope | Context diagram (Level 0) |
| 23 | Sequence Diagrams | Thứ tự thông điệp giữa các thành phần theo thời gian | API, microservice, xử lý bất đồng bộ | Sequence trong SRS (Level 3) |
| 24 | State Modelling | Vòng đời và điều kiện chuyển trạng thái của một đối tượng | Đơn hàng, đơn nghỉ phép, ticket | State diagram trong SRS |
| 25 | Use Cases and Scenarios | Tương tác giữa actor và hệ thống để đạt một mục tiêu | Đặc tả chức năng, nền cho kiểm thử | Use Case trong SRS |
| 26 | User Stories | Yêu cầu từ góc nhìn người dùng: ai, muốn gì, để làm gì | Agile/Scrum | `Curated templates/03-User-Story-Template.md` |

### Nhóm C: Chiến lược và tài chính (8 kỹ thuật)

| # | Kỹ thuật | Mục đích | Khi nào dùng | Artifact trong BA-agent |
|:-:|---|---|---|---|
| 27 | Balanced Scorecard | Đo hiệu quả theo 4 góc nhìn: tài chính, khách hàng, quy trình, học hỏi | Gắn dự án với chiến lược tổ chức | Scorecard trong Business Case |
| 28 | Benchmarking and Market Analysis | So sánh với đối thủ và chuẩn ngành | Xác định tính năng tạo khác biệt | Báo cáo đối sánh |
| 29 | Business Capability Analysis | Đánh giá năng lực cốt lõi cần có hoặc cần bổ sung | Chuyển đổi số, tái cấu trúc | Capability map |
| 30 | Business Cases | Giải trình chi phí, lợi ích, rủi ro để xin duyệt | Xin ngân sách, Go/No-Go | `templates/business-case.md` |
| 31 | Business Model Canvas | 9 khối của mô hình kinh doanh | Sản phẩm mới, đổi mô hình | Canvas trong Vision |
| 32 | Financial Analysis | Phân tích tài chính của phương án (NPV, IRR, payback, ROI) | So sánh phương án đầu tư | Bảng tài chính trong Business Case |
| 33 | SWOT Analysis | Điểm mạnh, yếu, cơ hội, thách thức | Khởi đầu chiến lược sản phẩm | Ma trận SWOT trong Vision |
| 34 | Vendor Assessment | Chấm điểm nhà cung cấp theo tiêu chí có trọng số | Quyết định mua hay tự xây | `core/decision-analysis-framework.md` |

### Nhóm D: Phân tích, ra quyết định và quản trị yêu cầu (16 kỹ thuật)

| # | Kỹ thuật | Mục đích | Khi nào dùng | Artifact trong BA-agent |
|:-:|---|---|---|---|
| 35 | Acceptance and Evaluation Criteria | Tiêu chí để chấp nhận yêu cầu hoặc đánh giá giải pháp | Nghiệm thu, DoD | `Curated templates/04-Acceptance-Criteria-Template.md` |
| 36 | Backlog Management | Ghi nhận, làm mịn, xếp thứ tự công việc | Scrum/Kanban | Product Backlog |
| 37 | Data Mining | Khai phá dữ liệu để tìm quy luật, bất thường | Phát hiện gian lận, dự báo | Báo cáo phân tích |
| 38 | Decision Analysis | Chọn phương án bằng tiêu chí có trọng số | Chọn kiến trúc, công nghệ, phương án | `core/decision-analysis-framework.md` |
| 39 | Estimation | Dự đoán nỗ lực, thời gian, chi phí | Lập kế hoạch, báo giá | [requirements-estimation-guide.md](requirements-estimation-guide.md) |
| 40 | Functional Decomposition | Chia chức năng lớn thành phần nhỏ hơn | Quản lý phạm vi, WBS | Feature Map (`04A-Feature-Map.md`) |
| 41 | Item Tracking | Theo dõi vấn đề, rủi ro, quyết định, hành động | Vận hành dự án hằng ngày, UAT | `templates/raid-log.md` |
| 42 | Lessons Learned | Rút bài học từ dự án hoặc giai đoạn | Cuối sprint, cuối dự án | `templates/post-implementation-review.md` |
| 43 | Metrics and Key Performance Indicators (KPIs) | Chỉ số đo thành công của giải pháp | Đánh giá sau triển khai | `templates/product-analytics-spec.md` |
| 44 | Non-Functional Requirements Analysis | Phân tích yêu cầu chất lượng: hiệu năng, bảo mật, sẵn sàng | Mọi SRS | `core/nfr-discovery-guide.md` |
| 45 | Prioritization | Xếp thứ tự yêu cầu (MoSCoW, value/effort, Kano, voting) | Quá nhiều yêu cầu, ngân sách giới hạn | MoSCoW trong BRD |
| 46 | Process Analysis | Tìm điểm nghẽn, lãng phí, cơ hội cải tiến trong quy trình | Sau As-Is, trước To-Be | Pain point map |
| 47 | Reviews | Rà soát tài liệu hoặc sản phẩm (inspection, walkthrough, peer review) | Trước khi chốt tài liệu | `core/quality-checklist.md` |
| 48 | Risk Analysis and Management | Nhận diện, đánh giá, ứng phó rủi ro | Toàn vòng đời dự án | `templates/risk-register.md` |
| 49 | Root Cause Analysis | Tìm nguyên nhân gốc (5 Whys, Fishbone) | Lỗi lặp lại, quy trình nghẽn | Fishbone, 5 Whys |
| 50 | Stakeholder List, Map, or Personas | Liệt kê, phân tích, mô tả stakeholder và người dùng | Đầu dự án | `templates/stakeholder-map.md`, `03-Stakeholder-Map.md` |

---

## 2. Kỹ thuật ngoài danh sách 50 của BABOK v3 mà dự án vẫn dùng

Các kỹ thuật này phổ biến trong thực hành nhưng **không nằm** trong 50 kỹ thuật của BABOK v3. Không dùng chúng khi trả lời câu hỏi thi theo BABOK.

| Kỹ thuật | Ghi chú |
|---|---|
| Gap Analysis | Có trong thực hành và trong các bản BABOK cũ; BABOK v3 xử lý gián tiếp qua Strategy Analysis (phân tích hiện trạng và trạng thái tương lai). |
| Kano Model | Công cụ phân loại tính năng, thường dùng bên trong Prioritization. |
| Decision Tree | Một dạng của Decision Modelling / Decision Analysis. |
| Dependency Modelling | Bảng hoặc đồ thị phụ thuộc giữa yêu cầu; thực hành Agile và quản lý dự án. |
| Social Media Analysis | Dạng riêng của Data Mining / Survey; không phải kỹ thuật riêng của BABOK v3. |
| Data Migration Planning | Hoạt động Transition Requirements, xem `templates/data-migration-plan.md`. |
| Requirements Workshop | Tên cũ ở BABOK v2; trong v3 gộp vào Workshops. |
| Problem Tracking | Tên cũ ở BABOK v2; v3 gọi là Item Tracking. |

---

## 3. 14 chiến lược ghi nhớ

1. **Grouping:** nhớ theo 4 nhóm mục đích (9 / 17 / 8 / 16) thay vì 50 tên rời.
2. **Chunking:** chia 5 tuần, mỗi tuần 10 kỹ thuật.
3. **Flashcards:** mặt trước ghi tên kỹ thuật; mặt sau ghi mục đích, khi nào dùng, đầu ra.
4. **Mind map:** nối 50 kỹ thuật vào 6 Knowledge Area (xem [babok-v3-framework.md](babok-v3-framework.md)).
5. **Gắn vào một dự án thật:** đi từ SWOT và Business Case, qua Interviews và Observation, Process Modelling và Use Cases, Prototyping, đến Acceptance Criteria.
6. **Áp dụng:** dùng mỗi kỹ thuật ít nhất một lần trong tài liệu thật.
7. **Dạy lại (Feynman):** giải thích một kỹ thuật cho người khác trong 3 phút.
8. **Mnemonics:** ghép chữ cái đầu của từng nhóm thành từ khóa.
9. **Acrostics:** đặt câu ngắn từ chữ cái đầu các kỹ thuật trọng tâm.
10. **Ôn ngắt quãng:** ngày 1, 3, 7, 30.
11. **Liên tưởng đời thường:** Observation giống quan sát giao thông trước khi đặt đèn đỏ; Functional Decomposition giống tháo xe máy thành phụ tùng.
12. **Đa giác quan:** đọc, vẽ tay, nói to định nghĩa.
13. **Đề tình huống:** làm câu hỏi chọn kỹ thuật theo bối cảnh kiểu CCBA/CBAP.
14. **Anki:** nạp 50 thẻ để lặp lại ngắt quãng.
