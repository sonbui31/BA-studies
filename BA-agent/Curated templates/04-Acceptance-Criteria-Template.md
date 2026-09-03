# 4. Acceptance Criteria (AC) Template
*Dành cho Developers & QA/QC — Định dạng Gherkin (Given–When–Then).*

---

## 4.1 Template Chuẩn 4 Kịch bản Bắt buộc

```text
Mã Acceptance Criteria: AC-[MODULE]-[XXX]
Thuộc User Story: US-[MODULE]-[XXX]

===================================================================
KỊCH BẢN 1: [Tên kịch bản - Happy Path / Luồng chuẩn thành công]
===================================================================
Given [tiền điều kiện ban đầu hợp lệ]
When [người dùng thực hiện hành động chính]
Then [hệ thống xử lý thành công, hiển thị kết quả mong đợi]

===================================================================
KỊCH BẢN 2: [Tranh chấp đồng thời - Race Condition / Concurrency]
===================================================================
Given [hai người dùng cùng thao tác trên một tài nguyên đồng thời]
When [người A bấm xác nhận trước 1 giây so với người B]
Then [người A thành công, người B nhận mã lỗi phù hợp (VD: HTTP 409 Conflict) và hệ thống làm mới lại dữ liệu]

===================================================================
KỊCH BẢN 3: [Giá trị biên - Boundary / Limit Case]
===================================================================
Given [hôm nay là ngày X]
When [người dùng chọn giá trị chạm đúng ranh giới hạn mức (VD: đúng +30 ngày hoặc đúng độ dài ký tự tối đa)]
Then [hệ thống cho phép thực hiện bình thường]

===================================================================
KỊCH BẢN 4: [Ngoại lệ & Vi phạm luật - Negative / Rule Violation (BRULE-xx)]
===================================================================
Given [người dùng đã chạm ngưỡng giới hạn (theo quy định BRULE-xx)]
When [cố tình thực hiện thêm hành động vượt ngưỡng cho phép]
Then [hệ thống từ chối, trả về mã lỗi thích hợp (VD: HTTP 422) và không tạo bản ghi mới]

===================================================================
CHECKLIST NGHIỆM THU NHANH:
===================================================================
[ ] Kiểm tra điều kiện đầu vào (Input validation)
[ ] Kiểm tra hiển thị giao diện thành công
[ ] Kiểm tra xử lý tranh chấp / đồng thời không bị trùng dữ liệu
[ ] Kiểm tra thông báo lỗi & mã lỗi hiển thị đúng ngữ cảnh
[ ] Kiểm tra log và dữ liệu lưu trong database
```

---

## 4.2 Ví dụ thực chiến: AC-APT-021 (Thuộc US-APT-021)

```text
Scenario 1: Đặt lịch thành công (Happy Path)
Given khách hàng đã đăng nhập và chọn bác sĩ Nguyễn Văn B
When khách hàng chọn khung giờ 09:00 - 09:30 ngày 10/07/2026 (còn trống) và bấm "Xác nhận đặt lịch"
Then hệ thống tạo lịch hẹn thành công, hiển thị mã lịch hẹn và khung giờ đó không còn hiển thị trống cho khách khác

Scenario 2: Khung giờ vừa bị người khác đặt trước (Race Condition)
Given hai khách hàng cùng xem một khung giờ trống 09:00 - 09:30
When khách hàng A xác nhận đặt lịch trước 1 giây so với khách B
Then khách hàng B nhận lỗi ERR_SLOT_TAKEN (HTTP 409 Conflict) và danh sách khung giờ được cập nhật lại

Scenario 3: Đặt lịch đúng ranh giới +30 ngày (Boundary Case)
Given hôm nay là 07/07/2026
When khách hàng chọn ngày khám 06/08/2026 (đúng ranh giới +30 ngày)
Then hệ thống cho phép đặt lịch bình thường

Scenario 4: Vượt giới hạn số lịch hẹn đang chờ (BRULE-04)
Given khách hàng đã có 3 lịch hẹn ở trạng thái "Chờ khám"
When khách hàng cố đặt thêm lịch hẹn thứ 4
Then hệ thống báo lỗi ERR_LIMIT_REACHED (HTTP 422) và không tạo lịch hẹn mới
```
