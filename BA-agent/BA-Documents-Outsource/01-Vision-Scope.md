# TẦM NHÌN & PHẠM VI — DỰ ÁN OUTSOURCE
# Dự án Hệ thống Quản lý Tài sản Bệnh viện

> **Phiên bản:** 1.0 | **Ngày:** 10/02/2026
> **Tác giả:** Nguyễn Văn A — BA Lead, Nhà cung cấp | **Trạng thái:** Baseline 1.0 — đã ký mục 8 ngày 10/02/2026
> **Khách hàng:** Bệnh viện Đa khoa An Phúc
> **Nhà cung cấp:** Công ty Giải pháp Số Sao Việt
> **Hợp đồng tham chiếu:** HD-AP-2026-018
> **Nhãn:** [TÀI LIỆU MẪU] — ví dụ minh họa cấu trúc, không phải dự án thật

---

## 1. Giới thiệu

### 1.1. Mục đích tài liệu
Tài liệu này xác định tầm nhìn, phạm vi và mục tiêu của dự án **Hệ thống Quản lý Tài sản Bệnh viện**, ký giữa **Bệnh viện Đa khoa An Phúc** và **Công ty Giải pháp Số Sao Việt** theo Hợp đồng số **HD-AP-2026-018**. Bản 1.0 đã ký ở mục 8 và là bản chốt phạm vi (Baseline); mọi thay đổi phạm vi sau đó đi qua quy trình Yêu cầu thay đổi (CR). Chi tiết yêu cầu nằm ở `02-BRD.md`; số liệu chi phí và lợi ích lấy theo BRD mục 3.

### 1.2. Bối cảnh dự án
- **Tên Khách hàng:** Bệnh viện Đa khoa An Phúc (650 nhân sự, 420 giường, 18 khoa/phòng)
- **Ngành:** Y tế, bệnh viện tư nhân quy mô vừa, đang mở thêm cơ sở vệ tinh
- **Vấn đề cần giải quyết:** Tài sản y tế, thiết bị CNTT và vật tư giá trị cao được theo dõi bằng file Excel riêng của từng khoa. Kiểm kê tháng mất 24-30 giờ công và sai lệch trung bình 12%; điều chuyển giữa khoa không có xác nhận giao nhận; lịch bảo trì nằm trong email và sổ riêng của kỹ sư.
- **Giải pháp đề xuất:** Ứng dụng web quản lý tài sản tập trung: hồ sơ và mã barcode cho từng tài sản, điều chuyển có duyệt và hai bên xác nhận, kiểm kê theo đợt bằng quét barcode, cảnh báo bảo trì, dashboard cho Ban điều hành.

### 1.3. Tài liệu liên quan

| Tài liệu | Mã | Trạng thái |
|-----------|----|-----------|
| Hợp đồng | HD-AP-2026-018 | Đã ký 30/01/2026 |
| Thỏa thuận bảo mật (NDA) | NDA-AP-2026-004 | Đã ký 15/01/2026 |
| Yêu cầu báo giá (RFQ) của bệnh viện | RFQ-AP-2025-11 | Đã nhận 12/2025 |

### 1.4. Thuật ngữ

| Thuật ngữ | Giải thích |
|-----------|------------|
| KH | Khách hàng / Bên A — Bệnh viện Đa khoa An Phúc |
| NCC | Nhà cung cấp / Bên B — Công ty Giải pháp Số Sao Việt |
| PO | Người đại diện Khách hàng (Product Owner) — người ra quyết định về yêu cầu |
| CR | Yêu cầu thay đổi — phát sinh ngoài phạm vi ban đầu, có ảnh hưởng chi phí |
| HĐ | Hợp đồng — văn bản pháp lý quy định phạm vi công việc và điều khoản |
| Baseline | Bản chốt phạm vi — phiên bản tài liệu đã được phê duyệt, làm cơ sở cho mọi thay đổi |

---

## 2. Tầm nhìn sản phẩm

