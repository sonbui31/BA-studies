# USER FLOW & JOURNEY MAP
# SignalDesk

> **Phiên bản:** 1.0 | **Ngày:** 13/05/2026
> **Tham chiếu:** `02-BRD.md`, `05-SRS-Lite.md`, `08-Beta-Testing-Plan.md`

---

## 1. High-Level Product Flow

### 1.1. Workspace Activation Flow

```
┌─────────────┐     ┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Sign Up /   │────▶│ Create      │────▶│ Import CSV or │────▶│ Publish      │────▶│ First Feedback │
│ Invite      │     │ Workspace   │     │ sample data   │     │ Portal       │     │ Submitted      │
└─────────────┘     └─────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
      │                    │                    │                    │                      │
      │                    │                    │                    │                      └── 📊 `feedback_submitted`
      │                    │                    │                    └── 📊 `portal_published`
      │                    │                    └── 📊 `feedback_imported`
      │                    └── 📊 `workspace_created`
      └── 📊 `signup_completed`
```

**Target activation path**
- `signup_completed` -> `workspace_created` trong cùng session
- `portal_published` trong 14 ngày
- `feedback_submitted` hoặc `feedback_imported` trong 7 ngày đầu

---

### 1.2. Core User Flow - Feedback-to-Response Loop

```
Portal User truy cập portal
    ├── Tìm ý tưởng tương tự
    │      └── Nếu thấy item phù hợp -> Upvote -> Subscribe -> Chờ update
    └── Không thấy item phù hợp -> Submit feedback mới
                                  └── Hệ thống tạo item status `New`

PM mở inbox
    ├── Review feedback mới
    ├── Xem duplicate candidates
    ├── Merge nếu cần
    ├── Gắn tag / status public
    └── Khi feature ship -> Publish release note gắn feedback liên quan

Subscriber / Customer Champion
    ├── Nhận email khi status đổi
    └── Đọc release note khi feedback được `Released`
```

**Related requirements**
- `BR-001` / `FR-101`, `FR-102`
- `BR-002` / `FR-201`, `FR-202`
- `BR-003` / `FR-301`, `FR-302`
- `BR-004`, `BR-005` / `FR-303`

---

## 2. Journey Map by Persona

### 2.1. Persona: Product Manager

| Giai đoạn | Hành động | Suy nghĩ | Cảm xúc | Touchpoint | Cơ hội cải thiện |
|-----------|----------|---------|--------|------------|-----------------|
| **Setup** | Tạo workspace, import feedback cũ | "Mình có gom được backlog cũ đủ nhanh không?" | 😐 Cẩn trọng | Workspace onboarding | CSV import + sample data |
| **Portal Launch** | Publish portal public | "Liệu khách hàng có chịu dùng portal thay vì email?" | 🙂 Hy vọng | Portal settings | Portal preview + branding nhẹ |
| **Daily Triage** | Review feedback inbox, xem duplicate candidates | "Mình cần lọc noise nhanh, không muốn inbox thành bãi rác" | 😊 Tập trung | Inbox, duplicate suggestion | Confidence score + merge preview |
| **Status Update** | Đổi status và gắn tag | "Status này có public được không?" | 🙂 Cân nhắc | Feedback detail | Public/private status guardrails |
| **Delivery Proof** | Publish release note linked to feedback | "Giờ mình có bằng chứng để nói với khách hàng rồi" | 🎉 Tự tin | Release notes | One-click link từ feedback sang release |

### 2.2. Persona: Customer Success Lead

| Giai đoạn | Hành động | Suy nghĩ | Cảm xúc | Touchpoint | Cơ hội cải thiện |
|-----------|----------|---------|--------|------------|-----------------|
| **Feedback Intake** | Thu feedback từ customer call/email | "Item này đã tồn tại chưa?" | 😐 Bận rộn | CRM, portal search | Quick search trước khi tạo mới |
| **Subscription** | Subscribe customer vào item đúng | "Mình muốn khỏi phải theo dõi tay" | 🙂 Thực dụng | Feedback detail / portal | Simple subscribe flow |
| **Status Follow-up** | Kiểm tra item đã `Planned` hay `Released` chưa | "Mình có thể trả lời khách hàng ngay không?" | 😊 Nhẹ đầu | Portal public status | Consistent status wording |
| **Release Sharing** | Gửi release note cho customer | "Đây là bằng chứng tốt cho renewal/QBR" | 🎉 Hài lòng | Release notes | Share-ready release copy |

### 2.3. Persona: Customer Champion

| Giai đoạn | Hành động | Suy nghĩ | Cảm xúc | Touchpoint | Cơ hội cải thiện |
|-----------|----------|---------|--------|------------|-----------------|
| **Discover** | Vào portal từ email hoặc help center | "Có ai thực sự đọc feedback ở đây không?" | 😐 Tò mò | Public portal | Social proof, count of supporters |
| **Contribute** | Search, upvote, hoặc submit feedback | "Mình muốn làm việc này thật nhanh" | 🙂 Tích cực | Search, submit form | Fast form, duplicate hint |
| **Track** | Subscribe vào item đã quan tâm | "Bao giờ mình sẽ biết có update?" | 🙂 Hy vọng | Subscribe action | Clear expectation về notification |
| **Receive Update** | Mở email status / release note | "Ồ, họ thực sự làm theo feedback này" | 🎉 Tin tưởng | Email + portal | Direct link về item / changelog |

