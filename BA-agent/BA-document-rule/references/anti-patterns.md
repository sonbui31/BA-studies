# ANTI-PATTERNS BA — 15 Sai lầm Thường gặp và Cách Tránh

> **Mục đích:** Biết "nên làm" chưa đủ — BA phải biết "ĐỪNG làm gì" để tránh lặp lại sai lầm phổ biến.
> **Nguồn:** Tổng hợp từ kinh nghiệm dự án thực tế + IIBA case studies + industry research.
> **Phiên bản:** v3.2 | **Ngày:** 03/04/2026

---

## 🔴 CRITICAL — Sai lầm chí mạng (gây fail dự án)

### AP-01: "Jump to Solution" — Nhảy thẳng vào giải pháp

| Mô tả | KH nói "cần hệ thống quản lý tài sản" → BA lập tức viết SRS mà chưa hiểu WHY |
|---|---|
| **Hậu quả** | Build đúng hệ thống nhưng SAI nhu cầu. Rework 60-80% |
| **Root Cause** | Áp lực deadline / thiếu quy trình Elicitation |
| **Tín hiệu** | BRD không có Problem Statement. "Tại sao cần?" trả lời "vì sếp bảo" |
| **Cách tránh** | **Mandatory Elicitation Gate** (Step 0) — Hỏi "Tại sao?" trước "Cái gì?" |
| **Tham chiếu** | `core/customer-intelligence-guide.md` — Probing Level 1-6 |

---

### AP-02: "Assumption is Fact" — Giả định = Sự thật

| Mô tả | BA giả định KH muốn X mà không confirm. "Chắc họ muốn thế này" |
|---|---|
| **Hậu quả** | Feature không ai dùng. KH nói "tôi không yêu cầu thế" |
| **Root Cause** | Lười confirm / sợ hỏi "ngu" |
| **Tín hiệu** | BRD nhiều assumption nhưng Status = "Unvalidated" |
| **Cách tránh** | Mọi assumption → ghi vào bảng → confirm với stakeholder → chỉ sau khi confirmed mới viết requirement |
| **Tham chiếu** | `core/pre-flight-checklist.md` — PFC-BRD item 7 |

---

### AP-03: "Skip As-Is" — Bỏ qua hiện trạng

| Mô tả | BA viết To-Be mà không document quy trình hiện tại |
|---|---|
| **Hậu quả** | To-Be không fit thực tế. Users bỏ hệ thống mới vì workflow quá khác |
| **Root Cause** | "Hệ thống cũ dở quá, viết mới hoàn toàn" |
| **Tín hiệu** | Không có As-Is process document. Gap Analysis = "N/A" |
| **Cách tránh** | **Mandatory As-Is (Step 2.5)** — nếu greenfield thì ghi "N/A + lý do" |
| **Tham chiếu** | `templates/as-is-process.md` |

---

### AP-04: "Sign-off ≠ Understanding" — KH ký nhưng không hiểu

| Mô tả | KH ký sign-off BRD/SRS nhưng thực tế chưa đọc kỹ. Sau UAT mới phát hiện sai |
|---|---|
| **Hậu quả** | UAT fail hàng loạt. Blame game. CR explosion |
| **Root Cause** | BA gửi tài liệu 25 trang → KH không muốn đọc |
| **Tín hiệu** | KH sign-off quá nhanh (< 1 ngày cho SRS 20 trang). Không có câu hỏi nào |
| **Cách tránh** | Walk-through meeting: BA trình bày từng section → KH confirm từng phần. Dùng wireframe/prototype thay text thuần |
| **Tham chiếu** | `core/writing-guide.md` — Section 8 (Review Workflow) |

---

### AP-05: "No Traceability" — Requirements mồ côi

| Mô tả | BRD ghi 20 BRQs nhưng SRS chỉ cover 12. 8 BRQs "bay hơi" không ai biết |
|---|---|
| **Hậu quả** | Feature thiếu. UAT fail. Phát hiện muộn → costly rework |
| **Root Cause** | Viết docs riêng lẻ, không cross-check |
| **Tín hiệu** | Không có Traceability Matrix. ID không nhất quán giữa docs |
| **Cách tránh** | **Traceability Validator (Step 6.7)** — auto-scan BRQ→FR→US→TC chain |
| **Tham chiếu** | `core/traceability-validator.md` |

---

## 🟡 HIGH — Sai lầm nghiêm trọng (gây delay + rework)

### AP-06: "Vague Requirements" — Yêu cầu mơ hồ

| Mô tả | "Hệ thống phải nhanh", "Giao diện phải đẹp", "Dùng dễ" |
|---|---|
| **Hậu quả** | Dev không biết build gì. QC không biết test gì. UAT vĩnh viễn không pass |
| **Cách tránh** | SMART requirements. "Nhanh" → "Load < 3s cho 95% requests". "Đẹp" → wireframe sign-off |
| **Tham chiếu** | `core/writing-guide.md` — Section 5 (SMART Checklist) |

---

### AP-07: "Scope Creep Silence" — Im lặng trước scope phình

| Mô tả | KH yêu cầu thêm feature → BA cứ nhận mà không ghi CR → scope phình dần |
|---|---|
| **Hậu quả** | Timeline nổ. Budget nổ. Team burn-out |
| **Cách tránh** | Mọi thêm sau sign-off = **CR chính thức**. Có Impact Analysis + Effort re-estimation |
| **Tham chiếu** | `templates/change-log.md`, `core/impact-analysis-guide.md` |

---

### AP-08: "Gold Plating" — Vẽ nhiều hơn KH cần

