# QUY TRÌNH BA — DỰ ÁN PRODUCT (SaaS / Platform / App)

> **Methodology:** Product Development Cycle (Lean + Agile)
> **Version:** 1.0 | **Ngày:** 06/03/2026
> **Đặc thù:** Data-driven, iteration liên tục, user research, metrics-focused

---

## 1. Tổng quan — Product khác gì In-house/Outsource?

| Yếu tố | In-house / Outsource | Product |
|---------|---------------------|---------|
| Người dùng | Biết trước, số lượng cố định | **Chưa biết rõ, cần research** |
| Yêu cầu | Stakeholder nội bộ / khách hàng đặt | **Tự phát hiện qua data + user research** |
| Thành công | Hoàn thành đúng scope, deadline | **Metrics: DAU, Retention, Revenue** |
| Tài liệu | BRD, SRS formal | **BRD nhẹ + User Stories chi tiết** |
| Testing | UAT formal → Sign-off | **A/B Test + Beta + Analytics** |
| Release | Big bang / milestone | **Continuous delivery, feature flags** |
| Lifecycle | Có điểm kết thúc | **Không kết thúc — continuous improvement** |

---

## 2. Product Development Cycle — 4 Giai đoạn (Lặp lại)

```
        ┌──────────┐
        │ DISCOVER │ ← User Research, Data Analysis, Competitive Analysis
        └────┬─────┘
             ↓
        ┌──────────┐
        │  DEFINE  │ ← BRD, User Stories, OKRs, Wireframe/Prototype
        └────┬─────┘
             ↓
        ┌──────────┐
        │  BUILD   │ ← Sprint, Feature Flags, CI/CD
        └────┬─────┘
             ↓
        ┌──────────┐
        │ MEASURE  │ ← A/B Test, Analytics, NPS, Retrospective
        └────┬─────┘
             ↓
        (Quay lại DISCOVER)
```

> ⚠️ **Không có "Closure" — Product liên tục cải tiến.**

---

### Phase 1: DISCOVER (Khám phá) — 1-2 tuần / iteration

**Mục tiêu:** Hiểu user, tìm cơ hội, xác nhận vấn đề đáng giải quyết.

| Hoạt động | Output | Người tham gia |
|-----------|--------|----------------|
| User Interview / Survey | Insights, Pain Points | BA/PM, UX Researcher |
| Phân tích dữ liệu (Analytics) | Behavior Report, Funnel Analysis | BA/PM, Data Analyst |
| Competitive Analysis | Competitive Landscape | BA/PM |
| Review feedback & support tickets | Prioritized Problem List | BA/PM, CS Team |

**Deliverables:**
- `01-Vision-Scope.md` (nếu sản phẩm mới)
- User Insights Report
- `03-User-Personas.md`

**Exit Criteria:** Có Problem Statement rõ ràng + thống nhất OKRs cho iteration.

---

### Phase 2: DEFINE (Định nghĩa) — 1-2 tuần / iteration

**Mục tiêu:** Chuyển insight thành giải pháp cụ thể, ưu tiên tính năng.

| Hoạt động | Output | Người tham gia |
|-----------|--------|----------------|
| Viết BRD | BRD (Business Requirements Document) | PM/BA |
| Design Sprint / Wireframe | Prototype có thể click | UX Designer, PM, BA |
| User Story Writing | User Stories + Acceptance Criteria | BA, Dev Lead |
| Prioritize (MoSCoW + Kano) | Prioritized Backlog | PM, BA, Stakeholders |

**Deliverables:**
- `02-BRD.md`
- `04-User-Flow.md`
- `06-User-Story-Map.md`
- Wireframe / Prototype (Figma)

**Exit Criteria:** BRD approved, prototype validated với ≥5 users.

---

### Phase 3: BUILD (Xây dựng) — N Sprints (1-2 tuần/Sprint)

**Mục tiêu:** Phát triển tính năng, ship nhanh, thu thập dữ liệu.

| Hoạt động | Output | Tần suất |
|-----------|--------|----------|
| Sprint Planning | Sprint Backlog | Đầu Sprint |
| Daily Standup | Standup Notes | Hàng ngày |
| BA giải đáp requirements | Clarification Notes | Khi cần |
| Sprint Review / Demo | Demo Recording, Feedback | Cuối Sprint |
| Retrospective | Action Items | Cuối Sprint |

**Deliverables:**
- User Stories + AC (cập nhật liên tục)
- `07-Data-Model.md`
- `09-Release-Notes.md`
- `10-Standup-Notes.md`

**BA tham gia:** Sprint Planning, Daily (khi cần), Sprint Review, Retro.

---

### Phase 4: MEASURE (Đo lường) — Liên tục sau release

**Mục tiêu:** Đo lường impact, quyết định iteration tiếp theo.

| Hoạt động | Output | Người tham gia |
|-----------|--------|----------------|
| Theo dõi OKR metrics | Metrics Dashboard | PM, Data Analyst |
| A/B Test analysis | Test Results | PM, BA, Dev |
| Beta user feedback | Feedback Report | BA, CS |
| NPS Survey | NPS Score + Comments | PM, CS |
| Feature adoption tracking | Adoption Rate Report | PM, Data |

**Deliverables:**
- `08-Beta-Testing-Plan.md`
- Metrics Report
- `09-Release-Notes.md` (cập nhật)

**Exit Criteria:** OKRs đạt target → maintain. Chưa đạt → quay lại DISCOVER.

---

## 3. Ma trận RACI — Hồ sơ BA cho Product

| Hồ sơ | BA/PM | UX | Dev Lead | Data | Stakeholder |
|--------|-------|-----|----------|------|-------------|
| Vision & Scope | **R** | C | I | I | **A** |
| BRD | **R** | **C** | C | C | A |
| User Personas | **R** | **R** | I | C | I |
| User Flow | C | **R** | C | I | I |
| User Story Map | **R** | C | **C** | I | I |
| Data Model | C | I | **R** | **C** | I |
| Beta Testing Plan | **R** | C | C | **C** | A |
| Release Notes | **R** | I | C | I | I |

> **R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed

---

## 4. Công cụ khuyến nghị

| Mục đích | Công cụ | Ghi chú |
|----------|---------|---------|
| Product Management | Jira / Linear / ProductBoard | BRD, Backlog, Sprint |
| User Research | Maze / UserTesting / Hotjar | Survey, Heatmap |
| Wireframe / Prototype | Figma / Sketch / Framer | Design + Prototype |
| Analytics | Mixpanel / Amplitude / GA4 | User Behavior |
| A/B Testing | Optimizely / Firebase A/B | Feature Experiments |
| Feature Flags | LaunchDarkly / Flagsmith | Gradual Rollout |

---

## 5. Checklist chuyển Phase

### Discover → Define
- [ ] Problem Statement được team thống nhất
- [ ] User Insights có dữ liệu hỗ trợ (≥5 interviews hoặc analytics data)
- [ ] OKRs xác định cho iteration này

### Define → Build
- [ ] BRD approved bởi Product Lead
- [ ] Prototype validated với ≥5 users
- [ ] User Stories written + estimated

### Build → Measure
- [ ] Feature shipped (100% hoặc behind feature flag)
- [ ] Analytics events tracked
- [ ] Release Notes published

### Measure → Discover (next iteration)
- [ ] OKR results reviewed
- [ ] Retrospective completed
- [ ] Next iteration priorities identified
