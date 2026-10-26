# Senior judgement run: 2026-10-26

Mục đích: kiểm tra BA-agent (SKILL.md và các guide trỏ tới) trả lời tình huống phán đoán như thế nào. Chấm theo `senior_signals` viết trước khi chạy.

## Phương pháp

- Mỗi tình huống do một subagent riêng trả lời như BA-agent. Agent đọc `SKILL.md` và các file SKILL.md trỏ tới.
- Vòng 1 (4 tình huống đầu): agent không bị cấm đọc `tests/golden/`. Một agent tự báo đã đọc file đáp án. Tình huống KPI gần giống ví dụ trong `solution-evaluation-guide.md`. **Kết quả vòng 1 không dùng để chấm.**
- Vòng 2 (4 tình huống mới: `vague_nfr_all_must`, `refund_retry_double`, `fixed_price_unconfirmed_api`, `uat_change_request`): đáp án viết trước khi chạy, agent bị cấm đọc `tests/`, `senior-ba-rubric.md`, `case-study-parent-app.md` và phải liệt kê file đã đọc. Cả 4 danh sách file đều tuân thủ.
- Người chấm: phiên làm việc chính (không phải người thật, không phải LLM-judge độc lập).

## Kết quả vòng 2

| Tình huống | Đạt | Chưa đạt |
|---|---|---|
| `vague_nfr_all_must` | Chỉ ra không kiểm thử được, không bịa số, định nghĩa Must, nêu ngân sách chỉ đủ 60%, ba lựa chọn, Won't có điều kiện | Để trống `___` thay vì đề xuất ngưỡng khởi điểm gắn `[Giả định]` |
| `refund_retry_double` | Idempotent, máy trạng thái, đối soát, log kiểm toán, chuyển câu hỏi pháp lý, Tier 3 | Không phác kịch bản AC nào vì dừng ở gate |
| `fixed_price_unconfirmed_api` | Không báo giá cố định, khoảng giá theo kịch bản, PERT, khảo sát kỹ thuật, CR sau này | CR chưa được đưa vào nội dung gửi khách |
| `uat_change_request` | Đủ 5 ý: CR, phân biệt mức thay đổi, người duyệt đúng, 3 lựa chọn, đóng băng tài liệu | Không có |

## Điều chỉnh sau lần chạy

- `SKILL.md`: Gate 3 và 4 không chặn việc phác kịch bản AC dạng `[DỰ THẢO, CHƯA DUYỆT]`; thiếu ngưỡng thì đề xuất giá trị khởi điểm gắn `[Giả định]`.
- `elicitation-playbook.md`: thêm dòng cho yêu cầu chất lượng thiếu ngưỡng.

## Giới hạn

- 4 tình huống, 1 lần chạy mỗi tình huống, người chấm là phiên chính: kết quả chỉ mang tính chỉ dẫn.
- Chưa có nhóm đối chứng (cùng tình huống với phiên bản trước 3.5.0), nên chưa chứng minh được mức cải thiện do nội dung mới.
- Chưa chạy lại sau điều chỉnh.
