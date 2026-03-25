# QUY TRÌNH BA TỔNG QUÁT 2.0 — DATA & AI DRIVEN

> **Áp dụng:** Mọi loại dự án (Hybrid/Agile)
> **Đặc điểm:** AI-Augmented, Data-Informed, Visual-First
> **Tham chiếu:** BABOK® v3 + Modern Product Management

---

## 1. Tổng quan 5 Pha 2.0

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐    ┌───────────┐
│  INCEPTION   │───▶│  DISCOVERY   │───▶│ ELABORATION │───▶│   DELIVERY   │───▶│  CLOSURE  │
│  (AI Assist) │    │ (Data Driven)│    │ (Visual Dev)│    │  (Agile Ref) │    │ (Analytics)│
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘    └───────────┘
```

> ⚠️ Thời lượng, deliverables, và mức chi tiết tài liệu **tùy thuộc loại dự án**.
> Xem `overlays/` tương ứng để biết điều chỉnh cụ thể.

---

## 2. Chi tiết từng Phase

### Phase 1: INCEPTION — Khởi động

**Mục tiêu:** Hiểu bối cảnh, xác định phạm vi, nhận diện stakeholder.

**BACCM Focus:** `Change` (tại sao?), `Context` (bối cảnh), `Stakeholder` (ai liên quan?)

| Hoạt động | Output | BABOK Knowledge Area |
|-----------|--------|---------------------|
| Kickoff Meeting | Meeting Minutes | BA Planning & Monitoring |
| Khảo sát hiện trạng | As-Is Process Flow | Elicitation & Collaboration |
| Phỏng vấn stakeholder | Stakeholder Map | Elicitation & Collaboration |
| Xác định Vision & Scope | Vision & Scope Document | Strategy Analysis |

**Deliverables:**
- `vision-scope.md`
- `brd.md` (draft hoặc full — tùy overlay)
- `stakeholder-map.md`
- `process-flow.md` (phần As-Is)

**Exit Criteria (Quality Gate):**
- [ ] Sponsor ký duyệt Vision & Scope
- [ ] BACCM check: Change + Context + Stakeholder đã xác định rõ
- [ ] Stakeholder Map hoàn thành (có Power/Interest classification)

---

### Phase 2: DISCOVERY — Khám phá

**Mục tiêu:** Thu thập yêu cầu chi tiết, xây dựng prototype, validate với người dùng.

**BACCM Focus:** `Need` (nhu cầu thực), `Value` (giá trị mang lại)

| Hoạt động | Output | BABOK Knowledge Area |
|-----------|--------|---------------------|
| Workshop yêu cầu nghiệp vụ | User Story Map (draft) | Elicitation & Collaboration |
| Phân tích gap (As-Is → To-Be) | To-Be Process Flow | Requirements Analysis |
| Prototype (lo-fi / hi-fi) | Wireframe/Mockup | Requirements Analysis |
| Demo prototype | Feedback Log | Elicitation & Collaboration |

**Deliverables:**
- `process-flow.md` (bổ sung To-Be)
- `user-story-map.md` (draft — phân loại MoSCoW)
- Wireframe/Prototype (Figma / Draw.io)

**Exit Criteria (Quality Gate):**
- [ ] Stakeholder xác nhận To-Be process
- [ ] Prototype được end-user validate
- [ ] User Story Map draft có phân loại MoSCoW rõ ràng

---

### Phase 3: ELABORATION — Chi tiết hóa

**Mục tiêu:** Hoàn thiện đặc tả yêu cầu, mô hình dữ liệu, chuẩn bị cho phát triển.

**BACCM Focus:** `Solution` (giải pháp cụ thể), `Need` (chi tiết hóa)

| Hoạt động | Output | BABOK Knowledge Area |
|-----------|--------|---------------------|
| Viết SRS | SRS Document | Requirements Analysis |
| Thiết kế Data Model | ERD + Data Dictionary | Requirements Analysis |
| Finalize User Story Map | User Story Map (final) | Req. Lifecycle Management |
| Review & Sign-off | Signed SRS | Req. Lifecycle Management |

**Deliverables:**
- `srs.md`
- `user-story-map.md` (final — có Acceptance Criteria theo Given-When-Then)
- `data-model.md`
- `api-specification.md` (nếu có API)

**Exit Criteria (Quality Gate):**
- [ ] SRS được sign-off
- [ ] Data Model review bởi Dev Lead
- [ ] User Story Map finalize + prioritize (MoSCoW confirmed)
- [ ] Mọi story đạt **Definition of Ready (DoR)**

---

### Phase 4: DELIVERY — Phát triển (N Sprints)

**Mục tiêu:** Hỗ trợ Dev team, refine stories, kiểm soát thay đổi.

**BACCM Focus:** `Solution` (theo dõi), `Value` (đo lường)

| Hoạt động | Output | Tần suất |
|-----------|--------|----------|
| Sprint Planning — refine stories | Updated User Stories + AC | Đầu Sprint |
| Giải đáp yêu cầu cho Dev/QC | Clarification Notes | Hàng ngày |
| Sprint Review / Demo | Feedback / CR | Cuối Sprint |
| Change Request Management | Change Log | Khi có thay đổi |

**Deliverables:**
- User Stories + Acceptance Criteria (cập nhật liên tục)
- `change-log.md`
- `meeting-minutes.md`

**BA tham gia:** Sprint Planning, Daily (khi cần), Sprint Review, Retrospective.

**Exit Criteria (Quality Gate):**
- [ ] Mọi story đạt **Definition of Done (DoD)**
- [ ] Change Log cập nhật đầy đủ
- [ ] Demo đạt acceptance từ PO/Stakeholder

---

### Phase 5: CLOSURE — Kết thúc

**Mục tiêu:** UAT, bàn giao, rút kinh nghiệm.

**BACCM Focus:** `Value` (xác nhận giá trị), toàn bộ 6 yếu tố (tổng kết)

| Hoạt động | Output | BABOK Knowledge Area |
|-----------|--------|---------------------|
| Chuẩn bị UAT | UAT Plan + Test Scenarios | Solution Evaluation |
| Hỗ trợ UAT | Defect Log, UAT Report | Solution Evaluation |
| Đào tạo end-user | Training Materials | Solution Evaluation |
| Bàn giao & Lessons Learned | Handover Checklist, Lessons | BA Planning & Monitoring |

**Deliverables:**
- `uat-plan.md`
- UAT Sign-off Report
- `handover-checklist.md`
- Lessons Learned

**Exit Criteria (Quality Gate):**
- [ ] UAT Pass — Biên bản nghiệm thu được ký
- [ ] Tài liệu bàn giao hoàn chỉnh
- [ ] Lessons Learned được ghi nhận

---

## 3. Mapping: Phase → BABOK Knowledge Area

| BABOK Knowledge Area | Inception | Discovery | Elaboration | Delivery | Closure |
|---------------------|:---------:|:---------:|:-----------:|:--------:|:-------:|
| BA Planning & Monitoring | ● | ○ | ○ | ○ | ● |
| Elicitation & Collaboration | ● | ● | ○ | ○ | ○ |
| Requirements Life Cycle Mgmt | ○ | ○ | ● | ● | ○ |
| Strategy Analysis | ● | ● | ○ | ○ | ○ |
| Requirements Analysis & DD | ○ | ● | ● | ○ | ○ |
| Solution Evaluation | ○ | ○ | ○ | ○ | ● |

> ● = Trọng tâm, ○ = Có hoạt động

---

## 4. Checklist chuyển Phase

> ⚠️ Phải pass **tất cả** exit criteria mới được chuyển phase.
> Xem `core/quality-checklist.md` để biết chi tiết từng checklist item.

| Chuyển Phase | Điều kiện bắt buộc |
|-------------|-------------------|
| Inception → Discovery | Vision & Scope approved, Stakeholder Map done |
| Discovery → Elaboration | To-Be confirmed, Prototype validated, Story Map drafted |
| Elaboration → Delivery | SRS signed-off, Data Model reviewed, DoR met |
| Delivery → Closure | All features done, Change Log updated, UAT Plan ready |
| Closure → Done | UAT signed-off, Handover complete, Lessons documented |
