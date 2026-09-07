# Curated Templates

Folder này chứa các template thực chiến dạng Markdown/DOCX/PDF để BA-agent dùng làm lớp tham chiếu khi sinh tài liệu.

## Cách agent dùng

- Dùng `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done` trước khi sinh hoặc review BRD, SRS, User Story và Acceptance Criteria.
- Dùng `SRS.pdf` khi sinh hoặc audit SRS để đối chiếu cấu trúc và mức độ đầy đủ.
- Với 4 tài liệu lõi BRD/SRS/User Story/Acceptance Criteria, output cuối phải dùng chính các template curated trong folder này làm nguồn cấu trúc. `BA-document-rule/templates/` chỉ dùng cho tài liệu phụ trợ như RAID, RBAC, Risk Register, Test Strategy.
- Nội dung tiếng Việt hướng người đọc phải dùng tiếng Việt có dấu; chỉ giữ ASCII cho ID, tên file, code, endpoint, database field, command và URL.
- **Quy tắc mapping xuyên suốt:** Khi sinh bộ tài liệu mới, mã ID giữa 4 file phải ánh xạ chính xác theo chuỗi canonical: `BRQ/BR (BRD) → FR/NFR (SRS) → Feature → US → AC/TC`. Chi tiết xem `SKILL.md` mục "QUY TẮC TRACEABILITY MAPPING".

## File hiện có

| File | Vai trò |
|---|---|
| `01-BRD-Template.md` | Template BRD chuẩn 14 phần cho Business / Khách hàng (gồm BRQ, RACI, BR→FR Enforcement, Traceability BRQ↔FR) |
| `02-SRS-Template.md` | Template SRS chuẩn kỹ thuật 11 phần cho Dev / QA (gồm FR-CC, BR→FR Enforcement, External Interface, Mermaid diagrams) |
| `03-User-Story-Template.md` | Template User Story chuẩn INVEST & DoD cho Scrum Team (gồm Sprint Roadmap, Bảng tổng hợp, Story Points, Nguồn gốc FR, BR áp dụng) |
| `04-Acceptance-Criteria-Template.md` | Template AC chuẩn Given-When-Then 4+4 Scenarios (gồm Traceability FR→US→AC, 4 kịch bản bổ sung, Checklist nghiệm thu) |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.md` | Bản Markdown tổng hợp từ file gốc Word (kèm ví dụ thực chiến Đặt lịch khám) |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.docx` | Mẫu gốc Word tổng hợp (kèm ví dụ thực chiến Đặt lịch khám) |
| `SRS.pdf` | Reference SRS đầy đủ chuẩn IEEE để kiểm tra completeness |
| `media/` | Thư mục hình ảnh sơ đồ trực quan (BPMN, Use Case, ERD, Wireframe, Sequence, Activity Diagram) chuẩn hóa từ Parent App |

## Khai báo hình ảnh trong `media/`

| Nhóm ảnh | Trạng thái khai báo | Nơi sử dụng |
|---|---|---|
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done_image_01.png` → `..._06.png` | Đã nhúng trực tiếp | `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done.md` bằng relative path `media/...` |
| `BRD_BPMN_XinNghi_ToBe.jpg` và `SRS_Hinh*.jpg` | Reference-only | Được mô tả trong `media/README.md`; dùng khi cần ví dụ sơ đồ chi tiết hơn cho BRD/SRS |

> Khi thêm ảnh ví dụ mới, phải khai báo ở `media/README.md` và nếu ảnh là minh họa bắt buộc cho template thì phải nhúng trực tiếp vào template tương ứng bằng đường dẫn tương đối `media/<ten-file>`.
