# OVERLAY: PRODUCT DEVELOPMENT

> **Áp dụng:** Dự án phát triển sản phẩm (SaaS, platform, mobile app)
> **Đặc điểm:** Data-driven, iteration liên tục, user research, metrics-focused

---

## 1. Tài liệu bắt buộc vs Tùy chọn

| # | Tài liệu | Bắt buộc? | Thay đổi so với Generic |
|---|----------|----------|------------------------|
| 1 | Vision & Scope | ✅ Bắt buộc | **Thêm: Product Vision Board, OKRs** |
| 2 | BRD | ✅ **Giữ BRD** | BRD nhẹ hơn in-house, thêm OKR + Metrics |
| 3 | Stakeholder Map | ⚠️ Khuyến nghị | Focus vào User Personas |
| 4 | Process Flow | ✅ Bắt buộc | User Flow thay vì Business Process |
| 5 | SRS | ☐ Tùy chọn | **Thay bằng User Stories chi tiết** |
| 6 | User Story Map | ✅ **Bắt buộc** | Core document — kèm OKR mapping |
| 7 | Data Model | ✅ Bắt buộc | Thêm Analytics data model |
| 8 | UAT Plan | → **A/B Test + Beta** | Thay UAT formal bằng beta testing |
| 9 | Change Log | ✅ Bắt buộc | → Release Notes |
| 10 | Meeting Minutes | ⚠️ Khuyến nghị | Standup notes |
| 11 | Handover Checklist | ❌ Không cần | Continuous — không có "bàn giao" |
| 12 | API Specification | ✅ Bắt buộc | Public API docs (developer portal) |

---

## 2. Tài liệu bổ sung cho Product

### BRD cho Product

> Giữ BRD nhưng bổ sung thêm phần Product-specific: OKR, Metrics, Rollout Plan.

```markdown
# BRD: {{Feature Name}}

## Problem Statement
{{User problem — viết từ góc nhìn user}}

## User Personas
| Persona | Đặc điểm | Nhu cầu | Pain point |
|---------|----------|---------|-----------|

## Success Metrics (OKRs)
| Objective | Key Result | Target | Baseline |
|-----------|-----------|--------|---------|

## Solution
{{Mô tả giải pháp}}

## User Flow
{{Diagram}}

## Scope (MoSCoW)
| Feature | MoSCoW | Kano | Sprint |

## Out of Scope
## Risks
## Open Questions
```

### Metrics & Analytics

| Metric Category | Metrics | Tool |
|----------------|---------|------|
| **Acquisition** | DAU, MAU, Sign-up rate | Analytics |
| **Activation** | Onboarding completion, Time-to-value | Mixpanel |
| **Retention** | D1/D7/D30 retention | Analytics |
| **Revenue** | MRR, ARPU, Churn rate | Billing |
| **Referral** | NPS, Viral coefficient | Survey |

---

## 3. Điều chỉnh quy trình

| Phase Generic | Product Equivalent | Thay đổi |
|-------------|-------------------|---------|
| Inception | **Product Discovery** | User research, competitive analysis |
| Discovery | **Design Sprint** | Prototype + User testing (1-2 tuần) |
| Elaboration | **Sprint Planning** | BRD + Stories, không cần SRS formal |
| Delivery | **Build + Ship** | CI/CD, feature flags, A/B testing |
| Closure | **Launch + Measure** | Không đóng, continuous improvement |

### Product Development Cycle

```
        ┌──────────┐
        │ DISCOVER │ ← User Research, Data Analysis
        └────┬─────┘
             ↓
        ┌──────────┐
        │  DEFINE  │ ← BRD, User Stories, OKRs
        └────┬─────┘
             ↓
        ┌──────────┐
        │  BUILD   │ ← Sprint, Feature Flags
        └────┬─────┘
             ↓
        ┌──────────┐
        │ MEASURE  │ ← A/B Test, Analytics, NPS
        └────┬─────┘
             ↓
        (Quay lại DISCOVER)
```
