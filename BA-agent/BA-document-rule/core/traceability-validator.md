# TRACEABILITY VALIDATOR (v3.4)

> **Mục đích:** Tự động phát hiện gaps trong cross-document traceability.
> **Trigger:** Chạy SAU khi sinh xong bộ tài liệu (hoặc khi user yêu cầu audit).
> **Output:** Full Chain Report + Missing Items List.

---

## 1. Mô hình Chuỗi Truy vết (Traceability Chain)

```text
FR Chain:  BRQ-ID (BRD) → FR-ID (SRS) → Feature-ID (Feature Map) → US-ID (Story Map) → AC/TC-ID
NFR Chain: BRQ-ID (BRD) → NFR-ID (SRS) → AC/TC-ID (Acceptance Criteria / UAT Plan)
```

Mỗi BRQ-ID phải có **ít nhất 1 đường đi hoàn chỉnh**. Với dự án canonical, strict mode còn yêu cầu mỗi FR map trực tiếp tới đúng 1 US, và mỗi US map trực tiếp tới đúng 1 AC/TC. NFR cũng PHẢI có Test Case hoặc Acceptance Criteria tương ứng (Performance test, Security test, etc.).

---

## 2. Quy trình Validation

### Step 1: Extract IDs từ mỗi tài liệu

| Tài liệu | ID Pattern | Ví dụ |
|---|---|---|
| BRD | `BRQ-XX`, `BRQ-XX.X` | BRQ-01, BRQ-06.3 |
| SRS | `FR-MOD-XXX`, `NFR-MOD-XXX` | FR-STC-001, NFR-SEC-001 |
| Feature Spec | `Fxx` | F01, F16, F20 |
| Story Map | `US-MOD-XXX` | US-ORD-001, US-CAP-013 |
| Acceptance Criteria / UAT Plan | `AC-MOD-XXX`, `TC-MOD-XXX` | AC-ORD-001, TC-CAP-011 |

### Step 2: Build Traceability Matrix tự động

