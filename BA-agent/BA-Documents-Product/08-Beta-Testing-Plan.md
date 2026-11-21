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

| ID | Feature | Test Scenario | Ref BRQ | Ref FR | Ref Story | Pass/Fail |
|----|---------|--------------|---------|--------|-----------|-----------|
| IT-001 | Public portal | Submit feedback happy path | BRQ-01 | FR-POR-001 | US-POR-001 | ☐ |
| IT-002 | Public portal | Upvote duplicate attempt blocked | BRQ-01 | FR-POR-002 | US-POR-002 | ☐ |
| IT-003 | Duplicate merge | Merge keeps votes and history | BRQ-02 | FR-TRI-002 | US-TRI-002 | ☐ |
| IT-004 | Status notification | Subscriber receives update on status change | BRQ-03 | FR-STS-001, FR-STS-002 | US-STS-001 | ☐ |
| IT-005 | Release notes | Published release note links delivered feedback | BRQ-04, BRQ-05 | FR-REL-001 | US-REL-001 | ☐ |

### 2.2.1. Dữ liệu kiểm thử và môi trường

| Hạng mục | Nội dung |
|---|---|
| Môi trường | Staging tách biệt production; email thông báo chỉ gửi tới hộp thư nội bộ |
| Tài khoản thử | 3 workspace: Free, Pro, workspace đã tắt portal; mỗi workspace có 1 PM, 1 CS, 2 End User |
| Dữ liệu thử | 60 feedback mẫu, trong đó 12 cặp trùng nội dung (để kiểm IT-003), 5 feedback có vote từ cùng một người (để kiểm IT-002) |
| Dữ liệu cá nhân | Chỉ dùng dữ liệu giả lập; không sao chép feedback thật của khách hàng vào staging |

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

| ID | Scenario | Ref BRQ | Ref FR | Ref Story | Result |
|---|---|---|---|---|---|
| TC-POR-001 | Portal user submit feedback successfully | BRQ-01 | FR-POR-001 | US-POR-001 | ☐ |
| TC-POR-002 | Portal user cannot upvote same feedback twice | BRQ-01, BR-001 | FR-POR-002 | US-POR-002 | ☐ |
| TC-TRI-001 | PM sees duplicate candidates with confidence score; no suggestion below threshold | BRQ-02 | FR-TRI-001 | US-TRI-001 | ☐ |
| TC-TRI-002 | PM merge duplicate feedback without losing vote/history | BRQ-02, BR-002 | FR-TRI-002 | US-TRI-002 | ☐ |
| TC-STS-001 | Subscriber gets notification when feedback status changes; event `feedback_status_changed` and audit log are recorded | BRQ-03, BR-005 | FR-STS-001, FR-STS-002 | US-STS-001 | ☐ |
| TC-STS-002 | Feedback in `New` or `Reviewed` status does not show a public status on the portal | BRQ-03, BR-003 | FR-STS-001 | US-STS-001 | ☐ |
| TC-REL-001 | Release note only publishes linked Released feedback and stays hidden before `publish_at` | BRQ-04, BRQ-05, BR-004 | FR-REL-001 | US-REL-001 | ☐ |
| TC-NFR-001 | NFR-PERF-001, NFR-PERF-002, NFR-AVL-001, NFR-SEC-001, NFR-SEC-002, NFR-AUD-001, NFR-EVT-001, NFR-DATA-001, NFR-COMP-001: Beta NFR coverage for performance, availability, security, audit, eventing, data, and unsubscribe | BRQ-01, BRQ-02, BRQ-03, BRQ-04, BRQ-05 | NFR-PERF-001, NFR-PERF-002, NFR-AVL-001, NFR-SEC-001, NFR-SEC-002, NFR-AUD-001, NFR-EVT-001, NFR-DATA-001, NFR-COMP-001 | — | ☐ |

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
