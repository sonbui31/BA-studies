# Vietnamese User Manual Writing Guide

Write for end users, not implementers. Use a warm, direct Vietnamese tone and address the reader as "bạn".

## Style Rules

| Rule | Avoid | Prefer |
| --- | --- | --- |
| Use action language | "Người dùng nhấn nút Lưu" | "Nhấn **Lưu** để hoàn tất" |
| Avoid raw technical terms | "Sidebar", "modal" | "Menu bên trái", "hộp thoại" |
| Explain abbreviations first | "SLA" | "Thời hạn xử lý (SLA)" |
| Use user-centered FAQs | "Lỗi đăng nhập" | "Tôi không đăng nhập được, phải làm sao?" |
| Use concrete examples | "Nhập email" | "Nhập email, ví dụ: `nguyenvana@example.vn`" |
| Keep permissions readable | "`module:readAll`" | "Xem danh sách" |

Use "vui lòng" sparingly. Prefer concise instructions such as "hãy liên hệ Admin" or "nhấn **Lưu**".

## Do Not Invent

Only include these details when verified from the app, source, screenshots, or user input:

- Automatic password emails.
- Server URL, QR/barcode, or device setup.
- AI face check-in or camera onboarding.
- Approval levels and role names.
- Import/export formats.
- Delete constraints and validation messages.

If a detail is plausible but unverified, keep it in a separate implementation note or TODO list.

Create `handoff-notes.md` for every real manual. Put all unresolved facts there instead of publishing them as final user guidance.

## Coverage Rules

Each real module page should cover the user's complete path through the feature:

- Where to open the feature.
- What the main screen is for.
- Which controls matter and what they do.
- How to complete primary tasks.
- What validation, error, empty, and confirmation states mean when they exist.
- Which roles can perform each action when permissions differ.

Avoid pages that are only UI inventories. A good page lets the reader finish work without guessing the next step.

## Privacy And Example Data

Use fake but realistic example data. Replace or mask real personal, medical, financial, customer, employee, token, and credential data before the docs are published.

Good examples:

- `nguyenvana@example.vn`
- `0900 000 000`
- `REC-000123`
- `Phong Hanh chinh`

Do not include production passwords, API keys, access tokens, internal-only URLs, or real patient/customer records in the manual.

Do not use real organization domains in examples unless the owner explicitly confirms they are publishable. Prefer `example.vn` or neutral fake values.

## Module Page Template

```markdown
# [Emoji] [Tên chức năng]

> **Đường dẫn:** Menu bên trái -> [Nhóm] -> [Chức năng]

## Màn hình chính

![Màn hình chính](/img/screenshots/[module]/[module]-01-overview.png)

[1-2 câu mô tả trang này dùng để làm gì.]

### Thanh công cụ phía trên

| Nút | Dùng để làm gì? |
| --- | --- |
| **Thêm mới** | Mở form nhập dữ liệu mới |
| **Tải lại** | Làm mới danh sách và xóa bộ lọc |

### Tìm kiếm và lọc

| Cách tìm | Mô tả |
| --- | --- |
| **Tìm theo tên** | Gõ từ khóa vào ô tìm kiếm, sau đó nhấn Enter |
| **Lọc nâng cao** | Lọc theo các điều kiện có trên màn hình |

### Bảng danh sách

| Cột | Giải thích |
| --- | --- |
| **Mã** | Mã định danh của bản ghi |
| **Tên** | Tên đầy đủ của bản ghi |
| **Trạng thái** | Tình trạng hiện tại |
| **Thao tác** | Mở các thao tác nhanh trên từng dòng |

## Hướng dẫn thao tác

### Thêm mới [đối tượng]

![Form thêm mới](/img/screenshots/[module]/[module]-02-create-form.png)

1. Nhấn **Thêm mới**.
2. Điền các trường bắt buộc.
3. Nhấn **Lưu** để hoàn tất.

:::note[Ghi chú]

Chỉ thêm lưu ý khi có ràng buộc thật sự được xác minh.

:::

## Ai được làm gì?

| Thao tác | [Vai trò 1] | [Vai trò 2] |
| --- | :---: | :---: |
| Xem danh sách | Có | Có |
| Thêm mới | Có | Không |
```

## Handoff Notes

Use `references/handoff-template.md` when creating `handoff-notes.md` for a real manual.

## README Template

```markdown
---
title: Hướng dẫn sử dụng - [Tên hệ thống]
sidebar_label: Trang chủ
slug: /intro
---

# Hướng dẫn sử dụng - [Tên hệ thống]

> **Phiên bản:** [vX.X.X] | **Cập nhật:** [DD/MM/YYYY]

## Chào mừng bạn!

[Giới thiệu ngắn gọn hệ thống và nhóm người dùng chính.]

## Phần mềm giúp bạn làm gì?

| Chức năng | Mô tả |
| --- | --- |

## Bạn thuộc nhóm nào?

| Vai trò | Bạn có thể làm gì? |
| --- | --- |

## Bắt đầu từ đâu?

- [Trước khi bắt đầu](/docs/getting-started/prerequisites)
- [Đăng nhập](/docs/getting-started/login)
- [Tổng quan giao diện](/docs/getting-started/interface-overview)
```

## FAQ Template

```markdown
### Tôi không đăng nhập được, phải làm sao?

1. Kiểm tra email và mật khẩu, chú ý chữ hoa/thường.
2. Kiểm tra địa chỉ máy chủ nếu hệ thống yêu cầu nhập máy chủ.
3. Nhấn **Quên mật khẩu** nếu hệ thống có hỗ trợ.
4. Nếu vẫn không được, hãy liên hệ người phụ trách hệ thống.

### Tại sao tôi không thấy mục [X] trong menu?

Menu chỉ hiện những chức năng bạn có quyền sử dụng. Nếu thiếu mục cần dùng, hãy liên hệ người quản trị để kiểm tra quyền.
```
