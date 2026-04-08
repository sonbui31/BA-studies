# QUY TRÌNH BA — DỰ ÁN OUTSOURCE
# (Kết hợp: Agile + Tài liệu chính thống)

> **Phương pháp:** Quy trình BA kết hợp cho dự án Outsource
> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Đặc thù:** Quan hệ Khách hàng – Nhà cung cấp, ràng buộc hợp đồng, làm việc từ xa

---

## 1. Tổng quan — Outsource khác gì In-house?

| Yếu tố | In-house | Outsource |
|---------|----------|-----------|
| Quan hệ | Nội bộ, linh hoạt | Hợp đồng, pháp lý ràng buộc |
| Giao tiếp | Ngồi cạnh, hỏi luôn | Từ xa, lệch múi giờ, họp theo lịch |
| Tài liệu | Vừa đủ, linh hoạt | **Phải chính thống**, chốt phạm vi (baseline) + phê duyệt |
| Thay đổi yêu cầu | Dễ, nhanh | Yêu cầu thay đổi (CR) có **ảnh hưởng chi phí**, cần phê duyệt |
| Nghiệm thu | Demo + phản hồi | **Nghiệm thu UAT chính thức** + Biên bản nghiệm thu + thanh toán |
| Rủi ro chính | Phát sinh yêu cầu ngoài phạm vi | Hiểu sai yêu cầu, kỳ vọng lệch, phụ thuộc nhà cung cấp |

---

## 2. Quy trình BA — 6 Giai đoạn

```
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│ TIỀN DỰ ÁN │──▶│ KHỞI ĐỘNG  │──▶│  KHÁM PHÁ  │──▶│ CHI TIẾT   │──▶│ PHÁT TRIỂN │──▶│  KẾT THÚC  │
│ & HỢP ĐỒNG │   │ (2 tuần)   │   │ (2-3 tuần) │   │ (2-3 tuần) │   │ (N Sprint) │   │ (2-3 tuần) │
└────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘
```

---

### Giai đoạn 0: TIỀN DỰ ÁN & HỢP ĐỒNG (Trước dự án)

**Mục tiêu:** Hiểu sơ bộ yêu cầu, ước lượng, ký hợp đồng.

| Hoạt động | Kết quả đầu ra | Người phụ trách |
|-----------|----------------|----------------|
| Tiếp nhận yêu cầu từ Khách hàng (RFP/RFQ) | Phân tích yêu cầu | Kinh doanh + BA |
| Khảo sát sơ bộ yêu cầu | Yêu cầu tổng quan | BA |
| Ước lượng khối lượng (ROM) | Bảng ước lượng | BA + Tech Lead |
| Soạn Đề xuất | Đề xuất + BRD (draft) | PM + BA |
| Đàm phán & ký hợp đồng | Hợp đồng đã ký | PM + Pháp lý |

**Sản phẩm bàn giao:**
- `02-BRD.md` (draft) ← **Luận chứng kinh doanh cho Khách hàng phê duyệt**
- Bảng ước lượng (ROM)
- Thỏa thuận bảo mật (NDA) nếu chưa có

**BA cần lưu ý:**
- ⚠️ **KHÔNG ước lượng khi chưa hiểu rõ yêu cầu** → đề xuất giai đoạn Khám phá có trả phí
- ⚠️ Hợp đồng phải ghi rõ: phạm vi, ngoại trừ, giả định, quy trình thay đổi, mốc thanh toán

---

### Giai đoạn 1: KHỞI ĐỘNG — 2 tuần

**Giống In-house + thêm:**

| Hoạt động đặc thù Outsource | Kết quả đầu ra |
|-------------------------------|----------------|
| Họp giới thiệu (Khách hàng + Nhà cung cấp) | Giới thiệu nhóm, quy ước giao tiếp |
| Thiết lập kênh giao tiếp | Kênh Slack/Teams, Confluence, dự án Jira |
| Thống nhất Tiêu chí hoàn thành (DoD) | Tài liệu DoD |
| Thống nhất tần suất báo cáo | Mẫu báo cáo tuần |
| Thỏa thuận bảo mật & sở hữu trí tuệ | NDA đã ký |

**Sản phẩm bàn giao:**
- `01-Vision-Scope.md` (Khách hàng phê duyệt bắt buộc)
- `03-Stakeholder-Map.md` (cả 2 bên: Khách hàng + Nhà cung cấp)
- `04-Process-Flow.md`
- Quy ước giao tiếp

**Điều kiện chuyển giai đoạn:** Khách hàng phê duyệt Tầm nhìn & Phạm vi + BRD đã chốt phạm vi (baseline)

---

### Giai đoạn 2: KHÁM PHÁ — 2-3 tuần

**Giống In-house + thêm:**

