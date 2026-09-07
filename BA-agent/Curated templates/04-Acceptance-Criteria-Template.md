# 4. Acceptance Criteria (AC) Template
*Dành cho Developers & QA/QC — Định dạng Gherkin (Given–When–Then).*

---

## 4.0 Thông tin chung

| Mục | Chi tiết |
|---|---|
| **Tên dự án** | [Tên dự án] |
| **Loại tài liệu** | Acceptance Criteria (AC) |
| **Phiên bản** | [x.x] Draft |
| **Tác giả** | [Tên chuyên viên BA] |
| **Ngày tạo** | [DD-MM-YYYY] |
| **Nguồn gốc** | Gắn trực tiếp với User Stories v[x.x] |

### Nhật ký thay đổi (Change Log)
| Version | Ngày | Nội dung thay đổi | Người sửa |
|---|---|---|---|
| 1.0 | [DD-MM-YYYY] | Khởi tạo AC cho toàn bộ User Stories | [Tên BA] |

---

## 4.1 Ma trận truy xuất (FR → US → AC Traceability)
*Đảm bảo mỗi FR đều có User Story và AC tương ứng — không bỏ sót yêu cầu nào.*

| Mã FR (SRS) | Mã US | Mã AC | Số kịch bản | Trạng thái AC |
|---|---|---|---|---|
| `FR-A01` | US-01 | AC-01 | 4 | ✅ Done |
| `FR-A02` | US-02 | AC-02 | 4 | ✅ Done |
| `FR-B01` | US-03 | AC-03 | 5 | 🔄 In Progress |
| `FR-CC-01` | US-04 | AC-04 | 6 | ⬜ To Do |

> **Quy tắc:** Mỗi AC **tối thiểu 4 kịch bản** (Happy Path, Race Condition, Boundary, Negative). Story phức tạp có thể cần 5-8 kịch bản.

---

## 4.2 Template Chuẩn — Tối thiểu 4 Kịch bản Bắt buộc

```text
Mã Acceptance Criteria: AC-[XXX]
Thuộc User Story: US-[XXX]

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
```

---

## 4.3 Kịch bản bổ sung (Dùng khi story phức tạp)

```text
===================================================================
KỊCH BẢN 5: [Hết hạn phiên / Token Expiry]
===================================================================
Given [người dùng đã đăng nhập nhưng session đã hết hạn (quá [X] phút không hoạt động)]
When [người dùng thực hiện hành động yêu cầu xác thực]
Then [hệ thống chuyển về màn hình đăng nhập, hiển thị thông báo "Phiên đã hết hạn, vui lòng đăng nhập lại"]
  And [dữ liệu đang nhập (nếu có) được lưu tạm để khôi phục sau khi đăng nhập lại]

===================================================================
KỊCH BẢN 6: [Chặn trùng lặp - Duplicate Prevention]
===================================================================
Given [người dùng đã tạo thành công một bản ghi]
When [người dùng bấm nút Xác nhận lần thứ 2 (double-click hoặc refresh)]
Then [hệ thống trả về bản ghi đã tạo thay vì tạo bản ghi trùng (idempotent)]

===================================================================
KỊCH BẢN 7: [Sai mật khẩu liên tiếp - Account Lockout]
===================================================================
Given [người dùng đã nhập sai mật khẩu [X-1] lần]
When [người dùng nhập sai mật khẩu lần thứ [X]]
Then [hệ thống khoá tạm thời tài khoản trong [Y] phút]
  And [gửi email/SMS cảnh báo cho chủ tài khoản]
  And [hiển thị thông báo "Tài khoản tạm khoá, vui lòng thử lại sau [Y] phút hoặc đặt lại mật khẩu"]

===================================================================
KỊCH BẢN 8: [Mất kết nối mạng - Offline / Network Error]
===================================================================
Given [người dùng đang thực hiện thao tác trên ứng dụng]
When [kết nối mạng bị mất giữa chừng]
Then [hệ thống hiển thị thông báo lỗi mạng rõ ràng]
  And [không mất dữ liệu đang nhập]
  And [tự động retry khi kết nối được khôi phục (nếu áp dụng)]
```

---

## 4.4 Checklist nghiệm thu nhanh

```text
===================================================================
CHECKLIST NGHIỆM THU:
===================================================================
[ ] Kiểm tra điều kiện đầu vào (Input validation)
[ ] Kiểm tra hiển thị giao diện thành công
[ ] Kiểm tra xử lý tranh chấp / đồng thời không bị trùng dữ liệu
[ ] Kiểm tra thông báo lỗi & mã lỗi hiển thị đúng ngữ cảnh
[ ] Kiểm tra log và dữ liệu lưu trong database
[ ] Kiểm tra hết hạn token / session timeout
[ ] Kiểm tra chặn double-submit (idempotent)
[ ] Kiểm tra hành vi khi mất kết nối mạng
```

---

## 4.5 Ví dụ thực chiến: AC-APT-021 (Thuộc US-APT-021)

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

Scenario 5: Token hết hạn giữa chừng đặt lịch
Given khách hàng đã chọn bác sĩ và khung giờ nhưng session hết hạn (idle > 30 phút)
When khách hàng bấm "Xác nhận đặt lịch"
Then hệ thống chuyển về màn hình đăng nhập, giữ lại thông tin đã chọn
  And sau khi đăng nhập lại, khách hàng quay về màn xác nhận với dữ liệu đã chọn

Scenario 6: Double-click nút Xác nhận (Duplicate Prevention)
Given khách hàng đã bấm "Xác nhận đặt lịch" và hệ thống đang xử lý
When khách hàng bấm nút lần thứ 2
Then hệ thống chỉ tạo 1 lịch hẹn duy nhất (idempotent), không trùng lặp
```
