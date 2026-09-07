# SRS Canonical Full Bundle

## 2.1 Yêu cầu chức năng

| Mã FR | Mô tả | Trace |
|---|---|---|
| FR-AST-001 | Precondition: người dùng có quyền asset.create. Khi tạo tài sản, hệ thống phải lưu mã tài sản duy nhất trong 2 giây. | BRQ-01, BR-001, F01, US-AST-001 |
| FR-TRN-001 | Precondition: tài sản có lịch sử sở hữu. Khi người dùng mở chi tiết tài sản, hệ thống phải hiển thị lịch sử điều chuyển trong 2 giây. | BRQ-02, F02, US-TRN-001 |

## 2.2 Yêu cầu phi chức năng

| Mã NFR | Nhóm | Mô tả | Ngưỡng | Kiểm chứng |
|---|---|---|---|---|
| NFR-PERF-001 | Performance | Hệ thống phải phản hồi thao tác tạo tài sản trong ngưỡng đo được. | ≤ 2 giây p95 | AC-AST-001 |
