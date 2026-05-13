# TẦM NHÌN & PHẠM VI — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Tác giả:** [Tên BA — Nhà cung cấp] | **Trạng thái:** Draft
> **Khách hàng:** [Tên công ty khách hàng]
> **Nhà cung cấp:** [Tên công ty phát triển]
> **Hợp đồng tham chiếu:** [Số hợp đồng]

---

## 1. Giới thiệu

### 1.1. Mục đích tài liệu
Tài liệu này xác định tầm nhìn, phạm vi và mục tiêu của dự án **[Tên dự án]**, được ký kết giữa **[Khách hàng]** và **[Nhà cung cấp]** theo Hợp đồng số **[HĐ-ID]**. Đây là tài liệu **Chốt phạm vi (Baseline)** — mọi thay đổi phạm vi sau khi phê duyệt sẽ được xử lý qua quy trình Yêu cầu thay đổi (CR).

### 1.2. Bối cảnh dự án
- **Tên Khách hàng:** [Công ty ABC]
- **Ngành:** [Fintech / Y tế / Thương mại điện tử / ...]
- **Vấn đề cần giải quyết:** [Mô tả vấn đề kinh doanh]
- **Giải pháp đề xuất:** [Tóm tắt giải pháp kỹ thuật]

### 1.3. Tài liệu liên quan

| Tài liệu | Mã | Trạng thái |
|-----------|----|-----------| 
| Hợp đồng | HĐ-[ID] | Đã ký |
| Thỏa thuận bảo mật (NDA) | NDA-[ID] | Đã ký |
| Yêu cầu đề xuất (RFP/RFQ) | — | Đã nhận |

### 1.4. Thuật ngữ

| Thuật ngữ | Giải thích |
|-----------|------------|
| KH | Khách hàng / Bên A — chủ sở hữu sản phẩm |
| NCC | Nhà cung cấp / Bên B — đội outsource |
| PO | Người đại diện Khách hàng (Product Owner) — người ra quyết định về yêu cầu |
| CR | Yêu cầu thay đổi — phát sinh ngoài phạm vi ban đầu, có ảnh hưởng chi phí |
| HĐ | Hợp đồng — văn bản pháp lý quy định phạm vi công việc và điều khoản |
| Baseline | Bản chốt phạm vi — phiên bản tài liệu đã được phê duyệt, làm cơ sở cho mọi thay đổi |

---

## 2. Tầm nhìn sản phẩm

> **"[Mô tả tầm nhìn sản phẩm — viết 2-3 câu: sản phẩm gì, cho ai, giải quyết vấn đề gì, khác biệt gì]"**
>
> _Ví dụ: "Xây dựng nền tảng quản lý kho hàng trực tuyến, giúp doanh nghiệp SME theo dõi tồn kho thời gian thực, giảm 50% thời gian kiểm kê và tích hợp với các sàn TMĐT phổ biến."_

---

## 3. Mục tiêu dự án

| # | Mục tiêu | Chỉ số đo lường | Chỉ tiêu | Thời hạn |
|---|----------|-----------------|----------|----------|
| 1 | [Mục tiêu 1] | [Chỉ số] | [Giá trị] | [Ngày] |
| 2 | [Mục tiêu 2] | [Chỉ số] | [Giá trị] | [Ngày] |
| 3 | [Mục tiêu 3] | [Chỉ số] | [Giá trị] | [Ngày] |

**Tiêu chí thành công:**
1. Nghiệm thu đạt ≥ 95% kịch bản kiểm thử
2. Vận hành đúng thời hạn ± 2 tuần
3. 0 lỗi Nghiêm trọng/Chặn tại thời điểm vận hành
4. Điểm hài lòng Khách hàng ≥ 4/5

---

## 4. Phạm vi dự án

### 4.1. Trong phạm vi

> ⚠️ **CHỈ những hạng mục dưới đây nằm trong hợp đồng và ngân sách đã thỏa thuận.**

