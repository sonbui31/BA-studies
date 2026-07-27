# Acceptance Criteria

## PARENT MOBILE APP

Acceptance Criteria (đi kèm User Story)

Version: 1.1

Author: Bùi Ngọc Sơn (BA)

Date: 23-07-2026

Nguồn gốc: tách từ Parent-App-UserStory-v1.0.docx (mục Acceptance Criteria của từng User Story)

Ghi chú: mỗi Acceptance Criteria dưới đây dùng chung mã số với User Story tương ứng (AC-XX ↔ US-XX). Xem nội dung đầy đủ của User Story (vai trò, mục tiêu, priority, story points, dependencies, DoD) tại file "Parent-App-UserStory-v1.1.docx".

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)

| Version | Ngày | Nội dung | Người thực hiện |
| --- | --- | --- | --- |
| 1.1 | 23-07-2026 | Tách riêng từ Parent-App-UserStory-v1.0.docx — giữ nguyên nội dung Acceptance Criteria (Given-When-Then) của cả 19 story, không chỉnh sửa nội dung nghiệp vụ. | Sơn |

## Mục lục

## Giới thiệu

Tài liệu này tập hợp toàn bộ Acceptance Criteria (AC-01 → AC-19) của Parent App, tách riêng khỏi User Story để dễ tra cứu và cập nhật độc lập khi nghiệp vụ thay đổi mà story không đổi. Mỗi AC-XX được viết theo định dạng Given-When-Then, có thể gồm nhiều Scenario.

Sắp xếp: các AC được trình bày theo đúng thứ tự Sprint như trong User Story doc, để 2 tài liệu dễ đối chiếu song song khi review hoặc viết test case.

## Sprint 1 - Nền tảng (Đăng nhập, Phân quyền, Consent, Audit log)

## AC-16 — Đăng nhập vào hệ thống (liên kết US-16)

Scenario 1: Đăng nhập thành công

Given: Người dùng đã có tài khoản hợp lệ, chưa bị khoá

When: Nhập đúng tài khoản và mật khẩu, nhấn Đăng nhập

Then: Hệ thống tạo phiên đăng nhập (token) và điều hướng vào màn hình chính theo đúng vai trò

Scenario 2: Sai mật khẩu

Given: Người dùng nhập sai mật khẩu

When: Nhấn Đăng nhập

Then: Hệ thống báo lỗi "Sai tài khoản hoặc mật khẩu", không tiết lộ tài khoản có tồn tại hay không

Scenario 3: Khoá tài khoản tạm thời

Given: Người dùng đã nhập sai mật khẩu 5 lần liên tiếp

When: Nhập lần thứ 6 (dù đúng hay sai)

Then: Hệ thống chặn đăng nhập và hiển thị thông báo tài khoản bị khoá tạm thời, hướng dẫn cách mở khoá

## AC-17 — Phân quyền truy cập dữ liệu (liên kết US-17)

Scenario 1: Truy cập đúng phạm vi

Given: Phụ huynh đã đăng nhập, có token hợp lệ

When: Gọi API lấy dữ liệu của con mình

Then: Hệ thống trả về dữ liệu thành công

Scenario 2: Truy cập ngoài phạm vi

Given: Phụ huynh đã đăng nhập

When: Cố gắng gọi API lấy dữ liệu của học sinh KHÔNG liên kết với tài khoản mình

Then: Hệ thống trả về lỗi 403 Forbidden, ghi nhận vào Audit Log (US-19)

Scenario 3: Giáo viên xem đơn xin nghỉ ngoài lớp phụ trách

Given: Giáo viên A không phụ trách lớp của học sinh X

When: Giáo viên A cố gắng duyệt đơn xin nghỉ của học sinh X

Then: Hệ thống chặn hành động, không hiển thị đơn đó trong danh sách chờ duyệt của Giáo viên A

## AC-18 — Xác nhận Consent thu thập dữ liệu khuôn mặt (liên kết US-18)

Scenario 1: Phụ huynh đồng ý consent

Given: Phụ huynh đăng nhập lần đầu, học sinh liên kết chưa có consent

When: Phụ huynh đọc màn hình consent và chọn "Đồng ý"

Then: Hệ thống lưu consent_status = Đồng ý kèm timestamp, học sinh có thể điểm danh bằng khuôn mặt

Scenario 2: Phụ huynh từ chối consent

