# ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)
# Dự án Gia công: [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Trạng thái:** Draft
> **Hợp đồng tham chiếu:** [HĐ-ID]
> **⚠️ Đây là tài liệu BASELINE — mọi thay đổi sau sign-off phải qua quy trình CR**

---

## 1. Tổng quan

### 1.1 Mục đích
Đặc tả yêu cầu phần mềm chi tiết cho dự án **[Tên dự án]** — đủ để đội phát triển NCC phát triển mà **giảm thiểu cần giao tiếp thời gian thực** với KH (đặc điểm gia công).

### 1.2 Đối tượng đọc

| Đối tượng | Đọc phần |
|-----------|---------|
| PO/Sponsor KH | Mục 1-4, 7 (phạm vi, tính năng, sign-off) |
| Đội phát triển NCC | Mục 2-6 (chi tiết chức năng, NFR, dữ liệu, API) |
| QC NCC | Mục 2-3, 5 (tiêu chí chấp nhận, NFR, quy tắc xác nhận) |
| BA NCC | Toàn bộ |

### 1.3 Tài liệu tham chiếu

| Tài liệu | Mã/Link | Phiên bản |
|-----------|---------|-----------|
| Tầm nhìn & Phạm vi | [Link] | v1.0 đã ký |
| Hợp đồng | HĐ-[ID] | Đã ký |
| Quy trình nghiệp vụ | [Link] | v1.0 đã ký |
| Story Map | [Link] | v1.0 |
| Wireframe/Prototype | [Link Figma] | v[X] |

### 1.4 Thuật ngữ & Viết tắt

| Thuật ngữ | Giải thích |
|-----------|------------|
| [Thuật ngữ 1] | [Định nghĩa] |
| [Thuật ngữ 2] | [Định nghĩa] |
| [Thuật ngữ 3] | [Định nghĩa] |

---

## 2. Yêu cầu chức năng

> **Quy ước ưu tiên:**
> - **P0 (Bắt buộc):** Phải có, ảnh hưởng payment milestone
> - **P1 (Nên có):** Quan trọng, nên có trước vận hành
> - **P2 (Có thể):** Tốt nếu có, có thể hoãn sang giai đoạn sau

### 2.1 Module 1: [Tên Module — VD: Quản lý người dùng]

#### Tính năng 1.1: [Tên — VD: Đăng ký người dùng]

| Mã | Yêu cầu | Mô tả chi tiết | Ưu tiên | Ref Wireframe |
|----|---------|-----------------|---------|---------------|
| FR-101 | [Tên] | [Mô tả đầy đủ hành vi mong đợi] | P0 | Màn hình 1.1 |
| FR-102 | [Tên] | [Mô tả] | P0 | Màn hình 1.2 |
| FR-103 | [Tên] | [Mô tả] | P1 | Màn hình 1.3 |

**Quy tắc nghiệp vụ:**
- BR-101: [Quy tắc nghiệp vụ 1]
- BR-102: [Quy tắc nghiệp vụ 2]

**Quy tắc xác nhận:**
- VR-101: [Trường X] phải [xác nhận gì]
- VR-102: [Trường Y] định dạng [quy định]

**Acceptance Criteria (FR-101):**
```gherkin
Scenario: [Happy path]
  Given [điều kiện tiên quyết]
  When [hành động]
  Then [kết quả mong đợi]
    And [xác nhận bổ sung]

Scenario: [Trường hợp lỗi]
  Given [điều kiện tiên quyết]
  When [hành động không hợp lệ]
  Then [xử lý lỗi]
```

---

#### Tính năng 1.2: [Tên — VD: Đăng nhập]

| Mã | Yêu cầu | Mô tả chi tiết | Ưu tiên | Ref Wireframe |
|----|---------|-----------------|---------|---------------|
| FR-110 | [Tên] | [Mô tả] | P0 | Màn hình 2.1 |
| FR-111 | [Tên] | [Mô tả] | P0 | Màn hình 2.2 |

---

### 2.2 Module 2: [Tên Module]

#### Tính năng 2.1: [Tên]

| Mã | Yêu cầu | Mô tả chi tiết | Ưu tiên | Ref Wireframe |
|----|---------|-----------------|---------|---------------|
| FR-201 | [Tên] | [Mô tả] | P0 | Màn hình 3.1 |
| FR-202 | [Tên] | [Mô tả] | P1 | Màn hình 3.2 |

