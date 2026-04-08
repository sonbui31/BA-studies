# TÀI LIỆU YÊU CẦU KINH DOANH (BRD)
# Dự án Outsource: [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Tác giả:** [Tên BA — Nhà cung cấp]
> **Khách hàng:** [Tên công ty khách hàng]
> **Nhà cung cấp:** [Tên công ty phát triển]
> **Trạng thái:** Draft
> **⚠️ Tài liệu CHỐT PHẠM VI (Baseline) — mọi thay đổi sau khi phê duyệt phải qua quy trình Yêu cầu thay đổi (CR)**

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Người | Phê duyệt bởi |
|-----------|------|----------|-------|----------------|
| 0.1 | | Draft đầu tiên | BA | — |
| 0.2 | | Cập nhật theo phản hồi Khách hàng | BA | — |
| 1.0 | | **Đã phê duyệt — Chốt phạm vi** | BA | Nhà tài trợ KH |

---

## 1. Tóm tắt điều hành

### 1.1 Tóm tắt dự án
[2-3 đoạn tóm tắt: dự án này là gì, giải quyết vấn đề gì, cho ai, kết quả mong đợi. Viết cho ban lãnh đạo đọc — không kỹ thuật.]

_Ví dụ: "Dự án xây dựng hệ thống quản lý đơn hàng trực tuyến cho Công ty ABC, nhằm thay thế quy trình xử lý đơn hàng thủ công hiện tại. Hệ thống sẽ giúp giảm 60% thời gian xử lý đơn, giảm 80% sai sót nhập liệu, và cung cấp dashboard thời gian thực cho ban lãnh đạo theo dõi doanh thu."_

### 1.2 Mục đích tài liệu
Tài liệu này mô tả **yêu cầu kinh doanh** cho dự án [Tên], phục vụ:
- Làm cơ sở cho việc **phê duyệt đầu tư** từ Ban lãnh đạo
- Làm baseline cho **hợp đồng outsource** giữa Khách hàng và Nhà cung cấp
- Làm đầu vào cho **SRS** (đặc tả yêu cầu phần mềm chi tiết)

### 1.3 Đối tượng đọc

| Đối tượng | Đọc phần |
|-----------|---------|
| Ban giám đốc / Nhà tài trợ (Sponsor) | Mục 1-3, 7 (Tóm tắt, Luận chứng kinh doanh, Lợi ích đầu tư) |
| Người đại diện KH (Product Owner) / Quản lý kinh doanh | Toàn bộ |
| Quản lý dự án (PM) / Chuyên viên phân tích (BA) Nhà cung cấp | Toàn bộ |
| Đội phát triển Nhà cung cấp | Mục 4-6 (yêu cầu chi tiết) |
| Tài chính / Mua sắm | Mục 3, 7 (Chi phí-Lợi ích, Ngân sách) |
| Pháp lý | Mục 8 (Ràng buộc, Tuân thủ) |

---

## 2. Bối cảnh kinh doanh

### 2.1 Tổ chức
- **Tên tổ chức:** [Công ty / Cơ quan]
- **Ngành:** [Lĩnh vực]
- **Quy mô:** [Số nhân viên, doanh thu, số chi nhánh...]
- **Vị trí thị trường:** [Vị thế cạnh tranh]

### 2.2 Hiện trạng
[Mô tả cách tổ chức đang vận hành hiện tại — quy trình thủ công, hệ thống cũ, điểm đau]

| # | Vấn đề hiện tại | Ảnh hưởng | Mức độ |
|---|-----------------|-----------|--------|
| 1 | [Điểm đau 1 — VD: Xử lý đơn hàng bằng Excel] | [Mất 2 giờ/đơn, sai sót 15%] | 🔴 Nghiêm trọng |
| 2 | [Điểm đau 2 — VD: Báo cáo tổng hợp thủ công] | [Mất 3 ngày cuối tháng] | 🟠 Cao |
| 3 | [Điểm đau 3 — VD: Khách hàng không tra cứu được] | [30% cuộc gọi là hỏi tiến độ] | 🟠 Cao |
| 4 | [Điểm đau 4 — VD: Không có dữ liệu phân tích] | [Ra quyết định dựa trên cảm tính] | 🟡 Trung bình |

