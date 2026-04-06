# AI/ML FEATURE SPECIFICATION — Template
# {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}
> **⭐ NEW v3.1** — Template dành cho hệ thống có tính năng AI/ML

---

## Lịch sử thay đổi

| Phiên bản | Ngày | Người chỉnh | Mô tả thay đổi |
|-----------|------|-------------|----------------|
| 0.1 | {{ngày}} | {{tên}} | Phiên bản đầu tiên |

---

## 1. Mục đích tài liệu

> Tài liệu này mô tả chi tiết spec cho các tính năng AI/ML trong dự án {{Tên dự án}}.
> **Khi nào cần:** Khi hệ thống có ≥ 1 tính năng sử dụng AI/ML (NLP, OCR, Classification, Recommendation, Anomaly Detection, etc.)
> **Quan hệ:** Bổ sung cho BRD (business rules) và SRS (technical spec). KHÔNG thay thế.

### Đối tượng đọc

| Đối tượng | Mục đích đọc |
|-----------|-------------|
| BA / PM | Hiểu scope AI, đánh giá feasibility |
| AI/ML Engineer | Cơ sở để thiết kế model, chọn approach |
| QC / Tester | Biết cách test AI output (accuracy, edge cases) |
| Product Owner | Quyết định trade-off (accuracy vs speed vs cost) |

---

## 2. AI Behavior Definition (Định nghĩa Hành vi AI)

> Mỗi hành vi AI là 1 "khả năng" mà hệ thống cần có. Liệt kê TẤT CẢ hành vi AI ở đây.

| # | Behavior ID | Tên Hành vi | Input | Expected Output | Loại AI | BRQ liên quan |
|---|------------|------------|-------|-----------------|---------|---------------|
| 1 | AIB-001 | {{VD: Trích xuất bảng từ PDF}} | {{VD: File PDF/Scan}} | {{VD: Dữ liệu bảng dạng structured}} | {{VD: OCR + Table Extraction}} | BR-xxx |
| 2 | AIB-002 | {{VD: Đối chiếu ngữ nghĩa}} | {{VD: 2 danh sách chỉ tiêu}} | {{VD: Mapping 1-1 + lỗi sai lệch}} | {{VD: NLP Semantic Matching}} | BR-xxx |
| 3 | AIB-003 | {{VD: Truy vấn lịch sử}} | {{VD: Context hiện tại + Folder history}} | {{VD: Quyết định override lỗi}} | {{VD: Rule-based + Database Query}} | BR-xxx |

---

## 3. Accuracy Requirements (Yêu cầu Độ chính xác)

> **Quan trọng:** Mọi AI behavior PHẢI có accuracy target. "AI chính xác" ❌ → "Precision ≥ 90%" ✅

### 3.1 Accuracy Targets

| Behavior ID | Metric | Target | Acceptable Min | Đo bằng cách nào |
|------------|--------|:------:|:--------------:|---|
| AIB-001 | Character Accuracy (OCR) | ≥ {{95%}} | ≥ {{90%}} | {{So sánh OCR output vs ground truth trên 100 mẫu}} |
| AIB-002 | Precision (đúng khi báo match) | ≥ {{90%}} | ≥ {{85%}} | {{So sánh AI mapping vs expert mapping}} |
| AIB-002 | Recall (không bỏ sót) | ≥ {{95%}} | ≥ {{90%}} | {{Đếm số lỗi AI miss / tổng lỗi thực tế}} |
| AIB-003 | Decision Accuracy | ≥ {{95%}} | ≥ {{90%}} | {{So sánh AI override decision vs expert decision}} |

### 3.2 False Positive / False Negative Impact

| Behavior ID | False Positive (Báo sai) | Impact | False Negative (Bỏ sót) | Impact |
|------------|---|---|---|---|
| AIB-001 | OCR đọc sai ký tự | 🟡 Medium — user phải sửa tay | OCR bỏ sót dòng/cột | 🔴 High — mất dữ liệu |
| AIB-002 | Báo "match" nhưng thực tế khác | 🟡 Medium — bỏ sót lỗi thật | Báo "không match" nhưng thực tế giống | 🟡 Medium — gây noise |

> ⚠️ **Quy tắc:** Luôn đánh giá cái nào **nguy hiểm hơn** — False Positive hay False Negative — để điều chỉnh model bias.

---

## 4. Human-in-the-Loop Design (Thiết kế Con người Trong Vòng lặp)

> **Triết lý:** AI assist, Human decide. Trừ khi accuracy ≥ 99% VÀ impact thấp, luôn cho user review.

### 4.1 Confidence-based Action Matrix

