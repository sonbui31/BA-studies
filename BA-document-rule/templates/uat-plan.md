# UAT PLAN — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **BABOK KA:** Solution Evaluation

---

## 1. Tổng quan UAT

| Hạng mục | Chi tiết |
|---------|---------|
| **Mục tiêu** | Xác nhận hệ thống đáp ứng yêu cầu kinh doanh |
| **Phạm vi** | {{Modules / features cần UAT}} |
| **Thời gian** | {{Ngày bắt đầu}} — {{Ngày kết thúc}} |
| **Môi trường** | {{Staging / UAT environment URL}} |
| **Người thực hiện** | {{Tên end-users + BA support}} |

---

## 2. Entry / Exit Criteria

### Entry Criteria — Điều kiện BẮT ĐẦU UAT

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | Tất cả features deploy lên môi trường UAT | ☐ |
| 2 | Smoke test pass bởi QC | ☐ |
| 3 | Test data đã chuẩn bị | ☐ |
| 4 | UAT accounts đã tạo | ☐ |
| 5 | No Critical/High bugs mở | ☐ |
| 6 | User guide / training hoàn thành | ☐ |

### Exit Criteria — Điều kiện KẾT THÚC UAT

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | 100% test scenarios đã chạy | ☐ |
| 2 | Pass rate ≥ {{95%}} | ☐ |
| 3 | No Critical/High bugs mở | ☐ |
| 4 | Biên bản nghiệm thu đã ký | ☐ |

---

## 3. Test Scenarios

### Module: {{Tên Module 1}}

| TC ID | Scenario | Precondition | Steps | Expected Result | Priority | Trace |
|-------|----------|-------------|-------|----------------|----------|-------|
| TC-001 | {{Tên scenario}} | {{Điều kiện tiên quyết}} | 1. {{Bước 1}}<br>2. {{Bước 2}}<br>3. {{Bước 3}} | {{Kết quả mong đợi}} | High | FR-{{MOD}}-001 |
| TC-002 | {{Tên scenario}} | {{Precondition}} | {{Steps}} | {{Expected}} | Medium | FR-{{MOD}}-002 |

---

## 4. Bug Tracking

### Bug Report Format

| Field | Mô tả |
|-------|-------|
| **Bug ID** | BUG-{{NNN}} |
| **Title** | {{Mô tả ngắn}} |
| **Steps to Reproduce** | 1. {{Bước 1}} 2. {{Bước 2}} |
| **Expected** | {{Kết quả mong đợi}} |
| **Actual** | {{Kết quả thực tế}} |
| **Severity** | S1 Critical / S2 Major / S3 Minor / S4 Trivial |
| **Priority** | P1 Urgent / P2 High / P3 Medium / P4 Low |
| **Screenshot** | {{Đính kèm}} |
| **Environment** | {{Browser, OS, URL}} |

> Severity & Priority definition: xem `core/quality-checklist.md` > Mục 5

### Bug Summary

| Severity | Mở | Đang sửa | Đã sửa | Đã verify | Closed |
|---------|-----|---------|--------|----------|--------|
| S1 Critical | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| S2 Major | | | | | |
| S3 Minor | | | | | |
| S4 Trivial | | | | | |

---

## 5. Traceability Matrix

| BRD Req | SRS FR | User Story | Test Case | Result |
|---------|--------|-----------|-----------|--------|
| BR-001 | FR-{{MOD}}-001 | US-{{MOD}}-001 | TC-001 | ✅ / ❌ |

---

## 6. UAT Sign-off

### Biên bản nghiệm thu

| Hạng mục | Chi tiết |
|---------|---------|
| Tổng test case | {{N}} |
| Pass | {{N}} ({{%}}) |
| Fail (open) | {{N}} |
| Blocked | {{N}} |
| **Kết luận** | ☐ PASS — Đồng ý nghiệm thu / ☐ FAIL — Cần sửa và test lại |

**Ký xác nhận:**

| Vai trò | Tên | Ngày | Chữ ký |
|---------|-----|------|--------|
| Đại diện Khách hàng / PO | | | |
| PM | | | |
| BA | | | |

---

## ✅ Review Checklist

```
☐ Test scenarios cover tất cả FR
☐ Mỗi test case có: Precondition, Steps, Expected Result
☐ Entry/Exit criteria rõ ràng
☐ Traceability: FR → Test Case
☐ Test data đã chuẩn bị
☐ Bug severity/priority classification đúng
☐ Sign-off template sẵn sàng
```
