# USER PERSONAS & STAKEHOLDER MAP
# SignalDesk

> **Phiên bản:** 1.0 | **Ngày:** 13/05/2026
> **Tham chiếu:** `01-Vision-Scope.md`, `02-BRD.md`

---

## 1. User Personas

### Persona 1: Lan Nguyen - Product Manager at B2B SaaS Startup

| Mục | Chi tiết |
|-----|----------|
| **Tên** | Lan Nguyen |
| **Tuổi** | 29-35 |
| **Vai trò** | Product Manager |
| **Kỹ năng tech** | Medium |
| **Goal** | Gom feedback về một chỗ, giảm noise, và có bằng chứng định lượng để defend roadmap |
| **Pain Points** | - Feedback nằm rải rác ở Slack, Intercom, email, spreadsheet<br>- Vote count bị phân mảnh vì duplicate requests<br>- Khó chứng minh feature nào nên làm trước |
| **Hành vi hiện tại** | Tổng hợp feedback thủ công mỗi tuần, copy vào Notion hoặc Airtable, tự gắn label và ping CS để hỏi bối cảnh |
| **Kỳ vọng** | Một inbox feedback đủ nhẹ để review hằng ngày, có duplicate suggestion và status public để giảm phải trả lời thủ công |
| **Quote** | _"Tôi không cần bộ roadmap quá nặng; tôi cần biết khách hàng đang đòi cái gì và mình đã phản hồi tới đâu."_ |

**User Journey**
```
[Traffic review] -> [Publish portal] -> [Import backlog] -> [Triage inbox] -> [Merge duplicates] -> [Publish update]
       😐                 🙂                🙂                😊                😊                 🎉
```

**Jobs-to-be-done**
- Khi feedback đến từ nhiều nguồn, tôi muốn gom chúng về một inbox chung để không mất ngữ cảnh.
- Khi nhiều khách hàng nói cùng một vấn đề, tôi muốn merge chúng lại để vote count đáng tin.
- Khi stakeholder hỏi tại sao làm feature này, tôi muốn có dữ liệu feedback và release proof để trả lời.

**Success Signals**
- Publish portal trong 14 ngày đầu.
- Tối thiểu 60% feedback mới có status trong 7 ngày.
- Dùng release notes linked to feedback trong mỗi sprint release.

---

### Persona 2: Minh Tran - Customer Success Lead

| Mục | Chi tiết |
|-----|----------|
| **Tên** | Minh Tran |
| **Tuổi** | 30-38 |
| **Vai trò** | Customer Success Lead |
| **Kỹ năng tech** | Medium |
| **Goal** | Trả lời khách hàng nhanh về trạng thái request mà không cần chase PM liên tục |
| **Pain Points** | - Khách hàng hỏi "request của tôi đang tới đâu?" quá nhiều<br>- Không có status timeline thống nhất để trả lời<br>- Khi feature ship xong, khó quay lại chứng minh là đã xử lý |
| **Hành vi hiện tại** | Ghi chú feedback trong CRM hoặc spreadsheet, sau đó ping PM trên Slack để hỏi status và tự soạn email update |
| **Kỳ vọng** | Có portal public để khách hàng tự theo dõi status, có subscriber notification và release notes để giảm support friction |
| **Quote** | _"Mỗi lần khách hàng hỏi lại status là một lần team mất thời gian vì không có nguồn sự thật chung."_ |

**User Journey**
```
[Collect request] -> [Search existing item] -> [Subscribe customer] -> [Track status] -> [Share release note]
       😐                  🙂                     🙂                 😊               🎉
```

**Jobs-to-be-done**
- Khi khách hàng gửi request mới, tôi muốn kiểm tra nhanh đã có item tương tự chưa để tránh tạo noise.
- Khi PM đổi status, tôi muốn subscriber tự nhận được update để giảm follow-up thủ công.
- Khi feature phát hành, tôi muốn gửi release note gắn đúng feedback để tăng trust.

**Success Signals**
- Giảm 30% ticket hỏi trạng thái request.
- Mọi khách hàng quan trọng đều có item feedback/subscriber rõ ràng.
- Dùng release note link như bằng chứng trong QBR hoặc renewal call.

