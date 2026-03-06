# HƯỚNG DẪN VIẾT TÀI LIỆU BA

> **Mục đích:** Chuẩn hóa cách viết để mọi tài liệu BA nhất quán, chuyên nghiệp
> **Áp dụng:** Mọi document trong bộ BA-document-rule

---

## 1. Cấu trúc file chuẩn

Mọi tài liệu BA phải có:

```markdown
# [TÊN TÀI LIỆU] — [TÊN DỰ ÁN]

> **Phiên bản:** [x.y] | **Ngày:** [DD/MM/YYYY]
> **Tác giả:** [Tên BA] | **Trạng thái:** [Draft / In Review / Approved / Baseline]
> **Dự án:** [Tên dự án]

---

## Lịch sử thay đổi

| Phiên bản | Ngày | Người chỉnh | Mô tả thay đổi |
|-----------|------|-------------|----------------|
| 1.0       | ...  | ...         | Phiên bản đầu  |

---

## Phê duyệt

| Vai trò | Tên | Ngày ký | Chữ ký |
|---------|-----|---------|--------|
| BA      | ... | ...     | ...    |
| PM      | ... | ...     | ...    |
| Sponsor | ... | ...     | ...    |

---

[NỘI DUNG CHÍNH]

---

## Phụ lục (nếu có)
## Tài liệu tham chiếu
```

---

## 2. Quy tắc đặt tên file

### Format: `[STT]-[Tên-tài-liệu].md`

| Tài liệu | Tên file | Ví dụ |
|-----------|----------|-------|
| Process Framework | `00-BA-Process-Framework.md` | |
| Vision & Scope | `01-Vision-Scope.md` | |
| BRD | `02-BRD.md` | |
| Stakeholder Map | `03-Stakeholder-Map.md` | |
| Process Flow | `04-Process-Flow.md` | |
| SRS | `05-SRS.md` | |
| User Story Map | `06-User-Story-Map.md` | |
| Data Model | `07-Data-Model.md` | |
| UAT Plan | `08-UAT-Plan.md` | |
| Change Log | `09-Change-Log.md` | |
| Meeting Minutes | `10-Meeting-Minutes.md` | |
| Handover Checklist | `11-Handover-Checklist.md` | |
| API Specification | `12-API-Specification.md` | |

### Quy tắc khác
- **Tên bằng tiếng Anh** — dễ đồng bộ, tránh lỗi encoding
- **Dùng PascalCase với dấu gạch ngang** — `Vision-Scope.md`, không phải `vision scope.md`
- **Đánh số để giữ thứ tự** — 00, 01, 02... theo trình tự quy trình BA

---

## 3. Versioning — Quản lý phiên bản

| Trạng thái | Version | Ý nghĩa |
|-----------|---------|---------|
| **Draft** | 0.x | Đang viết, chưa review |
| **In Review** | 0.x | Đã gửi review, chờ feedback |
| **Approved** | 1.0 | Đã được phê duyệt lần đầu |
| **Baseline** | 1.0 ✓ | Đã ký, là cơ sở cho CR tracking |
| **Updated** | 1.x | Cập nhật nhỏ (không thay đổi scope) |
| **Major Update** | 2.0 | Thay đổi lớn (cần re-approve) |

**Quy tắc:**
- `0.1 → 0.2 → 0.3` = draft iterations
- `0.x → 1.0` = approved / signed-off
- `1.0 → 1.1` = minor update (typo, clarification)
- `1.x → 2.0` = major change (scope change, CR impact)

---

## 4. Ngôn ngữ & Giọng văn

### Ngôn ngữ theo đối tượng đọc

| Đối tượng | Ngôn ngữ | Ví dụ |
|-----------|---------|-------|
| **Sponsor / C-level** | Kinh doanh, không kỹ thuật | "Giảm 50% thời gian xử lý" |
| **Product Owner** | Nghiệp vụ + user-centric | "Khách hàng có thể đặt hàng trong 3 bước" |
| **Dev / Tech Lead** | Kỹ thuật, cụ thể | "API POST /orders trả về 201 + order_id" |
| **QC / Tester** | Scenario-based | "GIVEN ... WHEN ... THEN ..." |

### Quy tắc viết

| ✅ Nên | ❌ Tránh |
|--------|---------|
| "Hệ thống **phải** hiển thị..." (SHALL) | "Hệ thống nên hiển thị..." (mơ hồ) |
| "Thời gian phản hồi **< 3 giây**" | "Hệ thống phải nhanh" |
| "**Khi** user nhấn Submit" | "User sẽ nhấn Submit" |
| Câu ngắn, 1 ý / 1 câu | Câu dài lê thê, 3 mệnh đề |
| Active voice: "Hệ thống gửi email" | Passive: "Email được gửi bởi hệ thống" |

