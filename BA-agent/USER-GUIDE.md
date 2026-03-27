# HƯỚNG DẪN SỬ DỤNG BỘ KIT BA 2.6.1 (ULTIMATE AI-ORCHESTRATED)

> **Chào mừng bạn đến với kỷ nguyên BA 2026!**
> Bộ kit "Layered OS" v2.6.1 — tự động hóa toàn diện: dự báo rủi ro, khai thác thông tin KH, và vẽ sơ đồ tự động từ dữ liệu thô.

---

## 🚀 Khởi động nhanh

**Lệnh chính:** `/ba-workflow [tên_dự_án] [mô_tả_ngắn]`

**Quy trình 2.6.1:**
1. **Predictive Scan** — Dự báo rủi ro Scope Creep ngay từ đầu.
2. **Customer Intelligence** — Phỏng vấn & khai thác insight từ KH.
3. **AI Drafting & Auto-Diagram** — Viết tài liệu + Vẽ sơ đồ tự động + Wireframes.
4. **Traceability Audit** — Đối soát Code vs Yêu cầu để tránh sai sót.
5. **Quality Gate** — Chấm điểm C-S-K-A.

---

## 🤖 Các kỹ năng "Hạng nặng" (8 Ultimate Skills)

| Kỹ năng | Lệnh tiêu biểu | Kết quả |
|---|---|---|
| **Predictive BA** | `@ba-specialist dự báo rủi ro dự án này` | Cảnh báo Scope Creep & Chậm deadline |
| **Code-to-Req Audit** | `@ba-specialist đối soát SRS này với code` | Tìm lỗi logic giữa tài liệu và thực tế |
| **Impact Analysis** | `@ba-specialist phân tích ảnh hưởng thay đổi X`| Tìm file mâu thuẫn dắt dây |
| **Persona Sim** | `@ba-specialist đóng vai CFO phản biện` | Stress-test yêu cầu trước khi họp |
| **AI Prototyping** | `@ba-specialist tạo wireframe cho tính năng X`| Link bản phác thảo UI trực quan |
| **Customer Intelligence** | `@ba-specialist phỏng vấn KH cho dự án X` | Bộ câu hỏi chiến lược + phân tích insight |
| **Auto-Diagram Engine** | `@ba-specialist vẽ [loại sơ đồ] cho [quy trình]` | Mermaid diagram tự động từ dữ liệu thô |

---

## 🕵️ Chi tiết Kỹ năng mới (v2.6 → v2.6.1)

### 1. Đối soát Yêu cầu vs Mã nguồn (v2.6)
Đảm bảo Dev thực hiện đúng 100% những gì BA đã viết.
- **Lệnh:** `@ba-specialist đối soát [tài_liệu] với [thư_mục_code]`

### 2. Dự báo BA & Rủi ro (v2.6)
Sử dụng dữ liệu để "nhìn thấy" tương lai dự án.
- **Lệnh:** `@ba-specialist dự báo rủi ro phình scope cho dự án này`

### 3. Customer Intelligence (v2.6)
Khai thác tối đa thông tin từ KH — từ trao đổi, moi móc nhu cầu ẩn đến phân tích tâm lý.
- **Lệnh:** `@ba-specialist phỏng vấn KH cho dự án [tên]`
- **Lệnh:** `@ba-specialist phân tích insight từ buổi phỏng vấn`
- **Lệnh:** `@ba-specialist tạo câu hỏi deep-dive cho [stakeholder/topic]`

### 4. Auto-Diagram Engine (v2.6.1) ✨ MỚI
Chỉ cần đưa dữ liệu thô — agent tự chọn đúng loại sơ đồ và vẽ tự động.

| Bạn nói... | Agent tự vẽ |
|---|---|
| "ai tương tác với hệ thống" | Context Diagram |
| "ai làm gì / chức năng" | Use Case Diagram |
| "quy trình / luồng / BPMN" | Swimlane / BPMN 2.0 |
| "hệ thống gọi nhau / API" | Sequence Diagram |
| "trạng thái / vòng đời" | State Diagram |
| "bảng dữ liệu / database" | ERD |
| "trải nghiệm / pain point" | User Journey Map |
| "điều kiện / nếu...thì" | Decision Flowchart |
| "timeline / sprint" | Gantt Chart |

- **Lệnh mẫu:** `@ba-specialist vẽ sơ đồ cho quy trình: [paste quy trình thô vào đây]`

---

## 📂 Cấu trúc thư mục

```
BA-agent/
├── agents/ba-specialist.md     ← Agent persona & 8 Ultimate Skills (v2.6.1)
├── workflows/ba-workflow.md    ← Slash command logic (9 bước)
├── BA-document-rule/           ← "Hệ điều hành" (Core + Templates + Overlays)
│   ├── core/                   ← 12 files: Principles, Guides, Intelligence...
│   ├── templates/              ← 12 templates generic
│   ├── overlays/               ← Config theo loại dự án (Product/Outsource/...)
│   └── references/             ← RACI, Estimation, Elicitation
├── BA-Documents-Product/       ← 11 files mẫu cho Sản phẩm (Metric-heavy)
├── BA-Documents-Outsource/     ← 12 files mẫu cho Thuê ngoài (Sign-off-heavy)
├── DOCUMENT-MAP.md             ← Bản đồ chỉ đường cho mọi file
├── USER-GUIDE.md               ← Hướng dẫn sử dụng bộ kit (file này)
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
