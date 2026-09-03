# 2. SRS — Software Requirements Specification
*Dành cho Đội Dev & QA — Ngôn ngữ kỹ thuật chính xác, chi tiết, đo lường được.*

---

## 2.1 Giới thiệu

- **1.1 Mục đích tài liệu:** Mô tả chi tiết yêu cầu chức năng và phi chức năng cho hệ thống [Tên hệ thống], làm cơ sở để Dev và QA thiết kế, lập trình và kiểm thử.
- **1.2 Phạm vi hệ thống:** Áp dụng cho các modules [Liệt kê modules trong scope]; không bao gồm [Liệt kê ngoài scope].
- **1.3 Định nghĩa & Thuật ngữ viết tắt:**
  - `OTP`: One-Time Password
  - `FR`: Functional Requirement
  - `NFR`: Non-Functional Requirement
  - `BR`: Business Requirement
- **1.4 Tài liệu tham chiếu:**
  - BRD v1.0 ([Ngày])
  - Quy trình nghiệp vụ nội bộ

---

## 2.2 Mô tả tổng quan

- **2.1 Bối cảnh sản phẩm:** [Mô tả ngắn bối cảnh kỹ thuật và nghiệp vụ]
- **2.2 Chức năng chính:** [Liệt kê các chức năng cốt lõi]
- **2.3 Đối tượng người dùng (Actors):** [Khách hàng, Nhân viên, Quản trị viên, Hệ thống ngoài]
- **2.4 Môi trường vận hành:** Web (Chrome, Safari), Mobile (iOS, Android), Cloud Backend
- **2.5 Use Case Diagram tổng quan:**
  - *(Chèn sơ đồ Mermaid Use Case với quan hệ `<<include>>`, `<<extend>>`)*

---

## 2.3 Yêu cầu chức năng (Functional Requirements — FR)

### Phân rã Use Case (Use Case Decomposition)
```text
UC-00: [Tên Use Case tổng]
├── UC-01: [Tên Use Case con 1]
├── UC-02: [Tên Use Case con 2]
└── UC-03: [Tên Use Case con 3]
```

### Ánh xạ Use Case ➔ FR
| Use Case | FR tương ứng | Ghi chú |
|---|---|---|
| **UC-01** | `FR-001a`: [Tên chức năng] | API GET |
| **UC-02** | `FR-001b`: [Tên chức năng] | API GET |
| **UC-03** | `FR-001`: [Tên chức năng chính] | Chi tiết bên dưới |

---

### Chi tiết chức năng: FR-001 — [Tên chức năng]

- **Actor:** [Tên Actor]
- **Mô tả:** [Mô tả chi tiết hành động hệ thống]
- **Pre-condition:** [Điều kiện trước khi thực hiện]
- **Post-condition:** [Điều kiện sau khi thực hiện thành công]

#### Bảng Input & Validation
| Field | Kiểu dữ liệu | Bắt buộc (Required) | Ràng buộc Validation |
|---|---|---|---|
| `field_id` | UUID / String | Có | Phải tồn tại trong bảng [Tên bảng] |
| `date_field` | Date (YYYY-MM-DD) | Có | >= Ngày hiện tại, <= +30 ngày |
| `note` | String | Không | Tối đa 250 ký tự |

#### Xử lý (Processing Logic)
1. Hệ thống kiểm tra dữ liệu đầu vào và trạng thái tài nguyên (real-time check).
2. Khóa tạm thời tài nguyên (giữ chỗ 5 phút) qua DB transaction.
3. Tạo bản ghi mới với trạng thái ban đầu.
4. Gửi thông báo bất đồng bộ qua SMS/Email.

#### Output
- `id`: Mã định danh vừa tạo
- `status`: Trạng thái xử lý
- `data`: Object thông tin chi tiết

