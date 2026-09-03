# User Manual Generator

`user-manual-generator` là bộ skill dùng chung để tạo tài liệu hướng dẫn sử dụng tiếng Việt cho nhiều loại dự án: web app, desktop app, Electron app, mobile app, hệ thống nội bộ hoặc sản phẩm SaaS.

Mục tiêu của skill là biến một ứng dụng thật thành một bộ tài liệu Docusaurus rõ ràng, có ảnh chụp màn hình, có hướng dẫn thao tác, có phân quyền, có trang Home giới thiệu sản phẩm và có bước kiểm tra chất lượng trước khi bàn giao.

## Mục Đích

Sử dụng skill này khi cần:

- Tạo user manual chuyên nghiệp bằng tiếng Việt.
- Chuyển tài liệu cũ sang Docusaurus 3.10.
- Tạo trang tài liệu có sidebar, search, route rõ ràng.
- Deploy tài liệu lên GitHub Pages.
- Luôn có một màn Home giới thiệu sản phẩm, tách riêng với trang hướng dẫn `/docs/intro`.
- Kiểm tra lỗi tài liệu trước khi bàn giao.

Skill này giúp tránh việc viết tài liệu bằng phỏng đoán. Nội dung user-facing phải dựa trên bằng chứng đã xác minh từ UI, screenshot, source code, route, permission config hoặc thông tin do chủ dự án cung cấp.

## Nguyên Tắc Chính

- Không tự bịa role, workflow, permission, menu item, onboarding, email tự động, QR/barcode/camera behavior hoặc approval rule.
- Không đưa dữ liệu nhạy cảm vào tài liệu public.
- Không expose permission code kỹ thuật như `module:readAll`, `user:update`, `order:approve`.
- Không dùng Home page dạng redirect sang `/docs/intro`.
- Không gộp vai trò người dùng nếu chưa có source chứng minh các vai trò có cùng quyền.
- Những điểm chưa xác minh phải để trong `handoff-notes.md`, không đưa vào tài liệu chính.

## Cách Hoạt Động

Quy trình chuẩn:

1. Thu thập đầu vào: app entry point, local dev command, screenshot folder, scope, role, output directory, branding, version, GitHub owner/repo nếu cần deploy.
2. Khám phá app thật: đọc menu, route, màn hình, form, bảng, dialog, trạng thái lỗi/rỗng/loading và workflow chính.
3. Chụp hoặc dùng screenshot có sẵn: overview, filters, create/edit forms, dialogs, approvals, role-specific views.
4. Map role và permission từ source/UI/API/permission matrix đã xác minh.
5. Viết tài liệu Markdown tiếng Việt theo ngôn ngữ người dùng.
6. Tạo site Docusaurus 3.10.
7. Chạy audit tài liệu trước khi bàn giao.

## Cấu Trúc Output Khuyến Nghị

```text
manual/
|-- package.json
|-- package-lock.json
|-- docusaurus.config.js
|-- sidebars.js
|-- static/
|   |-- .nojekyll
|   `-- img/
|       |-- logo.png
|       `-- screenshots/
|-- src/
|   |-- css/
|   |   `-- custom.css
|   `-- pages/
|       |-- index.js
|       `-- index.module.css
|-- docs/
|   |-- intro.md
|   |-- getting-started/
|   |-- dashboard/
|   |-- <module-folders>/
|   `-- appendix/
|-- handoff-notes.md
`-- README.md
```

## Home Giới Thiệu Sản Phẩm

Mỗi manual Docusaurus phải có một trang Home thật tại:

```text
src/pages/index.js
```

Trang này dùng để giới thiệu sản phẩm, không phải bản sao của `/docs/intro` và không phải redirect.

Home page nên có:

- Logo, tên sản phẩm và category ngắn.
- Headline nêu rõ giá trị chính.
- Một đoạn mô tả ngắn về sản phẩm.
- CTA chính vào `/docs/intro`.
- CTA phụ vào module quan trọng nhất.
- Screenshot thật của sản phẩm.
- Summary band 3-4 điểm chính về sản phẩm.

## Nội Dung Mỗi Trang Module

Mỗi trang module nên bao gồm:

- Đường dẫn mở chức năng.
- Ảnh màn hình chính.
- Mục đích của màn hình.
- Thanh công cụ, bộ lọc, bảng, tab, row actions.
- Hướng dẫn từng bước cho workflow chính.
- Validation, lỗi thường gặp, empty state hoặc confirmation khi có.
- Bảng "Ai được làm gì?" nếu quyền khác nhau theo role.

## Handoff Notes

`handoff-notes.md` dùng để chứa những thông tin chưa đủ chắc hoặc không nên publish trực tiếp.

Ví dụ:

- Role mapping kỹ thuật.
- Source xác minh quyền.
- Production URL cần hỏi có được public không.
- Workflow chưa có screenshot.
- Behavior chưa xác minh như email tự động, import template, QR/barcode/print, approval level.
- Open questions cho project owner.

Template nằm tại:

```text
references/handoff-template.md
```

## Privacy Và Dữ Liệu Ví Dụ

Mặc định dùng dữ liệu giả an toàn:

- Email: `nguyenvana@example.vn`
- Phone: `0900 000 000`
- Server URL: `https://example.vn`
- Record code: `REC-000123`

