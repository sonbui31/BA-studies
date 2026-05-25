# BA KNOWLEDGE BASE

> **Mục đích:** Lưu kiến thức BA đã chắt lọc từ kho học liệu `BA/` để BA-agent dùng độc lập khi tạo, review, hoặc audit tài liệu BA.
> **Cập nhật:** 25/05/2026
> **Phạm vi:** Self-contained knowledge base. Không cần folder `BA/` tồn tại lúc runtime.

---

## 1. Khi nào dùng knowledge base này

Dùng file này khi:
- Agent cần tham khảo kiến thức nền trước khi viết BRD/SRS/User Story/UAT/RTM.
- Agent cần chọn artifact, kỹ thuật elicitation, mô hình, hoặc checklist review phù hợp.
- Agent cần áp dụng kiến thức BA/Product/UX/Data/Technical/Domain đã tổng hợp từ kho `BA/`.
- User đã xoá folder `BA/` nhưng vẫn muốn `BA-agent` giữ năng lực suy luận BA từ kho đó.

Nếu cần truy xuất nhanh theo chủ đề, dùng `ba-knowledge-cards.json` qua `scripts/knowledge_search.py`.

Không dùng file này để:
- Trích nguyên văn sách/PDF dài.
- Yêu cầu mở lại file trong `BA/` nếu folder nguồn không còn tồn tại.
- Ghi đè rule/template trong `BA-agent` nếu chưa có yêu cầu cụ thể.

---

## 2. Provenance từ folder BA

Phần này chỉ ghi lại kiến thức đã được lấy từ vùng nào của folder `BA/`. Agent không được phụ thuộc vào các path này khi chạy.

| Nguồn gốc trong folder `BA/` | Kiến thức đã chắt lọc | Đã nhúng vào phần |
|---|---|---|
| Roadmap/training files | BA role, SDLC, BABOK/BACCM, requirement basics, elicitation, modeling, artifacts. | 6.1, 6.2, 6.3 |
| Portfolio/templates | BRD, SRS, User Story, UAT, RTM, Data Dictionary, RACI, Change Request. | 6.2, 6.6 |
| Slides/session materials | BA introduction, SDLC, Requirement, Elicitation, Diagram, Documents, Prototype, Scrum, User Story, Testing. | 6.1-6.7 |
| BA exercise/case studies | OTA, agency, restaurant, rental, omnichannel sales case patterns. | 6.2-6.6 |
| BA books/BRD/SRS/BPMN/UML docs | Requirements engineering, modeling, documentation standards. | 6.4, 6.5 |
| Day-to-day BA documents | Practical tools, diagrams, templates, use cases, UAT, requirements. | 6.2-6.6 |
| Agile/Scrum/Product Owner docs | Backlog, story refinement, DoR/DoD, sprint collaboration. | 6.6, 6.7 |
| Product management docs | Product strategy, roadmap, prioritization, launch, backlog refinement. | 6.7 |
| UI/UX docs and videos | Wireframe, user flow, prototype, screen inventory, UX validation. | 6.5, 6.7 |
| Technical BA docs | Web apps, APIs, microservices, architecture, database, mobile. | 6.8 |
| Data/BI/SQL/Excel docs | Reporting, KPI, dashboard, data dictionary, analytics. | 6.8 |
| Domain docs | Banking/finance, insurance, healthcare/government style domain routing. | 6.9 |
| BACCM case doc | Internal training/testing system with AI-generated lessons/quiz/exams. | 6.1, 6.8 |
| ML experiment doc | Predictive feature metrics, train/validation/test split, outlier and explainability concerns. | 6.8 |

---

## 3. Insight đã chắt lọc

| Nhóm insight | Nội dung agent phải nhớ |
|---|---|
| BA foundation | BA phải đi từ problem/value/stakeholder/context trước khi viết solution. BACCM là sanity check cho mọi artifact. |
| Portfolio/documentation | Một bundle BA tốt cần Vision/Scope, BRD, Process, SRS, Story Map, Data Model, UAT, RTM, Change Log, Meeting Minutes. |
| Traceability | BRD/SRS/User Story/UAT không được rời nhau; phải giữ chain requirement -> implementation planning -> acceptance. |
| Training/internal system | Với hệ thống đào tạo nội bộ có AI, phải capture source material, learning objective, quiz/exam generation, evaluation, role/permission, auditability. |
| AI/ML feature | BA cần mô tả input/output, metric, acceptable error, confidence, fallback, monitoring, và cách giải thích kết quả cho stakeholder. |

---

## 4. Quy tắc sử dụng knowledge base

