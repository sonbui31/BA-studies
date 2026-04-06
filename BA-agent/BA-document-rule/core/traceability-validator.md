# TRACEABILITY VALIDATOR (v3.3)

> **Mục đích:** Tự động phát hiện gaps trong cross-document traceability.
> **Trigger:** Chạy SAU khi sinh xong bộ tài liệu (hoặc khi user yêu cầu audit).
> **Output:** Full Chain Report + Missing Items List.

---

## 1. Mô hình Chuỗi Truy vết (Traceability Chain)

```
FR Chain:  BRQ-ID (BRD) → FR-ID (SRS) → Feature-ID (Feature Spec) → US-ID (Story Map) → TC-ID (UAT Plan)
NFR Chain: BRQ-ID (BRD) → NFR-ID (SRS) → NFR-TC-ID (UAT Plan)  ⭐ NEW v3.2
```

Mỗi BRQ-ID phải có **ít nhất 1 đường đi hoàn chỉnh**. NFR cũng PHẢI có Test Case tương ứng (Performance test, Security test, etc.).

---

## 2. Quy trình Validation

### Step 1: Extract IDs từ mỗi tài liệu

| Tài liệu | ID Pattern | Ví dụ |
|---|---|---|
| BRD | `BRQ-XX`, `BRQ-XX.X` | BRQ-01, BRQ-06.3 |
| SRS | `FR-XXX-XX`, `NFR-XX` | FR-STC-01, NFR-03 |
| Feature Spec | `Fxx` | F01, F16, F20 |
| Story Map | `USxx` | US01, US15 |
| UAT Plan | `TC-XX-X` | TC-01-A, TC-11-B |

### Step 2: Build Traceability Matrix tự động

```markdown
| BRQ-ID | BRD ✓ | SRS (FR) | Feature | Story (US) | UAT (TC) | Status |
|---|:---:|---|---|---|---|---|
| BRQ-01 | ✅ | FR-F15-01 | F05 | US01 | TC-02-A | ✅ FULL |
| BRQ-07 | ✅ | FR-CAP-01 | F16 | US13 | ??? | ❌ MISSING TC |
| BRQ-09.1 | ✅ | NFR-11 | F20 | US16 | TC-04-E | ✅ FULL |
```

### Step 3: Gap Detection Rules

| Gap Type | Mô tả | Severity |
|---|---|---|
| **ORPHAN_BRQ** | BRQ tồn tại trong BRD nhưng không có FR nào trong SRS | 🔴 Critical |
| **ORPHAN_FR** | FR tồn tại trong SRS nhưng không có BRQ nào trong BRD | 🟡 Warning (có thể là NFR) |
| **MISSING_STORY** | BRQ có FR nhưng không có User Story | 🔴 Critical |
| **MISSING_TC** | User Story tồn tại nhưng không có Test Case | 🔴 Critical |
| **BROKEN_CHAIN** | Chuỗi đứt ở giữa (có BRQ + FR + US nhưng không có Feature) | 🟡 Warning |
| **DUPLICATE_MAP** | 2 BRQs cùng map tới 1 FR mà logic khác nhau | 🟡 Warning |
| **ORPHAN_NFR** | NFR tồn tại trong SRS nhưng không có NFR-TC trong UAT Plan | 🔴 Critical ⭐ NEW v3.2 |
| **STALE_REF** | TC reference một US đã bị xóa/deprecated | 🟡 Warning ⭐ NEW v3.2 |

### Step 4: Sinh Validation Report

```markdown
# 🔍 TRACEABILITY VALIDATION REPORT
> **Dự án:** [Tên] | **Ngày:** [Date] | **Phiên bản:** v3.0

## Tổng quan

| Metric | Giá trị |
|---|---|
| Tổng BRQ-IDs | XX |
| Full Chain (5/5) | XX (XX%) |
| Partial Chain | XX (XX%) |
| Broken/Missing | XX (XX%) |

## ✅ Full Chains (XX items)
[Bảng BRQ → FR → Feature → US → TC]

## ❌ Gaps Found (XX items)

### 🔴 Critical Gaps
| # | Gap Type | Item | Missing At | Suggested Fix |
|---|---|---|---|---|
| 1 | MISSING_TC | BRQ-07 / US13 | UAT Plan | Thêm TC cho "Nhập Công suất Thiết bị" |

### 🟡 Warnings
| # | Gap Type | Item | Detail |
|---|---|---|---|
| 1 | ORPHAN_FR | NFR-08 | NFR Availability không có BRQ tường minh (OK nếu là NFR chung) |

## 📋 Action Items
- [ ] [Critical] Thêm X Test Cases cho Y User Stories
- [ ] [Warning] Verify Z orphan FRs có cần thiết không
```

---

## 3. Khi nào Agent Tự Chạy Validator

| Thời điểm | Trigger | Hành động |
|---|---|---|
| Sau sinh xong **tất cả 5 docs** | Tự động | Chạy Full Validation + Output Report |
| Sau sinh xong **1 doc** | Tự động (partial) | Chạy Partial Validation cho doc đó |
| User yêu cầu | Manual | `@ba-specialist kiểm tra truy vết toàn bộ dự án` |
| Trước sign-off | Mandatory | Agent PHẢI chạy trước khi tuyên bố "hoàn tất" |

