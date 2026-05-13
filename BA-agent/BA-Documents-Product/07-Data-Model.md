# DATA MODEL & ANALYTICS
# SignalDesk

> **Phiên bản:** 1.0 | **Ngày:** 13/05/2026
> **Tham chiếu:** `05-SRS-Lite.md`, `08-Beta-Testing-Plan.md`

---

## 1. Core Data Model (Conceptual ERD)

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  Workspaces  │1    N │ Workspace    │ N   1 │    Users     │
│              │──────▶│ Members      │◀──────│              │
└──────┬───────┘       └──────────────┘       └──────────────┘
       │
       │1
       │
       │N
       ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ FeedbackItem │1    N │ FeedbackVote │       │ Feedback     │
│              │──────▶│              │       │ Subscriber   │
└──────┬───────┘       └──────────────┘       └──────────────┘
       │ 1                                            ▲
       │                                              │
       │ N                                            │ N
       ▼                                              │
┌──────────────┐       ┌──────────────┐               │
│ Feedback     │       │ Feedback     │               │
│ StatusHistory│       │ Merge        │───────────────┘
└──────────────┘       └──────────────┘
       │
       │
       ▼
┌──────────────┐       ┌────────────────────┐       ┌──────────────┐
│ ReleaseNote  │1    N │ ReleaseNoteFeedback│ N   1 │ FeedbackItem │
└──────────────┘       └────────────────────┘       └──────────────┘

