# VISION & SCOPE — PRODUCT
# SignalDesk

> **Phiên bản:** 1.0 | **Ngày:** 12/05/2026
> **Tác giả:** Product Manager + BA | **Trạng thái:** Draft

---

## 1. Tầm nhìn Sản phẩm

| Mục | Nội dung |
|-----|----------|
| **Tầm nhìn (Vision)** | Giúp product teams nhỏ thu thập, ưu tiên, và phản hồi customer feedback trong một luồng làm việc duy nhất thay vì tản mạn qua email, chat, và bảng tính. |
| **Nhóm người dùng mục tiêu** | PM, founder, CS lead, và khách hàng power-user của các SaaS B2B quy mô nhỏ đến vừa. |
| **Nhu cầu cốt lõi** | Gom feedback về một nơi, tránh feedback trùng, cho khách hàng thấy trạng thái xử lý, và biến insight thành roadmap có thể đo được. |
| **Loại sản phẩm** | SaaS web application |
| **Mục tiêu kinh doanh** | Tăng số workspace trả phí bằng cách giải quyết pain point feedback chaos và tạo habit weekly review cho teams sản phẩm. |

---

## 2. Mục tiêu chiến lược (OKRs)

### OKR Q1

| Mục tiêu (Objective) | Kết quả then chốt (Key Result) | Chỉ tiêu | Hiện tại | Phụ trách |
|---------------------|-------------------------------|----------|----------|-----------|
| O1: Kích hoạt workspace thành công | KR1: 65% workspace mới import ít nhất 20 feedback trong 7 ngày đầu | 65% | 0% | PM |
| | KR2: 55% workspace mới publish ít nhất 1 public feedback portal trong 14 ngày | 55% | 0% | PM |
| | KR3: Activation-to-value time ≤ 20 phút | ≤ 20 phút | N/A | UX |
| O2: Tạo thói quen review feedback hàng tuần | KR1: 45% workspace active có ít nhất 1 roadmap review/tuần | 45% | 0% | Product Ops |
| | KR2: 35% feedback mới được gắn trạng thái trong 7 ngày | 35% | 0% | PM |
| O3: Chứng minh willingness to pay | KR1: 8% workspace free chuyển sang Pro trong 60 ngày | 8% | 0% | Growth |
| | KR2: MRR đạt 18.000 USD cuối quý | 18.000 USD | 0 | Business |

---

## 3. Nhóm Khách hàng mục tiêu

> Chi tiết tại `03-User-Personas.md`

| Nhóm khách hàng | Đặc điểm | Nhu cầu chính | Khó khăn / Nỗi đau |
|-----------------|----------|---------------|--------------------|
| Product Manager tại startup SaaS | Team 5-30 người, làm nhiều việc cùng lúc | Có một inbox feedback tập trung và thứ tự ưu tiên rõ | Feedback nằm rải rác ở Intercom, Slack, email, spreadsheet |
| Founder / Head of Product | Quyết định roadmap trực tiếp | Muốn thấy feature nào được khách hàng đòi nhiều nhất | Không có dữ liệu định lượng để defend roadmap |
| Customer Success Lead | Là người nhận feedback đầu tiên từ khách hàng | Muốn trả lời khách hàng có update trạng thái hay release note rõ | Mất thời gian ping PM, không thấy status thống nhất |

---

## 4. Vấn đề cần giải quyết

> **Vấn đề:** Các team sản phẩm nhỏ đang thu feedback từ nhiều nguồn nhưng không có một hệ thống đủ nhẹ để gom, lọc trùng, và phản hồi lại cho khách hàng.
>
> **Giải pháp hiện tại:** Dùng Notion, Airtable, Trello, hoặc spreadsheet tự chế; đôi khi thêm form public nhưng không nối với roadmap.
>
> **Tại sao phải làm ngay?:** AI summarization và self-serve portals đang làm kỳ vọng của khách hàng tăng. Nếu SignalDesk không giúp team phản hồi nhanh hơn, họ sẽ quay về tool cũ hoặc chọn đối thủ có portal + changelog tích hợp.

---

## 5. Phạm vi Sản phẩm

### 5.1. Tính năng cốt lõi (Trong phạm vi)

| # | Tính năng | Mô tả | Mức ưu tiên | Phân loại giá trị |
|---|-----------|-------|-------------|-------------------|
| 1 | Workspace onboarding | Tạo workspace, mời team, import feedback mẫu | Bắt buộc (Must) | Nâng cao (Performance) |
| 2 | Public feedback portal | Cho khách hàng gửi feedback, upvote, theo dõi trạng thái | Bắt buộc (Must) | Nâng cao (Performance) |
| 3 | Duplicate merge & triage | Gợi ý feedback trùng, gộp vote, gán tag và status | Bắt buộc (Must) | Nâng cao (Performance) |
| 4 | Status notification | Thông báo khi feedback đổi trạng thái hoặc có release note liên quan | Nên có (Should) | Gây ấn tượng (Attractive) |
| 5 | Release notes feed | Publish changelog theo feature hoặc theme | Nên có (Should) | Gây ấn tượng (Attractive) |

