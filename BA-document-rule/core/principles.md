# NGUYÊN TẮC & MÔ HÌNH CỐT LÕI CỦA BA

> **Mục đích:** Kim chỉ nam cho mọi hoạt động Business Analysis
> **Áp dụng:** Mọi tài liệu, mọi dự án, mọi phase

---

## 1. BACCM — Business Analysis Core Concept Model

> Mô hình lõi của BABOK® v3. **Mọi tài liệu BA phải đảm bảo cover đủ 6 yếu tố.**

```
                    ┌─────────────┐
                    │   CHANGE    │
                    │ Tại sao cần │
                    │  thay đổi?  │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
        ┌─────▼─────┐ ┌───▼───┐ ┌─────▼─────┐
        │   NEED    │ │ VALUE │ │ CONTEXT   │
        │ Nhu cầu   │ │ Giá   │ │ Bối cảnh  │
        │  thực sự  │ │ trị   │ │ tổ chức   │
        └─────┬─────┘ └───┬───┘ └─────┬─────┘
              │            │            │
              └────────────┼────────────┘
                           │
              ┌────────────┼────────────┐
              │                         │
        ┌─────▼──────┐          ┌──────▼──────┐
        │ STAKEHOLDER│          │  SOLUTION   │
        │ Ai liên    │          │ Giải pháp   │
        │  quan?     │          │  đáp ứng?   │
        └────────────┘          └─────────────┘
```

### 6 Khái niệm lõi

| # | Core Concept | Câu hỏi chính | Áp dụng vào tài liệu |
|---|-------------|---------------|----------------------|
| 1 | **Change** | Tại sao cần thay đổi? Vấn đề/cơ hội gì? | Vision & Scope, BRD |
| 2 | **Need** | Nhu cầu gốc (root need) là gì? | BRD, User Story Map |
| 3 | **Solution** | Giải pháp nào đáp ứng need? | SRS, Data Model, API Spec |
| 4 | **Stakeholder** | Ai bị ảnh hưởng? Ai có quyền quyết định? | Stakeholder Map |
| 5 | **Value** | Giá trị mang lại là gì? Đo lường thế nào? | BRD (ROI), UAT |
| 6 | **Context** | Ràng buộc kỹ thuật, tổ chức, pháp lý? | Vision & Scope, SRS (NFR) |

### ✅ BACCM Checklist — Dùng khi review BẤT KỲ tài liệu BA nào

```
☐ CHANGE:      Đã nêu rõ lý do thay đổi / vấn đề cần giải quyết?
☐ NEED:        Nhu cầu gốc (root need) đã được xác định, không chỉ symptom?
☐ SOLUTION:    Giải pháp đã align với need (không over-engineer)?
☐ STAKEHOLDER: Đã map đầy đủ người liên quan + quyền quyết định?
☐ VALUE:       Giá trị kinh doanh đã được lượng hóa (KPI / metric)?
☐ CONTEXT:     Ràng buộc kỹ thuật / tổ chức / pháp lý đã ghi nhận?
```

---

## 2. BABOK® v3 — 7 Knowledge Areas

> **BABOK** (Business Analysis Body of Knowledge) là tiêu chuẩn quốc tế của IIBA.

| # | Knowledge Area | Mô tả | Phase chính |
|---|---------------|-------|-------------|
| 1 | **BA Planning & Monitoring** | Lập kế hoạch BA, xác định cách tiếp cận | Inception |
| 2 | **Elicitation & Collaboration** | Thu thập yêu cầu, hợp tác stakeholder | Inception, Discovery |
| 3 | **Requirements Life Cycle Mgmt** | Quản lý vòng đời yêu cầu, traceability | Elaboration, Delivery |
| 4 | **Strategy Analysis** | Phân tích chiến lược, current/future state | Inception, Discovery |
| 5 | **Requirements Analysis & Design Definition** | Phân tích, mô hình hóa, thiết kế giải pháp | Discovery, Elaboration |
| 6 | **Solution Evaluation** | Đánh giá giải pháp, UAT, acceptance | Closure |
| 7 | **Underlying Competencies** | Kỹ năng nền tảng: tư duy, giao tiếp, lãnh đạo | Xuyên suốt |

---

## 3. MoSCoW — Phương pháp phân loại ưu tiên

> Dùng khi phân loại yêu cầu trong BRD, User Story Map.

| Ký hiệu | Tên | Ý nghĩa | Tỷ lệ khuyến nghị |
|---------|-----|---------|-------------------|
| **M** | Must Have | Bắt buộc — không có thì hệ thống **không dùng được** | ~60% |
| **S** | Should Have | Nên có — quan trọng nhưng có workaround | ~20% |
| **C** | Could Have | Có thì tốt — nice-to-have, cải thiện UX | ~15% |
| **W** | Won't Have (this time) | Không làm lần này — ghi nhận cho phase sau | ~5% |

### Quy tắc áp dụng

1. **Phân loại từ trên xuống:** Hỏi "Nếu bỏ feature này, hệ thống còn dùng được không?"
   - Không → **Must**
   - Có, nhưng khó chịu → **Should**
   - Có, không ảnh hưởng lớn → **Could**
