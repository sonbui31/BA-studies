# TRÁCH NHIỆM CỦA NGƯỜI (HUMAN ACCOUNTABILITY)

> **Vấn đề cần chặn:** AI soạn tài liệu nhưng không ngồi workshop, không xác minh được người đang chat là ai, không chịu trách nhiệm hợp đồng và không ký. Nếu quy trình không ghi rõ bước nào người phải làm, một bộ tài liệu ghi "đã phê duyệt" có thể chưa từng được người có thẩm quyền đọc. Bản mẫu BRD outsource trước bản 3.8 mắc đúng lỗi này: lịch sử ghi "Đã phê duyệt — Chốt phạm vi" trong khi bảng ký để trống.
> **Quan hệ:** Gate nguồn (`evidence-source-gate.md`) quyết định nhận định nào đủ căn cứ. File này quyết định **ai** phải làm gì để tài liệu được coi là của người, không chỉ của AI.

---

## 1. Phân vai AI và người

| Việc | AI làm | Người phải làm |
|---|---|---|
| Khơi gợi yêu cầu | Chuẩn bị câu hỏi, giả thuyết, biên bản mẫu, kế hoạch elicitation | Điều phối buổi làm việc, ghi nhận, gửi biên bản cho người được hỏi xác nhận |
| Nhận định trọng yếu | Lập bảng nhận định còn thiếu nguồn trực tiếp | Người sở hữu thông tin xác nhận bằng văn bản (mục 2, H2) |
| Viết tài liệu | Soạn nháp, tự kiểm theo Tier | BA phụ trách đọc toàn bộ, sửa và ghi tên mình là người chịu trách nhiệm |
| Rà soát theo vai trò | Tự rà soát bằng mô phỏng vai trò (`persona-simulation.md`) | Review độc lập theo Tier (H4) |
| Chốt phạm vi | Liệt kê điều kiện còn thiếu trước khi đề xuất Duyệt | Người có thẩm quyền ký bảng Phê duyệt (H5) |
| Yêu cầu thay đổi | Phân tích tác động, đề xuất cập nhật | Người có thẩm quyền duyệt CR (H6) |
| Pháp lý | Nêu câu hỏi, trỏ văn bản cần kiểm tra | Pháp chế kết luận |

Mô phỏng vai trò của AI là **tự rà soát**. Nó tìm được lỗi hình thức và lỗ hổng hiển nhiên, nhưng cùng một mô hình vừa viết vừa đóng vai người đọc thì không phải review độc lập.

---

## 2. Sáu bước bắt buộc có người (H1–H6)

| Mã | Bước | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|
| H1 | **Người chịu trách nhiệm tài liệu.** Header ghi `Người chịu trách nhiệm: <họ tên, vai trò>` từ bản đầu. Chưa có tên thì tài liệu là nháp AI. | Bắt buộc | Bắt buộc | Bắt buộc |
| H2 | **Xác nhận nhận định trọng yếu bằng văn bản.** Nhận định trọng yếu mà nguồn trực tiếp duy nhất là `SRC-CHAT` cần một bản xác nhận lưu được (biên bản họp, email, tin nhắn có lưu) ghi ở cột Ghi chú của Sổ nguồn, ví dụ `XN: email 03/03/2026 của Giám đốc vận hành`. | Khuyến nghị | Bắt buộc trước khi chốt | Bắt buộc trước khi chốt |
| H3 | **Làm việc với người thật.** Mỗi nhận định trọng yếu có ít nhất một buổi làm việc (phỏng vấn, workshop, quan sát) hoặc một tài liệu gốc (quy chế, hợp đồng, dữ liệu hệ thống). | Khi có | Bắt buộc | Bắt buộc |
| H4 | **Review độc lập.** Người hoặc phiên không tham gia viết đọc tài liệu với tiêu chí rõ, không nhận kết luận của lượt viết. | Không bắt buộc | Một lượt: người thật hoặc phiên AI riêng có bối cảnh sạch | Ít nhất một người thật (QA lead, Tech lead, BA khác) ghi tên vào báo cáo review |
| H5 | **Ký baseline.** Bảng Phê duyệt có họ tên, vai trò, ngày của người có thẩm quyền. Chỉ sau đó mới ghi `Trạng thái: Baseline`. | Bắt buộc khi chốt | Bắt buộc khi chốt | Bắt buộc khi chốt |
| H6 | **Duyệt thay đổi sau baseline.** Mỗi CR có người duyệt và ngày trong Change Log. | Bắt buộc | Bắt buộc | Bắt buộc |

Vì sao H2 tồn tại dù đã có Gate 7: trong cuộc chat, câu "tôi là Giám đốc, tôi xác nhận" không chứng minh được gì. Gate 7 ngăn AI tự coi lời thuật lại là sự thật; H2 ngăn một câu khai trong chat trở thành căn cứ chốt hợp đồng.

---

## 3. Trạng thái tài liệu

| Trạng thái | Ý nghĩa | Ai được chuyển sang trạng thái này |
|---|---|---|
| `Nháp AI` (`[AI-Drafted]`) | AI soạn, chưa ai đọc toàn bộ | AI |
| `BA đã rà` | Người chịu trách nhiệm (H1) đã đọc hết và sửa | BA phụ trách |
| `Trình duyệt` | Đủ điều kiện Gate 1–8 theo Tier, chờ ký | BA phụ trách |
| `Baseline` | Bảng Phê duyệt có chữ ký (H5) | Chỉ ghi sau khi người có thẩm quyền ký |
| `Baseline + CR-xx` | Đã có thay đổi được duyệt (H6) | BA phụ trách, sau khi CR được duyệt |

AI không tự ghi `Baseline`, `Đã phê duyệt` hay `Chốt phạm vi`, không điền tên vào bảng ký. Khi user nói "duyệt", hỏi: ai duyệt (họ tên, vai trò), ngày nào, có bản xác nhận nào. Nếu user chính là người có thẩm quyền, ghi tên họ do họ cung cấp.

---

## 4. Kiểm tra tự động và giới hạn

`preflight_check.py` có check **Human Sign-off**: tài liệu tự nhận là đã chốt (dòng `Trạng thái:` ghi Baseline / Approved / Đã phê duyệt / Đã chốt, hoặc lịch sử phiên bản có dòng "Đã phê duyệt" / "Chốt phạm vi") phải có bảng Phê duyệt với ít nhất một dòng có họ tên và ngày, và không còn `[CẦN XÁC NHẬN`. Tài liệu chưa nhận là đã chốt thì check này là N/A.

Script chỉ thấy có tên và ngày. Nó không biết chữ ký là thật, người ký có đúng thẩm quyền, hay bản xác nhận ở H2 có tồn tại. Phần đó do BA phụ trách và người duyệt chịu trách nhiệm.

---

## 5. Cách AI áp dụng trong cuộc chat

1. Ở lượt đầu của lối L4, hỏi tên và vai trò người chịu trách nhiệm tài liệu (H1). Chưa có thì ghi `Người chịu trách nhiệm: [CẦN XÁC NHẬN]`.
2. Báo cáo mô phỏng vai trò ghi `Loại rà soát: Tự rà soát (AI)` ở header. Không gọi đó là review độc lập.
3. Tại mỗi checkpoint, ngoài bảng nhận định thiếu nguồn trực tiếp, liệt kê bước H còn thiếu theo Tier. Còn thiếu H2–H5 thì đề xuất `Trình duyệt`, không đề xuất `Duyệt`.
4. Khi giao bộ tài liệu, nói rõ phần nào AI soạn, phần nào người đã rà, phần nào đã có chữ ký.