### Từ khóa yêu cầu (RFC 2119)

| Từ khóa | Ý nghĩa | Dùng khi |
|---------|---------|---------|
| **PHẢI** / **SHALL** | Bắt buộc, không thương lượng | Functional requirement cốt lõi |
| **NÊN** / **SHOULD** | Khuyến nghị mạnh | Requirement quan trọng nhưng có workaround |
| **CÓ THỂ** / **MAY** | Tùy chọn | Nice-to-have feature |
| **KHÔNG ĐƯỢC** / **SHALL NOT** | Cấm | Security, compliance requirement |

---

## 5. Viết Requirement — Checklist SMART

Mỗi requirement phải đạt:

| Tiêu chí | Câu hỏi kiểm tra | ❌ Ví dụ sai | ✅ Ví dụ đúng |
|----------|-------------------|-------------|-------------|
| **S**pecific | Cụ thể, rõ ràng? | "Quản lý đơn hàng" | "Hiển thị danh sách đơn hàng với filter theo status" |
| **M**easurable | Đo lường được? | "Load nhanh" | "Thời gian load < 3 giây cho 95% request" |
| **A**chievable | Khả thi? | "AI dự đoán chính xác 100%" | "AI suggest với accuracy >= 80%" |
| **R**elevant | Liên quan đến goal? | "Đổi logo mỗi ngày" | "Dashboard hiển thị KPI doanh thu" |
| **T**ime-bound | Có deadline? | "Cần xong sớm" | "Triển khai trước 01/07/2026" |

---

## 6. Requirement ID — Hệ thống đánh mã

### Format: `[Prefix]-[Module]-[Number]`

| Prefix | Loại | Ví dụ |
|--------|------|-------|
| `FR` | Functional Requirement | `FR-ORD-001` |
| `NFR` | Non-Functional Requirement | `NFR-PERF-001` |
| `BR` | Business Rule | `BR-PRICE-001` |
| `US` | User Story | `US-ORD-001` |
| `UC` | Use Case | `UC-ORD-001` |

### Traceability Chain

```
BRD (BR-001) → SRS (FR-ORD-001) → User Story (US-ORD-001) → Test Case (TC-ORD-001)
```

> Mỗi requirement PHẢI trace được ngược về business need và xuôi đến test case.

---

## 7. Sử dụng Diagram

### Quy tắc chung

1. **Luôn kèm diagram** — văn bản mô tả + diagram minh họa
2. **1 diagram = 1 mục đích** — không gộp Use Case + Activity vào 1 sơ đồ
3. **Dùng Mermaid** trong markdown — dễ version control, dễ edit
4. **Đánh label rõ ràng** — mũi tên phải có nhãn, node phải có tên
5. **Giới hạn kích thước** — tối đa 7-10 node chính / diagram

### Khi nào dùng diagram nào

| Cần trả lời | Loại diagram | Tài liệu |
|-------------|-------------|----------|
| Ai tương tác với hệ thống? | Context Diagram | Vision & Scope |
| User làm gì? | Use Case Diagram | BRD, SRS |
| Quy trình chạy thế nào? | Activity/Swimlane | Process Flow |
| Hệ thống gọi nhau thế nào? | Sequence Diagram | SRS |
| Trạng thái chuyển thế nào? | State Diagram | SRS, Data Model |
| Dữ liệu quan hệ thế nào? | ERD | Data Model |
| Trải nghiệm user end-to-end? | User Journey | Vision & Scope |
| Quy tắc rẽ nhánh? | Decision Flowchart | SRS (BR) |
| Timeline dự án? | Gantt Chart | Vision & Scope |

> Chi tiết cú pháp và ví dụ: xem `core/diagram-guide.md`

---

## 8. Review & Approval Workflow

```
BA viết (Draft 0.1)
    ↓
BA self-review (BACCM Checklist)
    ↓
Peer review (BA khác hoặc QC)
    ↓
Technical review (Dev Lead — cho SRS/Data Model)
    ↓
Stakeholder review (PO / Sponsor)
    ↓
Sign-off → Version 1.0 (Baseline)
```

### Review Checklist tối thiểu

```
☐ Đúng template format (header, version, approval table)
☐ BACCM check pass (6/6 yếu tố)
☐ Requirement viết chuẩn SMART
☐ Diagram đi kèm (nếu applicable)
☐ Traceability: requirement có ID, link được
☐ Ngôn ngữ phù hợp đối tượng đọc
☐ Không còn placeholder / TODO
☐ Spelling & grammar check
```
