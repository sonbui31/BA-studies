# CHECKLIST CHẤT LƯỢNG TÀI LIỆU BA

> **Mục đích:** Đảm bảo mọi tài liệu BA đạt chuẩn trước khi sign-off
> **Áp dụng:** Review ở cuối mỗi phase và trước khi bàn giao

---

## 1. BACCM Check — Áp dụng cho MỌI tài liệu

> 6 khái niệm lõi phải được đề cập đầy đủ trong bộ tài liệu.

| # | Core Concept | Câu hỏi | Check |
|---|-------------|---------|-------|
| 1 | **Change** | Lý do thay đổi đã nêu rõ ràng? | ☐ |
| 2 | **Need** | Nhu cầu gốc (root need) đã xác định, không chỉ triệu chứng? | ☐ |
| 3 | **Solution** | Giải pháp phù hợp need, không over-engineer? | ☐ |
| 4 | **Stakeholder** | Map đủ người liên quan + quyền quyết định? | ☐ |
| 5 | **Value** | Giá trị kinh doanh đã lượng hóa (KPI/metric)? | ☐ |
| 6 | **Context** | Ràng buộc kỹ thuật / tổ chức / pháp lý ghi nhận đủ? | ☐ |

---

## 2. Definition of Ready (DoR) — Story đủ điều kiện vào Sprint

> Một User Story phải đạt **tất cả** tiêu chí dưới đây trước khi đưa vào Sprint Backlog.

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | Story viết đúng format: `As a [role], I want [goal], so that [benefit]` | ☐ |
| 2 | INVEST check pass (Independent, Negotiable, Valuable, Estimable, Small, Testable) | ☐ |
| 3 | Có **Acceptance Criteria** rõ ràng (Given-When-Then) | ☐ |
| 4 | Có **MoSCoW priority** | ☐ |
| 5 | Có **wireframe / mockup** đi kèm (nếu có UI) | ☐ |
| 6 | BA đã giải đáp hết câu hỏi từ Dev team | ☐ |
| 7 | Story đã được **PO/Stakeholder confirm** | ☐ |
| 8 | Kích thước phù hợp — hoàn thành trong **1 Sprint** | ☐ |
| 9 | **Dependencies** đã xác định và giải quyết | ☐ |
| 10 | **Data** cần thiết đã có hoặc đã plan | ☐ |

---

## 3. Definition of Done (DoD) — Story hoàn thành

> Một User Story coi là **Done** khi pass tất cả:

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | Code hoàn thành và **đã merge** vào branch chính | ☐ |
| 2 | **Unit test** pass (coverage >= ngưỡng team quy định) | ☐ |
| 3 | **Code review** pass bởi ít nhất 1 dev khác | ☐ |
| 4 | **Acceptance Criteria** pass (tất cả Given-When-Then scenario) | ☐ |
| 5 | QC đã **test** trên môi trường staging | ☐ |
| 6 | **No Critical / High bug** mở | ☐ |
| 7 | **UI/UX** khớp với wireframe/mockup (nếu có) | ☐ |
| 8 | **API documentation** cập nhật (nếu có API mới) | ☐ |
| 9 | **Demo** thành công cho PO/BA | ☐ |
| 10 | **Traceability** cập nhật: Story → Test Case → Result | ☐ |

---

## 4. Checklist Review theo từng loại tài liệu

### 📄 Vision & Scope

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | Business opportunity / problem statement rõ ràng | ☐ |
| 2 | Scope: IN scope và OUT of scope rõ ràng | ☐ |
| 3 | Success criteria có metric đo được | ☐ |
| 4 | Có Context Diagram | ☐ |
| 5 | Assumptions & Constraints liệt kê đầy đủ | ☐ |
| 6 | Impact Mapping: Goal → Actors → Impacts → Features | ☐ |

### 📄 BRD (Business Requirements Document)

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | Business need + justification rõ ràng (WHY) | ☐ |
| 2 | SWOT analysis (nếu applicable) | ☐ |
| 3 | Stakeholder list + vai trò | ☐ |
| 4 | High-level requirements có MoSCoW priority | ☐ |
| 5 | Feasibility assessment (kỹ thuật + kinh doanh) | ☐ |
| 6 | ROI hoặc cost-benefit analysis | ☐ |
| 7 | Risk & Mitigation plan | ☐ |