Không đưa vào tài liệu public:

- Email thật
- Số điện thoại thật
- Token/API key/password
- URL nội bộ hoặc production URL chưa được xác nhận
- Thông tin khách hàng, bệnh nhân, nhân viên, dữ liệu tài chính

## Docusaurus 3.10

Skill ưu tiên Docusaurus 3.10 cho tài liệu dạng website.

Các rule quan trọng:

- GitHub Pages project site phải dùng `baseUrl` theo repo, ví dụ `/user-guide/`.
- Root Pages repo dạng `<owner>.github.io` mới dùng `baseUrl: '/'`.
- Static assets để trong `static/img/...`.
- Markdown image path dùng `/img/...`.
- Docs link dùng `/docs/...`.
- Admonition có title phải dùng cú pháp Docusaurus v3:

```markdown
:::tip[Mẹo]

Nội dung mẹo.

:::

:::warning[Lưu ý]

Nội dung cảnh báo.

:::
```

Không dùng cú pháp cũ:

```markdown
:::tip Mẹo
```

## Chạy Audit

Chạy audit với:

```bash
node user-manual-generator/scripts/audit-docs.js <manual-dir>
```

Ví dụ:

```bash
node user-manual-generator/scripts/audit-docs.js ./manual
```

Nếu dự án có thuật ngữ cấm riêng, truyền thêm qua biến môi trường:

```bash
DOCS_BANNED_TERMS="Term A,Term B" node user-manual-generator/scripts/audit-docs.js ./manual
```

Audit script kiểm tra:

- Thiếu file Docusaurus quan trọng.
- Thiếu `static/.nojekyll`.
- Thiếu Home page.
- Home page bị redirect.
- Home page thiếu CTA vào `/docs/intro`.
- Home page thiếu screenshot sản phẩm.
- Link hoặc image bị hỏng.
- Placeholder chưa được thay.
- Cú pháp admonition sai.
- Email, phone, token, secret, URL production/internal.
- Permission code kỹ thuật còn trong user docs.
- Workflow page không có screenshot.
- Ảnh orphan không được dùng.
- Khả năng sai `baseUrl` khi deploy GitHub Pages.

## Khi Nào Tài Liệu Được Xem Là Sẵn Sàng

Một bộ manual được xem là sẵn sàng khi:

- `npm run build` chạy thành công.
- `audit-docs.js` đã chạy và các issue quan trọng đã xử lý hoặc ghi rõ trong `handoff-notes.md`.
- Mọi screenshot được reference đều tồn tại.
- Không còn placeholder trong user-facing docs.
- Không có dữ liệu nhạy cảm chưa được xác nhận.
- Role/permission có source rõ ràng.
- Public GitHub Pages URL đã được kiểm tra đúng path.
- Final response báo rõ thư mục manual, số trang, số screenshot, kết quả build/audit và open questions còn lại.

## Các File Trong Skill

```text
user-manual-generator/
|-- SKILL.md
|-- README.md
|-- references/
|   |-- capture-guide.md
|   |-- docusaurus.md
|   |-- handoff-template.md
|   `-- writing-guide.md
`-- scripts/
    `-- audit-docs.js
```

Trong đó:

- `SKILL.md`: rule chính để agent sử dụng skill.
- `references/docusaurus.md`: hướng dẫn tạo và deploy Docusaurus 3.10.
- `references/writing-guide.md`: quy chuẩn viết tài liệu tiếng Việt.
- `references/capture-guide.md`: hướng dẫn chụp màn hình và log bằng chứng.
- `references/handoff-template.md`: template cho thông tin chưa xác minh.
- `scripts/audit-docs.js`: script kiểm tra chất lượng tài liệu.
