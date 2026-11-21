# PHÂN LOẠI YÊU CẦU ĐẦU VÀO (INTAKE TRIAGE)

> **Mục đích:** Công sức tỉ lệ với việc được nhờ. Một câu hỏi nhanh không cần quy trình 6 bước; một dự án mới không được rút gọn thành một câu trả lời.
> **Khi nào:** Ngay lượt đầu tiên của mọi yêu cầu, trước mọi bước khác trong `SKILL.md`.
> **Quan hệ:** Chọn **lối** ở đây, chọn **Tier** ở `rigor-tiers.md`. Hai việc độc lập: một việc nhỏ (lối L2) vẫn có thể là Tier 3 nếu chạm tiền hoặc dữ liệu nhạy cảm.

---

## 1. Năm lối xử lý

| Lối | Nhận diện | Làm gì | Hard Gate | Đầu ra |
|---|---|---|---|---|
| **L0 — Hỏi đáp** | Hỏi khái niệm, kỹ thuật, cách làm ("INVEST là gì", "khi nào dùng BPMN") | Trả lời thẳng, dẫn nguồn trong `references/ba-knowledge-base.md` khi cần | Không áp dụng | Câu trả lời |
| **L1 — Review một artifact** | Dán hoặc trỏ tới một tài liệu, story, AC, sơ đồ và nhờ góp ý | Rà theo checklist của loại tài liệu đó (`document-rulebook.md`, `requirement-quality-rubric.md`); review vai trò theo Tier nếu user muốn bản review chính thức | Không áp dụng; không đòi BPMN hay BRD | Bảng phát hiện: vị trí, vấn đề, mức (BLOCK/FIX/ASK/NOTE), đề xuất |
| **L2 — Viết/sửa một artifact lẻ** | "Viết AC cho story này", "vẽ sequence cho luồng thanh toán", "viết lại BR này" | Viết từ ngữ cảnh user cung cấp. Thiếu rule, ngưỡng, actor thì ghi `[CẦN XÁC NHẬN]` hoặc `[Giả định]` kèm căn cứ, không dừng lại hỏi hết trước khi viết | Gate được thay bằng **kiểm tra đầu vào**: liệt kê thông tin còn thiếu ở cuối; phần dựa trên giả định gắn `[DỰ THẢO, CHƯA DUYỆT]` | Artifact + danh sách câu hỏi mở |
| **L3 — Change Request** | Sửa hệ thống hoặc bộ tài liệu đang có | Delta protocol (`SKILL.md` Bước 1 mục 3, `impact-analysis-guide.md`): chỉ phân tích phần thay đổi, tác động ngược, dữ liệu lịch sử | Gate áp dụng cho phần thay đổi, không bắt viết lại phần không đổi | Brief thay đổi, tài liệu cập nhật, Change Log |
| **L4 — Dự án/epic mới** | Bắt đầu sản phẩm, dự án, epic, hoặc nhờ "làm bộ tài liệu" | Quy trình 6 bước đầy đủ; chọn lối đầy đủ, Agile Lite, hoặc chốt theo lát cắt (`slice-baselining.md`) | Đủ Hard Gate | Bộ tài liệu theo checkpoint |

---

## 2. Quy tắc phân loại

1. **Nói lối đã chọn bằng một dòng** ở đầu câu trả lời, ví dụ: "Xử lý theo lối L2 (viết một artifact lẻ), Tier 2 vì có hạn mức tiền." User có thể đổi lối.
2. **Không hỏi trước khi làm ở L0–L2** trừ khi thiếu thông tin khiến không thể viết được gì có ích. Viết bản tốt nhất với dữ kiện đang có, rồi hỏi phần còn thiếu.
3. **Nâng lối khi có tín hiệu.** Đang ở L2 mà phát hiện story kéo theo business rule mới về tiền, quyền hoặc dữ liệu nhạy cảm, hoặc story mâu thuẫn với tài liệu đã duyệt → nói rõ, đề xuất chuyển L3 hoặc L4, nhưng vẫn giao bản nháp của việc được nhờ.
4. **Không hạ lối để né quy trình.** User nhờ "viết nhanh BRD cho dự án mới" là L4. Có thể đi Agile Lite nếu điều kiện cho phép, không coi là L2.
5. **Những điều không nới ở lối nào:** không bịa số liệu; tách Fact / Giả định / Câu hỏi mở; gắn `[AI-Drafted]` cho tài liệu AI soạn; không kết luận pháp lý (`rigor-tiers.md` mục 3).

---

## 3. Mức kiểm tra theo lối

| Lối | Kiểm tra tối thiểu trước khi trả lời |
|---|---|
| L0 | Đúng kiến thức; dẫn nguồn khi khẳng định chuẩn hoặc số liệu |
| L1 | Mỗi phát hiện có vị trí và lý do; phân biệt lỗi chắc chắn với câu hỏi |
| L2 | Checklist Anti-AI; AC có "Then" quan sát được; ID theo scheme của tài liệu gốc |
| L3 | Như L2 cho phần thay đổi + `traceability_scan.py` trên bộ tài liệu sau khi sửa |
| L4 | Mức kiểm tra theo Tier (`rigor-tiers.md` mục 2, dòng "Kiểm tra sau mỗi tài liệu") |

---

## 4. Ví dụ

| Yêu cầu | Lối | Lý do |
|---|---|---|
| "AC Given-When-Then khác gì checklist?" | L0 | Hỏi kiến thức |
| "Review giúp 5 user story này" | L1 | Một nhóm artifact có sẵn |
| "Viết AC cho story đổi mật khẩu, khóa sau 5 lần sai" | L2 | Một artifact; rule chính đã có |
| "Viết AC cho story hoàn tiền" (chưa có hạn mức, chưa rõ ai duyệt) | L2, Tier 3 | Viết các kịch bản dự kiến gắn `[DỰ THẢO, CHƯA DUYỆT]`; nêu câu hỏi về hạn mức và người duyệt; đề xuất L3/L4 nếu hoàn tiền là luồng mới |
| "Thêm thanh toán trả góp vào app đang chạy" | L3 | Thay đổi hệ thống có sẵn |
| "Làm BRD, SRS cho hệ thống quản lý tài sản bệnh viện" | L4 | Dự án mới |
