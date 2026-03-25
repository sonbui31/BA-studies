# MÔ HÌNH DỮ LIỆU & TỪ ĐIỂN DỮ LIỆU — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Rà soát bởi:** [Tech Lead — NCC] | **Phê duyệt bởi:** [CNTT KH]

---

## 1. Đặc thù gia công

| Hạng mục | Nội bộ | Gia công |
|----------|--------|----------|
| Mức chi tiết | Thực thể cốt lõi, Dev tự bổ sung | **Đầy đủ thực thể** — Dev xây đúng theo đặc tả |
| Quy ước đặt tên | Nhóm tự quy ước | **Phải tài liệu hóa** — bàn giao cho KH sau |
| Chuyển đổi dữ liệu | Nhóm hiểu dữ liệu cũ | KH cung cấp **tài liệu ánh xạ** |
| Đặc tả API | Nội bộ | **Swagger/OpenAPI** giao cùng Mô hình dữ liệu |

---

## 2. Quy ước cơ sở dữ liệu

| Quy ước | Quy tắc | Ví dụ |
|---------|---------|-------|
| Tên bảng | snake_case, số nhiều | `users`, `order_items` |
| Tên cột | snake_case | `created_at`, `user_id` |
| Khóa chính | UUID v4 (hoặc BIGINT tự tăng) | `id UUID PK DEFAULT gen_random_uuid()` |
| Khóa ngoại | `{bảng_tham_chiếu_số_ít}_id` | `user_id`, `order_id` |
| Dấu thời gian | `created_at`, `updated_at` trên mọi bảng | `TIMESTAMP WITH TIME ZONE` |
| Soft delete | `deleted_at TIMESTAMP NULL` | NULL = hoạt động, NOT NULL = đã xóa |
| Boolean | Tiền tố `is_` hoặc `has_` | `is_active`, `has_verified` |
| Enum | Dùng VARCHAR + enum ứng dụng | `status VARCHAR(20)` |
| Chỉ mục | Mọi FK + trường tìm kiếm | `CREATE INDEX idx_users_email ON users(email)` |

---

## 3. ERD (ERD)

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│    Users     │       │    Roles     │       │ Permissions  │
│  (Ng. dùng)  │◄─────▶│  (Vai trò)   │◄─────▶│  (Quyền)     │
└──────┬───────┘       └──────────────┘       └──────────────┘
       │
       │ 1:N
       ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ [Thực thể 1] │◄─────▶│ [Thực thể 2] │       │ [Thực thể 3] │
│              │       │              │       │              │
└──────┬───────┘       └──────┬───────┘       └──────────────┘
       │                      │
       │ 1:N                  │ 1:N
       ▼                      ▼
┌──────────────┐       ┌──────────────┐
│ [Thực thể 4] │       │ [Thực thể 5] │
│              │       │              │
└──────────────┘       └──────────────┘