1. **Self-contained first:** Không mở folder nguồn để hoàn thành tác vụ thông thường; dùng kiến thức đã nhúng trong file này.
2. **Ưu tiên artifact thực chiến:** Khi user yêu cầu tạo tài liệu, ưu tiên template trong `BA-agent`; dùng knowledge base này để chọn nội dung và checklist phù hợp.
3. **Traceability là bắt buộc:** Mọi portfolio hoặc project bundle phải giữ chain `BRQ-* -> FR-* -> Feature -> US-* -> TC-*` hoặc nêu rõ dùng legacy scheme.
4. **Không overfit vào một template:** Template `BA-agent` là chuẩn hiện hành; knowledge base chỉ bổ sung phán đoán BA.
5. **No source-folder dependency:** Nếu folder `BA/` đã bị xoá, agent vẫn phải hoạt động bình thường.
6. **Domain cần kiểm chứng:** Với luật, chứng chỉ, tiêu chuẩn, hoặc thông tin hiện hành, phải kiểm tra nguồn chính thức mới nhất trước khi khẳng định.

---

## 5. Route nhanh theo nhu cầu

| User cần | Agent dùng |
|---|---|
| Portfolio BA | Section 6.2, 6.4, 6.6 + templates trong `BA-agent/BA-document-rule/templates/` |
| BRD/SRS/RTM/UAT | `DOCUMENT-MAP.md`, `templates/brd.md`, `templates/srs.md`, `templates/uat-plan.md`, `core/traceability-validator.md` |
| User Story/AC | `templates/user-story-map.md`, `core/writing-guide.md`, `references/writing-examples.md` |
| BPMN/UML/DFD | `templates/bpmn-modeling-standard.md`, `core/diagram-guide.md`, `core/process-decomposition-guide.md` |
| Product/SaaS | Section 6.7 + `overlays/product/overlay-config.md`, `templates/product-analytics-spec.md` |
| Data/BI/Reporting | `templates/reporting-specification.md`, `templates/data-governance-plan.md`, `templates/data-model.md` |
| AI/ML feature | Section 6.8 + `templates/ai-feature-spec.md` |
| Internal training system | Section 6.1, 6.8 + `templates/ai-feature-spec.md`, `templates/operational-readiness-checklist.md` |

---

## 6. Knowledge distilled into BA-agent

Phần này là lớp kiến thức tổng hợp từ folder `BA/` để agent áp dụng trực tiếp khi tạo/review artifact. Đây là phần chính cần dùng khi folder nguồn không còn tồn tại.

### 6.1 BA role and operating model

BA-agent phải xử lý dự án theo tư duy:
- Bắt đầu từ business problem và expected value, không bắt đầu từ màn hình hoặc feature.
- Luôn phân biệt `business requirement`, `stakeholder requirement`, `solution requirement`, `transition requirement`, `functional requirement`, và `non-functional requirement`.
- Với dự án outsource, tài liệu là cơ sở hợp đồng/sign-off/change request.
- Với dự án product, tài liệu là cơ chế alignment liên tục giữa discovery, delivery, metric, và feedback.
- Với dự án nội bộ, cần cân bằng tốc độ, adoption, training, operational readiness, và governance.

### 6.2 Core BA artifact set

Khi user yêu cầu tạo bộ tài liệu BA, agent phải cân nhắc các artifact sau:

| Artifact | Kiến thức áp dụng |
|---|---|
| Vision & Scope | Clarify problem, objectives, stakeholders, scope boundary, success metrics. |
| BRD | Business goals, business requirements, assumptions, constraints, risks, approval. |
| SRS/FRS | Functional requirements, NFRs, business rules, UI behavior, data, integration, error handling. |
| Use Case Specification | Actors, preconditions, main flow, alternate flow, exception flow, postconditions. |
| User Story + AC | INVEST, role-goal-benefit, Given-When-Then, negative/boundary/permission scenarios. |
| Process Flow/BPMN | As-Is, To-Be, swimlanes, gateway rules, exception flow, handoff, SLA. |
| Context Diagram/DFD | System boundary, external actors/systems, data movement, integration touchpoints. |
| ERD/Data Dictionary | Entities, attributes, relationships, validation rules, ownership, source of truth. |
| RTM | Trace business need -> requirement -> feature -> story -> test case. |
| UAT Plan/Test Case | Entry/exit criteria, UAT scenarios, acceptance evidence, sign-off. |
| Change Request/Change Log | Baseline, impact analysis, approval, cost/schedule/scope effect. |
| Meeting Minutes/Communication Plan | Decisions, action items, open questions, owner, deadline, escalation. |

### 6.3 Elicitation knowledge

Agent phải ưu tiên chọn kỹ thuật elicitation theo bối cảnh:

| Tình huống | Kỹ thuật phù hợp |
|---|---|
| Stakeholder chưa rõ nhu cầu | Interview, 5W1H, probing, problem framing. |
| Nhiều bên liên quan cần đồng thuận | Workshop, facilitation, decision log, RACI. |
| Quy trình hiện tại phức tạp | Observation/shadowing, document analysis, As-Is process mapping. |
| Có hệ thống cũ | Interface analysis, data analysis, screen inventory, gap analysis. |
| User khó mô tả mong muốn | Prototype/wireframe, scenario walkthrough, usability feedback. |
| Cần xác định rule | Business rules analysis, decision table, state transition. |
| Cần ưu tiên phạm vi | MoSCoW, Kano, value-effort, risk-based prioritization. |

