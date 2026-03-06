# OVERLAY: IN-HOUSE PROJECT

> **Áp dụng:** Dự án nội bộ, team ngồi cùng nhau, không ràng buộc hợp đồng
> **Đặc điểm:** Linh hoạt, tài liệu vừa đủ, iteration nhanh

---

## 1. Tài liệu bắt buộc vs Tùy chọn

| # | Tài liệu | Bắt buộc? | Mức chi tiết | Ghi chú |
|---|----------|----------|-------------|---------|
| 1 | Vision & Scope | ✅ Bắt buộc | Trung bình | 2-3 trang |
| 2 | BRD | ☐ Tùy chọn | Rút gọn | Gộp vào Vision & Scope nếu dự án nhỏ |
| 3 | Stakeholder Map | ✅ Bắt buộc | Đơn giản | RACI là đủ, bỏ Engagement Plan |
| 4 | Process Flow | ✅ Bắt buộc | Trung bình | As-Is + To-Be |
| 5 | SRS | ✅ Bắt buộc | **Rút gọn (5-8 trang)** | Gọi là "SRS Lite" |
| 6 | User Story Map | ✅ Bắt buộc | Trung bình | MoSCoW + AC là đủ |
| 7 | Data Model | ✅ Bắt buộc | Trung bình | ERD + Data Dictionary core |
| 8 | UAT Plan | ✅ Bắt buộc | Đơn giản | Có thể dùng test case trên Jira |
| 9 | Change Log | ⚠️ Khuyến nghị | Đơn giản | Tracking trên Jira cũng OK |
| 10 | Meeting Minutes | ⚠️ Khuyến nghị | Đơn giản | Quyết định + Action Items |
| 11 | Handover Checklist | ☐ Tùy chọn | — | Chỉ cần nếu team thay đổi |
| 12 | API Specification | ✅ Bắt buộc | Trung bình | Nếu có API |

---

## 2. Điều chỉnh quy trình

### Thời lượng mỗi Phase

| Phase | Thời lượng In-house | So với Generic |
|-------|-------------------|---------------|
| Inception | 1-2 tuần | Giảm — quen team, ít ceremony |
| Discovery | 2-3 tuần | Giữ nguyên |
| Elaboration | 1-2 tuần | **Giảm** — SRS lite, hỏi trực tiếp Dev |
| Delivery | N Sprints | Giữ nguyên |
| Closure | 1 tuần | **Giảm** — không cần ký hợp đồng |

### Khác biệt so với Generic

| Hạng mục | Generic | In-house |
|---------|---------|---------|
| Sign-off | Ký chính thức | Email confirm hoặc comment trên Jira |
| SRS | Đầy đủ (15-25 tr) | **Lite (5-8 tr)** — Dev ngồi cạnh để hỏi |
| Wireframe | Trung bình-Cao | **Phác thảo** — iterate nhanh |
| CR Process | Chính thức | **Flexible** — PO confirm là đủ |
| Báo cáo | Tuần | **Sprint Review** là đủ |
| Giao tiếp | Theo kênh quy định | **Hỏi trực tiếp** + document lại |

---

## 3. Bỏ qua các phần sau

- ❌ NDA / Hợp đồng
- ❌ Payment Milestone
- ❌ Communication Protocol (đã ngồi cùng)
- ❌ SRS chi tiết từng field (dùng SRS Lite)
- ❌ Formal sign-off ceremony
- ❌ Ghi hình workshop