---

### 2.3 Module 3: [Tên Module]

_(Thêm modules tương tự)_

---

## 3. Yêu cầu phi chức năng (NFR)

| Mã | Danh mục | Yêu cầu | Chỉ tiêu | Cách xác minh |
|----|----------|---------|----------|---------------|
| NFR-01 | **Hiệu năng** | Thời gian tải trang | ≤ 3 giây (3G) | Điểm Lighthouse ≥ 80 |
| NFR-02 | **Hiệu năng** | Thời gian phản hồi API | ≤ 500ms (p95) | Báo cáo load test |
| NFR-03 | **Hiệu năng** | Người dùng đồng thời | ≥ [X] người | Kiểm thử K6/JMeter |
| NFR-04 | **Khả dụng** | Thời gian hoạt động | ≥ 99.5% | Công cụ giám sát |
| NFR-05 | **Mở rộng** | Mở rộng ngang | Hỗ trợ [X]→[10X] người dùng | Rà soát kiến trúc |
| NFR-06 | **Bảo mật** | Xác thực | JWT + refresh token, 2FA tùy chọn | Kiểm tra bảo mật |
| NFR-07 | **Bảo mật** | Phân quyền | RBAC với [N] vai trò | Kịch bản kiểm thử |
| NFR-08 | **Bảo mật** | Mã hóa dữ liệu | TLS 1.2+ truyền tải, AES-256 lưu trữ | Quét bảo mật |
| NFR-09 | **Bảo mật** | OWASP Top 10 | Không có lỗ hổng Nghiêm trọng/Cao | Quét OWASP ZAP |
| NFR-10 | **Bảo mật** | Audit Log | Ghi tất cả thao tác CRUD | Rà soát nhật ký |
| NFR-11 | **Khả dụng** | Responsive | Di động, Máy tính bảng, Máy tính | Kiểm thử trình duyệt |
| NFR-12 | **Khả dụng** | Hỗ trợ trình duyệt | Chrome, Safari, Firefox, Edge (2 phiên bản mới nhất) | Kiểm thử đa trình duyệt |
| NFR-13 | **Tin cậy** | Sao lưu | Tự động hàng ngày, lưu 30 ngày | Kiểm thử sao lưu |
| NFR-14 | **Tin cậy** | Khắc phục thảm họa | RTO ≤ 4 giờ, RPO ≤ 1 giờ | Diễn tập DR |
| NFR-15 | **Bảo trì** | Chất lượng mã | SonarQube Quality Gate đạt | Báo cáo CI |
| NFR-16 | **Bảo trì** | Độ phủ kiểm thử | ≥ 80% unit test | Báo cáo CI |
| NFR-17 | **Tuân thủ** | Bảo mật dữ liệu | [GDPR/PDPA/Quy định địa phương] | Danh mục tuân thủ |

---

## 4. Phân quyền (RBAC)

### 4.1 Định nghĩa vai trò

| Vai trò | Mô tả | Tạo bởi |
|---------|--------|---------|
| **Quản trị tối cao** | Toàn quyền, quản lý hệ thống | Cài đặt sẵn |
| **Quản trị** | Quản lý người dùng, cấu hình | Quản trị tối cao |
| **Quản lý** | Xem báo cáo, phê duyệt | Quản trị |
| **Nhân viên** | Thao tác nghiệp vụ chính | Quản trị |
| **Người xem** | Chỉ đọc | Quản trị |
| **Khách hàng** | Tự đăng ký, truy cập hạn chế | Tự đăng ký |

### 4.2 Ma trận phân quyền

| Tính năng | QT tối cao | Quản trị | Quản lý | Nhân viên | Người xem | Khách hàng |
|-----------|-----------|----------|---------|-----------|-----------|-----------|
| Quản lý người dùng | CRUD | CRUD | R | — | — | — |
| [Module 1] | CRUD | CRUD | CRUD | CRUD | R | R (riêng) |
| [Module 2] | CRUD | CRUD | CRU | CR | R | — |
| Báo cáo | Toàn bộ | Toàn bộ | Phòng mình | Cá nhân | — | — |
| Cài đặt | Toàn bộ | Toàn bộ | — | — | — | — |
| Audit Log | R | R | — | — | — | — |

> **Chú thích:** C=Tạo, R=Đọc, U=Sửa, D=Xóa, —=Không truy cập

---

## 5. Yêu cầu tích hợp

