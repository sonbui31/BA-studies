# BRD — BUSINESS REQUIREMENTS DOCUMENT
# {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## Lịch sử thay đổi

| Phiên bản | Ngày | Người chỉnh | Mô tả thay đổi |
|-----------|------|-------------|----------------|
| 0.1 | {{ngày}} | {{tên}} | Phiên bản đầu tiên |

## Phê duyệt

| Vai trò | Tên | Ngày ký | Chữ ký |
|---------|-----|---------|--------|
| BA | | | |
| PM | | | |
| Sponsor | | | |

---

## 1. Giới thiệu

### 1.1 Mục đích tài liệu

Tài liệu này mô tả yêu cầu kinh doanh (business requirements) cho dự án {{Tên dự án}}, bao gồm nhu cầu kinh doanh, phân tích tính khả thi, và yêu cầu cấp cao.

### 1.2 Đối tượng đọc

| Đối tượng | Mục đích đọc |
|-----------|-------------|
| Sponsor / C-level | Phê duyệt dự án, đánh giá ROI |
| PM | Lập kế hoạch dự án |
| BA | Cơ sở để viết SRS |
| Dev Lead | Đánh giá tính khả thi kỹ thuật |

### 1.3 Tham chiếu

| Tài liệu | Mô tả |
|-----------|-------|
| Vision & Scope | Tầm nhìn và phạm vi dự án |
| {{Tài liệu khác}} | {{Mô tả}} |

---

## 2. Nhu cầu kinh doanh (Need — BACCM)

### 2.1 Phân tích 5W1H

| Câu hỏi | Trả lời |
|---------|---------|
| **What** — Cần làm gì? | {{Mô tả giải pháp ở mức cao}} |
| **Why** — Tại sao cần? | {{Vấn đề / cơ hội kinh doanh}} |
| **Who** — Ai sử dụng / ai quyết định? | {{Stakeholder chính}} |
| **When** — Khi nào cần hoàn thành? | {{Timeline}} |
| **Where** — Triển khai ở đâu? | {{Platform / thị trường}} |
| **How** — Thực hiện như thế nào? | {{Phương pháp / approach}} |

### 2.2 Vấn đề hiện tại (As-Is Pain Points)

| # | Vấn đề | Ai bị ảnh hưởng | Tần suất | Chi phí ảnh hưởng |
|---|--------|----------------|---------|-------------------|
| 1 | {{Vấn đề}} | {{Stakeholder}} | {{Hàng ngày / tuần / tháng}} | {{Ước tính}} |

---

## 3. SWOT Analysis

```
         Tích cực (+)                    Tiêu cực (-)
       ┌──────────────────────┐       ┌──────────────────────┐
 Nội   │      STRENGTHS       │       │     WEAKNESSES       │
 bộ    │                      │       │                      │
       │ • {{Điểm mạnh 1}}   │       │ • {{Điểm yếu 1}}    │
       │ • {{Điểm mạnh 2}}   │       │ • {{Điểm yếu 2}}    │
       │                      │       │                      │
       └──────────────────────┘       └──────────────────────┘
       ┌──────────────────────┐       ┌──────────────────────┐
 Bên   │    OPPORTUNITIES     │       │       THREATS        │
 ngoài │                      │       │                      │
       │ • {{Cơ hội 1}}      │       │ • {{Nguy cơ 1}}     │
       │ • {{Cơ hội 2}}      │       │ • {{Nguy cơ 2}}     │
       │                      │       │                      │
       └──────────────────────┘       └──────────────────────┘
```

---

## 4. Yêu cầu kinh doanh cấp cao

### 4.1 Danh sách yêu cầu (MoSCoW Priority)

| Req ID | Yêu cầu | Mô tả | MoSCoW | Kano |
|--------|---------|-------|--------|------|
| BR-001 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | Must | Basic |
| BR-002 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | Must | Basic |
| BR-003 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | Should | Performance |
| BR-004 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | Could | Excitement |
| BR-005 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | Won't | — |

> **Tham chiếu phân loại:**
> - MoSCoW: xem `core/principles.md` > Mục 3
> - Kano: xem `core/principles.md` > Mục 4

### 4.2 Thống kê phân bổ MoSCoW