Given: Phụ huynh đăng nhập lần đầu

When: Phụ huynh chọn "Từ chối"

Then: Hệ thống lưu consent_status = Từ chối; học sinh đó CHỈ có thể điểm danh thủ công (không dùng khuôn mặt)

Scenario 3: Không cho phép bỏ qua màn hình consent

Given: Phụ huynh đang ở màn hình consent, chưa chọn Đồng ý/Từ chối

When: Phụ huynh cố gắng thoát hoặc điều hướng sang màn hình khác

Then: Hệ thống chặn điều hướng, bắt buộc phải chọn 1 trong 2 lựa chọn trước khi tiếp tục sử dụng app

## AC-19 — Ghi nhận Audit Log (liên kết US-19)

Scenario 1: Ghi log khi điểm danh

Given: Giáo viên vừa điểm danh xong 1 học sinh

When: Bản ghi điểm danh được lưu vào hệ thống

Then: Hệ thống tự động tạo 1 bản ghi AuditLog gồm: người thực hiện, hành động, thời gian, dữ liệu

Scenario 2: Log không thể sửa/xoá

Given: Đã có 1 bản ghi AuditLog tồn tại

When: Bất kỳ ai (kể cả admin) cố gắng sửa hoặc xoá bản ghi đó qua API/DB trực tiếp

Then: Hệ thống từ chối thao tác — AuditLog là immutable (không thể sửa/xoá) sau khi ghi

## Sprint 2 - Sổ liên lạc, Thời khoá biểu

## AC-01 — Xem sổ liên lạc (liên kết US-01)

Scenario 1: Có dữ liệu sổ liên lạc

Given: Phụ huynh đã đăng nhập, học sinh liên kết đã có ít nhất 1 bản ghi sổ liên lạc

When: Phụ huynh mở màn hình Sổ liên lạc

Then: Hệ thống hiển thị danh sách nội dung, sắp xếp mới nhất lên đầu, kèm tên giáo viên cập nhật

Scenario 2: Chưa có dữ liệu

Given: Học sinh liên kết chưa có bản ghi sổ liên lạc nào

When: Phụ huynh mở màn hình Sổ liên lạc

Then: Hệ thống hiển thị thông báo "Chưa có thông tin sổ liên lạc"

## AC-02 — Cập nhật nội dung sổ liên lạc (liên kết US-02)

Scenario 1: Cập nhật thành công

Given: Giáo viên đã chọn học sinh/lớp hợp lệ thuộc quyền quản lý

When: Nhập nội dung (không trống) và nhấn Lưu

Then: Hệ thống lưu bản ghi mới, gửi thông báo cho phụ huynh liên quan

Scenario 2: Nội dung trống

Given: Giáo viên để trống ô nội dung

When: Nhấn Lưu

Then: Hệ thống chặn lưu, hiển thị lỗi "Nội dung không được để trống"

Scenario 3: Ảnh đính kèm sai định dạng

Given: Giáo viên đính kèm 1 file không phải JPG/PNG hoặc vượt quá 5MB

When: Nhấn Lưu

Then: Hệ thống chặn lưu, hiển thị lỗi định dạng/dung lượng ảnh

## AC-03 — Xem thời khoá biểu (liên kết US-03)

Scenario 1: Xem thành công

Given: Học sinh đã được gán vào 1 lớp hợp lệ, lớp đã có thời khoá biểu

When: Phụ huynh mở màn hình Thời khoá biểu

Then: Hệ thống hiển thị đúng lịch học tuần hiện tại, cho phép chuyển tuần trước/sau

Scenario 2: Học sinh chưa gán lớp hợp lệ

Given: Học sinh chưa được gán vào lớp nào (lỗi dữ liệu)

When: Phụ huynh mở màn hình Thời khoá biểu

Then: Hệ thống hiển thị thông báo lỗi và ghi log để School Admin xử lý

## AC-04 — Đồng bộ thời khoá biểu từ hệ thống nhà trường (liên kết US-04)

Scenario 1: Đồng bộ thành công

Given: Có kết nối hợp lệ đến hệ thống nguồn, dữ liệu nguồn hợp lệ

When: Tiến trình đồng bộ chạy theo lịch (hoặc School Admin bấm Đồng bộ ngay)

Then: Dữ liệu ThoiKhoaBieu được cập nhật thành công trong Parent App

Scenario 2: Đồng bộ thất bại

