# Kế hoạch UAT mẫu — các kiểu viết ID gặp trong dự án thật

## 1. Kịch bản kiểm thử

| TC | Kịch bản | Story | Kết quả mong đợi |
|---|---|---|---|
| **TC-01-A** | Quét QR hợp lệ | US01 | Trang tài sản mở trong 2 giây. |
| **TC-01-B** | Quét khi mất mạng | US01 | Hiển thị dữ liệu đã lưu. |
| **TC-02-A** | Duyệt bảng lương | US02 | Bảng lương chuyển sang Đã duyệt và bị khóa. |

## 2. Các bước kiểm thử

| Kịch bản | Bước | Mô tả |
|---|---|---|
| TC-01-A | 1 | Mở camera, quét tem QR trên tài sản. |
| TC-01-A | 2 | Kiểm tra thời gian mở trang. |
| TC-02-A | 1 | Kế toán gửi bảng lương, quản lý bấm Duyệt. |
