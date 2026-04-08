# KẾ HOẠCH NGHIỆM THU (UAT) — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

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

### 3.1 Phạm vi theo phiên bản

| Phiên bản | Modules | Ngày nghiệm thu | Mốc thanh toán |
|-----------|---------|----------|----------------|
| PB1 (MVP) | [Module 1, Module 2] | [Ngày] | M2 — 25% |
| PB2 (Đầy đủ) | [Module 3, Module 4, Tích hợp] | [Ngày] | M3 — 25% |

### 3.2 Điều kiện bắt đầu (Bắt đầu UAT khi)

- [ ] QC NCC đã kiểm thử xong — Báo cáo kiểm thử gửi KH
- [ ] 0 lỗi Nghiêm trọng/Chặn mở
- [ ] ≤ 3 lỗi Lớn mở (có cách giải quyết tạm đã tài liệu)
- [ ] Môi trường UAT đã triển khai & ổn định
- [ ] Dữ liệu kiểm thử có sẵn (dữ liệu thực tế, không phải giả)
- [ ] Kịch bản UAT đã được KH xem xét
- [ ] Hướng dẫn sử dụng / Ghi chú phiên bản gửi KH

### 3.3 Điều kiện kết thúc (Kết thúc UAT khi)

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

### 5.1 Module 1: [Tên Module]

| Mã KT | Kịch bản | Điều kiện tiên quyết | Các bước | Kết quả mong đợi | Đ/K | Ghi chú |
|-------|----------|---------------------|----------|-------------------|-----|---------|
| UAT-001 | **[Kịch bản happy path]** | [Thiết lập cần thiết] | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] | - [Mong đợi 1]<br>- [Mong đợi 2] | ☐ | BRD ref: X.X |
| UAT-002 | **[Kịch bản xử lý lỗi]** | [Thiết lập] | 1. [Bước 1]<br>2. [Hành động sai] | - [Thông báo lỗi]<br>- [Không hỏng dữ liệu] | ☐ | |
| UAT-003 | **[Kịch bản edge case]** | [Thiết lập] | 1. ... | - ... | ☐ | |
| UAT-004 | **[Kịch bản phân quyền]** | Đăng nhập với [Vai trò] | 1. Thử truy cập [tính năng hạn chế] | - [Rejected / xem hạn chế] | ☐ | |

### 5.2 Module 2: [Tên Module]

| Mã KT | Kịch bản | Điều kiện tiên quyết | Các bước | Kết quả mong đợi | Đ/K |
|-------|----------|---------------------|----------|-------------------|-----|
| UAT-010 | **[Tên kịch bản]** | | | | ☐ |
| UAT-011 | **[Tên kịch bản]** | | | | ☐ |

### 5.3 Kịch bản tích hợp

| Mã KT | Kịch bản | Hệ thống liên quan | Các bước | Kết quả mong đợi | Đ/K |
|-------|----------|-------------------|----------|-------------------|-----|
| UAT-INT-01 | **[Tích hợp bên thứ 3]** | [Hệ thống A ↔ Hệ thống B] | 1. ... | - ... | ☐ |
| UAT-INT-02 | **[Luồng thanh toán]** | [Ứng dụng ↔ Cổng thanh toán] | 1. ... | - ... | ☐ |

### 5.4 Xác minh yêu cầu phi chức năng

| Mã KT | Yêu cầu phi chức năng | Phương pháp | Tiêu chí chấp nhận | Kết quả | Đ/K |
|-------|-----|-----------|---------------------|---------|-----|
| UAT-NFR-01 | Hiệu năng (tải trang ≤ 3 giây) | Kiểm tra Lighthouse | Điểm ≥ 80 | — | ☐ |
| UAT-NFR-02 | Người dùng đồng thời (≥ X) | Load test (K6/JMeter) | [X] người, p95 < 500ms | — | ☐ |
| UAT-NFR-03 | Bảo mật (OWASP Top 10) | Quét OWASP ZAP | Không có Nghiêm trọng/Cao | — | ☐ |
| UAT-NFR-04 | Đa trình duyệt | Kiểm thử thủ công | Chrome, Safari, Edge OK | — | ☐ |
| UAT-NFR-05 | Responsive | Kiểm thử di động/tablet | Bố cục không vỡ | — | ☐ |

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

**Tham chiếu SRS/BRD:** [FR-XXX / BRD mục X.X]
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
