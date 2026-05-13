# TEST STRATEGY — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA/QC}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Định nghĩa chiến lược kiểm thử tổng thể để đảm bảo BRD/SRS/User Story được kiểm chứng qua SIT, UAT, regression và non-functional tests.

## 2. Test Scope

| In Scope | Out of Scope | Ghi chú |
|----------|--------------|---------|
| {{Module / Feature}} | {{}} | {{}} |

## 3. Test Levels

| Level | Mục tiêu | Owner | Entry Criteria | Exit Criteria |
|-------|----------|-------|----------------|---------------|
| Unit Test | Kiểm tra code-level | Dev | Code complete | Pass threshold |
| SIT | Kiểm tra tích hợp hệ thống | QC / Dev | Build stable | 0 Critical/High open |
| UAT | Nghiệm thu nghiệp vụ | Business User | SIT pass | Business sign-off |
| Regression | Đảm bảo không lỗi chức năng cũ | QC | Change deployed | Regression suite pass |

## 4. Coverage Matrix

| Requirement ID | Test Level | Test Case ID | Priority | Coverage Status |
|----------------|------------|--------------|----------|-----------------|
| FR-{{MOD}}-001 | SIT / UAT | TC-{{MOD}}-001 | Must | Covered / Missing |
| NFR-{{MOD}}-001 | Performance / Security | TC-NFR-001 | Must | Covered / Missing |

## 5. Test Data Strategy

| Data Set | Mục đích | Nguồn | Masking Required | Owner |
|----------|----------|-------|------------------|-------|
| TD-001 | Happy path | Synthetic / Production copy | Yes / No | {{}} |
| TD-002 | Boundary / Error | Synthetic | No | {{}} |

## 6. Defect Triage

| Severity | Định nghĩa | SLA xử lý | Điều kiện release |
|----------|------------|-----------|-------------------|
| Critical | Block business flow / data loss / security breach | Immediate | Không được open |
| High | Major feature unusable, có workaround khó | {{}} | Không được open trừ waiver |
| Medium | Lỗi có workaround | {{}} | Có thể release nếu accepted |
| Low | UI/content minor | {{}} | Có thể defer |

## 7. Regression Strategy

| Change Type | Regression Scope | Owner | Automation Candidate |
|-------------|------------------|-------|----------------------|
| Business rule change | Related module + downstream reports | QC | Yes / No |
| API contract change | Consumer systems + integration tests | Dev/QC | Yes |

## Review Checklist

```
☐ Mọi Must requirement có test case
☐ NFR có test approach riêng
☐ Test data đã xác định nguồn và masking
☐ Defect severity/SLA rõ ràng
☐ Regression scope dựa trên impact analysis
```
