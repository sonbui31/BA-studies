# CUSTOMER INTELLIGENCE — Kỹ năng Khai thác & Phân tích Thông tin Khách hàng

> **BABOK KA:** Elicitation & Collaboration (Nâng cao)
> **Mục đích:** Biến BA thành "thám tử thông tin" — trao đổi, thu thập, moi móc & phân tích mọi insight từ khách hàng
> **Level:** Advanced | **Cập nhật:** 03/2026

---

## 1. Năm Nguyên tắc Vàng (Golden Rules)

| # | Nguyên tắc | Giải thích | Anti-pattern |
|---|-----------|-----------|-------------|
| 1 | **Nghe 80% — Nói 20%** | KH nói càng nhiều = càng nhiều data. BA là người dẫn dắt, không phải người giảng | ❌ BA nói nhiều hơn KH |
| 2 | **Hỏi "Tại sao" trước "Cái gì"** | Hiểu động cơ → mới hiểu đúng yêu cầu | ❌ Nhảy vào giải pháp ngay |
| 3 | **Không bao giờ giả định** | Mọi thông tin phải được confirm bằng dẫn chứng | ❌ "Chắc KH muốn thế này" |
| 4 | **Tạo không gian an toàn** | KH phải thoải mái nói thật — kể cả nói xấu quy trình cũ | ❌ Phán xét ý kiến KH |
| 5 | **Ghi chép real-time, confirm ngay** | Paraphrase & xác nhận tại chỗ, không chờ về mới viết | ❌ "Để về tôi nhớ lại" |

---

## 2. Ma trận Stakeholder Intelligence

> **Mục đích:** Phân loại KH/Stakeholder để chọn chiến lược tiếp cận tối ưu

```
              ẢNH HƯỞNG CAO
                    │
   ┌────────────────┼────────────────┐
   │                │                │
   │  🔴 MANAGE     │  🟢 PARTNER   │
   │  CLOSELY       │  DEEPLY       │
   │  (C-level,     │  (PO, Key     │
   │   Sponsor)     │   User, SME)  │
   │                │                │
HT ├────────────────┼────────────────┤ HT
ÍT │                │                │ NHIỀU
   │  ⚪ MONITOR    │  🔵 KEEP      │
   │  (Observe)     │  INFORMED     │
   │  (IT ops,      │  (End-users,  │
   │   Support)     │   Dept heads) │
   │                │                │
   └────────────────┼────────────────┘
                    │
              ẢNH HƯỞNG THẤP
```

### Chiến lược theo ô

| Ô | Chiến lược | Tần suất | Kỹ thuật ưu tiên |
|---|-----------|---------|-----------------|
| 🟢 **Partner** | Deep interview, collaborative workshop | Hàng tuần | Probing Level 4-6, Empathy Map |
| 🔴 **Manage** | Executive briefing, approval gates | Khi cần sign-off | Elevator pitch, Impact framing |
| 🔵 **Informed** | Newsletter, demo, survey | 2 tuần/lần | Survey, Focus group |
| ⚪ **Monitor** | Passive observation | Khi cần | Document review |

---

## 3. Kỹ thuật Probing — 6 Cấp độ hỏi sâu

> **Nguyên tắc:** Bắt đầu từ Surface → đi sâu dần → đào ra hidden needs

### Level 1 — Surface (Bề mặt)
**Mục đích:** Hiểu bối cảnh chung

```
"Anh/chị có thể kể cho tôi về quy trình hiện tại của bộ phận?"
"Hệ thống đang dùng là gì? Dùng từ khi nào?"
"Mỗi ngày anh/chị xử lý khoảng bao nhiêu [đơn/ticket/request]?"
```

### Level 2 — Problem (Vấn đề)
**Mục đích:** Tìm pain points

```
"Bước nào trong quy trình khiến anh/chị mất thời gian NHẤT?"
"Lần cuối cùng anh/chị gặp SỰ CỐ với hệ thống là khi nào? Chuyện gì xảy ra?"
"Nếu có thể thay đổi MỘT THỨ DUY NHẤT, anh/chị sẽ thay đổi gì?"
```

### Level 3 — Impact (Hệ quả)
**Mục đích:** Lượng hóa thiệt hại / cơ hội

```
"Vấn đề đó gây mất bao nhiêu THỜI GIÓ mỗi tuần?"
"Đã bao giờ vấn đề này khiến MẤT KHÁCH / MẤT TIỀN chưa?"
"Nếu không giải quyết, 6 tháng nữa tình hình sẽ ra sao?"
```

### Level 4 — Root Cause (Nguyên nhân gốc)
**Mục đích:** Tìm "bệnh" thay vì chỉ thấy "triệu chứng"

