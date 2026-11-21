# QUY CHUẨN TỪNG LOẠI TÀI LIỆU: ĐỘC GIẢ, NGÔN NGỮ, CẤU TRÚC

> **Nguồn gốc:** Tách từ `SKILL.md` để skill chính chỉ giữ phần điều phối. Đọc file này khi bắt đầu viết một loại tài liệu cụ thể.
> **Quy tắc cốt lõi:** Biết mình đang viết cho ai đọc. Mỗi tài liệu có độc giả riêng; giọng điệu và từ vựng phải đổi theo độc giả.

---

## 1. Ma trận độc giả và ngôn ngữ

| Loại tài liệu | Độc giả mục tiêu | Phong cách ngôn ngữ | Điều cấm | Ví dụ |
|---|---|---|---|---|
| **BRD** | Khách hàng, Sponsor, Business Owner, Ban Giám đốc, End-User | Ngôn ngữ nghiệp vụ và người dùng cuối. Giải thích *Cái gì* và *Tại sao*, tập trung vào giá trị kinh doanh và quy trình. Có **Glossary** nếu có từ chuyên ngành. | Thuật ngữ kỹ thuật (API, SQL, bảng database, endpoint, JSON payload, class, kiến trúc server, code). | ❌ "Hệ thống gọi API GET /customers để truy vấn bảng customer."<br>✅ "Hệ thống hiển thị hồ sơ khách hàng ngay khi đăng nhập thành công." |
| **SRS** | Tech Lead, Developer, QA/QC, Architect, DevOps | Ngôn ngữ kỹ thuật chính xác. Giải thích *Như thế nào*: logic, validation, kiểu dữ liệu, API contract, mã lỗi, state machine, bảo mật, NFR đo được. | Từ định tính, cảm tính ("nhanh", "dễ dùng", "tiện lợi"). Mọi yêu cầu phải test được. | ❌ "Tìm kiếm thật nhanh."<br>✅ "Phản hồi tìm kiếm < 300 ms với 100.000 bản ghi; hỗ trợ tìm kiếm mờ." |
| **Product Vision / Vision & Scope** | Founder, Ban Giám đốc, Nhà đầu tư | Ngôn ngữ chiến lược: bài toán thị trường, nỗi đau khách hàng, đề xuất giá trị, định vị, chỉ số thành công (MRR, CAC, LTV, Retention). | Chi tiết server, màn hình, giải thuật. | "Giảm 40% thời gian chờ của bệnh nhân tại phòng khám đa khoa nhờ đặt lịch khám trực tuyến." |
| **BPMN** | Business Stakeholder và đội kỹ thuật | Tên Task dạng **[Động từ] + [Danh từ]**; nhãn Gateway là câu hỏi điều kiện rõ (Có/Không, Đạt/Không đạt). | Tên Task kiểu code: "Execute function", "Call service", "Set state". | ❌ "Call notification service"<br>✅ "Gửi email thông báo phê duyệt" |
| **User Story & AC** | Product Owner, Scrum Team, Dev, Tester | Story: "Là [ai], tôi muốn [làm gì], để [giá trị gì]". AC: Given–When–Then, bao phủ quy tắc và rủi ro thực tế; số kịch bản theo Tier (`rigor-tiers.md`). | Kiến trúc code hoặc câu lệnh kỹ thuật trong Story. | ❌ "Là dev tôi muốn tạo bảng SQL users."<br>✅ "Là nhân viên bán hàng, tôi muốn xem lịch sử mua của khách, để tư vấn sản phẩm phù hợp." |
| **Data Model & Data Dictionary** | Database Architect, Backend Dev, Data Engineer | Tên bảng/trường theo `snake_case`. Data Dictionary **7 cột**: Tên trường, Kiểu dữ liệu, Null/Required, Default, Validation Rule, Mô tả, Độ nhạy cảm. | Mô tả chung chung, không có kiểu dữ liệu hoặc ràng buộc toàn vẹn. | Cột: `Field Name`, `Data Type`, `Null/Required`, `Default`, `Validation Rule`, `Description`, `Sensitivity`. |
| **UAT Plan & kịch bản test** | Người nghiệm thu, End-User kiểm thử, QA, PO | Kịch bản thao tác thực tế: từng bước bấm, nhập, kết quả hiển thị trên màn hình. | Bước kiểm tra log server, truy vấn DB bằng terminal. | ❌ "Query DB kiểm tra cờ status = 1"<br>✅ "Màn hình hiển thị thông báo màu xanh: 'Thanh toán thành công'." |

