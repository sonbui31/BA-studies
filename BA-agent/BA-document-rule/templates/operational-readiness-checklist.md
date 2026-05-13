# OPERATIONAL READINESS CHECKLIST — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Xác nhận hệ thống, đội vận hành, người dùng, dữ liệu, hỗ trợ và quy trình fallback đã sẵn sàng trước go-live.

## 2. Go-Live Readiness Summary

| Area | Status | Owner | Evidence | Blocker |
|------|:------:|-------|----------|---------|
| Scope & Sign-off | Green / Amber / Red | {{}} | {{Link}} | {{}} |
| Data Migration | Green / Amber / Red | {{}} | {{Link}} | {{}} |
| Training | Green / Amber / Red | {{}} | {{Link}} | {{}} |
| Support | Green / Amber / Red | {{}} | {{Link}} | {{}} |
| Monitoring | Green / Amber / Red | {{}} | {{Link}} | {{}} |

## 3. Cutover Plan

| Step | Thời gian | Hành động | Owner | Dependency | Rollback Point |
|------|-----------|-----------|-------|------------|----------------|
| 1 | {{}} | {{Backup dữ liệu}} | {{}} | {{}} | RP-01 |
| 2 | {{}} | {{Deploy release}} | {{}} | {{}} | RP-02 |
| 3 | {{}} | {{Smoke test}} | {{}} | {{}} | RP-03 |

## 4. Support Model

| Level | Trách nhiệm | Kênh tiếp nhận | SLA phản hồi | Escalation |
|-------|-------------|----------------|--------------|------------|
| L1 | Tiếp nhận và phân loại | Hotline / Ticket / Chat | {{}} | L2 |
| L2 | Phân tích nghiệp vụ/kỹ thuật | Ticket | {{}} | L3 |
| L3 | Fix code/infrastructure | Ticket | {{}} | Vendor/Dev Lead |

## 5. Training and Adoption

| Nhóm người dùng | Nội dung đào tạo | Format | Ngày | Trainer | Evidence |
|-----------------|------------------|--------|------|---------|----------|
| {{Role}} | {{Module}} | Online / Offline / Video | {{}} | {{}} | {{Attendance / recording}} |

## 6. Monitoring and Alerts

| Metric | Threshold | Alert Channel | Owner | Runbook |
|--------|-----------|---------------|-------|---------|
| API error rate | > {{x}}% trong {{n}} phút | {{}} | {{}} | {{Link}} |
| Job failure | >= 1 critical job fail | {{}} | {{}} | {{Link}} |

## 7. Rollback Criteria

| Criteria ID | Điều kiện rollback | Người quyết định | Hành động |
|-------------|--------------------|------------------|-----------|
| RB-001 | Lỗi Critical không workaround sau {{N}} giờ | Sponsor / PM | Kích hoạt rollback plan |

## Final Go/No-Go

| Quyết định | Người quyết định | Ngày | Điều kiện còn lại |
|------------|------------------|------|-------------------|
| Go / No-Go | {{}} | {{}} | {{}} |

## Review Checklist

```
☐ Cutover plan có owner và rollback point
☐ Support model có SLA và escalation
☐ Training có evidence
☐ Monitoring có threshold và owner
☐ Go/No-Go decision được ghi nhận
```
