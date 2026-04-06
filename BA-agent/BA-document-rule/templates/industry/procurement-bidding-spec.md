# HỒ SƠ MỜI THẦU & ĐẤU THẦU — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Áp dụng:** 🏛️ Government only
> **Mục đích:** Chuẩn bị đặc tả kỹ thuật cho gói thầu CNTT + ước lượng ngân sách

---

## 1. Thông tin gói thầu

| Hạng mục | Chi tiết |
|---------|---------|
| **Tên gói thầu** | {{Tên}} |
| **Chủ đầu tư** | {{Tên cơ quan}} |
| **Nguồn vốn** | {{NSNN / ODA / PPP}} |
| **Giá gói thầu** | {{VNĐ}} |
| **Hình thức lựa chọn** | {{Đấu thầu rộng rãi / Hạn chế / Chỉ định}} |
| **Phương thức đấu thầu** | {{Một giai đoạn một túi hồ sơ / Hai giai đoạn}} |
| **Thời gian thực hiện HĐ** | {{N tháng}} |
| **Thời gian bảo hành** | {{12 tháng}} |

---

## 2. Yêu cầu năng lực nhà thầu

| # | Tiêu chí | Yêu cầu | Tài liệu chứng minh |
|---|---------|---------|---------------------|
| 1 | Kinh nghiệm | ≥ {{N}} dự án CNTT tương tự trong {{N}} năm gần nhất | Hợp đồng + Biên bản nghiệm thu |
| 2 | Năng lực tài chính | Doanh thu trung bình {{N}} năm ≥ {{X}} tỷ | Báo cáo tài chính đã kiểm toán |
| 3 | Nhân sự chủ chốt | PM (≥ {{N}} năm), BA (≥ {{N}} năm), Tech Lead (≥ {{N}} năm) | CV + Bảng chấm kinh nghiệm |
| 4 | Chứng chỉ | {{ISO 27001 / CMMI / tương đương}} | Chứng chỉ còn hiệu lực |

---

## 3. Đặc tả kỹ thuật (Phụ lục HSMT)

> ⚠️ Đây là bản tóm tắt. Chi tiết đầy đủ ở SRS.

### 3.1 Yêu cầu chức năng tổng quan

| # | Module / Phân hệ | Mô tả | Số CR ước tính | MoSCoW |
|---|-----------------|-------|:-------------:|:------:|
| 1 | {{Module}} | {{Mô tả}} | {{N}} | Must |

### 3.2 Yêu cầu kỹ thuật

| Hạng mục | Yêu cầu |
|---------|---------|
| **Nền tảng** | {{Web / Desktop / Mobile / Hybrid}} |
| **Kiến trúc** | {{Monolithic / Microservices / SOA}} |
| **Database** | {{PostgreSQL / Oracle / SQL Server}} |
| **Tích hợp** | {{LGSP / NGSP / API hệ thống khác}} |
| **Bảo mật** | {{Cấp độ ATTT theo NĐ 85/2016}} |
| **Backup** | {{RPO / RTO}} |

### 3.3 Yêu cầu hạ tầng

| Hạng mục | Bên cung cấp | Ghi chú |
|---------|-------------|---------|
| Server vật lý / Cloud | {{CĐT / Nhà thầu}} | {{Cấu hình tối thiểu}} |
| SSL Certificate | {{CĐT}} | {{Wildcard / đơn domain}} |
| Tên miền | {{CĐT}} | {{.gov.vn}} |

---

## 4. Bảng ước lượng khối lượng (ROM)

| # | Hạng mục | Đơn vị | Khối lượng | Đơn giá | Thành tiền |
|---|---------|-------|:----------:|--------:|----------:|
| 1 | Phân tích & Thiết kế | Manday | {{N}} | {{X}} | {{Total}} |
| 2 | Lập trình | Manday | {{N}} | {{X}} | {{Total}} |
| 3 | Kiểm thử | Manday | {{N}} | {{X}} | {{Total}} |
| 4 | Triển khai & Đào tạo | Manday | {{N}} | {{X}} | {{Total}} |
| 5 | Bản quyền phần mềm | License | {{N}} | {{X}} | {{Total}} |
| 6 | Bảo hành 12 tháng | Gói | 1 | {{X}} | {{Total}} |
| | **TỔNG** | | | | **{{Total}}** |

---

## 5. Kế hoạch đào tạo CBCC

| # | Đối tượng | Nội dung | Hình thức | Thời lượng | Số lượng |
|---|----------|---------|----------|:----------:|:--------:|
| 1 | Admin hệ thống | Quản trị, backup, monitoring | Tại chỗ + Tài liệu | {{N}} buổi | {{N}} người |
| 2 | End-user (CBCC) | Sử dụng các phân hệ | Tại chỗ + Video | {{N}} buổi | {{N}} người |
| 3 | Lãnh đạo | Dashboard, báo cáo | Online | {{1}} buổi | {{N}} người |

**Sản phẩm đào tạo:**
- [ ] Tài liệu hướng dẫn sử dụng (PDF)
- [ ] Video hướng dẫn từng chức năng
- [ ] FAQ thường gặp
- [ ] Hotline hỗ trợ trong thời gian bảo hành

---

## 6. Tiến độ thực hiện (gắn với Payment Milestone)

```mermaid
gantt
    title Tiến độ gói thầu — {{Tên dự án}}
    dateFormat  YYYY-MM-DD

    section Ký HĐ & Khởi động
        Ký hợp đồng + Tạm ứng (M0)      :milestone, m0, {{date}}, 0d
        Khảo sát & Phân tích              :a1, after m0, 30d

    section Thiết kế & Phát triển
        Thiết kế chi tiết (SRS)           :b1, after a1, 21d
        Sign-off thiết kế (M1)            :milestone, m1, after b1, 0d
        Phát triển Release 1              :c1, after b1, 60d
        Nghiệm thu sơ bộ R1 (M2)         :milestone, m2, after c1, 0d

    section Vận hành thử
        Vận hành thử (30-90 ngày)         :d1, after c1, 60d
        Nghiệm thu chính thức (M3)        :milestone, m3, after d1, 0d

    section Bảo hành
        Bảo hành 12 tháng                 :e1, after d1, 365d
        Thanh toán cuối (M4)              :milestone, m4, after e1, 0d
```

---

## ✅ Checklist HSMT

```
☐ Thông tin gói thầu đầy đủ (tên, nguồn vốn, giá, hình thức)
☐ Yêu cầu năng lực nhà thầu rõ ràng + đo lường được
☐ Đặc tả kỹ thuật đủ chi tiết để nhà thầu báo giá chính xác
☐ Bảng ước lượng có đơn vị + đơn giá + justify
☐ Kế hoạch đào tạo bao gồm tài liệu + video + hỗ trợ
☐ Tiến độ gắn với payment milestone
☐ Yêu cầu ATTT theo đúng cấp độ
```