```
"Tại sao bước này lại phải làm thủ công?" → Trả lời → "Tại sao lại thế?" (5 Whys)
"Vấn đề này bắt đầu từ KHI NÀO? Trước đó có hoạt động bình thường không?"
"Ai là người ĐẦU TIÊN phát hiện vấn đề? Và họ xử lý thế nào?"
```

### Level 5 — Hidden Need (Nhu cầu ẩn)
**Mục đích:** Tìm điều KH cần nhưng CHƯA biết cách diễn đạt

```
"Ngoài vấn đề anh/chị nói, có điều gì anh/chị MUỐN nhưng nghĩ là KHÔNG KHẢ THI không?"
"Nếu hệ thống mới có thể làm BẤT CỨ ĐIỀU GÌ — không giới hạn — anh/chị muốn gì?"
"Đối thủ / bên đối tác của anh/chị đang làm gì mà anh/chị thấy HAY?"
```

### Level 6 — Vision (Tầm nhìn)
**Mục đích:** Align tầm nhìn dài hạn

```
"3 năm nữa, anh/chị hình dung bộ phận mình hoạt động ra sao?"
"Nếu dự án này THÀNH CÔNG HOÀN HẢO, anh/chị sẽ khoe gì với sếp?"
"Metric nào chứng minh dự án này ĐÃ THÀNH CÔNG?"
```

---

## 4. Kỹ thuật "Moi" Thông tin Ẩn

> **Cảnh báo:** Dùng với thiện chí — mục tiêu là giúp KH diễn đạt đúng nhu cầu, KHÔNG phải thao túng.

### 4.1 Reverse Questioning (Hỏi ngược)

**Nguyên lý:** Hỏi về điều NGƯỢC LẠI để KH tự khám phá nhu cầu thật

```
Thay vì: "Anh cần tính năng gì?"
Hỏi:     "Nếu BỎ tính năng X đi, anh/chị có chấp nhận được không?"

Thay vì: "Quy trình nào cần tự động?"
Hỏi:     "Bước nào mà NẾU TẮT HỆ THỐNG thì anh/chị vẫn làm được?"
→ Bước nào KHÔNG thể làm = bước cần ưu tiên automation
```

### 4.2 Scenario-Based Extraction (Kịch bản giả định)

**Nguyên lý:** Đặt KH vào tình huống cụ thể để lộ edge cases

```
HAPPY PATH:
"Hãy walk me through: sáng thứ 2, anh/chị mở máy tính lên và làm gì ĐẦU TIÊN?"

EDGE CASE:
"Giả sử đang xử lý đơn hàng thì MẤT MẠNG. Anh/chị xử lý thế nào?"
"Nếu 1 nhân viên NGHỈ VIỆC đột ngột, ai tiếp quản công việc? Có tài liệu bàn giao?"

STRESS TEST:
"Nếu số lượng đơn tăng GẤP 10 LẦN trong Black Friday, hệ thống hiện tại chịu được không?"
"Nếu sếp yêu cầu báo cáo NGAY TRONG 5 PHÚT, anh/chị lấy data từ đâu?"
```

### 4.3 Pain Amplification (Khuếch đại vấn đề)

**Nguyên lý:** Giúp KH nhận ra mức độ nghiêm trọng thật sự (để họ ưu tiên đúng)

```
KH: "Quy trình hơi chậm"
BA: "Chậm là bao lâu? 10 phút hay 2 giờ?"
BA: "Mỗi ngày xử lý bao nhiêu? → Nhân lên = bao nhiêu giờ/tháng?"
BA: "Nếu quy giờ đó thành TIỀN LƯƠNG, con số là bao nhiêu?"
→ KH tự nhận ra: "À, mất 500 giờ/tháng = 50 triệu tiền lương!"
```

### 4.4 Comparative Extraction (So sánh để lộ)

**Nguyên lý:** So sánh với thực tế khác để KH tự đánh giá

```
"Hệ thống CŨ so với hiện tại — cái nào TỐT HƠN ở điểm nào?"
"Bộ phận bên kia dùng [tool X], anh/chị nghĩ gì về cách họ làm?"
"Nếu so với CHUẨN NGÀNH, quy trình anh/chị đang ở đâu: 3/10 hay 8/10?"
```

---

## 5. Đọc vị & Phân tích Tâm lý Stakeholder

### 5.1 Tín hiệu hành vi (Online & Offline)