| Priority | Số lượng | % | Khuyến nghị |
|----------|---------|---|-------------|
| Must | {{x}} | {{%}} | ~60% |
| Should | {{x}} | {{%}} | ~20% |
| Could | {{x}} | {{%}} | ~15% |
| Won't | {{x}} | {{%}} | ~5% |

> ⚠️ Nếu Must > 60% → cần review lại: có thật sự phải Must không?

---

## 5. Stakeholder Analysis

> Chi tiết: xem `stakeholder-map.md`

| Stakeholder | Vai trò | Interest | Power | Chiến lược quản lý |
|-------------|---------|----------|-------|-------------------|
| {{Tên}} | {{Vai trò}} | Cao/Thấp | Cao/Thấp | Manage Closely / Keep Satisfied / Keep Informed / Monitor |

---

## 6. Use Case tổng quan

```mermaid
graph LR
    subgraph "🖥️ {{TÊN HỆ THỐNG}}"
        UC1(["{{Use Case 1}}"])
        UC2(["{{Use Case 2}}"])
        UC3(["{{Use Case 3}}"])
    end

    A1("👤 {{Actor 1}}") --- UC1
    A1 --- UC2
    A2("👤 {{Actor 2}}") --- UC3
```

---

## 7. Phân tích tính khả thi (Feasibility)

### 7.1 Khả thi kỹ thuật

| Tiêu chí | Đánh giá | Ghi chú |
|----------|---------|---------|
| Công nghệ có sẵn | ✅ / ⚠️ / ❌ | {{Chi tiết}} |
| Team có kinh nghiệm | ✅ / ⚠️ / ❌ | {{Chi tiết}} |
| Hạ tầng | ✅ / ⚠️ / ❌ | {{Chi tiết}} |
| Tích hợp hệ thống | ✅ / ⚠️ / ❌ | {{Chi tiết}} |

### 7.2 Khả thi kinh doanh (ROI)

| Hạng mục | Năm 1 | Năm 2 | Năm 3 |
|---------|-------|-------|-------|
| Chi phí đầu tư | {{$}} | — | — |
| Chi phí vận hành / năm | {{$}} | {{$}} | {{$}} |
| Lợi ích dự kiến / năm | {{$}} | {{$}} | {{$}} |
| **ROI lũy kế** | {{$}} | {{$}} | {{$}} |

### 7.3 Khả thi thời gian

| Phase | Thời lượng dự kiến | Deadline cứng? |
|-------|-------------------|---------------|
| {{Phase}} | {{Tuần}} | Có / Không |

---

## 8. Rủi ro & Giải pháp giảm thiểu

| # | Rủi ro | Xác suất | Ảnh hưởng | Risk Score | Giải pháp |
|---|--------|---------|-----------|-----------|-----------|
| 1 | {{Rủi ro}} | C/TB/T | C/TB/T | {{H/M/L}} | {{Mitigation}} |

> **Risk Score:** Cao × Cao = High, còn lại = Medium/Low

---

## 9. Giả định & Ràng buộc

### Giả định

| # | Giả định | Nếu sai → ảnh hưởng |
|---|---------|---------------------|
| 1 | {{Giả định}} | {{Hậu quả}} |

### Ràng buộc

| # | Ràng buộc | Loại |
|---|----------|------|
| 1 | {{Ràng buộc}} | Kỹ thuật / Kinh doanh / Pháp lý / Thời gian |

---

## 10. Tiêu chí thành công

| # | Tiêu chí | KPI | Target | Cách đo |
|---|---------|-----|--------|---------|
| 1 | {{Tiêu chí}} | {{Metric}} | {{Mục tiêu}} | {{Phương pháp}} |

---

## ✅ BACCM Self-Check

```
☐ CHANGE:      Vấn đề / cơ hội kinh doanh rõ ràng (Mục 2)
☐ NEED:        Nhu cầu gốc đã phân tích (5W1H — Mục 2.1)
☐ SOLUTION:    Phạm vi giải pháp phù hợp (Use Case — Mục 6)
☐ STAKEHOLDER: Stakeholder đầy đủ + phân loại (Mục 5)
☐ VALUE:       ROI / cost-benefit đã tính (Mục 7.2)
☐ CONTEXT:     SWOT + ràng buộc ghi nhận (Mục 3, 9)
```
