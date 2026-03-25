# HƯỚNG DẪN PHÂN TÍCH ẢNH HƯỞNG (Impact Analysis Guide 2.5)

> **Mục đích:** Đảm bảo tính nhất quán (Consistency) của bộ tài liệu khi có thay đổi xảy ra.
> **Nguyên tắc:** Một thay đổi nhỏ ở thượng nguồn (BRD) có thể gây sóng thần ở hạ nguồn (UAT/Code).

---

## 1. Ma trận Truy vết (Traceability Matrix)

Khi một yêu cầu thay đổi, @ba-specialist thực hiện quét theo luồng sau:

| Level | Tài liệu | Ảnh hưởng tiềm năng |
|---|---|---|
| **L0: Vision** | `01-Vision-Scope.md` | Thay đổi mục tiêu kinh doanh, OKRs, phạm vi tổng thể. |
| **L1: Business** | `02-BRD.md` | Thay đổi quy trình nghiệp vụ, luật kinh doanh (Business Rules). |
| **L2: System** | `06-SRS.md` | Thay đổi tính năng kỹ thuật, API, Non-functional requirements. |
| **L3: Agile** | `User Story Map` | Thay đổi Acceptance Criteria, độ ưu tiên Story, Release plan. |
| **L4: Data** | `07-Data-Model.md` | Thay đổi schema, thêm/sửa field, ảnh hưởng tới báo cáo. |
| **L5: Testing** | `09-UAT-Plan.md` | Test case cũ không còn đúng, cần tạo bộ test mới. |

---

## 2. Quy trình Thực hiện (Audit Flow)

1. **Identify Change:** Xác định chính xác dòng/mục nào bị thay đổi.
2. **Scan Downstream:**
   - Dùng AI tìm các từ khóa liên quan trong toàn bộ thư mục `BA-agent/`.
   - Ví dụ: Thay đổi "Phương thức thanh toán" → Quét qua SRS, Story Map, ERD.
3. **Conflict Detection:** Phát hiện mâu thuẫn (ví dụ: BRD bảo "Thanh toán khi nhận hàng", nhưng ERD không có trường `cod_amount`).
4. **Report & Sync:** Xuất báo cáo ảnh hưởng và gợi ý các file cần cập nhật.

---

## 3. Lệnh Audit Ảnh hưởng

- `@[ba-specialist] hãy phân tích ảnh hưởng khi tôi thay đổi [tính năng X] tại file [Y]`
- `@[ba-specialist] kiểm tra tính nhất quán giữa Story Map và SRS sau đợt cập nhật này`
- `@[ba-specialist] quét toàn bộ project để tìm các requirement mâu thuẫn nhau`
