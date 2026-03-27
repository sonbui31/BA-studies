================================================================================
                BA KIT 2.6.1 — HƯỚNG DẪN SỬ DỤNG NHANH (QUICK START)
================================================================================

Chào bạn! Đây là bộ Kit BA 2.6.1 — AI-Orchestrated với 8 Kỹ năng Hạng nặng.

--------------------------------------------------------------------------------
BƯỚC 1: KHỞI TẠO DỰ ÁN (Dùng Workflow tự động)
--------------------------------------------------------------------------------
Gõ lệnh sau vào ô chat:
👉  /ba-workflow [Tên dự án] [Yêu cầu ngắn gọn]

Hệ thống sẽ tự động:
1. Predictive Scan: Cảnh báo rủi ro bùng nổ dự án (Scope Creep).
2. Customer Intelligence: Khai thác thông tin & insight sâu từ KH.
3. Auto-Diagram: Vẽ sơ đồ tự động từ dữ liệu thô bạn cung cấp.
4. Drafting: Viết BRD, SRS, User Stories theo chuẩn Layered OS.
5. Traceability: Đối soát xem Code có làm đúng theo Tài liệu không.

--------------------------------------------------------------------------------
BƯỚC 2: SỬ DỤNG "SIÊU NĂNG LỰC" BA (@ba-specialist)
--------------------------------------------------------------------------------
Khi cần giải quyết các đầu việc cụ thể, BẮT BUỘC gọi @ba-specialist:

🔍 Đối soát:  "@ba-specialist đối soát SRS này với folder code src/"
🧠 Moi tin:   "@ba-specialist phỏng vấn khách hàng về tính năng thanh toán"
🌪 Ảnh hưởng: "@ba-specialist nếu đổi logic X thì ảnh hưởng đến những file nào?"
📉 Rủi ro:    "@ba-specialist dự báo rủi ro trễ deadline cho dự án này"
🎭 Phản biện: "@ba-specialist đóng vai sếp khó tính để phản biện yêu cầu này"
📊 Sơ đồ:    "@ba-specialist vẽ [loại sơ đồ] cho [mô tả quy trình]"

--------------------------------------------------------------------------------
BƯỚC 3: THƯ VIỆN PROMPT MẪU (Dùng để Copy & Paste)
--------------------------------------------------------------------------------
Áp dụng công thức: [Bối cảnh] + [Nhiệm vụ] + [Chuẩn] + [Định dạng]

1. Khi bắt đầu dự án mới:
   "@ba-specialist, dự án App gọi xe. Viết Vision & Scope theo BACCM. Vẽ Context Diagram."

2. Khi cần sơ đồ quy trình (tự động nhận diện loại):
   "@ba-specialist, vẽ sơ đồ cho quy trình: [paste nội dung quy trình vào đây]"

3. Khi cần vẽ BPMN cụ thể:
   "@ba-specialist, vẽ BPMN cho quy trình: KH gửi yêu cầu → CSKH xem xét
   → nếu > 1 triệu thì Quản lý duyệt, nếu nhỏ hơn thì tự duyệt → Refund → Email."

4. Khi cần viết User Stories:
   "@ba-specialist, viết 5 User Stories module Admin. Chuẩn INVEST + Given-When-Then."

5. Khi cần check chất lượng:
   "@ba-specialist, chấm điểm C-S-K-A file 02-BRD.md và chỉ ra 3 điểm cần sửa."

6. Khi muốn moi thêm thông tin KH:
   "@ba-specialist, tạo 10 câu hỏi phỏng vấn để tìm nhu cầu ẩn cho tính năng kho."

--------------------------------------------------------------------------------
BƯỚC 4: QUẢN LÝ TÀI LIỆU (Thư mục BA-agent/)
--------------------------------------------------------------------------------
• Hướng dẫn chi tiết: [ BA-agent/USER-GUIDE.md ]
• Bản đồ file:        [ BA-agent/DOCUMENT-MAP.md ]
• Thư viện sơ đồ:     [ BA-agent/so_do.md ] (10 loại sơ đồ, 868 dòng mẫu)

--------------------------------------------------------------------------------
MẸO: Dùng đúng AI cho đúng việc
• Nghĩ sâu/Logic: OpenAI o4 | Viết/Vẽ đẹp: Claude 4.6 | Audit cả repo: Gemini 3
================================================================================