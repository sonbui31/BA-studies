# TÀI LIỆU YÊU CẦU NGHIỆP VỤ (BRD)
# {{Tên Feature / Epic}}

> **Phiên bản:** 1.0 | **Ngày:** {{DD/MM/YYYY}}
> **Product:** {{Tên sản phẩm}} | **Trạng thái:** Draft
> **Tham chiếu:** Vision & Scope v1.0

---

## 1. Vấn đề cần giải quyết

> **Vấn đề người dùng gặp phải:**
> {{Mô tả vấn đề từ góc nhìn người dùng — không phải từ góc nhìn kinh doanh}}

> **Bằng chứng / Số liệu:**
> - {{Dữ liệu phản hồi khách hàng / lý do rời bỏ / phỏng vấn người dùng}}
> - {{Thống kê: X% người dùng bỏ dở tại bước Y}}
> - {{Đối thủ Z đã giải quyết vấn đề này}}

---

## 2. Nhóm người dùng mục tiêu

| Nhóm người dùng | Đặc điểm | Nhu cầu | Khó khăn / Nỗi đau | Mục tiêu |
|-----------------|----------|---------|---------------------|----------|
| {{Persona A}} | {{Tuổi, vai trò, hành vi}} | {{Họ cần gì}} | {{Điều gì khiến họ bực mình}} | {{Kết quả mong muốn}} |
| {{Persona B}} | {{Tuổi, vai trò, hành vi}} | {{Họ cần gì}} | {{Điều gì khiến họ bực mình}} | {{Kết quả mong muốn}} |

---

## 3. Chỉ tiêu đo lường thành công (OKRs)

| Mục tiêu | Kết quả then chốt | Chỉ tiêu | Hiện tại | Công cụ đo |
|----------|--------------------|----------|----------|------------|
| {{O1}} | {{KR1}} | {{Target}} | {{Current}} | {{Công cụ}} |
| | {{KR2}} | {{Target}} | {{Current}} | {{Công cụ}} |
| {{O2}} | {{KR3}} | {{Target}} | {{Current}} | {{Công cụ}} |

---

## 4. Giải pháp đề xuất

### 4.1 Mô tả giải pháp
{{Mô tả tổng quan giải pháp, approach, và tại sao chọn cách này}}

### 4.2 Luồng thao tác người dùng
> Chi tiết tại `04-User-Flow.md`

```
[Mô tả user flow chính — hoặc link đến Figma]
```

### 4.3 Giao diện phác thảo
> Link Figma: {{URL}}

---

## 5. Yêu cầu nghiệp vụ (Business Requirements)

### 5.1 Yêu cầu chức năng

| Mã | Yêu cầu nghiệp vụ | Mô tả | Bên liên quan |
|----|-------------------|-------|---------------|
| BR-001 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | {{Ai}} |
| BR-002 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | {{Ai}} |

### 5.2 Quy tắc nghiệp vụ (Business Rules)

| Mã | Quy tắc | Áp dụng cho |
|----|---------|-------------|
| BIZ-01 | {{Quy tắc}} | {{Feature}} |
| BIZ-02 | {{Quy tắc}} | {{Feature}} |

---

## 6. Phạm vi tính năng (Phân loại ưu tiên)

### ✅ BẮT BUỘC (Must) — Không có không nghiệm thu

| ID | Tính năng | Mô tả nhu cầu | Phân loại giá trị | Giai đoạn |
|----|-----------|---------------|-------------------|----------|
| F-001 | {{Feature}} | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | Nâng cao (Performance) | GĐ1 |
| F-002 | {{Feature}} | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | Nâng cao (Performance) | GĐ1 |

### 🟡 NÊN CÓ (Should) — Quan trọng nhưng có thể dời

| ID | Tính năng | Mô tả nhu cầu | Phân loại giá trị | Giai đoạn |
|----|-----------|---------------|-------------------|----------|
| F-003 | {{Feature}} | {{Mô tả nhu cầu}} | Gây ấn tượng (Attractive) | GĐ2 |

### 🔵 CÓ THỂ (Could) — Làm nếu còn thời gian

| ID | Tính năng | Mô tả nhu cầu | Phân loại giá trị | Giai đoạn |
|----|-----------|---------------|-------------------|----------|
| F-004 | {{Feature}} | {{Mô tả nhu cầu}} | Gây ấn tượng (Attractive) | GĐ3+ |

### ❌ CHƯA LÀM (Won't) — Loại bỏ đợt này

| Feature | Lý do | Xem xét lại |
|---------|-------|-------------|
| {{Feature}} | {{Lý do}} | {{Timeline}} |

---

## 7. Ngoài phạm vi

- {{Những gì KHÔNG làm trong BRD này}}
- {{Ranh giới rõ ràng}}

---

## 8. Phụ thuộc & Giả định

### Phụ thuộc (Dependencies)
| # | Phụ thuộc vào | Đội / Dịch vụ | Trạng thái |
|---|-----------|-------------|--------|
| 1 | {{Phụ thuộc}} | {{Team}} | {{Status}} |

### Assumptions
1. {{Giả định}}
2. {{Giả định}}

---

## 9. Rủi ro & Giải pháp giảm thiểu

| # | Rủi ro | Xác suất | Mức ảnh hưởng | Giải pháp giảm thiểu |
|---|--------|----------|---------------|----------------------|
| 1 | {{Rủi ro}} | Cao/TB/Thấp | Cao/TB/Thấp | {{Cách giảm thiểu}} |
| 2 | {{Rủi ro}} | Cao/TB/Thấp | Cao/TB/Thấp | {{Cách giảm thiểu}} |

---

## 10. Câu hỏi chưa có lời đáp

| # | Câu hỏi | Phụ trách | Hạn trả lời | Đáp án |
|---|---------|-----------|-------------|--------|
| 1 | {{Câu hỏi chưa trả lời}} | {{Ai}} | {{Khi nào}} | |

---

## 11. Kế hoạch Phát hành & Triển khai

| Giai đoạn | % Người dùng | Thời gian | Tiêu chí chuyển tiếp |
|-----------|-------------|-----------|----------------------|
| Kiểm thử nội bộ | Chỉ đội ngũ | 1 tuần | 0 lỗi nghiêm trọng |
| Thử nghiệm kín (Beta) | 5% người dùng | 1-2 tuần | NPS ≥ 7, không có sự cố lớn |
| Thử nghiệm mở | 20% người dùng | 1 tuần | Các chỉ số ổn định |
| Ra mắt chính thức | 100% người dùng | — | Đạt mục tiêu OKRs |

---

## 12. Ma trận truy vết (RTM — Requirement Traceability Matrix)

| Mục tiêu nghiệp vụ | Yêu cầu liên quan | Tính năng | Giai đoạn |
|-------------|-------------|---------|--------|
| {{Objective 1}} | BR-001, BR-002 | F-001, F-002 | S1 |
| {{Objective 2}} | BR-003 | F-003 | S2 |

---

## 13. Phê duyệt

| Vai trò | Họ tên | Chữ ký | Ngày |
|---------|--------|--------|------|
| Product Lead | | | |
| PM / BA | | | |

> **Quy tắc:** Sau khi phê duyệt, mọi thay đổi yêu cầu phải qua quy trình Yêu cầu Thay đổi (CR) — xem `09-Release-Notes.md`

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Người |
|-----------|------|----------|-------|
| 0.1 | | Draft đầu tiên | PM/BA |
| 1.0 | | Approved — bắt đầu Build | PM/BA |
