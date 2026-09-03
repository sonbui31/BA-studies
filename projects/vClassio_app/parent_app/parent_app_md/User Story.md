# User Story

## PARENT MOBILE APP

User Story & Acceptance Criteria

Version: 1.1

Author: Bùi Ngọc Sơn (BA)

Date: 23-07-2026

Nguồn gốc: cụ thể hoá từ SRS - Parent App v1.6

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)

| Version | Ngày | Nội dung | Người thực hiện |
| --- | --- | --- | --- |
| 1.0 | 22-07-2026 | Bản đầu tiên — chuyển 19 Functional Requirement (FR) trong SRS v1.6 thành 19 User Story (tỷ lệ 1:1), sắp xếp vào 5 Sprint theo dependency, kèm Acceptance Criteria (Given-When-Then) cho từng story | Sơn |
| 1.1 | 23-07-2026 | Tách Acceptance Criteria ra file riêng (Parent-App-Acceptance-Criteria-v1.1.docx). File này chỉ còn User Story + metadata + DoD bổ sung, giữ mã liên kết AC-XX để truy vết. | Sơn |

## Mục Lục

## Giới thiệu

Tài liệu này chuyển hóa 19 Functional Requirements (FR) đã đặc tả trong SRS v1.6 thành User Stories theo chuẩn Agile/Scrum, phục vụ trực tiếp việc lên Backlog và Sprint Planning. Mỗi User Story được đánh mã US-XX; Acceptance Criteria (AC-XX) tương ứng nằm ở file riêng, được tham chiếu qua trường "Liên kết Acceptance Criteria" trong bảng metadata bên dưới.

## Quy tắc đặt mã

- User Story: US-01 → US-19, đánh số tuần tự không theo nhóm chức năng (khác với FR-xx.y ở SRS) — vì trên Jira/Backlog thực tế, story được đánh số tuần tự theo thứ tự tạo, không nhóm theo module

- Acceptance Criteria: AC-XX dùng chung số với US-XX tương ứng (US-01 ↔ AC-01)

- Traceability: mỗi US ghi rõ "Nguồn gốc FR" để truy vết ngược lại SRS/BRD khi cần

## Nguyên tắc ước lượng Story Point

Áp dụng thang Fibonacci (1, 2, 3, 5, 8, 13) theo độ phức tạp tương đối, không phải thời gian tuyệt đối:

- 1-2 điểm: thao tác đọc dữ liệu đơn giản (view-only), ít logic

- 3-5 điểm: có validate, có luồng ngoại lệ, hoặc liên quan thông báo

- 8-13 điểm: tích hợp hệ thống ngoài, xử lý AI/thiết bị phần cứng, hoặc nhiều nhánh rẽ phức tạp

## Defiinition of Done (DoD) chuẩn - áp dụng cho mọi User Story

- Code đã merge vào nhánh main, pass code review

- Unit test + integration test đạt coverage ≥ 80%

- Toàn bộ Acceptance Criteria pass trên môi trường Staging

- API liên quan đã cập nhật vào Swagger/Postman collection

- QA sign-off, không còn bug mức Critical/Major

Ở mỗi User Story dưới đây, mục DoD chỉ ghi phần BỔ SUNG/khác biệt so với chuẩn chung này (nếu có) — để tránh lặp lại 19 lần cùng 5 gạch đầu dòng.

## Sơ đồ Sprint tổng quan

| Sprint | Chủ đề | User Story | Tổng điểm |
| --- | --- | --- | --- |
| Sprint 1 | Nền tảng: Đăng nhập, phân quyền, consent, audit log | US-16, US-17, US-18, US-19 | 18 |
| Sprint 2 | Sổ liên lạc, Thời khoá biểu | US-01, US-02, US-03, US-04 | 15 |
| Sprint 3 | Học phí, Tin tức | US-05, US-06, US-14, US-15 | 10 |
| Sprint 4 | Điểm danh (nhận diện khuôn mặt + thông báo) | US-07, US-08 | 18 |
| Sprint 5 | Thống kê, Lịch sử đăng ký, Xin nghỉ | US-09, US-10, US-11, US-12, US-13 | 17 |

## Sprint 1 - Nền tảng (Đăng nhập, Phân quyền, Consent, Audit log)

Nhóm story này PHẢI hoàn thành trước, vì mọi chức năng nghiệp vụ khác đều phụ thuộc vào đăng nhập và phân quyền.

## US-16 — Đăng nhập vào hệ thống

