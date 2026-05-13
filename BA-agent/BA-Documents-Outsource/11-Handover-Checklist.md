# DANH MỤC BÀN GIAO & CHUYỂN GIAO KIẾN THỨC
# Dự án [Tên dự án]

> **⚠️ ĐẶC THÙ GIA CÔNG: Bàn giao là giai đoạn BẮT BUỘC — KH cần tự vận hành sau khi NCC rời đi**

---

## 1. Tại sao bàn giao quan trọng?

| Không có bàn giao | Có bàn giao đầy đủ |
|--------------------|---------------------|
| KH phụ thuộc NCC mãi mãi (khóa chân NCC) | KH tự chủ vận hành & phát triển |
| Không ai biết mã nguồn chạy thế nào | Tài liệu đầy đủ cho nhóm mới |
| Mất mã nguồn nếu NCC đóng cửa | Mã nguồn + toàn quyền sở hữu |
| Lỗi xảy ra không biết sửa ở đâu | Kiến trúc rõ ràng, nhóm biết cách gỡ lỗi |

---

## 2. Danh mục bàn giao

### 2.1. Mã nguồn & Kho lưu trữ

| # | Hạng mục | Định dạng / Vị trí | Trạng thái | KH đã xác nhận |
|---|---------|-------------------|-----------|----------------|
| 1 | Mã nguồn (đầy đủ, phiên bản mới nhất) | Chuyển kho Git | ☐ | ☐ |
| 2 | Tất cả nhánh (main, develop, feature, release) | Git | ☐ | ☐ |
| 3 | Lịch sử Git được bảo toàn | ≥ [X] tháng lịch sử | ☐ | ☐ |
| 4 | .env.example (tất cả biến môi trường có tài liệu) | File trong kho | ☐ | ☐ |
| 5 | README.md (hướng dẫn cài đặt) | File trong kho | ☐ | ☐ |
| 6 | Tệp migration CSDL (đầy đủ, chạy được) | Tệp migration | ☐ | ☐ |
| 7 | Script dữ liệu khởi tạo (dữ liệu test/demo) | Tệp seed | ☐ | ☐ |

### 2.2. Tài liệu

| # | Tài liệu | Định dạng | Trạng thái | Xác nhận |
|---|----------|----------|-----------|---------|
| 1 | **Tổng quan kiến trúc** (công nghệ, sơ đồ hệ thống, tương tác thành phần) | Markdown + sơ đồ | ☐ | ☐ |
| 2 | **Tài liệu API** (Swagger/OpenAPI, tất cả endpoint) | Swagger JSON/YAML | ☐ | ☐ |
| 3 | **Lược đồ CSDL** (ERD + Data Dictionary, mới nhất) | Tài liệu + sơ đồ | ☐ | ☐ |
| 4 | **Hướng dẫn triển khai** (từng bước triển khai sản xuất) | Markdown | ☐ | ☐ |
| 5 | **Cấu hình môi trường** (tất cả biến env, chức năng, cách thiết lập) | Markdown + .env.example | ☐ | ☐ |
| 6 | **Tích hợp bên thứ 3** (vị trí API key, giới hạn, liên hệ) | Markdown | ☐ | ☐ |
| 7 | **Hướng dẫn quản trị** (quản lý người dùng, cấu hình, dữ liệu) | Markdown + ảnh chụp | ☐ | ☐ |
| 8 | **Hướng dẫn sử dụng** (sổ tay người dùng cuối) | PDF/Markdown | ☐ | ☐ |
| 9 | **Hướng dẫn xử lý sự cố** (vấn đề thường gặp + cách sửa) | Markdown | ☐ | ☐ |
| 10 | **Vấn đề đã biết & Nợ kỹ thuật** (ghi nhận trung thực) | Markdown | ☐ | ☐ |

### 2.3. Hạ tầng & DevOps

| # | Hạng mục | Chi tiết | Trạng thái | Xác nhận |
|---|---------|---------|-----------|---------|
| 1 | Thông tin đăng nhập máy chủ | [Ở đâu, cách truy cập] | ☐ | ☐ |
| 2 | Cấu hình CI/CD pipeline | [GitHub Actions / GitLab CI / Jenkins] | ☐ | ☐ |
| 3 | Cấu hình Docker/Container | Dockerfile, docker-compose.yml | ☐ | ☐ |
| 4 | Cài đặt tên miền & DNS | Nhà đăng ký, nameservers | ☐ | ☐ |
| 5 | Chứng chỉ SSL | Nhà cung cấp, ngày hết hạn, quy trình gia hạn | ☐ | ☐ |
| 6 | Cấu hình CDN | [CloudFront / Cloudflare / ...] | ☐ | ☐ |
| 7 | Giám sát & cảnh báo | [Datadog / New Relic / ...], quy tắc cảnh báo | ☐ | ☐ |
| 8 | Cấu hình sao lưu | Lịch, thời gian lưu giữ, quy trình khôi phục | ☐ | ☐ |
| 9 | Tổng hợp nhật ký | [ELK / CloudWatch / ...], vị trí nhật ký | ☐ | ☐ |

### 2.4. Tài khoản & Thông tin đăng nhập