AuditLog và AnalyticsEvent là cross-cutting entities ghi nhận mutation và hành vi người dùng.
```

### 1.1. Entity Responsibility Summary

| Entity | Vai trò | Ref |
|--------|---------|-----|
| `Workspace` | Tenant gốc cho toàn bộ dữ liệu | `BR-001` đến `BR-005` |
| `WorkspaceMember` | Quy định quyền nội bộ như Admin, PM, CS Lead | `NFR-005` |
| `FeedbackItem` | Đơn vị feedback chính được submit, triage, gắn status | `FR-101`, `FR-201`, `FR-301` |
| `FeedbackVote` | Lưu từng lượt upvote để enforce one-vote-per-user/email | `FR-102`, `BIZ-01` |
| `FeedbackSubscriber` | Lưu người theo dõi để gửi status/release updates | `FR-302`, `NFR-009` |
| `FeedbackMerge` | Ghi parent-child merge history | `FR-202`, `BIZ-02` |
| `FeedbackStatusHistory` | Ghi timeline status công khai và nội bộ | `FR-301`, `NFR-006` |
| `ReleaseNote` | Changelog public sau khi publish | `FR-303`, `BIZ-04` |
| `ReleaseNoteFeedback` | Bảng nối giữa release note và delivered feedback | `FR-303` |
| `AnalyticsEvent` | Lưu hoặc chuyển tiếp event cho activation/engagement | `BR-005`, `NFR-007` |
| `AuditLog` | Ghi lại các mutation quan trọng để điều tra và trust | `BIZ-05`, `NFR-006` |

---

## 2. Data Dictionary

### 2.1. Workspaces

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `workspace_id` | UUID | PK | Tenant ID |
| `name` | VARCHAR(120) | NOT NULL | Tên workspace |
| `slug` | VARCHAR(80) | UNIQUE, NOT NULL | Dùng cho URL portal |
| `plan_code` | ENUM | NOT NULL | `FREE`, `PRO`, `BUSINESS` |
| `portal_status` | ENUM | NOT NULL | `DRAFT`, `PUBLISHED`, `PAUSED` |
| `primary_color` | VARCHAR(20) | NULL | Branding cơ bản cho portal |
| `logo_asset_url` | VARCHAR(500) | NULL | Logo portal |
| `created_by_user_id` | UUID | FK -> Users | Người tạo workspace |
| `created_at` | TIMESTAMP | DEFAULT NOW | Audit |
| `updated_at` | TIMESTAMP | NOT NULL | Audit |

### 2.2. Users

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `user_id` | UUID | PK | User nội bộ |
| `email` | VARCHAR(150) | UNIQUE, NOT NULL | Dùng login và notification nội bộ |
| `full_name` | VARCHAR(120) | NOT NULL | Tên hiển thị |
| `auth_provider` | ENUM | NOT NULL | `EMAIL`, `GOOGLE`, `MICROSOFT` |
| `is_active` | BOOLEAN | DEFAULT TRUE | Trạng thái hoạt động |
| `last_login_at` | TIMESTAMP | NULL | Theo dõi usage |
| `created_at` | TIMESTAMP | DEFAULT NOW | Audit |

### 2.3. WorkspaceMembers

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `workspace_member_id` | UUID | PK | |
| `workspace_id` | UUID | FK -> Workspaces | |
| `user_id` | UUID | FK -> Users | |
| `role_code` | ENUM | NOT NULL | `ADMIN`, `PM`, `CS_LEAD`, `VIEWER` |
| `joined_at` | TIMESTAMP | DEFAULT NOW | |
| `invited_by_user_id` | UUID | FK -> Users | |

### 2.4. FeedbackItems

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `feedback_id` | UUID | PK | ID feedback |
| `workspace_id` | UUID | FK -> Workspaces, NOT NULL | Tenant ownership |
| `source_type` | ENUM | NOT NULL | `PORTAL`, `CSV_IMPORT`, `MANUAL`, `API` |
| `title` | VARCHAR(120) | NOT NULL | Theo `VR-101` |
| `description` | TEXT | NULL | Theo `VR-102` |
| `category_code` | VARCHAR(50) | NULL | Theme / area |
| `status_code` | ENUM | NOT NULL | `NEW`, `REVIEWED`, `PLANNED`, `IN_PROGRESS`, `RELEASED`, `MERGED`, `ARCHIVED` |
| `visibility_code` | ENUM | NOT NULL | `PUBLIC`, `INTERNAL_ONLY` |
| `vote_count` | INTEGER | DEFAULT 0 | Count denormalized |
| `subscriber_count` | INTEGER | DEFAULT 0 | Count denormalized |
| `submitter_email` | VARCHAR(150) | NULL | Dùng cho portal user nếu chưa có account |
| `created_by_actor_type` | ENUM | NOT NULL | `PORTAL_USER`, `WORKSPACE_MEMBER`, `SYSTEM_IMPORT` |
| `created_at` | TIMESTAMP | DEFAULT NOW | |
| `updated_at` | TIMESTAMP | NOT NULL | |
| `merged_into_feedback_id` | UUID | FK -> FeedbackItems, NULL | Set khi item bị merge |

### 2.5. FeedbackVotes

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `feedback_vote_id` | UUID | PK | |
| `workspace_id` | UUID | FK -> Workspaces | |
| `feedback_id` | UUID | FK -> FeedbackItems | |
| `voter_key` | VARCHAR(180) | NOT NULL | Hash từ email hoặc account ID |
| `voter_type` | ENUM | NOT NULL | `PORTAL_EMAIL`, `PORTAL_USER`, `WORKSPACE_MEMBER` |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

**Unique constraint**
- `(workspace_id, feedback_id, voter_key)` để enforce `BIZ-01`

### 2.6. FeedbackSubscribers

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `subscriber_id` | UUID | PK | |
| `workspace_id` | UUID | FK -> Workspaces | |
| `feedback_id` | UUID | FK -> FeedbackItems | |
| `subscriber_key` | VARCHAR(180) | NOT NULL | Email hoặc account key |
| `channel` | ENUM | NOT NULL | `EMAIL`, `IN_APP` |
| `is_unsubscribed` | BOOLEAN | DEFAULT FALSE | Phục vụ `NFR-009` |
| `subscribed_at` | TIMESTAMP | DEFAULT NOW | |
| `unsubscribed_at` | TIMESTAMP | NULL | |

### 2.7. FeedbackMerges

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `merge_id` | UUID | PK | |
| `workspace_id` | UUID | FK -> Workspaces | |
| `parent_feedback_id` | UUID | FK -> FeedbackItems | Item giữ lại |
| `child_feedback_id` | UUID | FK -> FeedbackItems | Item bị gộp |
| `merged_by_user_id` | UUID | FK -> Users | Người thực hiện |
| `merge_reason` | VARCHAR(255) | NULL | Lý do / note |
| `merged_at` | TIMESTAMP | DEFAULT NOW | |

### 2.8. FeedbackStatusHistory

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `status_history_id` | UUID | PK | |
| `workspace_id` | UUID | FK -> Workspaces | |
| `feedback_id` | UUID | FK -> FeedbackItems | |
| `from_status_code` | ENUM | NULL | |
| `to_status_code` | ENUM | NOT NULL | |
| `is_public_transition` | BOOLEAN | DEFAULT TRUE | Có public ra portal hay không |
| `changed_by_user_id` | UUID | FK -> Users | |
| `changed_at` | TIMESTAMP | DEFAULT NOW | |
| `change_note` | VARCHAR(255) | NULL | |

### 2.9. ReleaseNotes

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `release_note_id` | UUID | PK | |
| `workspace_id` | UUID | FK -> Workspaces | |
| `title` | VARCHAR(150) | NOT NULL | |
| `summary` | TEXT | NOT NULL | Nội dung public |
| `status_code` | ENUM | NOT NULL | `DRAFT`, `PUBLISHED`, `ARCHIVED` |
| `publish_at` | TIMESTAMP | NULL | Chỉ public sau thời điểm này |
| `published_by_user_id` | UUID | FK -> Users | |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

### 2.10. ReleaseNoteFeedback

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `release_note_feedback_id` | UUID | PK | |
| `release_note_id` | UUID | FK -> ReleaseNotes | |
| `feedback_id` | UUID | FK -> FeedbackItems | Phải đang `RELEASED` |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

### 2.11. AuditLogs

| Column | Type | Constraint | Mô tả |
|--------|------|-----------|-------|
| `audit_log_id` | BIGINT | PK | |
| `workspace_id` | UUID | FK -> Workspaces | |
| `actor_user_id` | UUID | FK -> Users, NULL | Null nếu system actor |
| `action_code` | VARCHAR(60) | NOT NULL | `MERGE_FEEDBACK`, `UPDATE_STATUS`, `PUBLISH_RELEASE_NOTE` |
| `entity_type` | VARCHAR(60) | NOT NULL | |
| `entity_id` | UUID | NOT NULL | |
| `before_payload` | JSONB | NULL | |
| `after_payload` | JSONB | NULL | |
| `created_at` | TIMESTAMP | DEFAULT NOW | |

---

## 3. Analytics Data Model

### 3.1. Required Events Schema

| Event | Trigger | Properties tối thiểu | Ref |
|-------|---------|----------------------|-----|
| `signup_completed` | User hoàn tất đăng ký | `user_id`, `auth_provider`, `utm_source` | Activation |
| `workspace_created` | Workspace được tạo | `workspace_id`, `plan_code` | Activation |
| `feedback_imported` | Import CSV thành công | `workspace_id`, `import_count`, `source_type` | Activation |
| `portal_published` | Portal chuyển sang `PUBLISHED` | `workspace_id`, `theme_variant` | `O1-KR1` |
| `feedback_submitted` | Submit feedback thành công | `workspace_id`, `feedback_id`, `category_code`, `source_type` | `FR-101` |
| `feedback_upvoted` | Upvote thành công | `workspace_id`, `feedback_id`, `voter_type` | `FR-102` |
| `feedback_merged` | Merge thành công | `workspace_id`, `parent_feedback_id`, `child_feedback_id`, `merged_by_role` | `FR-202` |
| `feedback_status_changed` | Public status đổi | `workspace_id`, `feedback_id`, `from_status`, `to_status` | `FR-301` |
| `release_note_published` | Release note được publish | `workspace_id`, `release_note_id`, `linked_feedback_count` | `FR-303` |
| `notification_delivery_failed` | Notification fail sau retry | `workspace_id`, `feedback_id`, `channel`, `failure_type` | Operations |

### 3.2. Dashboard Map

| Dashboard | Metrics chính | Audience |
|-----------|---------------|----------|
| Activation | `signup_completed -> workspace_created -> portal_published` funnel | Product, Growth |
| Feedback Loop | submit volume, upvote rate, status-in-7-days | PM, CS Lead |
| Triage Quality | merge rate, merge reversal rate, duplicate candidate acceptance | Product, Engineering |
| Value Proof | release notes linked feedback ratio, notification CTR | Product, CS |

### 3.3. Event QA Rules

- Mọi event trong `BR-005` phải có `workspace_id`.
- Các event mutation quan trọng phải có `entity_id` tương ứng.
- Event retries không được ghi trùng user-facing outcomes.
- Event names dùng `snake_case`, không đổi nghĩa giữa beta và GA.

---

## 4. Data Business Rules

| ID | Rule | Logic | Áp dụng |
|----|------|-------|---------|
| `DR-001` | Multi-tenancy bắt buộc | Mọi bảng nghiệp vụ phải có `workspace_id`; mọi query public/admin phải lọc theo tenant | All business tables |
| `DR-002` | One vote per feedback per voter | Unique constraint trên `(workspace_id, feedback_id, voter_key)` | `FeedbackVotes` |
| `DR-003` | Merge không làm mất lịch sử | Vote, subscriber, audit history phải được re-linked hoặc preserved khi merge | `FeedbackMerges`, `FeedbackVotes`, `FeedbackSubscribers` |
| `DR-004` | Public status chỉ dùng tập trạng thái cho phép | Portal chỉ hiển thị `PLANNED`, `IN_PROGRESS`, `RELEASED` | `FeedbackItems`, `FeedbackStatusHistory` |
| `DR-005` | Release note public chỉ link feedback `RELEASED` | Chặn publish nếu feedback chưa `RELEASED` | `ReleaseNotes`, `ReleaseNoteFeedback` |
| `DR-006` | Notification phải support unsubscribe | Subscriber opt-out phải được tôn trọng ở mọi lần gửi tiếp theo | `FeedbackSubscribers` |
| `DR-007` | Mọi status transition và merge phải có audit log | Tạo `AuditLog` trước khi commit transaction hoàn tất | `AuditLogs` |

---

## 5. Retention, Privacy, and Operational Notes

| Area | Rule | Lý do |
|------|------|-------|
| Soft delete | Không hard-delete `FeedbackItem` đã public; dùng archive hoặc merge marker | Giữ traceability và release proof |
| PII | `submitter_email` và `subscriber_key` phải được bảo vệ theo chính sách privacy | Tránh lộ email end-user |
| Recovery | Merge operations phải có replayable audit trail | Điều tra khi duplicate merge sai |
| Reporting | Denormalized `vote_count` và `subscriber_count` phải có job reconcile định kỳ | Tránh lệch số liệu portal |
