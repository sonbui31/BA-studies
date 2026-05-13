# RAID LOG — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

RAID Log theo dõi tập trung **Risks, Assumptions, Issues, Dependencies** để tránh mất thông tin giữa BRD, SRS, sprint planning và sign-off.

## 2. Status Rules

| Status | Ý nghĩa | Quy tắc xử lý |
|--------|---------|---------------|
| Open | Mới ghi nhận | Phải có owner và next action |
| In Progress | Đang xử lý | Cập nhật mỗi tuần/sprint |
| Blocked | Đang chặn tiến độ | Escalate trong 24 giờ |
| Closed | Đã xử lý | Ghi rõ evidence hoặc decision |

## 3. Risks

| ID | Risk | Impact | Probability | Score | Owner | Mitigation | Status | Due Date |
|----|------|:------:|:-----------:|:-----:|-------|------------|--------|----------|
| RSK-001 | {{Rủi ro}} | 1-5 | 1-5 | {{}} | {{}} | {{}} | Open | {{}} |

## 4. Assumptions

| ID | Assumption | Impact nếu sai | Validation Method | Owner | Validate By | Result | Status |
|----|------------|----------------|-------------------|-------|-------------|--------|--------|
| ASM-001 | {{Giả định}} | High / Medium / Low | Ask / Data Check / Prototype / Expert Review | {{}} | {{}} | {{}} | Open |

## 5. Issues

| ID | Issue | Severity | Tác động | Owner | Next Action | Due Date | Status |
|----|-------|----------|----------|-------|-------------|----------|--------|
| ISS-001 | {{Vấn đề đã xảy ra}} | Critical / High / Medium / Low | {{}} | {{}} | {{}} | {{}} | Open |

## 6. Dependencies

| ID | Dependency | Type | Needed By | Provider | Impact nếu trễ | Contingency | Status |
|----|------------|------|-----------|----------|----------------|-------------|--------|
| DEP-001 | {{Phụ thuộc}} | Internal / Vendor / Client / Legal / Data | {{}} | {{}} | {{}} | {{}} | Open |

## 7. Escalation Rules

| Điều kiện | Hành động | Người nhận |
|-----------|-----------|------------|
| Critical issue chưa có owner sau 24h | Escalate ngay | PM + Sponsor |
| Dependency trễ ảnh hưởng milestone | Tạo Change/Risk update | PM + PO |
| Assumption High impact chưa validate trước Sprint 2 | Chuyển thành Risk | BA + PM |

## Review Checklist

```
☐ Mọi item Open đều có Owner
☐ Mọi Assumption High impact có ngày validate
☐ Mọi Dependency có contingency
☐ Issue Critical/High được review trong meeting gần nhất
☐ RAID đã đồng bộ với Risk Register và Meeting Minutes
```