| Confidence Level | Range | UI Behavior | User Action | Feedback Loop |
|---|:---:|---|---|---|
| 🟢 **High** | ≥ {{90%}} | Auto-accept, hiển thị kết quả | Review nếu muốn | None (silent) |
| 🟡 **Medium** | {{70-90%}} | Highlight kết quả, yêu cầu confirm | PHẢI review & confirm/reject | User correction → cập nhật knowledge base |
| 🔴 **Low** | < {{70%}} | Cảnh báo "Không chắc chắn" | PHẢI review thủ công | User correction → retrain candidate |

### 4.2 Override & Feedback Mechanism

| Action | User Flow | System Response |
|--------|-----------|-----------------|
| User **confirms** AI result | Click ✅ | Ghi nhận positive feedback |
| User **rejects** AI result | Click ❌ + nhập correction | Ghi nhận negative feedback + log correction |
| User **overrides** AI severity | Đổi từ 🔴 → 🟡 hoặc ngược lại | Ghi nhận override + reason |

> **Feedback data** được dùng để:
> - Đo lường accuracy thực tế (production accuracy)
> - Cải thiện model/rules trong phiên bản tiếp

---

## 5. Training Data & Knowledge Base

### 5.1 Initial Training Data

| # | Data Source | Volume | Format | Chất lượng | Owner |
|---|-----------|:------:|--------|:----------:|-------|
| 1 | {{VD: 500 file PDF đã kiểm tra}} | {{500 files}} | {{PDF}} | {{Cao — đã human-verified}} | {{Phòng KH}} |
| 2 | {{VD: Bảng synonym ngành}} | {{200 cặp}} | {{CSV}} | {{TB — cần review}} | {{BA}} |

### 5.2 Data Quality Requirements

| Tiêu chí | Yêu cầu |
|----------|---------|
| **Volume tối thiểu** | ≥ {{X}} samples cho mỗi AI Behavior |
| **Label quality** | ≥ {{Y%}} samples đã được ≥ 2 người verify |
| **Diversity** | Cover ≥ {{Z%}} edge cases đã biết |
| **Freshness** | Data không cũ quá {{N}} tháng |

---

## 6. User-Managed Knowledge Base (Configurable Intelligence) ⭐

> **Khi nào cần:** Khi AI cần kiến thức chuyên ngành mà thay đổi theo thời gian, và user (không phải dev) cần tự cập nhật.
> **Ví dụ:** Từ điển đồng nghĩa, bảng quy đổi đơn vị, danh mục phân loại, threshold configs.

### 6.1 Knowledge Base Specification

| Aspect | Specification |
|--------|--------------|
| **Tên KB** | {{VD: Từ điển Đồng nghĩa Chỉ tiêu Môi trường}} |
| **Data type** | {{VD: Synonym pairs (Thuật ngữ A = Thuật ngữ B)}} |
| **Upload format** | {{VD: CSV/Excel — columns: term_1, term_2, category}} |
| **Ai được quản lý?** | {{VD: Trưởng phòng + Admin}} |
| **Validation khi upload** | {{VD: Duplicate check, format check, tối đa X rows}} |
| **Version control** | {{VD: Có — giữ 5 phiên bản gần nhất, rollback được}} |
| **Scope** | {{VD: Global (toàn công ty) / Per-project / Per-department}} |
| **Có hiệu lực ngay?** | {{VD: Có / Cần Trưởng phòng approve trước}} |

### 6.2 Knowledge Base CRUD Matrix

| Action | Nhân viên | Trưởng phòng | Admin |
|--------|:---------:|:------------:|:-----:|
| Xem KB hiện tại | ✅ | ✅ | ✅ |
| Đề xuất thêm/sửa entry | ✅ (đề xuất) | ✅ (trực tiếp) | ✅ |
| Approve đề xuất | ❌ | ✅ | ✅ |
| Upload bulk (CSV/Excel) | ❌ | ✅ | ✅ |
| Xoá entry | ❌ | ✅ | ✅ |
| Rollback version | ❌ | ❌ | ✅ |

### 6.3 Inline Knowledge Extension

> **Pattern nâng cao:** Cho phép user bổ sung KB **ngay trong kết quả kiểm toán**.

```
Ví dụ:
AI báo "Lệch tên gọi: File Gốc = Ammonia, Kế hoạch = NH3"
→ User click "Thêm vào từ điển" → Tự động tạo entry (Ammonia = NH3)
→ Lần sau AI tự nhận ra, không báo nữa.
```

---

## 7. Fallback Behavior (Hành vi Dự phòng)

> **Triết lý:** AI PHẢI có fallback cho mọi failure scenario. Không bao giờ "im lặng fail".

