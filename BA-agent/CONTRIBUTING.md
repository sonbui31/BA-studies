# CONTRIBUTING — Hướng dẫn Đóng góp cho BA-Agent Framework

> **Mục đích:** Quy trình chuẩn để đóng góp template, skill, hoặc cải tiến cho framework.
> **Áp dụng:** Mọi thành viên trong team BA / AI BA.

---

## 1. Khi nào đóng góp?

| Loại | Ví dụ | Action |
|------|-------|--------|
| **Thêm template mới** | Data Migration Plan, Competitor Analysis | Tạo file trong `templates/` |
| **Thêm core guide** | New risk framework, new elicitation technique | Tạo file trong `core/` |
| **Thêm reference** | Estimation method, review checklist | Tạo file trong `references/` |
| **Thêm overlay** | Government project, Blockchain project | Tạo folder trong `overlays/` |
| **Sửa template** | Thêm section, fix lỗi, cập nhật | Edit file trực tiếp |
| **Thêm skill cho Agent** | New analysis capability | Edit `ba-specialist.md` |

---

## 2. Quy trình Đóng góp

```
1. Identify Need → Có gap nào trong framework?
2. Draft → Viết content theo structuring rules
3. Self-Review → Checklist bên dưới
4. Submit → Commit + mô tả thay đổi
5. Review → Peer BA review
6. Merge → Update CHANGELOG.md
```

---

## 3. Template Quality Checklist

Trước khi submit template mới, check:

| # | Tiêu chí | Check |
|---|---------|:-----:|
| 1 | **Có header chuẩn** — Phiên bản, Ngày, Mục đích | ☐ |
| 2 | **Có bảng Lịch sử thay đổi** | ☐ |
| 3 | **Format nhất quán** với các templates hiện tại | ☐ |
| 4 | **Placeholder rõ ràng** — dùng `{{}}` cho biến | ☐ |
| 5 | **Có ví dụ** minh họa cho mỗi section quan trọng | ☐ |
| 6 | **Có link** đến core guides liên quan | ☐ |
| 7 | **Actionable** — Dev/QC/PO có thể dùng được ngay | ☐ |
| 8 | **Không duplicate** nội dung đã có trong template khác | ☐ |
| 9 | **Pre-Flight checklist** — Nếu template mới, có cần PFC mới? | ☐ |
| 10 | **DOCUMENT-MAP.md** — Đã cập nhật bản đồ file | ☐ |

---

## 4. Core Guide Quality Checklist

| # | Tiêu chí | Check |
|---|---------|:-----:|
| 1 | **Có mục đích rõ ràng** — giải quyết gap cụ thể | ☐ |
| 2 | **Có ví dụ thực chiến** — không chỉ lý thuyết | ☐ |
| 3 | **Có integration points** — link với workflow steps nào | ☐ |
| 4 | **Không conflict** với nguyên tắc trong `principles.md` | ☐ |
| 5 | **Có lệnh kích hoạt** — `@ba-specialist [lệnh]` | ☐ |

---

## 5. Overlay Quality Checklist

| # | Tiêu chí | Check |
|---|---------|:-----:|
| 1 | **Có `overlay-config.md`** — bảng tài liệu bắt buộc vs tùy chọn | ☐ |
| 2 | **Có điều chỉnh timeline** so với generic | ☐ |
| 3 | **Có phase gate bổ sung** (nếu cần) | ☐ |
| 4 | **Có quy tắc đặc thù** (ví dụ: 5 Quy tắc Outsource) | ☐ |

---

## 6. Commit Message Format

```
[TYPE] Mô tả ngắn

TYPE:
- [ADD] Thêm mới (template, guide, skill)
- [FIX] Sửa lỗi (typo, logic error)
- [UPDATE] Cập nhật (version, content)
- [REMOVE] Xóa bỏ (deprecated content)

Ví dụ:
[ADD] post-implementation-review.md — PIR template for BABOK KA#6
[FIX] Version mismatch across README, principles, ba-specialist
[UPDATE] risk-register.md — Thêm Risk Response Strategies section
```

---

## 7. Version Bumping Rules

| Thay đổi | Version bump | Ví dụ |
|----------|:---:|---|
| **Thêm template/guide mới** | MINOR (x.Y.z) | v3.1 → v3.2 |
| **Sửa nhỏ (typo, clarification)** | PATCH (x.y.Z) | v3.2 → v3.2.1 |
| **Thay đổi cấu trúc framework** | MAJOR (X.y.z) | v3.2 → v4.0 |
| **Thêm skill cho Agent** | MINOR | v3.2 → v3.3 |

**Quy tắc:** Khi bump version → cập nhật TẤT CẢ files có version number (xem CHANGELOG.md cho danh sách).

---

## 8. Files cần update khi thêm nội dung mới

| Khi thêm... | Cập nhật files sau |
|---|---|
| Template mới | `DOCUMENT-MAP.md`, `USER-GUIDE.md`, `README.md`, `CHANGELOG.md` |
| Core guide mới | `DOCUMENT-MAP.md`, `ba-specialist.md` (nếu thêm skill), `CHANGELOG.md` |
| Overlay mới | `DOCUMENT-MAP.md`, `QUICK-START.md`, `CHANGELOG.md` |
| Reference mới | `DOCUMENT-MAP.md`, `CHANGELOG.md` |
