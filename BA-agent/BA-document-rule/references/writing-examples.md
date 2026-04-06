# WRITING EXAMPLES LIBRARY — Bộ Mẫu Viết cho Từng Section Type (v3.3)

> **Mục đích:** Cung cấp ví dụ viết mẫu cho các section khó — BA junior dùng làm tham khảo.
> **Nguyên tắc:** Mỗi section type có 2-3 ví dụ thực tế (domain: Quản lý Tài sản + E-commerce + HRM).

---

## 1. Precondition — Viết mẫu (3 Patterns)

### Pattern A: UI Precondition

```
Precondition:
  1. User đã đăng nhập với role Admin hoặc KTTS
  2. Module "Quản lý Tài sản" đã enabled trong hệ thống
  3. User đang ở trang Danh sách Tài sản (/assets)
```

### Pattern B: API Precondition

```
Precondition:
  1. Client đã authenticated (Bearer Token valid, chưa expired)
  2. User có permission "asset:create" trong RBAC
  3. Request body conform OpenAPI schema v2.0
```

### Pattern C: Batch Job Precondition

```
Precondition:
  1. Scheduled job "daily-sync" đã enabled trong Admin Console
  2. Source database (HIS) reachable (ping < 100ms)
  3. Destination table "assets" không đang bị locked bởi job khác
  4. Disk space available ≥ 500MB cho temporary files
```

---

## 2. Exception Flow — Viết mẫu (3 Patterns)

### Pattern A: Validation Exception

```
Exception: E1 — Input Validation Failed (tại Bước 3)
  Trigger:   User submit form với field bắt buộc bị trống hoặc invalid
  System:    - Hiển thị lỗi inline dưới field lỗi (đỏ, font 12px)
             - Highlight border field lỗi (border: 2px solid #dc3545)
             - Focus cursor vào field lỗi ĐẦU TIÊN (top-down order)
             - KHÔNG xóa data user đã nhập ở các field khác
  Resume:    User sửa → Re-submit → Quay lại Bước 3
```

### Pattern B: Timeout Exception

```
Exception: E2 — External API Timeout (tại Bước 5)
  Trigger:   Gateway không phản hồi trong 10 giây (timeout threshold)
  System:    - Retry tự động 3 lần (interval: 2s, 4s, 8s — exponential backoff)
             - Nếu retry 3 lần FAIL: show "Dịch vụ tạm gián đoạn. Thử lại sau."
             - Log error: {timestamp, request_id, gateway_url, http_status, attempt_count}
             - Giao dịch ROLLBACK về trạng thái trước Bước 5
  Resume:    User nhấn "Thử lại" → Quay lại Bước 5 (không cần nhập lại)
```

### Pattern C: Permission Exception

```
Exception: E3 — Insufficient Permission (tại Bước 1)
  Trigger:   User access endpoint không có quyền (role Viewer access POST /assets)
  System:    - Return HTTP 403 Forbidden
             - Response body: {"error": "FORBIDDEN", "message": "Bạn không có quyền thực hiện thao tác này", "required_permission": "asset:create"}
             - Log: {user_id, attempted_action, required_role, timestamp}
             - UI: Redirect về trang trước + Toast warning
  Resume:    User liên hệ Admin để cấp quyền
```

---

## 3. Business Rule — Viết mẫu (3 Formats)

### Format A: IF/THEN/ELSE (Đơn giản)

```markdown
**BR-APPROVE-001: Phê duyệt mua sắm theo giá trị**

IF    asset_value > 500,000,000 VND  THEN  Approver = "Giám đốc"
ELIF  asset_value > 100,000,000 VND  THEN  Approver = "Phó Giám đốc"
ELSE                                 THEN  Approver = "Trưởng phòng"

Note: asset_value = đơn giá × số lượng (trước thuế)
```

### Format B: Truth Table (Nhiều điều kiện kết hợp)

```markdown
**BR-DISCOUNT-001: Tính chiết khấu đơn hàng**

| Loại KH | Giá trị đơn | Lần mua thứ | Discount |
|---------|:-----------:|:----------:|:--------:|
| VIP | > 10M | Any | 15% |
| VIP | ≤ 10M | Any | 10% |
| Regular | > 10M | ≥ 5 | 8% |
| Regular | > 10M | < 5 | 5% |
| Regular | ≤ 10M | Any | 0% |
| New | Any | 1 | 5% (welcome) |
| New | Any | > 1 | → becomes Regular |

Precedence: VIP rules override Regular rules.
Stacking: Discount KHÔNG được cộng dồn (chọn rate cao nhất).
```

### Format C: State-based Rule (Phụ thuộc trạng thái)

```markdown
**BR-TRANSFER-001: Quy tắc điều chuyển tài sản**

| Current State | Action Allowed | Condition | Next State |
|:-------------:|:--------------:|-----------|:----------:|
| In Use | Transfer | Approved by both dept heads | Transferring |
| In Use | Repair Request | Has warranty OR approved budget | Under Repair |
| In Use | Dispose | Asset age ≥ depreciation period | Pending Disposal |
| Under Repair | Return to Use | Repair completed + QC passed | In Use |
| Under Repair | Write Off | Repair cost > 50% current value | Disposed |
| Transferring | Received | Receiving dept confirms | In Use (new dept) |
| Transferring | Rejected | Receiving dept rejects | In Use (original dept) |

Rule: Disposed assets CANNOT return to any other state (terminal state).
```

---

## 4. NFR — Viết mẫu (theo Category)

