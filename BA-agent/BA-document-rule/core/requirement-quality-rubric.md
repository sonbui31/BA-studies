# REQUIREMENT QUALITY RUBRIC — Rubric Chấm Điểm Chất Lượng Yêu Cầu (v3.3)

> **Mục đích:** Đánh giá chất lượng MỖI CÂU requirement (FR/NFR/BRQ) trên thang 5 điểm.
> **Người dùng:** @ba-specialist (Inline Audit) + BA Manual Review.
> **Triết lý:** "Agent viết xong 1 FR → tự chấm → nếu < 3 điểm → tự sửa → rồi mới viết FR tiếp."

---

## 1. Thang Điểm 5 Bậc (5-Point Rubric)

| Điểm | Level | Tiêu chí | Ví dụ FR |
|:---:|-------|---------|----------|
| **5** | 🏆 **Exemplary** | SMART + Testable + Traceable + Có metric + Có constraint + Có actor | "Admin PHẢI thêm được tài sản mới với fields bắt buộc (Tên, Mã TS unique, Loại, Vị trí). Hệ thống validate trùng Mã TS trước khi lưu (response < 500ms). Trace: BRQ-01." |
| **4** | ✅ **Good** | SMART + Testable + Có constraint, thiếu trace hoặc metric | "Hệ thống PHẢI validate trùng Mã tài sản trước khi lưu, hiển thị lỗi inline nếu trùng." |
| **3** | 🟡 **Acceptable** | Rõ ràng, có actor, nhưng thiếu metric hoặc boundary | "Admin có thể thêm tài sản mới với các trường bắt buộc." |
| **2** | 🟠 **Weak** | Mơ hồ, thiếu actor, không test được | "Hệ thống quản lý tài sản." |
| **1** | 🔴 **Unacceptable** | Không phải requirement, chỉ là mong muốn | "Tài sản cần được quản lý tốt hơn." |

---

## 2. Smell Detector — 8 "Mùi" Yêu Cầu Kém Chất Lượng

> **Agent phải scan MỖI câu requirement qua 8 smell patterns trước khi chuyển sang câu tiếp.**

| # | Smell | Dấu hiệu | Fix | Ví dụ Trước → Sau |
|---|-------|----------|-----|-------------------|
| 1 | **Vague Adjective** | "nhanh", "đẹp", "dễ dùng", "linh hoạt", "hiệu quả" | Thay bằng metric cụ thể | "Load nhanh" → "Load < 3s cho p95" |
| 2 | **Passive Voice** | "Dữ liệu được xử lý", "Email được gửi" | Active: [Actor] + [verb] | "Email được gửi" → "Hệ thống gửi email" |
| 3 | **Missing Actor** | Không rõ AI thực hiện hay User | Thêm actor đầu câu | "Tạo báo cáo" → "Admin tạo báo cáo" |
| 4 | **Compound Requirement** | "PHẢI lưu, validate, VÀ gửi email" (3 actions = 3 FRs) | Tách thành N FRs | FR-01 lưu, FR-02 validate, FR-03 gửi email |
| 5 | **Implementation Bias** | "Dùng React", "Lưu vào PostgreSQL" | Bỏ tech, giữ behavior | "Dùng React hiển thị" → "Hệ thống hiển thị..." |
| 6 | **Missing Boundary** | "Hỗ trợ nhiều records", "upload file lớn" | Thêm số cụ thể | "File lớn" → "File ≤ 50MB, formats: PDF/XLSX/DOCX" |
| 7 | **Untestable NFR** | "An toàn", "sẵn sàng", "mở rộng được" | Thêm metric + target | "Hệ thống an toàn" → "Pass OWASP Top 10 với 0 Critical" |
| 8 | **Orphan Requirement** | Không link được về BRQ hoặc xuôi đến TC | Thêm Trace ID | "FR-AST-01" → "FR-AST-01 (Trace: BRQ-01 → TC-AST-01)" |

---

## 3. Scoring Workflow cho Agent

### 3.1 Inline Mode (khi đang viết tài liệu)

```
Agent viết FR-AST-01
  ↓
Chạy Smell Detector (8 patterns)
  ↓
Nếu ≥ 1 smell detected → Auto-fix → Re-score
  ↓
Score ≥ 3 → ✅ Proceed to FR-AST-02
Score < 3 → ⚠️ Flag + Attempt rewrite (max 2 attempts)
Score < 3 sau 2 attempts → 🔴 STOP + Ask user for clarification
```

### 3.2 Audit Mode (khi review tài liệu hoàn chỉnh)

```markdown
### 📊 Requirement Quality Audit Report

| FR ID | Raw Score | Smells Detected | Auto-Fixed? | Final Score |
|-------|:--------:|----------------|:-----------:|:-----------:|
| FR-AST-01 | 2 | Vague Adjective, Missing Boundary | ✅ Yes | 4 |
| FR-AST-02 | 4 | None | — | 4 |
| FR-AST-03 | 1 | Missing Actor, Compound, Untestable | ⚠️ Partial | 3 |

**Summary:** 12 FRs | Avg Score: 3.8/5 | 2 smells auto-fixed | 1 needs user input
**Quality Gate:** ≥ 3.0 avg = PASS ✅
```

---

## 4. Áp dụng cho Từng Loại Tài liệu

| Tài liệu | Level áp dụng | Threshold PASS | Ghi chú |
|-----------|:------------:|:--------------:|---------|
| **BRD** (BRQs) | Mỗi BRQ | ≥ 3/5 | BRQ thường high-level hơn FR → chấp nhận 3 |
| **SRS** (FRs) | Mỗi FR | ≥ 4/5 | FR cần chi tiết → yêu cầu cao hơn |
| **SRS** (NFRs) | Mỗi NFR | ≥ 4/5 | NFR PHẢI có metric |
| **Story Map** (ACs) | Mỗi AC scenario | ≥ 3/5 | GWT format tự giúp đạt 3+ |
| **UAT** (Test Cases) | Mỗi TC step | ≥ 3/5 | Expected Result phải cụ thể |

---

## 5. Escalation Rules

| Avg Score | Action |
|:---------:|--------|
| **≥ 4.0** | 🏆 Excellent — proceed without review |
| **3.0 - 3.9** | ✅ Acceptable — proceed, recommend improvement |
| **2.0 - 2.9** | ⚠️ Weak — must fix smells before proceeding |
| **< 2.0** | 🔴 Block — document cannot be used. Rewrite required |

---

## 6. Lệnh Kích hoạt

```
@ba-specialist chấm điểm chất lượng requirement cho file [X]
@ba-specialist chạy smell detector cho toàn bộ SRS
@ba-specialist inline audit FR vừa viết (rubric mode)
```
