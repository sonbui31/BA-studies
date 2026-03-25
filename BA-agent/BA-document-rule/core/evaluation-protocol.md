# GIAO THỨC ĐÁNH GIÁ TÀI LIỆU BA (Evaluation Protocol 2.2)

> **Mục đích:** Cung cấp khung chấm điểm khách quan và phản hồi có tính hành động cao cho mọi tài liệu Business Analysis.
> **Người thực hiện:** @ba-specialist (Orchestrating Multi-LLM)

---

## 1. Thang điểm Đánh giá (Scoring Scale)

Mỗi tài liệu sẽ được chấm trên thang điểm 10 dựa trên 4 trụ cột:

| Tiêu chí | Trọng số | Định nghĩa |
|----------|----------|------------|
| **Completeness (C)** | 30% | Độ đầy đủ so với template và yêu cầu thực tế. |
| **Clarity & SMART (S)** | 30% | Sự rõ ràng, không mơ hồ, dễ hiểu và có thể đo lường. |
| **Consistency (K)** | 20% | Tính nhất quán nội tại và nhất quán với các tài liệu khác. |
| **Actionability (A)** | 20% | Khả năng thực thi (Dev có code được không? QC có test được không?). |

**Xếp hạng:**
- **9.0 - 10:** Xuất sắc (Production Ready)
- **7.5 - 8.9:** Tốt (Cần sửa lỗi nhỏ)
- **5.0 - 7.4:** Trung bình (Cần review lại cấu trúc)
- **< 5.0:** Kém (Phải viết lại)

---

## 2. Quy trình Đánh giá (Multi-LLM Strategy)

Khi nhận yêu cầu đánh giá, @ba-specialist thực hiện:

1. **Phase 1: Deep Scan (Gemini 3 Pro)**
   - Đọc toàn bộ tài liệu và đối soát với bộ Rule (`BA-document-rule`).
   - Kiểm tra tính nhất quán với các tài liệu liên quan trong project.
2. **Phase 2: Logic Audit (OpenAI o4)**
   - Tìm lỗ hổng logic, mâu thuẫn giữa các requirements.
   - Phát hiện các "điểm mù" (Edge Cases) chưa được xử lý.
3. **Phase 3: Precision Review (Claude 4.6)**
   - Kiểm tra tính thẩm mỹ của sơ đồ Mermaid.
   - Review câu từ, định dạng theo `writing-guide.md`.
4. **Phase 4: Scoring & Feedback (GPT-5)**
   - Tổng hợp điểm số và đưa ra bảng "Action Items" ưu tiên.

---

## 3. Format Báo cáo Đánh giá (Output Format)

```markdown
# 🔍 BÁO CÁO ĐÁNH GIÁ: [Tên Tài Liệu]
> **Phiên bản:** 2.2 | **Trạng thái:** [Pass/Fail/Pending]

## 📊 Tổng điểm: [X.X] / 10

| Tiêu chí | Điểm | Nhận xét nhanh |
|---|---|---|
| Completeness | 8/10 | Thiếu phần NFR |
| clarity & SMART | 7/10 | Story ID 04 còn mơ hồ |
| Consistency | 9/10 | Khớp với Vision & Scope |
| Actionability | 8/10 | AC viết tốt |

## ✅ Điểm mạnh
- [Liệt kê các điểm làm tốt]

## ⚠️ Các vấn đề cần khắc phục (Prioritized)
1. **[High]** Sửa lỗi logic tại Section X...
2. **[Medium]** Thêm sơ đồ Sequence cho luồng Y...

## 🤖 AI Insight (o4 Reasoning)
- "Hệ thống có rủi ro mâu thuẫn tại điểm Z nếu user thực hiện thao tác..."

---
*Được thực hiện bởi @ba-specialist v2.2*
```

---

## 4. Các lệnh đánh giá mẫu

- `@[ba-specialist] hãy đánh giá file [tài liệu] theo protocol 2.2`
- `@[ba-specialist] audit logic và chấm điểm SRS này`
- `@[ba-specialist] kiểm tra chéo BRD này với Vision & Scope đã có`
