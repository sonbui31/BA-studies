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
| `FR-AUTH-001` | US-AUTH-001 | AC-AUTH-001 | 4 | ✅ Done |
| `FR-AUTH-002` | US-AUTH-002 | AC-AUTH-002 | 4 | ✅ Done |
| `FR-MODA-001` | US-MODA-001 | AC-MODA-001 | 5 | 🔄 In Progress |
| `FR-CC-001` | US-CC-001 | AC-CC-001 | 6 | ⬜ To Do |

> 🔴 **Quy tắc Vàng cho Acceptance Criteria (AC Rules):**
> 1. **Số lượng kịch bản:** Mức tối thiểu 2/4 theo Tier trong `BA-document-rule/core/rigor-tiers.md` là **quy ước nội bộ**, không phải quy định của Gherkin hoặc Scrum. Chọn kịch bản theo rule và rủi ro; chỉ thêm Race, Boundary, Permission, Network khi áp dụng. Mỗi story phải có ít nhất một AC quan sát được.
> 2. **Story Splitting Trigger:** Hơn 8 kịch bản là tín hiệu rà soát: nếu có nhiều quy tắc hoặc nhiều kết quả độc lập, cân nhắc tách story; nếu là nhiều bộ dữ liệu cho cùng một quy tắc, dùng `Scenario Outline` và `Examples`. Không có trần 8 kịch bản trong Gherkin.
> 2b. **Điều chỉnh theo mức rủi ro:** Tier 1 thường có ít nhất 2 kịch bản; Tier 2 ít nhất 4; Tier 3 bổ sung tình huống rủi ro cao khi áp dụng. Lý do bỏ các nhánh liên quan cần được ghi lại. Xem `BA-document-rule/core/rigor-tiers.md`.
> 3. **Chống Anti-patterns & Ảo giác logic trong AC:**
>    - ❌ Cấm mô tả UI chi tiết/styling: *"Nút chuyển màu xanh"* ➔ ✅ *"Hệ thống hiển thị trạng thái thành công"*.
>    - ❌ Cấm chèn mã kỹ thuật/API: *"Gọi API POST /v1/booking"* ➔ ✅ *"Hệ thống tạo bản ghi đặt lịch và trừ hạn mức tương ứng"*.
>    - ❌ Cấm động từ mơ hồ (Điều 25 Anti-AI): Thay `manage, handle, do` bằng động từ hành động cụ thể.
>    - ❌ Cấm mệnh đề "Then" mơ hồ (Điều 27 Anti-AI): Mệnh đề "Then" phải nêu kết quả cụ thể, quan sát/kiểm tra được. Dùng ngưỡng số khi quy tắc có ngưỡng; trạng thái, quyền hoặc thông báo chính xác cũng có thể là kết quả kiểm tra được. Thiếu dữ kiện thì đánh dấu `[CẦN XÁC NHẬN]`, không tự đặt ngưỡng.

---

## 4.2 Template Chuẩn — Bốn kịch bản minh họa, chọn theo nghiệp vụ và Tier

> Bộ ví dụ dưới đây dành cho giao dịch có giới hạn và tranh chấp tài nguyên. Với tính năng không có xử lý đồng thời, thay kịch bản 2 bằng tình huống có rủi ro thật. Viết `Then` theo kết quả nghiệp vụ; mã HTTP thuộc API/SRS nếu thực sự cần kiểm tra ở tầng đó. [Nguồn Gherkin](https://cucumber.io/docs/gherkin/reference/).

```text
Mã Acceptance Criteria: AC-[MODULE]-001
Thuộc User Story: US-[MODULE]-001

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
KỊCH BẢN 4: [Ngoại lệ & Vi phạm luật - Negative / Rule Violation (BR-xxx)]
===================================================================
Given [người dùng đã chạm ngưỡng giới hạn (theo quy định BR-xxx)]
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

Scenario 4: Vượt giới hạn số lịch hẹn đang chờ (BR-004)
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