Given: Mất kết nối đến hệ thống nguồn, hoặc dữ liệu nguồn sai định dạng

When: Tiến trình đồng bộ chạy

Then: Hệ thống ghi log lỗi, thông báo cho School Admin, và GIỮ NGUYÊN dữ liệu cũ (không xoá)

## Sprint 3 - Học phí, Tin tức

## AC-05 — Xem thông tin học phí (liên kết US-05)

Scenario 1: Xem danh sách học phí

Given: Học sinh có ít nhất 1 khoản học phí trong hệ thống

When: Phụ huynh mở màn hình Học phí

Then: Hệ thống hiển thị danh sách khoản học phí, sắp xếp theo hạn đóng gần nhất lên đầu

Scenario 2: Khoản quá hạn được đánh dấu nổi bật

Given: Có 1 khoản học phí đã quá hạn đóng nhưng chưa thanh toán

When: Phụ huynh mở màn hình Học phí

Then: Dòng tương ứng được hiển thị nổi bật (VD: màu đỏ) để dễ nhận biết

## AC-06 — Nhắc nhở hạn đóng học phí (liên kết US-06)

Scenario 1: Gửi nhắc nhở đúng ngưỡng

Given: Có khoản học phí ở trạng thái Chưa đóng, còn đúng số ngày trong ngưỡng cấu hình trước hạn

When: Hệ thống chạy tiến trình quét hàng ngày

Then: Phụ huynh nhận được push notification nhắc nhở

Scenario 2: Không nhắc khoản đã đóng

Given: Khoản học phí đã chuyển trạng thái Đã đóng

When: Hệ thống chạy tiến trình quét hàng ngày

Then: Phụ huynh KHÔNG nhận thông báo nhắc nhở cho khoản này dù còn trong ngưỡng ngày cấu hình

## AC-14 — Đăng tin tức (liên kết US-14)

Scenario 1: Đăng thành công

Given: School Admin đã nhập đủ tiêu đề và nội dung

When: Nhấn Đăng

Then: Hệ thống lưu bài đăng, gửi thông báo cho toàn bộ phụ huynh

Scenario 2: Thiếu tiêu đề/nội dung

Given: School Admin để trống tiêu đề hoặc nội dung

When: Nhấn Đăng

Then: Hệ thống chặn đăng, hiển thị lỗi tương ứng

## AC-15 — Xem tin tức (liên kết US-15)

Scenario 1: Có tin tức

Given: Đã có ít nhất 1 bài tin tức được đăng

When: Phụ huynh mở màn hình Tin tức

Then: Hệ thống hiển thị danh sách bài đăng, mới nhất lên đầu

Scenario 2: Chưa có tin tức

Given: Chưa có bài đăng nào

When: Phụ huynh mở màn hình Tin tức

Then: Hệ thống hiển thị màn hình trống với thông báo phù hợp

## Sprint 4 - Điểm danh (Nhận diện khuôn mặt)

## AC-07 — Điểm danh bằng nhận diện khuôn mặt (liên kết US-07)

Scenario 1: Nhận diện thành công

Given: Học sinh đã có consent + dữ liệu khuôn mặt hợp lệ; ánh sáng đủ

When: Giáo viên hướng camera vào học sinh

Then: Hệ thống đối chiếu khớp (confidence score vượt ngưỡng), ghi nhận điểm danh THÀNH CÔNG kèm giờ, GPS, ảnh chụp

## AC-08 — Nhận thông báo điểm danh real-time (liên kết US-08)

Scenario 1: Gửi thông báo đầy đủ nội dung

Given: Vừa có 1 bản ghi điểm danh thành công (từ US-07)

When: Hệ thống xử lý sự kiện điểm danh

Then: Phụ huynh nhận push notification gồm đủ 4 trường: ảnh chụp, giờ vào lớp, địa điểm (tên lớp + GPS), tên giáo viên

Scenario 2: Gửi thất bại — retry

Given: Thiết bị phụ huynh offline tại thời điểm gửi

When: Hệ thống cố gắng gửi push notification

Then: Hệ thống áp dụng cơ chế retry (giãn cách 30s/60s/120s theo NFR-08)

## Sprint 5 - Thông kê điểm danh, Lịch sử đăng ký, Xin nghỉ

## AC-09 — Xem thống kê chuyên cần (liên kết US-09)

Scenario 1: Có dữ liệu trong khoảng thời gian chọn

