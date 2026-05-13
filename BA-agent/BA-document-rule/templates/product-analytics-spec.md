# PRODUCT ANALYTICS SPEC — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA/Product}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Định nghĩa metrics, funnel, events, properties và kiểm tra dữ liệu để đo adoption, conversion, retention và hiệu quả sản phẩm.

## 2. Metrics Framework

| Metric ID | Metric | Loại | Định nghĩa | Target | Owner |
|-----------|--------|------|------------|--------|-------|
| MET-001 | {{Activation Rate}} | AARRR / OKR / KPI | {{Công thức}} | {{}} | {{}} |

## 3. Funnel Definition

| Step | Event | Điều kiện pass | Drop-off cần theo dõi |
|------|-------|----------------|-----------------------|
| 1 | {{event_name}} | {{}} | {{}} |
| 2 | {{event_name}} | {{}} | {{}} |

## 4. Event Taxonomy

| Event Name | Trigger | Actor | Required Properties | Optional Properties | Trace Feature |
|------------|---------|-------|---------------------|---------------------|---------------|
| {{entity_action}} | {{Khi user/system làm gì}} | {{Role}} | `user_id`, `timestamp`, `source` | {{}} | FR-{{MOD}}-001 |

## 5. Property Dictionary

| Property | Type | Required | Definition | Allowed Values |
|----------|------|:--------:|------------|----------------|
| `user_id` | string | ✅ | ID người dùng | UUID |
| `source` | string | ✅ | Nguồn truy cập | web / mobile / api |

## 6. Experiment Tracking

| Experiment ID | Hypothesis | Variant | Primary Metric | Guardrail Metric | Decision Rule |
|---------------|------------|---------|----------------|------------------|---------------|
| EXP-001 | {{Nếu làm X thì Y tăng}} | A/B | {{}} | {{}} | Ship / Iterate / Stop |

## 7. Data Quality Checks

| Check ID | Rule | Frequency | Owner | Fail Action |
|----------|------|-----------|-------|-------------|
| DQ-001 | Event không được thiếu `user_id` | Daily | Data Owner | Alert + fix instrumentation |

## Review Checklist

```
☐ Metric có công thức và target
☐ Event name theo naming convention nhất quán
☐ Required properties đủ để phân tích funnel
☐ Experiment có primary và guardrail metric
☐ Data quality check có owner
```