| Hoạt động đặc thù Outsource | Kết quả đầu ra |
|-------------------------------|----------------|
| Workshop từ xa (video call + Miro) | User Story Map |
| Trình bày prototype với Khách hàng | Phiên ghi hình + phản hồi |
| Gửi prototype cho Khách hàng xem offline (2-3 ngày) | Phản hồi bằng văn bản |
| Phê duyệt chính thức phạm vi bản đồ câu chuyện | Bản đồ câu chuyện đã chốt phạm vi (baseline) và ký |

**⚠️ Mẹo Outsource:**
- Mọi workshop **phải ghi hình** (video/âm thanh) → tránh "tôi không nói vậy" sau này
- Gửi **Biên bản họp trong vòng 24 giờ** → Khách hàng xác nhận qua email
- Prototype phải **bấm được** (không chỉ hình tĩnh) vì từ xa khó giải thích

---

### Giai đoạn 3: CHI TIẾT HÓA — 2-3 tuần

**Outsource cần SRS đầy đủ hơn In-house:**

| Tài liệu | In-house (Rút gọn) | Outsource (Đầy đủ) |
|-----------|---------------------|---------------------|
| SRS | 5-8 trang | **15-25 trang** (vì Dev không ngồi cạnh để hỏi) |
| Wireframe | Phác thảo đơn giản | **Trung bình trở lên** (ít mơ hồ) |
| Mô hình dữ liệu | Thực thể cốt lõi | **Đầy đủ thực thể** + đặc tả API |
| Đặc tả API | Thỏa thuận miệng | **Swagger/OpenAPI chính thức** |

**Sản phẩm bàn giao:**
- `05-SRS.md` → chi tiết hơn bản in-house
- `06-User-Story-Map.md` (đã chốt phạm vi và ký)
- `07-Data-Model.md` + Đặc tả API

**Điều kiện chuyển giai đoạn:** Khách hàng phê duyệt SRS → đây là **bản chốt phạm vi (baseline)** cho theo dõi CR

---

### Giai đoạn 4: PHÁT TRIỂN — N Sprint

**BA trong Sprint outsource:**

```
Dòng thời gian Sprint (2 tuần):
────────────────────────────────────────────────

Ngày 1: Lập kế hoạch Sprint
├── BA trình bày các story đã phân tích
├── Đội Dev ước lượng (story points)
└── Cam kết khối lượng sprint

Ngày 2-8: Thực hiện
├── BA sẵn sàng 1-2 giờ/ngày cho giải đáp (khung giờ cố định)
├── BA phân tích story cho Sprint tiếp theo
├── Đồng bộ với PO Khách hàng (2 lần/tuần)
└── ⚠️ Mọi giải đáp phải GHI CHÉP (email/bình luận Jira)

Ngày 9: Đánh giá Sprint/Demo
├── Demo cho Khách hàng (video call, GHI HÌNH)
├── Phản hồi Khách hàng → phân loại: lỗi vs CR
├── Lỗi → sửa trong Sprint tiếp
└── CR → vào Nhật ký thay đổi → đánh giá chi phí

Ngày 10: Rút kinh nghiệm + Phân tích trước
├── Rút kinh nghiệm nội bộ (đội Nhà cung cấp)
├── Gửi Báo cáo Sprint cho Khách hàng
└── Phân tích Sprint tiếp

Báo cáo tuần cho Khách hàng:
├── Tiến độ: hoàn thành/đang làm/bị chặn
├── Chỉ số: tốc độ, burndown chart
├── Rủi ro & Vấn đề
├── Tình trạng CR
└── Kế hoạch sprint tiếp
```

**⚠️ Quy tắc vàng Outsource:**
1. **Mọi thay đổi yêu cầu = Yêu cầu thay đổi (CR)** → có ảnh hưởng chi phí/tiến độ
2. **Mọi quyết định = email/văn bản** → không chỉ nói miệng
3. **Báo cáo Sprint = bắt buộc** → Khách hàng phải biết tiền đang được dùng thế nào

---

### Giai đoạn 5: KẾT THÚC — 2-3 tuần (dài hơn in-house)

```
Tuần 1: Nghiệm thu (UAT)
├── BA chuẩn bị Kịch bản kiểm thử
├── Khách hàng chạy UAT (BA hỗ trợ)
├── Theo dõi lỗi → sửa → kiểm thử lại
└── Báo cáo UAT

Tuần 2: Bàn giao & Chuyển giao kiến thức
├── Bàn giao mã nguồn                          ← ĐẶC THÙ OUTSOURCE
├── Bàn giao tài liệu kỹ thuật
├── Hướng dẫn quản trị + Hướng dẫn sử dụng
├── Các buổi chuyển giao kiến thức (ghi hình)
├── Hỗ trợ triển khai sản xuất
└── Thông tin đăng nhập môi trường sản xuất

Tuần 3: Phê duyệt & Bảo hành
├── Ký Biên bản nghiệm thu
├── Thanh toán mốc cuối
├── Bắt đầu thời gian bảo hành (30-90 ngày)
├── Quy trình hỗ trợ cho bảo hành
└── Rút kinh nghiệm dự án
```

---

