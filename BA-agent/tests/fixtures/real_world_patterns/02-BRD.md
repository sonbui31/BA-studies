# BRD mẫu — các kiểu viết ID gặp trong dự án thật

> Fixture kiểm thử. Tái hiện cách viết của bộ tài liệu thật (không chứa dữ liệu khách hàng).

## 1. Yêu cầu nghiệp vụ

| BRQ-ID | Tên | Mô tả |
|---|---|---|
| **BRQ-01** | Tra cứu tài sản | Nhân viên tra cứu thông tin tài sản bằng mã QR. |
| **BRQ-01.1** | Tra cứu khi mất mạng | Nhân viên xem lại thông tin đã lưu khi mất mạng. |
| **BRQ-02** | Duyệt bảng lương | Quản lý duyệt bảng lương trước khi chi trả. |

## 2. Quy tắc nghiệp vụ

| Mã | Quy tắc | Áp dụng |
|---|---|---|
| **Rule-1** | Mỗi tài sản chỉ thuộc một khoa tại một thời điểm. | FR-QR-01 |

## 3. Ma trận truy vết

| BRQ | Tên | FR | Story | Test |
|---|---|---|---|---|
| BRQ-01 | Tra cứu tài sản | FR-QR-01 | US01 | TC-01-A |
| BRQ-01.1 | Tra cứu khi mất mạng | FR-QR-01 | US01 | TC-01-B |
| BRQ-02 | Duyệt bảng lương | FR-PAY-003 | US02 | TC-02-A |
