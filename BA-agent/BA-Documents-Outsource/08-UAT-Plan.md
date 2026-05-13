# KẾ HOẠCH NGHIỆM THU (UAT) — DỰ ÁN OUTSOURCE
# Dự án Hệ thống Quản lý Tài sản Bệnh viện

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **⚠️ Nghiệm thu đạt = Điều kiện thanh toán mốc. Khách hàng PHẢI tham gia.**

---

## 1. Mục tiêu nghiệm thu

- **Khách hàng** xác nhận hệ thống đáp ứng yêu cầu trong BRD & SRS
- Phát hiện lỗi/khoảng cách trước khi vận hành
- **Phê duyệt chính thức** → kích hoạt mốc thanh toán

---

## 2. Đặc thù UAT trong gia công

| Yếu tố | UAT nội bộ | UAT gia công |
|---------|-----------|-------------|
| Ai kiểm thử | Người dùng cuối + QC | **PO/Người dùng cuối KH** (QC NCC hỗ trợ) |
| Kết quả | Phản hồi → sửa | **Đạt/Không đạt → Thanh toán/Không thanh toán** |
| Xử lý lỗi | Sửa ngay | Lỗi vs Yêu cầu thay đổi (CR) — phân loại ảnh hưởng chi phí |
| Phê duyệt | Không chính thức | **Biên bản nghiệm thu có giá trị pháp lý** |
| Bảo hành | Không rõ ràng | **30-90 ngày sau khi phê duyệt** |
| Môi trường | Dev/Staging | **Môi trường UAT riêng** (KH xác nhận) |

---

## 3. Phạm vi & Tiêu chí

### 3.1. Phạm vi theo phiên bản

| Phiên bản | Modules | Ngày nghiệm thu | Mốc thanh toán |
|-----------|---------|----------|----------------|
| PB1 (MVP) | Danh mục tài sản, Điều chuyển, Kiểm kê | 10/10/2026 | M2 — 25% |
| PB2 (Đầy đủ) | Bảo trì, Dashboard, Tích hợp cảnh báo | 30/11/2026 | M3 — 25% |

### 3.2. Điều kiện bắt đầu (Bắt đầu UAT khi)

- [ ] QC NCC đã kiểm thử xong — Báo cáo kiểm thử gửi KH
- [ ] 0 lỗi Nghiêm trọng/Chặn mở
- [ ] ≤ 3 lỗi Lớn mở (có cách giải quyết tạm đã tài liệu)
- [ ] Môi trường UAT đã triển khai & ổn định
- [ ] Dữ liệu kiểm thử có sẵn (dữ liệu thực tế, không phải giả)
- [ ] Kịch bản UAT đã được KH xem xét
- [ ] Hướng dẫn sử dụng / Ghi chú phiên bản gửi KH

### 3.3. Điều kiện kết thúc (Kết thúc UAT khi)

- [ ] ≥ 95% kịch bản kiểm thử Đạt
- [ ] 0 lỗi Nghiêm trọng mở
- [ ] ≤ 3 lỗi Lớn mở (đồng ý sửa trong bảo hành)
- [ ] **Người đại diện KH (PO) ký biên bản nghiệm thu**

---

## 4. Phân loại lỗi & SLA

| Mức | Mô tả | SLA sửa (NCC) | Ảnh hưởng UAT |
|-----|--------|---------------|---------------|
| 🔴 **Nghiêm trọng** | Hệ thống sập, mất dữ liệu, lỗ hổng bảo mật | **4 giờ** | **Chặn UAT** — không tiếp tục |
| 🟠 **Lớn** | Tính năng chính hỏng, không có cách giải quyết tạm | **1 ngày** | Chặn kịch bản cụ thể |
| 🟡 **Nhỏ** | Tính năng hoạt động nhưng sai hành vi, có cách giải quyết tạm | **3 ngày** | Tiếp tục UAT |
| 🟢 **Giao diện** | Lỗi UI, lỗi chính tả, căn lề | **Backlog / Bảo hành** | Tiếp tục UAT |

### ⚠️ Lỗi vs Yêu cầu thay đổi — Quy tắc phân loại

