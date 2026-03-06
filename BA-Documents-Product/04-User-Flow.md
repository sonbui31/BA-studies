# USER FLOW & JOURNEY MAP
# {{Tên sản phẩm}}

> **Phiên bản:** 1.0 | **Ngày:** {{DD/MM/YYYY}}

---

## 1. High-Level User Flow

### 1.1 Onboarding Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Landing    │────▶│  Sign Up    │────▶│  Onboarding │────▶│ First Value │
│  Page       │     │  (Email/SSO)│     │  (3-5 steps)│     │  Moment     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                         │                                         │
                    ❌ Drop-off                               ✅ Activated!
                    (Track: signup_abandoned)                 (Track: first_value)
```

**Metrics to track:**
| Step | Event | Target |
|------|-------|--------|
| Landing → Sign Up | `signup_started` | Conversion ≥ {{X}}% |
| Sign Up Completed | `signup_completed` | Completion ≥ {{X}}% |
| Onboarding Step 1-N | `onboarding_step_N` | Completion ≥ {{X}}% |
| First Value | `first_value_achieved` | Within {{X}} minutes |

---

### 1.2 Core User Flow — {{Core Feature}}

```
{{Mô tả luồng chính của sản phẩm — thay thế bằng nội dung cụ thể}}

Ví dụ luồng tạo đơn hàng (E-commerce SaaS):

┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
│  Browse   │────▶│  Add to   │────▶│ Checkout  │────▶│  Payment  │
│  Products │     │  Cart     │     │  Info     │     │  Process  │
└───────────┘     └───────────┘     └───────────┘     └─────┬─────┘
                                                            │
                                                    ┌───────┴───────┐
                                                    │               │
                                              ✅ Success      ❌ Failed
                                              Order created   Retry / Alert
```

---

## 2. User Journey Map

### Persona: {{Persona chính}}

| Giai đoạn | Hành động | Suy nghĩ | Cảm xúc | Touchpoint | Cơ hội cải thiện |
|-----------|----------|---------|--------|------------|-----------------|
| **Awareness** | Tìm thấy qua {{kênh}} | "Sản phẩm này giải quyết vấn đề gì?" | 😐 Tò mò | Landing page, Blog, Ads | SEO, Content marketing |
| **Consideration** | So sánh với {{competitor}} | "Có tốt hơn cái đang dùng không?" | 🤔 Cân nhắc | Pricing page, Demo, Reviews | Social proof, Case study |
| **Sign-up** | Đăng ký tài khoản | "Hy vọng không quá phức tạp" | 😊 Lạc quan | Sign-up form | Giảm friction (SSO, ít fields) |
| **Onboarding** | Làm theo hướng dẫn | "Mình setup đúng chưa?" | 😐 Hơi lo | Tour, Checklist, Templates | Interactive guide, Progress bar |
| **First Value** | Hoàn thành {{core task}} lần đầu | "Ồ, nhanh thật!" | 🎉 Ấn tượng | Core feature | Celebration UI, Quick win |
| **Regular Use** | Sử dụng hàng ngày | "Tiết kiệm thời gian thật" | 😊 Hài lòng | Dashboard, Notifications | Personalization |
| **Upgrade** | Gặp giới hạn free, cần thêm | "Liệu có đáng tiền?" | 🤔 Cân nhắc | Upgrade prompt, Pricing | Gentle nudge, ROI calculator |
| **Advocacy** | Giới thiệu cho bạn bè | "Mình thích sản phẩm này" | 🥰 Advocate | Referral, NPS survey | Referral program, Social share |

---

## 3. Error Flows & Edge Cases

### 3.1 Sign-up Failures
| Scenario | Xử lý | UX |
|----------|--------|----|
| Email đã tồn tại | Gợi ý đăng nhập hoặc reset password | Friendly message |
| SSO fail | Fallback về email/password | Error toast + retry |
| Network error | Retry button + save draft | Auto-retry 3 lần |

### 3.2 Payment Failures
| Scenario | Xử lý | UX |
|----------|--------|----|
| Card declined | Gợi ý thử card khác | Clear error message |
| 3D Secure timeout | Auto-retry 1 lần rồi báo | Loading → Error page |
| Webhook missed | Background retry + email | Admin alert |

### 3.3 Data Error Flows
| Scenario | Xử lý | UX |
|----------|--------|----|
| Form validation fail | Inline error, highlight field | Real-time validation |
| Upload file quá lớn | Reject + message size limit | Pre-upload check |
| Server error (5xx) | Error page + auto-report | "Chúng tôi đang xử lý" |

---

## 4. Notification Flows

| Trigger | Channel | Message | Timing |
|---------|---------|---------|--------|
| Sign-up thành công | Email + In-app | Welcome + Onboarding CTA | Ngay lập tức |
| Chưa hoàn thành onboarding | Email | "Bạn chỉ còn 2 bước!" | Sau 24h |
| First value achieved | In-app | 🎉 Celebration + Next step | Ngay lập tức |
| Inactive {{X}} ngày | Email + Push | "Bạn có {{data}} chờ xử lý" | Sau {{X}} ngày |
| Trial sắp hết | Email + In-app | Upgrade prompt + Benefits | 3 ngày trước |
| New feature released | In-app + Email | What's New modal | Khi release |

---

## 5. User Flow Documentation Convention

> Khi viết User Flow cho sản phẩm Product, tuân theo quy ước:

| Ký hiệu | Ý nghĩa |
|----------|---------|
| `───▶` | Luồng chính (happy path) |
| `- - ▶` | Luồng phụ / error |
| `✅` | Thành công |
| `❌` | Thất bại / drop-off |
| `📊` | Tracking point (analytics event) |
| `🔔` | Notification trigger |
