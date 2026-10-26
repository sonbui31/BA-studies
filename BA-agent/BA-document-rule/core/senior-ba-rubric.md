# SENIOR BA RUBRIC: Thang đánh giá năng lực và cách kiểm tra đầu ra

> **Mục đích:** Kiểm tra một câu trả lời, một bộ tài liệu hoặc một quyết định của BA-agent đạt mức nào. Dùng cho reviewer người thật hoặc LLM-judge.
> **Bộ tình huống kèm theo:** `tests/golden/senior_judgement_cases.jsonl`.
> **Khác với** `requirement-quality-rubric.md`: file đó chấm từng câu yêu cầu; file này chấm phán đoán BA.

---

## 1. Bốn mức

| Mức | Tên | Mô tả ngắn |
|:-:|---|---|
| 1 | Junior | Làm theo hướng dẫn, ghi lại điều được nói, chưa phát hiện khoảng trống |
| 2 | Middle | Viết tài liệu đúng chuẩn, tự phát hiện lỗi định dạng và truy vết, nhưng chấp nhận yêu cầu như được giao |
| 3 | Senior | Đặt lại vấn đề, tìm phương án, nêu đánh đổi bằng số, quản lý xung đột, điều chỉnh độ chặt theo rủi ro |
| 4 | Lead | Định hình cách làm cho cả đội, thiết lập tiêu chuẩn, ra quyết định khi thiếu thông tin và chịu trách nhiệm kết quả |

---

## 2. Chín chiều đánh giá

| # | Chiều | 1 (Junior) | 2 (Middle) | 3 (Senior) |
|:-:|---|---|---|---|
| 1 | **Đặt vấn đề** | Chép yêu cầu như được nêu | Viết Problem Statement | Tách vấn đề khỏi giải pháp, hỏi bằng chứng và hậu quả của việc không làm |
| 2 | **Bằng chứng** | Ghi lời nói | Ghi nguồn | Gắn mức bằng chứng (E1–E4), thiết kế cách đo khi thiếu baseline |
| 3 | **Phương án và đánh đổi** | Một phương án | So sánh định tính | Có Do Nothing và phương án nhẹ, tính số, độ nhạy, điều kiện dừng |
| 4 | **Stakeholder và xung đột** | Ghi tất cả yêu cầu | Lập Stakeholder Map | Ghi xung đột, xác định người quyết định, không chọn phe, ghi lại quyết định |
| 5 | **Độ chặt theo rủi ro** | Áp dụng mọi quy tắc như nhau | Tuân thủ template | Chọn Tier theo rủi ro, ghi lý do khi nới hoặc siết |
| 6 | **Chất lượng yêu cầu và truy vết** | Viết FR/AC theo mẫu | Truy vết đủ, không smell | Phát hiện mâu thuẫn giữa FR, AC, KPI; kiểm tra nghĩa, không chỉ ID |
| 7 | **Truyền thông** | Chuyển thông tin nguyên văn | Viết đúng ngôn ngữ theo độc giả | Dẫn bằng quyết định cần chốt, nêu hệ quả bằng số, đưa lựa chọn |
| 8 | **Tuân thủ và đạo đức** | Bỏ qua | Ghi vào rủi ro | Phát hiện dữ liệu nhạy cảm và ràng buộc pháp lý, chuyển đúng người, không tự kết luận |
| 9 | **Đo giá trị** | Không có KPI | KPI có target | KPI có baseline, mẫu số, nguồn, guardrail, lịch review, quy tắc quyết định |

---

## 3. Quy tắc xếp mức

- Chấm từng chiều 1–3. Mức 4 (Lead) không chấm được từ một đầu ra; chỉ xét qua việc cả đội theo cách làm đó.
- **Senior:** không chiều nào dưới 2 và ít nhất 6 trong 9 chiều ở mức 3.
- **Middle:** không chiều nào ở mức 1 trong các chiều 3, 6, 8 và ít nhất 5 chiều từ mức 2 trở lên.
- Còn lại: Junior.
- Một dấu hiệu đỏ (mục 4) hạ cả bài xuống một mức bất kể điểm.

---

## 4. Dấu hiệu đỏ

| Dấu hiệu | Vì sao nghiêm trọng |
|---|---|
| Bịa số liệu, ví dụ ROI hoặc baseline không có nguồn | Phá niềm tin; quyết định dựa trên số giả |
| Nhận giải pháp của Sponsor làm yêu cầu đã chốt | Bỏ qua vấn đề thực |
| Kết luận pháp lý ("luật cho phép") | BA không có thẩm quyền |
| Bỏ qua dữ liệu nhạy cảm (trẻ em, sinh trắc, y tế, tài chính) | Rủi ro người dùng và pháp lý |
| Chọn phe khi hai bên mâu thuẫn | Mất vai trò trung gian |
| Chỉ có một phương án, không có Do Nothing | Business Case thành biện minh |
| KPI mâu thuẫn nhau mà không phát hiện | Tài liệu không đáng tin khi nghiệm thu |
| "Ký trước, sửa sau" mà không ghi điều kiện | Rủi ro hợp đồng |

---

## 5. Cross-check nghĩa giữa FR, US, AC (không chỉ ID)

Scanner kiểm tra ID khớp. Reviewer hoặc LLM-judge kiểm tra thêm nghĩa.

Với mỗi cặp FR → US → AC:

1. **Cùng actor:** FR, US và AC nói về cùng vai trò?
2. **Cùng điều kiện số:** ngưỡng, độ dài, thời gian, số lần thử có trùng giữa ba tài liệu?
3. **AC bao phủ FR:** mỗi hành vi trong FR có kịch bản AC kiểm tra? Hành vi nào chưa có AC?
4. **AC không thêm yêu cầu mới:** kịch bản nào kiểm tra điều FR không yêu cầu? Nếu có, bổ sung FR hoặc bỏ kịch bản.
5. **Business Rule:** BR được enforce trong FR có xuất hiện đúng điều kiện trong kịch bản Negative?
6. **Ngoại lệ:** luồng ngoại lệ trong FR có kịch bản AC tương ứng?
7. **KPI và NFR:** KPI ở BRD có NFR hoặc event đo tương ứng?

Mẫu prompt cho LLM-judge:

```
Bạn là BA Senior. Đọc FR [ID], US [ID], AC [ID] dưới đây.
Trả lời bảng: | Kiểm tra | Đạt/Không | Bằng chứng (trích nguyên văn) | Đề xuất sửa |
cho 7 kiểm tra ở senior-ba-rubric.md mục 5.
Chỉ dùng nội dung được cung cấp. Thiếu thông tin thì ghi [CHƯA CÓ THÔNG TIN].
```

---

## 6. Cách chạy

1. Chọn tình huống trong `tests/golden/senior_judgement_cases.jsonl`.
2. Cho agent trả lời đề bài (`ask`).
3. So với `senior_signals`, `middle_signals`, `red_flags` của tình huống.
4. Chấm 9 chiều, xếp mức theo mục 3.
5. Lưu kết quả vào `tests/golden/senior_runs/` (không commit nếu chứa dữ liệu thật).

Bộ này kiểm tra phán đoán. Việc chấm cuối cùng do người hoặc LLM-judge thực hiện, vì từ khóa không đo được phán đoán.