## 3. Ma trận RACI — Hồ sơ BA cho Outsource

| Hồ sơ | BA (NCC) | PM (NCC) | PO (KH) | Nhà tài trợ (KH) | Dev Lead |
|--------|----------|----------|---------|---------------------|-----------------|
| BRD / Hợp đồng | C | **R** | **A** | **A** | C |
| Tầm nhìn & Phạm vi | **R** | A | **A** | **A** | I |
| Stakeholder Map | **R/A** | I | C | — | — |
| Quy trình nghiệp vụ | **R** | I | **A** | I | C |
| SRS | **R** | A | **A** | I | **C** |
| Story Map | **R** | C | **A** | I | C |
| Mô hình dữ liệu | **R** | I | C | — | **A** |
| Kế hoạch UAT | **R** | A | **A** | A | C |
| Nhật ký thay đổi | **R** | **A** | **A** | I | C |
| Báo cáo Sprint | C | **R** | I | I | C |
| Bộ tài liệu bàn giao | **R** | **A** | **A** | A | R |

> **R** = Thực hiện, **A** = Phê duyệt, **C** = Tham vấn, **I** = Thông báo
> **NCC** = Nhà cung cấp, **KH** = Khách hàng
> ⚠️ Khách hàng luôn **Phê duyệt** tài liệu chính thức (khác biệt lớn nhất so với nội bộ)

---

## 4. Quy ước Giao tiếp — Outsource

| Kênh | Mục đích | Tần suất | SLA phản hồi |
|------|----------|----------|-------------|
| **Jira** | Theo dõi công việc, lỗi, CR | Liên tục | 24 giờ |
| **Slack/Teams** | Hỏi đáp nhanh, làm rõ | Giờ làm việc | 4 giờ (giờ hành chính) |
| **Email** | Quyết định chính thức, phê duyệt, báo cáo cấp trên | Khi cần | 24 giờ |
| **Video Call** | Sự kiện Sprint, workshop, demo | Theo lịch | Đúng giờ |
| **Confluence** | Tài liệu, wiki, cơ sở tri thức | Cập nhật liên tục | — |

**Quy tắc múi giờ:**
- Trùng ít nhất **4 giờ/ngày** giữa Khách hàng và Nhà cung cấp
- Các cuộc họp quan trọng đặt trong khung giờ trùng

---

## 5. Mốc thanh toán — Gắn với Sản phẩm bàn giao

| Mốc | % Thanh toán | Điều kiện |
|------|-------------|-----------|
| M0: Ký hợp đồng | 20% | Hợp đồng đã ký |
| M1: Phê duyệt SRS | 15% | Khách hàng phê duyệt SRS + Mô hình dữ liệu |
| M2: Demo MVP (Phiên bản 1) | 25% | Nghiệm thu đạt Phiên bản 1 |
| M3: Phiên bản đầy đủ | 25% | Nghiệm thu đạt toàn bộ |
| M4: Vận hành + Hết bảo hành | 15% | Hết bảo hành, không còn lỗi nghiêm trọng |

---

## 6. Danh mục kiểm tra chuyển giai đoạn — Outsource

### Tiền dự án → Khởi động
- [ ] Hợp đồng đã ký bởi cả 2 bên
- [ ] NDA đã ký
- [ ] Nhóm dự án đã phân công (cả Khách hàng + Nhà cung cấp)
- [ ] Kênh giao tiếp đã thiết lập

### Khởi động → Khám phá
- [ ] Tầm nhìn & Phạm vi **đã được Khách hàng phê duyệt**
- [ ] Stakeholder Map hoàn thành
- [ ] Quy trình hiện tại (As-Is) đã được ghi nhận
- [ ] Thanh toán M0 đã nhận ✅

### Khám phá → Chi tiết hóa
- [ ] Bản đồ câu chuyện (User Story Map) **đã được Khách hàng phê duyệt chốt phạm vi**
- [ ] Prototype đã được người dùng cuối xác nhận
- [ ] Quy trình tương lai (To-Be) đã được xác nhận

### Chi tiết hóa → Phát triển
- [ ] SRS **đã được Khách hàng phê duyệt** (= bản chốt phạm vi yêu cầu)
- [ ] Mô hình dữ liệu đã được Dev Lead xem xét
- [ ] Nhịp Sprint đã thống nhất
- [ ] Thanh toán M1 đã nhận ✅

### Phát triển → Kết thúc
- [ ] Tất cả tính năng đã cam kết hoàn thành
- [ ] Kế hoạch UAT sẵn sàng
- [ ] Tài liệu bàn giao đã chuẩn bị
- [ ] Thanh toán M2 đã nhận ✅

### Kết thúc → Hoàn tất
- [ ] Biên bản nghiệm thu đã ký
- [ ] Mã nguồn & tài liệu đã bàn giao
- [ ] Chuyển giao kiến thức hoàn tất
- [ ] Thời gian bảo hành bắt đầu
- [ ] Thanh toán M3 đã nhận ✅
