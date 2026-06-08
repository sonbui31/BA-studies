# Project Classification Gate

> **Purpose:** Prevent the BA agent from jumping directly into BRD/SRS/backlog before deciding what kind of initiative it is. This gate must run before recommending or drafting documents.

## 1. Mandatory Classification Questions

Ask or infer these first. If evidence is missing, state the assumption explicitly.

| Question | Why it matters |
|---|---|
| Is this a new product/platform/SaaS/app, an internal system, an outsource delivery, or a change to an existing system? | Selects the correct document stack and overlay. |
| Will this be commercialized or sold outside the first organization? | Makes Product Vision mandatory. |
| Is this an MVP/PoC only, or a product MVP that needs a longer product direction? | Distinguishes Lean Canvas-only work from Product Vision-led work. |
| Does the solution include AI/ML, scoring, recommendation, or generated content? | Adds AI Feature Spec, human review, model-risk, and data governance. |
| Are dashboards, HR data, permissions, audit, or sensitive personal data in scope? | Adds reporting, RBAC, audit log, privacy, and governance documents. |
| Is the domain regulated or industry-specific? | Routes to government, healthcare, fintech, or generic overlays. |

## 2. Classification Rules

| Signal | Classification | Required first documents |
|---|---|---|
| "Product", "platform", "SaaS", "app", "sell to external companies", "B2B", "subscription", "market" | Product | Product Vision Document, Product Strategy/Roadmap if needed, Project Charter, BRD |
| "Internal tool", "for one company", "department workflow", "in-house operation" | In-house | Project Charter, BRD, Scope In/Out, As-Is/To-Be |
| "Vendor", "client", "outsourcing", "contract", "milestone payment", "sign-off" | Outsource | Vision & Scope, Project Charter or SoW input, BRD, Stakeholder/RACI, Scope baseline |
| "PoC", "2-4 week MVP", "validate idea fast", "no long-term product plan yet" | Startup/MVP | Lean Canvas plus a short Vision Statement and MVP Scope |
| "AI generates", "AI scores", "recommendation", "chatbot interview", "model", "confidence" | AI/ML add-on | AI Feature Spec, Human Review Policy, Data Governance, Monitoring/Fallback rules |
| "Dashboard", "KPI", "export", "report" | Reporting add-on | Reporting Specification, Metric Dictionary |
| "Role", "permission", "HR data", "personal score", "audit" | Governance add-on | RBAC Matrix, Audit Log Requirement, Data Privacy/Security Requirement |

## 3. Non-Negotiable Vision Rule

If the initiative is a new product, platform, SaaS, app, B2B offering, or commercializable MVP, the agent must propose **Product Vision Document before Project Charter and BRD**.

Do not treat Project Charter or BRD as a replacement for Product Vision:

| Document | Answers |
|---|---|
| Product Vision | What should this product become, for whom, and why it is meaningfully different. |
| Project Charter | What project will be delivered, by whom, by when, and under which constraints. |
| BRD | What business needs and measurable requirements must be satisfied. |

## 4. Document Recommendation Matrix

When the user asks "what documents are needed", recommend documents by layer, not by habit.

| Layer | Typical documents |
|---|---|
| Product | Product Vision Document, Product Strategy/Roadmap, Product Analytics Spec |
| Business | Project Charter, BRD, Business Case, KPI/Success Metrics, Stakeholder Map/RACI, Scope In/Out |
| Process | As-Is Process, To-Be Process, Business Rules Catalog, BPMN/Swimlane |
| Requirements | SRS/FRD, Use Case Specification, User Story Map, Product Backlog, Acceptance Criteria |
| UX | Personas, User Journey, User Flow, Screen Inventory, Wireframe/Prototype |
| AI/Data | AI Feature Spec, Assessment Framework, Prompt/Output Spec, Data Dictionary, ERD, Data Governance |
| Technical | High-Level Architecture, API Specification, NFR, Deployment Plan, Environment Guide |
| QA/UAT | Test Strategy, Test Cases, RTM, UAT Plan, UAT Sign-off |
| Delivery | Operational Readiness, Release Notes, User/Admin Guide, Handover Checklist |

## 5. Output Format for the Gate

Before drafting a document plan, show a compact routing summary:

```text
Project classification: Product + In-house MVP + AI/ML add-on
Commercialization signal: Yes, planned B2B sale
Required first artifact: Product Vision Document
Selected overlay: product
Supporting add-ons: AI Feature Spec, RBAC, Reporting, Data Governance, Audit Log
Assumptions to validate: ...
```
