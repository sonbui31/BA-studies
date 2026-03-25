# NGUYÊN TẮC & MÔ HÌNH CỐT LÕI CỦA BA 2.2

> **Phiên bản:** 2.2 | **Ngày:** 25/03/2026
> **Đặc điểm:** Multi-LLM Orchestrated (Gemini 3, Claude 4.6, GPT-5 & o4), Data-Driven, Hybrid Agile

---

## 1. BACCM — Business Analysis Core Concept Model

> Mô hình lõi của BABOK® v3. Mọi tài liệu BA phải đảm bảo cover đủ 6 yếu tố.

| # | Core Concept | Câu hỏi chính | Ví dụ (E-commerce) |
|---|-------------|---------------|---------------------|
| 1 | **Change** | Tại sao cần thay đổi? Vấn đề/cơ hội gì? | Quy trình đặt hàng thủ công mất 15 phút |
| 2 | **Need** | Nhu cầu gốc (root need) là gì? | Đặt hàng < 3 phút, tự động xác nhận |
| 3 | **Solution** | Giải pháp nào đáp ứng need? | Hệ thống đặt hàng online tự động |
| 4 | **Stakeholder** | Ai bị ảnh hưởng? Ai có quyền quyết định? | Khách hàng, NV bán hàng, Quản lý |
| 5 | **Value** | Giá trị mang lại là gì? Đo lường thế nào? | Giảm 80% thời gian xử lý, tăng 30% đơn hàng |
| 6 | **Context** | Ràng buộc kỹ thuật, tổ chức, pháp lý? | Tích hợp ERP hiện tại, tuân thủ PDPA |

---

## 2. BABOK® v3 — 7 Knowledge Areas

1. **BA Planning & Monitoring** — Lập kế hoạch và giám sát hoạt động BA
2. **Elicitation & Collaboration** — Thu thập và cộng tác với Stakeholder
3. **Requirements Life Cycle Mgmt** — Quản lý vòng đời yêu cầu
4. **Strategy Analysis** — Phân tích chiến lược kinh doanh
5. **Requirements Analysis & Design Definition** — Phân tích và thiết kế giải pháp
6. **Solution Evaluation** — Đánh giá giải pháp sau triển khai
7. **Underlying Competencies** — Năng lực nền tảng (giao tiếp, tư duy, lãnh đạo)

---

## 3. MoSCoW — Phân loại ưu tiên

