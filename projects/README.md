# Projects — Dự án thực tế

Thư mục chứa các dự án thực tế / dự án mẫu sử dụng BA-agent.

---

## Danh sách dự án

| Dự án | Loại | Trạng thái | Mô tả | Tài liệu có |
|---|---|---|---|---|
| **QLTS** | In-house | Đang phát triển | Hệ thống Quản lý Tài sản — cấp phát, thu hồi, kiểm kê, báo cáo | BRD, SRS, Feature Spec, User Story Map, UAT Plan, Evaluation Report |
| **vClassio_app** | Product | Đang phát triển | Ứng dụng giáo dục VClassio — parent app, teacher app, web feature expansion | BRD, SRS, User Story, AC, BACCM Feature Expansion |
| **SaaS-HRM-Platform** | Product/SaaS | Proposal | Nền tảng quản lý nhân sự SaaS | Proposal |

---

## Cách tạo dự án mới

1. Tạo thư mục con tại `projects/<tên-dự-án>/`
2. Dùng BA-agent để phân loại dự án và chọn overlay phù hợp
3. Tham khảo bộ tài liệu mẫu:
   - **Outsource**: `BA-agent/BA-Documents-Outsource/`
   - **Product/SaaS**: `BA-agent/BA-Documents-Product/`

### Prompt tạo dự án mới

```text
Dùng BA-agent cho dự án: [tên dự án].
Mô tả ngắn: [mô tả].
Output folder: projects/[tên-dự-án]/

Hãy phân loại dự án, chọn overlay và đề xuất bộ tài liệu cần tạo.
```

---

## Cấu trúc tài liệu dự án

Mỗi dự án nên tuân theo numbering chuẩn của BA-agent:

```
projects/<tên-dự-án>/
├── 00-BA-Process-Framework.md     ← Quy trình tổng quan
├── 01-Vision-Scope.md             ← Vision & Scope
├── 02-BRD.md                      ← Business Requirements
├── 03-Stakeholder-Map.md          ← Stakeholder (outsource) / User-Personas.md (product)
├── 04-Process-Flow.md             ← As-Is / To-Be
├── 04A-Feature-Map.md             ← Feature layer map
├── 05-SRS.md                      ← System Requirements
├── 06-User-Story-Map.md           ← User Stories + AC
├── 07-Data-Model.md               ← ERD + Data Dictionary
├── 08-UAT-Plan.md                 ← UAT + nghiệm thu
├── 09-Change-Log.md               ← Change Requests
├── 10-Meeting-Minutes.md          ← Biên bản họp
└── 11-Handover-Checklist.md       ← Bàn giao (outsource)
```

> Xem chi tiết tại [BA-agent/DOCUMENT-MAP.md](../BA-agent/DOCUMENT-MAP.md)
