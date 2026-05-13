# BA Agent Gap Checklist

> **Ngày rà soát:** 13/05/2026
> **Mục tiêu:** Theo dõi các khoảng trống tài liệu/kỹ năng BA đã phát hiện và trạng thái triển khai trong `BA-agent`.

---

## 1. Checklist tài liệu đã bổ sung

| Gap | Trạng thái | Tài liệu triển khai | Khi nào dùng |
|-----|:---------:|---------------------|--------------|
| Business Case / Feasibility | Done | `BA-document-rule/templates/business-case.md` | Cần Go/No-Go, ROI, buy/build, approval ngân sách |
| RAID Log | Done | `BA-document-rule/templates/raid-log.md` | Có risks, assumptions, issues, dependencies cần owner và escalation |
| RBAC / Permission Matrix | Done | `BA-document-rule/templates/rbac-matrix.md` | Hệ thống có vai trò, quyền, data scope, phê duyệt |
| Reporting / BI Specification | Done | `BA-document-rule/templates/reporting-specification.md` | Có dashboard, báo cáo, KPI, export, reconciliation |
| Operational Readiness | Done | `BA-document-rule/templates/operational-readiness-checklist.md` | Chuẩn bị go-live, support, monitoring, rollback |
| Test Strategy | Done | `BA-document-rule/templates/test-strategy.md` | Cần SIT, regression, NFR test, test data, defect triage |
| User Research Plan | Done | `BA-document-rule/templates/user-research-plan.md` | Cần discovery, interview, observation, usability test |
| Product Analytics Spec | Done | `BA-document-rule/templates/product-analytics-spec.md` | Cần funnel, event taxonomy, experiment metrics |
| BPMN Modeling Standard | Done | `BA-document-rule/templates/bpmn-modeling-standard.md` | Quy trình phức tạp, nhiều lane/gateway/exception |
| Data Governance Plan | Done | `BA-document-rule/templates/data-governance-plan.md` | Có data owner, CDE, quality rule, retention, access |

## 2. Checklist kỹ năng đã gắn vào agent

| Skill gap | Trạng thái | Nơi triển khai |
|-----------|:---------:|----------------|
| Business case analysis | Done | `agents/ba-specialist.md` Skill 16 + `SKILL.md` routing |
| RAID/RBAC governance | Done | `agents/ba-specialist.md` Skill 17 + Step 3 workflow routing |
| Reporting/analytics/data governance | Done | `agents/ba-specialist.md` Skill 18 + supporting templates |
| Research/product discovery | Done | `agents/ba-specialist.md` Skill 19 + `user-research-plan.md` |
| Test/BPMN/operational readiness | Done | `agents/ba-specialist.md` Skill 20 + Step 7.6 workflow gate |

## 3. Checklist điều phối đã cập nhật

| File | Trạng thái | Nội dung đã cập nhật |
|------|:---------:|----------------------|
| `SKILL.md` | Done | Thêm routing cho 10 template mới và rules chọn supporting artifact |
| `DOCUMENT-MAP.md` | Done | Cập nhật số lượng generic templates từ 18 lên 28 và mô tả template mới |
| `BA-document-rule/README.md` | Done | Cập nhật cây thư mục template và hướng đọc theo vai trò |
| `USER-GUIDE.md` | Done | Cập nhật số lượng template trong cấu trúc |
| `workflows/ba-workflow.md` | Done | Thêm routing ở Step 3, generation rule ở Step 5, readiness gate ở Step 7.6 |
| `agents/ba-specialist.md` | Done | Mở rộng Skills Suite từ 15 lên 20 skills |

## 4. Phần nên mở rộng tiếp

| Gap còn lại | Ưu tiên | Gợi ý triển khai |
|-------------|:-------:|------------------|
| Tool execution thật với Jira/Confluence/Figma | High | Thêm connector workflow hoặc hướng dẫn thao tác theo từng tool |
| SIT/UAT automation scripts | Medium | Mở rộng `traceability_scan.py` để check test coverage từ `test-strategy.md` |
| Analytics event linting | Medium | Thêm script kiểm tra event naming và required properties |
| RBAC consistency scan | Medium | Thêm script check Role/Permission trong SRS/API/UAT |
| BPMN diagram linting | Low | Thêm checklist parser cho gateway/lane/exception trong Mermaid/BPMN text |
