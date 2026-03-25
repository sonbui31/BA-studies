# BETA TESTING & A/B TEST PLAN
# {{Tên sản phẩm}}

> **Phiên bản:** 1.0 | **Ngày:** {{DD/MM/YYYY}}
> **Thay thế UAT formal** — Product dùng Beta Testing + A/B Test thay vì UAT truyền thống.

---

## 1. Testing Strategy Overview

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   Internal    │────▶│  Closed Beta  │────▶│   Open Beta   │────▶│      GA       │
│   Testing     │     │   (5% users)  │     │  (20% users)  │     │  (100% users) │
│   (Team only) │     │   1-2 tuần    │     │   1 tuần      │     │               │
└───────────────┘     └───────────────┘     └───────────────┘     └───────────────┘
```

---

## 2. Internal Testing

### 2.1 Entry Criteria
- [ ] Feature development completed
- [ ] Unit tests pass (≥ 80% coverage)
- [ ] E2E tests pass for happy path
- [ ] Code review approved

### 2.2 Test Plan

| ID | Feature | Test Scenario | Pass/Fail |
|----|---------|--------------|-----------|
| IT-01 | {{Feature A}} | {{Happy path test}} | ☐ |
| IT-02 | {{Feature A}} | {{Error case test}} | ☐ |
| IT-03 | {{Feature A}} | {{Edge case test}} | ☐ |
| IT-04 | {{Feature B}} | {{Happy path}} | ☐ |

### 2.3 Exit Criteria
- [ ] 100% happy path tests pass
- [ ] 0 Critical bugs
- [ ] Performance acceptble (P95 < 500ms)

---

## 3. Closed Beta

### 3.1 Criteria chọn Beta Users
| Criteria | Value |
|----------|-------|
| Số lượng | {{X}} users |
| Profile | {{Power users / Early adopters}} |
| Nguồn | {{Waitlist / invite / existing users}} |
| Incentive | {{Early access / discount / swag}} |

### 3.2 Feedback Collection

| Method | Tool | Timing |
|--------|------|--------|
| In-app Survey | Typeform / In-app modal | Sau 3 ngày dùng |
| User Interview | Video call 15-30p | Cuối beta period |
| Bug Report | In-app widget / Email | Liên tục |
| Analytics | Mixpanel / Amplitude | Liên tục |

### 3.3 Success Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Feature adoption rate | ≥ {{X}}% | |
| Task completion rate | ≥ {{X}}% | |
| NPS (beta users) | ≥ {{X}} | |
| Bug reports (Critical) | 0 | |
| Bug reports (Major) | ≤ {{X}} | |

### 3.4 Exit Criteria
- [ ] NPS ≥ {{X}} từ beta users
- [ ] 0 Critical bugs
- [ ] Feature adoption ≥ {{X}}%
- [ ] No major usability issues

---

## 4. Open Beta (Gradual Rollout)

### 4.1 Rollout Plan

| Day | % Users | Feature Flag | Monitor |
|-----|---------|-------------|---------|
| Day 1 | 5% | `feature_x_enabled: 5%` | Error rate, latency |
| Day 3 | 20% | `feature_x_enabled: 20%` | Metrics, feedback |
| Day 5 | 50% | `feature_x_enabled: 50%` | Business metrics |
| Day 7 | 100% | `feature_x_enabled: 100%` | All |

### 4.2 Rollback Criteria
- 🔴 Error rate tăng > {{X}}%
- 🔴 P95 latency > {{X}}ms
- 🔴 User complaints spike

---

## 5. A/B Testing Plan

### Test 1: {{Tên Test}}

| Mục | Chi tiết |
|-----|----------|
| **Hypothesis** | {{Nếu chúng ta thay đổi X thì Y sẽ tăng Z%}} |
| **Metric** | {{Primary metric: conversion/retention/engagement}} |
| **Variants** | A: {{Control — hiện tại}} / B: {{Treatment — thay đổi}} |
| **Traffic Split** | 50/50 |
| **Sample Size** | ≥ {{X}} users per variant |
| **Duration** | {{X}} tuần (đủ statistical significance) |
| **Significance Level** | p < 0.05 |

**Results:**

| Variant | Metric | Value | Significance |
|---------|--------|-------|-------------|
| A (Control) | {{metric}} | | |
| B (Treatment) | {{metric}} | | |
| **Winner** | | | |

### Test 2: {{Tên Test}}

| Mục | Chi tiết |
|-----|----------|
| **Hypothesis** | {{...}} |
| **Metric** | {{...}} |
| **Variants** | A: {{...}} / B: {{...}} |
| **Duration** | {{X}} tuần |

---

## 6. Bug Severity & SLA

| Severity | Mô tả | SLA Fix |
|----------|--------|---------| 
| 🔴 **Critical** | Data loss, security issue, app crash | Hotfix trong 4h |
| 🟠 **Major** | Feature broken, no workaround | Fix trong 24h |
| 🟡 **Minor** | Feature broken + có workaround | Sprint tiếp |
| 🟢 **Cosmetic** | UI glitch, typo | Backlog |

---

## 7. Post-Release Monitoring

| Metric | Tool | Alert Threshold |
|--------|------|----------------|
| Error Rate | Sentry / Datadog | > {{X}}% → Alert |
| P95 Latency | Datadog / CloudWatch | > {{X}}ms → Alert |
| DAU Change | Mixpanel | Drop > {{X}}% → Alert |
| Crash Rate (Mobile) | Firebase Crashlytics | > {{X}}% → Alert |
| NPS | In-app Survey | < {{X}} → Review |