### Performance NFR

```markdown
**NFR-PERF-001: API Response Time**
  Statement: API PHẢI trả response trong điều kiện 500 concurrent users
  Metric: Response time (p95)
  Target: < 500ms cho GET, < 1000ms cho POST
  Measurement: k6 load test, Grafana dashboard
  Boundary: p99 < 2000ms (soft limit) | > 5000ms = Critical alert

**NFR-PERF-002: Page Load Time**
  Statement: Trang Dashboard PHẢI load hoàn chỉnh (LCP)
  Metric: Largest Contentful Paint
  Target: < 2.5s trên 4G mobile connection
  Measurement: Lighthouse CI, Chrome DevTools
```

### Security NFR

```markdown
**NFR-SEC-001: Authentication**
  Statement: Hệ thống PHẢI authenticate user qua JWT + Refresh Token
  Spec: Access Token TTL = 15 min | Refresh Token TTL = 7 days
  Password Policy: ≥ 8 chars, 1 uppercase, 1 number, 1 special
  Lockout: 5 failed attempts → lock 15 min → email notification

**NFR-SEC-002: Data Encryption**
  Statement: Dữ liệu PII PHẢI được mã hóa
  In-transit: TLS 1.3 (minimum TLS 1.2)
  At-rest: AES-256-GCM cho database columns: [name, phone, email, cmnd]
  Key Management: AWS KMS / Azure Key Vault (auto-rotation 90 days)
```

### Availability NFR

```markdown
**NFR-AVA-001: Uptime SLA**
  Statement: Hệ thống PHẢI đạt availability target trong business hours
  Target: 99.9% uptime (≤ 8.76 hrs downtime/year)
  Business Hours: 7:00 - 22:00 GMT+7 (Mon-Sat)
  Planned Maintenance: 2:00 - 5:00 Chủ nhật (pre-announced 48h)
  
**NFR-AVA-002: Disaster Recovery**
  RTO (Recovery Time Objective): ≤ 30 minutes
  RPO (Recovery Point Objective): ≤ 1 hour
  Backup: Daily full + hourly incremental → S3 cross-region
  DR Test: Quarterly simulation (documented in PIR)
```

---

## 5. Integration Spec — Viết mẫu

### API Contract

```markdown
**INT-HIS-001: Lấy thông tin bệnh nhân từ HIS**

Endpoint: GET /api/v1/patients/{patient_id}
Auth: Bearer Token (service-to-service, OAuth2 client_credentials)
Timeout: 10s | Retry: 3x exponential backoff (2s, 4s, 8s)

Request:
  Headers: { Authorization: "Bearer {token}", Content-Type: "application/json" }
  Path Params: { patient_id: string (UUID format) }

Response (200 OK):
  { 
    "id": "uuid", "name": "string", "dob": "YYYY-MM-DD",
    "department": "string", "bed_number": "string|null"
  }

Error Responses:
  | HTTP Code | Error Code | Meaning | Action |
  |:---------:|:----------:|---------|--------|
  | 404 | PATIENT_NOT_FOUND | ID không tồn tại | Show "Không tìm thấy BN" |
  | 401 | TOKEN_EXPIRED | Token hết hạn | Auto-refresh token → retry |
  | 429 | RATE_LIMITED | Quá 100 req/min | Queue request, retry after 60s |
  | 500 | INTERNAL_ERROR | HIS lỗi nội bộ | Retry 3x → fallback manual input |

Circuit Breaker:
  - Threshold: 5 consecutive failures → OPEN (stop calling for 60s)
  - Half-open: After 60s, try 1 request → if success → CLOSE
  - Fallback: Show "HIS tạm gián đoạn" + allow manual input
```

---

## 6. Test Case — Viết mẫu

```markdown
**TC-AST-001: Thêm tài sản mới - Happy Path**

| Thuộc tính | Chi tiết |
|-----------|---------|
| Test ID | TC-AST-001 |
| Story | US-AST-001 |
| Priority | High |
| Type | Functional — Happy Path |
| Precondition | Admin đã đăng nhập, đang ở /assets |

| Step | Action | Input | Expected Result |
|:----:|--------|-------|----------------|
| 1 | Nhấn "Thêm tài sản" | — | Form thêm tài sản hiển thị, tất cả fields trống |
| 2 | Điền Tên tài sản | "Máy siêu âm GE V9" | Field accept, no error |
| 3 | Điền Mã tài sản | "TS-2026-001" | Field accept, format validated |
| 4 | Chọn Loại tài sản | "TSCĐ" (dropdown) | Dropdown close, value shown |
| 5 | Chọn Vị trí | "Khoa Ngoại - Tầng 3" | Dropdown close, value shown |
| 6 | Điền Giá trị | "500000000" | Auto-format: "500,000,000 VND" |
| 7 | Nhấn "Lưu" | — | Toast "Tạo thành công" ✅ |
| 8 | Verify danh sách | — | Tài sản mới xuất hiện đầu list, Mã TS-2026-001 |

| Status | Tester | Date | Ghi chú |
|:------:|--------|------|---------|
| ☐ Pending | — | — | — |
```

---

## 7. Lệnh Kích hoạt

```
@ba-specialist viết exception flow cho bước [X] theo pattern [validation/timeout/permission]
@ba-specialist viết business rule cho [logic Y] dạng truth table
@ba-specialist viết integration spec cho API [Z] đầy đủ contract + error codes
@ba-specialist viết mẫu NFR cho [Performance/Security/Availability]
```
