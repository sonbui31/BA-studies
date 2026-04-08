# MEETING MINUTES — {{TÊN DỰ ÁN}}

> **Mục đích:** Ghi nhận quyết định, việc cần làm, báo cáo rủi ro cấp trên từ các cuộc họp
> **Quy tắc:** Gửi cho tất cả attendee trong vòng 24 giờ sau họp
> **Phiên bản:** v3.2

---

## Template — Biên bản họp

### Thông tin cuộc họp

| Hạng mục | Chi tiết |
|---------|---------|
| **Tiêu đề** | {{Tên cuộc họp}} |
| **Ngày** | {{DD/MM/YYYY}} |
| **Thời gian** | {{HH:MM}} — {{HH:MM}} |
| **Địa điểm** | {{Phòng họp / Link video call}} |
| **Người ghi** | {{Tên BA}} |
| **Loại họp** | Kickoff / Sprint Planning / Sprint Review / Workshop / Ad-hoc |
| **Ghi hình?** | ✅ Có (link: {{URL}}) / ❌ Không |

### Người tham dự

| Tên | Vai trò | Bên | Có mặt | Ghi chú |
|-----|---------|-----|--------|---------|
| {{Tên}} | {{Vai trò}} | KH / NCC | ✅ / ❌ | {{Ghi chú — ví dụ: vào muộn 10 phút}} |

### Agenda

| # | Chủ đề | Thời lượng | Người trình bày | Status |
|---|--------|-----------|----------------|--------|
| 1 | {{Chủ đề}} | {{XX phút}} | {{Tên}} | ✅ Xong / ⚠️ Chưa hết / ❌ Skip |

---

### Nội dung thảo luận

#### Chủ đề 1: {{Tên chủ đề}}

**Tóm tắt:**
{{Tóm tắt nội dung thảo luận — ghi ý chính, không cần verbatim}}

**Trích dẫn quan trọng (nếu có):**
> "{{Nguyên văn lời stakeholder quan trọng}}" — {{Tên, Vai trò}}

---

### 📋 Decision Log ⭐ NEW v3.2

> **Mục đích:** Ghi nhận TẤT CẢ quyết định đã đưa ra trong cuộc họp. Quan trọng cho traceability và tránh "tôi không nói vậy".

| # | Quyết định | Người quyết | Lý do | Ảnh hưởng | Trạng thái |
|---|-----------|:---:|---|---|:---:|
| D-01 | {{VD: Chọn PostgreSQL thay vì MySQL}} | {{CTO}} | {{Performance tốt hơn cho geo-queries}} | {{Data Model cần update}} | ✅ Final |
| D-02 | {{VD: Defer F04 sang Phase 2}} | {{PO}} | {{Timeline không đủ}} | {{Update BRD scope, Sprint Plan}} | ✅ Final |
| D-03 | {{VD: Thêm bulk import cho module X}} | {{PM}} | {{KH yêu cầu}} | {{CR-003, +2 story points}} | ⏳ Chờ phê duyệt |

**Quy tắc Decision Log:**
1. Quyết định PHẢI có **người chịu trách nhiệm** — không "team đồng thuận" mơ hồ
2. Quyết định ảnh hưởng scope/timeline → **trở thành CR** → link vào Change Log
3. Quyết định pending → **ghi deadline confirm** → follow up

---

### ⚠️ Báo cáo rủi ro cấp trên (Risk Escalation) ⭐ NEW v3.2

> **Mục đích:** Ghi nhận rủi ro và vấn đề phát hiện TRONG cuộc họp, cần báo cáo cấp trên hoặc thêm vào Risk Register.

| # | Vấn đề phát hiện | Severity | Ai phát hiện | Cần báo cáo đến | Deadline | Linked Risk ID |
|---|---|:---:|---|---|---|---|
| E-01 | {{VD: API HIS chưa có docs, có thể delay Sprint 3}} | 🔴 | {{BA}} | {{PM + HIS vendor}} | {{DD/MM}} | RSK-04 |
| E-02 | {{VD: Key dev có thể nghỉ phép 2 tuần Sprint 4}} | 🟡 | {{Dev Lead}} | {{PM}} | {{DD/MM}} | RSK-NEW |

**Quy tắc báo cáo cấp trên:**
1. 🔴 Critical → Báo cáo **trong 24 giờ**, không chờ meeting tiếp theo
2. 🟡 High → Báo cáo **trước Sprint Planning tiếp theo**
3. Mỗi lần báo cáo → **tạo hoặc cập nhật Risk Register entry**

---

### ❓ Open Items vs Closed Items ⭐ NEW v3.2

> **Tracking:** Vấn đề mở từ meetings TRƯỚC chưa giải quyết.

| # | Item | Mở từ cuộc họp | Owner | Deadline | Status |
|---|------|----------------|-------|----------|--------|
| OI-01 | {{VD: KH chưa confirm màu sắc branding}} | {{Meeting 15/03}} | {{PO}} | {{20/03}} | ☐ Open |
| OI-02 | {{VD: Test env chưa setup}} | {{Meeting 10/03}} | {{DevOps}} | {{18/03}} | ✅ Closed {{17/03}} |
| OI-03 | {{VD: RACI chưa ký}} | {{Meeting 01/03}} | {{PM}} | {{05/03}} | ⏰ **Overdue** |

---

### Action Items

| # | Action | Owner | Deadline | Priority | Status | Linked Decision |
|---|--------|-------|----------|:--------:|--------|:---:|
| 1 | {{Công việc cần làm}} | {{Tên}} | {{DD/MM/YYYY}} | P1/P2/P3 | ☐ Open | D-01 |
| 2 | {{Công việc}} | {{Tên}} | {{DD/MM}} | P1 | ☐ Open | — |

### Cuộc họp tiếp theo

| Hạng mục | Chi tiết |
|---------|---------|
| **Ngày** | {{DD/MM/YYYY}} |
| **Thời gian** | {{HH:MM}} |
| **Agenda dự kiến** | {{Chủ đề}} |
| **Open Items cần resolve** | OI-01, OI-03 |

---

## Quy tắc ghi Meeting Minutes v3.2

1. **Gửi trong 24 giờ** — người tham dự phải xác nhận (reply email "Confirmed" hoặc comment trên Confluence)
2. **Ghi QUYẾT ĐỊNH, không ghi tranh luận** — focus vào outcome
3. **Action Item phải có: Owner + Deadline + Priority** — không có = không tracking được
4. **Decision Log cho mọi quyết định** — dù nhỏ, để truy vết sau này
5. **Báo cáo rủi ro cấp trên ngay khi phát hiện** — không chờ meeting tiếp
6. **Open Items carry-forward** — items chưa close phải chuyển vào meeting tiếp
7. **Đánh số liên tục** theo format — `[PROJECT]-MoM-YYYY-MM-DD-01`
8. **Outsource: GHI HÌNH bắt buộc** — tránh "tôi không nói vậy"

---

## Log tất cả cuộc họp

| # | Ngày | Tiêu đề | Loại | Decisions | Escalations | Open Items | Status |
|---|------|--------|------|:---------:|:-----------:|:----------:|--------|
| 1 | {{ngày}} | {{tiêu đề}} | {{loại}} | {{N}} | {{N}} | {{N}} | ☐ Open / ✅ Closed |
