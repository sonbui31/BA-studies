# GIAO THỨC MÔ PHỎNG PERSONA (Stakeholder Simulation 2.5)

> **Mục đích:** "Stress-test" yêu cầu nghiệp vụ thông qua góc nhìn của các Stakeholder khác nhau trước khi trình bày thực tế.
> **Công nghệ:** Sử dụng Multi-LLM Roleplay (o4 cho Logic, Claude cho Empathy).

---

## 1. Danh sách Persona AI mẫu

| Persona | Vai trò | Trọng tâm Audit | "Tính cách" AI |
|---|---|---|---|
| **Skeptic CFO** | Giám đốc tài chính | ROI, Chi phí, Rủi ro tài chính, Giá trị kinh doanh. | Khắt khe, thực tế, luôn hỏi "Tiền ở đâu?". |
| **Grumpy Architect** | Kiến trúc sư trưởng | Độ phức tạp, Tech Debt, Khả năng mở rộng, Bảo mật. | Thẳng thắn, lo ngại rủi ro kỹ thuật. |
| **Lazy End-User** | Người dùng cuối | Usability, UX, Số bước thực hiện, Độ đơn giản. | Dễ nản lòng, muốn mọi thứ nhanh và rõ. |
| **Rigid Compliance** | Chuyên gia pháp chế | Quy định bảo mật, PDPA/GDPR, Tính hợp pháp. | Cẩn thận, chi tiết, bám sát luật. |

---

## 2. Quy trình Mô phỏng (The Gauntlet)

1. **Input:** Cung cấp tài liệu (BRD/SRS) cần test.
2. **Interaction:**
   - @ba-specialist kích hoạt một hoặc nhiều Persona.
   - Persona sẽ đặt câu hỏi hóc búa hoặc chỉ ra điểm yếu trong giải pháp.
3. **Rebuttal:** BA (User) trả lời hoặc điều chỉnh tài liệu.
4. **Final Verdict:** Persona đưa ra đánh giá "Phê duyệt" hoặc "Cần sửa đổi".

---

## 3. Lệnh kích hoạt

- `@[ba-specialist] hãy đóng vai CFO để phản biện tính năng này`
- `@[ba-specialist] hãy dùng Technical Lead mode để tìm rủi ro triển khai cho SRS này`
- `@[ba-specialist] mô phỏng buổi họp Stakeholder bao gồm CFO, Dev Lead và End-user để audit BRD`