| Mô tả | BA tự thêm feature "nice-to-have" vì nghĩ KH sẽ thích. Không ai yêu cầu |
|---|---|
| **Hậu quả** | Tốn effort dev không cần thiết. Delay feature Must |
| **Cách tránh** | MoSCoW bắt buộc. Only Must + Should trong Phase 1. Could = Phase 2 |
| **Tham chiếu** | `core/principles.md` — Section 3 (MoSCoW) |

---

### AP-09: "Silo Documentation" — Viết tài liệu trong silo

| Mô tả | BA viết BRD xong chuyển sang SRS → không update BRD khi phát hiện thiếu |
|---|---|
| **Hậu quả** | BRD nói 1 đằng, SRS nói 1 nẻo. Cross-doc inconsistency |
| **Cách tránh** | **Inline Audit (Step 6)** — check K (Consistency) sau mỗi section. Living documents |
| **Tham chiếu** | `core/evaluation-protocol.md` — Inline Audit |

---

### AP-10: "Stakeholder Avoidance" — Né stakeholder khó

| Mô tả | Stakeholder hostile/silent → BA tránh giao tiếp → thiếu input quan trọng |
|---|---|
| **Hậu quả** | Requirement thiếu perspective. Go-live mới biết "phòng đó không đồng ý" |
| **Cách tránh** | 4 chiến lược trong Customer Intelligence Guide: Silent → 1:1, Hostile → Empathy First |
| **Tham chiếu** | `core/customer-intelligence-guide.md` — Section 6 |

---

## 🟠 MEDIUM — Sai lầm phổ biến (giảm chất lượng)

### AP-11: "Text-Only Specs" — Tài liệu chỉ có chữ

| Mô tả | SRS 25 trang text thuần, không diagram, không wireframe |
|---|---|
| **Hậu quả** | Dev hiểu sai. Phải hỏi đi hỏi lại. Multiple iterations |
| **Cách tránh** | **Visual First** — Mỗi feature ≥ 1 diagram. Screen Inventory bắt buộc |
| **Tham chiếu** | `core/screen-inventory-guide.md`, `core/diagram-guide.md` |

---

### AP-12: "Copy-Paste Templates" — Copy template xong là xong

| Mô tả | Fill template chỉ để điền placeholder → tài liệu đẹp nhưng rỗng nội dung |
|---|---|
| **Hậu quả** | Tài liệu "có vẻ" đầy đủ nhưng không ai dùng được |
| **Cách tránh** | Nguyên tắc #10: "Template là khởi đầu, không phải kết thúc" + Pre-Flight Engine check |
| **Tham chiếu** | `core/principles.md` — Nguyên tắc 10 |

---

### AP-13: "UAT = Cuối cùng mới test" — Dồn UAT vào cuối

| Mô tả | UAT chỉ 3-5 ngày cuối dự án. Bug phát hiện muộn |
|---|---|
| **Hậu quả** | Fix lỗi gấp. Go-live delay. Quality kém |
| **Cách tránh** | Rolling UAT mỗi sprint. Pre-Flight cho UAT Plan (PFC-UAT) từ đầu |
| **Tham chiếu** | `templates/uat-plan.md`, `core/pre-flight-checklist.md` — PFC-UAT |

---

### AP-14: "Ignore NFRs" — Bỏ quên Non-Functional Requirements

| Mô tả | BRD/SRS chỉ focus chức năng. Không nói gì về Performance, Security, Availability |
|---|---|
| **Hậu quả** | Hệ thống "chạy" nhưng chậm, không an toàn, hay sập |
| **Cách tránh** | PFC-SRS item 9: ≥ 5 NFRs bắt buộc. NFR Traceability chain đến NFR-TC |
| **Tham chiếu** | `core/pre-flight-checklist.md` — PFC-SRS, `core/traceability-validator.md` |

---

### AP-15: "AI = Magic" — Tin AI output 100%

| Mô tả | Copy-paste AI output vào tài liệu mà không verify. "AI nói thế nên đúng" |
|---|---|
| **Hậu quả** | Hallucination → requirement sai. Data leak nếu PII gửi lên public API |
| **Cách tránh** | Golden Rule: "AI draft, BA review". Security first — không đưa PII lên AI |
| **Tham chiếu** | `core/principles.md` — Section 11 (AI Golden Rules) |

---

## 📋 Quick Reference — Anti-Pattern Checklist

> Dùng như self-check trước khi sign-off tài liệu.

| # | Anti-Pattern | Tôi có mắc không? | Check |
|---|---|---|:---:|
| AP-01 | Nhảy vào giải pháp chưa hiểu vấn đề | ☐ |
| AP-02 | Giả định chưa confirm | ☐ |
| AP-03 | Bỏ qua quy trình hiện tại | ☐ |
| AP-04 | KH ký nhưng chưa hiểu | ☐ |
| AP-05 | Requirement không trace được | ☐ |
| AP-06 | Yêu cầu mơ hồ (không SMART) | ☐ |
| AP-07 | Nhận thêm scope không ghi CR | ☐ |
| AP-08 | Tự thêm feature không ai yêu cầu | ☐ |
| AP-09 | Tài liệu không nhất quán chéo | ☐ |
| AP-10 | Né stakeholder khó | ☐ |
| AP-11 | Tài liệu chỉ chữ, không hình | ☐ |
| AP-12 | Fill template cho có | ☐ |
| AP-13 | UAT dồn cuối | ☐ |
| AP-14 | Quên NFR | ☐ |
| AP-15 | Tin AI không verify | ☐ |