| Tiêu chí | Lỗi (NCC sửa miễn phí) | CR (Có ảnh hưởng chi phí) |
|----------|------------------------|--------------------------|
| Có trong SRS/Story? | Có → Lỗi | Không → **CR** |
| Đúng như TC nhưng KH muốn khác? | — | **CR** |
| Hoạt động đúng đặc tả nhưng UX không tốt? | — | **CR** (hoặc nâng cấp P2) |
| Thiếu tính năng so với BRD/Hợp đồng? | **Lỗi** (thiếu yêu cầu) | — |

> ⚠️ **Quy tắc vàng:** Nếu tính năng **không có trong bản chốt đặc tả (SRS baseline)** → đó là Yêu cầu thay đổi (CR), không phải lỗi.
> Đây là lý do phê duyệt đặc tả (SRS) rất quan trọng trong gia công.

---

## 5. Kịch bản kiểm thử UAT

### 5.1. Module 1: Danh mục tài sản

| Mã KT | Kịch bản | Điều kiện tiên quyết | Các bước | Kết quả mong đợi | Kết quả | Ref BRD | Ref FR | Ref Story |
|-------|----------|---------------------|----------|-------------------|---------|---------|--------|-----------|
| UAT-001 | **Tạo tài sản mới** | Tài khoản Vật tư có quyền tạo tài sản | 1. Mở form tạo tài sản<br>2. Nhập đủ trường bắt buộc<br>3. Lưu hồ sơ | - Tài sản mới được tạo<br>- Có mã tài sản duy nhất<br>- Có audit log tạo mới | ☐ | BRD-101 | FR-101 | US-001 |
| UAT-002 | **Từ chối mã tài sản trùng** | Đã tồn tại tài sản AP-TS-0001 | 1. Tạo tài sản mới<br>2. Nhập mã AP-TS-0001<br>3. Lưu hồ sơ | - Hệ thống chặn lưu<br>- Hiển thị thông báo trùng mã<br>- Không phát sinh bản ghi mới | ☐ | BRD-102 | FR-102 | US-002 |
| UAT-003 | **Bắt buộc chu kỳ bảo trì với thiết bị quan trọng** | Tài khoản Vật tư có quyền tạo | 1. Chọn nhóm thiết bị y tế quan trọng<br>2. Để trống chu kỳ bảo trì<br>3. Lưu hồ sơ | - Hệ thống yêu cầu nhập chu kỳ bảo trì | ☐ | BRD-103 | FR-103 | US-003 |
| UAT-004 | **Chặn truy cập trái quyền** | Đăng nhập bằng vai trò Người dùng khoa | 1. Mở màn hình cấu hình danh mục | - Hệ thống từ chối truy cập | ☐ | BRD-201 | FR-105 | US-005 |

### 5.2. Module 2: Điều chuyển và Kiểm kê

| Mã KT | Kịch bản | Điều kiện tiên quyết | Các bước | Kết quả mong đợi | Kết quả | Ref BRD | Ref FR | Ref Story |
|-------|----------|---------------------|----------|-------------------|---------|---------|--------|-----------|
| UAT-011 | **Tạo yêu cầu điều chuyển** | Tài sản đang Active, user khoa có quyền tạo yêu cầu | 1. Chọn tài sản<br>2. Chọn khoa nhận<br>3. Nhập lý do<br>4. Gửi yêu cầu | - Yêu cầu ở trạng thái Pending Approval | ☐ | BRD-201 | FR-201 | US-011 |
| UAT-012 | **Xác nhận giao và nhận tài sản** | Yêu cầu điều chuyển đã duyệt | 1. Bên giao xác nhận<br>2. Bên nhận xác nhận | - Khoa sở hữu mới được cập nhật<br>- Có lịch sử điều chuyển | ☐ | BRD-201 | FR-202 | US-012 |
| UAT-021 | **Mở đợt kiểm kê và ghi nhận lệch** | Danh sách tài sản khoa Nội đã sẵn sàng | 1. Tạo đợt kiểm kê<br>2. Quét barcode 3 tài sản<br>3. Đánh dấu 1 tài sản sai vị trí | - Đợt kiểm kê được tạo<br>- Tài sản lệch được phân loại `Sai vị trí` | ☐ | BRD-202, BRD-203 | FR-203 | US-021, US-022 |