| Tín hiệu | Ý nghĩa | Hành động của BA |
|----------|---------|-----------------|
| Trả lời nhanh, ngắn gọn | Có thể đang bận HOẶC tránh né | Hỏi: "Anh/chị muốn hẹn lịch khác?" |
| Liên tục nhắc giải pháp cụ thể | KH đã có ý tưởng sẵn (bias) | Hỏi: "Tại sao anh/chị thấy cách đó tốt?" → tìm need thực |
| Im lặng khi hỏi về lỗi/sự cố | Sợ bị đổ lỗi / xấu hổ | Normalize: "Hệ thống nào cũng có lỗi, mình cần hiểu để cải thiện" |
| Nói "mọi thứ đều ổn" | Chưa tin BA hoặc chưa thấy vấn đề | Dùng Scenario-Based: "Nếu X xảy ra thì sao?" |
| Hay thay đổi ý kiến | Chưa rõ ràng nhu cầu / bị áp lực nội bộ | Pin down: "Lần trước mình thống nhất A, giờ anh thích B — điều gì THAY ĐỔI?" |
| Email dài, nhiều cc | Muốn bảo vệ mình / political | Chuyển sang meeting 1:1 để nói thật |
| Nhắc đi nhắc lại 1 điểm | Đây là TOP PRIORITY thực sự | Ghi nhận rõ ràng + confirm priority |

### 5.2 Reading Online Signals (Remote/Outsource)

| Signal | Dấu hiệu cụ thể | Cách xử lý |
|--------|-----------------|------------|
| **Camera off liên tục** | Không engage / multi-tasking | Đặt câu hỏi trực tiếp: "[Tên], anh/chị nghĩ sao?" |
| **Delay reply chat** | Bận thật hoặc né tránh | Gửi follow-up có deadline: "Xin feedback trước thứ 5" |
| **"Cái này để tôi hỏi lại"** | Không có quyền quyết định | Hỏi: "Ai là người quyết cuối cùng? Mình invite luôn?" |
| **Đồng ý mọi thứ quá nhanh** | Chưa đọc kỹ / muốn cho xong | Review cùng: "Mình walk-through từng mục nhé?" |

---

## 6. Xử lý Stakeholder Khó

### 6.1 Silent Stakeholder (Người im lặng)

**Triệu chứng:** Không phản hồi, "ok hết", bỏ meeting

**Chiến lược:**
```
1. 1:1 thay vì group → Giảm áp lực xã hội
2. Gửi câu hỏi TRƯỚC meeting → Cho time chuẩn bị
3. Dùng visual (mockup, diagram) → Dễ phản ứng hơn text
4. Hỏi cụ thể, không hỏi mở:
   ❌ "Anh nghĩ sao?"
   ✅ "Giữa Option A và B, anh chọn cái nào? Tại sao?"
5. CỰC KỲ QUAN TRỌNG: Ghi vào MoM → "Đã trình bày cho [Tên], không có phản đối"
```

### 6.2 Hostile Stakeholder (Người chống đối)

**Triệu chứng:** Phản đối mọi thứ, "hệ thống cũ tốt rồi", toxic

**Chiến lược:**
```
1. ĐỒNG CẢM TRƯỚC: "Tôi hiểu anh đã dùng hệ thống cũ 10 năm rất thuần thục"
2. TÌM NGUYÊN NHÂN: Sợ mất việc? Sợ thay đổi? Bị ép từ trên?
3. MỜI LÀM ĐỒNG MINH: "Kinh nghiệm 10 năm của anh rất quý — anh giúp team tránh sai lầm được không?"
4. CHỨNG MINH BẰNG DATA: "Quy trình mới giảm 60% thời gian xử lý — anh sẽ có thời gian cho việc quan trọng hơn"
5. NẾU VẪN CHỐNG: Escalate cho PM/Sponsor, GHI CHÉP mọi thứ
```

### 6.3 Vague Stakeholder (Người mơ hồ)

**Triệu chứng:** "Tôi muốn nó đẹp", "giống Facebook", "linh hoạt"

**Chiến lược:**
```
1. PIN DOWN: "Đẹp = màu sắc? layout? tốc độ? Anh cho ví dụ 1 trang web anh thấy đẹp?"
2. MoSCoW NGAY: "Trong 5 tính năng anh nói, cái nào CHẾT nếu không có?"
3. PROTOTYPE SỚM: Cho xem wireframe → "Giống cái này không?" → iterate
4. VIẾT RA: "Mình ghi lại: [yêu cầu]. Anh đọc và confirm nhé?"
5. ANTI-REQUIREMENTS: "Anh KHÔNG muốn hệ thống giống cái gì?"
```

### 6.4 Political Stakeholder (Người chính trị nội bộ)

**Triệu chứng:** Nói một đằng — email cc sếp một nẻo

