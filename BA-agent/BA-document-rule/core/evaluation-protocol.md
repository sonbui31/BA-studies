# GIAO THỨC ĐÁNH GIÁ TÀI LIỆU BA (Evaluation Protocol 3.3)

> **Mục đích:** Khung chấm điểm khách quan với **inline audit** — đánh giá realtime khi đang sinh tài liệu, không chờ cuối.
> **Người thực hiện:** @ba-specialist (Multi-LLM Orchestrated)

---

## 1. Thang điểm Đánh giá (Scoring Scale)

Mỗi tài liệu được chấm trên thang điểm 10 dựa trên 4 trụ cột:

| Tiêu chí | Trọng số | Định nghĩa |
|----------|----------|------------|
| **Completeness (C)** | 30% | Độ đầy đủ so với template, Pre-Flight Checklist, và yêu cầu thực tế |
| **Clarity & SMART (S)** | 30% | Sự rõ ràng, không mơ hồ, **Requirement Quality Rubric ≥ 3/5**, **Không lỗi chính tả (Zero-Tolerance)** |
| **Consistency (K)** | 20% | Nhất quán nội tại + cross-document + **Trật tự chỉ mục/đánh số chuẩn** + **Conflict Detection** |
| **Actionability (A)** | 20% | Dev có triển khai được không? QC có kiểm tra được không? AC bao phủ quy tắc và rủi ro theo Tier của repo |

**Xếp hạng:**
- **9.0 - 10:** Xuất sắc (Production Ready)
- **7.5 - 8.9:** Tốt (Cần sửa lỗi nhỏ)
- **5.0 - 7.4:** Trung bình (Cần review lại cấu trúc)
- **< 5.0:** Kém (Phải viết lại)

---

## 2. Quy trình Đánh giá (Multi-LLM Strategy)

### 2.1 Inline Audit (⭐ ENHANCED v3.3 — Chạy TRONG KHI viết)

Sau mỗi major section khi sinh tài liệu, agent thực hiện **quick C-S-K-A check** + **Smell Detector**:

```markdown
### ✅ Inline Check: [Tên Section]
| C | S | K | A | Rubric Avg | Smells | Quick Notes |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| ✓ | ✓ | ⚠ | ✓ | 3.8/5 | 1 fixed | K: Cần verify ID mapping với BRD |
```

**Inline Rules:**
- ⚠ Warning → Ghi chú, tiếp tục viết, fix ở cuối
- ❌ Fail → STOP section, fix ngay trước khi viết tiếp
- 🔍 Smell Detected → Auto-fix (max 2 attempts) → nếu vẫn fail → flag cho user
- Mục đích: Bắt lỗi **sớm**, giảm rework từ 4+ vòng → ≤ 2 vòng

**v3.3 Additions:**
- Chạy **Requirement Quality Rubric** score cho mỗi FR/NFR vừa viết
- Chạy **Conflict Detection** scan sau mỗi nhóm FRs liên quan
- Check **AC Coverage** theo rule và Tier; không ép đủ bốn loại tình huống khi không áp dụng

### 2.2 Full Audit (Chạy SAU KHI hoàn tất document)

Khi nhận yêu cầu đánh giá toàn bộ, @ba-specialist thực hiện:

1. **Phase 1: Deep Scan (Gemini 3 Pro)**
   - Đọc toàn bộ tài liệu, đối soát với bộ Rule (`BA-document-rule`)
   - Kiểm tra nhất quán cross-document (BRD ↔ SRS ↔ Stories ↔ UAT)
   - Verify Pre-Flight Checklist items đều PASS

2. **Phase 2: Logic Audit (OpenAI o4)**
   - Tìm contradictions giữa requirements — **dùng 6 Conflict Detection Patterns** (`writing-guide.md` §12), rà bằng đọc hiểu vì script không tự phát hiện mâu thuẫn
   - Phát hiện edge cases chưa xử lý — **check AC coverage 8 loại** (`writing-guide.md` §11)
   - Verify Business Rules không mâu thuẫn
   - **v3.3:** Validate assumptions đã được verify (`writing-guide.md` §13)

3. **Phase 3: Precision Review (Claude 4.6)**
   - Review câu từ theo `writing-guide.md`
   - **Zero-Tolerance Check:** Bắt buộc không sai chính tả, không lộn xộn layout, đánh số tuần tự (1., 1.1, 1.2)
   - Kiểm tra User Stories chuẩn INVEST
   - Verify Acceptance Criteria chuẩn BDD

