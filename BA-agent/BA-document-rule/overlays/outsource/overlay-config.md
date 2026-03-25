# OVERLAY: OUTSOURCE PROJECT

> **Áp dụng:** Dự án thuê ngoài, quan hệ Khách hàng – Nhà cung cấp
> **Đặc điểm:** Tài liệu chính thống, ràng buộc hợp đồng, sign-off bắt buộc, giao tiếp từ xa

---

## 1. Tài liệu bắt buộc vs Tùy chọn

| # | Tài liệu | Bắt buộc? | Mức chi tiết | Ghi chú |
|---|----------|----------|-------------|---------|
| 1 | Vision & Scope | ✅ Bắt buộc | **Cao — Khách hàng sign-off** | Baseline cho scope |
| 2 | BRD | ✅ **Bắt buộc** | **Cao** | Cơ sở cho hợp đồng + ước lượng |
| 3 | Stakeholder Map | ✅ Bắt buộc | **Cao — cả 2 bên** | KH + NCC, kèm Communication Protocol |
| 4 | Process Flow | ✅ Bắt buộc | Cao | As-Is + To-Be + Gap Analysis |
| 5 | SRS | ✅ **Bắt buộc** | **Cao (15-25 trang)** | Dev không ngồi cạnh → phải rõ ràng |
| 6 | User Story Map | ✅ Bắt buộc | **Cao — baseline signed** | Story Map = scope agreement |
| 7 | Data Model | ✅ Bắt buộc | **Cao + API Spec** | Kèm Swagger/OpenAPI |
| 8 | UAT Plan | ✅ **Bắt buộc** | **Cao — formal** | Biên bản nghiệm thu gắn với thanh toán |
| 9 | Change Log | ✅ **Bắt buộc** | **Cao** | CR = ảnh hưởng chi phí/hợp đồng |
| 10 | Meeting Minutes | ✅ **Bắt buộc** | **Cao — GHI HÌNH** | Bằng chứng pháp lý |
| 11 | Handover Checklist | ✅ **Bắt buộc** | **Cao** | Bàn giao code + tài liệu + knowledge |
| 12 | API Specification | ✅ Bắt buộc | **Cao — Swagger** | Formal API docs |

---

## 2. Phase bổ sung: TIỀN DỰ ÁN & HỢP ĐỒNG (Phase 0)

> Phase không có trong quy trình generic — đặc thù outsource.

```
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│ TIỀN DỰ ÁN │──▶│ KHỞI ĐỘNG  │──▶│  KHÁM PHÁ  │──▶│ CHI TIẾT   │──▶│ PHÁT TRIỂN │──▶│  KẾT THÚC  │
│ & HỢP ĐỒNG │   │  (2 tuần)  │   │ (2-3 tuần) │   │ (2-3 tuần) │   │ (N Sprint) │   │ (2-3 tuần) │
└────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘
```

### Hoạt động Phase 0

| Hoạt động | Output | Người phụ trách |
|-----------|--------|----------------|
| Tiếp nhận RFP/RFQ từ Khách hàng | Phân tích yêu cầu | Sales + BA |
| Khảo sát sơ bộ yêu cầu | Yêu cầu tổng quan | BA |
| Ước lượng khối lượng (ROM) | Bảng ước lượng | BA + Tech Lead |
| Soạn Đề xuất | Proposal + BRD (draft) | PM + BA |
| Đàm phán & ký hợp đồng | Hợp đồng đã ký | PM + Pháp lý |

---

## 3. Điều chỉnh quy trình

### Thời lượng

| Phase | Outsource | So với In-house |
|-------|----------|----------------|
| Phase 0 (Tiền dự án) | 1-4 tuần | **Mới — không có ở in-house** |
| Inception | 2 tuần | +1 tuần (onboarding, DoD, NDA) |
| Discovery | 2-3 tuần | Giữ nguyên |
| Elaboration | 2-3 tuần | **+1 tuần** (SRS chi tiết hơn) |
| Delivery | N Sprints | Giữ nguyên |
| Closure | **2-3 tuần** | **+1-2 tuần** (bàn giao code, bảo hành) |

### ⚠️ 5 Quy tắc vàng Outsource

1. **Mọi thay đổi = CR chính thức** → có ảnh hưởng chi phí/tiến độ
2. **Mọi quyết định = email/văn bản** → không bao giờ chỉ nói miệng
3. **Mọi workshop = GHI HÌNH** → tránh "tôi không nói vậy"
4. **Biên bản họp gửi trong 24 giờ** → KH phải confirm
5. **Báo cáo Sprint = bắt buộc** → KH biết tiền đang được dùng thế nào

---

## 4. Payment Milestone — Gắn với Deliverables

| Mốc | % | Điều kiện |
|------|---|----------|
| M0: Ký hợp đồng | 20% | Hợp đồng đã ký |
| M1: Sign-off SRS | 15% | KH sign-off SRS + Data Model |
| M2: Demo MVP (Release 1) | 25% | UAT pass Release 1 |
| M3: Release đầy đủ | 25% | UAT pass toàn bộ |
| M4: Hết bảo hành | 15% | 30-90 ngày không lỗi nghiêm trọng |

---

## 5. Communication Protocol

| Kênh | Mục đích | SLA phản hồi |
|------|---------|-------------|
| **Jira** | Tracking công việc, bug, CR | 24 giờ |
| **Slack/Teams** | Hỏi đáp nhanh | 4 giờ (giờ hành chính) |
| **Email** | Quyết định chính thức, sign-off | 24 giờ |
| **Video Call** | Sprint events, workshop, demo | Đúng giờ |
| **Confluence** | Tài liệu, wiki | Cập nhật liên tục |

**Quy tắc múi giờ:** Trùng ít nhất **4 giờ/ngày** giữa KH và NCC.

---

## 6. Phase Gate bổ sung

### Tiền dự án → Khởi động
- [ ] Hợp đồng đã ký bởi cả 2 bên
- [ ] NDA đã ký
- [ ] Nhóm dự án phân công (cả KH + NCC)
- [ ] Kênh giao tiếp đã thiết lập
- [ ] Thanh toán M0 ✅

### Closure bổ sung
- [ ] Bàn giao mã nguồn
- [ ] Bàn giao tài liệu kỹ thuật
- [ ] Knowledge Transfer sessions (ghi hình)
- [ ] Biên bản nghiệm thu đã ký
- [ ] Thanh toán M3 ✅
- [ ] Bắt đầu bảo hành