### 2.3 Trạng thái mong muốn
[Mô tả tổ chức sẽ vận hành NHƯ THẾ NÀO sau khi có hệ thống mới]

```
HIỆN TẠI (AS-IS)                    TƯƠNG LAI (TO-BE)
──────────────────                   ──────────────────
Excel + Email + Giấy       ───▶     Hệ thống tập trung
Xử lý 2 giờ/đơn            ───▶     Xử lý 15 phút/đơn
Sai sót 15%                 ───▶     Sai sót < 1%
Báo cáo 3 ngày              ───▶     Dashboard thời gian thực
KH gọi hỏi tiến độ          ───▶     KH tự tra cứu trực tuyến
```

### 2.4 Động lực thay đổi
- **Kinh doanh:** [Tăng doanh thu, giảm chi phí, mở rộng thị trường...]
- **Công nghệ:** [Hệ thống cũ hết hỗ trợ, chuyển đổi số...]
- **Pháp quy:** [Quy định mới bắt buộc số hóa...]
- **Cạnh tranh:** [Đối thủ đã có hệ thống, mất lợi thế...]

---

## 3. Luận chứng kinh doanh & Phân tích chi phí-lợi ích

### 3.1 Tóm tắt luận chứng

| Tiêu chí | Chi tiết |
|----------|---------|
| **Vấn đề** | [1 câu tóm tắt vấn đề] |
| **Giải pháp** | [1 câu tóm tắt giải pháp] |
| **Chi phí ước tính** | [VND/USD — từ Hợp đồng] |
| **Lợi ích ước tính** | [VND/USD/năm — tiết kiệm + tăng thu] |
| **Thời gian hoàn vốn** | [X tháng] |
| **Khuyến nghị** | ☐ Tiến hành ☐ Hoãn ☐ Hủy |

### 3.2 Chi phí

| # | Hạng mục | Loại | Năm 1 | Năm 2 | Năm 3 |
|---|----------|------|-------|-------|-------|
| 1 | Phát triển phần mềm (NCC) | Một lần | $[___] | — | — |
| 2 | Giấy phép phần mềm (nếu có) | Định kỳ | $[___] | $[___] | $[___] |
| 3 | Hạ tầng / Đám mây | Định kỳ | $[___] | $[___] | $[___] |
| 4 | Đào tạo nhân viên | Một lần | $[___] | — | — |
| 5 | Chuyển đổi dữ liệu | Một lần | $[___] | — | — |
| 6 | Bảo trì hàng năm (sau bảo hành) | Định kỳ | — | $[___] | $[___] |
| 7 | Nhân sự nội bộ (PO, quản trị) | Định kỳ | $[___] | $[___] | $[___] |
| | **TỔNG** | | **$[___]** | **$[___]** | **$[___]** |

### 3.3 Lợi ích

#### Lợi ích định lượng

| # | Lợi ích | Cách tính | Giá trị/năm |
|---|---------|-----------|-------------|
| 1 | Giảm thời gian xử lý | [X] giờ/ngày × [Y] ngày × chi phí/giờ | $[___]/năm |
| 2 | Giảm sai sót → giảm chi phí sửa lỗi | [X]% giảm lỗi × chi phí mỗi lỗi | $[___]/năm |
| 3 | Giảm nhân sự thủ công | [X] người × lương | $[___]/năm |
| 4 | Tăng doanh thu (nếu áp dụng) | [X]% cải thiện chuyển đổi | $[___]/năm |
| | **TỔNG LỢI ÍCH/NĂM** | | **$[___]** |