| Mức | Ý nghĩa | Tỷ lệ khuyến nghị | Ví dụ |
|-----|---------|-------------------|-------|
| **M (Must)** | Bắt buộc, không có không chạy được | ~60% | Đăng nhập, Đặt hàng |
| **S (Should)** | Quan trọng, có workaround | ~20% | Lọc sản phẩm nâng cao |
| **C (Could)** | Nice-to-have, tăng UX | ~15% | Dark mode |
| **W (Won't)** | Không làm lần này | ~5% | Chatbot AI |

---

## 4. Kano Model — Mức độ hài lòng

| Loại | Đặc điểm | Chiến lược | Ví dụ |
|------|---------|-----------|-------|
| **Basic** | Phải có, thiếu là bực | Đảm bảo 100% | Trang thanh toán hoạt động |
| **Performance** | Càng nhiều càng tốt | Tối ưu liên tục | Tốc độ load trang |
| **Excitement** | WOW factor, không mong đợi | Đầu tư sáng tạo | Gợi ý sản phẩm bằng AI |

---

## 5. INVEST — Tiêu chí User Story

| Chữ | Tiêu chí | Câu hỏi kiểm tra |
|-----|---------|-------------------|
| **I** | Independent | Story này có phụ thuộc story khác không? |
| **N** | Negotiable | Có thể thương lượng cách làm không? |
| **V** | Valuable | Mang lại giá trị gì cho user/business? |
| **E** | Estimable | Team có thể ước lượng effort không? |
| **S** | Small | Có hoàn thành trong 1 sprint không? |
| **T** | Testable | Viết được Acceptance Criteria không? |

---

## 6. Given-When-Then (GWT) — Acceptance Criteria

```
GIVEN  [bối cảnh ban đầu — precondition]
WHEN   [hành động của user — trigger]
THEN   [kết quả mong đợi — expected outcome]
```

**Ví dụ:**
```
GIVEN  Khách hàng đã đăng nhập và có sản phẩm trong giỏ
WHEN   Khách nhấn "Đặt hàng" và thanh toán thành công
THEN   Hệ thống tạo đơn status=CONFIRMED, gửi email xác nhận, trừ tồn kho
```

---

## 7. SWOT Analysis — Phân tích chiến lược

> Dùng trong BRD, Vision & Scope để đánh giá tính khả thi.

```
         Tích cực (+)              Tiêu cực (-)
       ┌──────────────┐         ┌──────────────┐
 Nội   │  STRENGTHS   │         │  WEAKNESSES  │
 bộ    │  Điểm mạnh   │         │  Điểm yếu    │
       │  nội tại     │         │  nội tại     │
       └──────────────┘         └──────────────┘
       ┌──────────────┐         ┌──────────────┐
 Bên   │ OPPORTUNITIES│         │   THREATS    │
 ngoài │  Cơ hội      │         │  Nguy cơ     │
       │  từ thị trường│        │  từ bên ngoài│
       └──────────────┘         └──────────────┘
```

---

## 8. Impact Mapping — Từ mục tiêu → tính năng

> Dùng trong Vision & Scope để connect business goal → features.

```
WHY?           WHO?          HOW?           WHAT?
(Goal)    →  (Actors)   →  (Impacts)   →  (Deliverables)
─────────    ─────────    ───────────    ──────────────
Tăng         Khách hàng   Mua nhanh     One-click order
doanh thu    ─────────    hơn           Auto-fill address
20%          NV bán hàng  ───────────    ──────────────
             ─────────    Upsell        Recommend engine
             Marketing    hiệu quả     Bundle deals
```

**Quy tắc:**
1. Bắt đầu từ **WHY** (business goal) — không phải feature
2. Mỗi Impact phải **đo lường được** (metric)
3. Feature chỉ có giá trị khi connect được về Goal

---

## 9. 5W1H — Khung phân tích toàn diện

| Câu hỏi | Ý nghĩa | Ví dụ |
|---------|---------|-------|
| **What** | Làm gì? | Hệ thống quản lý đơn hàng trực tuyến |
| **Why** | Tại sao cần? | Giảm 50% thời gian xử lý đơn hàng thủ công |
| **Who** | Ai sử dụng? Ai quyết định? | Khách hàng, NV bán hàng, Quản lý |
| **When** | Khi nào cần? Deadline? | Go-live trước Q3/2026 |
| **Where** | Ở đâu? Platform? | Web + Mobile App, thị trường VN |
| **How** | Thực hiện như thế nào? | Agile, 6 sprints, team 5 người |

---

## 10. Mười Nguyên tắc vàng của BA Documentation

1. **Viết cho người đọc, không phải người viết** — Dev đọc SRS, Sponsor đọc BRD → ngôn ngữ khác nhau
2. **Một tài liệu, một mục đích** — BRD ≠ SRS. Không gộp
3. **Đủ chi tiết, không thừa** — viết đủ để người đọc hành động được, không viết tiểu thuyết
4. **Có thể verify** — mọi requirement phải testable ("Hệ thống nhanh" ❌ → "Load < 3s" ✅)
5. **Traceability** — mỗi requirement có ID, link được từ BRD → SRS → Story → Test Case
6. **Version control** — mọi thay đổi phải tracked, không edit trực tiếp bản đã sign-off
7. **Visual first** — 1 sơ đồ tốt hơn 1000 chữ. Luôn kèm diagram
8. **Review trước khi sign-off** — ít nhất 2 người review (BA + Dev/QC)
9. **Living document** — tài liệu sống, cập nhật liên tục trong Delivery
10. **Template là khởi đầu, không phải kết thúc** — fill template xong mới là bắt đầu tư duy

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

### ⚠️ Quy tắc Vàng AI-BA:
1. **AI draft, BA review:** Không bao giờ copy-paste output của AI mà không kiểm chứng.
2. **Security first:** Tuyệt đối không đưa dữ liệu nhạy cảm của khách hàng (PII, NDA) lên các mô hình AI công cộng.
3. **Context is King:** Cung cấp đầy đủ bối cảnh (Business Goal, Tech Stack) để AI cho kết quả tốt nhất.

---

## 12. Data-Driven Business Analysis — BA 2.2

> BA không chỉ "nghe" stakeholder nói, mà phải "nhìn" vào dữ liệu để ra quyết định.

### Bộ chỉ số thành công (Success Metrics)
Mọi giải pháp (Solution) phải đi kèm với cách đo lường giá trị (Value):
- **North Star Metric:** Chỉ số quan trọng nhất (ví dụ: Churn Rate, Conversion Rate).
- **Lỗ hổng Dữ liệu (Tracking Plan):** Xác định các event cần track ngay trong pha thiết kế.

### Kỹ năng Data cho BA:
1. **Trực quan hóa:** Chọn đúng biểu đồ (Trend, Distribution, Comparison) để kể chuyện (Data Storytelling).
2. **Cấu trúc Dữ liệu:** Thiết kế ERD không chỉ cho lưu trữ mà còn cho phân tích (OLTP vs OLAP).
3. **A/B Testing:** Thiết kế các thí nghiệm để chọn ra giải pháp tối ưu dựa trên click-through-rate.

---

## 13. Mười Nguyên tắc vàng của BA 2.2

1. **AI as a Partner** — Co-creation thay vì manual creation.
2. **Data-Informed Decisions** — Kết hợp trực giác kinh doanh và bằng chứng dữ liệu.
3. **Speed to Value** — Ưu tiên bản draft nhanh (MVP Docs) để sớm nhận feedback.
4. **Agile Documentation** — Tài liệu gọn nhẹ, cập nhật liên tục, không viết "chết".
5. **Visual Thinking** — Ưu tiên hình ảnh và sơ đồ hơn văn bản thuần túy.
6. **Empathy & UX** — Luôn đặt mình vào vị trí user cuối cùng.
7. **Traceability 2.0** — Link từ OKR đến từng dòng code thông qua ID.
8. **Feedback Loop** — Xây dựng cơ chế lấy feedback tự động sau mỗi tính năng.
9. **Continuous Learning** — Cập nhật công nghệ và mô hình kinh doanh mới hàng tháng.
10. **Ethical AI** — Đảm bảo tính minh bạch và đạo đức khi áp dụng AI.
