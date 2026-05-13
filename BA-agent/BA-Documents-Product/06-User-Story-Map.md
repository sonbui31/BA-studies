# USER STORY MAP
# SignalDesk

> **Phiên bản:** 1.0 | **Ngày:** 12/05/2026

---

## Cấu trúc: Epic -> Feature -> User Story + OKR Mapping

---

## EPIC 1: Feedback Capture — OKR: O1 Kích hoạt workflow feedback

### Feature 1.1: Public feedback portal

| ID | User Story | Acceptance Criteria | Ref BRD | Ref FR | OKR | Sprint |
|----|-----------|---------------------|---------|--------|-----|--------|
| US-001 | As a **Portal User**, I want **gửi feedback qua portal public** so that **tôi không phải email thủ công cho team sản phẩm** | **Happy:** Given portal đang public<br>When tôi nhập title, description, email và bấm Submit<br>Then feedback mới được tạo ở status `New`<br>And event `feedback_submitted` fired<br><br>**Negative:** Given title dưới 5 ký tự<br>When tôi submit<br>Then hệ thống báo validation error<br><br>**Boundary:** Given mô tả dài hơn 2.000 ký tự<br>When tôi submit<br>Then hệ thống chặn lưu | BR-001 | FR-101 | O1-KR1 | S1 |
| US-002 | As a **Portal User**, I want **upvote feedback có sẵn** so that **team sản phẩm biết request nào được nhiều người quan tâm** | **Happy:** Given feedback item đang public<br>When tôi nhấn Upvote<br>Then vote_count tăng 1<br>And event `feedback_upvoted` fired<br><br>**Permission:** Given tôi đã upvote trước đó<br>When tôi nhấn lại<br>Then hệ thống không tăng vote_count | BR-001 | FR-102 | O1-KR1 | S1 |

### Feature 1.2: Workspace onboarding

| ID | User Story | Acceptance Criteria | Ref BRD | Ref FR | OKR | Sprint |
|----|-----------|---------------------|---------|--------|-----|--------|
| US-003 | As a **Product Manager**, I want **thấy duplicate candidates khi review feedback** so that **tôi không phải triage thủ công từng item trùng** | **Happy:** Given inbox có feedback mới<br>When tôi mở feedback detail<br>Then hệ thống hiển thị candidate duplicates với confidence score<br><br>**Exception:** Given score dưới threshold<br>When tôi mở detail<br>Then hệ thống không gợi ý duplicate | BR-002 | FR-201 | O1-KR2 | S2 |

---

## EPIC 2: Triage & Response — OKR: O2 Giảm support friction

### Feature 2.1: Duplicate merge & public status

| ID | User Story | Acceptance Criteria | Ref BRD | Ref FR | OKR | Sprint |
|----|-----------|---------------------|---------|--------|-----|--------|
| US-004 | As a **Product Manager**, I want **merge feedback trùng** so that **vote count và history không bị phân mảnh** | **Happy:** Given tôi có quyền merge<br>When tôi merge 1 child vào 1 parent<br>Then vote, subscriber, history được chuyển sang parent<br>And child có trạng thái `Merged`<br><br>**Permission:** Given tôi không có quyền PM/Admin<br>When tôi cố merge<br>Then hệ thống từ chối | BR-002 | FR-202 | O2-KR3 | S3 |
| US-005 | As a **Customer Success Lead**, I want **subscriber nhận status update** so that **khách hàng không cần hỏi thủ công trạng thái request** | **Happy:** Given feedback có subscriber<br>When PM đổi status sang `Planned` hoặc `Released`<br>Then subscriber nhận email update<br>And event `feedback_status_changed` fired<br><br>**Exception:** Given subscriber đã unsubscribe<br>When status đổi<br>Then hệ thống không gửi email | BR-003 | FR-301, FR-302 | O2-KR3 | S3 |

---

## EPIC 3: Value Proof — OKR: O3 Tăng willingness to pay

### Feature 3.1: Release notes linked to shipped work

| ID | User Story | Acceptance Criteria | Ref BRD | Ref FR | OKR | Sprint |
|----|-----------|---------------------|---------|--------|-----|--------|
| US-006 | As a **Product Manager**, I want **publish release note gắn với feedback đã ship** so that **khách hàng thấy feedback của họ dẫn tới outcome thực tế** | **Happy:** Given feedback đang ở trạng thái `Released`<br>When tôi publish release note<br>Then release note public hiển thị linked feedback<br>And event `release_note_published` fired<br><br>**Negative:** Given feedback chưa Released<br>When tôi cố link vào release note public<br>Then hệ thống chặn publish | BR-004, BR-005 | FR-303 | O3-KR4 | S4 |

---

## OKR Traceability Matrix

| OKR | User Stories | Feature | Epic |
|-----|-------------|---------|------|
| O1-KR1 | US-001, US-002 | Public feedback portal | Feedback Capture |
| O1-KR2 | US-003 | Duplicate candidates | Feedback Capture |
| O2-KR3 | US-004, US-005 | Merge + status notification | Triage & Response |
| O3-KR4 | US-006 | Release notes linked to feedback | Value Proof |

---

## Acceptance Criteria Convention (Product)

```gherkin
Given precondition
When user action
Then visible outcome
And analytics or notification side-effect
```

> ⚠️ Mọi AC P0/P1 trong Product phải có tracking event hoặc side effect đo được.

---

## Traceability Matrix

| Ref BRD | Ref FR | Story | Sprint | Test Ref |
|---|---|---|---|---|
| BR-001 | FR-101, FR-102 | US-001, US-002 | S1 | IT-001, IT-002, UAT-001, UAT-002 |
| BR-002 | FR-201, FR-202 | US-003, US-004 | S2-S3 | IT-003, UAT-003 |
| BR-003 | FR-301, FR-302 | US-005 | S3 | IT-004, UAT-004 |
| BR-004, BR-005 | FR-303 | US-006 | S4 | IT-005, UAT-005, UAT-NFR-001 |

---

## Release Mapping

```
MVP - Sprint 1-4
  S1: Public portal + submit/upvote
  S2: Duplicate suggestion
  S3: Merge + status notifications
  S4: Release notes + beta validation

Growth - Sprint 5-8
  S5: Saved filters
  S6: Advanced analytics
  S7: Workflow automation
  S8: Monetization refinements
```