┌──────────────┐       ┌──────────────┐
│  Tệp đính   │       │  Nhật ký     │
│  kèm (Đa    │       │  kiểm toán   │
│  hình)       │       │              │
└──────────────┘       └──────────────┘
```

> **Sản phẩm:** Sơ đồ ERD (draw.io / dbdiagram.io) phải giao kèm tài liệu này

---

## 4. Data Dictionary

### 4.1 Users (Người dùng)

| Cột | Kiểu | Ràng buộc | Mô tả | Mã hóa? |
|-----|------|----------|--------|---------|
| `id` | UUID | PK | | |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL | Email đăng nhập | |
| `password_hash` | VARCHAR(255) | NOT NULL | Mã băm bcrypt | 🔒 |
| `full_name` | VARCHAR(100) | NOT NULL | Họ và tên | |
| `phone` | VARCHAR(20) | | Số điện thoại | 🔒 DLCN |
| `avatar_url` | VARCHAR(500) | | URL ảnh đại diện | |
| `role_id` | UUID | FK → Roles | Vai trò | |
| `is_active` | BOOLEAN | DEFAULT TRUE | Trạng thái hoạt động | |
| `email_verified_at` | TIMESTAMP | NULL | Thời điểm xác thực email | |
| `last_login_at` | TIMESTAMP | NULL | Lần đăng nhập cuối | |
| `created_at` | TIMESTAMP | DEFAULT NOW | | |
| `updated_at` | TIMESTAMP | ON UPDATE | | |
| `deleted_at` | TIMESTAMP | NULL | Soft delete | |

**Chỉ mục:** `email` (duy nhất), `role_id`, `is_active`
**Dữ liệu khởi tạo:** 1 tài khoản Quản trị tối cao

> 🔒 = Cần mã hóa | DLCN = Dữ liệu cá nhân

---

### 4.2 Roles (Vai trò)

| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|----------|--------|
| `id` | UUID | PK | |
| `name` | VARCHAR(50) | UNIQUE, NOT NULL | Tên vai trò (VD: admin, manager) |
| `display_name` | VARCHAR(100) | NOT NULL | Tên hiển thị |
| `description` | TEXT | | Mô tả quyền |
| `is_system` | BOOLEAN | DEFAULT FALSE | Vai trò hệ thống (không xóa được) |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

**Dữ liệu khởi tạo:** QT tối cao, Quản trị, Quản lý, Nhân viên, Người xem, Khách hàng

---

### 4.3 [Thực thể 1 — Tên theo nghiệp vụ]

| Cột | Kiểu | Ràng buộc | Mô tả | Mã hóa? |
|-----|------|----------|--------|---------|
| `id` | UUID | PK | | |
| `[trường_1]` | VARCHAR(X) | NOT NULL | [Mô tả] | |
| `[trường_2]` | VARCHAR(X) | | [Mô tả] | |
| `[trường_3]` | DECIMAL(X,Y) | | [Mô tả] | |
| `status` | VARCHAR(20) | NOT NULL, DEFAULT '[khởi tạo]' | Trạng thái | |
| `[khóa_ngoại]_id` | UUID | FK → [Bảng] | | |
| `created_by` | UUID | FK → Users | Người tạo | |
| `created_at` | TIMESTAMP | DEFAULT NOW | | |
| `updated_at` | TIMESTAMP | ON UPDATE | | |
| `deleted_at` | TIMESTAMP | NULL | Soft delete | |

**Enum trạng thái:**

| Giá trị | Mô tả | Màu UI | Chuyển từ |
|---------|--------|--------|----------|
| `DRAFT` | Nháp | ⚪ Xám | — (khởi tạo) |
| `ACTIVE` | Đang hoạt động | 🟢 Xanh lá | DRAFT |
| `COMPLETED` | Hoàn thành | 🔵 Xanh dương | ACTIVE |
| `CANCELLED` | Đã hủy | 🔴 Đỏ | DRAFT, ACTIVE |

---

### 4.4 Attachments (Attachment — Đa hình)

| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|----------|--------|
| `id` | UUID | PK | |
| `attachable_type` | VARCHAR(50) | NOT NULL | Loại thực thể (VD: 'order', 'user') |
| `attachable_id` | UUID | NOT NULL | ID thực thể cha |
| `file_name` | VARCHAR(255) | NOT NULL | Tên tệp gốc |
| `file_path` | VARCHAR(500) | NOT NULL | Đường dẫn trên bộ lưu trữ |
| `file_size` | BIGINT | | Bytes |
| `mime_type` | VARCHAR(100) | | application/pdf, image/jpeg... |
| `uploaded_by` | UUID | FK → Users | |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

---

### 4.5 Audit_Logs (Audit Log)

| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|----------|--------|
| `id` | BIGSERIAL | PK | |
| `user_id` | UUID | FK → Users | Người thực hiện |
| `action` | VARCHAR(20) | NOT NULL | CREATE, UPDATE, DELETE, LOGIN |
| `entity_type` | VARCHAR(50) | | Loại thực thể |
| `entity_id` | UUID | | ID thực thể |
| `old_values` | JSONB | | Giá trị cũ |
| `new_values` | JSONB | | Giá trị mới |
| `ip_address` | VARCHAR(45) | | IPv4/IPv6 |
| `user_agent` | VARCHAR(300) | | Trình duyệt/Ứng dụng |
| `created_at` | TIMESTAMP | DEFAULT NOW | Không thay đổi |

> **Không soft delete** — audit log không bao giờ bị xóa
> **Lưu giữ:** [X tháng], lưu trữ lạnh sau đó

---

## 5. Chuyển đổi dữ liệu (nếu có)

### 5.1 Ánh xạ chuyển đổi

| Trường cũ | Kiểu cũ | Bảng.Cột mới | Kiểu mới | Quy tắc chuyển đổi |
|----------|---------|-------------|----------|-------------------|
| [trường_cũ_1] | VARCHAR | [bảng_mới].[trường_mới] | VARCHAR | Sao chép trực tiếp |
| [trường_cũ_2] | INT | [bảng_mới].[trường_mới] | UUID | Tra cứu từ bảng ánh xạ |
| [trường_cũ_3] | TEXT | [bảng_mới].[trường_mới] | JSONB | Phân tích CSV → JSON |

### 5.2 Phân công trách nhiệm chuyển đổi

| Công việc | Chịu trách nhiệm | Ghi chú |
|----------|-------------------|---------|
| Cung cấp xuất dữ liệu cũ | **Khách hàng** | CSV/SQL dump |
| Viết script chuyển đổi | **Nhà cung cấp** | |
| Xác nhận dữ liệu đã chuyển | **Khách hàng** + NCC | So sánh song song |
| Làm sạch/loại bỏ trùng lặp | **Khách hàng** quyết định quy tắc | NCC triển khai |

---

## 6. Tóm tắt đặc tả API

> **Đặc tả đầy đủ:** File Swagger/OpenAPI — giao riêng

### Tổng quan Endpoint chính

| Phương thức | Endpoint | Mô tả | Xác thực |
|------------|----------|-------|----------|
| POST | `/api/v1/auth/login` | Đăng nhập | Công khai |
| POST | `/api/v1/auth/register` | Đăng ký | Công khai |
| GET | `/api/v1/[thực_thể]` | Danh sách (phân trang) | Token Bearer |
| POST | `/api/v1/[thực_thể]` | Tạo mới | Token Bearer |
| GET | `/api/v1/[thực_thể]/:id` | Lấy theo ID | Token Bearer |
| PUT | `/api/v1/[thực_thể]/:id` | Cập nhật | Token Bearer |
| DELETE | `/api/v1/[thực_thể]/:id` | Soft delete | Token Bearer |

### Định dạng phản hồi chuẩn

```json
{
  "success": true,
  "data": { ... },
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 150,
    "total_pages": 8
  },
  "message": "OK"
}
```

### Định dạng phản hồi lỗi

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      { "field": "email", "message": "Email is required" }
    ]
  }
}
```

---

## 7. Sign-off

| Vai trò | Bên | Họ tên | Ngày |
|---------|-----|--------|------|
| CNTT/PO KH | Khách hàng | | |
| Tech Lead | Nhà cung cấp | | |
| BA Lead | Nhà cung cấp | | |
