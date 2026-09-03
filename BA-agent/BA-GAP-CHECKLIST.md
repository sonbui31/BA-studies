# BA Agent Gap Checklist

> **Ngày rà soát:** 03/09/2026
> **Mục tiêu:** Theo dõi các khoảng trống tài liệu/kỹ năng BA đã phát hiện và trạng thái triển khai trong `BA-agent`.

---

## 1. Checklist tài liệu đã bổ sung

| Gap | Trạng thái | Tài liệu triển khai | Khi nào dùng |
|-----|:---------:|---------------------|----|
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
| Tách 4 Curated Templates độc lập | Done | `Curated templates/01-BRD`, `02-SRS`, `03-User-Story`, `04-AC` | Khi sinh BRD/SRS/Story/AC riêng biệt |

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
| `SKILL.md` | Done | Routing Table 4 template độc lập + Exclusive Curated rule + Audit Scripts section + Diagram standards |
| `DOCUMENT-MAP.md` | Done | Curated templates section liệt kê 7 file + Scripts section 14 file + Exclusive role description |
| `BA-document-rule/README.md` | Done | Cập nhật cây thư mục template và hướng đọc theo vai trò |
| `USER-GUIDE.md` | Done | Directory tree liệt kê 4 template mới + Exclusive Curated rule + Tùy chỉnh phân biệt cốt lõi vs phụ trợ |
| `workflows/ba-workflow.md` | Done | Step 3 trỏ tới 4 template mới + Step 5 Exclusive Curated Template Rule |
| `agents/ba-specialist.md` | Done | Rule 5 Exclusive Curated Templates + Rule 6 Audience Calibration |
| `Curated templates/README.md` | Done | Danh mục 6 file (4 template + Word + PDF) |

## 4. Phần nên mở rộng tiếp

| Gap còn lại | Ưu tiên | Gợi ý triển khai |
|-------------|:-------:|------------------|
| Tool execution thật với Jira/Confluence/Figma | High | Thêm connector workflow hoặc hướng dẫn thao tác theo từng tool |
| SIT/UAT automation scripts | Medium | Mở rộng `traceability_scan.py` để check test coverage từ `test-strategy.md` |
| Analytics event linting | Medium | Thêm script kiểm tra event naming và required properties |
| RBAC consistency scan | Medium | Thêm script check Role/Permission trong SRS/API/UAT |
| BPMN diagram linting | Low | Thêm checklist parser cho gateway/lane/exception trong Mermaid/BPMN text |

## 5. Scorecard audit tài liệu và logic

| Hạng mục | Chuẩn đạt | Trạng thái hiện tại |
|---|---|---|
| Pre-flight structure | Product/Outsource sample pass `preflight_check.py` | Pass |
| Requirement quality | BRD/SRS/Story Map sample pass `quality_rubric.py` với avg >= 3 và không item nào < 3 | Pass |
| Strict traceability | Sample có Feature layer và pass `traceability_scan.py --scheme legacy --strict` | Pass |
| Canonical traceability | Fixture canonical pass `--scheme canonical --strict` | Pass |
| Runtime cleanliness | Python cache không còn track trong Git, `.gitignore` chặn cache mới | Pass sau khi commit thay đổi |
| Documentation clarity | `DOCUMENT-MAP.md`, `SKILL.md`, `USER-GUIDE.md` nêu rõ legacy/canonical/strict | Pass |

## 6. Acceptance criteria để giữ mức 9/10

- `python -m unittest discover -s tests -v` pass.
- `python .\scripts\ba_bundle_audit.py` pass.
- `python .\scripts\preflight_check.py .\BA-Documents-Product` pass.
- `python .\scripts\preflight_check.py .\BA-Documents-Outsource` pass.
- `python .\scripts\quality_rubric.py .\BA-Documents-Product` pass.
- `python .\scripts\quality_rubric.py .\BA-Documents-Outsource` pass.
- `python .\scripts\traceability_scan.py .\BA-Documents-Product --scheme legacy --strict` pass.
- `python .\scripts\traceability_scan.py .\BA-Documents-Outsource --scheme legacy --strict` pass.
- `python .\scripts\traceability_scan.py .\tests\fixtures\canonical_bundle --scheme canonical --strict` pass.