#### Lợi ích định tính
- ✅ Nâng cao trải nghiệm khách hàng → tăng trung thành
- ✅ Ra quyết định nhanh hơn dựa trên dữ liệu
- ✅ Nâng cao hình ảnh thương hiệu (ưu tiên số hóa)
- ✅ Sẵn sàng mở rộng quy mô
- ✅ Tuân thủ quy định

### 3.4 Phân tích ROI

```
                    Năm 0       Năm 1       Năm 2       Năm 3
                    ──────      ──────      ──────      ──────
Đầu tư:           -$[___]       —           —           —
Chi phí vận hành:    —         -$[___]     -$[___]     -$[___]
Lợi ích:             —         +$[___]     +$[___]     +$[___]
                    ──────      ──────      ──────      ──────
Lợi ích ròng:     -$[___]     +$[___]     +$[___]     +$[___]
Lũy kế:           -$[___]     -$[___]     +$[___]     +$[___]
                                             ▲
                                     Điểm hòa vốn
                                     (~[X] tháng)

ROI (3 năm) = (Tổng lợi ích - Tổng chi phí) / Tổng chi phí × 100
           = ([___] - [___]) / [___] × 100
           = [___]%
```

---

## 4. Phạm vi dự án

### 4.1 Mục tiêu dự án

| # | Mục tiêu | KPI | Chỉ tiêu | Thời hạn |
|---|----------|-----|----------|----------|
| O1 | [Mục tiêu nghiệp vụ 1] | [Chỉ số] | [Giá trị] | [Ngày] |
| O2 | [Mục tiêu nghiệp vụ 2] | [Chỉ số] | [Giá trị] | [Ngày] |
| O3 | [Mục tiêu nghiệp vụ 3] | [Chỉ số] | [Giá trị] | [Ngày] |

**Tiêu chí thành công:**
1. [Tiêu chí thành công 1]
2. [Tiêu chí thành công 2]
3. [Tiêu chí thành công 3]

### 4.2 Trong phạm vi

#### Nhóm chức năng 1: [Tên Module]
**Nhu cầu kinh doanh:** [Tại sao cần module này?]

| Mã BRD | Yêu cầu kinh doanh | Mô tả | Ưu tiên | Ref HĐ |
|--------|---------------------|--------|---------|--------|
| BRD-101 | [Tên yêu cầu nghiệp vụ] | [Mô tả ở mức NGHIỆP VỤ, không kỹ thuật] | Bắt buộc | HĐ 2.1 |
| BRD-102 | [Tên yêu cầu] | [Mô tả] | Bắt buộc | HĐ 2.1 |
| BRD-103 | [Tên yêu cầu] | [Mô tả] | Nên có | HĐ 2.1 |

#### Nhóm chức năng 2: [Tên Module]
**Nhu cầu kinh doanh:** [Tại sao cần?]

| Mã BRD | Yêu cầu kinh doanh | Mô tả | Ưu tiên | Ref HĐ |
|--------|---------------------|--------|---------|--------|
| BRD-201 | [Tên] | [Mô tả] | Bắt buộc | HĐ 2.2 |
| BRD-202 | [Tên] | [Mô tả] | Nên có | HĐ 2.2 |

#### Nhóm chức năng 3: [Tên Module]
_(Thêm modules tương tự)_

### 4.3 Ngoài phạm vi

| # | Hạng mục | Lý do loại trừ | Xem xét lại khi |
|---|----------|----------------|-----------------|
| 1 | [Hạng mục 1] | Hạn chế ngân sách | Giai đoạn 2 / Năm 2 |
| 2 | [Hạng mục 2] | Chưa có nhu cầu rõ ràng | Khi kinh doanh mở rộng |
| 3 | [Hạng mục 3] | Hệ thống khác đang xử lý | Khi hệ thống cũ nghỉ hưu |

### 4.4 Giả định

| # | Giả định | Nếu KHÔNG đúng thì... | Người xác nhận |
|---|----------|----------------------|----------------|
| A1 | [Giả định 1] | [Ảnh hưởng] | [KH/NCC] |
| A2 | [Giả định 2] | [Ảnh hưởng] | [KH/NCC] |
| A3 | [Giả định 3] | [Ảnh hưởng] | [KH/NCC] |