#### Nhóm chức năng 1: [Tên Module]
- Tính năng 1.1: [Mô tả]
- Tính năng 1.2: [Mô tả]
- Tính năng 1.3: [Mô tả]

#### Nhóm chức năng 2: [Tên Module]
- Tính năng 2.1: [Mô tả]
- Tính năng 2.2: [Mô tả]

#### Nhóm chức năng 3: [Tên Module]
- Tính năng 3.1: [Mô tả]
- Tính năng 3.2: [Mô tả]

### 4.2. Ngoài phạm vi

> ⚠️ **Các hạng mục dưới đây KHÔNG nằm trong hợp đồng. Nếu Khách hàng yêu cầu thêm, cần thông qua quy trình CR với đánh giá chi phí & tiến độ.**

- ❌ [Hạng mục 1] — ví dụ: Ứng dụng di động native
- ❌ [Hạng mục 2] — ví dụ: Chuyển đổi dữ liệu cũ
- ❌ [Hạng mục 3] — ví dụ: Tích hợp bên thứ 3 ngoài danh sách
- ❌ [Hạng mục 4] — ví dụ: Đào tạo người dùng cuối (KH tự thực hiện)
- ❌ Bảo trì/vận hành sau kỳ bảo hành

### 4.3. Giả định

| # | Giả định | Rủi ro nếu sai | Biện pháp |
|---|----------|----------------|-----------|
| A1 | KH cung cấp tài liệu API hệ thống cũ trong 2 tuần đầu | Trì hoãn tích hợp | Báo cáo cấp trên sớm |
| A2 | KH bổ nhiệm PO sẵn sàng ≥ 4 giờ/ngày | Trì hoãn quyết định | PO dự phòng |
| A3 | Môi trường kiểm thử do KH cung cấp | Trì hoãn kiểm thử | NCC tự thiết lập |
| A4 | Nội dung (văn bản, hình ảnh) do KH cung cấp | Hiển thị tạm ở demo | Ghi rõ trong Báo cáo Sprint |
| A5 | API bên thứ 3 (cổng thanh toán, SMS...) có môi trường sandbox | Không thể kiểm thử tích hợp | Giả lập API |

### 4.4. Ràng buộc

| # | Ràng buộc | Loại |
|---|-----------|------|
| C1 | Ngân sách: [Theo hợp đồng] | Tài chính |
| C2 | Thời hạn: Vận hành trước [ngày] | Tiến độ |
| C3 | Công nghệ: [React/Node.js/PostgreSQL...] — theo thỏa thuận | Kỹ thuật |
| C4 | Hạ tầng: [AWS/Azure/Hạ tầng KH] | Hạ tầng |
| C5 | Tuân thủ: [GDPR/PCI-DSS/Quy định Bộ TT&TT...] | Pháp lý |
| C6 | Ngôn ngữ: Giao diện tiếng Việt, mã nguồn + tài liệu kỹ thuật tiếng Anh | Bản địa hóa |

### 4.5. Phụ thuộc

| # | Phụ thuộc vào | Phụ trách | Thời hạn | Trạng thái |
|---|-------------|-----------|----------|-----------|
| D1 | Tài liệu API hệ thống cũ | CNTT KH | Tuần 2 | ⏳ Chờ |
| D2 | Bộ nhận diện thương hiệu, logo, tài nguyên | Marketing KH | Tuần 3 | ⏳ Chờ |
| D3 | Thiết lập máy chủ staging | CNTT KH / DevOps NCC | Tuần 4 | ⏳ Chờ |
| D4 | Tài khoản thử nghiệm bên thứ 3 | KH | Tuần 4 | ⏳ Chờ |

---

## 5. Các bên liên quan chính

### Phía Khách hàng

| Vai trò | Tên | Trách nhiệm | Sẵn sàng |
|---------|-----|-------------|----------|
| Nhà tài trợ (Sponsor) | [Tên] | Phê duyệt, quyết định | Khi cần báo cáo cấp trên |
| Người đại diện KH (PO) | [Tên] | Quyết định yêu cầu, ưu tiên, nghiệm thu | ≥ 4 giờ/ngày |
| Chuyên gia nghiệp vụ (SME) | [Tên] | Giải đáp nghiệp vụ chuyên sâu | 2-3 giờ/tuần |
| Đầu mối CNTT | [Tên] | API, hạ tầng, triển khai | Khi cần |

