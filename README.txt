================================================================================
                BA KIT v3.0 — SIÊU NĂNG LỰC & THƯ VIỆN PROMPT
================================================================================

Chào bạn! Đây là từ điển Prompt dành riêng cho 11 kỹ năng lõi của @ba-specialist trong hệ thống Layered OS v3.0. Đầu vào càng rõ ràng, AI làm càng chính xác.

Công thức chung: "@ba-specialist + [Hành động] + [Đối tượng] + [Ràng buộc]"

--------------------------------------------------------------------------------
1. CỔNG KHAI THÁC & CHUẨN ĐOÁN (Elicitation & Risk)
--------------------------------------------------------------------------------
Khi bắt đầu dự án, khoan hãy viết requirement. Khai thác nội dung và rủi ro trước:

🧠 Phỏng vấn KH (Skill: Customer Intelligence):
👉 "@ba-specialist, tạo 10 câu hỏi phỏng vấn để tìm nhu cầu ẩn cho tính năng [Tên tính năng]. Tập trung vào góc nhìn của [Vai trò user]."
👉 "@ba-specialist, phân tích đoạn hội thoại sau với khách hàng và tạo Insight Cards (Pain points, Hidden needs, Constraints): [Dán nội dung hội thoại]"

📉 Quản trị Rủi ro (Skill: Risk Management):
👉 "@ba-specialist, tạo Risk Register cho dự án này dựa trên file BRD. Áp dụng các quy tắc tự động phát hiện mẫu rủi ro tiềm ẩn (Scope, Tech, Timeline)!"
👉 "@ba-specialist, phân tích What-If: Nếu hệ thống đối tác delay API 2 tuần thì ảnh hưởng đến luồng nào trong dự án?"

--------------------------------------------------------------------------------
2. PHÂN TÍCH QUY TRÌNH & GIAO DIỆN (As-Is & Screen Inventory)
--------------------------------------------------------------------------------
Xóa bỏ sự mù mờ trước khi viết spec kỹ thuật.

🏭 Vẽ As-Is Process (Skill: As-Is Documentation):
👉 "@ba-specialist, viết tài liệu As-Is cho quy trình [Tên quy trình]. Xác định pain points, tạo Gap Analysis và thiết lập baseline metrics."

📱 Lên danh sách Màn hình (Skill: Screen Inventory & AI Prototyping):
👉 "@ba-specialist, liệt kê Screen Inventory cho Feature [Fxx]. Xác định rõ mục đích, actor và loại màn hình theo chuẩn hệ thống!"
👉 "@ba-specialist, tạo wireframe (hoặc sơ đồ UI mockup) cho màn hình [Tên màn hình]. Chỉ ra layout, dữ liệu chính và nút action."

--------------------------------------------------------------------------------
3. VẼ SƠ ĐỒ TỰ ĐỘNG (Auto-Diagram Engine)
--------------------------------------------------------------------------------
Bot tự động nhận diện ý định và chọn đúng loại sơ đồ (Context, ERD, Sequence, BPMN...)

📊 Prompt Vẽ chung:
👉 "@ba-specialist, vẽ sơ đồ cho quy trình sau: [Dán quy trình / nghiệp vụ / mô tả văn bản]"

📊 Prompt Vẽ chỉ định:
👉 "Vẽ Sequence Diagram cho luồng thanh toán qua VNPay."
👉 "Vẽ ERD thể hiện mối quan hệ giữa User, Role, và Permission."
👉 "Vẽ State Diagram cho vòng đời của một Đơn hàng."

--------------------------------------------------------------------------------
4. KIỂM ĐỊNH TÀI LIỆU & LOGIC (C-S-K-A & Stakeholder Sim)
--------------------------------------------------------------------------------
Luôn kiểm tra tài liệu sau khi tạo để đạt trạng thái "Right First Time".

✅ Inline Audit (Skill: Document Evaluation):
👉 "@ba-specialist, tiến hành chấm điểm C-S-K-A cho file [Tên file]. Chỉ ra các lỗi Critical cần ưu tiên sửa ngay."
👉 "@ba-specialist, tôi vừa viết xong phần [X], chạy inline audit cho nó và báo lỗi ngay nếu có."

🎭 Đóng vai phản biện (Skill: Persona Simulation):
👉 "@ba-specialist, đóng vai CFO khó tính để phản biện các yêu cầu non-functional trong tài liệu này (đặc biệt về chi phí server và logic thanh toán)."

--------------------------------------------------------------------------------
5. TRUY VẾT & KẾT NỐI (Traceability & Impact Analysis)
--------------------------------------------------------------------------------
Đảm bảo luồng đi từ Yêu cầu Khách hàng xuống tới bản Code không bị đứt.

⛓️ Scan rớt Requirement (Skill: Traceability Validator):
👉 "@ba-specialist, chạy Traceability Validator cho toàn bộ tài liệu hiện tại (BRQ → FR → US → TC). Hãy list ra các User Story chưa có Test Case."

🌪️ Phân tích rủi ro đổi yêu cầu (Skill: Impact Analysis):
👉 "@ba-specialist, KH muốn đổi [Yêu cầu A] thành [Yêu cầu B]. Khởi động dò quét cross-file xem ảnh hưởng đến những file nào?"

🔍 Đối soát với Code thực tế của Dev (Skill: Requirement-to-Code Audit):
👉 "@ba-specialist, khởi chạy đối soát yêu cầu vs mã nguồn. Kiểm tra tính năng [Tên tính năng] trong SRS đã được code đúng Logic Acceptance Criteria chưa?"

--------------------------------------------------------------------------------
6. LỆNH AUTO ROOT (Ba-Workflow)
--------------------------------------------------------------------------------
Nếu bạn lười gõ từng lệnh, hãy chạy toàn bộ chuỗi dây chuyền:
👉 `/ba-workflow [Tên dự án] [Mô tả ngắn gọn mục tiêu]`

================================================================================
MẸO: AI làm việc theo "ngữ cảnh". 
Luôn đảm bảo bạn đang mở các file cần thiết trong Editor trước khi ra lệnh!
================================================================================