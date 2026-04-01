# HƯỚNG DẪN SỬ DỤNG BỘ KIT BA 3.0 (MULTI-LLM ORCHESTRATED + ACTIONABLE GATES)

> **Chào mừng bạn đến với BA-Agent 3.0!**
> Bộ kit "Layered OS" v3.0 — **"Right First Time"**: Mandatory gates + Inline audit + Auto-traceability.
> Giữ Multi-LLM orchestration (Claude 4.6, o4, GPT-5, Gemini 3) với vai trò CỤ THỂ tại từng bước.

---

## 🚀 Khởi động nhanh

**Lệnh chính:** `/ba-workflow [tên_dự_án] [mô_tả_ngắn]`

**Quy trình 3.0 (12 bước):**

```
🚪 GATES (bắt buộc)
  0. Elicitation Gate — Phỏng vấn / Extract insight từ KH
  1. Risk Scan — Phát hiện rủi ro + sinh Risk Register
  2. Customer Intelligence — Deep probing, hidden needs
  2.5 As-Is Process — Document quy trình hiện tại + Gap Analysis

📝 GENERATION (có Pre-Flight)
  3. Template Selection — Chọn overlay + plan metrics
  4. Screen Inventory — Liệt kê screens + Navigation Map
  5. Document + Diagram + Wireframe — PRE-FLIGHT trước mỗi doc

✅ VALIDATION (multi-layer)
  6. AI Quality Gate — C-S-K-A inline audit
  6.5 Pre-Flight Verify — Re-check sau khi viết
  6.7 Traceability Validation — BRQ→FR→US→TC chain check
  7. Impact & Persona Sim — Cross-file scan + stress-test
  8. Final Report — Scorecard + Risk + Traceability + Diagrams
```

---

## 🆕 Có gì mới trong v3.0?

| Feature | v2.6.1 | v3.0 |
|---------|--------|------|
| **Elicitation** | Có guide, chưa enforce | ⭐ MANDATORY Step 0 — không bỏ qua |
| **As-Is Process** | Không có | ⭐ Bắt buộc trước To-Be |
| **Pre-Flight Checklist** | Không có | ⭐ Check TRƯỚC + SAU mỗi doc |
| **Traceability Validator** | Thủ công | ⭐ Tự động scan cross-doc |
| **Screen Inventory** | Không có | ⭐ Mỗi Feature ≥ 1 screen |
| **Risk Register** | Predictive lý thuyết | ⭐ Actionable register + auto-detect |
| **C-S-K-A Audit** | Chỉ cuối | ⭐ Inline (sau mỗi section) |
| **Multi-LLM** | Claim chung | ⭐ Vai trò cụ thể tại từng step |

---

## 🤖 Các kỹ năng (11 Skills)

| Kỹ năng | Lệnh tiêu biểu | Kết quả | LLM |
|---|---|---|---|
| **Elicitation Gate** | `@ba-specialist phỏng vấn KH cho dự án X` | Interview questions + Insight Cards | Claude 4.6 |
| **Risk Management** | `@ba-specialist tạo risk register dựa trên BRD` | Risk Register + Heatmap | o4 |
| **As-Is Documentation** | `@ba-specialist document As-Is cho quy trình [X]` | As-Is Swimlane + Gap Analysis | — |
| **Pre-Flight Engine** | (Tự động chạy trước mỗi doc) | Checklist PASS/FAIL | — |
| **Traceability Validator** | `@ba-specialist kiểm tra truy vết dự án` | Full Chain Report + Gaps | Gemini 3 |
| **Screen Inventory** | `@ba-specialist liệt kê screens cho dự án X` | Screen list + Nav map + Wireframes | — |
| **Auto-Diagram Engine** | `@ba-specialist vẽ [loại] cho [quy trình]` | Mermaid diagram tự động | — |
| **Code-to-Req Audit** | `@ba-specialist đối soát SRS với code` | Audit Report + Match/Mismatch | Claude + o4 |
| **Impact Analysis** | `@ba-specialist phân tích ảnh hưởng thay đổi X` | Dependency scan | Gemini 3 |
| **Persona Simulation** | `@ba-specialist đóng vai CFO phản biện` | Stress-test report | o4 |
| **AI Prototyping** | `@ba-specialist tạo wireframe cho feature X` | StitchMCP wireframe | — |

---

## 📂 Cấu trúc thư mục

```
BA-agent/
├── agents/ba-specialist.md     ← Agent persona & 11 Skills (v3.0)
├── workflows/ba-workflow.md    ← Slash command logic (12 bước với gates)
├── BA-document-rule/           ← "Hệ điều hành" (Core + Templates + Overlays)
│   ├── core/                   ← 15 files: Principles, Guides, Pre-Flight, Validator...
│   │   ├── pre-flight-checklist.md    ⭐ NEW: Check trước khi viết
│   │   ├── traceability-validator.md  ⭐ NEW: Auto-scan gaps
│   │   ├── screen-inventory-guide.md  ⭐ NEW: Screen & Wireframe guide
│   │   └── ... (12 existing files)
│   ├── templates/              ← 16 templates generic
│   │   ├── as-is-process.md           ⭐ NEW: As-Is documentation
│   │   ├── risk-register.md           ⭐ NEW: Actionable risk register
│   │   ├── data-migration-plan.md     ⭐ NEW: Migration with rollback
│   │   ├── screen-inventory.md        ⭐ NEW: Screen tracking
│   │   └── ... (12 existing templates)
│   ├── overlays/               ← Config theo loại dự án
│   └── references/             ← RACI, Estimation, Elicitation
├── BA-Documents-Product/       ← 11 files mẫu cho Sản phẩm
├── BA-Documents-Outsource/     ← 12 files mẫu cho Thuê ngoài
├── DOCUMENT-MAP.md             ← Bản đồ chỉ đường cho mọi file
├── USER-GUIDE.md               ← Hướng dẫn sử dụng (file này)
└── so_do.md                    ← Thư viện Mermaid (10 loại sơ đồ)
```

---

## 📈 4 Nguyên tắc cốt lõi v3.0

1. **Right First Time** — Pre-Flight + Inline Audit = giảm iterations từ 4+ → ≤ 2
2. **Facts, not Theory** — Risk Register từ patterns thực tế, không predict từ "hàng ngàn mẫu"
3. **Visual First** — Screen Inventory + Wireframe TRƯỚC khi code. Diagram tốt hơn 1000 chữ
4. **Multi-LLM Precision** — Claude viết, o4 nghĩ, Gemini đọc, GPT-5 draft specs

---

## 🛠 Tùy chỉnh

- **Sửa nguyên tắc:** `BA-document-rule/core/principles.md`
- **Sửa template:** `BA-document-rule/templates/*.md`
- **Sửa Pre-Flight items:** `BA-document-rule/core/pre-flight-checklist.md`
- **Sửa traceability rules:** `BA-document-rule/core/traceability-validator.md`
- **Thêm overlay mới:** Tạo folder trong `BA-document-rule/overlays/`
