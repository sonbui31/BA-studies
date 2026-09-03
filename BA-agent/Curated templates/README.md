# Curated Templates

Folder này chứa các template thực chiến dạng DOCX/PDF để BA-agent dùng làm lớp tham chiếu khi sinh tài liệu.

## Cách agent dùng

- Dùng `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done` trước khi sinh hoặc review BRD, SRS, User Story và Acceptance Criteria.
- Dùng `SRS.pdf` khi sinh hoặc audit SRS để đối chiếu cấu trúc và mức độ đầy đủ.
- Sau khi tham chiếu curated template, output cuối vẫn phải tuân thủ markdown templates trong `BA-document-rule/templates/`, overlay dự án, quy tắc traceability, numbering và quality gates.
- Nội dung tiếng Việt hướng người đọc phải dùng tiếng Việt có dấu; chỉ giữ ASCII cho ID, tên file, code, endpoint, database field, command và URL.

## File hiện có

| File | Vai trò |
|---|---|
| `01-BRD-Template.md` | Template BRD chuẩn 11 phần cho Business / Khách hàng |
| `02-SRS-Template.md` | Template SRS chuẩn kỹ thuật 9 phần cho Dev / QA |
| `03-User-Story-Template.md` | Template User Story chuẩn INVEST & DoD cho Scrum Team |
| `04-Acceptance-Criteria-Template.md` | Template Acceptance Criteria chuẩn Given-When-Then 4 Scenarios |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.docx` | Mẫu gốc Word tổng hợp (kèm ví dụ thực chiến Đặt lịch khám) |
| `SRS.pdf` | Reference SRS đầy đủ chuẩn IEEE để kiểm tra completeness |
