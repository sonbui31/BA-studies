# SRS mẫu — các kiểu viết ID gặp trong dự án thật

## 1. Yêu cầu chức năng

- **FR-QR-01: Quét mã QR mở trang tài sản**
  - **Nguồn:** BRQ-01, BRQ-01.1
  - **Mô tả:** Camera điện thoại quét mã, trình duyệt mở trang chi tiết tài sản.

#### FR-PAY-003 — Duyệt bảng lương

| Thuộc tính | Chi tiết |
|---|---|
| ID | FR-PAY-003 |
| Truy vết | BRQ-02 |

| Mã | Yêu cầu |
|---|---|
| FR-PAY-003.1 | Hệ thống phải cho phép kế toán gửi bảng lương để quản lý duyệt. |
| FR-PAY-003.2 | Hệ thống phải khóa bảng lương đã duyệt. |

## 2. Quy tắc nghiệp vụ áp dụng

| Mã | Quy tắc | FR |
|---|---|---|
| BR-PAY-001 | Bảng lương đã duyệt không được sửa trực tiếp. | FR-PAY-003.2 |