### 5.3. Kịch bản tích hợp

| Mã KT | Kịch bản | Hệ thống liên quan | Các bước | Kết quả mong đợi | Đ/K |
|-------|----------|-------------------|----------|-------------------|-----|
| UAT-INT-01 | **Gửi email cảnh báo bảo trì** | Tài sản có lịch bảo trì đến hạn, cấu hình email đã sẵn sàng | 1. Đẩy ngày hệ thống tới mốc cảnh báo<br>2. Chạy scheduler | - Email cảnh báo được gửi đúng người nhận | ☐ |
| UAT-INT-02 | **Đăng nhập qua SSO** | SSO test account khả dụng | 1. Chọn đăng nhập SSO<br>2. Xác thực thành công | - Người dùng vào hệ thống đúng vai trò | ☐ |

**Module 3: Bảo trì và Dashboard**

| Mã KT | Kịch bản | Điều kiện tiên quyết | Các bước | Kết quả mong đợi | Kết quả | Ref BRD | Ref FR | Ref Story |
|-------|----------|---------------------|----------|-------------------|---------|---------|--------|-----------|
| UAT-031 | **Tạo cảnh báo bảo trì đến hạn** | Tài sản có chu kỳ bảo trì 30 ngày và sắp đến hạn 15 ngày | 1. Chạy scheduler<br>2. Mở danh sách cảnh báo | - Có work item bảo trì<br>- Có cảnh báo cho Vật tư | ☐ | BRD-301, BRD-302 | FR-301 | US-031 |
| UAT-032 | **Cập nhật kết quả bảo trì** | Có work item bảo trì đang mở | 1. Mở phiếu bảo trì<br>2. Nhập kết quả<br>3. Lưu | - Lịch sử bảo trì được ghi nhận<br>- Ngày bảo trì kế tiếp được tính lại | ☐ | BRD-301, BRD-302 | FR-302 | US-032 |
| UAT-033 | **Xem dashboard điều hành** | Tài khoản Ban điều hành có quyền dashboard | 1. Mở dashboard<br>2. Lọc theo khoa Nội | - Hiển thị tổng tài sản, trạng thái, tài sản đến hạn bảo trì, lệch kiểm kê | ☐ | BRD-303 | FR-303 | US-033 |

### 5.4. Xác minh yêu cầu phi chức năng

| Mã KT | Yêu cầu phi chức năng | Phương pháp | Tiêu chí chấp nhận | Kết quả | Đ/K |
|-------|-----|-----------|---------------------|---------|-----|
| UAT-NFR-01 | NFR-001: Hiệu năng dashboard (≤ 3 giây) | Kiểm tra Lighthouse / synthetic | Điểm ≥ 80, tải ≤ 3 giây | — | ☐ |
| UAT-NFR-02 | NFR-003: Người dùng đồng thời (≥ 250) | Load test (K6/JMeter) | 250 người, p95 < 500ms | — | ☐ |
| UAT-NFR-03 | NFR-009: Bảo mật (OWASP Top 10) | Quét OWASP ZAP | Không có Nghiêm trọng/Cao | — | ☐ |
| UAT-NFR-04 | Đa trình duyệt | Kiểm thử thủ công | Chrome, Safari, Edge OK | — | ☐ |
| UAT-NFR-05 | NFR-11: Responsive | Kiểm thử di động/tablet | Bố cục không vỡ | — | ☐ |

---

## 6. Mẫu báo cáo lỗi — Gia công

```markdown
### Mã lỗi: BUG-[NNN]
- **Người báo cáo:** [Tên] — [KH/NCC]
- **Mức nghiêm trọng:** Nghiêm trọng / Lớn / Nhỏ / Giao diện
- **Module:** [Tên module]
- **Kịch bản kiểm thử:** UAT-[NNN]
- **Ngày:** [DD/MM/YYYY]
- **Môi trường:** [URL/phiên bản UAT]

**Tham chiếu SRS/BRD:** [FR-XXX / BRD-XXX / US-XXX]
→ Đây là Lỗi / CR? [BA phân loại]

**Mô tả:**
[Mô tả ngắn gọn]

**Các bước tái tạo:**
1. ...
2. ...
3. ...

**Kết quả thực tế:**
[Điều gì xảy ra]

**Kết quả mong đợi:**
[Theo SRS/TC, đáng lẽ phải như thế nào]

**Ảnh chụp/Video:**
[Đính kèm]

**Trạng thái:** Mở → Đã gán → Đang xử lý → Đã sửa → Đã xác nhận → Đã đóng
**Sửa trong phiên bản:** [Phiên bản]
**Xác nhận bởi:** [Tên — KH]
```

