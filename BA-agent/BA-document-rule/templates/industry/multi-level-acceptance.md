# NGHIỆM THU NHIỀU CẤP & CLINICAL VALIDATION — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Áp dụng:** 🏛️ Government · 🏥 Healthcare
> **Mục đích:** Quy trình nghiệm thu nhiều bước + xác nhận y khoa (nếu Healthcare)

---

## 1. Quy trình nghiệm thu tổng quan

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  NGHIỆM THU  │──▶│  VẬN HÀNH    │──▶│  NGHIỆM THU  │──▶│  BÀN GIAO    │
│  SƠ BỘ       │   │  THỬ         │   │  CHÍNH THỨC   │   │  & BẢO HÀNH  │
│  (1-2 tuần)  │   │  (1-3 tháng) │   │  (1-2 tuần)  │   │  (12 tháng)  │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

---

## 2. Nghiệm thu sơ bộ

### 2.1 Checklist nghiệm thu sơ bộ

| # | Hạng mục | Tiêu chí | Kết quả | Ghi chú |
|---|---------|---------|:------:|---------|
| 1 | Chức năng | 100% FR trong SRS hoạt động đúng | ✅ / ❌ | |
| 2 | Dữ liệu | Migration data đúng + đủ (nếu có) | ✅ / ❌ / N/A | |
| 3 | Hiệu năng | Đáp ứng NFR (response time, concurrent) | ✅ / ❌ | |
| 4 | Bảo mật | ATTT đạt cấp yêu cầu | ✅ / ❌ | |
| 5 | Tài liệu | Hướng dẫn sử dụng + Admin guide | ✅ / ❌ | |
| 6 | Đào tạo | Đào tạo end-user hoàn thành | ✅ / ❌ | |

### 2.2 Biên bản nghiệm thu sơ bộ

| Hạng mục | Chi tiết |
|---------|---------|
| Ngày nghiệm thu | {{DD/MM/YYYY}} |
| Địa điểm | {{Địa chỉ}} |
| Hội đồng nghiệm thu | {{Danh sách thành viên}} |
| Kết luận | ☐ **ĐẠT** — Chuyển sang vận hành thử / ☐ **CHƯA ĐẠT** — Cần bổ sung |
| Lỗi còn tồn đọng | {{Số lỗi, mức độ, deadline sửa}} |

**Ký xác nhận:**

| Vai trò | Tên | Chức vụ | Chữ ký |
|---------|-----|---------|--------|
| Đại diện Chủ đầu tư | | | |
| Đại diện Nhà thầu | | | |
| Giám sát (nếu có) | | | |

---

## 3. Vận hành thử

| Hạng mục | Chi tiết |
|---------|---------|
| Thời gian | {{DD/MM}} — {{DD/MM/YYYY}} ({{N}} ngày) |
| Phạm vi | {{Tất cả modules / Modules cốt lõi}} |
| Người sử dụng | {{N}} CBCC / nhân viên y tế |
| Hỗ trợ | Nhà thầu bố trí {{N}} người onsite |

### 3.1 Theo dõi vận hành thử

| Tuần | Lỗi phát sinh | Lỗi đã sửa | Lỗi tồn | Uptime | Ghi chú |
|:----:|:-------------:|:----------:|:-------:|:------:|---------|
| 1 | {{N}} | {{N}} | {{N}} | {{%}} | |
| 2 | | | | | |
| ... | | | | | |

### 3.2 Tiêu chí hoàn thành vận hành thử

```
☐ Uptime ≥ {{99%}} trong toàn bộ thời gian thử
☐ Lỗi Critical: 0 (đã sửa hết)
☐ Lỗi Major: ≤ {{3}} (có kế hoạch sửa)
☐ ≥ {{80%}} end-user đã sử dụng hệ thống
☐ Không gián đoạn nghiệp vụ do hệ thống
```

---

## 4. Clinical Validation (🏥 Healthcare only)

> ⚠️ Bỏ qua section này nếu không phải dự án Y tế.

### 4.1 Ma trận Clinical Validation

| # | Module / Feature | Logic y khoa cần validate | Bác sĩ Reviewer | Kết quả | Ngày |
|---|-----------------|-------------------------|------------------|:------:|------|
| 1 | {{Kê đơn thuốc}} | {{DDI check, liều dùng, chống chỉ định}} | {{BS. Nguyễn Văn A — Nội khoa}} | ✅ / ❌ | |
| 2 | {{Chẩn đoán ICD}} | {{Mapping ICD-10 đúng per chuyên khoa}} | {{BS. Trần Thị B — BV XYZ}} | ✅ / ❌ | |
| 3 | {{Xét nghiệm}} | {{Giá trị bình thường, cảnh báo bất thường}} | {{BS. CLS}} | ✅ / ❌ | |

### 4.2 Biên bản Clinical Validation

| Hạng mục | Chi tiết |
|---------|---------|
| Ngày | {{DD/MM/YYYY}} |
| Bác sĩ tham gia | {{Danh sách BS + Chuyên khoa + BV}} |
| Kết luận | ☐ **Logic y khoa ĐÚNG** — An toàn cho bệnh nhân / ☐ **CẦN SỬA** — Chỉ ra lỗi cụ thể |
| Điều kiện | {{VD: Phải cập nhật bảng DDI trước go-live}} |

**Ký xác nhận (tối thiểu 3 BS):**

| # | Họ tên | Chuyên khoa | Đơn vị | Chữ ký |
|---|--------|------------|--------|--------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## 5. Nghiệm thu chính thức

### 5.1 Checklist nghiệm thu chính thức

| # | Hạng mục | Tiêu chí | Kết quả |
|---|---------|---------|:------:|
| 1 | Nghiệm thu sơ bộ | Đã ĐẠT | ☐ |
| 2 | Vận hành thử | Hoàn thành đủ thời gian + đạt tiêu chí | ☐ |
| 3 | Lỗi tồn đọng | Critical = 0, Major ≤ kế hoạch | ☐ |
| 4 | Clinical Validation (nếu HC) | Tất cả BS đã ký xác nhận | ☐ |
| 5 | Tài liệu bàn giao | Đầy đủ theo hợp đồng | ☐ |
| 6 | Đào tạo | ≥ 80% end-user đã đào tạo | ☐ |
| 7 | ATTT | Đánh giá ATTT đạt cấp yêu cầu | ☐ |

### 5.2 Biên bản nghiệm thu chính thức

| Hạng mục | Chi tiết |
|---------|---------|
| Số biên bản | {{BB-YYYY-NNN}} |
| Ngày | {{DD/MM/YYYY}} |
| Hội đồng | {{Danh sách + chức vụ}} |
| Kết luận | ☐ **NGHIỆM THU ĐẠT** / ☐ **CHƯA ĐẠT — Lý do:** {{...}} |
| Giá trị thanh toán | {{VNĐ}} |
| Thời gian bảo hành | Bắt đầu từ {{DD/MM/YYYY}}, kết thúc {{DD/MM/YYYY}} |

**Ký xác nhận Hội đồng:**

| STT | Họ tên | Chức vụ | Vai trò trong HĐ | Chữ ký |
|:---:|--------|---------|-----------------|--------|
| 1 | | | Chủ tịch HĐ | |
| 2 | | | Thành viên | |
| 3 | | | Thành viên | |
| 4 | | | Thư ký | |
