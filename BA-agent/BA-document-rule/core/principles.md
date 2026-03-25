# NGUYÊN TẮC & MÔ HÌNH CỐT LÕI CỦA BA 2.1

> **Phiên bản:** 2.1 | **Ngày:** 25/03/2026
> **Đặc điểm:** AI-Augmented (Gemini 3 & Claude 4.6), Data-Driven, Hybrid Agile

---

## 1. BACCM — Business Analysis Core Concept Model
> Mô hình lõi của BABOK® v3. Mọi tài liệu BA phải đảm bảo cover đủ 6 yếu tố.

| # | Core Concept | Câu hỏi chính |
|---|-------------|---------------|
| 1 | **Change** | Tại sao cần thay đổi? Vấn đề/cơ hội gì? |
| 2 | **Need** | Nhu cầu gốc (root need) là gì? |
| 3 | **Solution** | Giải pháp nào đáp ứng need? |
| 4 | **Stakeholder** | Ai bị ảnh hưởng? Ai có quyền quyết định? |
| 5 | **Value** | Giá trị mang lại là gì? Đo lường thế nào? |
| 6 | **Context** | Ràng buộc kỹ thuật, tổ chức, pháp lý? |

---

## 2. BABOK® v3 — 7 Knowledge Areas
1. **BA Planning & Monitoring**
2. **Elicitation & Collaboration**
3. **Requirements Life Cycle Mgmt**
4. **Strategy Analysis**
5. **Requirements Analysis & Design Definition**
6. **Solution Evaluation**
7. **Underlying Competencies**

---

## 3. MoSCoW — Phân loại ưu tiên
- **M (Must):** Bắt buộc, không có không chạy được (~60%)
- **S (Should):** Quan trọng, có workaround (~20%)
- **C (Could):** Nice-to-have, tăng UX (~15%)
- **W (Won't):** Không làm lần này (~5%)

---

## 4. Kano Model — Mức độ hài lòng
- **Basic:** Phải có, thiếu là bực.
- **Performance:** Càng nhiều càng tốt.
- **Excitement:** WOW factor (AI, Innovation).

---

## 5. INVEST — Tiêu chí User Story
- **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable.

---

## 6. Given-When-Then (GWT) — Acceptance Criteria
- **GIVEN** [context] **WHEN** [action] **THEN** [result].

---

## 7. SWOT Analysis
- **Strengths, Weaknesses, Opportunities, Threats**.

---

## 8. Impact Mapping
- **WHY** (Goal) → **WHO** (Actors) → **HOW** (Impacts) → **WHAT** (Deliverables).

---

## 9. 5W1H
- **What, Why, Who, When, Where, How**.

---

## 10. Mười Nguyên tắc vàng của BA Documentation
1. Viết cho người đọc.
2. Một tài liệu, một mục đích.
3. Đủ chi tiết, không thừa.
4. Có thể verify (SMART).
5. Traceability (ID-linked).
6. Version control.
7. Visual first (Mermaid).
8. Review trước khi sign-off.
9. Living document.
10. Template là khởi đầu.

---

## 11. Multi-LLM Orchestration (Gemini 3, Claude 4.6, GPT-5 & o4) — BA 2.2

> Sử dụng sức mạnh tối thượng của các thế hệ LLM mới nhất (Q1/2026) để dẫn đầu trong phân tích nghiệp vụ.

| Mô hình | Điểm mạnh (Best for) | Tác vụ khuyến nghị |
|----------|-------------------|-------------------|
| **Gemini 3 Pro** | **Infinite Context & Strategy:** Xử lý hàng chục triệu tokens, tư duy chiến lược đa lớp. | Phân tích thị trường vĩ mô, Audit toàn bộ project, kết nối insight từ hàng ngàn tài liệu. |
| **Claude 4.6** | **Creative Precision & Artifacts:** Thiết kế UI/UX và logic nghiệp vụ với sự tinh tế và chính xác tuyệt đối. | Chi tiết hóa User Story, vẽ Mermaid phức tạp, thiết kế luồng người dùng (User Journey). |
| **GPT-5** | **General Reasoning & Versatility:** Khả năng suy luận tổng quát và bám sát framework Layered OS cực tốt. | Draft nhanh Vision & Scope, BRD, đề xuất các giải pháp sáng tạo. |
| **OpenAI o4** | **Complex Logic & Edge Cases:** Mô hình chuyên sâu về lý luận (Reasoning) để giải quyết các bài toán hóc búa. | Phân tích các luồng nghiệp vụ lắt léo, giải quyết mâu thuẫn yêu cầu, tìm lỗ hổng logic. |

### Chiến thuật Phối hợp (Orchestration):
1. **Gemini 3 for Architecture:** Xây dựng cấu trúc tổng thể và "bơm" toàn bộ bối cảnh dự án.
2. **OpenAI o4 for Logic Audit:** Dùng o4 để tìm ra các "điểm mù" (blind spots) và mâu thuẫn trong yêu cầu nghiệp vụ.
3. **Claude 4.6 for Visuals:** Trực quan hóa mọi thứ bằng Mermaid và Prototyping.
4. **Cross-Validation:** Dùng Gemini 3 để tổng hợp và kiểm tra chéo độ nhất quán cuối cùng.

---

## 12. Data-Driven Business Analysis — BA 2.0
- **Success Metrics (OKRs):** Đo lường giá trị thực tế.
- **Tracking Plan:** Track event ngay từ khâu thiết kế.
- **Data Storytelling:** Dùng dữ liệu để thuyết phục Stakeholder.

---

## 13. Mười Nguyên tắc vàng của BA 2.0
1. AI as a Partner.
2. Data-Informed Decisions.
3. Speed to Value.
4. Agile Documentation.
5. Visual Thinking.
6. Empathy & UX.
7. Traceability 2.0.
8. Feedback Loop.
9. Continuous Learning.
10. Ethical AI.
