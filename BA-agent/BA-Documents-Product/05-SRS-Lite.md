# FUNCTIONAL SPECIFICATIONS (LITE)
# {{Tên sản phẩm}}

> **Phiên bản:** 1.0 | **Ngày:** {{DD/MM/YYYY}}
> **Trạng thái:** Draft | **Tham chiếu:** BRD v1.0

> ⚠️ **Product Note:** Trong dự án Product, SRS Lite là tài liệu **tùy chọn**.
> Thường chỉ dùng cho technical features phức tạp (API integration, complex business rules).
> Đa số features được mô tả qua **User Stories chi tiết** trong `06-User-Story-Map.md`.

---

## 1. Tổng quan

### 1.1 Mục đích
Mô tả kỹ thuật chi tiết cho các tính năng phức tạp không thể cover đầy đủ bằng User Stories.

### 1.2 Tài liệu tham chiếu
- `01-Vision-Scope.md`
- `02-BRD.md`
- `04-User-Flow.md`

---

## 2. API Specifications

### 2.1 API Overview

| Method | Endpoint | Mô tả |
|--------|---------|-------|
| POST | `/api/v1/{{resource}}` | Tạo mới {{resource}} |
| GET | `/api/v1/{{resource}}` | Lấy danh sách (paginated) |
| GET | `/api/v1/{{resource}}/:id` | Lấy chi tiết |
| PUT | `/api/v1/{{resource}}/:id` | Cập nhật |
| DELETE | `/api/v1/{{resource}}/:id` | Xóa (soft delete) |

### 2.2 API Detail — {{API Name}}

**Endpoint:** `POST /api/v1/{{resource}}`

**Request:**
```json
{
  "field_1": "string (required)",
  "field_2": "number (optional)",
  "field_3": {
    "nested_field": "string"
  }
}
```

**Response (201 Created):**
```json
{
  "id": "uuid",
  "field_1": "string",
  "created_at": "ISO 8601"
}
```

**Error Responses:**
| Status | Code | Message |
|--------|------|---------|
| 400 | `VALIDATION_ERROR` | Field X is required |
| 401 | `UNAUTHORIZED` | Invalid or expired token |
| 409 | `DUPLICATE` | Resource already exists |
| 500 | `INTERNAL_ERROR` | Something went wrong |

---

## 3. Business Rules (Phức tạp)

> Chỉ document ở đây khi business rules quá complex cho AC trong User Story.

| ID | Rule | Logic | Áp dụng cho |
|----|------|-------|-------------|
| BIZ-01 | {{Tên rule}} | {{Mô tả logic chi tiết}} | {{Feature}} |
| BIZ-02 | {{Tên rule}} | {{Mô tả}} | {{Feature}} |

---

## 4. Yêu cầu Phi chức năng (NFR)

| ID | Loại | Yêu cầu | Chỉ tiêu |
|----|------|---------|----------|
| NFR-01 | **Performance** | Thời gian phản hồi API | ≤ 200ms (P95) |
| NFR-02 | **Performance** | Số request đồng thời | ≥ {{X}} req/s |
| NFR-03 | **Availability** | Uptime | ≥ 99.9% |
| NFR-04 | **Security** | Xác thực | JWT + OAuth 2.0 |
| NFR-05 | **Security** | Dữ liệu nhạy cảm | AES-256 at rest, TLS 1.3 in transit |
| NFR-06 | **Security** | Audit log | Ghi log mọi mutation |
| NFR-07 | **Scalability** | Horizontal scaling | Stateless services, auto-scale |
| NFR-08 | **Usability** | Responsive | Desktop + Tablet + Mobile |
| NFR-09 | **Compatibility** | Browser | Chrome, Firefox, Safari, Edge (latest 2) |
| NFR-10 | **Data** | Backup | Daily automated backup, 30-day retention |
| NFR-11 | **Compliance** | GDPR/Privacy | Data export, deletion, consent management |

---

## 5. Integration Specifications

| # | External Service | Purpose | Protocol | Auth |
|---|-----------------|---------|----------|------|
| 1 | {{Service A}} | {{Mục đích}} | REST API | API Key |
| 2 | {{Service B}} | {{Mục đích}} | Webhook | Shared Secret |
| 3 | {{Service C}} | {{Mục đích}} | OAuth 2.0 | Client Credentials |

---

## 6. Phân quyền (RBAC)

| Role | Permissions | Scope |
|------|-----------|-------|
| **Admin** | Full access | All resources |
| **Member** | CRUD own resources, view team resources | Own + Team |
| **Viewer** | Read-only | Shared resources |
| **Guest** | Limited free features | Public resources |