Là một người dùng (Phụ huynh/Giáo viên/School Admin), tôi muốn đăng nhập bằng tài khoản đã được cấp, để truy cập vào đúng chức năng theo vai trò của mình.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 5 |
| Sprint | Sprint 1 |
| Dependencies | Không có |
| Liên kết Acceptance Criteria | AC-16 |
| Nguồn gốc (FR) | FR-CC.01 |

Definition of Done (bổ sung ngoài chuẩn chung):

- Cơ chế khoá tài khoản tạm thời sau 5 lần đăng nhập sai (NFR-06) đã được test

## US-17 — Phân quyền truy cập dữ liệu

Là một hệ thống, tôi muốn kiểm tra và giới hạn quyền truy cập dữ liệu theo đúng vai trò của tài khoản đang đăng nhập, để đảm bảo Phụ huynh/Giáo viên/School Admin chỉ thấy đúng dữ liệu được phép, không rò rỉ thông tin học sinh khác.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 5 |
| Sprint | Sprint 1 |
| Dependencies | US-16 (Đăng nhập) |
| Liên kết Acceptance Criteria | AC-17 |
| Nguồn gốc (FR) | FR-CC.02 |

Definition of Done (bổ sung ngoài chuẩn chung):

- Có test case giả lập truy cập trái phép (VD: Phụ huynh A gọi API lấy dữ liệu học sinh của Phụ huynh B) và xác nhận bị chặn

## US-18 — Xác nhận Consent thu thập dữ liệu khuôn mặt

Là một phụ huynh, tôi muốn xác nhận đồng ý (hoặc từ chối) cho việc thu thập dữ liệu khuôn mặt của con để phục vụ điểm danh, để kiểm soát được việc dữ liệu sinh trắc học của con mình có được thu thập hay không, tuân thủ quyền riêng tư.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 5 |
| Sprint | Sprint 1 |
| Dependencies | US-16 (Đăng nhập) |
| Liên kết Acceptance Criteria | AC-18 |
| Nguồn gốc (FR) | FR-CC.03 |

Definition of Done (bổ sung ngoài chuẩn chung):

- Nội dung màn hình consent đã được xác nhận bởi School Admin/pháp lý trước khi release

## US-19 — Ghi nhận Audit Log

Là một hệ thống, tôi muốn tự động ghi lại lịch sử các thay đổi dữ liệu quan trọng (điểm danh, duyệt đơn nghỉ, cập nhật học sinh/lớp), để có thể tra soát khi có tranh chấp hoặc sự cố, đảm bảo tính minh bạch và trách nhiệm giải trình.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 3 |
| Sprint | Sprint 1 |
| Dependencies | Không có (chạy song song, ngầm) |
| Liên kết Acceptance Criteria | AC-19 |
| Nguồn gốc (FR) | FR-CC.04 |

## Sprint 2 - Sổ liên lạc, Thời khoá biểu

## US-01 — Xem sổ liên lạc

Là một phụ huynh, tôi muốn xem nội dung sổ liên lạc của con, để nắm được tình hình học tập và sinh hoạt hàng ngày của con một cách tập trung.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 2 |
| Sprint | Sprint 2 |
| Dependencies | US-16, US-17 |
| Liên kết Acceptance Criteria | AC-01 |
| Nguồn gốc (FR) | FR-01.1 |

## US-02 — Cập nhật nội dung sổ liên lạc

Là một giáo viên, tôi muốn thêm nội dung mới vào sổ liên lạc cho học sinh/lớp mình phụ trách, để thông báo kịp thời tình hình học tập/sinh hoạt của học sinh đến phụ huynh.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 3 |
| Sprint | Sprint 2 |
| Dependencies | US-16, US-17 |
| Liên kết Acceptance Criteria | AC-02 |
| Nguồn gốc (FR) | FR-01.2 |

## US-03 — Xem thời khoá biểu

Là một phụ huynh, tôi muốn xem thời khoá biểu của con theo tuần, để chủ động sắp xếp việc đưa đón và hỗ trợ học tập tại nhà.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 2 |
| Sprint | Sprint 2 |
| Dependencies | US-16, US-04 (đã có dữ liệu đồng bộ) |
| Liên kết Acceptance Criteria | AC-03 |
| Nguồn gốc (FR) | FR-02.1 |

## US-04 — Đồng bộ thời khoá biểu từ hệ thống nhà trường

Là một School Admin, tôi muốn hệ thống tự động đồng bộ (hoặc tôi có thể chủ động bấm đồng bộ ngay) dữ liệu thời khoá biểu từ hệ thống quản lý của nhà trường, để dữ liệu thời khoá biểu trên Parent App luôn khớp với dữ liệu gốc của trường, không cần nhập tay lại.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 8 |
| Sprint | Sprint 2 |
| Dependencies | US-17 |
| Liên kết Acceptance Criteria | AC-04 |
| Nguồn gốc (FR) | FR-02.2 |

