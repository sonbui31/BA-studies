# ĐỐI SOÁT YÊU CẦU VS MÃ NGUỒN (Requirement-to-Code Audit 2.6)

> **Mục đích:** Đảm bảo những gì được code (Implementation) khớp chính xác với những gì được yêu cầu (SRS/Stories).
> **Kỹ thuật:** AI Code Analysis + Traceability Mapping.

---

## 1. Quy trình Đối soát (The Alignment Check)

Khi nhận lệnh Audit Code, @ba-specialist thực hiện:

1. **Extraction (Gemini 3 Pro):**
   - Trích xuất danh sách tính năng và tiêu chí chấp nhận (AC) từ SRS/User Story Map.
2. **Analysis (Claude 4.6):**
   - Đọc mã nguồn thực tế (từ thư mục code dự án).
   - Đối soát mapping: Requirement ID ↔ Code Function/Component.
3. **Reasoning (OpenAI o4):**
   - Tìm các logic trong code mâu thuẫn với Business Rules trong SRS.
   - Phát hiện các yêu cầu "đã viết nhưng chưa code" hoặc "code thừa không có trong yêu cầu".
4. **Data Verification (GPT-5):**
   - Kiểm tra các tracking events trong code có khớp với Data Model/Tracking Plan ban đầu hay không.

---

## 2. Các chỉ số Audit (Audit Metrics)

- **Requirement Coverage:** Tỷ lệ % yêu cầu đã được chuyển hóa thành code.
- **Logic Sync Score:** Mức độ đồng nhất về logic nghiệp vụ giữa tài liệu và thực tế.
- **Tracking Accuracy:** Tỷ lệ % các event đo lường được đặt đúng chỗ trong code.

---

## 3. Lệnh kích hoạt

- `@[ba-specialist] hãy đối soát file SRS này với mã nguồn trong thư mục [src]`
- `@[ba-specialist] kiểm tra xem tính năng [X] đã được code đúng theo AC chưa`
- `@[ba-specialist] audit xem có requirement nào trong Story Map bị sót chưa triển khai không`