Given: Học sinh có ít nhất 1 bản ghi điểm danh trong khoảng thời gian được chọn

When: Phụ huynh chọn khoảng thời gian (tuần/tháng) và xem thống kê

Then: Hệ thống hiển thị số buổi đi học, số buổi vắng, tỷ lệ chuyên cần (%)

Scenario 2: Không có dữ liệu

Given: Chưa có bản ghi điểm danh nào trong khoảng thời gian chọn

When: Phụ huynh xem thống kê

Then: Hệ thống hiển thị thông báo "Chưa có dữ liệu”

## AC-10 — Xem lịch sử đăng ký khoá học (liên kết US-10)

Scenario 1: Có lịch sử khoá học

Given: Học sinh đã từng đăng ký ít nhất 1 khoá học

When: Phụ huynh mở màn hình Lịch sử đăng ký

Then: Hệ thống hiển thị danh sách khoá học kèm trạng thái (Đang học/Đã hoàn thành), mới nhất lên đầu

Scenario 2: Chưa từng đăng ký

Given: Học sinh chưa từng đăng ký khoá học nào

When: Phụ huynh mở màn hình Lịch sử đăng ký

Then: Hệ thống hiển thị thông báo trống

## AC-11 — Gửi đơn xin nghỉ học (liên kết US-11)

Scenario 1: Gửi đơn thành công

Given: Phụ huynh nhập ngày nghỉ hợp lệ (trong giới hạn BRULE-005) và lý do đầy đủ

When: Nhấn Gửi đơn

Then: Hệ thống lưu đơn với trạng thái Pending, gửi thông báo cho giáo viên phụ trách lớp

Scenario 2: Ngày nghỉ vượt giới hạn

Given: Phụ huynh chọn ngày nghỉ vượt quá X ngày cho phép (BRULE-005)

When: Nhấn Gửi đơn

Then: Hệ thống chặn gửi, hiển thị lỗi giới hạn ngày

Scenario 3: Thiếu lý do

Given: Phụ huynh để trống ô lý do

When: Nhấn Gửi đơn

Then: Hệ thống chặn gửi, yêu cầu nhập đầy đủ lý do

Scenario 4: Trùng đơn đã tồn tại

Given: Đã có 1 đơn Pending/Approved cho cùng ngày nghỉ đó

When: Phụ huynh cố gắng gửi thêm 1 đơn khác cho cùng ngày

Then: Hệ thống chặn tạo đơn trùng, thông báo đã có đơn tồn tại

## AC-12 — Duyệt / Từ chối đơn xin nghỉ (liên kết US-12)

Scenario 1: Duyệt đơn

Given: Đơn đang ở trạng thái Pending, giáo viên là người phụ trách đúng lớp

When: Giáo viên nhấn Duyệt

Then: Hệ thống chuyển trạng thái sang Approved, gửi thông báo cho phụ huynh

Scenario 2: Từ chối đơn — bắt buộc lý do

Given: Giáo viên chọn Từ chối nhưng để trống lý do

When: Nhấn xác nhận Từ chối

Then: Hệ thống chặn, yêu cầu nhập lý do từ chối

Scenario 3: Giáo viên không phụ trách lớp

Given: Giáo viên không phải người phụ trách lớp của học sinh gửi đơn

When: Giáo viên tìm đơn đó trong danh sách chờ duyệt

Then: Đơn KHÔNG hiển thị trong danh sách chờ duyệt của giáo viên này (theo BRULE-008)

## AC-13 — Theo dõi trạng thái đơn xin nghỉ (liên kết US-13)

Scenario 1: Xem danh sách đơn

Given: Phụ huynh đã từng gửi ít nhất 1 đơn xin nghỉ

When: Phụ huynh mở màn hình Lịch sử đơn xin nghỉ

Then: Hệ thống hiển thị danh sách đơn, mới nhất lên đầu, kèm badge màu theo trạng thái (Pending/Approved/Rejected)

Scenario 2: Xem lý do từ chối

Given: Có 1 đơn đã bị từ chối kèm lý do

When: Phụ huynh mở chi tiết đơn đó

Then: Hệ thống hiển thị đầy đủ lý do từ chối của giáo viên

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
| FR-CC.03 | US-18 | AC-18 | Sprint 1 |
| FR-CC.04 | US-19 | AC-19 | Sprint 1 |