```markdown
| BRQ-ID | BRD ✓ | SRS (FR/NFR) | Feature | Story (US) | AC/TC | Status |
|---|:---:|---|---|---|---|---|
| BRQ-01 | ✅ | FR-ORD-001 | F05 | US-ORD-001 | AC-ORD-001 | ✅ FULL |
| BRQ-07 | ✅ | FR-CAP-001 | F16 | US-CAP-013 | ??? | ❌ MISSING TC |
| BRQ-09.1 | ✅ | NFR-PERF-011 | F20 | US-RPT-016 | TC-RPT-004 | ✅ FULL |
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
| **MISSING_US_FOR_FR** | Canonical strict: FR không có US trực tiếp | 🔴 Critical ⭐ NEW v3.4.3 |
| **MULTIPLE_US_FOR_FR** | Canonical strict: FR map tới nhiều hơn 1 US trực tiếp | 🔴 Critical ⭐ NEW v3.4.3 |
| **MISSING_AC_FOR_US** | Canonical strict: US không có AC/TC trực tiếp | 🔴 Critical ⭐ NEW v3.4.3 |
| **MULTIPLE_AC_FOR_US** | Canonical strict: US map tới nhiều hơn 1 AC/TC trực tiếp | 🔴 Critical ⭐ NEW v3.4.3 |
| **INDEX_SKIP** | ID numbering nhảy cóc (VD: BRQ-01 → BRQ-03, thiếu BRQ-02) | 🔴 Critical ⭐ NEW v3.4 |
| **INDEX_DUPLICATE** | 2+ items cùng ID (VD: 2 cái US-ORD-001 hoặc 2 cái TC-ORD-003) | 🔴 Critical ⭐ NEW v3.4 |
| **HEADING_SKIP** | Section numbering nhảy cóc (VD: §2.1 → §2.3, thiếu §2.2) | 🟡 Warning ⭐ NEW v3.4 |

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
| 1 | MISSING_TC | BRQ-07 / US-CAP-013 | UAT Plan | Thêm TC cho "Nhập Công suất Thiết bị" |

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
| Sau sinh xong **tất cả core docs** | Tự động | Chạy Full Validation + Output Report |
| Sau sinh xong **1 doc** | Tự động (partial) | Chạy Partial Validation cho doc đó |
| User yêu cầu | Manual | `@ba-specialist kiểm tra truy vết toàn bộ dự án` |
| Trước sign-off | Mandatory | Agent PHẢI chạy trước khi tuyên bố "hoàn tất" |

### Lệnh script ưu tiên

```powershell
python .\scripts\traceability_scan.py <project-folder>
python .\scripts\traceability_scan.py <project-folder> --output-md traceability-report.md --output-json traceability-report.json
python .\scripts\traceability_scan.py <project-folder> --scheme legacy
python .\scripts\traceability_scan.py <project-folder> --scheme canonical --strict
```

> Dự án mới nên dùng `--scheme canonical --strict`. Legacy mode chỉ dùng cho bundle cũ có ID dạng `BRD-101 / FR-101 / US-001 / UAT-001`.

> Nếu tài liệu đang có drift về heading hoặc ID, chạy thêm:

```powershell
python .\scripts\reindex_markdown.py <project-folder>
python .\scripts\reindex_markdown.py <project-folder> --apply
python .\scripts\reindex_markdown.py <project-folder> --include-baseline --apply
```

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
| MISSING_US_FOR_FR | Sinh hoặc link đúng 1 US cho FR đang thiếu ⭐ NEW v3.4.3 |
| MULTIPLE_US_FOR_FR | Tách FR hoặc chọn 1 US owner, các US còn lại chuyển dependency ⭐ NEW v3.4.3 |
| MISSING_AC_FOR_US | Sinh hoặc link đúng 1 AC/TC cho US đang thiếu ⭐ NEW v3.4.3 |
| MULTIPLE_AC_FOR_US | Gộp/tách AC để mỗi US có đúng 1 artifact nghiệm thu owner ⭐ NEW v3.4.3 |
| INDEX_SKIP | Quét tất cả ID cùng prefix → Re-number tuần tự → Cập nhật cross-references ⭐ NEW v3.4 |
| INDEX_DUPLICATE | Flag 2 items trùng ID → Đề xuất rename item sau → Cập nhật cross-references ⭐ NEW v3.4 |
| HEADING_SKIP | Quét heading tree → Re-number tuần tự ⭐ NEW v3.4 |

---

## 5. Bi-Directional Tracing ⭐ NEW v3.2

> **Mục đích:** Không chỉ trace xuôi (BRQ→TC), mà còn trace ngược (TC→BRQ) — phát hiện items "mồ côi" ở cả hai đầu.

### Forward Scan (Xuôi): BRQ → FR/NFR → Feature → US → AC/TC
- "BRQ này dẫn đến Test Case nào?"
- Gap = Requirement chưa được test

### Reverse Scan (Ngược): TC → US → Feature → FR → BRQ
- "Test Case này thuộc User Story nào? Story đó có còn valid không?"
- Gap = Test Case cho requirement đã bị xóa/deprecated

### Reverse Scan Table

```markdown
| AC/TC-ID | Linked US | US Status | Linked FR | FR Status | Linked BRQ | BRQ Status | Verdict |
|---|---|:---:|---|:---:|---|:---:|:---:|
| AC-ORD-001 | US-ORD-001 | ✅ Active | FR-ORD-001 | ✅ Active | BRQ-01 | ✅ Active | ✅ Valid |
| TC-STC-005 | US-STC-008 | ❌ Deleted | FR-STC-003 | ❌ Deleted | BRQ-04 | ❌ Removed | 🔴 Stale — Remove TC |
| TC-CAP-011 | US-CAP-015 | ✅ Active | FR-CAP-002 | ⚠️ Changed | BRQ-07 | ⚠️ Updated | 🟡 Review TC |
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
    ├── FR-ORD-003 → ⚠️ REVIEW NEEDED
    │   ├── F07 → ⚠️ REVIEW NEEDED
    │   │   ├── US-ORD-005 → ⚠️ REVIEW NEEDED
    │   │   │   ├── AC-ORD-005 → ⚠️ UPDATE ACCEPTANCE CRITERIA
    │   │   │   └── TC-ORD-005 → ⚠️ UPDATE TEST CASE
    │   │   └── US-ORD-006 → ⚠️ REVIEW NEEDED
    │   │       └── AC-ORD-006 → ⚠️ UPDATE ACCEPTANCE CRITERIA
    │   └── Screen SCR-07 → ⚠️ UPDATE WIREFRAME
    └── NFR-PERF-003 → ⚠️ REVIEW NEEDED
        └── TC-PERF-003 → ⚠️ UPDATE TEST CASE
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
| Story Map | US-ORD-005, US-ORD-006 | ⚠️ Stale | Update AC (Given/When/Then) |
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