4. **Phase 4: Scoring & Feedback (GPT-5)**
   - Tổng hợp điểm số C-S-K-A
   - **v3.3:** Tổng hợp Requirement Quality Rubric scores (avg per doc)
   - Sinh bảng "Action Items" ưu tiên theo severity
   - Cross-check với Traceability Validator results

---

### 2.3 Review theo vai trò trước khi người thật duyệt

Sau Full Audit, dùng `persona-simulation.md` để kiểm tra **vai trò bắt buộc theo Tier trên từng tài liệu** (Tier 3 đủ 21), với một dòng PASS/ISSUE/N/A và căn cứ cho từng vai trò; đọc sâu các vai trò liên quan theo loại tài liệu/Tier. N/A cần lý do cụ thể. Chạy `persona_review_check.py` trên báo cáo của từng tài liệu; thiếu vai trò hoặc còn PENDING thì chưa hoàn tất. Báo cáo riêng từng phát hiện với bằng chứng, tác động, đề xuất và decision owner. Mục `BLOCK` cần người có quyền xác nhận; không lấy điểm C-S-K-A hoặc phiếu đa số để tự duyệt. Vai trò AI là mô phỏng phục vụ review, không thay ý kiến thật của stakeholder.

---

## 3. Format Báo cáo Đánh giá (Output Format)

```markdown
# 🔍 BÁO CÁO ĐÁNH GIÁ: [Tên Tài Liệu]
> **Phiên bản Agent:** 3.5.5 | **Trạng thái:** [Pass/Fail/Pending]
> **Pre-Flight Status:** [X/Y PASS] | **Traceability:** [Full/Partial/Broken]
> **Rubric Avg:** [X.X/5] | **Conflicts:** [N detected] | **AC Coverage:** [Các rule và rủi ro liên quan đã bao phủ / còn thiếu]
> **Review theo vai trò:** [N/N vai trò bắt buộc của Tier đã kiểm tra] | [Không phát hiện vấn đề / Cần sửa / Chờ quyết định] — báo cáo riêng theo `persona-simulation.md`

## 📊 Tổng điểm: [X.X] / 10

| Tiêu chí | Điểm | Nhận xét nhanh |
|---|---|---|
| Completeness | X/10 | [Chi tiết] |
| Clarity & SMART | X/10 | [Chi tiết] |
| Consistency | X/10 | [Chi tiết] |
| Actionability | X/10 | [Chi tiết] |

## ✅ Điểm mạnh
- [Liệt kê điểm tốt]

## ⚠️ Các vấn đề cần khắc phục (Prioritized)
1. **[Critical]** [Mô tả + Suggested Fix]
2. **[High]** [Mô tả + Suggested Fix]
3. **[Medium]** [Mô tả + Suggested Fix]

## 🔗 Cross-Document Consistency Check
| Doc A | Doc B | Check | Status |
|---|---|---|---|
| BRD BRQ-01 | SRS FR-01 | ID mapping | ✅ Matched |
| SRS FR-05 | Story Map US-07 | Coverage | ❌ Missing Story |

## 🤖 AI Insight (o4 Reasoning)
- "[Edge case / contradiction phát hiện]"

## 📋 Pre-Flight vs Actual
| Check Item | Pre-Flight (before) | Actual (after) |
|---|---|---|
| MoSCoW Priority | ✅ PASS | ✅ Confirmed in BRD §3 |
| Data Dictionary | ⚠ PARTIAL | ✅ Fixed — 12/12 entities covered |

---
*Được thực hiện bởi @ba-specialist v3.3*
```

---

## 4. Các lệnh đánh giá

```
@ba-specialist đánh giá file [tài liệu] theo protocol 3.3
@ba-specialist audit logic và chấm điểm SRS này
@ba-specialist kiểm tra chéo BRD này với SRS và Story Map
@ba-specialist chạy inline audit cho section [X] vừa viết
@ba-specialist so sánh Pre-Flight results trước vs sau khi viết
@ba-specialist chạy Requirement Quality Rubric cho toàn bộ SRS
@ba-specialist scan conflict detection cho file [X]
@ba-specialist kiểm tra AC coverage cho Must stories
```