### 5.1 API bên ngoài

| # | Hệ thống | Hướng | Giao thức | Xác thực | Chủ quản | Trạng thái |
|---|---------|-------|-----------|----------|----------|-----------|
| INT-01 | [Cổng thanh toán] | Gửi đi | REST API | API Key | KH | Sandbox sẵn sàng |
| INT-02 | [Dịch vụ email] | Gửi đi | SMTP / API | API Key | NCC | — |
| INT-03 | [Nhà cung cấp SMS] | Gửi đi | REST API | API Key+Secret | KH | Chờ |
| INT-04 | [Hệ thống cũ] | Hai chiều | REST/SOAP | OAuth2 | CNTT KH | Chờ tài liệu API |
| INT-05 | [SSO] | Nhận vào | OIDC/SAML | Client ID | CNTT KH | — |

### 5.2 API do NCC xây dựng

| # | Nhóm Endpoint | Mô tả | Người sử dụng |
|---|-------------|-------|---------------|
| API-01 | /api/v1/auth/* | Xác thực & phân quyền | Frontend, Di động |
| API-02 | /api/v1/[module1]/* | [Module 1] CRUD | Frontend |
| API-03 | /api/v1/[module2]/* | [Module 2] CRUD | Frontend |
| API-04 | /api/v1/reports/* | Tạo báo cáo | Frontend, Bộ lập lịch |
| API-05 | /api/v1/webhooks/* | Nhận webhook | Bên thứ 3 |

> **Sản phẩm:** Swagger/OpenAPI spec phải được giao cùng sign-off SRS

---

## 6. Yêu cầu giao diện

### 6.1 Hệ thống thiết kế

| Hạng mục | Đặc tả | Tham chiếu |
|----------|--------|-----------|
| Màu chính | [Mã Hex / Quy chuẩn thương hiệu] | Tài liệu thương hiệu |
| Kiểu chữ | [Tên font], kích thước theo thành phần | Hệ thống thiết kế |
| Bộ biểu tượng | [Material Icons / FontAwesome / Tùy chỉnh] | — |
| Điểm ngắt responsive | Di động: ≤768px, Máy tính bảng: 769-1024px, Máy tính: ≥1025px | — |

### 6.2 Màn hình chính (Ref Wireframe)

| Mã MH | Tên màn hình | Module | Link Wireframe | Ưu tiên |
|-------|-------------|--------|----------------|---------|
| S-001 | Đăng nhập | Xác thực | [Link Figma] | P0 |
| S-002 | Dashboard | Trang chủ | [Link Figma] | P0 |
| S-003 | [Tên màn hình] | Module 1 | [Link Figma] | P0 |
| S-004 | [Tên màn hình] | Module 1 | [Link Figma] | P0 |
| S-005 | [Tên màn hình] | Module 2 | [Link Figma] | P1 |

---

## 7. Ma trận truy vết (RTM)

> ⚠️ **Bắt buộc trong gia công:** Đảm bảo mỗi yêu cầu trong BRD/Hợp đồng đều có triển khai + kiểm thử

| Mục BRD | Mã FR | Wireframe | Story | Kịch bản KT | Trạng thái |
|---------|-------|-----------|-----------|-------------|-----------|
| BRD-101 | FR-101, FR-102 | S-001 | US-001 | TC-001 | ☐ |
| BRD-102 | FR-103 | S-002 | US-002 | TC-002 | ☐ |
| BRD-201 | FR-201 | S-003 | US-010 | TC-010 | ☐ |

---

## 8. Phê duyệt — SRS Baseline

> ⚠️ **Sign-off SRS = Baseline yêu cầu = Cơ sở cho theo dõi CR**
> Mọi thay đổi sau thời điểm này PHẢI đi qua quy trình CR (10-Change-Log.md)

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Product Owner | Khách hàng | | | |
| Quản lý CNTT | Khách hàng | | | |
| Project Manager | Nhà cung cấp | | | |
| BA Lead | Nhà cung cấp | | | |
| Tech Lead | Nhà cung cấp | | | |

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Mã CR | Người |
|-----------|------|----------|-------|-------|
| 0.1 | | Draft đầu tiên | — | BA |
| 0.2 | | Cập nhật theo phản hồi KH | — | BA |
| 1.0 | | **Baseline đã sign-off** | — | BA |
| 1.1 | | [Cập nhật theo CR-001] | CR-001 | BA |