| # | Dịch vụ | Chủ tài khoản | Chuyển cho KH? | Trạng thái |
|---|---------|--------------|---------------|-----------|
| 1 | Nhà cung cấp đám mây (AWS/Azure/GCP) | ☐ KH ☐ NCC | ☐ Chuyển / ☐ KH sở hữu | ☐ |
| 2 | Hosting CSDL | ☐ KH ☐ NCC | ☐ | ☐ |
| 3 | Dịch vụ email (SendGrid/SES) | ☐ KH ☐ NCC | ☐ | ☐ |
| 4 | Nhà cung cấp SMS | ☐ KH ☐ NCC | ☐ | ☐ |
| 5 | Cổng thanh toán | ☐ KH ☐ NCC | ☐ | ☐ |
| 6 | Phân tích (GA/Mixpanel) | ☐ KH ☐ NCC | ☐ | ☐ |
| 7 | Theo dõi lỗi (Sentry) | ☐ KH ☐ NCC | ☐ | ☐ |
| 8 | Figma/File thiết kế | ☐ KH ☐ NCC | ☐ | ☐ |
| 9 | Jira/Công cụ quản lý dự án | ☐ KH ☐ NCC | ☐ Xuất dữ liệu | ☐ |

> ⚠️ **Quy tắc:** Tất cả tài khoản nên được chuyển về sở hữu KH trước khi bảo hành kết thúc

### 2.5. Tài liệu kiểm thử

| # | Hạng mục | Định dạng | Trạng thái |
|---|---------|----------|-----------|
| 1 | Kịch bản kiểm thử (tất cả) | Xuất Jira/TestRail | ☐ |
| 2 | Script kiểm thử tự động | Trong kho lưu trữ | ☐ |
| 3 | Bộ dữ liệu kiểm thử | Tệp SQL/CSV | ☐ |
| 4 | Kết quả kiểm thử hiệu năng | Báo cáo | ☐ |
| 5 | Kết quả quét bảo mật | Báo cáo | ☐ |

---

## 3. Các buổi chuyển giao kiến thức (KT)

### 3.1. Lịch KT

| Buổi | Chủ đề | Người trình bày (NCC) | Người tham dự (KH) | Thời lượng | Ngày | Đã ghi? |
|------|--------|----------------------|-------------------|-----------|------|--------|
| KT-01 | Tổng quan kiến trúc & Công nghệ | Trưởng nhóm KT | Đội Dev KH | 2 giờ | | ☐ |
| KT-02 | Hướng dẫn mã nguồn — Frontend | Dev Frontend | Dev KH | 2 giờ | | ☐ |
| KT-03 | Hướng dẫn mã nguồn — Backend + API | Dev Backend | Dev KH | 2 giờ | | ☐ |
| KT-04 | Lược đồ CSDL & Luồng dữ liệu | BA + Backend | Dev KH + DBA | 1.5 giờ | | ☐ |
| KT-05 | DevOps, CI/CD, Triển khai | DevOps | DevOps KH | 1.5 giờ | | ☐ |
| KT-06 | Bảng quản trị & Cấu hình | BA | Quản trị KH | 1 giờ | | ☐ |
| KT-07 | Giám sát, Nhật ký, Xử lý sự cố | DevOps + Trưởng nhóm KT | Vận hành KH | 1 giờ | | ☐ |
| KT-08 | Logic nghiệp vụ & Edge case | BA | PO KH + Dev | 1.5 giờ | | ☐ |

> **Tổng:** ~12-13 giờ buổi KT
> **⚠️ Tất cả buổi phải được GHI HÌNH** — KH có thể xem lại

### 3.2. Thời gian hỏi đáp sau KT
- Sau các buổi KT, NCC sẵn sàng cho hỏi đáp: **[2 tuần]**
- Kênh: [Slack / Email]
- SLA phản hồi: 24 giờ (ngày làm việc)

---

## 4. Chuyển đổi hỗ trợ sau bàn giao

| Giai đoạn | Thời lượng | Mức hỗ trợ NCC | Chi phí |
|-----------|-----------|---------------|---------|
| **Bảo hành** | [30-90] ngày | Sửa lỗi (Nghiêm trọng + Lớn) miễn phí | Bao gồm trong Hợp đồng |
| **Hỗ trợ mở rộng** (tùy chọn) | [3-6] tháng | [X] giờ/tháng, sửa lỗi + thay đổi nhỏ | $[Giá]/tháng |
| **Hợp đồng bảo trì** (tùy chọn) | Liên tục | Hỗ trợ đầy đủ + cập nhật | Thỏa thuận riêng |

---

## 5. Phê duyệt bàn giao

```
═══════════════════════════════════════════════════
         BIÊN BẢN BÀN GIAO
═══════════════════════════════════════════════════

Dự án:      [Tên dự án]
Hợp đồng:   [HĐ-ID]
Ngày:       ___/___/______

Các bên xác nhận đã hoàn tất bàn giao:

☐ Mã nguồn & kho lưu trữ              (Mục 2.1)
☐ Tài liệu                             (Mục 2.2)
☐ Hạ tầng & DevOps                     (Mục 2.3)
☐ Tài khoản & Thông tin đăng nhập      (Mục 2.4)
☐ Tài liệu kiểm thử                   (Mục 2.5)
☐ Các buổi chuyển giao kiến thức       (Mục 3)
☐ Bản ghi đã giao                      (Mục 3)

Hạng mục chưa hoàn tất (nếu có):
1. _____________ — Thời hạn: ___/___/______
2. _____________ — Thời hạn: ___/___/______

Bảo hành bắt đầu: ___/___/______
Bảo hành kết thúc: ___/___/______

CHỮ KÝ:

Khách hàng:   _________________ Ngày: ___/___/______
Nhà cung cấp: _________________ Ngày: ___/___/______

═══════════════════════════════════════════════════
```
