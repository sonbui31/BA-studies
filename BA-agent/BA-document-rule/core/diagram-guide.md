# HƯỚNG DẪN VẼ SƠ ĐỒ BA

Chuẩn vẽ sơ đồ nằm ở một nơi duy nhất: **`BA-agent/so_do.md`**. File này chỉ giữ chỗ cho các liên kết cũ.

| Cần | Mục trong `so_do.md` |
|---|---|
| Khối khai báo giao diện và bộ lớp màu | 1.1 |
| Mười quy tắc chung | 1.2 |
| Chọn loại sơ đồ theo tài liệu và người đọc | 2 |
| Hình khối, đường nối | 3 |
| Quy trình nghiệp vụ BPMN 2.0 (bpmn.io), bản mô tả `.json`, phác thảo Mermaid | 4 |
| Context, Use Case, Sequence, State, ERD, Decision, Journey, Gantt | 5–12 |
| Kiểm tra trước khi gửi | 13 |

Kiểm tra tự động: `python BA-agent/scripts/bpmn_tool.py check <thư-mục>` cho BPMN, `python BA-agent/scripts/diagram_check.py <file-hoặc-thư-mục>` cho Mermaid.
