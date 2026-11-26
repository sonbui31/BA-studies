# FEATURE MAP
# Dự án Outsource: Hệ thống Quản lý Tài sản Bệnh viện

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Mục đích:** Chuẩn hóa lớp Feature để truy vết BRQ/BR -> FR -> Feature -> US -> TC.

---

## 1. Danh sách Feature

| Feature ID | Feature | Module | Business Ref | Business Rule |
|---|---|---|---|---|
| F01 | Đăng ký và định danh tài sản | AST | BRQ-01, BRQ-02, BRQ-03 | BR-001, BR-004 |
| F02 | Quản trị danh mục và phân quyền | ADM | BRQ-01, BRQ-04 | — |
| F03 | Điều chuyển tài sản | TRF | BRQ-04 | BR-002, BR-003, BR-006 |
| F04 | Kiểm kê và xử lý lệch | INV | BRQ-05, BRQ-06 | BR-005 |
| F05 | Bảo trì và cảnh báo | MNT | BRQ-07, BRQ-08 | BR-004 |
| F06 | Dashboard điều hành | RPT | BRQ-09 | — |

## 2. Phân rã FR → Feature → US → TC

| FR | Feature | Story | Test |
|---|---|---|---|
| FR-AST-001 | F01 | US-AST-001 | TC-AST-001 |
| FR-AST-002 | F01 | US-AST-002 | TC-AST-002 |
| FR-AST-003 | F01 | US-AST-003 | TC-AST-003 |
| FR-ADM-001 | F02 | US-ADM-001 | TC-ADM-001 |
| FR-ADM-002 | F02 | US-ADM-002 | TC-ADM-002 |
| FR-TRF-001 | F03 | US-TRF-001 | TC-TRF-001, TC-TRF-003 |
| FR-TRF-002 | F03 | US-TRF-002 | TC-TRF-002 |
| FR-TRF-003 | F03 | US-TRF-003 | TC-TRF-004 |
| FR-INV-001 | F04 | US-INV-001, US-INV-002 | TC-INV-001 |
| FR-MNT-001 | F05 | US-MNT-001 | TC-MNT-001 |
| FR-MNT-002 | F05 | US-MNT-002 | TC-MNT-002 |
| FR-RPT-001 | F06 | US-RPT-001 | TC-RPT-001 |
