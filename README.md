# BA Studies

Hệ thống kiến thức và công cụ Business Analysis, được tổ chức thành 3 phần chính.

---

## Cấu trúc repo

```
BA studies/
├── BA-agent/              ← Lõi hệ thống BA Agent (AI trợ lý phân tích nghiệp vụ)
├── projects/              ← Các dự án thực tế / dự án mẫu
├── learning/              ← Tài liệu học tập BA (sách, khóa học, bài tập)
└── BA-WORKFLOW-GUIDE.md   ← Hướng dẫn quy trình xây dựng BA Agent
```

### 📦 [BA-agent/](BA-agent/)

Hệ thống AI Agent đóng vai Business Analyst — thu thập yêu cầu, phân tích nghiệp vụ, sinh tài liệu BRD/SRS/User Story, review và audit chất lượng.

| Thành phần | Mô tả |
|---|---|
| [SKILL.md](BA-agent/SKILL.md) | Entrypoint cho skill system |
| [README.md](BA-agent/README.md) | Hướng dẫn chat 1-1 chi tiết với BA-agent |
| [USER-GUIDE.md](BA-agent/USER-GUIDE.md) | Hướng dẫn sử dụng |
| [DOCUMENT-MAP.md](BA-agent/DOCUMENT-MAP.md) | Bản đồ toàn bộ tài liệu BA |
| `agents/` | Agent persona (ba-specialist) |
| `workflows/` | Quy trình BA workflow |
| `scripts/` | 14 scripts tự động: preflight, quality rubric, traceability, knowledge search... |
| `BA-document-rule/` | Bộ rule, template, overlay theo loại dự án |
| `Curated templates/` | Template thực chiến BRD/SRS/User Story |
| `BA-Documents-Outsource/` | Bộ tài liệu mẫu dự án outsource |
| `BA-Documents-Product/` | Bộ tài liệu mẫu dự án product/SaaS |

### 📁 [projects/](projects/)

Dự án thực tế sử dụng BA-agent. Xem [projects/README.md](projects/README.md) để biết chi tiết.

| Dự án | Loại | Mô tả |
|---|---|---|
| QLTS | In-house | Hệ thống Quản lý Tài sản |
| vClassio_app | Product | Ứng dụng VClassio (parent app, teacher app) |
| SaaS-HRM-Platform | Product/SaaS | Nền tảng quản lý nhân sự SaaS |

### 📚 learning/

Thư viện tài liệu học tập BA — sách, khóa học, bài tập, template gốc. *Không được git track (gitignored).*

---

## Bắt đầu nhanh

1. **Đọc** [BA-WORKFLOW-GUIDE.md](BA-WORKFLOW-GUIDE.md) để hiểu quy trình BA Agent
2. **Sử dụng** BA-agent theo hướng dẫn tại [BA-agent/README.md](BA-agent/README.md)
3. **Tham khảo** dự án mẫu tại [projects/](projects/)

### Prompt bắt đầu

```text
Dùng BA-agent cho dự án: [tên dự án].
Mô tả ngắn: [mô tả].
Hãy làm việc với tôi theo kiểu hỏi đáp 1-1.
```

---

## Scripts thường dùng

```powershell
# Kiểm tra preflight trước khi viết tài liệu
python BA-agent\scripts\preflight_check.py <project-folder>

# Chấm chất lượng requirement
python BA-agent\scripts\quality_rubric.py <project-folder-or-file>

# Kiểm tra traceability
python BA-agent\scripts\traceability_scan.py <project-folder>

# Tra cứu kiến thức BA
python BA-agent\scripts\knowledge_search.py "topic" --format markdown

# Audit toàn bộ BA-agent
python BA-agent\scripts\ba_bundle_audit.py
```
