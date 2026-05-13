# REPORTING SPECIFICATION — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Định nghĩa báo cáo, dashboard, KPI, nguồn dữ liệu, filter, quyền truy cập và tiêu chí nghiệm thu cho reporting/BI.

## 2. Report Catalog

| Report ID | Tên báo cáo | Người dùng | Mục đích quyết định | Tần suất | Output |
|-----------|-------------|------------|---------------------|----------|--------|
| RPT-001 | {{Tên báo cáo}} | {{Role}} | {{Quyết định cần hỗ trợ}} | Daily / Weekly / Monthly / Ad-hoc | Screen / Excel / PDF / API |

## 3. KPI Definition

| KPI ID | KPI | Định nghĩa nghiệp vụ | Công thức | Đơn vị | Owner | Target |
|--------|-----|----------------------|-----------|--------|-------|--------|
| KPI-001 | {{Tên KPI}} | {{Ý nghĩa}} | {{Công thức}} | {{% / VND / count}} | {{}} | {{}} |

## 4. Data Source Mapping

| Field | Business Definition | Source System | Source Table/API | Transformation | Refresh |
|-------|---------------------|---------------|------------------|----------------|---------|
| {{field}} | {{Định nghĩa}} | {{System}} | {{Table/API}} | {{Rule}} | Realtime / Batch |

## 5. Filter and Drilldown

| Filter | Kiểu | Default | Bắt buộc | Quy tắc |
|--------|------|---------|----------|---------|
| Date Range | Date | Current month | ✅ | Không vượt quá {{N}} tháng |
| Department | Dropdown | All allowed | ☐ | Theo RBAC data scope |

## 6. Visualization Requirements

| Widget ID | Loại biểu đồ | Data | Interaction | Empty State |
|-----------|--------------|------|-------------|-------------|
| W-001 | Table / Bar / Line / KPI Card | {{}} | Sort / Drill / Export | {{Thông điệp}} |

## 7. Non-Functional Requirements

| NFR ID | Loại | Requirement | Acceptance Criteria |
|--------|------|-------------|---------------------|
| NFR-RPT-001 | Performance | Báo cáo phải tải trong {{N}} giây với {{X}} dòng | p95 <= {{N}} giây |
| NFR-RPT-002 | Security | Dữ liệu hiển thị theo RBAC data scope | User ngoài scope không xem được |

## 8. Reconciliation and Data Quality

| Check ID | Rule | Frequency | Owner | Fail Action |
|----------|------|-----------|-------|-------------|
| DQ-001 | Tổng dashboard khớp tổng giao dịch nguồn | Daily | Data Owner | Alert + block publish nếu lệch > {{x}}% |

## Review Checklist

```
☐ Mọi KPI có công thức và owner
☐ Mọi field có source mapping
☐ Filter/default/empty state rõ ràng
☐ Có NFR performance cho báo cáo lớn
☐ Có kiểm tra data quality/reconciliation
```