#### Luồng chính & Luồng ngoại lệ
- **Main Flow (Luồng chính):**
  1. Người dùng chọn thông tin và bấm xác nhận.
  2. Hệ thống kiểm tra hợp lệ, tạo bản ghi, hiển thị màn hình thành công.
  3. Hệ thống gửi thông báo xác nhận.
- **Exception Flow (Luồng ngoại lệ):**
  - `3a.` Tài nguyên vừa bị người khác chọn trước:
    - ➔ Báo lỗi `ERR_SLOT_TAKEN (HTTP 409 Conflict)`, yêu cầu chọn lại.
  - `3b.` Người dùng chạm ngưỡng giới hạn (theo `BRULE-04`):
    - ➔ Báo lỗi `ERR_LIMIT_REACHED (HTTP 422)`, từ chối tạo mới.

#### Sequence Diagram (Minh họa tương tác)
*(Chèn sơ đồ Sequence Diagram: User ➔ App ➔ Backend ➔ DB ➔ External API)*

#### Bảng Mã lỗi & Thông báo (Error Codes)
| Mã lỗi | HTTP Status | Message hiển thị người dùng |
|---|---|---|
| `ERR_SLOT_TAKEN` | 409 | Khung giờ vừa được đặt, vui lòng chọn giờ khác |
| `ERR_LIMIT_REACHED` | 422 | Bạn đã đạt giới hạn số lịch hẹn đang chờ |
| `ERR_INVALID_INPUT` | 400 | Dữ liệu nhập vào không hợp lệ |

---

## 2.4 Yêu cầu phi chức năng (Non-Functional Requirements — NFR)

| Phân loại | Yêu cầu định lượng cụ thể (SLA / Metric) |
|---|---|
| **Hiệu năng (Performance)** | Thời gian phản hồi API tra cứu ≤ 2 giây; tạo bản ghi ≤ 1 giây |
| **Bảo mật (Security)** | Xác thực OTP 2 lớp; mã hóa thông tin nhạy cảm bằng AES-256; truyền tải qua TLS 1.3 |
| **Mở rộng (Scalability)** | Hỗ trợ tối thiểu 500 CCU đặt lịch đồng thời trong giờ cao điểm |
| **Độ tin cậy (Reliability)** | Uptime 99.5%; cơ chế retry 3 lần khi gửi thông báo thất bại |

---

## 2.5 Mô hình dữ liệu (Data Model / ERD)

- *(Chèn sơ đồ quan hệ thực thể ERD: Entity, Relationships `||--o{`, Attributes PK/FK)*
- Mô tả các quy tắc toàn vẹn dữ liệu.

---

## 2.6 Đặc tả API (API Specification)

```http
POST /api/v1/appointments
Headers:
  Authorization: Bearer {access_token}
  Content-Type: application/json
Body:
  {
    "doctor_id": "DOC-102",
    "slot_id": "SLOT-5002",
    "reason": "Khám tổng quát định kỳ"
  }
Response 201 Created:
  {
    "booking_id": "APT-88213",
    "status": "confirmed"
  }
Response 409 Conflict:
  {
    "error_code": "ERR_SLOT_TAKEN",
    "message": "Khung giờ vừa được đặt, vui lòng chọn giờ khác"
  }
```

---

## 2.7 Giao diện người dùng (UI / Wireframe)

- *(Chèn wireframe bố cục màn hình và các trạng thái element: Active, Hover, Disabled, Selected)*

---

## 2.8 Ma trận truy xuất (Traceability Matrix)

| Mã BR | Mã FR (SRS) | Mã User Story | Test Case / AC | Trạng thái |
|---|---|---|---|---|
| **BR-001** | `FR-001` | `US-021` | `AC-021` | Done |
| **BR-002** | `FR-002` | `US-022` | `AC-022` | Done |
| **BR-003** | `FR-003` | `US-023` | `AC-023` | In Progress |

---

## 2.9 Phụ lục — Module / Package Use Case Diagram
*(Chèn sơ đồ phân rã package nếu hệ thống có nhiều phân hệ)*
