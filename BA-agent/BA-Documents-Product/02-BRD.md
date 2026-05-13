# TÀI LIỆU YÊU CẦU NGHIỆP VỤ (BRD)
# Epic: Feedback Portal & Triage Loop

> **Phiên bản:** 1.0 | **Ngày:** 12/05/2026
> **Product:** SignalDesk | **Trạng thái:** Draft
> **Tham chiếu:** Vision & Scope v1.0

---

## 1. Vấn đề cần giải quyết

> **Vấn đề người dùng gặp phải:**
> PM và CS teams đang thu feedback từ nhiều nguồn nhưng không có một luồng thống nhất để biến feedback thành roadmap decisions.

> **Bằng chứng / Số liệu:**

### 1.1. Pain Points / Vấn đề hiện tại

| # | Vấn đề hiện tại | Ảnh hưởng | Mức độ |
|---|----------------------|-----------|--------|
| 1 | 43% feedback mới đang nằm trong Slack hoặc email, không vào backlog | PM không thấy toàn cảnh nhu cầu khách hàng | 🔴 Cao |
| 2 | 31% khách hàng beta nói họ không biết request của mình đang ở trạng thái nào | CS mất thời gian trả lời thủ công | 🟠 Cao |
| 3 | 22% feedback bị trùng nội dung nhưng không được gộp | Roadmap bị noisy, vote count không đáng tin | 🟠 Cao |

### 1.2. Glossary

| Thuật ngữ | Giải thích |
|---|---|
| Feedback item | Một yêu cầu hoặc phản hồi từ người dùng cuối |
| Subscriber | Người theo dõi một feedback item để nhận update |
| Merge | Gộp feedback trùng vào một parent item |
| Release note | Bản ghi public mô tả giá trị đã phát hành |

---

## 2. Nhóm người dùng mục tiêu

| Nhóm người dùng | Đặc điểm | Nhu cầu | Khó khăn / Nỗi đau | Mục tiêu |
|-----------------|----------|---------|---------------------|----------|
| Product Manager | Quản lý roadmap cho 1-3 squads | Thấy feedback theo theme và priority | Feedback rải rác, khó defend roadmap | Prioritize đúng hơn |
| CS Lead | Là người tiếp xúc khách hàng mỗi ngày | Trả lời khách hàng có update trạng thái | Không biết feedback đã được PM xử lý chưa | Reduce manual follow-up |
| End User / Customer Champion | Power user trong công ty khách hàng | Gửi request, upvote, theo dõi tiến độ | Không có kênh rõ ràng, gửi rồi “mất hút” | Được phản hồi rõ ràng |

---

## 3. Chỉ tiêu đo lường thành công (OKRs)

| Mục tiêu | Kết quả then chốt | Chỉ tiêu | Hiện tại | Công cụ đo |
|----------|--------------------|----------|----------|------------|
| O1: Kích hoạt workflow feedback | KR1: 55% workspace mới publish portal trong 14 ngày | 55% | 0% | Mixpanel |
| | KR2: 60% feedback mới có status trong 7 ngày | 60% | 0% | Mixpanel |
| O2: Giảm support friction | KR3: 30% ticket “status request” chuyển sang portal self-serve | 30% | 0% | Zendesk + Mixpanel |
| O3: Tạo perceived value cho Pro | KR4: 8% workspace free dùng notification feature nâng cấp Pro trong 60 ngày | 8% | 0% | Stripe |

---

## 4. Giải pháp đề xuất

### 4.1. Mô tả giải pháp
SignalDesk cung cấp public feedback portal cho khách hàng gửi request và upvote. Team nội bộ nhìn thấy feedback trong inbox chung, được gợi ý feedback trùng, gắn tag, đổi status, và publish release notes khi hoàn thành.

### 4.2. Luồng thao tác người dùng
> Chi tiết tại `04-User-Flow.md`

```
Customer gửi feedback -> Workspace inbox nhận feedback -> PM review và gắn status/tag
-> Nếu trùng thì merge vote/history -> Customer nhận update trạng thái
-> Khi release, PM publish changelog gắn với feedback liên quan
```

**As-Is / Hiện trạng**
- Feedback đang nằm ở Slack, Intercom, email, spreadsheet.
- Không có một current-state workflow thống nhất giữa PM và CS.

