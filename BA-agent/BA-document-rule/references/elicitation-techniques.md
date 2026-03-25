# KỸ THUẬT THU THẬP YÊU CẦU (Elicitation Techniques)

> **BABOK KA:** Elicitation & Collaboration
> **Mục đích:** Chọn đúng kỹ thuật cho đúng tình huống

---

## 1. Ma trận chọn kỹ thuật

| Kỹ thuật | Khi nào dùng | Stakeholder | Output | Effort |
|---------|-------------|-----------|--------|--------|
| **Phỏng vấn 1:1** | Cần hiểu sâu quan điểm cá nhân | SME, Manager | Meeting Notes, Req list | Thấp |
| **Workshop nhóm** | Cần đồng thuận nhiều bên | 5-10 người | User Story Map, Process Flow | Trung bình |
| **Quan sát (Shadowing)** | Hiểu quy trình thực tế vs quy trình giấy | End-user | As-Is Process Flow | Trung bình |
| **Khảo sát (Survey)** | Thu thập ý kiến số đông | Nhiều users | Dữ liệu định lượng | Thấp |
| **Phân tích tài liệu** | Hiện có quy trình / hệ thống cũ | — | Gap Analysis | Thấp |
| **Prototype / Mockup** | Validate UI/UX sớm | End-user, PO | Wireframe + Feedback | Trung bình |
| **Brainstorming** | Cần ý tưởng sáng tạo | Team đa năng | Idea List | Thấp |
| **Focus Group** | Cần phản hồi từ nhóm đại diện | End-users | Insights, Pain points | Trung bình |
| **Reverse Engineering** | Xây dựng lại từ hệ thống cũ | — | FR list, Data Model | Cao |
| **Job Shadowing** | Hiểu workflow thực tế | End-user | As-Is Process, Pain points | Cao |

---

## 2. Chi tiết từng kỹ thuật

### 2.1 Phỏng vấn 1:1 (Interview)

**Chuẩn bị:**
- Danh sách câu hỏi (5W1H framework)
- Ghi âm / ghi chép (xin phép trước)
- 30-60 phút / session

**Câu hỏi mẫu theo 5W1H:**
```
WHAT: "Anh/chị mô tả quy trình hiện tại đang làm thế nào?"
WHY:  "Tại sao bước này cần thiết? Nếu bỏ thì sao?"
WHO:  "Ai tham gia vào bước này? Ai phê duyệt?"
WHEN: "Bước này xảy ra khi nào? Tần suất?"
WHERE:"Dữ liệu lấy từ đâu? Kết quả gửi đi đâu?"
HOW:  "Nếu gặp lỗi ở bước này thì xử lý thế nào?"
```

**Kỹ thuật phỏng vấn hiệu quả:**
- **Open-ended first:** "Hãy kể cho tôi về..." → sau đó mới hỏi cụ thể
- **5 Whys:** Hỏi "Tại sao?" 5 lần liên tiếp để tìm root cause
- **Negative path:** "Nếu [tình huống xấu] thì sao?"
- **Paraphrase:** "Nếu tôi hiểu đúng thì..." → xác nhận lại

### 2.2 Workshop nhóm

**Chuẩn bị:**
- Agenda rõ ràng, gửi trước 2-3 ngày
- Facilitator (BA) + Note-taker
- Công cụ: Miro (remote) / Whiteboard (offline)
- 2-4 giờ / session

**Structure:**
```
1. Warm-up (10 min)         — Giới thiệu, mục tiêu
2. As-Is walkthrough (30 min) — Mô tả quy trình hiện tại
3. Pain points (20 min)      — Sticky notes: 1 vấn đề / 1 note
4. To-Be ideation (40 min)   — Brainstorm giải pháp
5. Prioritize (20 min)       — MoSCoW voting
6. Wrap-up (10 min)          — Action items, next steps
```

### 2.3 Prototype / Mockup

**Mức độ chi tiết:**

| Level | Mô tả | Công cụ | Khi nào |
|-------|-------|---------|---------|
| **Lo-fi** | Sketch trên giấy / whiteboard | Giấy, Balsamiq | Discovery sớm |
| **Mid-fi** | Wireframe có layout, navigation | Figma, Draw.io | Discovery → Elaboration |
| **Hi-fi** | Mockup full design, clickable | Figma (interactive) | Trước development |

---

## 3. Mapping: Phase → Kỹ thuật phù hợp

| Phase | Kỹ thuật chính | Kỹ thuật bổ trợ |
|-------|---------------|----------------|
| **Inception** | Phỏng vấn 1:1, Phân tích tài liệu | Brainstorming |
| **Discovery** | Workshop, Quan sát, Prototype | Survey, Focus Group |
| **Elaboration** | Prototype (hi-fi), Review session | Reverse Engineering |
| **Delivery** | Sprint Review (feedback), Clarification | — |
| **Closure** | UAT feedback, Lessons Learned workshop | — |
