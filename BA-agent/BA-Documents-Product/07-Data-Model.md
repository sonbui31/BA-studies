# DATA MODEL & ANALYTICS
# {{Tên sản phẩm}}

> **Phiên bản:** 1.0 | **Ngày:** {{DD/MM/YYYY}}

---

## 1. Core Data Model (ERD)

```
{{Thay thế bằng ERD cụ thể của sản phẩm}}

Ví dụ cho SaaS Product:

┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│   Accounts   │       │    Users     │       │    Roles     │
│  (Tổ chức)   │◄─────▶│ (Người dùng) │◄─────▶│  (Vai trò)  │
└──────┬───────┘       └──────┬───────┘       └──────────────┘
       │                      │
       │ 1:N                  │ 1:N
       ▼                      ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│   Projects   │◄─────▶│   Members    │       │ Invitations  │
│   (Dự án)    │       │ (Thành viên) │       │  (Lời mời)   │
└──────┬───────┘       └──────────────┘       └──────────────┘
       │
       │ 1:N
       ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│    Tasks     │       │  Comments    │       │ Attachments  │
│ (Công việc)  │◄─────▶│ (Bình luận) │       │ (Đính kèm)  │
└──────┬───────┘       └──────────────┘       └──────────────┘
       │
       │ N:M
       ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│    Tags      │       │ Subscriptions│       │  AuditLogs   │
│  (Nhãn)      │       │ (Gói dịch vụ)│       │ (Nhật ký)    │
└──────────────┘       └──────────────┘       └──────────────┘
```

---

## 2. Data Dictionary

### 2.1 Accounts (Tổ chức / Workspace)

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|--------|
| `id` | UUID | PK | |
| `name` | VARCHAR(100) | NOT NULL | Tên tổ chức |
| `slug` | VARCHAR(50) | UNIQUE | URL slug (workspace) |
| `plan` | ENUM | DEFAULT 'FREE' | FREE, PRO, ENTERPRISE |
| `trial_ends_at` | TIMESTAMP | | Ngày hết trial |
| `owner_id` | UUID | FK → Users | Chủ sở hữu |
| `settings` | JSONB | | Cài đặt workspace |
| `created_at` | TIMESTAMP | DEFAULT NOW | |
| `updated_at` | TIMESTAMP | ON UPDATE | |

---

### 2.2 Users (Người dùng)

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|--------|
| `id` | UUID | PK | |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL | |
| `password_hash` | VARCHAR(255) | | Null nếu SSO |
| `full_name` | VARCHAR(100) | NOT NULL | |
| `avatar_url` | VARCHAR(500) | | |
| `auth_provider` | ENUM | DEFAULT 'EMAIL' | EMAIL, GOOGLE, GITHUB |
| `is_verified` | BOOLEAN | DEFAULT FALSE | |
| `last_login_at` | TIMESTAMP | | |
| `onboarding_completed` | BOOLEAN | DEFAULT FALSE | |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

---

### 2.3 Subscriptions (Gói dịch vụ)

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|--------|
| `id` | UUID | PK | |
| `account_id` | UUID | FK → Accounts | |
| `plan` | ENUM | NOT NULL | FREE, PRO, ENTERPRISE |
| `status` | ENUM | NOT NULL | ACTIVE, CANCELLED, PAST_DUE |
| `billing_cycle` | ENUM | | MONTHLY, YEARLY |
| `current_period_start` | TIMESTAMP | | |
| `current_period_end` | TIMESTAMP | | |
| `stripe_subscription_id` | VARCHAR(100) | | Stripe ref |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

---

### 2.4 {{Core Entity}} ({{Tên tiếng Việt}})

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|--------|
| `id` | UUID | PK | |
| `account_id` | UUID | FK → Accounts | Thuộc workspace nào |
| `created_by` | UUID | FK → Users | Người tạo |
| `{{field_1}}` | {{TYPE}} | {{CONSTRAINT}} | {{Mô tả}} |
| `{{field_2}}` | {{TYPE}} | {{CONSTRAINT}} | {{Mô tả}} |
| `status` | ENUM | NOT NULL | {{Các trạng thái}} |
| `created_at` | TIMESTAMP | DEFAULT NOW | |
| `updated_at` | TIMESTAMP | ON UPDATE | |
| `deleted_at` | TIMESTAMP | | Soft delete |

---

### 2.5 AuditLogs (Nhật ký hệ thống)

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|--------|
| `id` | BIGINT | PK, AUTO_INCREMENT | |
| `account_id` | UUID | FK → Accounts | |
| `user_id` | UUID | FK → Users | |
| `action` | VARCHAR(50) | NOT NULL | CREATE, UPDATE, DELETE, etc. |
| `entity_type` | VARCHAR(50) | | |
| `entity_id` | UUID | | |
| `changes` | JSONB | | {old: {}, new: {}} |
| `ip_address` | VARCHAR(45) | | |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

---

## 3. Analytics Data Model

> **Đặc thù Product:** Ngoài business data, cần tracking user behavior.

### 3.1 Analytics Events Schema

| Event | Trigger | Properties |
|-------|---------|-----------|
| `signup_completed` | User hoàn thành đăng ký | `{auth_provider, utm_source, utm_medium}` |
| `onboarding_step_completed` | Mỗi bước onboarding | `{step_number, step_name, time_spent_seconds}` |
| `first_value_achieved` | User đạt "aha moment" | `{time_since_signup_minutes, action_count}` |
| `feature_used` | User dùng 1 feature | `{feature_name, account_plan, session_id}` |
| `upgrade_clicked` | Click nút upgrade | `{current_plan, trigger_location}` |
| `payment_completed` | Thanh toán thành công | `{plan, amount, billing_cycle, coupon}` |
| `churn_risk_detected` | ML model detect risk | `{risk_score, days_inactive, last_feature}` |

### 3.2 Key Dashboards

| Dashboard | Metrics | Audience |
|-----------|---------|----------|
| **Growth** | DAU, WAU, MAU, Sign-up rate | PM, CEO |
| **Activation** | Onboarding funnel, Time-to-value | PM, UX |
| **Retention** | D1/D7/D30, Cohort analysis | PM, Data |
| **Revenue** | MRR, Churn rate, LTV, ARPU | PM, Finance |
| **Feature Adoption** | Feature usage %, Power users | PM, Dev |

---

## 4. Data Business Rules

| # | Rule | Logic | Áp dụng |
|---|------|-------|---------|
| BR-01 | Soft delete cho tất cả entity | Thêm `deleted_at`, không xóa thật | All |
| BR-02 | Multi-tenancy: data isolation | Mọi query phải có `account_id` filter | All |
| BR-03 | Free plan giới hạn | ≤ {{X}} {{resources}}, ≤ {{Y}} members | Subscriptions |
| BR-04 | Trial tự hết hạn | Sau {{X}} ngày, downgrade về FREE | Accounts |
| BR-05 | Audit log bắt buộc | Mọi mutation phải ghi log | AuditLogs |
| BR-06 | GDPR: right to deletion | Xóa user data theo yêu cầu (real delete + anonymize) | Users |
