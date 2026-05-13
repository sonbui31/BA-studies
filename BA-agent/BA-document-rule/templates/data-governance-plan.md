# DATA GOVERNANCE PLAN — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA/Data Owner}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Định nghĩa ownership, classification, quality, retention, access và lifecycle cho dữ liệu nghiệp vụ quan trọng.

## 2. Data Ownership

| Data Domain | Data Owner | Data Steward | Consumer chính | System of Record |
|-------------|------------|--------------|----------------|------------------|
| {{Customer / Asset / Order}} | {{}} | {{}} | {{}} | {{}} |

## 3. Data Classification

| Class | Mô tả | Ví dụ | Control bắt buộc |
|-------|------|-------|------------------|
| Public | Có thể công khai | {{}} | Basic integrity |
| Internal | Nội bộ | {{}} | Authenticated access |
| Confidential | Nhạy cảm | {{}} | RBAC + audit |
| Restricted | Rất nhạy cảm / pháp lý | {{}} | Encryption + approval + monitoring |

## 4. Critical Data Elements

| CDE ID | Field | Business Definition | Owner | Quality Rule | Downstream Impact |
|--------|-------|---------------------|-------|--------------|-------------------|
| CDE-001 | {{field}} | {{Định nghĩa}} | {{}} | {{Rule}} | {{Report/API/Process}} |

## 5. Data Quality Rules

| Rule ID | Data Element | Dimension | Rule | Threshold | Fail Action |
|---------|--------------|-----------|------|-----------|-------------|
| DQ-001 | {{field}} | Completeness | Không được null | 100% | Block save / Alert |
| DQ-002 | {{field}} | Accuracy | Phải khớp source of record | >= {{x}}% | Reconcile |

## 6. Retention and Archival

| Data Type | Retention Period | Archive Rule | Delete Rule | Legal Hold |
|-----------|------------------|--------------|-------------|------------|
| {{Data}} | {{Năm/tháng}} | {{}} | {{}} | Yes / No |

## 7. Access and Audit

| Data Class | Access Rule | Approval | Audit Event | Review Frequency |
|------------|-------------|----------|-------------|------------------|
| Confidential | Need-to-know + RBAC | Data Owner | View / Export / Update | Quarterly |

## Review Checklist

```
☐ Mọi data domain có owner
☐ Critical Data Elements có definition và quality rule
☐ Retention/delete/archive rõ ràng
☐ Access rule khớp RBAC Matrix
☐ Audit event được định nghĩa cho dữ liệu nhạy cảm
```