**Chiến lược:**
```
1. MỌI THỨ BẰNG VĂN BẢN: Email recap sau mỗi meeting
2. KHÔNG ĐỨNG VỀ PHE NÀO: BA là neutral ground
3. FOCUS VÀO DATA: "Theo data, phương án A tiết kiệm 30% chi phí"
4. ESCALATE SỚM: Nếu conflict ảnh hưởng dự án → báo PM/Sponsor ngay
```

---

## 7. Framework Phân tích — Từ Raw Data → Actionable Insights

### 7.1 Affinity Diagram (Gom nhóm ý tưởng)

**Khi nào:** Sau khi có NHIỀU data rời rạc từ interviews/workshops

```
Bước 1: Gom tất cả notes/quotes lên 1 board (Miro/Sticky notes)
Bước 2: Nhóm theo THEME — ĐỂ DATA TỰ GOM, không áp framework sẵn
Bước 3: Đặt tên cho mỗi nhóm
Bước 4: Tìm pattern → nhóm nào LỚN NHẤT = pain point chính

Ví dụ output:
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ 🔴 Tốc độ   │ │ 🟡 Quyền     │ │ 🟢 Báo cáo   │
│ (12 notes)   │ │ (8 notes)    │ │ (5 notes)    │
│              │ │              │ │              │
│ - Chậm load  │ │ - Ai duyệt?  │ │ - Muốn auto  │
│ - Timeout    │ │ - Conflict   │ │ - Export PDF │
│ - Lag filter │ │ - Phân quyền │ │ - Real-time  │
└──────────────┘ └──────────────┘ └──────────────┘
→ Priority: Tốc độ > Quyền > Báo cáo
```

### 7.2 Empathy Map (Bản đồ Đồng cảm)

**Khi nào:** Cần hiểu sâu 1 nhóm user cụ thể

```
┌───────────────────────────────────────────────┐
│                    THINKS                      │
│  "Sao hệ thống phức tạp thế?"                │
│  "Boss chỉ nhìn số, không hiểu khó khăn"     │
├──────────────────┬────────────────────────────┤
│      SAYS        │          DOES              │
│                  │                            │
│ "Cần nhanh hơn" │  Copy data sang Excel      │
│ "Thiếu tính năng"│  Ghi chú trên giấy        │
│ "OK, được rồi"  │  Bypass hệ thống           │
├──────────────────┴────────────────────────────┤
│                    FEELS                       │
│  😤 Frustrated với hệ thống hiện tại          │
│  😰 Lo lắng deadline                          │
│  🤷 Bất lực vì không được hỏi ý kiến          │
└───────────────────────────────────────────────┘

→ INSIGHT: User nói "OK" nhưng HÀNH VI cho thấy bypass hệ thống
→ ACTION: Redesign flow cho đơn giản hơn, không hỏi thêm tính năng
```

### 7.3 Insight Card (Thẻ phát hiện)

**Template cho mỗi insight khai thác được:**

```markdown
## INSIGHT #[số]

**Nguồn:** [Phỏng vấn/Workshop/Observation] — [Ngày] — [Stakeholder]
**Trích dẫn gốc:** "[Nguyên văn lời KH]"
**Phân tích:**
- Pain point: [Mô tả vấn đề cốt lõi]
- Root cause: [Nguyên nhân gốc rễ]
- Impact: [Ảnh hưởng lượng hóa nếu có]
**Khuyến nghị:** [Đề xuất cụ thể]
**Priority:** [P1 Critical / P2 High / P3 Medium / P4 Low]
**Linked Requirements:** [BR-xxx, FR-xxx]
```

---

## 8. Template Phỏng vấn theo Giai đoạn

### 8.1 Discovery Interview (Lần gặp đầu — 45-60 min)

```markdown
## Warm-up (5 min)
- Giới thiệu bản thân + vai trò
- "Cuộc nói chuyện này hoàn toàn để HIỂU, không phải để đánh giá"

## Context (10 min)
1. "Anh/chị ở bộ phận nào? Vai trò hàng ngày?"
2. "Bộ phận có bao nhiêu người? Ai làm gì?"
3. "Hệ thống/công cụ đang dùng? (tên, từ khi nào)"

## Current State (15 min) — Probing Level 1-3
4. "Walk me through 1 ngày làm việc điển hình"
5. "Bước nào MẤT THỜI GIAN nhất?"
6. "Lần cuối gặp SỰ CỐ là khi nào?"
7. "Nếu thay đổi 1 thứ, thay đổi gì?"

## Hidden Needs (10 min) — Probing Level 4-5
8. "Có gì anh/chị MUỐN nhưng nghĩ không khả thi?"
9. "Đối thủ/đối tác làm gì mà anh/chị thấy hay?"
10. "Nếu hệ thống mới làm được BẤT CỨ GÌ — anh/chị muốn gì?"

## Wrap-up (5 min)
11. "Có ai khác tôi NÊN NÓI CHUYỆN không?"
12. "Tôi có thể liên hệ lại nếu cần thêm thông tin?"
13. Paraphrase + confirm key takeaways
```