---

### Persona 3: Alex Vo - Customer Champion / Power User

| Mục | Chi tiết |
|-----|----------|
| **Tên** | Alex Vo |
| **Tuổi** | 26-40 |
| **Vai trò** | Ops Manager / Team Lead tại công ty khách hàng |
| **Kỹ năng tech** | Low to Medium |
| **Goal** | Gửi ý kiến dễ dàng, thấy request của mình có được xem xét hay không, và biết khi nào feature ship |
| **Pain Points** | - Gửi request qua email rồi không biết có ai đọc không<br>- Không biết nên upvote item nào thay vì tạo request mới<br>- Không nhận được tín hiệu rõ ràng khi tính năng đã phát hành |
| **Hành vi hiện tại** | Gửi email cho CS hoặc nhắn trực tiếp trong chat support, sau đó chờ phản hồi thủ công |
| **Kỳ vọng** | Một portal đơn giản để gửi feedback, upvote, theo dõi status và nhận update khi có thay đổi |
| **Quote** | _"Tôi không cần nhìn roadmap nội bộ; tôi chỉ muốn biết request của mình có được ghi nhận và có tiến triển hay không."_ |

**User Journey**
```
[Visit portal] -> [Search similar idea] -> [Submit or upvote] -> [Subscribe] -> [Receive status update] -> [Read release note]
      🙂                🙂                    😊                😊                 😊                    🎉
```

**Jobs-to-be-done**
- Khi tôi có nhu cầu mới, tôi muốn tìm xem đã có request tương tự chưa để chỉ cần upvote.
- Khi tôi gửi feedback, tôi muốn nhận xác nhận và theo dõi tiến độ rõ ràng.
- Khi feature phát hành, tôi muốn xem release note gắn đúng feedback đã theo dõi.

**Success Signals**
- Gửi feedback thành công dưới 2 phút.
- Dễ hiểu status công khai như `New`, `Planned`, `In Progress`, `Released`.
- Có thể unsubscribe nếu không muốn nhận thêm email.

---

## 2. Persona Priority Matrix

| Persona | Tần suất dùng | Ảnh hưởng đến doanh thu | Ưu tiên phát triển | Lý do |
|---------|---------------|-------------------------|-------------------|-------|
| Lan Nguyen - Product Manager | Hàng ngày | Rất cao | 🔴 Primary | Là buyer/user chính, quyết định adoption và renewal |
| Minh Tran - CS Lead | Hàng ngày | Cao | 🟠 Secondary | Tác động mạnh tới support load và perceived responsiveness |
| Alex Vo - Customer Champion | Hàng tuần / theo nhu cầu | Trung bình | 🟡 Tertiary | Không trả tiền trực tiếp nhưng quyết định volume feedback và trust |

---

## 3. Internal Stakeholders

| # | Stakeholder | Vai trò | Mức ảnh hưởng | Kỳ vọng chính | Approver | Conflict Risk |
|---|-------------|---------|---------------|----------------|----------|---------------|
| S01 | Product Lead | Sponsor / roadmap owner | 🔴 Rất cao | Activation, retention, paid conversion | Y | High |
| S02 | CTO / Tech Lead | Architecture & delivery | 🔴 Rất cao | Data model đúng từ đầu, merge/audit an toàn | Y | Medium |
| S03 | Product Designer | Portal UX, inbox UX | 🟠 Cao | Submit nhanh, status dễ hiểu, low friction | N | Medium |
| S04 | Engineering Team | Build features | 🟠 Cao | Scope rõ, API/event contracts ổn định | N | Medium |
| S05 | Customer Success Lead | Voice of customer | 🟠 Cao | Notification và release proof dùng được thật | N | High |
| S06 | Growth / Marketing | Positioning, activation experiments | 🟡 Trung bình | CTA, onboarding funnel, event tracking đủ dùng | N | Medium |
| S07 | Data Analyst | Event taxonomy & dashboards | 🟡 Trung bình | Event schema chuẩn, dễ đo activation | N | Low |

### 3.1. Decision Ownership

