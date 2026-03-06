# STAKEHOLDER MAP — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft

---

## 1. Danh sách Stakeholder

| # | Tên / Vai trò | Bộ phận / Tổ chức | Liên hệ | Loại |
|---|--------------|-------------------|---------|------|
| 1 | {{Tên}} | {{Bộ phận}} | {{Email / Phone}} | Nội bộ / Bên ngoài |

---

## 2. Power / Interest Grid

> Phân loại stakeholder để xác định **chiến lược giao tiếp** phù hợp.

```
     Ảnh hưởng (Power) CAO
             │
    ┌────────┼────────┐
    │ Keep   │ Manage │
    │Satisfied│Closely │ ← Sponsor, PO, C-level
    │        │  ★★★   │
    ├────────┼────────┤
    │Monitor │ Keep   │
    │ (Min   │Informed│ ← End-users, SME
    │Effort) │        │
    └────────┼────────┘
             │
     Quan tâm (Interest) CAO
```

### Chi tiết phân loại

| Stakeholder | Power | Interest | Quadrant | Chiến lược |
|-------------|-------|----------|----------|-----------|
| {{Sponsor}} | Cao | Cao | **Manage Closely** | Họp định kỳ, sign-off các deliverable chính |
| {{PO}} | Cao | Cao | **Manage Closely** | Tham gia Sprint Review, confirm requirements |
| {{Dev Lead}} | Trung bình | Cao | **Keep Informed** | Review kỹ thuật, tham vấn giải pháp |
| {{End-user}} | Thấp | Cao | **Keep Informed** | Workshop, UAT, feedback sessions |
| {{CFO}} | Cao | Thấp | **Keep Satisfied** | Báo cáo tài chính định kỳ |
| {{Đội IT hạ tầng}} | Thấp | Thấp | **Monitor** | Thông báo khi cần deployment |

### Chiến lược giao tiếp theo Quadrant

| Quadrant | Hành động | Tần suất | Kênh |
|----------|----------|---------|------|
| **Manage Closely** (High Power, High Interest) | Tham gia trực tiếp, sign-off | Hàng tuần | Meeting, Email chính thức |
| **Keep Satisfied** (High Power, Low Interest) | Update chủ động, tránh bất ngờ | 2 tuần / tháng | Email tóm tắt, Dashboard |
| **Keep Informed** (Low Power, High Interest) | Chia sẻ thông tin, lấy feedback | Hàng tuần | Slack/Teams, Workshop |
| **Monitor** (Low Power, Low Interest) | Theo dõi tối thiểu | Khi cần | Email thông báo |

---

## 3. RACI Matrix — Trách nhiệm theo tài liệu

> **R** = Responsible (Thực hiện) | **A** = Accountable (Phê duyệt)
> **C** = Consulted (Tham vấn) | **I** = Informed (Thông báo)

| Tài liệu / Hoạt động | {{BA}} | {{PM}} | {{PO}} | {{Dev Lead}} | {{Sponsor}} |
|----------------------|--------|--------|--------|-------------|-------------|
| Vision & Scope | **R** | A | C | I | **A** |
| BRD | **R** | A | **A** | C | **A** |
| Stakeholder Map | **R/A** | I | C | — | — |
| Process Flow | **R** | I | **C** | C | I |
| SRS | **R** | A | **A** | **C** | I |
| User Story Map | **R** | C | **A** | C | I |
| Data Model | **R** | I | I | **A** | — |
| UAT Plan | **R** | A | **A** | C | A |
| Change Log | **R** | **A** | **A** | I | I |
| Sprint Review | C | R | **A** | C | I |

---

## 4. Stakeholder Engagement Plan

| Stakeholder | Kỳ vọng chính | Mối lo ngại | Cách address | Owner |
|-------------|--------------|------------|-------------|-------|
| {{Sponsor}} | {{Kỳ vọng}} | {{Lo ngại}} | {{Giải pháp}} | {{BA/PM}} |
| {{PO}} | {{Kỳ vọng}} | {{Lo ngại}} | {{Giải pháp}} | {{BA}} |
| {{End-user}} | {{Kỳ vọng}} | {{Lo ngại}} | {{Giải pháp}} | {{BA}} |

---

## 5. Onion Diagram — Các tầng ảnh hưởng

```
┌─────────────────────────────────────────────────┐
│                    Bên ngoài                     │
│   Đối thủ, Cơ quan quản lý, Đối tác            │
│  ┌─────────────────────────────────────────┐    │
│  │              Tổ chức                     │    │
│  │   Ban lãnh đạo, Phòng ban liên quan     │    │
│  │  ┌─────────────────────────────────┐    │    │
│  │  │           Dự án                  │    │    │
│  │  │   PM, BA, Dev, QC, Designer     │    │    │
│  │  │  ┌─────────────────────────┐    │    │    │
│  │  │  │       Hệ thống          │    │    │    │
│  │  │  │   End-users trực tiếp   │    │    │    │
│  │  │  └─────────────────────────┘    │    │    │
│  │  └─────────────────────────────────┘    │    │
│  └─────────────────────────────────────────┘    │
└─────────────────────────────────────────────────┘
```

---

## ✅ Review Checklist

```
☐ Tất cả stakeholder key đã được nhận diện
☐ Power / Interest phân loại chính xác
☐ RACI matrix không có task thiếu "A" (phải có 1 A cho mỗi task)
☐ Chiến lược giao tiếp phù hợp quadrant
☐ Mối lo ngại + cách address đã ghi
```
