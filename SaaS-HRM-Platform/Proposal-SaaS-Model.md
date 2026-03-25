# PHƯƠNG ÁN CHI TIẾT: HỆ THỐNG QUẢN TRỊ NHÂN SỰ SAAS (HRM PLATFORM)

> **Phiên bản:** 2.0 | **Ngày:** 20/03/2026
> **Trạng thái:** Final Blueprint (User Approved)

---

## 1. Tư duy tổng thể (Core Model)
🎯 **Vai trò người dùng:**
- **User thường (Employee)**: Chấm công (Khuôn mặt + GPS), xin nghỉ, xem thông báo.
- **Admin (Company Owner - Free)**: Tạo công ty + bộ phận, mời user (bị giới hạn).
- **Admin trả phí (Pro / Subscription)**: Full quyền + không giới hạn hoặc limit lớn.

---

## 2. Luồng chính (User Flow)
- **Bước 1**: Tải app -> Đăng ký tài khoản (Personal).
- **Bước 2**: Lựa chọn:
    - **Tham gia công ty**: Nhập mã invite.
    - **Tạo công ty**: Vào luồng Admin Onboarding.
- **Bước 3 (Admin)**: Nhập Tên công ty + Bộ phận đầu tiên -> Hệ thống tự động khởi tạo Tenant (Company, Department, Role Admin) -> Bắt đầu Trial (30-90 ngày).

---

## 3. Cơ chế giới hạn & Subscription (Monetization)

### 3.1 Giai đoạn FREE (Trial / Free Plan)
Mục tiêu: Cho dùng đủ để "nghiện" nhưng đụng trần sớm để upsell.
- **User**: 5 – 20 người.
- **Bộ phận**: 2 – 3 phòng ban.
- **Thời gian**: 30 – 90 ngày.
- **Báo cáo**: Hạn chế hoặc khóa hoàn toàn.

### 3.2 Các gói đề xuất (Subscription)
- **Free**: 5 user, 1 admin, không báo cáo.
- **Basic (Tháng)**: 50 user, full chấm công/nghỉ phép, báo cáo cơ bản.
- **Pro**: 200+ user, nhiều admin, báo cáo nâng cao, Export Excel/PDF.
- **Lifetime**: Trả 1 lần, mở khóa giới hạn lớn (Dành cho Early Bird).

---

## 4. Cấu trúc dữ liệu (Backend Design)
Hệ thống sử dụng kiến trúc Multi-tenancy qua `company_id`:

- **users**: `id`, `email`, `role`, `company_id`.
- **companies**: `id`, `name`, `owner_id`, `plan_id`, `trial_expired_at`.
- **departments**: `id`, `company_id`, `name`.
- **subscriptions**: `id`, `company_id`, `plan_type`, `start_date`, `end_date`.
- **invites**: `code`, `company_id`, `role`, `expired_at`.

---

## 5. Logic "Sống còn" (Core Logic)
1. **Check Limit**: Kiểm tra `company.user_count >= plan.max_users` trước khi: Tạo user mới, Invite user, Tạo department.
2. **Check Expiration**: `if now > trial_expired_at: restrict_features()`.
3. **Invite Flow**: Gửi Link kèm `code=ABC123`. Click -> Auto Join. Hỗ trợ expire sau 24h.

---

## 6. Lộ trình phát triển tương lai
- Bổ sung cấu hình Chấm công đa địa điểm (Wifi, QR Code).
- Quản lý Ca làm việc (Shift) & OT / Payroll.
- Dashboard thống kê & API tích hợp doanh nghiệp lớn.

---

## 7. Gợi ý nâng cấp UX (Mẹo Convert Tiền 💰)
- **ProgressBar**: Hiển thị `"Bạn đã dùng 4/5 nhân viên (Free Plan)"` ngay Dashboard.
- **Upsell Popup**: Khi vượt limit, hiển thị ngay nút "Nâng cấp gói ngay" để giữ luồng làm việc.

---

## 8. Ma trận xử lý ngoại lệ (Edge Cases & Action Matrix)

Đây là các tình huống thực tế (Edge cases) có tỷ lệ xảy ra cao khi triển khai mô hình SaaS và cách hệ thống xử lý để đảm bảo dữ liệu toàn vẹn:

| Tình huống (Edge Case) | Hậu quả nếu không xử lý | Cách hệ thống xử lý (Solution) |
|-----------------------|-------------------------|--------------------------------|
| **1. Công ty hạ cấp (Downgrade) từ Basic (50 user) xuống Free (5 user)** | Admin có 40 nhân sự đang dùng nhưng chỉ trả tiền cho 5 người. Server quá tải, mất doanh thu. | - **Freeze Data**: Khóa trạng thái hoạt động (Deactivate) của 35 User mới nhất.<br>- **Read-Only Mode**: Các User này chỉ xem được lịch sử cũ, không chấm công được.<br>- Admin phải chọn 5 User được giữ lại (Active). |
| **2. Nhân viên nghỉ việc (Offboarding)** | Dữ liệu chấm công bị mất nết Admin xóa User. Hoặc Admin không thể chèn người mới vào slot cũ do full dung lượng. | - **Soft Delete**: Chuyển trạng thái User sang `Inactive` thay vì xóa hẳn.<br>- Tài khoản Inactive sẽ **lịch sử chấm công vẫn giữ nguyên** nhưng **KHÔNG chiếm Slot** (Limit) của gói hiện tại.<br>- Admin có thể dùng slot trống đó để mời nhân sự mới. |
| **3. Thanh toán gia hạn (Subscription Billing/Payment)** | MVP chưa có cổng thanh toán tự động, KH không biết cách chuyển tiền -> Gián đoạn dịch vụ. | - **Manual Approval**: Thêm màn hình hiển thị QR Code chuyển khoản kèm Cú pháp (Mã Công Ty).<br>- Admin upload ảnh giao dịch/Ủy nhiệm chi.<br>- Hệ thống tự động gia hạn ngay 3 ngày chờ (Grace period) để họ dùng tiếp trong khi kế toán kiểm tra và Click duyệt trên Back-Office. |
| **4. User cố tình spam tạo nhiều công ty (Abuse)** | Tạo 100 công ty cùng lúc để dùng thử cho 500 nhân viên miễn phí. | - Giới hạn 1 User (SĐT/Email) **chỉ được tạo tối đa 1 Công ty**. Muốn tạo công ty thứ 2 phải nâng cấp gói Pro. |

---

> [!IMPORTANT]
> **Kết luận**: Vì app hiện tại **ĐÃ CÓ sẵn Chấm công (Khuôn mặt + GPS)** kết hợp xin nghỉ + thông báo, đây là một "Killer Feature" cực mạnh so với các app chấm công truyền thống. Ta chỉ cần bọc thêm luồng **Company Creation & Invite** và **Giới hạn Limit (Monetization)** là có ngay một sản phẩm SaaS cực kỳ cạnh tranh và sẵn sàng thu tiền.
