# RACI MATRIX — Hướng dẫn & Template

> **Mục đích:** Phân công trách nhiệm rõ ràng cho từng hoạt động / tài liệu

---

## 1. Giải thích RACI

| Ký hiệu | Vai trò | Ý nghĩa | Quy tắc |
|---------|---------|---------|---------|
| **R** | Responsible | Người **thực hiện** công việc | Có thể nhiều người |
| **A** | Accountable | Người **chịu trách nhiệm** cuối cùng, phê duyệt | **CHỈ 1 người / task** |
| **C** | Consulted | Được **tham vấn** trước khi quyết định (2-way) | Hỏi ý kiến |
| **I** | Informed | Được **thông báo** sau khi quyết định (1-way) | Nhận thông tin |

### Quy tắc vàng

1. Mỗi hàng **PHẢI có đúng 1 A** — nếu không có A = không ai chịu trách nhiệm
2. Mỗi hàng **PHẢI có ít nhất 1 R** — phải có người làm
3. **A có thể = R** — người chịu trách nhiệm cũng tự thực hiện
4. **Tối thiểu C và I** — quá nhiều = bottleneck
5. Nếu 1 người vừa R vừa A → ghi là **R/A**

---

## 2. Template RACI — Theo loại dự án

### In-house

| Hoạt động / Tài liệu | BA | PM | PO | Dev Lead | Sponsor |
|----------------------|----|----|-----|---------|---------|
| Vision & Scope | **R** | A | C | I | **A** |
| Stakeholder Map | **R/A** | I | — | — | — |
| Process Flow | **R** | I | **C** | C | I |
| SRS (Lite) | **R** | A | **A** | **C** | I |
| User Story Map | **R** | C | **A** | C | I |
| Data Model | **R** | I | I | **A** | — |
| UAT Plan | **R** | A | **A** | C | I |
| Change Log | **R** | **A** | I | I | I |

### Outsource

| Hoạt động / Tài liệu | BA (NCC) | PM (NCC) | PO (KH) | Sponsor (KH) | Dev Lead |
|----------------------|----------|----------|---------|-------------|---------|
| BRD / Hợp đồng | C | **R** | **A** | **A** | C |
| Vision & Scope | **R** | A | **A** | **A** | I |
| SRS | **R** | A | **A** | I | **C** |
| Bộ tài liệu bàn giao | **R** | **A** | **A** | A | R |

> NCC = Nhà cung cấp, KH = Khách hàng

---

## 3. Sai lầm thường gặp

| Sai | Đúng |
|-----|------|
| Không có **A** → không ai sign-off | Mỗi task phải có đúng **1 A** |
| Quá nhiều **C** → họp kéo dài | Chỉ C những người thật sự cần tham vấn |
| **R** là phòng ban → ai trong phòng ban? | **R** phải là **cá nhân cụ thể** |
| A = "Ban lãnh đạo" → ai ký? | A phải là **1 người** có quyền quyết |
