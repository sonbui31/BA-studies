# ĐỐI SOÁT YÊU CẦU VS MÃ NGUỒN (Requirement-to-Code Audit 3.0)

> **Mục đích:** Đảm bảo Implementation khớp chính xác với SRS/Stories.
> **Kỹ thuật:** Multi-LLM Code Analysis + Automated Traceability Mapping.
> **v3.0 thay đổi:** Actionable quy trình, có output format rõ ràng, kết hợp với Traceability Validator.

---

## 1. Khi nào Chạy Code Audit

| Thời điểm | Trigger | Scope |
|-----------|---------|-------|
| Sau Sprint kết thúc | Sprint Review | Code changed trong sprint → verify vs Sprint Stories |
| Trước UAT | Pre-UAT gate | Toàn bộ codebase vs toàn bộ SRS |
| Change Request | CR approved | CR items → verify code changed đúng |
| User request | Manual | `@ba-specialist đối soát [doc] với [code folder]` |

---

## 2. Quy trình Đối soát (Multi-LLM)

### Step 1: Requirement Extraction
- Trích danh sách FR-IDs + AC từ SRS/Story Map
- Map: FR-ID → Function/Component expected
- **LLM:** Gemini 3 Pro — đọc large context (full SRS + Story Map)

### Step 2: Code Analysis
- Scan source code (structure, function names, routes, DB models)
- Build: Code Component Index (file → function → purpose)
- **LLM:** Claude 4.6 — precise code reading + semantic understanding

### Step 3: Traceability Mapping
- Map: FR-ID ↔ Code Component
- Detect:
  - **Unimplemented:** FR exists in SRS, no matching code
  - **Excess Code:** Code exists but no FR requires it
  - **Logic Mismatch:** Code implements FR but logic differs from spec
- **LLM:** OpenAI o4 — reasoning, logic contradiction detection

### Step 4: Data & Event Verification
- Check tracking events in code match Data Model/Tracking Plan
- Check DB schema matches SRS Data Dictionary
- **LLM:** GPT-5 — schema comparison, naming consistency

### Step 5: Report Generation
- Tổng hợp kết quả → sinh Audit Report

---

## 3. Output Format

```markdown
# 🔍 REQUIREMENT-TO-CODE AUDIT REPORT
> **Dự án:** [Tên] | **Ngày:** [Date] | **Phiên bản:** 3.0

## 📊 Tổng quan

| Metric | Giá trị |
|---|---|
| Tổng FRs trong SRS | XX |
| FRs implemented | XX (XX%) |
| FRs missing in code | XX (XX%) |
| Excess code (no FR) | XX items |
| Logic mismatches | XX items |

## ✅ Matched (XX items)
| FR-ID | Description | Code Location | Status |
|---|---|---|---|
| FR-STC-01 | CRUD Tài sản | `src/modules/assets/` | ✅ Matched |

## ❌ Unimplemented (XX items)
| FR-ID | Description | Expected In | Priority |
|---|---|---|---|
| FR-CAP-01 | Capacity Tracking | `src/modules/capacity/` | 🔴 Must Have |

## ⚠️ Logic Mismatch (XX items)
| FR-ID | SRS Says | Code Does | Impact |
|---|---|---|---|
| FR-RPT-03 | "Filter by date range" | Only filters by single date | 🟡 User sees wrong data |

## 📦 Excess Code (XX items)
| Code Location | Function | Notes |
|---|---|---|
| `src/utils/legacy.js` | `migrateLegacy()` | No FR found — may be dead code |

## 📋 Action Items
- [ ] [Critical] Implement FR-CAP-01 — Capacity Tracking
- [ ] [High] Fix logic mismatch in FR-RPT-03
- [ ] [Low] Review excess code for cleanup
```

---

## 4. Integration với Traceability Validator

Code Audit kết nối với `traceability-validator.md` để tạo **full chain**:

```
BRQ-ID (BRD) → FR-ID (SRS) → Feature-ID → US-ID → TC-ID → CODE (Source)
```

Khi chạy Code Audit, agent cập nhật Traceability Matrix thêm cột `Code Status`:

| BRQ-ID | FR-ID | US-ID | TC-ID | Code Status |
|---|---|---|---|---|
| BRQ-01 | FR-STC-01 | US01 | TC-02-A | ✅ Implemented |
| BRQ-07 | FR-CAP-01 | US13 | TC-11-B | ❌ Not Found |

---

## 5. Lệnh kích hoạt

```
@ba-specialist đối soát SRS với mã nguồn trong [thư mục src]
@ba-specialist kiểm tra FR [FR-ID] đã code đúng AC chưa
@ba-specialist audit xem Story nào trong Sprint 3 chưa code
@ba-specialist tìm dead code không có requirement tương ứng
@ba-specialist chạy full chain audit: BRQ → FR → US → TC → Code
```