### 5.2. Ngoài phạm vi (v1.0)

- ❌ Native mobile apps
- ❌ Billing self-serve nâng cao cho Enterprise
- ❌ AI auto-prioritization full tự động

### 5.3. Giả định (Assumptions)

1. Team sản phẩm chấp nhận public portal là kênh chính để gom feedback mới.
2. Workspace ban đầu có thể đạt time-to-value tốt nếu import được feedback từ CSV.
3. Customer Success sẵn sàng dùng status updates như một phần của communication workflow.

### 5.4. Ràng buộc (Constraints)

1. MVP phải ra trong 8 sprint.
2. Chỉ có 1 designer part-time và 1 data engineer hỗ trợ.
3. Portal public phải support custom branding ở mức logo + màu chính, không làm white-label full.

---

## 6. Bối cảnh cạnh tranh

| Đối thủ | Ưu điểm của họ | Nhược điểm của họ | Khác biệt của chúng ta |
|---------|---------------|------------------|------------------------|
| Canny | Portal + changelog rất rõ | Giá cao với team nhỏ | Onboarding nhẹ hơn, triage nhanh hơn |
| Productboard | Prioritization mạnh | Quá nặng với startup nhỏ | Tập trung vào feedback-to-action loop ngắn |
| Trello/Notion tự chế | Linh hoạt, rẻ | Không có public portal, no feedback loop | Có workflow chuyên biệt cho feedback |

---

## 7. Mô hình doanh thu

| Gói dịch vụ | Giá | Tính năng | Đối tượng phù hợp |
|-------------|------|----------|--------------------|
| Free / Trial | 0 USD | 1 workspace, 100 feedback items, portal cơ bản | Team mới |
| Pro | 79 USD/tháng | Unlimited feedback, duplicate merge, release notes, analytics cơ bản | Startup B2B |
| Business | 249 USD/tháng | Nhiều workspace, advanced permissions, SLA support | Scale-up |

---

## 8. Kế hoạch phát hành theo giai đoạn

```
Phase 1 — MVP (Sprint 1-4):
├── Workspace onboarding
├── Public feedback portal
└── Feedback inbox + basic status

Phase 2 — Workflow (Sprint 5-8):
├── Duplicate merge & triage
├── Status notification
└── Release notes feed

Phase 3 — Growth (Sprint 9-12):
├── Analytics dashboard
├── Billing upgrades
└── Workflow automation
```

---

## 9. Thước đo thành công (Mô hình AARRR)

| Giai đoạn | Thước đo | Công cụ | Chỉ tiêu (3 tháng) |
|-----------|----------|---------|---------------------|
| **Thu hút (Acquisition)** | Workspace signups / tuần | GA4 / Mixpanel | 250 |
| **Kích hoạt (Activation)** | Hoàn tất onboarding, portal published | Mixpanel | 55% |
| **Giữ chân (Retention)** | Weekly active workspaces | Amplitude | 45% |
| **Doanh thu (Revenue)** | MRR, free-to-pro conversion | Stripe / Nội bộ | 18.000 USD |
| **Lan tỏa (Referral)** | NPS, share rate release note | Khảo sát / Mixpanel | NPS ≥ 35 |

---

## 10. Rủi ro dự kiến

| # | Rủi ro | Xác suất | Tác động | Giải pháp giảm thiểu |
|---|--------|----------|----------|----------------------|
| 1 | Người dùng không import feedback cũ nên không thấy giá trị | Cao | Rất cao | Ưu tiên CSV import + sample data |
| 2 | Public portal bị spam | Trung bình | Cao | Rate limit, email verification |
| 3 | Duplicate merge sai làm mất trust | Trung bình | Cao | Chỉ gợi ý merge, không auto-merge bắt buộc |
| 4 | Activation tốt nhưng không chuyển đổi trả phí | Trung bình | Cao | Gate Pro đúng chỗ, prove value bằng notification + release notes |
| 5 | Data model không đủ cho analytics sau này | Thấp | Cao | Thiết kế event naming và entity model từ đầu |

---

## 11. Phê duyệt

| Vai trò | Họ tên | Chữ ký | Ngày |
|---------|--------|--------|------|
| Giám đốc Sản phẩm (Product Lead) | | | |
| Trưởng phòng Kỹ thuật (CTO) | | | |
| Chuyên viên phân tích (BA) | | | |