| Decision Type | Owner | Consulted | Informed |
|---------------|-------|-----------|----------|
| Public status model | Product Lead | CS Lead, Designer | Engineering |
| Duplicate merge logic | Product Lead | Tech Lead, PM | CS Lead |
| Event taxonomy | Growth / Product Analyst | PM, Tech Lead | Leadership |
| Release note publication policy | Product Lead | CS Lead | Customers via portal |

### 3.2. Expected Conflict Areas

| Area | Stakeholders | Risk | Handling approach |
|------|--------------|------|-------------------|
| Portal friction vs spam control | Product, Growth, Tech | Medium | A/B test email verification and rate-limit threshold |
| Status transparency vs commitment risk | Product, CS, Leadership | High | Use controlled public statuses defined in BR `BIZ-03` |
| Duplicate threshold aggressiveness | PM, Engineering, CS | Medium | Start suggestion-only, no forced auto-merge |
| Event coverage vs implementation scope | Growth, Engineering | Medium | Prioritize events in `BR-005` and `NFR-007` for P0 only |

---

## 4. Communication Plan

| Stakeholder | Nội dung | Tần suất | Kênh | Output |
|-------------|----------|----------|------|--------|
| Product Lead | Activation metrics, scope decisions, beta risks | Hàng tuần | Product review | Decision log |
| Engineering Team | Requirement clarifications, event schema changes, edge cases | 2 lần/tuần + ad hoc | Slack + grooming | Updated SRS Lite / story notes |
| Designer | Portal friction points, usability findings | Hàng tuần trong discovery/beta | Figma review | Prototype updates |
| CS Lead | Status wording, notification content, top customer asks | Hàng tuần | Sync meeting | Messaging backlog |
| Growth / Data | Funnel metrics, A/B test setup, dashboard review | 2 tuần/lần | Metrics review | Event QA sheet |

---

## 5. User Interview Plan

| Wave | Persona | Số lượng | Phương thức | Mục tiêu | Câu hỏi mẫu |
|------|---------|----------|------------|----------|-------------|
| Wave 1 - Discovery | Product Manager | >= 6 | Video call 30-45p | Hiểu hiện trạng feedback chaos, toolchain hiện tại | "Hiện tại bạn gom feedback từ đâu và quyết định ưu tiên bằng cách nào?" |
| Wave 1 - Discovery | CS Lead | >= 4 | Video call 30p | Hiểu support friction và status communication gap | "Một tuần bạn phải trả lời bao nhiêu câu hỏi kiểu 'feature này tới đâu rồi'?" |
| Wave 1 - Discovery | Customer Champion | >= 5 | Remote interview 20p | Hiểu kỳ vọng portal public, status visibility | "Khi gửi request cho vendor, bạn kỳ vọng điều gì xảy ra sau đó?" |
| Wave 2 - Prototype Validation | Product Manager + CS Lead | >= 5 | Usability test 30p | Validate portal submit, inbox triage, merge confidence | "Bạn có hiểu khi nào nên merge và khi nào không?" |
| Wave 3 - Closed Beta | All three personas | 25 workspace + end users chọn lọc | In-app survey + interview | Đo activation, trust, release proof value | "Điều gì khiến bạn quay lại SignalDesk sau tuần đầu?" |

### 5.1. Evidence to Capture

- Source system hiện tại: Slack, Intercom, email, spreadsheet, Notion.
- Current time spent để triage hoặc trả lời status questions.
- Frequency khách hàng gửi duplicate request.
- Mức sẵn sàng để dùng public portal thay cho email/chat.
- Reaction với các status công khai `New`, `Planned`, `In Progress`, `Released`.

---

## 6. Persona-to-Requirement Mapping

| Persona | Requirement ưu tiên | Vì sao |
|---------|---------------------|--------|
| Product Manager | `BR-001`, `BR-002`, `BR-005` | Cần inbox sạch, merge được duplicate và có dữ liệu để defend roadmap |
| CS Lead | `BR-003`, `BR-004` | Cần trả lời khách hàng nhanh bằng status và release proof |
| Customer Champion | `BR-001`, `BR-003`, `BIZ-03` | Cần gửi feedback dễ, thấy được status công khai và cập nhật đúng lúc |