> **"Phòng Vật tư, các khoa và Ban điều hành của Bệnh viện An Phúc cùng dùng một danh mục tài sản: biết tài sản nào đang ở khoa nào, ai nhận bàn giao, khi nào đến hạn bảo trì. Kiểm kê tháng xong trong 1 ngày thay vì 3 ngày, và quy trình này dùng được ngay khi mở cơ sở vệ tinh."**

---

## 3. Mục tiêu dự án

| # | Mục tiêu | Chỉ số đo lường | Chỉ tiêu | Thời hạn |
|---|----------|-----------------|----------|----------|
| 1 | Chuẩn hóa danh mục và vòng đời tài sản toàn viện | % tài sản có mã định danh hợp lệ | ≥ 98% | 31/08/2026 |
| 2 | Rút ngắn quy trình kiểm kê tháng | Thời gian hoàn tất kiểm kê | ≤ 1 ngày làm việc | 30/09/2026 |
| 3 | Kiểm soát bảo trì và điều chuyển tài sản có SLA | % yêu cầu được xử lý đúng SLA | ≥ 95% | 31/10/2026 |

Ba mục tiêu này là O1-O3 của `02-BRD.md` mục 4.1.

**Tiêu chí thành công:**
1. Nghiệm thu đạt ≥ 95% kịch bản kiểm thử
2. Vận hành đúng thời hạn ± 2 tuần
3. 0 lỗi Nghiêm trọng/Chặn tại thời điểm vận hành
4. Điểm hài lòng Khách hàng ≥ 4/5

---

## 4. Phạm vi dự án

### 4.1. Trong phạm vi

> ⚠️ **CHỈ những hạng mục dưới đây nằm trong hợp đồng và ngân sách đã thỏa thuận.**

#### Nhóm chức năng 1: Danh mục và Đăng ký tài sản (HĐ 2.1)
- Tính năng 1.1: Tạo hồ sơ tài sản tập trung, gắn khoa sở hữu
- Tính năng 1.2: Sinh mã định danh và in tem barcode
- Tính năng 1.3: Danh mục khoa, nhóm tài sản và phân quyền theo vai trò

#### Nhóm chức năng 2: Điều chuyển, bàn giao và kiểm kê (HĐ 2.2)
- Tính năng 2.1: Điều chuyển tài sản giữa khoa có duyệt và hai bên xác nhận
- Tính năng 2.2: Kiểm kê theo đợt bằng quét barcode, phân loại và chốt chênh lệch

#### Nhóm chức năng 3: Bảo trì và Báo cáo điều hành (HĐ 2.3)
- Tính năng 3.1: Lịch bảo trì định kỳ, cảnh báo đến hạn bảo trì và sắp hết thời gian sử dụng
- Tính năng 3.2: Dashboard điều hành theo khoa, trạng thái, giá trị

Chuyển đổi dữ liệu từ file Excel của các khoa và đào tạo người dùng nằm trong phạm vi (`02-BRD.md` mục 3.2).

### 4.2. Ngoài phạm vi

> ⚠️ **Các hạng mục dưới đây KHÔNG nằm trong hợp đồng. Nếu Khách hàng yêu cầu thêm, cần thông qua quy trình CR với đánh giá chi phí & tiến độ.**

- ❌ Tích hợp ERP kế toán (giai đoạn 1 chỉ xuất file đối chiếu)
- ❌ Ứng dụng di động offline đầy đủ
- ❌ Tự động nhận dạng tài sản bằng AI/camera
- ❌ Lập và duyệt hồ sơ thanh lý; hệ thống chỉ ghi trạng thái và cảnh báo
- ❌ Bảo trì/vận hành sau kỳ bảo hành (ký hợp đồng bảo trì riêng, `02-BRD.md` mục 3.2 dòng 6)

### 4.3. Giả định

