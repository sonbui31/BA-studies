# KHUNG TỔNG THỂ BABOK GUIDE V3

> **Nguồn:** IIBA, *BABOK Guide v3*. Tên Knowledge Area, task và khái niệm theo bản gốc; phần diễn giải và bảng ánh xạ sang BA-agent do dự án viết. Đối chiếu lại với sách gốc khi ôn thi CCBA/CBAP.
> **Đi kèm:** [50-babok-v3-techniques.md](50-babok-v3-techniques.md) (50 kỹ thuật).

---

## 1. Business Analysis Core Concept Model (BACCM)

BACCM có 6 khái niệm. Mỗi artifact BA phải trả lời được ít nhất một khái niệm, và không được mâu thuẫn với các khái niệm còn lại.

| Khái niệm | Câu hỏi | Dấu hiệu bị bỏ sót trong tài liệu |
|---|---|---|
| **Change** | Thay đổi nào đang được thực hiện để đáp ứng nhu cầu? | Tài liệu mô tả tính năng nhưng không nói thay đổi nào ở quy trình hoặc hệ thống |
| **Need** | Vấn đề hoặc cơ hội nào cần giải quyết? | BRD mở đầu bằng giải pháp, không có Problem Statement |
| **Solution** | Giải pháp cụ thể nào đáp ứng nhu cầu? | Giải pháp được chọn không có phương án so sánh |
| **Stakeholder** | Ai liên quan: bị ảnh hưởng, quyết định, hoặc cung cấp thông tin? | Lane BPMN hoặc role trong User Story không có trong Stakeholder Map |
| **Value** | Giá trị và đo bằng gì? | Mục tiêu không có chỉ số, baseline, target |
| **Context** | Môi trường nào ảnh hưởng đến thay đổi? | Thiếu ràng buộc pháp lý, hệ thống cũ, văn hóa tổ chức, thời hạn |

Cách dùng trong dự án: sau khi viết xong BRD hoặc Vision, kiểm tra từng khái niệm có ít nhất một đoạn trả lời. Khái niệm nào trống thì ghi vào Open Questions.

---

## 2. Sáu Knowledge Area và 28 task

### 2.1 Business Analysis Planning and Monitoring

| Task | Nội dung | Tương ứng trong BA-agent |
|---|---|---|
| Plan BA Approach | Chọn phương pháp BA cho dự án | `core/project-classification-gate.md`, overlays |
| Plan Stakeholder Engagement | Cách làm việc với từng stakeholder | Stakeholder Map, `references/communication-packaging.md` |
| Plan BA Governance | Ai quyết định, duyệt, đổi yêu cầu | RACI (`references/raci-matrix.md`), Hard Gates |
| Plan BA Information Management | Lưu trữ, đặt ID, truy vết thông tin BA | Quy ước ID, `core/traceability-validator.md` |
| Identify BA Performance Improvements | Đo và cải tiến cách làm BA | `templates/post-implementation-review.md` |

### 2.2 Elicitation and Collaboration

| Task | Nội dung | Tương ứng |
|---|---|---|
| Prepare for Elicitation | Xác định mục tiêu, nguồn, kỹ thuật, tài liệu chuẩn bị | `references/elicitation-techniques.md`, Bước 1 |
| Conduct Elicitation | Thực hiện phỏng vấn, workshop, quan sát | Socratic Gate, `templates/meeting-minutes.md` |
| Confirm Elicitation Results | Đối chiếu kết quả với stakeholder | Tóm tắt lại bài toán trước khi sang bước sau |
| Communicate BA Information | Chuyển thông tin BA đến đúng người, đúng dạng | Ma trận độc giả trong SKILL.md |
| Manage Stakeholder Collaboration | Duy trì quan hệ và cam kết | `core/stakeholder-conflict-resolution.md` |

### 2.3 Requirements Life Cycle Management

| Task | Nội dung | Tương ứng |
|---|---|---|
| Trace Requirements | Truy vết giữa các yêu cầu | `traceability_scan.py`, quy tắc M1–M7 |
| Maintain Requirements | Giữ yêu cầu đúng, tái sử dụng được | Change Log, `reindex_markdown.py` |
| Prioritize Requirements | Xếp thứ tự theo giá trị, rủi ro, phụ thuộc | MoSCoW, `core/decision-analysis-framework.md` |
| Assess Requirements Changes | Đánh giá tác động khi đổi yêu cầu | `core/impact-analysis-guide.md`, `templates/change-log.md` |
| Approve Requirements | Đạt thỏa thuận và phê duyệt | Human Checkpoints (Duyệt / Sửa / Dừng) |

### 2.4 Strategy Analysis

| Task | Nội dung | Tương ứng |
|---|---|---|
| Analyze Current State | Hiện trạng: tổ chức, năng lực, quy trình, công nghệ | `templates/as-is-process.md` |
| Define Future State | Trạng thái mong muốn, mục tiêu, phạm vi giải pháp | `templates/vision-scope.md`, To-Be |
| Assess Risks | Rủi ro của thay đổi | `templates/risk-register.md`, `raid-log.md` |
| Define Change Strategy | Chiến lược chuyển từ hiện trạng sang tương lai | `templates/business-case.md`, `data-migration-plan.md`, Transition Requirements |

