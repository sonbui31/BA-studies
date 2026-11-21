# RIGOR TIERS: Mức độ chặt chẽ theo rủi ro

> **Mục đích:** Điều chỉnh độ sâu tài liệu và kịch bản AC theo rủi ro. Các mức tối thiểu dưới đây là quy ước của BA-agent, không phải số lượng do Scrum hay Gherkin quy định.
> **Áp dụng:** Xác định Tier ở Bước 1 (cùng lúc phân loại dự án), ghi vào đầu tài liệu. Tier có thể thay đổi theo từng module trong cùng dự án.

---

## 1. Xác định Tier

Chấm từng câu: có = 1 điểm.

| # | Câu hỏi |
|:-:|---|
| 1 | Xử lý tiền, thanh toán, hoặc quyết định tài chính? |
| 2 | Xử lý dữ liệu cá nhân nhạy cảm (trẻ em, sức khỏe, sinh trắc học, định danh, vị trí)? |
| 3 | Có yêu cầu pháp lý hoặc hợp đồng với chế tài (phạt, mất giấy phép, bồi thường)? |
| 4 | Sai sót có thể gây hại cho người dùng (an toàn, danh tiếng, quyền lợi)? |
| 5 | Nhiều hệ thống hoặc đối tác phải tích hợp, và tích hợp chưa được xác nhận? |
| 6 | Có xử lý đồng thời (hai người cùng thao tác một tài nguyên) hoặc giao dịch không đảo ngược? |
| 7 | Thay đổi sau go-live khó hoặc đắt (hợp đồng cố định giá, firmware, dữ liệu đã gửi ra ngoài)? |

| Điểm | Tier | Điển hình |
|:-:|:-:|---|
| 0–1 | **Tier 1: Nhẹ** | Màn hình tra cứu, báo cáo nội bộ, CRUD đơn giản |
| 2–3 | **Tier 2: Chuẩn** | Quy trình phê duyệt, thông báo, tính năng có logic nghiệp vụ |
| 4+ | **Tier 3: Cao** | Thanh toán, nhận diện sinh trắc, hồ sơ bệnh án, dữ liệu trẻ em, báo cáo pháp lý |

Ghi đè: câu 2 hoặc câu 3 có điểm thì tối thiểu là Tier 2. Dự án đã ký hợp đồng cố định giá (outsource) tối thiểu là Tier 2.

---

## 2. Yêu cầu theo Tier

| Hạng mục | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Tài liệu | Mini-Brief (Lối Agile Lite) hoặc BRD rút gọn | BRD + SRS theo Curated templates | BRD + SRS đầy đủ + mục tuân thủ + đánh giá rủi ro pháp lý |
| Stakeholder Map | Quick Map 3 cột | 7 cột + Power/Interest | 7 cột + người ra quyết định và đơn vị pháp chế/bảo mật |
| Business Case / Strategy | Một đoạn lý do | Business Case rút gọn, có Do Nothing | Business Case đầy đủ (`strategy-analysis-guide.md`), có độ nhạy |
| BPMN | Chỉ luồng có nhánh rẽ | Luồng chính và ngoại lệ chính | Toàn bộ, kèm exception và rollback |
| Số kịch bản AC mỗi story | ≥ 2 (Happy + Negative), ghi rõ vì sao bỏ Boundary và Race | ≥ 4 (Happy, Negative, Boundary, Permission) | ≥ 4, thêm Race, Idempotent, Network khi áp dụng; không giới hạn 8, tách story nếu quá lớn |
| NFR | Hiệu năng cơ bản | NFR định lượng theo mục chính | NFR đầy đủ + threat/privacy review + kiểm thử NFR |
| Traceability | `US → AC` | Chuỗi canonical đủ | Canonical strict + đối chiếu hai chiều + Conflict Log |
| Benefit Register | KPI chính | Benefit Register (`solution-evaluation-guide.md`) | Benefit Register + guardrail + review 30/60/90 |
| Review người thật | BA tự rà bằng checklist | BA + 1 người khác | BA + SME + pháp lý/bảo mật + Sponsor ký |
| Review vai trò (`persona-simulation.md`) | R-BA + vai trò theo loại tài liệu | + R-SPONSOR, R-STAFF, R-TIME, R-QA, R-SEC, R-PM | Đủ 21 vai trò |
| Nguồn yêu cầu (`evidence-source-gate.md`) | Cột "Nguồn" trong bảng Fact; nguồn trực tiếp cho quy tắc nhánh rẽ và phạm vi | Sổ nguồn + kế hoạch elicitation; nguồn trực tiếp cho cả 5 nhóm nhận định trọng yếu | Như Tier 2, baseline và con số Business Case ở E3 trở lên |
| Cách chốt | Agile Lite | Theo tài liệu hoặc theo lát cắt (`slice-baselining.md`) | Theo tài liệu hoặc theo lát cắt; trình duyệt trọn bộ nếu hợp đồng/cơ quan quản lý yêu cầu |
| Kiểm tra sau mỗi tài liệu | Checklist Anti-AI, `preflight_check`, `ai_smell_scan` | + `quality_rubric`, `traceability_scan --strict`, `persona_review_check` | + đối chiếu nghĩa hai chiều, Conflict Log |

---

## 3. Điều không được nới ở bất kỳ Tier nào

1. Phân biệt Fact, Assumption, Open Question; không bịa số liệu; không ghi "đã chốt" cho quy tắc nhánh rẽ hoặc phạm vi khi chỉ có nguồn gián tiếp.
2. Mỗi User Story có ít nhất một Acceptance Criteria quan sát được và đo được.
3. Mọi yêu cầu truy được về một mục tiêu hoặc nhu cầu.
4. Nhãn `[AI-Drafted]` cho đến khi người thật xác nhận.
5. Dữ liệu nhạy cảm không bao giờ nằm ở Tier 1.
6. Tiếng Việt có dấu đầy đủ ở phần thuyết minh.

---

## 4. Ghi lại lựa chọn Tier

Ở đầu tài liệu:

```
Tier: 2 (Chuẩn). Điểm rủi ro: 3/7 (câu 3, 5, 6)
Điều chỉnh so với chuẩn: bỏ BPMN cho module Tin tức vì không có nhánh rẽ
Người xác nhận Tier: [vai trò], ngày [DD/MM/YYYY]
```

Khi nới so với chuẩn, ghi lý do ngắn. Khi tăng Tier giữa chừng (phát hiện dữ liệu nhạy cảm, yêu cầu pháp lý mới), quay lại bổ sung phần còn thiếu trước khi viết tiếp.

---

## 5. Quan hệ với quy tắc khác

- `SKILL.md`: Hard Gate 1–2 áp dụng cho lối đầy đủ; Tier 1 có thể đi Lối Agile Lite.
- `Curated templates/04-Acceptance-Criteria-Template.md`: bốn kịch bản là ví dụ cho một giao dịch; áp dụng số kịch bản theo Tier và rule thực tế trong bảng trên.
- `traceability_scan.py --strict`: dùng cho Tier 2 và 3.
- `intake-triage.md`: Tier chọn độ chặt, lối (L0–L4) chọn quy trình. Một việc nhỏ (L2) vẫn có thể là Tier 3.