| # | Giả định | Rủi ro nếu sai | Biện pháp |
|---|----------|----------------|-----------|
| A1 | Mỗi khoa cử 1 đầu mối xác nhận dữ liệu tài sản | Chậm chuẩn hóa dữ liệu, trễ chuyển đổi | Trưởng phòng Vật tư nhắc qua giao ban tuần |
| A2 | Danh mục tài sản hiện tại làm sạch được trong tối đa 8 tuần | Phạm vi chuyển đổi tăng, cần CR | Kiểm tra mẫu dữ liệu ở tuần 1 |
| A3 | KH bổ nhiệm PO sẵn sàng ≥ 4 giờ/ngày | Trì hoãn quyết định | PO dự phòng: Phó phòng Vật tư |
| A4 | CNTT KH cấp môi trường SSO thử nghiệm và VPN site-to-site trước tuần 4 | Trì hoãn kiểm thử tích hợp | Dùng tài khoản nội bộ của hệ thống trong lúc chờ |
| A5 | Bệnh viện có sẵn hoặc mua máy in tem barcode tương thích | Không in được tem khi go-live | Khảo sát máy in ở tuần 2 (INT-05) |

### 4.4. Ràng buộc

| # | Ràng buộc | Loại |
|---|-----------|------|
| C1 | Ngân sách phát triển tối đa 1,35 tỷ VND (giá cố định, `02-BRD.md` mục 4.5) | Tài chính |
| C2 | Go-live trước đợt kiểm kê Q4/2026 | Tiến độ |
| C3 | Ứng dụng web chạy trên trình duyệt; kiến trúc chốt với CNTT KH trong giai đoạn thiết kế | Kỹ thuật |
| C4 | Hạ tầng cloud của NCC, truy cập qua VPN site-to-site | Hạ tầng |
| C5 | Log bàn giao, bảo trì, kiểm kê lưu tối thiểu 5 năm theo quy chế kiểm soát nội bộ | Pháp lý / Tuân thủ |
| C6 | Ngôn ngữ: Giao diện tiếng Việt, mã nguồn + tài liệu kỹ thuật tiếng Anh | Bản địa hóa |

### 4.5. Phụ thuộc

| # | Phụ thuộc vào | Phụ trách | Thời hạn | Trạng thái |
|---|-------------|-----------|----------|-----------|
| D1 | Thông tin kết nối AD/SSO bệnh viện (INT-02) | CNTT KH | Tuần 2 | ⏳ Chờ |
| D2 | File Excel tài sản của 18 khoa, 6 đợt kiểm kê gần nhất | Phòng Vật tư | Tuần 1 | ✅ Đã nhận |
| D3 | VPN site-to-site và máy chủ staging | CNTT KH / DevOps NCC | Tuần 4 | ⏳ Chờ |
| D4 | Khảo sát máy in barcode (INT-05) | CNTT KH | Tuần 2 | ⏳ Chờ |

---

## 5. Các bên liên quan chính

Danh sách đầy đủ và vai trò trong quy trình: `03-Stakeholder-Map.md`.

### Phía Khách hàng

| Vai trò | Tên | Trách nhiệm | Sẵn sàng |
|---------|-----|-------------|----------|
| Nhà tài trợ (Sponsor) | Trần Minh Đức — Giám đốc vận hành | Phê duyệt, quyết định | Khi cần báo cáo cấp trên |
| Người đại diện KH (PO) | Phạm Thu Hà — Trưởng phòng Vật tư | Quyết định yêu cầu, ưu tiên, nghiệm thu | ≥ 4 giờ/ngày |
| Chuyên gia nghiệp vụ (SME) | Đặng Văn Hùng — Kỹ sư thiết bị y tế | Giải đáp nghiệp vụ bảo trì | 2-3 giờ/tuần |
| Đầu mối CNTT | Vũ Hoàng Nam — Trưởng phòng CNTT | SSO, VPN, hạ tầng, triển khai | Khi cần |

### Phía Nhà cung cấp

| Vai trò | Tên | Trách nhiệm |
|---------|-----|-------------|
| Quản lý dự án (PM) | Đỗ Thanh Tùng | Quản lý tiến độ, ngân sách, rủi ro |
| Trưởng nhóm Phân tích (BA Lead) | Nguyễn Văn A | Phân tích yêu cầu, tài liệu |
| Trưởng nhóm Kỹ thuật (Tech Lead) | Hoàng Gia Khánh | Kiến trúc, rà soát mã nguồn |
| Đội phát triển | 4 người | Lập trình, phát triển |
| Trưởng nhóm Kiểm thử (QC Lead) | Trịnh Thu Trang | Kiểm thử, hỗ trợ nghiệm thu |