### 4.3. Giao diện phác thảo
> Link Figma: Figma / SignalDesk Beta / Portal-v5

---

## 5. Yêu cầu nghiệp vụ (Business Requirements)

### 5.1. Yêu cầu chức năng

| Mã | Yêu cầu nghiệp vụ | Mô tả | Bên liên quan |
|----|-------------------|-------|---------------|
| BR-001 | Public portal nhận feedback | Khách hàng có thể gửi feedback và xem status của feedback đã gửi | End User, PM |
| BR-002 | Feedback trùng phải được gợi ý merge | PM phải thấy candidate duplicates để tránh vote bị phân mảnh | PM |
| BR-003 | Status update phải phản hồi lại cho người theo dõi | Khi PM đổi status, subscriber phải được thông báo | PM, CS Lead |
| BR-004 | Release notes phải nối với feedback đã ship | Product team cần chứng minh “feedback -> delivered value” | PM, Founder |
| BR-005 | Portal phải đo activation và engagement | Mọi luồng chính phải phát analytics events để đo activation | PM, Growth |

### 5.2. Quy tắc nghiệp vụ (Business Rules)

| Mã | Quy tắc | Áp dụng cho |
|----|---------|-------------|
| BIZ-01 | Một user chỉ được upvote một feedback item một lần trong cùng workspace | Portal |
| BIZ-02 | Merge feedback không được mất vote count, subscriber list, hay audit history | Triage |
| BIZ-03 | Chỉ feedback ở trạng thái `Planned`, `In Progress`, `Released` mới được hiển thị status công khai | Portal |
| BIZ-04 | Release note chỉ hiển thị public sau `publish_at` | Changelog |
| BIZ-05 | Mọi transition status phải ghi event analytics và audit log | Triage / Analytics |

### 5.3. Business Rule Architecture

- **Execution order:** submit feedback -> deduplicate review -> status assignment -> subscriber notification -> release note publication.
- **Override matrix:** chỉ Admin hoặc Product Manager mới được merge feedback hoặc đổi trạng thái public-facing.
- **Decision owner:** Product Lead quyết định status model; Growth Lead quyết định event taxonomy; CS Lead được consult về subscriber messaging.

### 5.4. Giả định & Ràng buộc

| Loại | Nội dung | Ảnh hưởng nếu sai |
|---|---|---|
| Assumption | Workspace có ít nhất 1 PM willing to maintain status hằng tuần | Portal thành “dead board”, mất trust |
| Assumption | Người dùng cuối chấp nhận đăng nhập magic-link hoặc email verify để theo dõi feedback | Adoption portal thấp |
| Constraint | MVP không hỗ trợ SSO cho end-user portal | Enterprise onboarding chưa support ngay |
| Constraint | Không làm AI auto-prioritization ở phase này | PM vẫn phải quyết định priority thủ công |
| Constraint | Chỉ support 1 portal public / workspace ở MVP | Hạn chế multi-brand use case |

---

## 6. Phạm vi tính năng (Phân loại ưu tiên)

### ✅ BẮT BUỘC (Must)

| ID | Tính năng | Mô tả nhu cầu | Phân loại giá trị | Giai đoạn |
|----|-----------|---------------|-------------------|----------|
| F-001 | Public feedback portal | Khách hàng gửi feedback và xem trạng thái | Nâng cao (Performance) | GĐ1 |
| F-002 | Feedback inbox & triage | PM xem feedback, tag, đổi status | Nâng cao (Performance) | GĐ1 |
| F-003 | Duplicate merge | PM gộp feedback trùng và giữ vote/history | Nâng cao (Performance) | GĐ1 |

### 🟡 NÊN CÓ (Should)

| ID | Tính năng | Mô tả nhu cầu | Phân loại giá trị | Giai đoạn |
|----|-----------|---------------|-------------------|----------|
| F-004 | Status notification | Subscriber nhận email khi feedback đổi trạng thái | Gây ấn tượng (Attractive) | GĐ2 |
| F-005 | Release notes feed | PM publish changelog gắn với delivered feedback | Gây ấn tượng (Attractive) | GĐ2 |

### 🔵 CÓ THỂ (Could)