---

## 4. Auto-Fix Suggestions

Khi phát hiện gap, agent đề xuất fix cụ thể:

| Gap Type | Auto-Fix |
|---|---|
| MISSING_STORY | Sinh draft User Story từ BRQ description |
| MISSING_TC | Sinh draft Test Case từ AC trong Story |
| ORPHAN_BRQ | Sinh draft FR-ID skeleton trong SRS |
| BROKEN_CHAIN | Tìm Feature phù hợp nhất và suggest mapping |
| ORPHAN_NFR | Sinh draft NFR-TC (Performance test / Security test / Load test) ⭐ NEW v3.2 |
| STALE_REF | Flag TC cho review, suggest remove hoặc re-link ⭐ NEW v3.2 |

---

## 5. Bi-Directional Tracing ⭐ NEW v3.2

> **Mục đích:** Không chỉ trace xuôi (BRQ→TC), mà còn trace ngược (TC→BRQ) — phát hiện items "mồ côi" ở cả hai đầu.

### Forward Scan (Xuôi): BRQ → FR → Feature → US → TC
- "BRQ này dẫn đến Test Case nào?"
- Gap = Requirement chưa được test

### Reverse Scan (Ngược): TC → US → Feature → FR → BRQ
- "Test Case này thuộc User Story nào? Story đó có còn valid không?"
- Gap = Test Case cho requirement đã bị xóa/deprecated

### Reverse Scan Table

```markdown
| TC-ID | Linked US | US Status | Linked FR | FR Status | Linked BRQ | BRQ Status | Verdict |
|---|---|:---:|---|:---:|---|:---:|:---:|
| TC-01-A | US01 | ✅ Active | FR-F15-01 | ✅ Active | BRQ-01 | ✅ Active | ✅ Valid |
| TC-05-B | US08 | ❌ Deleted | FR-STC-03 | ❌ Deleted | BRQ-04 | ❌ Removed | 🔴 Stale — Remove TC |
| TC-11-A | US15 | ✅ Active | FR-CAP-02 | ⚠️ Changed | BRQ-07 | ⚠️ Updated | 🟡 Review TC |
```

---

## 6. Impact Chain — Change Propagation ⭐ NEW v3.2

> **Mục đích:** Khi 1 BRQ thay đổi → auto-flag TẤT CẢ items downstream bị ảnh hưởng.

### Trigger
- BRQ được thêm / sửa / xóa trong BRD
- FR được thêm / sửa / xóa trong SRS
- User chạy `@ba-specialist phân tích ảnh hưởng thay đổi BRQ-XX`

### Impact Propagation Logic

```
BRQ-03 CHANGED
    ├── FR-ORD-03 → ⚠️ REVIEW NEEDED
    │   ├── F07 → ⚠️ REVIEW NEEDED
    │   │   ├── US-05 → ⚠️ REVIEW NEEDED
    │   │   │   ├── TC-05-A → ⚠️ UPDATE TEST CASE
    │   │   │   └── TC-05-B → ⚠️ UPDATE TEST CASE
    │   │   └── US-06 → ⚠️ REVIEW NEEDED
    │   │       └── TC-06-A → ⚠️ UPDATE TEST CASE
    │   └── Screen SCR-07 → ⚠️ UPDATE WIREFRAME
    └── NFR-03 → ⚠️ REVIEW NEEDED
        └── NFR-TC-03 → ⚠️ UPDATE TEST CASE
```

### Impact Report Format

```markdown
## ⚡ IMPACT ANALYSIS: BRQ-03 Changed
> **Mô tả thay đổi:** {{mô tả}}
> **Ngày:** {{DD/MM/YYYY}}

| Layer | Impacted Item | Current Status | Action Required |
|---|---|:---:|---|
| SRS | FR-ORD-03 | ⚠️ Stale | Update logic cho phù hợp BRQ mới |
| Feature Spec | F07 | ⚠️ Stale | Review feature description |
| Story Map | US-05, US-06 | ⚠️ Stale | Update AC (Given/When/Then) |
| UAT Plan | TC-05-A, TC-05-B, TC-06-A | ⚠️ Stale | Rewrite test steps |
| Screen | SCR-07 | ⚠️ Stale | Update wireframe |
| NFR | NFR-03, NFR-TC-03 | ⚠️ Stale | Review NFR target + test |

**Total impacted items:** 9
**Estimated rework:** ~{{X}} giờ
```

---

## 7. Lệnh kích hoạt

```
@ba-specialist kiểm tra truy vết dự án [tên]
@ba-specialist chạy traceability validator cho bộ tài liệu hiện tại
@ba-specialist tìm BRQ nào chưa có Test Case
@ba-specialist đối chiếu Story Map vs BRD — cái nào bị sót?
@ba-specialist kiểm tra NFR nào chưa có Test Case
@ba-specialist trace ngược: TC-05-A thuộc BRQ nào?
@ba-specialist phân tích ảnh hưởng thay đổi BRQ-03
```
