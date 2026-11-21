# User Story Map mẫu — các kiểu viết ID gặp trong dự án thật

## 1. Danh sách story

- US01. Tra cứu tài sản bằng QR
- US02. Duyệt bảng lương

### US01: Tra cứu tài sản bằng QR
> **Related BRQ-ID:** `BRQ-01`, `BRQ-01.1` | **FR-ID:** `FR-QR-01`

- **AC1-A (Thành công):** Given mã hợp lệ, When nhân viên quét, Then trang tài sản mở trong 2 giây.
- **AC1-B (Mất mạng):** Given mất mạng, When nhân viên quét, Then hiển thị dữ liệu đã lưu.

### US02: Duyệt bảng lương
> **Related BRQ-ID:** `BRQ-02` | **FR-ID:** `FR-PAY-003`

## 2. Bảng tổng hợp truy vết

| US | Tên | BRQ | FR | TC |
|---|---|---|---|---|
| US01 | Tra cứu tài sản bằng QR | BRQ-01, BRQ-01.1 | FR-QR-01 | TC-01-A, TC-01-B |
| US02 | Duyệt bảng lương | BRQ-02 | FR-PAY-003 | TC-02-A |
