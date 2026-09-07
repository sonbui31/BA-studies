# Curated Templates

Folder này chứa các template thực chiến dạng Markdown/DOCX/PDF để BA-agent dùng làm lớp tham chiếu khi sinh tài liệu.

## Cách agent dùng

- Dùng `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done` trước khi sinh hoặc review BRD, SRS, User Story và Acceptance Criteria.
- Dùng `SRS.pdf` khi sinh hoặc audit SRS để đối chiếu cấu trúc và mức độ đầy đủ.
- Sau khi tham chiếu curated template, output cuối vẫn phải tuân thủ markdown templates trong `BA-document-rule/templates/`, overlay dự án, quy tắc traceability, numbering và quality gates.
- Nội dung tiếng Việt hướng người đọc phải dùng tiếng Việt có dấu; chỉ giữ ASCII cho ID, tên file, code, endpoint, database field, command và URL.
- **Quy tắc mapping xuyên suốt:** Khi sinh bộ tài liệu, mã ID giữa 4 file phải ánh xạ chính xác theo chuỗi: `BR/SR (BRD) → FR (SRS) → US → AC`. Chi tiết xem `SKILL.md` mục "QUY TẮC TRACEABILITY MAPPING".

## File hiện có

| File | Vai trò |
|---|---|
| `01-BRD-Template.md` | Template BRD chuẩn 14 phần cho Business / Khách hàng (gồm SR, RACI, BRULE Mapping, Traceability BR↔SR) |
| `02-SRS-Template.md` | Template SRS chuẩn kỹ thuật 11 phần cho Dev / QA (gồm FR-CC, BRULE→FR Enforcement, External Interface, Mermaid diagrams) |
| `03-User-Story-Template.md` | Template User Story chuẩn INVEST & DoD cho Scrum Team (gồm Sprint Roadmap, Bảng tổng hợp, Story Points, Nguồn gốc FR, BRULE áp dụng) |
| `04-Acceptance-Criteria-Template.md` | Template AC chuẩn Given-When-Then 4+4 Scenarios (gồm Traceability FR→US→AC, 4 kịch bản bổ sung, Checklist nghiệm thu) |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.md` | Bản Markdown tổng hợp từ file gốc Word (kèm ví dụ thực chiến Đặt lịch khám) |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.docx` | Mẫu gốc Word tổng hợp (kèm ví dụ thực chiến Đặt lịch khám) |
| `SRS.pdf` | Reference SRS đầy đủ chuẩn IEEE để kiểm tra completeness |