---

## 7. Lịch trình UAT

| Giai đoạn | Thời lượng | Hoạt động | Sản phẩm |
|-----------|-----------|-----------|----------|
| **Chuẩn bị** | 3 ngày | Triển khai môi trường nghiệm thu, chuẩn bị dữ liệu, hướng dẫn Người đại diện KH | Danh mục sẵn sàng |
| **UAT Vòng 1** | 5 ngày | KH chạy kịch bản, ghi nhận lỗi | Danh sách lỗi |
| **Sửa lỗi** | 5 ngày | NCC sửa → triển khai → thông báo KH | Bản dựng đã sửa |
| **UAT Vòng 2** | 3 ngày | Kiểm thử lại lỗi + hồi quy | Danh sách lỗi cập nhật |
| **Dự phòng** | 2 ngày | Sửa nóng nếu còn Nghiêm trọng/Lớn | — |
| **Phê duyệt** | 1 ngày | Xem xét kết quả, ký biên bản | **Biên bản đã ký** |
| **Tổng** | **~3 tuần** | | |

**7.1. Defect deferment được KH chấp nhận**

| BUG ID | Mức độ | Mô tả | Lý do defer | Cam kết sửa | Owner |
|---|---|---|---|---|---|
| BUG-019 | Nhỏ | Màu badge trạng thái chưa đúng guideline | Không ảnh hưởng nghiệp vụ, chấp nhận trong bảo hành | 15/12/2026 | NCC UI Lead |

---

## 8. Biên bản nghiệm thu

```
═══════════════════════════════════════════════════════════
         BIÊN BẢN NGHIỆM THU / CHỨNG NHẬN CHẤP NHẬN
═══════════════════════════════════════════════════════════

Dự án:      [Tên dự án]
Hợp đồng:   [Số HĐ]
Phiên bản:  [PB1 / PB2 / Cuối cùng]

────────────────────────────────────────────────────────

1. CÁC BÊN:

   BÊN A (Khách hàng):  [Tên công ty]
   Đại diện:            [Họ tên, chức vụ]

   BÊN B (Nhà cung cấp): [Tên công ty]
   Đại diện:            [Họ tên, chức vụ]

2. PHẠM VI NGHIỆM THU:
   Các module/tính năng theo BRD/Hợp đồng mục: [X.X, Y.Y, Z.Z]

3. KẾT QUẢ UAT:
   Tổng kịch bản:    [N]
   Đạt:              [N] ([X]%)
   Không đạt (hoãn): [N] — danh sách lỗi hoãn đính kèm

4. KẾT LUẬN:
   ☐ ĐẠT — Hệ thống đáp ứng yêu cầu, đủ điều kiện vận hành
   ☐ ĐẠT CÓ ĐIỀU KIỆN — Đạt với cam kết sửa lỗi trong:
     Danh sách: [BUG-IDs]
     Thời hạn:  [N ngày]
   ☐ KHÔNG ĐẠT — Lý do: ________________

5. THANH TOÁN:
   Mốc:              M[N] — [X]%
   Số tiền:          [VND/USD]
   Điều kiện:        Kết luận = "ĐẠT" hoặc "ĐẠT CÓ ĐIỀU KIỆN"

6. BẢO HÀNH:
   Thời hạn bảo hành: [30/60/90] ngày kể từ ngày ký
   Phạm vi:           Sửa lỗi (Nghiêm trọng + Lớn) miễn phí
   Ngoài phạm vi:     Tính năng mới, nâng cấp = Hợp đồng mới

7. CHỮ KÝ:

   Bên A: _________________     Bên B: _________________
   Ngày:  ___/___/______         Ngày:  ___/___/______

═══════════════════════════════════════════════════════════
```
