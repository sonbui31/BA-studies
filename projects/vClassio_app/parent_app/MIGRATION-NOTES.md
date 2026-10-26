# Ghi chú chuyển scheme ID: Parent App

Bộ tài liệu `parent_app_md` (BRD v0.9, SRS, User Story, Acceptance Criteria) dùng scheme ID riêng, khác scheme canonical của `BA-agent`. Chưa chuyển đổi tự động vì hai lý do: bản gốc là các file `.docx` cùng thư mục, và canonical strict đòi quan hệ 1 FR : 1 US : 1 AC, trong khi bộ hiện tại có 19 FR, 20 US và 20 AC (gần 1:1 nhưng cần đối chiếu từng cặp).

## Ánh xạ

| Hiện tại | Canonical | Số lượng ước tính |
|---|---|---|
| `BR-001`…`BR-008` | `BRQ-01`…`BRQ-08` | 8 |
| `BRULE-001`…`BRULE-019` | `BR-001`…`BR-019` | 19 |
| `SR-01`…`SR-07` | Giữ nguyên (tầng Stakeholder Requirement) | 7 |
| `FR-01.1`…`FR-07.2`, `FR-CC.01`…`FR-CC.04` | `FR-[MODULE]-001` | 19 (15 FR theo SR + 4 cross-cutting) |
| `NFR-01`…`NFR-07` | `NFR-[LOẠI]-001` | 7 |

## Việc cần quyết định trước khi chuyển

1. Chốt mã module cho từng nhóm chức năng (ví dụ Sổ liên lạc, Thời khoá biểu, Học phí, Điểm danh, Xin nghỉ, Tin tức).
2. Đối chiếu quan hệ FR → US → AC từng cặp (19 FR, 20 US, 20 AC) và xử lý phần lệch bằng cách tách FR hoặc gộp US.
3. Điền tên vào bảng Stakeholder trong BRD (cột Tên đang trống; Change Log v0.2 ghi là đã điền `TBD` nhưng bảng chưa có).
4. Cập nhật bản `.docx` gốc sau khi chuyển, để hai bản không lệch nhau.
