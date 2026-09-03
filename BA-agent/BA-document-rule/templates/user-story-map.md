# USER STORY MAP — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Phương pháp:** Jeff Patton's Story Mapping + MoSCoW + Kano

---

## 1. Story Map Overview

> Story Map = Backbone (Activities) → Walking Skeleton (MVP) → Releases

> [!IMPORTANT]
> **Quy tắc cho User Story & Acceptance Criteria:**
> - **User Story:** Bắt buộc viết dưới góc nhìn người dùng theo chuẩn INVEST: `Là [vai trò], tôi muốn [hành động], để [nhận giá trị]`. CẤM lồng câu lệnh code hoặc kiến trúc kỹ thuật vào story.
> - **Acceptance Criteria (AC):** Bắt buộc định dạng Given–When–Then, bao phủ đủ 4 luồng: Happy path, Negative path, Boundary case, Permission case.

```
            Activity 1        Activity 2        Activity 3
           ┌─────────┐      ┌─────────┐      ┌─────────┐
Backbone:  │ Task 1.1 │      │ Task 2.1 │      │ Task 3.1 │     ← Backbone
           │ Task 1.2 │      │ Task 2.2 │      │ Task 3.2 │
           └────┬─────┘      └────┬─────┘      └────┬─────┘
                │                  │                  │
═══════════════════════════════════════════════════════════════  ← MVP Line
                │                  │                  │
Release 1: │ Story A  │      │ Story D  │      │ Story G  │     Must Have
           │ Story B  │      │ Story E  │      │          │
───────────┼──────────┤      ├──────────┤      ├──────────┤
Release 2: │ Story C  │      │ Story F  │      │ Story H  │     Should Have
           │          │      │          │      │ Story I  │
───────────┼──────────┤      ├──────────┤      ├──────────┤
Future:    │ Story X  │      │ Story Y  │      │ Story Z  │     Could / Won't
```

---

## 2. Backbone — Activities & Tasks

| Activity | Mô tả | Tasks |
|----------|-------|-------|
| {{Activity 1}} | {{Mô tả}} | Task 1.1, Task 1.2 |
| {{Activity 2}} | {{Mô tả}} | Task 2.1, Task 2.2 |
| {{Activity 3}} | {{Mô tả}} | Task 3.1, Task 3.2 |

---

## 3. User Stories

### Format chuẩn

```
As a [vai trò],
I want [mục tiêu],
So that [lợi ích / giá trị kinh doanh].
```

> Mỗi story phải đạt **INVEST** — xem `core/principles.md` > Mục 5

---

### Epic 1: {{Tên Epic}}

#### US-{{MOD}}-001: {{Tên Story}}

| Thuộc tính | Chi tiết |
|-----------|---------|
| **ID** | US-{{MOD}}-001 |
| **Epic** | {{Tên Epic}} |
| **Story** | As a {{vai trò}}, I want {{mục tiêu}}, so that {{lợi ích}} |
| **MoSCoW** | Must / Should / Could |
| **Kano** | Basic / Performance / Excitement |
| **Story Points** | {{SP}} |
| **Release** | Release {{N}} |
| **Trace từ BRD** | BR-{{xxx}} |

**INVEST Check:**

| I | N | V | E | S | T |
|---|---|---|---|---|---|
| ☐ Independent | ☐ Negotiable | ☐ Valuable | ☐ Estimable | ☐ Small | ☐ Testable |

**Acceptance Criteria (Given-When-Then):**

```gherkin
Scenario 1: {{Tên scenario — Happy Path}}
  GIVEN  {{bối cảnh / điều kiện tiên quyết}}
  WHEN   {{hành động của user}}
  THEN   {{kết quả mong đợi}}
  AND    {{kết quả bổ sung}}

Scenario 2: {{Tên scenario — Unhappy Path}}
  GIVEN  {{bối cảnh}}
  WHEN   {{hành động gây lỗi}}
  THEN   {{hệ thống phản hồi lỗi}}
```

**UI Reference:** {{Link đến wireframe/mockup nếu có}}

**Notes / Dependencies:** {{Ghi chú thêm}}

---

#### US-{{MOD}}-002: {{Tên Story tiếp theo}}

_(Lặp lại format trên cho mỗi story)_

---

## 4. Release Planning

### Release 1 — MVP (Walking Skeleton)

| Story ID | Story | MoSCoW | Kano | SP | Sprint |
|----------|-------|--------|------|----|--------|
| US-{{MOD}}-001 | {{Tên}} | Must | Basic | {{SP}} | Sprint 1 |
| US-{{MOD}}-002 | {{Tên}} | Must | Basic | {{SP}} | Sprint 1 |
| US-{{MOD}}-003 | {{Tên}} | Must | Performance | {{SP}} | Sprint 2 |

**Total SP Release 1:** {{Total}}
**Estimated Sprints:** {{N}} sprints × {{velocity}} SP/sprint

### Release 2

| Story ID | Story | MoSCoW | Kano | SP | Sprint |
|----------|-------|--------|------|----|--------|
| US-{{MOD}}-004 | {{Tên}} | Should | Performance | {{SP}} | Sprint {{N}} |

### Future / Backlog

| Story ID | Story | MoSCoW | Kano | SP |
|----------|-------|--------|------|----|
| US-{{MOD}}-010 | {{Tên}} | Could | Excitement | {{SP}} |
| US-{{MOD}}-011 | {{Tên}} | Won't | — | — |

---

## 5. Thống kê

### MoSCoW Distribution

| Priority | Số stories | Total SP | % SP |
|----------|-----------|---------|------|
| Must | {{N}} | {{SP}} | {{%}} |
| Should | {{N}} | {{SP}} | {{%}} |
| Could | {{N}} | {{SP}} | {{%}} |
| Won't | {{N}} | — | — |

> ⚠️ Must SP nên chiếm ~60%. Nếu > 70% → review lại ưu tiên.

### Kano Distribution

| Category | Số stories | Ghi chú |
|----------|-----------|---------|
| Basic | {{N}} | Đảm bảo 100% — đây là table stakes |
| Performance | {{N}} | Tối ưu liên tục |
| Excitement | {{N}} | Đầu tư có chọn lọc → WOW factor |

---

## 6. Definition of Ready (DoR) — Per Story

> Story chỉ được đưa vào Sprint khi pass tất cả:

```
☐ Story viết đúng format (As a... I want... So that...)
☐ INVEST check pass (6/6)
☐ Acceptance Criteria viết Given-When-Then (≥ 2 scenarios)
☐ MoSCoW priority assigned
☐ Story Points estimated
☐ UI mockup attached (nếu có UI)
☐ Dependencies resolved
☐ PO/Stakeholder confirmed
```

---

## ✅ Review Checklist

```
☐ Backbone (Activities → Tasks) rõ ràng
☐ Walking Skeleton (MVP line) xác định
☐ Mọi story đạt INVEST
☐ Acceptance Criteria viết Given-When-Then
☐ MoSCoW + Kano cho mỗi story
☐ Must SP ≤ 60% tổng
☐ Release plan có velocity + sprint allocation
☐ Traceability: Story → BRD requirement
```