Mọi elicitation output nên chuyển thành:
- Pain points.
- Needs.
- Constraints.
- Assumptions.
- Business rules.
- Open questions.
- Candidate requirements.
- Validation evidence.

### 6.4 Requirement quality knowledge

Requirement tốt phải:
- Atomic: một câu chỉ mô tả một ý kiểm thử được.
- Unambiguous: không dùng từ mơ hồ như nhanh, dễ dùng, linh hoạt nếu thiếu metric.
- Testable: QC/UAT có thể viết test case.
- Traceable: có ID và nguồn gốc.
- Feasible: có thể triển khai trong ràng buộc kỹ thuật/thời gian/chi phí.
- Valuable: nối được với need/value/stakeholder.
- Complete enough: có precondition, trigger, expected outcome, exception nếu cần.

Smell cần bắt:
- Feature disguised as business need.
- Missing actor.
- Missing condition.
- Missing data rule.
- Missing NFR metric.
- Hidden integration.
- Undefined approval owner.
- Scope creep hidden inside "nice to have".

### 6.5 Modeling knowledge

Chọn sơ đồ theo câu hỏi cần trả lời:

| Câu hỏi | Sơ đồ nên dùng |
|---|---|
| Ai tương tác với hệ thống? | Use Case Diagram / Context Diagram |
| Quy trình nghiệp vụ chạy thế nào? | BPMN / Activity Diagram / Swimlane |
| Dữ liệu đi qua đâu? | DFD / Integration Context |
| Dữ liệu lưu thế nào? | ERD / Data Dictionary |
| Các object/hệ thống gọi nhau theo thứ tự nào? | Sequence Diagram |
| Trạng thái thay đổi ra sao? | State Diagram |
| Màn hình nào phục vụ feature nào? | Screen Inventory / User Flow |

Rule quan trọng:
- Không vẽ sơ đồ chỉ để minh họa; mỗi sơ đồ phải trả lời một câu hỏi BA cụ thể.
- Sơ đồ và text phải khớp ID, actor, rule, và exception.
- Với process, luôn tách As-Is, pain point/gap, và To-Be.

### 6.6 Testing and acceptance knowledge

BA-agent phải nối yêu cầu với acceptance ngay từ lúc viết:
- User Story phải có AC đủ happy path, negative path, boundary, permission, state, integration, data volume nếu phù hợp.
- UAT scenario phải nói rõ actor, business scenario, precondition, test data, expected result, evidence.
- RTM phải phát hiện orphan business requirement, orphan FR, story không có test, NFR không có test strategy.
- Với outsource, UAT sign-off liên quan milestone/payment nên wording phải formal.

### 6.7 Product, UX, and delivery knowledge

Với product/SaaS/app:
- Bắt đầu từ user persona, journey, pain point, metric, và product hypothesis.
- User flow phải gắn analytics tracking points khi có funnel/conversion.
- Roadmap/backlog nên ưu tiên theo value, risk, dependency, effort, và learning.
- Prototype/wireframe phải ghi behavior, validation, empty/error/loading state.
- Release/beta plan nên có rollout, feature flag, feedback loop, adoption metric.

### 6.8 Data, BI, and technical BA knowledge

Khi có data/reporting/API:
- Data Dictionary phải có field name, type, required, rule, source, owner, sensitivity.
- Reporting spec phải có metric definition, formula, data source, refresh, filter, export, reconciliation.
- API spec phải ghi endpoint, method, request/response, auth, validation, error code, idempotency nếu giao dịch.
- NFR phải có metric: performance, availability, security, auditability, scalability, compatibility.
- Với AI/ML feature, phải ghi rõ input features, target, metric, acceptable error, confidence/fallback, human review, model monitoring.

### 6.9 Domain knowledge routing

Khi phát hiện domain, agent phải load overlay/template phù hợp trước khi viết:
- Banking/Finance/Fintech: transaction state, reconciliation, AML/KYC, audit trail, security, privacy.
- Insurance: policy lifecycle, claim process, underwriting, premium, beneficiary, exclusions.
- Healthcare: clinical workflow, PHI/PII, consent, HL7/FHIR, clinical validation.
- Government/Public sector: procurement, regulatory compliance, multi-level acceptance, security classification.
- E-commerce/Product: catalog, cart, order, payment, inventory, refund/cancel, promotion, analytics.

Nếu thông tin domain có thể thay đổi theo luật/chuẩn hiện hành, agent phải kiểm tra nguồn chính thức trước khi khẳng định.
