# BETA TESTING & A/B TEST PLAN
# SignalDesk

> **Phiên bản:** 1.0 | **Ngày:** 12/05/2026
> **Thay thế UAT formal** — Product dùng Beta Testing + A/B Test thay vì UAT truyền thống.

---

## 1. Testing Strategy Overview

```
Internal testing -> Closed beta (5% workspace) -> Open beta (20% workspace) -> GA
```

---

## 2. Internal Testing

### 2.1. Entry Criteria
- [ ] Feature development completed
- [ ] Unit tests pass (>= 80% coverage)
- [ ] E2E tests pass for happy path
- [ ] Code review approved

### 2.2. Test Plan

| ID | Feature | Test Scenario | Ref BRD | Ref FR | Ref Story | Pass/Fail |
|----|---------|--------------|---------|--------|-----------|-----------|
| IT-001 | Public portal | Submit feedback happy path | BR-001 | FR-101 | US-001 | ☐ |
| IT-002 | Public portal | Upvote duplicate attempt blocked | BR-001 | FR-102 | US-002 | ☐ |
| IT-003 | Duplicate merge | Merge keeps votes and history | BR-002 | FR-202 | US-004 | ☐ |
| IT-004 | Status notification | Subscriber receives update on status change | BR-003 | FR-301, FR-302 | US-005 | ☐ |
| IT-005 | Release notes | Published release note links delivered feedback | BR-004, BR-005 | FR-303 | US-006 | ☐ |

### 2.3. Exit Criteria
- [ ] 100% happy path tests pass
- [ ] 0 Critical bugs
- [ ] Performance acceptable (P95 < 500ms)

---

## 3. Closed Beta

### 3.1. Criteria chọn Beta Users

| Criteria | Value |
|----------|-------|
| Số lượng | 25 workspace |
| Profile | PM-led SaaS teams, early adopters |
| Nguồn | Waitlist + existing users |
| Incentive | 2 tháng Pro miễn phí |

### 3.2. Feedback Collection

| Method | Tool | Timing |
|--------|------|--------|
| In-app Survey | Typeform / modal | Sau 5 ngày dùng |
| User Interview | Video call 20 phút | Tuần 2 |
| Bug Report | In-app widget | Liên tục |
| Analytics | Mixpanel | Liên tục |

### 3.3. Success Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Portal publish rate | >= 55% | |
| Feedback submit completion | >= 60% | |
| NPS (beta users) | >= 35 | |
| Critical bugs | 0 | |
| Major bugs | <= 5 | |

### 3.4. Exit Criteria
- [ ] NPS >= 35 từ beta users
- [ ] 0 Critical bugs
- [ ] Portal publish rate >= 55%
- [ ] No major usability issues

---

## 4. Product Acceptance / Beta Scenarios

| ID | Scenario | Ref BRD | Ref FR | Ref Story | Result |
|---|---|---|---|---|---|
| UAT-001 | Portal user submit feedback successfully | BR-001 | FR-101 | US-001 | ☐ |
| UAT-002 | Portal user cannot upvote same feedback twice | BR-001 | FR-102 | US-002 | ☐ |
| UAT-003 | PM merge duplicate feedback without losing vote/history | BR-002 | FR-201, FR-202 | US-003, US-004 | ☐ |
| UAT-004 | Subscriber gets notification when feedback status changes | BR-003 | FR-301, FR-302 | US-005 | ☐ |
| UAT-005 | Release note only publishes linked Released feedback | BR-004, BR-005 | FR-303 | US-006 | ☐ |
| UAT-NFR-001 | Core analytics events fire for submit, upvote, merge, publish | BR-005 | NFR-007 | US-001 to US-006 | ☐ |

---

## 5. Open Beta (Gradual Rollout)

### 5.1. Rollout Plan

| Day | % Users | Feature Flag | Monitor |
|-----|---------|-------------|---------|
| Day 1 | 5% | `portal_beta: 5%` | Error rate, spam rate |
| Day 3 | 20% | `portal_beta: 20%` | Activation metrics |
| Day 5 | 50% | `portal_beta: 50%` | Notification delivery, retention |
| Day 7 | 100% | `portal_beta: 100%` | Business metrics |

### 5.2. Rollback Criteria
- Error rate tăng > 2%
- Duplicate merge mismatch > 1%
- Notification failure > 5%

---

## 6. A/B Testing Plan

### Test 1: Portal CTA wording

| Mục | Chi tiết |
|-----|----------|
| **Hypothesis** | Nếu CTA rõ hơn về value, tỷ lệ submit feedback sẽ tăng ít nhất 8% |
| **Metric** | Feedback submit completion rate |
| **Variants** | A: "Submit feedback" / B: "Share your idea and track progress" |
| **Traffic Split** | 50/50 |
| **Sample Size** | >= 1.000 portal visits per variant |
| **Duration** | 2 tuần |
| **Significance Level** | p < 0.05 |

---

## 7. Bug Severity & SLA

| Severity | Mô tả | SLA Fix |
|----------|--------|---------|
| Critical | Data loss, security issue, merge corruption | Hotfix trong 4h |
| Major | Feature broken, no workaround | Fix trong 24h |
| Minor | Có workaround | Sprint tiếp |
| Cosmetic | UI glitch, typo | Backlog |

---

## 8. Post-Release Monitoring

| Metric | Tool | Alert Threshold |
|--------|------|----------------|
| Error Rate | Sentry / Datadog | > 2% |
| P95 Latency | Datadog | > 500ms |
| Portal publish rate | Mixpanel | < 45% |
| Notification delivery success | Email provider + Mixpanel | < 95% |
| NPS | In-app Survey | < 20 |