---

## 6. Kế hoạch phát hành

Thời lượng theo `02-BRD.md` mục 9.1 (tổng 14 tuần); sprint theo `06-User-Story-Map.md` mục 3.

```
Khám phá & Thiết kế — 2 tuần:
└── Mốc M1: Phê duyệt đặc tả (SRS)

Giai đoạn 1 (MVP) — Sprint 1-4, 6 tuần:
├── Danh mục, đăng ký tài sản, barcode
├── Điều chuyển tài sản, kiểm kê theo đợt
├── Bảo trì, dashboard
└── 💰 Mốc M2: Nghiệm thu Phiên bản 1 → Thanh toán 25%

Giai đoạn 2 — Sprint 5-8, 4 tuần:
├── Tối ưu giao diện di động
├── Xuất file đối chiếu cho Kế toán tài sản
└── 💰 Mốc M3: Nghiệm thu Phiên bản đầy đủ → Thanh toán 25%

Vận hành + Bảo hành — 2 tuần:
├── Triển khai chính thức
├── Sửa lỗi (bảo hành)
└── 💰 Mốc M4: Hết bảo hành → Thanh toán 15%
```

---

## 7. Rủi ro ban đầu

| # | Rủi ro | Xác suất | Tác động | Chịu TN | Biện pháp giảm thiểu |
|---|--------|----------|----------|---------|----------------------|
| R1 | PO KH không sẵn sàng → trì hoãn quyết định | Cao | Cao | KH | PO dự phòng, quyết định qua email |
| R2 | Phát sinh yêu cầu ngoài phạm vi (Scope creep) | Cao | Cao | PM | Quy trình Yêu cầu thay đổi (CR), Chốt phạm vi (Baseline) |
| R3 | SSO và máy in barcode chưa xác nhận được thông số | Trung bình | Cao | NCC | Thử nghiệm tích hợp sớm (Giai đoạn 1) |
| R4 | Dữ liệu Excel cũ của các khoa không sạch | Trung bình | Trung bình | KH | Kiểm tra mẫu tuần 1, mỗi khoa có đầu mối dữ liệu (A1) |
| R5 | Nhân sự chủ chốt nghỉ/chuyển nhóm | Thấp | Cao | PM | Chia sẻ kiến thức, làm cặp |
| R6 | Các khoa ngại thao tác thêm khi điều chuyển | Trung bình | Trung bình | KH | Đào tạo theo khoa, giữ số bước xác nhận tối thiểu |

---

## 8. Phê duyệt

> ⚠️ **Tài liệu này sau khi phê duyệt sẽ trở thành BẢN CHỐT PHẠM VI (Baseline). Mọi thay đổi phạm vi phải thông qua quy trình Yêu cầu thay đổi (CR).**

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Nhà tài trợ (Sponsor) | Khách hàng | Trần Minh Đức — Giám đốc vận hành | Đã ký (bản giấy lưu PMO) | 10/02/2026 |
| Người đại diện KH (Product Owner) | Khách hàng | Phạm Thu Hà — Trưởng phòng Vật tư | Đã ký (bản giấy lưu PMO) | 10/02/2026 |
| Quản lý dự án (PM) | Nhà cung cấp | Đỗ Thanh Tùng | Đã ký | 10/02/2026 |
| Trưởng nhóm Phân tích (BA Lead) | Nhà cung cấp | Nguyễn Văn A | Đã ký | 10/02/2026 |

> Tên người ký là dữ liệu minh họa của tài liệu mẫu.

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Người |
|-----------|------|----------|-------|
| 0.1 | 03/02/2026 | Draft đầu tiên từ RFQ và buổi kick-off | BA |
| 0.2 | 07/02/2026 | Cập nhật theo phản hồi KH | BA |
| 1.0 | 10/02/2026 | **Đã phê duyệt — Chốt phạm vi** (chữ ký ở mục 8) | BA |