Definition of Done (bổ sung ngoài chuẩn chung):

- Cơ chế tích hợp cụ thể (API/file/thủ công) đã được xác nhận với nhà trường TRƯỚC khi bắt đầu code — nếu chưa xác nhận, story này KHÔNG được kéo vào sprint

## Sprint 3 - Học phí, Tin tức

## US-05 — Xem thông tin học phí

Là một phụ huynh, tôi muốn xem số tiền, hạn đóng và trạng thái học phí của con, để chủ động theo dõi nghĩa vụ tài chính, tránh quên hạn đóng.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 2 |
| Sprint | Sprint 3 |
| Dependencies | US-16, US-17 |
| Liên kết Acceptance Criteria | AC-05 |
| Nguồn gốc (FR) | FR-03.1 |

## US-06 — Nhắc nhở hạn đóng học phí

Là một phụ huynh, tôi muốn nhận thông báo nhắc nhở trước khi đến hạn đóng học phí, để không quên deadline, chủ động chuẩn bị đóng học phí đúng hạn.

| Độ ưu tiên | Should |
| --- | --- |
| Story Points | 3 |
| Sprint | Sprint 3 |
| Dependencies | US-05 |
| Liên kết Acceptance Criteria | AC-06 |
| Nguồn gốc (FR) | FR-03.2 |

US-14 — Đăng tin tức

Là một School Admin, tôi muốn đăng tin tức/thông báo chung cho toàn bộ phụ huynh trong trường, để truyền tải thông tin nhanh chóng, đồng đều đến mọi phụ huynh mà không phụ thuộc vào việc họ có mặt tại trường.

| Độ ưu tiên | Should |
| --- | --- |
| Story Points | 3 |
| Sprint | Sprint 3 |
| Dependencies | US-16, US-17 |
| Liên kết Acceptance Criteria | AC-14 |
| Nguồn gốc (FR) | FR-07.1 |

## US-15 — Xem tin tức

Là một phụ huynh, tôi muốn xem danh sách tin tức từ nhà trường, để không bỏ lỡ thông tin/sự kiện quan trọng của trường.

| Độ ưu tiên | Should |
| --- | --- |
| Story Points | 2 |
| Sprint | Sprint 3 |
| Dependencies | US-16, US-14 (đã có tin đăng) |
| Liên kết Acceptance Criteria | AC-15 |
| Nguồn gốc (FR) | FR-07.2 |

## Sprint 4 - Điểm danh (Nhận diện khuôn mặt)

Đây là Sprint chứa 2 story phức tạp nhất toàn dự án — nên KHÔNG gộp thêm story nào khác vào sprint này để đội Dev tập trung xử lý đúng rủi ro kỹ thuật (AI, GPS, consent).

## US-07 — Điểm danh bằng nhận diện khuôn mặt

Là một giáo viên, tôi muốn điểm danh học sinh bằng cách quét khuôn mặt qua camera thiết bị, để ghi nhận điểm danh nhanh, chính xác, có xác thực thay vì ghi chép thủ công dễ sai sót.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 13 |
| Sprint | Sprint 4 |
| Dependencies | US-16, US-17, US-18 (Consent) |
| Liên kết Acceptance Criteria | AC-07 |
| Nguồn gốc (FR) | FR-04.1 |

Definition of Done (bổ sung ngoài chuẩn chung):

- Đã test với tối thiểu 3 điều kiện ánh sáng khác nhau (đủ sáng, thiếu sáng, ngược sáng)

- Đã test luồng chặn khi học sinh chưa có consent

- Confidence score threshold đã được Technical Lead xác nhận cụ thể (chưa chốt số trong SRS)

## US-08 — Nhận thông báo điểm danh real-time

Là một phụ huynh, tôi muốn nhận thông báo ngay khi con vừa được điểm danh, để yên tâm và có thể phản ứng kịp thời nếu phát hiện bất thường (VD: giờ vào lớp không đúng dự kiến).

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 5 |
| Sprint | Sprint 4 |
| Dependencies | US-07 |
| Liên kết Acceptance Criteria | AC-08 |
| Nguồn gốc (FR) | FR-04.2 |

## Sprint 5 - Thông kê điểm danh, Lịch sử đăng ký, Xin nghỉ

## US-09 — Xem thống kê chuyên cần