### 📄 SRS (Software Requirements Specification)

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | FR viết chuẩn SMART, có requirement ID | ☐ |
| 2 | NFR cover: Performance, Security, Availability, Scalability | ☐ |
| 3 | Business Rules document rõ ràng | ☐ |
| 4 | Use Case Diagram đi kèm | ☐ |
| 5 | Sequence Diagram cho luồng phức tạp | ☐ |
| 6 | State Diagram cho entity có nhiều trạng thái | ☐ |
| 7 | Error handling / Edge cases đã cover | ☐ |
| 8 | Assumptions & Dependencies | ☐ |
| 9 | Traceability: BRD → SRS mapping | ☐ |

### 📄 User Story Map

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | Backbone (Activities → Tasks) rõ ràng | ☐ |
| 2 | Walking Skeleton xác định (MVP line) | ☐ |
| 3 | Stories viết đạt INVEST | ☐ |
| 4 | Acceptance Criteria viết Given-When-Then | ☐ |
| 5 | MoSCoW priority cho mỗi story | ☐ |
| 6 | Kano classification (nếu applicable) | ☐ |
| 7 | Story đủ nhỏ cho 1 sprint | ☐ |
| 8 | Estimation (story points) đã ghi | ☐ |

### 📄 Data Model

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | ERD rõ ràng, có đủ entity chính | ☐ |
| 2 | Quan hệ giữa entity chính xác (1:1, 1:N, N:M) | ☐ |
| 3 | Data Dictionary đầy đủ (tên, kiểu, constraint) | ☐ |
| 4 | PK, FK rõ ràng | ☐ |
| 5 | Audit fields: created_at, updated_at, deleted_at | ☐ |
| 6 | Enum values (status, type...) liệt kê đầy đủ | ☐ |

### 📄 UAT Plan

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | Test scenarios cover tất cả FR | ☐ |
| 2 | Test case format: Precondition, Steps, Expected Result | ☐ |
| 3 | UAT entry/exit criteria rõ ràng | ☐ |
| 4 | Traceability: FR → Test Case | ☐ |
| 5 | Test data đã chuẩn bị | ☐ |
| 6 | Bug severity / priority classification | ☐ |
| 7 | Có sign-off template | ☐ |

---

## 5. Severity & Priority Matrix — Phân loại Bug

### Severity (Mức nghiêm trọng — kỹ thuật)

| Level | Tên | Mô tả | Ví dụ |
|-------|-----|-------|-------|
| S1 | **Critical** | Hệ thống sập / mất dữ liệu / security breach | Không đăng nhập được, XSS |
| S2 | **Major** | Chức năng chính không hoạt động, không có workaround | Không đặt hàng được |
| S3 | **Minor** | Chức năng phụ bị lỗi hoặc có workaround | Filter không đúng kết quả |
| S4 | **Trivial** | Cosmetic, typo, không ảnh hưởng nghiệp vụ | Lỗi chính tả trên UI |

### Priority (Mức ưu tiên — kinh doanh)

| Level | Tên | Ý nghĩa | SLA sửa |
|-------|-----|---------|---------|
| P1 | **Urgent** | Phải sửa NGAY | < 4 giờ |
| P2 | **High** | Sửa trong sprint hiện tại | < 2 ngày |
| P3 | **Medium** | Sửa trong sprint tiếp | < 1 sprint |
| P4 | **Low** | Lên lịch khi có bandwidth | Backlog |

> ⚠️ Severity ≠ Priority. Ví dụ: Typo trên trang chủ CEO demo = S4 + P1

---

## 6. Phase Gate Checklist — Điều kiện chuyển pha

| Chuyển Phase | Checklist | Owner |
|-------------|-----------|-------|
| **Inception → Discovery** | Vision & Scope approved, Stakeholder Map done, As-Is documented | BA + PM |
| **Discovery → Elaboration** | To-Be confirmed, Prototype validated, Story Map drafted (MoSCoW) | BA + PO |
| **Elaboration → Delivery** | SRS signed-off, Data Model reviewed, All stories meet DoR | BA + Dev Lead |
| **Delivery → Closure** | All features done (DoD), Change Log updated, UAT Plan ready | BA + PM |
| **Closure → Done** | UAT signed-off, Handover complete, Lessons Learned documented | BA + Sponsor |