---

## 3. Detailed Operational Flows

### 3.1. Public Feedback Submission

```
[Portal visit]
   └── Search existing feedback
           ├── Found similar item -> Upvote -> Subscribe -> End
           └── No suitable item -> Fill form -> Validate title/email -> Create `New` feedback -> Confirmation -> Optional subscribe
```

**Tracking points**
- `portal_viewed`
- `feedback_search_performed`
- `feedback_submitted`
- `feedback_upvoted`
- `feedback_subscription_created`

### 3.2. Duplicate Triage Flow

```
[Feedback appears in inbox]
   -> PM opens detail
   -> System suggests duplicate candidates
      ├── PM rejects suggestion -> keep item separate
      └── PM accepts merge
             -> choose parent item
             -> move vote_count + subscribers + history
             -> child becomes `Merged`
             -> audit log + `feedback_merged`
```

**Control points**
- Chỉ `Admin` hoặc `PM` được merge.
- Không được merge khác workspace.
- Merge preview phải hiển thị item nào là parent.

### 3.3. Status Update and Release Proof Flow

```
[PM changes public status]
   -> Validate status in allowed public set
   -> Save status history
   -> Queue subscriber notification
      ├── unsubscribed -> skip send
      ├── email delivered -> mark success
      └── email failed -> retry / dead-letter

[PM publishes release note]
   -> choose feedback items in `Released`
   -> set publish_at
   -> publish release note
   -> link feedback items on portal
   -> emit `release_note_published`
```

---

## 4. Error Flows & Edge Cases

### 4.1. Portal / Submit Errors

| Scenario | Xử lý hệ thống | UX kỳ vọng | Ref |
|----------|----------------|-----------|-----|
| Title quá ngắn hoặc email invalid | Reject request, không tạo item | Inline validation rõ ràng | `FR-101`, `VR-101` |
| Portal bị spam liên tục | Rate-limit theo IP/email, có thể yêu cầu verify | Friendly anti-abuse message | `NFR-004` |
| User submit item trùng nội dung | Vẫn cho submit nhưng gợi ý item tương tự trước khi gửi | Suggest duplicate before final submit | `BR-002` |

### 4.2. Merge / Triage Errors

| Scenario | Xử lý hệ thống | UX kỳ vọng | Ref |
|----------|----------------|-----------|-----|
| User không có quyền merge | Chặn action, ghi audit nếu cần | Permission message rõ | `FR-202`, `NFR-005` |
| Chọn parent/child khác workspace | Chặn merge | Message nêu rõ data isolation rule | `BIZ-02` |
| Merge xong thiếu vote/subscriber | Không commit giao dịch và raise alert | Admin-visible error | `NFR-006` |

### 4.3. Notification / Release Errors

| Scenario | Xử lý hệ thống | UX kỳ vọng | Ref |
|----------|----------------|-----------|-----|
| Subscriber đã unsubscribe | Skip send, vẫn giữ status history | Không hiện lỗi cho PM | `NFR-009` |
| Email provider fail tạm thời | Retry async tối đa 2 lần | PM thấy trạng thái pending/retry | `FR-302` |
| PM cố link feedback chưa `Released` vào release note | Block publish | Validation message trước khi publish | `FR-303`, `BIZ-04` |

---

## 5. Notification Flows

| Trigger | Channel | Message intent | Timing | Event |
|---------|---------|----------------|--------|-------|
| Portal published | In-app | Xác nhận workspace đã public | Ngay lập tức | `portal_published` |
| Feedback submitted | Email or on-screen confirmation | Xác nhận request đã được ghi nhận | Ngay sau submit | `feedback_submitted` |
| Status changed to `Planned` / `In Progress` / `Released` | Email | Cập nhật tiến độ xử lý | Sau khi transition thành công | `feedback_status_changed` |
| Release note published with linked feedback | Email + portal | Chứng minh giá trị đã phát hành | Sau publish | `release_note_published` |
| Notification delivery failed repeatedly | Internal alert | Cảnh báo đội nội bộ xử lý | Sau 2 lần retry fail | `notification_delivery_failed` |

---

## 6. Flow Metrics

| Flow | Primary metric | Target | Supporting metrics |
|------|----------------|--------|--------------------|
| Activation | Portal publish rate | >= 55% | Time-to-first-feedback, CSV import completion |
| Contribution | Submit completion rate | >= 60% | Search-before-submit rate, upvote rate |
| Triage | Feedback with status in 7 days | >= 60% | Duplicate suggestion acceptance rate |
| Communication | Status request ticket reduction | >= 30% | Notification delivery success, unsubscribe rate |
| Value proof | Release note linked feedback usage | >= 40% of shipped items | Click-through from release note |

---

## 7. Flow Documentation Convention

| Ký hiệu | Ý nghĩa |
|---------|---------|
| `───▶` | Luồng chính |
| `- - ▶` | Exception / alternate flow |
| `✅` | Outcome thành công |
| `❌` | Outcome thất bại hoặc bị chặn |
| `📊` | Tracking point |
| `🔔` | Notification trigger |

> Với SignalDesk, mọi flow P0 phải chỉ ra ít nhất một trong ba thứ: `status transition`, `analytics event`, hoặc `customer-facing update`.
