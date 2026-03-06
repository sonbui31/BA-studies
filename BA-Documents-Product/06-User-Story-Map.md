# USER STORY MAP
# {{Tên sản phẩm}}

> **Phiên bản:** 1.0 | **Ngày:** {{DD/MM/YYYY}}

---

## Cấu trúc: Epic → Feature → User Story + OKR Mapping

---

## EPIC 1: {{TÊN EPIC}} — OKR: {{O1: Objective liên quan}}

### Feature 1.1: {{Tên Feature}}

| ID | User Story | Acceptance Criteria | OKR | Sprint |
|----|-----------|---------------------|-----|--------|
| US-001 | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | - {{AC 1}}<br>- {{AC 2}}<br>- {{AC 3}} | KR1.1 | S1 |
| US-002 | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | - {{AC 1}}<br>- {{AC 2}} | KR1.1 | S1 |

### Feature 1.2: {{Tên Feature}}

| ID | User Story | Acceptance Criteria | OKR | Sprint |
|----|-----------|---------------------|-----|--------|
| US-003 | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | - {{AC 1}}<br>- {{AC 2}} | KR1.2 | S2 |

---

## EPIC 2: {{TÊN EPIC}} — OKR: {{O2: Objective liên quan}}

### Feature 2.1: {{Tên Feature}}

| ID | User Story | Acceptance Criteria | OKR | Sprint |
|----|-----------|---------------------|-----|--------|
| US-004 | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | - {{AC 1}}<br>- {{AC 2}} | KR2.1 | S3 |

---

## EPIC 3: {{TÊN EPIC}} — OKR: {{O3}}

### Feature 3.1: {{Tên Feature}}

| ID | User Story | Acceptance Criteria | OKR | Sprint |
|----|-----------|---------------------|-----|--------|
| US-005 | Là **{{persona}}**, tôi muốn **{{action}}** để **{{benefit}}** | - {{AC 1}} | KR3.1 | S4 |

---

## OKR Traceability Matrix

| OKR | User Stories | Feature | Epic |
|-----|-------------|---------|------|
| O1-KR1: {{Key Result}} | US-001, US-002 | Feature 1.1 | Epic 1 |
| O1-KR2: {{Key Result}} | US-003 | Feature 1.2 | Epic 1 |
| O2-KR1: {{Key Result}} | US-004 | Feature 2.1 | Epic 2 |
| O3-KR1: {{Key Result}} | US-005 | Feature 3.1 | Epic 3 |

---

## Acceptance Criteria Convention (Product)

```gherkin
# Template cho AC trong Product
Given {{precondition — trạng thái ban đầu}}
When {{action — user làm gì}}
Then {{outcome — kết quả mong đợi}}
  And {{side effect — analytics event fired, notification sent, etc.}}
```

**Ví dụ:**
```gherkin
Given user đã đăng nhập và đang ở Dashboard
When user nhấn "Create New Project"
  And nhập tên "My Project" 
  And nhấn "Create"
Then project mới xuất hiện trong danh sách
  And status = "Active"
  And event "project_created" fired với property {project_name}
  And redirect đến project detail page
```

> ⚠️ **Mọi AC trong Product phải có tracking event** (dòng `And event "xxx" fired`)

---

## Release Mapping

```
╔══════════════════════════════════════════════════════════╗
║ MVP — Sprint 1-4                                         ║
║                                                          ║
║  S1: {{Core feature A}} + {{Onboarding}}                ║
║  S2: {{Core feature B}}                                  ║
║  S3: {{Feature C}} + {{Integration X}}                  ║
║  S4: Polish + Beta Testing                               ║
╠══════════════════════════════════════════════════════════╣
║ Growth — Sprint 5-8                                      ║
║                                                          ║
║  S5: {{Feature D}} + {{Notification system}}            ║
║  S6: {{Feature E}} + {{A/B Test infrastructure}}        ║
║  S7: {{Feature F}} + {{Analytics dashboard}}            ║
║  S8: Optimization based on data                          ║
╠══════════════════════════════════════════════════════════╣
║ Monetization — Sprint 9-12                               ║
║                                                          ║
║  S9: {{Payment/Billing integration}}                     ║
║  S10: {{Premium features}}                               ║
║  S11: {{Enterprise features}}                            ║
║  S12: {{Referral system}}                                ║
╚══════════════════════════════════════════════════════════╝
```
