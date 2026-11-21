# GIAO THỨC CHẠY THỬ TRÊN DỰ ÁN THẬT (PILOT PROTOCOL)

> **Vì sao cần:** Test và golden case chỉ chứng minh cấu trúc của skill. Chúng không chứng minh bộ quy trình giúp một dự án thật ít làm lại hơn. Trước bản 3.8, các script được chỉnh cho tới khi tài liệu mẫu đạt, rồi được coi là đúng; chạy lên tài liệu thật (QLTS, vClassio) thì phần lớn cảnh báo là sai. File này quy định cách đo trên dự án thật để không lặp lại lỗi tự ra đề rồi tự chấm.

---

## 1. Hai mức pilot

| Mức | Làm gì | Chứng minh được | Không chứng minh được |
|---|---|---|---|
| **P1 — Pilot công cụ** | Chạy scripts lên bộ tài liệu thật đã có, phân loại từng cảnh báo là đúng hay sai | Công cụ đọc đúng tài liệu thật; tỷ lệ cảnh báo sai | Quy trình có giúp dự án tốt hơn không |
| **P2 — Pilot quy trình** | Một BA thật dùng skill cho một dự án hoặc một epic từ đầu đến chốt baseline | Số vòng sửa, số lỗi người review bắt được, thời gian, mức hài lòng của người duyệt | Kết quả trên mọi loại dự án (một pilot là một mẫu) |

Kết quả P1 đầu tiên: `tests/golden/real_project_tool_run_2026-11-21.md`. P2 chưa chạy.

---

## 2. Cách chạy P1 (pilot công cụ)

1. Không sửa tài liệu dự án. Chỉ thêm `ba-scheme.json` nếu dự án dùng ID riêng (`scripts/README.md`, mục ba-scheme.json).
2. Chạy `traceability_scan.py`, `preflight_check.py`, `quality_rubric.py` với `--scheme project --strict` khi có `ba-scheme.json`.
3. Lấy mẫu tối thiểu 10 cảnh báo mỗi loại (hoặc tất cả nếu ít hơn), mở đúng dòng trong tài liệu, ghi **Đúng** (tài liệu có lỗi thật) hoặc **Sai** (công cụ đọc nhầm).
4. Cảnh báo sai: tạo fixture tái hiện mẫu viết đó (không chép dữ liệu khách hàng) trong `tests/fixtures/real_world_patterns/`, viết test, sửa script.
5. Ghi bản ghi pilot: số cảnh báo trước và sau, tỷ lệ sai, các mẫu viết đã hỗ trợ, các lỗi thật còn lại.

**Ngưỡng chấp nhận:** tỷ lệ cảnh báo sai dưới 10% trên mẫu đã lấy. Cao hơn thì công cụ chưa dùng được cho dự án đó.

---

## 3. Cách chạy P2 (pilot quy trình)

### 3.1. Chọn dự án

- Một dự án hoặc epic có người duyệt thật và có hạn bàn giao thật. Không dùng dự án mẫu.
- Ưu tiên Tier 2 (đủ gate để đo, không quá dài). Ghi lý do chọn.
- Có một nhóm so sánh: epic tương tự làm theo cách cũ, hoặc số liệu lịch sử của chính nhóm.

### 3.2. Chỉ số

| Chỉ số | Cách đo | Nguồn |
|---|---|---|
| Số vòng sửa trước khi người duyệt ký | Đếm phiên bản giữa `Trình duyệt` đầu tiên và `Baseline` | Lịch sử phiên bản |
| Lỗi người review bắt được | Số phát hiện của review độc lập (H4) theo mức BLOCK/FIX/ASK | Báo cáo review |
| Lỗi lọt sau baseline | Số CR do yêu cầu sai hoặc thiếu (không tính CR do đổi ý) trong 60 ngày | Change Log |
| Thời gian BA | Giờ công từ yêu cầu thô tới baseline | Timesheet hoặc tự ghi |
| Số câu hỏi gửi stakeholder | Đếm câu hỏi trong kế hoạch elicitation và Câu hỏi mở | Tài liệu |
| Nhận định trọng yếu chốt với nguồn gián tiếp | Phải bằng 0 | Sổ nguồn |
| Đánh giá của người duyệt | 3 câu, thang 1–5: dễ đọc, đủ để quyết định, tin được số liệu | Phiếu hỏi sau khi ký |

### 3.3. Ghi nhận

- Mỗi lần BA bỏ qua hoặc làm khác hướng dẫn, ghi lý do. Đây là dữ liệu quan trọng nhất: chỗ quy trình nặng quá hoặc thiếu.
- Không sửa skill trong lúc pilot, trừ lỗi chặn công việc. Ghi lại để sửa sau.

### 3.4. Kết luận

So với nhóm so sánh theo từng chỉ số. Một pilot không đủ để kết luận quy trình tốt hơn; nó đủ để tìm chỗ quy trình sai. Kết luận ghi vào CHANGELOG kèm đường dẫn bản ghi pilot.