### Phía Nhà cung cấp

| Vai trò | Tên | Trách nhiệm |
|---------|-----|-------------|
| Quản lý dự án (PM) | [Tên] | Quản lý tiến độ, ngân sách, rủi ro |
| Trưởng nhóm Phân tích (BA Lead) | [Tên] | Phân tích yêu cầu, tài liệu |
| Trưởng nhóm Kỹ thuật (Tech Lead) | [Tên] | Kiến trúc, rà soát mã nguồn |
| Đội phát triển | [N người] | Lập trình, phát triển |
| Trưởng nhóm Kiểm thử (QC Lead) | [Tên] | Kiểm thử, hỗ trợ nghiệm thu |

---

## 6. Kế hoạch phát hành

```
Giai đoạn 1 (MVP) — Sprint 1-4 (2 tháng):
├── Module 1: [Tính năng cốt lõi]
├── Module 2: [Tính năng phụ]
└── 💰 Mốc M2: Nghiệm thu Phiên bản 1 → Thanh toán 25%

Giai đoạn 2 — Sprint 5-8 (2 tháng):
├── Module 3: [Tính năng bổ sung]
├── Module 4: [Tính năng tích hợp]
└── 💰 Mốc M3: Nghiệm thu Phiên bản đầy đủ → Thanh toán 25%

Giai đoạn 3 — Vận hành + Bảo hành (1 tháng):
├── Triển khai sản xuất
├── Sửa lỗi (bảo hành)
└── 💰 Mốc M4: Hết bảo hành → Thanh toán 15%
```

---

## 7. Rủi ro ban đầu

| # | Rủi ro | Xác suất | Tác động | Chịu TN | Biện pháp giảm thiểu |
|---|--------|----------|----------|---------|----------------------|
| R1 | PO KH không sẵn sàng → trì hoãn quyết định | Cao | Cao | KH | PO dự phòng, quyết định qua email |
| R2 | Phát sinh yêu cầu ngoài phạm vi (Scope creep) | Cao | Cao | PM | Quy trình Yêu cầu thay đổi (CR), Chốt phạm vi (Baseline) |
| R3 | API hệ thống cũ không đúng tài liệu | Trung bình | Cao | NCC | Thử nghiệm tích hợp sớm (Giai đoạn 1) |
| R4 | Lệch múi giờ gây hiểu sai | Trung bình | Trung bình | PM | Trùng 4 giờ, tài liệu hóa bất đồng bộ |
| R5 | Nhân sự chủ chốt nghỉ/chuyển nhóm | Thấp | Cao | PM | Chia sẻ kiến thức, làm cặp |
| R6 | Thay đổi yêu cầu kỹ thuật muộn | Thấp | Cao | BA | Chốt phạm vi (Baseline) sớm, phát sinh qua quy trình CR |

---

## 8. Phê duyệt

> ⚠️ **Tài liệu này sau khi phê duyệt sẽ trở thành BẢN CHỐT PHẠM VI (Baseline). Mọi thay đổi phạm vi phải thông qua quy trình Yêu cầu thay đổi (CR).**

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Nhà tài trợ (Sponsor) | Khách hàng | | | |
| Người đại diện KH (Product Owner) | Khách hàng | | | |
| Quản lý dự án (PM) | Nhà cung cấp | | | |
| Trưởng nhóm Phân tích (BA Lead) | Nhà cung cấp | | | |

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Người |
|-----------|------|----------|-------|
| 0.1 | [Ngày] | Draft đầu tiên | BA |
| 0.2 | [Ngày] | Cập nhật theo phản hồi KH | BA |
| 1.0 | [Ngày] | **Đã phê duyệt — Chốt phạm vi** | BA |