### 8.2 Validation Interview (Lần gặp 2-3 — 30 min)

```markdown
## Review Findings (10 min)
1. "Lần trước mình thống nhất [A, B, C]. Anh/chị confirm lại?"
2. "Có gì THAY ĐỔI kể từ lần nói chuyện trước?"

## Deep-dive (15 min) — Probing Level 4-6
3. Specific questions based on gaps from round 1
4. Scenario-based: "Nếu [tình huống X] thì sao?"
5. Priority: "Trong 5 yêu cầu, cái nào CHẾT nếu không có?"

## Prototype Review (if applicable — 10 min)
6. "Đây là wireframe/mockup — giống cái anh/chị nói không?"
7. "Thiếu gì? Thừa gì? Sai gì?"

## Close
8. Confirm next steps + timeline
```

### 8.3 Stakeholder Report Template

```markdown
# BÁO CÁO KHAI THÁC THÔNG TIN KHÁCH HÀNG

**Dự án:** [Tên]
**Ngày báo cáo:** [DD/MM/YYYY]
**BA thực hiện:** [Tên]

## 1. Tổng quan phỏng vấn
| # | Stakeholder | Vai trò | Ngày | Phương thức | Thời lượng |
|---|------------|---------|------|------------|-----------|
| 1 | [Tên]      | [Role]  | [Date]| Online/F2F | [min]    |

## 2. Key Insights (Top 5)
[Dùng Insight Card template ở mục 7.3]

## 3. Empathy Map tổng hợp
[Empathy Map cho primary user group]

## 4. Ma trận Nhu cầu
| # | Need (Nhu cầu) | Loại | Source | Priority | Linked FR |
|---|----------------|------|--------|----------|----------|
| 1 | [Mô tả]        | Stated/Hidden | [Ai nói] | P1-P4 | FR-xxx |

## 5. Red Flags & Risks
- [Vấn đề cần escalate]
- [Mâu thuẫn giữa stakeholders]

## 6. Recommended Next Steps
- [ ] [Action item 1]
- [ ] [Action item 2]
```

---

## 9. Checklist Trước & Sau Phỏng vấn

### Trước phỏng vấn (Preparation)
- [ ] Research stakeholder (LinkedIn, org chart, vai trò)
- [ ] Đọc tài liệu hiện tại (quy trình, hệ thống, report cũ)
- [ ] Chuẩn bị câu hỏi theo Probing Level phù hợp
- [ ] Gửi agenda + mục tiêu trước 2 ngày
- [ ] Setup recording tool (nếu cần — xin phép trước)
- [ ] Chuẩn bị visual (mockup, sơ đồ) nếu là lần 2+

### Sau phỏng vấn (Follow-up)
- [ ] Viết meeting notes trong vòng 4 giờ
- [ ] Gửi email recap cho KH confirm trong 24 giờ
- [ ] Update Insight Cards
- [ ] Cập nhật Affinity Diagram
- [ ] Đánh dấu câu hỏi chưa trả lời → hẹn follow-up
- [ ] Update Stakeholder Intelligence Matrix (nếu thay đổi)

---

## 10. Quick Reference — Câu hỏi "Xương sống"

> **Dùng khi:** Không biết hỏi gì tiếp — quay về 10 câu này

| # | Câu hỏi | Mục đích |
|---|--------|---------|
| 1 | "Mô tả 1 ngày làm việc điển hình?" | Context |
| 2 | "Bước nào khó nhất / chậm nhất?" | Pain point |
| 3 | "Nếu thay đổi 1 thứ, thay đổi gì?" | Priority |
| 4 | "Lần cuối có sự cố là khi nào?" | Edge case |
| 5 | "Tại sao lại làm theo cách này?" | Root cause |
| 6 | "Ai quyết định cuối cùng?" | Governance |
| 7 | "Nếu không giải quyết thì 6 tháng nữa ra sao?" | Impact |
| 8 | "Có gì muốn nhưng nghĩ không khả thi?" | Hidden need |
| 9 | "Anh/chị KHÔNG muốn hệ thống giống cái gì?" | Anti-req |
| 10 | "Thành công là gì? Đo bằng metric nào?" | Success criteria |