| # | Failure Scenario | Fallback Action | User Notification |
|---|---|---|---|
| 1 | OCR không đọc được file (quá mờ, format lạ) | Dừng xử lý, hiển thị vùng lỗi | "⚠️ Không đọc được trang X. Vui lòng upload file rõ hơn." |
| 2 | AI confidence < threshold | Hiển thị kết quả với cảnh báo | "🟡 Kết quả chưa chắc chắn (70%). Vui lòng kiểm tra thủ công." |
| 3 | Không tìm thấy dữ liệu lịch sử | Bỏ qua Memory Check, thông báo | "ℹ️ Chưa có lịch sử trong Folder này. QT-6 bị skip." |
| 4 | File Gốc chưa được upload | Không chạy đối chiếu | "❌ Chưa có File Gốc trong DMS. Vui lòng upload trước." |
| 5 | Timeout xử lý (file quá lớn) | Xử lý background, thông báo khi xong | "⏳ File lớn, đang xử lý. Sẽ thông báo khi hoàn tất." |

---

## 8. Explainability (Khả năng Giải thích)

> **Triết lý:** User PHẢI hiểu **TẠI SAO** AI đưa ra kết quả đó. Black box ❌.

### 8.1 Explanation Level per Behavior

| Behavior ID | Explanation Type | Ví dụ Output |
|---|---|---|
| AIB-001 (OCR) | Highlight vùng trích xuất trên file gốc | Bôi vàng vùng text đã OCR trên ảnh PDF |
| AIB-002 (Matching) | Hiển thị lý do match/not match | "NH3 ≈ Ammonia (từ điển đồng nghĩa #42)" |
| AIB-003 (Memory) | Hiển thị lịch sử truy vấn | "Đợt 1 (15/01): ✅ Mùi, Đợt 2 (15/04): ✅ Mùi → Đã đủ 2/2 lần" |

### 8.2 Audit Trail

| Thông tin | Ghi lại? | Format |
|-----------|:--------:|--------|
| Input file + version | ✅ | File hash + timestamp |
| AI model/version | ✅ | "OCR v2.1 + Matcher v1.3" |
| Knowledge Base version | ✅ | "Synonym KB v5 (updated 01/03/2026)" |
| Confidence scores | ✅ | Per-item confidence |
| User overrides | ✅ | Who + When + Old value + New value + Reason |

---

## 9. AI Performance & Monitoring

### 9.1 Production Metrics (Post-deployment)

| Metric | Target | Alert Threshold | Đo bằng |
|--------|:------:|:---------------:|---------|
| Processing time (per file) | ≤ {{X}} giây | > {{Y}} giây | System log |
| Production accuracy | ≥ {{X%}} | < {{Y%}} | User feedback (confirm/reject rate) |
| False negative rate | ≤ {{X%}} | > {{Y%}} | QC spot-check hàng tuần |
| User override rate | ≤ {{X%}} | > {{Y%}} | Override log |

### 9.2 Model Degradation Detection

```
IF user_override_rate > threshold FOR 2_consecutive_weeks:
  → ALERT: "AI accuracy giảm. Cần review model/knowledge base."
  → ACTION: QC spot-check 50 samples → retrain/update nếu cần
```

---

## 10. Ethical & Security Considerations

| Concern | Mitigation |
|---------|-----------|
| **Bias trong training data** | Đảm bảo data đa dạng, review by ≥ 2 domain experts |
| **PII/Confidential data** | KHÔNG gửi dữ liệu khách hàng lên AI cloud API nếu chưa có NDA |
| **AI hallucination** | Rule-based validation layer ĐÈ LÊN AI output |
| **Over-reliance** | UI PHẢI hiển thị disclaimer "Kết quả AI chỉ mang tính tham khảo" |

---

## ✅ AI Feature Self-Check

```
☐ BEHAVIOR:     Mọi AI behavior có ID + Input + Output rõ ràng (Mục 2)
☐ ACCURACY:     Mọi behavior có accuracy target đo được (Mục 3)
☐ HUMAN-LOOP:   Confidence matrix + Override flow đã thiết kế (Mục 4)
☐ DATA:         Training data identified + quality requirements set (Mục 5)
☐ KNOWLEDGE:    User-managed KB đã spec (nếu applicable) (Mục 6)
☐ FALLBACK:     Mọi failure scenario có fallback action (Mục 7)
☐ EXPLAINABLE:  User hiểu được TẠI SAO AI ra kết quả (Mục 8)
☐ MONITORING:   Production metrics + degradation alert (Mục 9)
☐ ETHICAL:       PII/Bias/Hallucination đã address (Mục 10)
```