---

## 2. Stakeholder Map

**3 nhóm stakeholder bắt buộc phân loại:**

1. *Customers (Khách hàng và tài trợ):* Sponsor (cấp ngân sách, quan tâm ROI/chiến lược), Product Champion (thúc đẩy triển khai nội bộ).
2. *Users (Người dùng):* Direct User (thao tác hằng ngày), Indirect User (nhận báo cáo, xem số liệu, kiểm toán nội bộ).
3. *Others (Bên ngoại vi):* Advisor/SME (pháp lý, thuế, an ninh dữ liệu), Provider/Tech Partner (hạ tầng, cổng thanh toán, vận chuyển bên thứ 3).

**3 câu hỏi chống bỏ sót:**

- Ai ảnh hưởng hoặc chịu ảnh hưởng trực tiếp/gián tiếp bởi hệ thống?
- Hệ thống hoặc đối tượng bên ngoài nào gửi/nhận dữ liệu với sản phẩm?
- Ai nắm tri thức nghiệp vụ đặc thù mà tài liệu chưa ghi nhận?

**Bảng đầy đủ 7 cột (lối đầy đủ):**

`| Stakeholder | Phân nhóm (Customers/Users/Others) | Vai trò trong quy trình | Ảnh hưởng (H/M/L) | Quan tâm (H/M/L) | Nhu cầu / kỳ vọng chính | Kênh liên lạc phù hợp |`

**Bảng rút gọn 3 cột (lối Agile Lite hoặc khi user muốn bỏ bước):** `| Stakeholder | Vai trò | Nhu cầu chính |`

**Phân loại Power-Interest 2x2:**

| | Quan tâm cao | Quan tâm thấp |
|---|---|---|
| **Ảnh hưởng cao** | Quản lý chặt chẽ (Manage Closely) | Giữ hài lòng (Keep Satisfied) |
| **Ảnh hưởng thấp** | Cập nhật thông tin (Keep Informed) | Theo dõi tối thiểu (Monitor) |

Ghi rủi ro cụ thể nếu bỏ sót một bên liên quan gián tiếp.

---

## 3. BPMN (As-Is / To-Be)

- Dùng đúng BPMN 2.0: Pool, Lane, Start/End Event, Task, Gateway (Exclusive `X`, Parallel `+`, Inclusive `O`), Sequence Flow, Message Flow. Chuẩn chi tiết: `templates/bpmn-modeling-standard.md`.
- **Lane = Stakeholder:** mỗi Lane khớp một Stakeholder trong Stakeholder Map.
- **Nhánh chưa rõ:** gắn `[CẦN XÁC NHẬN]` trực tiếp trên Gateway; không tự đặt điều kiện rẽ nhánh.
- Mỗi Gateway có ít nhất một Business Rule (`BR-*`) viết thành văn bản.
- Sơ đồ Mermaid tuân thủ `so_do.md` (Start/End, mọi nhánh có đường đi, có Exception Flow, không phần tử lơ lửng).

---

## 4. Đặc tả tính năng AI và dữ liệu quan hệ

- Tính năng AI dùng `templates/ai-feature-spec.md`: độ chính xác mục tiêu, ngưỡng confidence, fallback khi model sai, human-in-the-loop, dữ liệu huấn luyện và giám sát drift.
- Khi thiết kế gợi ý, tìm kiếm ngữ nghĩa hoặc phát hiện gian lận: mô tả Thực thể (Node), Quan hệ (Edge) và Thuộc tính (Property); ghi rõ khi nào dùng Vector DB thuần, khi nào cần kết hợp Knowledge Graph.

---

## 5. Giao diện trong SRS

- Ghi rõ cấp độ trực quan: Sketch → Wireframe → Mockup → Prototype.
- Mô tả trạng thái trường dữ liệu: Default, Active, Error, Disabled, Empty State.
- Danh mục màn hình theo `screen-inventory-guide.md`; mỗi Feature có ít nhất một màn hình.