Là một phụ huynh, tôi muốn xem thống kê tổng hợp số buổi đi học/vắng của con theo tuần hoặc tháng, để nắm được xu hướng chuyên cần tổng thể, không chỉ theo từng buổi riêng lẻ.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 5 |
| Sprint | Sprint 5 |
| Dependencies | US-07 (đã có dữ liệu điểm danh) |
| Liên kết Acceptance Criteria | AC-09 |
| Nguồn gốc (FR) | FR-04.3 |

## US-10 — Xem lịch sử đăng ký khoá học

Là một phụ huynh, tôi muốn xem lại danh sách các khoá học con đã đăng ký, để theo dõi được quá trình học tập của con qua các khoá đã tham gia.

| Độ ưu tiên | Should |
| --- | --- |
| Story Points | 2 |
| Sprint | Sprint 5 |
| Dependencies | US-16 |
| Liên kết Acceptance Criteria | AC-10 |
| Nguồn gốc (FR) | FR-05.1 |

## US-11 — Gửi đơn xin nghỉ học

Là một phụ huynh, tôi muốn gửi đơn xin nghỉ học cho con trực tiếp trên app, để có 1 kênh chính thức, minh bạch thay vì gọi điện/nhắn tin không có xác nhận rõ ràng.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 5 |
| Sprint | Sprint 5 |
| Dependencies | US-16 |
| Liên kết Acceptance Criteria | AC-11 |
| Nguồn gốc (FR) | FR-06.1 |

Definition of Done (bổ sung ngoài chuẩn chung):

- Giá trị X (số ngày tối đa cho phép xin nghỉ trước/sau — BRULE-005) đã được chốt với School Admin trước khi bắt đầu code — nếu chưa chốt, story này KHÔNG được kéo vào sprint (áp cùng nguyên tắc như US-04, vì cùng phụ thuộc vào 1 biến nghiệp vụ chưa xác nhận)

## US-12 — Duyệt / Từ chối đơn xin nghỉ

Là một giáo viên, tôi muốn duyệt hoặc từ chối đơn xin nghỉ của học sinh lớp mình phụ trách, để xử lý đơn xin nghỉ nhanh chóng, có ghi nhận rõ ràng thay vì trao đổi miệng.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 3 |
| Sprint | Sprint 5 |
| Dependencies | US-11, US-17 |
| Liên kết Acceptance Criteria | AC-12 |
| Nguồn gốc (FR) | FR-06.2 |

## US-13 — Theo dõi trạng thái đơn xin nghỉ

Là một phụ huynh, tôi muốn xem lại lịch sử và trạng thái các đơn xin nghỉ đã gửi, để biết được đơn đã được xử lý hay chưa mà không cần hỏi lại giáo viên.

| Độ ưu tiên | Must |
| --- | --- |
| Story Points | 2 |
| Sprint | Sprint 5 |
| Dependencies | US-11 |
| Liên kết Acceptance Criteria | AC-13 |
| Nguồn gốc (FR) | FR-06.3 |

## Traceability Summary (FR → US → AC)

Bảng dưới đây điền nốt cột "User Story" đang để trống ở Traceability Matrix của BRD (mục 4.3) — mỗi FR trong SRS giờ đã có 1 User Story tương ứng.

| Mã FR (SRS) | Mã US | Mã AC | Sprint |
| --- | --- | --- | --- |
| FR-01.1 | US-01 | AC-01 | Sprint 2 |
| FR-01.2 | US-02 | AC-02 | Sprint 2 |
| FR-02.1 | US-03 | AC-03 | Sprint 2 |
| FR-02.2 | US-04 | AC-04 | Sprint 2 |
| FR-03.1 | US-05 | AC-05 | Sprint 3 |
| FR-03.2 | US-06 | AC-06 | Sprint 3 |
| FR-04.1 | US-07 | AC-07 | Sprint 4 |
| FR-04.2 | US-08 | AC-08 | Sprint 4 |
| FR-04.3 | US-09 | AC-09 | Sprint 5 |
| FR-05.1 | US-10 | AC-10 | Sprint 5 |
| FR-06.1 | US-11 | AC-11 | Sprint 5 |
| FR-06.2 | US-12 | AC-12 | Sprint 5 |
| FR-06.3 | US-13 | AC-13 | Sprint 5 |
| FR-07.1 | US-14 | AC-14 | Sprint 3 |
| FR-07.2 | US-15 | AC-15 | Sprint 3 |
| FR-CC.01 | US-16 | AC-16 | Sprint 1 |
| FR-CC.02 | US-17 | AC-17 | Sprint 1 |
