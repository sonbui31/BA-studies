# HƯỚNG DẪN SỬ DỤNG BỘ KIT BA 2.2 (AI-ORCHESTRATED)

> **Chào mừng bạn đến với kỷ nguyên BA 2026!**
> Bộ kit "Layered OS" v2.2 giúp bạn làm việc ít hơn nhưng chất lượng cao hơn gấp 10x nhờ phối hợp Gemini 3, Claude 4.6, OpenAI o4, GPT-5.

---

## 🚀 Khởi động nhanh

**Lệnh chính:** `/ba-workflow [tên_dự_án] [mô_tả_ngắn]`

**Ví dụ:**
```
/ba-workflow SaaS-HRM Xây dựng hệ thống quản lý nhân sự cho doanh nghiệp SME
```

**Quy trình tự động:**
1. **Phân loại** — Agent xác định `Product` hay `Outsource`
2. **Khởi tạo** — Tạo folder dự án + file brainstorming
3. **AI Drafting** — Claude 4.6 viết Stories, GPT-5 điền BRD/SRS, o4 tìm Edge Cases
4. **Data Plan** — Đề xuất OKRs cho từng tính năng
5. **Quality Gate** — Tự audit theo BACCM + Quality Checklist

---

## 🤖 Gọi BA-Specialist Agent

Dùng `@ba-specialist` bất cứ lúc nào:

| Yêu cầu | AI được gọi | Kết quả |
|---------|------------|---------|
| "Audit logic thanh toán" | OpenAI o4 | Tìm mâu thuẫn & edge cases |
| "Vẽ sơ đồ luồng đặt hàng" | Claude 4.6 | Mermaid diagram chuẩn |
| "Tổng hợp rủi ro 10 file tài liệu" | Gemini 3 Pro | Báo cáo rủi ro tổng thể |
| "Draft BRD cho tính năng X" | GPT-5 | BRD template đã điền sẵn |

---

## 📂 Cấu trúc thư mục

```
BA-agent/
├── agents/ba-specialist.md     ← Agent persona & protocols
├── workflows/ba-workflow.md    ← Slash command logic
├── BA-document-rule/           ← "Hệ điều hành" (Core + Templates + Overlays)
│   ├── core/                   ← Principles, Guides, Checklist, Glossary
│   ├── templates/              ← 12 templates generic
│   ├── overlays/               ← Config theo loại dự án (Product/Outsource/...)
│   └── references/             ← RACI, Estimation, Elicitation
├── BA-Documents-Product/       ← 11 files mẫu cho Sản phẩm (Metric-heavy)
├── BA-Documents-Outsource/     ← 12 files mẫu cho Thuê ngoài (Sign-off-heavy)
├── DOCUMENT-MAP.md             ← Bản đồ chỉ đường cho mọi file
└── so_do.md                    ← Thư viện Mermaid (10 loại sơ đồ, 868 dòng)
```

---

## 📈 3 nguyên tắc cốt lõi

1. **Visual First** — Một sơ đồ Mermaid tốt hơn 1000 chữ
2. **Metric First** — Mỗi tính năng phải gắn với chỉ số đo lường (North Star)
3. **AI Orchestra** — Dùng Gemini để đọc, o4 để nghĩ, Claude để vẽ/viết

---

## 🛠 Tùy chỉnh

- **Sửa nguyên tắc:** `BA-document-rule/core/principles.md`
- **Sửa template:** `BA-document-rule/templates/*.md`
- **Thêm overlay mới:** Tạo folder trong `BA-document-rule/overlays/`
