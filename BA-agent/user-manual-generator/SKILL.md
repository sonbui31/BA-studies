---
name: user-manual-generator
description: Generate Vietnamese Docusaurus 3.10 user manuals for desktop, web, or mobile apps from verified UI exploration, screenshots, roles, and workflows; includes GitHub Pages publishing guidance and documentation QA.
---

# User Manual Generator

Use this skill when the user wants a professional Vietnamese user manual for a real desktop, web, or mobile application, especially when the output should be a browsable Docusaurus documentation site.

The manual must be based on verified evidence from the app, supplied screenshots/PDFs, source routes, or user-provided domain facts. Do not invent roles, workflows, onboarding steps, permissions, menu items, automation behavior, QR/barcode/camera behavior, email behavior, or approval rules.

## Required Inputs

Before generating the final manual, identify what is available:

- App entry point: URL, local dev command, Electron command, mobile screenshots/PDF, or existing screenshot folder.
- Scope: platforms, modules, roles, and output directory.
- Access: test accounts per role, seed data, and any known login/server setup.
- Branding and publishing: system name, logo/favicon path, version, update date, GitHub owner/repo when applicable, and preferred publishing path.
- Public/private boundary: confirm whether server URLs, organization domains, real user data, and screenshots are allowed to appear in the published manual.

If a required input is missing, proceed with the parts that can be verified and clearly mark unresolved facts as questions or TODOs in `handoff-notes.md`, not as user-facing documentation.

## Workflow

1. Explore the app and build a module map from actual navigation, routes, screenshots, or source structure.
2. Capture representative screenshots: overview, filters, create/edit forms, long-form scroll states, dialogs, approvals, empty/error states, and role-specific views where relevant.
3. Map roles and permissions from verified UI behavior, API/source rules, or user-provided permission matrices. Keep the source of truth in `handoff-notes.md`.
4. Generate friendly Markdown docs in Vietnamese using natural user language.
5. Always create a dedicated Docusaurus product Home page at `src/pages/index.js`; this page introduces the product and links into the manual. Do not replace it with a redirect to `/docs/intro`.
6. Publish as a Docusaurus 3.10 site when requested or when the deliverable is a browsable manual.
7. Run documentation QA before finishing.

## Evidence And Coverage Rules

- Final user-facing docs require at least one verification source: live UI, screenshots, source code, API/permission config, or explicit user-provided facts.
- Keep unverified facts out of the manual. Put them in `handoff-notes.md` as questions, TODOs, or assumptions to confirm.
- For every module in scope, cover at least the overview, primary workflows, validation/error states when present, and role differences when relevant.
- Do not deliver pages that only describe a screen. Include the actual steps a user needs to complete the feature's core tasks.
- If generating a reusable template instead of a real manual, label it clearly as a template and allow placeholders. For a real manual, remove placeholders before delivery.

For detailed writing rules, read [references/writing-guide.md](references/writing-guide.md).

For Docusaurus publishing, read [references/docusaurus.md](references/docusaurus.md).

For UI capture guidance, read [references/capture-guide.md](references/capture-guide.md).

For handoff notes, use [references/handoff-template.md](references/handoff-template.md).

Use [scripts/audit-docs.js](scripts/audit-docs.js) to check links, images, short pages, and terminology when a docs folder exists. For project-specific banned terms, pass comma-separated values through `DOCS_BANNED_TERMS`.

## Manual Structure

Prefer this output shape unless the project already has a documentation convention:

```text
manual/
|-- package.json
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

Each module page should include:

- Path: where the user opens the feature.
- Main screen: screenshot and short purpose.
- Controls: buttons, filters, columns, tabs, and row actions.
- Step-by-step tasks: create, edit, delete/cancel, approve/reject, export/import, or other verified workflows.
- Notes and constraints: business rules, required fields, and common mistakes.
- "Ai được làm gì?": role permission table when role behavior differs.

The Docusaurus Home page should include:

- Product identity: logo, product name, short category line, and one strong headline.
- Value proposition: 1-2 concise sentences about what the product helps users control or complete.
- Primary routes: a main CTA to `/docs/intro` and a secondary CTA to the most important module.
- Product proof: a real screenshot from `static/img/screenshots/...`, preferably the dashboard, home, list, or overview screen that best represents the product.
- Quick summary band: 3-4 compact points for the product's core domains.
- Clear separation from docs: `docs/intro.md` remains the manual entry page; `src/pages/index.js` is the product introduction page.

## Docusaurus Lessons Learned

- For GitHub Pages project sites, set `url` to the account domain and `baseUrl` to `/<repo-name>/`. A repo named `owner.github.io` can use `baseUrl: '/'`; a normal project repo cannot.
- Always create a real product Home page at `/` with `src/pages/index.js`; do not use a redirect-only Home page. The brand/logo click should land on this product introduction.
- Keep links and assets Docusaurus-native: docs links can use `/docs/...`; static assets should live under `static/img/...` and be referenced as `/img/...`.
- Use Docusaurus v3 admonition titles with bracket syntax: `:::tip[Mẹo]`, `:::warning[Lưu ý]`. Do not write `:::tip Mẹo`, because it can render as plain text under modern MDX/directive parsing.
- Prefer `_category_.json` plus `sidebars.js` autogenerated sidebars over Docsify `_sidebar.md`.
- Test the production build with `npm run build`, then use a cache-busting query such as `?v=<commit>` when checking GitHub Pages after deployment.

## Permission Rules

Support any number of roles. If the project has no explicit role model, group permissions by observed access level and label the mapping as inferred.

Do not expose technical permission codes such as `module:readAll`, `user:update`, or `order:approve` in user-facing docs. Translate them into natural language such as "Xem danh sách", "Cập nhật thông tin", or "Duyệt yêu cầu".

For each permission table, know the source of truth: observed UI behavior, source/API rule, user-provided matrix, or inference. If the table includes inferred permissions, mention the inference in the handoff note and ask the project owner to confirm it.

When the app has more technical roles than the manual should expose, document both layers:

- In user-facing docs: group roles into clear user groups only when the grouping is verified.
- In `handoff-notes.md`: list the exact technical roles, labels, source file/API/screenshot, and which user-facing group each role maps to.
- Never merge roles such as Admin, Accountant, Manager, Approver, Operator, or Staff unless source behavior proves they share the same access.

## Privacy Rules

Screenshots and examples must not expose real sensitive data. Mask or replace patient/customer names, personal emails, phone numbers, addresses, access tokens, citizen IDs, medical identifiers, financial account numbers, and production credentials before publishing.

Use realistic fake data for examples. Do not include real production URLs, secrets, or internal infrastructure details unless the user explicitly confirms they are intended for the manual.

Use documentation-safe examples by default:

- Email: `nguyenvana@example.vn`
- Phone: `0900 000 000`
- Server URL: `https://example.vn`
- Record code: `REC-000123`

## Quality Bar

Before final delivery:

- `scripts/audit-docs.js` has been run against the manual directory, or the reason it could not run is stated.
- Every referenced local screenshot exists.
- Docusaurus config, sidebar, category metadata, docs links, and static image paths resolve.
- GitHub Pages project sites have `baseUrl` matching the repo name, and the checked public URL includes that repo path.
- Admonitions use Docusaurus v3 title syntax when they have custom titles.
- User-facing pages avoid unresolved placeholders like `[Tên hệ thống]` unless the user explicitly asked for a reusable template.
- Short pages are reviewed for missing workflow detail.
- Workflow pages include screenshots or a handoff note explaining why screenshots could not be captured.
- Terminology is consistent for the target product, for example "Menu bên trái", "Màn hình chính", "Hộp thoại", and "Ai được làm gì?".
- Any unverified assumptions are listed separately for the project owner to confirm.

The final response should report the manual directory, page count, screenshot count, Docusaurus build/audit command result, public or local URL when available, and remaining open questions.