2. **Must Have không quá 60%** — nếu quá → phạm vi quá lớn hoặc chưa phân tích kỹ
3. **Won't Have ≠ Rejected** — chỉ là "không trong scope lần này"
4. **Review lại MoSCoW ĐẦU MỖI SPRINT** — ưu tiên có thể thay đổi

---

## 4. Kano Model — Phân tích mức hài lòng

> Dùng khi đánh giá tính năng nào nên ưu tiên phát triển.

```
Hài lòng ▲
         │         ╱ Excitement (Delighters)
         │       ╱     → Không mong đợi nhưng "WOW"
         │     ╱       → Ví dụ: AI gợi ý sản phẩm
         │   ╱
         │──────────── Performance (Linear)
         │              → Càng nhiều càng hài lòng
         │              → Ví dụ: Tốc độ load trang
         │
─────────┼─────────────────────────▶ Mức thực hiện
         │
         │  ────────── Basic (Must-be)
         │              → Không có = RẤT BỰC
         │              → Có rồi = bình thường
         │              → Ví dụ: Đăng nhập, Bảo mật
Bực bội  ▼
```

| Loại | Có | Không có | Ví dụ | Chiến lược |
|------|-----|---------|-------|-----------|
| **Basic** | Bình thường | Rất bực bội | Login, Security | Đảm bảo 100%, không quảng cáo |
| **Performance** | Hài lòng tỷ lệ thuận | Bực bội tỷ lệ thuận | Tốc độ, Dung lượng | Tối ưu liên tục |
| **Excitement** | WOW | Không ảnh hưởng | AI suggest, Dark mode | Đầu tư có chọn lọc |
| **Indifferent** | Không care | Không care | Thay đổi icon nhỏ | Bỏ qua, tiết kiệm effort |

### Kano + MoSCoW Mapping

| Kano | MoSCoW thường gặp |
|------|-------------------|
| Basic | **Must Have** |
| Performance | **Should Have** |
| Excitement | **Could Have** |
| Indifferent | **Won't Have** |

---

## 5. INVEST — Tiêu chí viết User Story

> Mỗi User Story phải đạt 6 tiêu chí INVEST.

| Ký tự | Tiêu chí | Câu hỏi kiểm tra | ❌ Vi phạm |
|-------|----------|-------------------|-----------|
| **I** | Independent | Story này có phụ thuộc story khác không? | Story A phải xong trước B |
| **N** | Negotiable | Chi tiết có thể thảo luận được không? | Đặc tả cứng nhắc từng pixel |
| **V** | Valuable | Mang lại giá trị cho user/business không? | "Refactor database" (kỹ thuật thuần) |
| **E** | Estimable | Team có thể ước lượng được không? | "Tích hợp AI" (quá mơ hồ) |
| **S** | Small | Hoàn thành trong 1 Sprint không? | Epic 3 tháng |
| **T** | Testable | Viết được Acceptance Criteria không? | "Hệ thống nhanh" (không đo được) |

---

## 6. Given-When-Then — Viết Acceptance Criteria

> Chuẩn BDD (Behavior-Driven Development) cho Acceptance Criteria.

### Format

```
GIVEN  [bối cảnh / điều kiện tiên quyết]
WHEN   [hành động của user / sự kiện xảy ra]
THEN   [kết quả mong đợi / hệ thống phản hồi]
```

### Ví dụ

```
Feature: Đặt hàng

Scenario: Đặt hàng thành công
  GIVEN  Khách hàng đã đăng nhập và có sản phẩm trong giỏ hàng
  WHEN   Khách nhấn "Đặt hàng" và thanh toán thành công
  THEN   Hệ thống tạo đơn hàng status = CONFIRMED
  AND    Gửi email xác nhận cho khách hàng
  AND    Trừ tồn kho tương ứng

Scenario: Đặt hàng thất bại — hết hàng
  GIVEN  Khách hàng đã đăng nhập và có sản phẩm trong giỏ hàng
  WHEN   Khách nhấn "Đặt hàng" nhưng sản phẩm đã hết hàng
  THEN   Hệ thống hiển thị thông báo "Sản phẩm đã hết hàng"
  AND    Không tạo đơn hàng
  AND    Đề xuất sản phẩm tương tự
```

### Quy tắc

1. **Mỗi Scenario = 1 hành vi cụ thể** — không gộp nhiều case
2. **GIVEN phải đủ context** — ai, ở đâu, điều kiện gì
3. **THEN phải đo lường được** — "hiển thị thông báo X", không phải "thông báo phù hợp"
4. **Luôn viết cả Happy Path + Unhappy Path**

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
                          ───────────    ──────────────
                          Quay lại      Loyalty program
                          thường xuyên  Push notification
```

**Quy tắc:**
1. Bắt đầu từ **WHY** (business goal) — không phải feature
2. Mỗi Impact phải **đo lường được** (metric)
3. Feature chỉ có giá trị khi connect được về Goal

---

## 9. 5W1H — Khung thu thập yêu cầu

> Dùng khi phỏng vấn, workshop, hoặc phân tích yêu cầu.

| Câu hỏi | Ý nghĩa | Ví dụ |
|---------|---------|-------|
| **What** | Cần làm gì? | Xây dựng hệ thống đặt hàng online |
| **Why** | Tại sao cần? | Giảm 50% thời gian xử lý đơn hằng thủ công |
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
