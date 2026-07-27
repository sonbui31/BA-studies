# Curated Templates

Folder này chứa các template thực chiến dạng DOCX/PDF để BA-agent dùng làm lớp tham chiếu khi sinh tài liệu.

## Cách agent dùng

- Dùng `Template-tai-lieu-BA-BRD-SRS-UserStory-AC.docx` trước khi sinh hoặc review BRD, SRS, User Story và Acceptance Criteria.
- Dùng `SRS.pdf` khi sinh hoặc audit SRS để đối chiếu cấu trúc và mức độ đầy đủ.
- Sau khi tham chiếu curated template, output cuối vẫn phải tuân thủ markdown templates trong `BA-document-rule/templates/`, overlay dự án, quy tắc traceability, numbering và quality gates.
- Nội dung tiếng Việt hướng người đọc phải dùng tiếng Việt có dấu; chỉ giữ ASCII cho ID, tên file, code, endpoint, database field, command và URL.

## File hiện có

| File | Vai trò |
|---|---|
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC.docx` | Mẫu tổng hợp có cấu trúc BRD, SRS, User Story, Acceptance Criteria và ví dụ minh họa |
| `SRS.pdf` | Reference SRS đầy đủ để kiểm tra completeness |
