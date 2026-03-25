# CHANGE LOG — {{TÊN DỰ ÁN}}

> **Mục đích:** Theo dõi mọi thay đổi yêu cầu sau khi baseline
> **Tham chiếu:** BABOK® — Requirements Life Cycle Management

---

## 1. Quy trình Change Request (CR)

```
Phát sinh yêu cầu thay đổi
    ↓
BA ghi nhận CR (log vào bảng dưới)
    ↓
BA phân tích Impact (phạm vi, thời gian, chi phí)
    ↓
Review meeting (BA + PM + Dev Lead)
    ↓
Trình Sponsor / PO phê duyệt
    ↓ Approved?
    ├── ✅ Approved → Cập nhật SRS/Story Map → Đưa vào Sprint
    └── ❌ Rejected → Ghi lý do, đóng CR
```

---

## 2. Phân loại CR

| Loại | Mô tả | Ai phê duyệt |
|------|-------|-------------|
| **Scope Change** | Thêm/bớt feature ngoài baseline | Sponsor |
| **Enhancement** | Cải tiến feature đã có | PO |
| **Bug/Defect** | Lỗi so với SRS (KHÔNG phải CR) | Dev Lead |
| **Clarification** | Làm rõ requirement mơ hồ | BA |

> ⚠️ **Bug ≠ CR.** Bug = hệ thống không đúng SRS. CR = thay đổi SRS.

---

## 3. Change Log

| CR ID | Ngày | Người yêu cầu | Mô tả thay đổi | Loại | Ảnh hưởng | Impact (Effort) | Impact (Cost) | Status | Người duyệt | Ngày duyệt |
|-------|------|--------------|----------------|------|----------|----------------|--------------|--------|------------|-----------|
| CR-001 | {{ngày}} | {{tên}} | {{mô tả}} | Scope / Enhancement | {{FR/Module bị ảnh hưởng}} | {{SP / man-days}} | {{$}} | Pending / Approved / Rejected | {{tên}} | {{ngày}} |

### Status Values

| Status | Ý nghĩa |
|--------|---------|
| `Pending` | Đang chờ phân tích impact |
| `Analyzing` | BA đang phân tích |
| `In Review` | Đang chờ phê duyệt |
| `Approved` | Đã phê duyệt → schedule vào Sprint |
| `Rejected` | Từ chối (ghi lý do) |
| `Implemented` | Đã triển khai |
| `Deferred` | Hoãn lại phase / release sau |

---

## 4. Impact Analysis Template

> Dùng khi phân tích chi tiết 1 CR.

### CR-{{NNN}}: {{Tên CR}}

| Hạng mục | Chi tiết |
|---------|---------|
| **Mô tả thay đổi** | {{Chi tiết}} |
| **Lý do** | {{Tại sao cần thay đổi}} |
| **SRS/Story bị ảnh hưởng** | FR-{{xxx}}, US-{{xxx}} |
| **Module bị ảnh hưởng** | {{Modules}} |
| **Effort thêm** | {{SP / man-days}} |
| **Chi phí thêm** | {{$}} (nếu outsource) |
| **Timeline impact** | {{Delay bao nhiêu ngày}} |
| **Rủi ro** | {{Rủi ro khi làm / không làm}} |
| **Đề xuất** | Approve / Reject / Defer |

---

## 5. Thống kê CR

| Metric | Giá trị |
|--------|---------|
| Tổng CR | {{N}} |
| Approved | {{N}} ({{%}}) |
| Rejected | {{N}} ({{%}}) |
| Pending | {{N}} |
| Total effort thêm | {{SP}} |
| Scope creep % | {{Effort thêm / Effort gốc × 100}}% |

> ⚠️ Scope creep > 20% → cần escalate lên Sponsor.