### 2.5 Requirements Analysis and Design Definition

| Task | Nội dung | Tương ứng |
|---|---|---|
| Specify and Model Requirements | Đặc tả và mô hình hóa | BRD, SRS, `so_do.md` |
| Verify Requirements | Yêu cầu đúng chất lượng: rõ, đủ, nhất quán, test được | `requirement-quality-rubric.md`, `quality_rubric.py` |
| Validate Requirements | Yêu cầu thực sự phục vụ mục tiêu kinh doanh | Review với Sponsor, UAT |
| Define Requirements Architecture | Cách các yêu cầu và mô hình khớp nhau | Chuỗi `BRQ → FR/NFR → Feature → US → AC/TC` |
| Define Solution Options | Liệt kê phương án giải pháp | `core/decision-analysis-framework.md` |
| Analyze Potential Value and Recommend Solution | Ước lượng giá trị và đề xuất phương án | `templates/business-case.md` |

### 2.6 Solution Evaluation

| Task | Nội dung | Tương ứng |
|---|---|---|
| Measure Solution Performance | Đo giải pháp đang chạy | `templates/product-analytics-spec.md`, KPI trong BRD |
| Analyze Performance Measures | Hiểu số đo nói gì về giá trị | Báo cáo sau triển khai |
| Assess Solution Limitations | Giới hạn của giải pháp | `templates/post-implementation-review.md` |
| Assess Enterprise Limitations | Giới hạn của tổ chức làm giảm giá trị | Post-implementation review |
| Recommend Actions to Increase Solution Value | Đề xuất hành động nâng giá trị | Change Request, backlog |

Lưu ý: Knowledge Area không phải các bước tuần tự. BABOK v3 nhấn mạnh các task được làm lặp và theo thứ tự tùy bối cảnh. Quy trình 6 bước của BA-agent là một cách tổ chức thực hành, không phải cách đọc chính thức của BABOK.

---

## 3. Phân loại yêu cầu theo BABOK v3

| Loại | Trả lời câu hỏi | Ví dụ |
|---|---|---|
| **Business requirements** | Vì sao tổ chức cần thay đổi? | Giảm 50% cuộc gọi hỏi thông tin |
| **Stakeholder requirements** | Stakeholder cần gì để đạt mục tiêu? | Phụ huynh cần biết con đã đến lớp |
| **Solution requirements: functional** | Giải pháp phải làm gì? | Hệ thống gửi thông báo khi điểm danh |
| **Solution requirements: non-functional** | Giải pháp phải đạt chất lượng nào? | Thông báo đến máy trong 10 giây ở p95 |
| **Transition requirements** | Cần gì để chuyển từ hiện trạng sang giải pháp mới? | Đào tạo giáo viên, chuyển dữ liệu học sinh |

BABOK v3 gom functional và non-functional vào một loại (solution requirements), nên có 4 loại chính. Bảng "5 tầng yêu cầu" ở Bước 1 của SKILL.md tách functional và non-functional ra để theo dõi riêng; hai cách nhìn không mâu thuẫn.

Tầng Stakeholder requirements nằm giữa BRQ và FR. Chuỗi canonical của BA-agent (`BRQ → FR/NFR`) không có mã riêng cho tầng này. Dự án nào cần tầng đó (ví dụ vClassio dùng mã `SR-xx`) phải khai báo theo mục 8 của `BA-document-rule/core/traceability-validator.md`.

---

## 4. Underlying Competencies (6 năng lực nền)

| Năng lực | Nội dung chính |
|---|---|
| Analytical Thinking and Problem Solving | Tư duy sáng tạo, quyết định, học hỏi, giải quyết vấn đề, tư duy hệ thống |
| Behavioral Characteristics | Đạo đức, trách nhiệm cá nhân, đáng tin cậy, tổ chức, thích ứng |
| Business Knowledge | Hiểu ngành, tổ chức, giải pháp, phương pháp luận |
| Communication Skills | Giao tiếp bằng lời và văn bản, lắng nghe |
| Interaction Skills | Điều phối, lãnh đạo, hợp tác, thương lượng, giảng dạy |
| Tools and Technology | Công cụ văn phòng, mô hình hóa, quản lý yêu cầu, cộng tác |

---

## 5. Perspectives (5 góc nhìn bối cảnh)

| Perspective | Trọng tâm | Overlay gần nhất trong dự án |
|---|---|---|
| Agile | Giao theo vòng ngắn, yêu cầu tiến hóa | `overlays/startup-mvp`, `overlays/product` |
| Business Intelligence | Dữ liệu, báo cáo, phân tích | `templates/reporting-specification.md`, `data-governance-plan.md` |
| Information Technology | Phát triển, tích hợp, vận hành hệ thống | `overlays/outsource`, `templates/api-specification.md` |
| Business Architecture | Năng lực, giá trị, cấu trúc tổ chức | `templates/business-case.md` (Capability Analysis) |
| Business Process Management | Quy trình đầu cuối, cải tiến quy trình | `templates/process-flow.md`, `bpmn-modeling-standard.md` |
