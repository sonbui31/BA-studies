# TÀI LIỆU YÊU CẦU NGHIỆP VỤ (BRD)
# {{Tên Feature / Epic}}

> **Phiên bản:** 1.0 | **Ngày:** {{DD/MM/YYYY}}
> **Product:** {{Tên sản phẩm}} | **Trạng thái:** Draft
> **Tham chiếu:** Vision & Scope v1.0

---

## 1. Problem Statement

> **User Problem:**
> {{Mô tả vấn đề từ góc nhìn user — không phải từ góc nhìn business}}

> **Evidence:**
> - {{Dữ liệu support ticket / churn reason / user interview}}
> - {{Analytics data: X% users drop off tại bước Y}}
> - {{Competitor Z đã giải quyết vấn đề này}}

---

## 2. User Personas

| Persona | Đặc điểm | Nhu cầu | Pain Point | Goal |
|---------|----------|---------|------------|------|
| {{Persona A}} | {{Age, role, behavior}} | {{What they need}} | {{What frustrates them}} | {{Desired outcome}} |
| {{Persona B}} | {{Age, role, behavior}} | {{What they need}} | {{What frustrates them}} | {{Desired outcome}} |

---

## 3. Success Metrics (OKRs)

| Objective | Key Result | Target | Baseline | Measurement |
|-----------|-----------|--------|----------|-------------|
| {{O1}} | {{KR1}} | {{Target}} | {{Current}} | {{Tool/Method}} |
| | {{KR2}} | {{Target}} | {{Current}} | {{Tool/Method}} |
| {{O2}} | {{KR3}} | {{Target}} | {{Current}} | {{Tool/Method}} |

---

## 4. Solution

### 4.1 Mô tả giải pháp
{{Mô tả tổng quan giải pháp, approach, và tại sao chọn cách này}}

### 4.2 User Flow
> Chi tiết tại `04-User-Flow.md`

```
[Mô tả user flow chính — hoặc link đến Figma]
```

### 4.3 Wireframe / Mockup
> Link Figma: {{URL}}

---

## 5. Yêu cầu nghiệp vụ (Business Requirements)

### 5.1 Yêu cầu chức năng

| Mã | Yêu cầu nghiệp vụ | Mô tả | Stakeholder |
|----|-------------------|-------|-------------|
| BR-001 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | {{Ai}} |
| BR-002 | {{Tên yêu cầu}} | {{Mô tả chi tiết}} | {{Ai}} |

### 5.2 Quy tắc nghiệp vụ (Business Rules)

| Mã | Quy tắc | Áp dụng cho |
|----|---------|-------------|
| BIZ-01 | {{Quy tắc}} | {{Feature}} |
| BIZ-02 | {{Quy tắc}} | {{Feature}} |

---

## 6. Feature Scope (MoSCoW + Kano)

### ✅ MUST — Bắt buộc cho Release này

| ID | Feature | User Story | Kano | Sprint |
|----|---------|-----------|------|--------|
| F-001 | {{Feature}} | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | Performance | S1 |
| F-002 | {{Feature}} | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | Performance | S1 |

### 🟡 SHOULD — Nên có

| ID | Feature | User Story | Kano | Sprint |
|----|---------|-----------|------|--------|
| F-003 | {{Feature}} | {{User Story}} | Attractive | S2 |

### 🔵 COULD — Có thể có

| ID | Feature | User Story | Kano | Sprint |
|----|---------|-----------|------|--------|
| F-004 | {{Feature}} | {{User Story}} | Attractive | S3+ |

### ❌ WON'T (đợt này)

| Feature | Lý do | Xem xét lại |
|---------|-------|-------------|
| {{Feature}} | {{Lý do}} | {{Timeline}} |

---

## 7. Out of Scope

- {{Những gì KHÔNG làm trong BRD này}}
- {{Ranh giới rõ ràng}}

---

## 8. Dependencies & Assumptions

### Dependencies
| # | Dependency | Team/Service | Status |
|---|-----------|-------------|--------|
| 1 | {{Phụ thuộc}} | {{Team}} | {{Status}} |

### Assumptions
1. {{Giả định}}
2. {{Giả định}}

---

## 9. Risks & Mitigations

| # | Risk | Probability | Impact | Mitigation |
|---|------|------------|--------|------------|
| 1 | {{Rủi ro}} | High/Med/Low | High/Med/Low | {{Cách giảm thiểu}} |
| 2 | {{Rủi ro}} | High/Med/Low | High/Med/Low | {{Cách giảm thiểu}} |

---

## 10. Open Questions

| # | Question | Owner | Deadline | Answer |
|---|---------|-------|----------|--------|
| 1 | {{Câu hỏi chưa trả lời}} | {{Ai}} | {{Khi nào}} | |

---

## 11. Release & Rollout Plan

| Phase | % Users | Duration | Criteria chuyển tiếp |
|-------|---------|----------|--------------------|
| Internal Testing | Team only | 1 tuần | 0 Critical bugs |
| Beta (Closed) | 5% users | 1-2 tuần | NPS ≥ 7, no major issues |
| Beta (Open) | 20% users | 1 tuần | Metrics stable |
| GA (General Availability) | 100% users | — | OKRs on track |

---

## 12. Ma trận truy vết (RTM)

| Mục tiêu NV | BR liên quan | Feature | Sprint |
|-------------|-------------|---------|--------|
| {{Objective 1}} | BR-001, BR-002 | F-001, F-002 | S1 |
| {{Objective 2}} | BR-003 | F-003 | S2 |

---

## 13. Phê duyệt

| Vai trò | Họ tên | Chữ ký | Ngày |
|---------|--------|--------|------|
| Product Lead | | | |
| PM / BA | | | |

> **Quy tắc:** Sau khi approved, mọi thay đổi yêu cầu phải qua quy trình CR (`09-Release-Notes.md`)

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Người |
|-----------|------|----------|-------|
| 0.1 | | Draft đầu tiên | PM/BA |
| 1.0 | | Approved — bắt đầu Build | PM/BA |