| ID | Tính năng | Mô tả nhu cầu | Phân loại giá trị | Giai đoạn |
|----|-----------|---------------|-------------------|----------|
| F-006 | Saved filters | PM lưu view theo tag/status | Gây ấn tượng (Attractive) | GĐ3+ |

### ❌ CHƯA LÀM (Won't)

| Feature | Lý do | Xem xét lại |
|---------|-------|-------------|
| AI auto-prioritization | Chưa đủ dữ liệu và trust threshold | Sau 2 quý usage |

---

## 7. Ngoài phạm vi

- Multi-workspace consolidated analytics
- Native mobile app
- White-label portal full custom domain

---

## 8. Phụ thuộc & Giả định

### Phụ thuộc (Dependencies)

| # | Phụ thuộc vào | Đội / Dịch vụ | Trạng thái |
|---|-----------|-------------|--------|
| 1 | Email delivery service | Platform | Ready |
| 2 | Event pipeline vào Mixpanel | Data | Planned |
| 3 | Release note editor basic | Frontend | In progress |

### Elicitation Record

- 12 cuộc phỏng vấn với PM và CS leads tại startup SaaS 10-80 nhân sự.
- 37 đoạn hội thoại support được audit để phân loại feedback requests.
- 3 prototype tests cho portal public và feedback inbox.

### System Memory / Historical Data

- Merge feedback phải giữ full history của parent/child item.
- Status timeline của feedback phải xem lại được để CS giải thích với khách hàng.
- Release notes cần nối với feedback đã tồn tại từ các sprint trước.

---

## 9. Rủi ro & Giải pháp giảm thiểu

| # | Rủi ro | Xác suất | Mức ảnh hưởng | Giải pháp giảm thiểu |
|---|--------|----------|---------------|----------------------|
| 1 | PM không maintain status đều đặn | Cao | Cao | Weekly digest + owner reminder |
| 2 | Merge suggestion false positive | Trung bình | Cao | Manual review only, không auto merge |
| 3 | Portal bị spam | Trung bình | Trung bình | Rate limit + email verify |
| 4 | Notification gây noise | Trung bình | Cao | Cho subscribe/unsubscribe theo item |

---

## 10. Câu hỏi chưa có lời đáp

| # | Câu hỏi | Phụ trách | Hạn trả lời | Đáp án |
|---|---------|-----------|-------------|--------|
| 1 | Có cần custom status per workspace trong MVP không? | Product Lead | 20/05/2026 | |
| 2 | Có cho anonymous feedback submit không? | PM + Legal | 22/05/2026 | |

---

## 11. Kế hoạch Phát hành & Triển khai

| Giai đoạn | % Người dùng | Thời gian | Tiêu chí chuyển tiếp |
|-----------|-------------|-----------|----------------------|
| Kiểm thử nội bộ | Chỉ đội ngũ | 1 tuần | 0 lỗi nghiêm trọng |
| Thử nghiệm kín (Beta) | 5% workspace | 2 tuần | Activation ≥ 45%, 0 critical issue |
| Thử nghiệm mở | 20% workspace | 1 tuần | Metrics ổn định, spam rate thấp |
| Ra mắt chính thức | 100% người dùng | — | Đạt KR activation chính |

---

## 12. Ma trận truy vết (RTM — Requirement Traceability Matrix)

| Goal Ref | Yêu cầu liên quan | Tính năng | Story | Test / Beta |
|-------------|-------------|---------|-------|-------------|
| O1-KR1 | BR-001, BR-002 | F-001, F-002, F-003 | US-001, US-002, US-003 | UAT-001, UAT-002, IT-001 |
| O2-KR3 | BR-003 | F-004 | US-004 | UAT-004, IT-004 |
| O3-KR4 | BR-004, BR-005 | F-005 | US-005 | UAT-005, UAT-NFR-001 |

---

## 13. Phê duyệt

| Vai trò | Họ tên | Chữ ký | Ngày |
|---------|--------|--------|------|
| Product Lead | | | |
| PM / BA | | | |

> **Quy tắc:** Sau khi phê duyệt, mọi thay đổi yêu cầu phải qua quy trình Yêu cầu Thay đổi (CR) — xem `09-Release-Notes.md`

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Người |
|-----------|------|----------|-------|
| 0.1 | 05/05/2026 | Draft đầu tiên | PM/BA |
| 1.0 | 12/05/2026 | Approved cho discovery build | PM/BA |
