# QUICK-START — Bắt đầu dự án mới trong 5 phút

> Copy hướng dẫn này và làm theo từng bước.

---

## Bước 1: Xác định loại dự án (1 phút)

| Loại | Đặc điểm | Overlay |
|------|---------|---------|
| **In-house** | Team nội bộ, linh hoạt, không hợp đồng | `overlays/inhouse/` |
| **Outsource** | Khách hàng – Nhà cung cấp, hợp đồng, sign-off | `overlays/outsource/` |
| **Product** | SaaS/Platform, data-driven, continuous | `overlays/product/` |
| **Startup/MVP** | Lean, nhanh, validate giả thuyết | `overlays/startup-mvp/` |

→ Mở `overlays/{{loại}}/overlay-config.md` → xem tài liệu nào **bắt buộc**.

---

## Bước 2: Tạo folder dự án (1 phút)

```
{{Tên-dự-án}}/
├── 00-BA-Process-Framework.md    ← Copy từ core/ (nếu cần customize)
├── 01-Vision-Scope.md            ← Copy từ templates/vision-scope.md
├── 02-BRD.md                     ← Copy từ templates/brd.md
├── 03-Stakeholder-Map.md
├── 04-Process-Flow.md
├── 05-SRS.md
├── 06-User-Story-Map.md
├── 07-Data-Model.md
├── 08-UAT-Plan.md
├── 09-Change-Log.md
├── 10-Meeting-Minutes.md
├── 11-Handover-Checklist.md
├── 12-API-Specification.md
├── 13-Risk-Register.md           ← ⭐ NEW v3.0 (từ templates/risk-register.md)
├── 14-Screen-Inventory.md        ← ⭐ NEW v3.0 (từ templates/screen-inventory.md)
├── 15-As-Is-Process.md           ← ⭐ NEW v3.0 (từ templates/as-is-process.md)
└── 16-Data-Migration-Plan.md     ← ⭐ Tùy chọn (từ templates/data-migration-plan.md)
```

> ⚠️ Chỉ copy những file **bắt buộc** theo overlay. Startup chỉ cần 2-4 files.

---

## Bước 3: Điền thông tin cơ bản (2 phút)

Mở từng file → thay thế `{{...}}` bằng thông tin thực:

```
{{TÊN DỰ ÁN}}     → Tên dự án
{{DD/MM/YYYY}}     → Ngày tạo
{{Tên BA}}         → Tên bạn
{{Tên dự án}}      → Tên đầy đủ
```

---

## Bước 4: Bắt đầu theo Phase (1 phút)

### Phase đầu tiên (Inception):
1. ☐ Điền `01-Vision-Scope.md` — đặc biệt: Context, Change, Scope
2. ☐ Điền `03-Stakeholder-Map.md` — Power/Interest Grid
3. ☐ Document As-Is trong `15-As-Is-Process.md` (⭐ bắt buộc trước To-Be)
4. ☐ Điền `13-Risk-Register.md` — Risk patterns từ BRD
5. ☐ Đặt lịch Kickoff Meeting

### ⚡ Mandatory Gates (v3.0+):
- **Pre-Flight:** Chạy `core/pre-flight-checklist.md` TRƯỚC mỗi document
- **Traceability:** Chạy `core/traceability-validator.md` SAU khi sinh xong bộ tài liệu

### Review trước khi chuyển Phase:
→ Mở `core/quality-checklist.md` → làm Phase Gate Checklist

---

## Cheat Sheet — BA Models

| Model | 1 câu tóm tắt | Dùng ở đâu |
|-------|-------------|-----------|
| **BACCM** | 6 yếu tố lõi: Change, Need, Solution, Stakeholder, Value, Context | Review MỌI tài liệu |
| **MoSCoW** | Must/Should/Could/Won't — Must ≤ 60% | BRD, Story Map |
| **INVEST** | Story phải: Independent, Negotiable, Valuable, Estimable, Small, Testable | Story Map |
| **GWT** | Given [context] When [action] Then [result] | Acceptance Criteria |
| **Kano** | Basic (phải có) / Performance (càng nhiều càng tốt) / Excitement (WOW) | Story Map, BRD |
| **5W1H** | What, Why, Who, When, Where, How | Phỏng vấn, BRD |

---

## Tài liệu tham chiếu nhanh

| Cần gì | Mở file |
|--------|---------|
| Không biết viết requirement thế nào | `core/writing-guide.md` |
| Không biết vẽ sơ đồ nào | `core/diagram-guide.md` |
| Review tài liệu trước sign-off | `core/quality-checklist.md` |
| Phân công ai làm gì | `references/raci-matrix.md` |
| Ước lượng effort | `references/estimation-guide.md` |
| Chọn kỹ thuật thu thập yêu cầu | `references/elicitation-techniques.md` |
| Phỏng vấn & moi thông tin KH chuyên sâu | `core/customer-intelligence-guide.md` |
| Thuật ngữ không hiểu | `core/glossary.md` |
| Xem lỗi BA hay mắc | `references/anti-patterns.md` |
| Mẫu viết requirement/AC/BR | `references/writing-examples.md` |
| Đóng gói tài liệu cho audiences khác nhau | `references/communication-packaging.md` |
| Chấm điểm chất lượng requirement | `core/requirement-quality-rubric.md` |
| Phân tích quyết định (A vs B) | `core/decision-analysis-framework.md` |