### 4.5 Ràng buộc

| # | Ràng buộc | Loại | Ảnh hưởng |
|---|-----------|------|-----------|
| C1 | Ngân sách: [Số tiền] | Tài chính | Giới hạn phạm vi |
| C2 | Thời hạn: [Ngày] | Tiến độ | Phải chia phiên bản |
| C3 | [Yêu cầu tuân thủ] | Pháp quy | Cần kiểm tra bảo mật |
| C4 | [Ràng buộc kỹ thuật] | Kỹ thuật | Giới hạn lựa chọn công nghệ |

---

## 5. Phân tích stakeholder

### 5.1 Các stakeholder chính

| # | Stakeholder | Vai trò | Kỳ vọng | Mức ảnh hưởng |
|---|--------------|---------|---------|---------------|
| 1 | [Giám đốc/Ban lãnh đạo] | Nhà tài trợ (Sponsor) | Lợi ích đầu tư (ROI), đúng ngân sách | 🔴 Rất cao |
| 2 | [Quản lý kinh doanh] | Người đại diện KH (Product Owner) | Đúng nghiệp vụ | 🔴 Rất cao |
| 3 | [Người dùng cuối] | Người dùng chính | Dễ dùng, giải quyết được việc | 🟠 Cao |
| 4 | [Phòng CNTT] | Giám sát kỹ thuật | Tuân thủ chuẩn kỹ thuật | 🟠 Cao |
| 5 | [Khách hàng/Đối tác] | Người dùng bên ngoài | Tự phục vụ, nhanh | 🟡 Trung bình |

_(Chi tiết: xem `03-Stakeholder-Map.md`)_

---

## 6. Tổng quan quy trình nghiệp vụ

### 6.1 Quy trình hiện tại (As-Is) — Tóm tắt

```
[Sơ đồ tóm tắt quy trình hiện tại — giữ mức cao, 5-7 bước chính]

Bước 1 → Bước 2 → Bước 3 → ... → Bước N
(thủ công) (Excel)  (email)       (báo cáo tay)
```

**Điểm nghẽn chính:**
1. 🔴 [Nghẽn 1 — mô tả + ảnh hưởng]
2. 🟠 [Nghẽn 2]
3. 🟡 [Nghẽn 3]

### 6.2 Quy trình tương lai (To-Be) — Tóm tắt

```
[Sơ đồ tóm tắt quy trình tương lai — 5-7 bước]

Bước 1 → Hệ thống tự động → Bước 3 → ... → Dashboard
(biểu mẫu) (xác nhận)      (phê duyệt)      (thời gian thực)
```

**Cải tiến:**
- ✅ [Cải tiến 1 — KPI cụ thể]
- ✅ [Cải tiến 2]
- ✅ [Cải tiến 3]

_(Chi tiết: xem `04-Process-Flow.md`)_

---

## 7. Yêu cầu phi chức năng (Tóm tắt)

| Danh mục | Yêu cầu | Chỉ tiêu |
|----------|---------|----------|
| **Hiệu năng** | Thời gian tải trang | ≤ 3 giây |
| **Khả dụng** | Thời gian hoạt động | ≥ 99.5% |
| **Bảo mật** | Xác thực | JWT + 2FA |
| **Bảo mật** | Mã hóa dữ liệu | TLS 1.2+ / AES-256 |
| **Mở rộng** | Người dùng đồng thời | ≥ [X] |
| **Tuân thủ** | Bảo vệ dữ liệu | [GDPR/PDPA/quy định] |
| **Khả dụng** | Responsive | Di động + Máy tính |

_(Chi tiết: xem `05-SRS.md` Mục 3)_

---

## 8. Rủi ro

| # | Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu | Chịu trách nhiệm |
|---|--------|----------|----------|----------------------|-------------------|
| R1 | Phát sinh yêu cầu ngoài phạm vi (Scope creep) → vượt ngân sách | Cao | Cao | Chốt phạm vi (Baseline) + quy trình Yêu cầu thay đổi (CR) | Cả hai |
| R2 | Người dùng kháng cự thay đổi | Cao | Trung bình | Cho tham gia sớm, đào tạo, quản lý thay đổi | KH |
| R3 | Tích hợp phức tạp hơn dự kiến | Trung bình | Cao | Thử nghiệm sớm, xem xét API tuần 2 | NCC |
| R4 | Stakeholder chính thay đổi giữa chừng | Thấp | Cao | Ghi nhận quyết định, phê duyệt chính thức | KH |
| R5 | Dữ liệu cũ không sạch | Trung bình | Trung bình | Kiểm tra dữ liệu sớm, KH chịu trách nhiệm chất lượng dữ liệu | KH |

---

## 9. Tóm tắt tiến độ & Ngân sách

### 9.1 Tiến độ tổng quan

| Giai đoạn | Thời lượng | Sản phẩm chính | Mốc |
|-----------|-----------|----------------|-----|
| Khám phá & Thiết kế | [X] tuần | Đặc tả yêu cầu (SRS), Giao diện phác thảo | M1: Phê duyệt đặc tả |
| Phát triển Giai đoạn 1 (Bản cơ bản - MVP) | [X] tuần | Phần mềm hoạt động được | M2: Nghiệm thu GĐ1 |
| Phát triển Giai đoạn 2 | [X] tuần | Đầy đủ tính năng | M3: Nghiệm thu GĐ2 |
| Vận hành + Bảo hành | [X] tuần | Hệ thống chính thức | M4: Kết thúc bảo hành |
| **Tổng** | **[X] tuần** | | |

### 9.2 Tóm tắt ngân sách

| Hạng mục | Số tiền |
|----------|---------|
| Phát triển phần mềm (NCC) | $[___] |
| Hạ tầng/Hosting (Năm 1) | $[___] |
| Đào tạo + Quản lý thay đổi | $[___] |
| Dự phòng (10-15%) | $[___] |
| **TỔNG** | **$[___]** |

---

## 10. Ma trận truy vết (BRD → SRS → HĐ)

| Yêu cầu BRD | Tham chiếu SRS | Mục HĐ | User Story | Ưu tiên |
|-------------|----------------|---------|----------------------|---------|
| BRD-101 | FR-101, FR-102 | HĐ 2.1 | US-001, US-002 | Bắt buộc |
| BRD-102 | FR-103 | HĐ 2.1 | US-003 | Bắt buộc |
| BRD-201 | FR-201 | HĐ 2.2 | US-010 | Nên có |
| BRD-202 | FR-202, FR-203 | HĐ 2.2 | US-011, US-012 | Có thể |

> **Truy vết đảm bảo:** Mọi yêu cầu kinh doanh đều được triển khai và kiểm thử

---

## 11. Phê duyệt BRD

> ⚠️ **Phê duyệt BRD = Phê duyệt đầu tư + Chốt phạm vi (Baseline)**
> Sau thời điểm này, mọi thay đổi phạm vi phải qua quy trình Yêu cầu thay đổi (CR)

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Nhà tài trợ (Sponsor) | Khách hàng | | | |
| Người đại diện KH (Product Owner) | Khách hàng | | | |
| Tài chính/Mua sắm | Khách hàng | | | |
| Quản lý dự án (PM) | Nhà cung cấp | | | |
| Trưởng nhóm Phân tích (BA Lead) | Nhà cung cấp | | | |

---

## Phụ lục

- **Phụ lục A:** Bảng thuật ngữ
- **Phụ lục B:** Chi tiết Quy trình nghiệp vụ → xem `04-Process-Flow.md`
- **Phụ lục C:** Chi tiết SRS → xem `05-SRS.md`
- **Phụ lục D:** Hợp đồng → xem tài liệu hợp đồng riêng
- **Phụ lục E:** Ghi chú phỏng vấn stakeholder
