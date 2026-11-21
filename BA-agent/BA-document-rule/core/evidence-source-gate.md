# NGUỒN YÊU CẦU VÀ GATE BẰNG CHỨNG (SOURCE REGISTER)

> **Vấn đề cần chặn:** Người chat với AI thường là BA, PM hoặc trưởng nhóm, không phải Sponsor, người dùng cuối hay bên vận hành. Nếu mọi câu trả lời của user được ghi thẳng thành sự thật, BRD trông đầy đủ nhưng đứng trên một nguồn gián tiếp duy nhất. Đây là nguyên nhân phổ biến khiến dự án thật phải làm lại.
> **Quan hệ:** Mức bằng chứng E1–E4 định nghĩa ở `strategy-analysis-guide.md` mục 2. File này thêm **nguồn** (ai nói, vai trò gì, trực tiếp hay gián tiếp) và **gate** trước khi chốt.

---

## 1. Hai trục đánh giá một nhận định

| Trục | Câu hỏi | Giá trị |
|---|---|---|
| **Mức bằng chứng** | Bằng chứng mạnh tới đâu? | E1 một người nói · E2 nhiều người nói giống nhau · E3 quan sát hoặc mẫu nhỏ · E4 dữ liệu hệ thống hoặc đo đủ lớn |
| **Loại nguồn** | Người nói có phải người nắm thông tin không? | **Trực tiếp:** người sở hữu tri thức hoặc quyết định đó (Trưởng khoa nói về quy trình khoa, Kế toán trưởng nói về quy tắc hạch toán), hoặc dữ liệu E3/E4 · **Gián tiếp:** người truyền đạt lại (BA, PM, user trong cuộc chat thuật lại lời khách hàng) |

Một nhận định có thể là E2 nhưng gián tiếp ("PM nói các khoa đều phàn nàn") hoặc E1 nhưng trực tiếp ("Giám đốc vận hành xác nhận hạn mức duyệt là 50 triệu"). Với quyết định và quy tắc, nguồn trực tiếp quan trọng hơn số người nói.

---

## 2. Sổ nguồn (Source Register)

Đặt ở BRD (Tier 2 trở lên) hoặc cuối Mini-Brief (Tier 1, có thể gộp thành một cột "Nguồn" trong bảng Fact).

| Mã nguồn | Loại | Người / đơn vị | Vai trò stakeholder | Trực tiếp / Gián tiếp | Ngày | Ghi chú |
|---|---|---|---|---|---|---|
| SRC-01 | Workshop | Phòng Vật tư (3 người) | Direct User, chủ quy trình | Trực tiếp | 20/02/2026 | Biên bản `10-Meeting-Minutes.md` |
| SRC-02 | Dữ liệu hệ thống | File Excel kiểm kê 6 tháng | — | Trực tiếp (E4) | 22/02/2026 | Đếm chênh lệch theo khoa |
| SRC-CHAT | Trao đổi với AI | [Tên/vai trò người chat] | [Vai trò của họ trong dự án] | Gián tiếp, trừ khi họ là người sở hữu thông tin đó | [Ngày] | Ghi rõ "thuật lại từ ai" nếu biết |

Loại nguồn thường gặp: phỏng vấn, workshop, quan sát, khảo sát, tài liệu hiện có (quy chế, hợp đồng, spec cũ), dữ liệu hệ thống, trao đổi trong cuộc chat.

**Mỗi Fact trong BRD/SRS ghi `Nguồn: SRC-xx · E1–E4`.** Ví dụ: "Mỗi đợt kiểm kê tháng mất 5 ngày công của Phòng Vật tư (SRC-01 · E2)."

---

## 3. Nhận định trọng yếu

Một nhận định là **trọng yếu** khi sai thì phải làm lại phạm vi, tiền hoặc kiểm thử. Cụ thể:

1. Quy tắc nghiệp vụ quyết định nhánh rẽ (BR gắn với Gateway), hạn mức, ngưỡng, quyền phê duyệt.
2. Phạm vi In/Out và mục tiêu kinh doanh.
3. Baseline và chỉ tiêu KPI.
4. Nghĩa vụ pháp lý, hợp đồng, bảo mật, dữ liệu cá nhân.
5. Tích hợp với hệ thống hoặc đối tác bên ngoài (ai sở hữu, giao thức, SLA).

---

## 4. Gate nguồn bằng chứng (Hard Gate 7)

**Không ghi một tài liệu hoặc một lát cắt là "đã chốt" khi còn nhận định trọng yếu chỉ có nguồn gián tiếp.**

- Nhận định trọng yếu cần ít nhất **một nguồn trực tiếp**. Baseline KPI và con số dùng cho Business Case cần thêm mức **E3 trở lên** (`strategy-analysis-guide.md`).
- Chưa có nguồn trực tiếp thì nhận định nằm ở **Câu hỏi mở**, kèm người cần xác nhận và hạn. Có thể giữ giá trị khởi điểm gắn `[Giả định]` để các bên phản hồi, nhưng không ghi thành yêu cầu đã duyệt.
- Không chặn việc **viết nháp**. Gate chặn việc **chốt**.
- Tier 1: gate áp dụng cho nhóm 1–2 ở mục 3; Tier 2–3: áp dụng cho cả 5 nhóm.
- **Tier 2–3: lời khai trong chat chưa đủ để chốt.** Nhận định trọng yếu mà nguồn trực tiếp duy nhất là `SRC-CHAT` cần bản xác nhận lưu được (biên bản, email, tin nhắn có lưu), ghi ở cột Ghi chú của Sổ nguồn dạng `XN: <loại> <ngày> của <ai>`. Trong chat, AI không xác minh được người nói là ai (`human-accountability.md`, H2).

---

## 5. Kế hoạch elicitation

Lập ở Bước 1 khi xử lý lối L4 (bắt buộc từ Tier 2; Tier 1 viết 2–3 dòng):

| Stakeholder | Cần xác nhận gì (nhận định trọng yếu) | Kỹ thuật | Khi nào | Ai phụ trách | Trạng thái |
|---|---|---|---|---|---|
| Giám đốc vận hành | Hạn mức duyệt điều chuyển tài sản (BR-002) | Phỏng vấn 30 phút | Tuần 1 | BA Lead | Chưa |
| Kế toán | Quy tắc ghi nhận thanh lý | Đọc quy chế + phỏng vấn | Tuần 1 | BA | Chưa |

Chọn kỹ thuật theo `references/elicitation-playbook.md`. AI không thay buổi làm việc với người thật; AI chuẩn bị câu hỏi, giả thuyết và biên bản mẫu.

---

## 6. Cách AI áp dụng trong cuộc chat

1. Thông tin user cung cấp được ghi nguồn `SRC-CHAT`. Hỏi một lần: "Thông tin về [quy tắc X] anh/chị nắm trực tiếp hay được [ai] truyền đạt lại?" Nếu user chính là người sở hữu thông tin đó, ghi trực tiếp.
2. Khi gặp nhận định trọng yếu chỉ có `SRC-CHAT` gián tiếp, không dừng việc viết; gắn `[CẦN XÁC NHẬN: <ai> — <hạn>]` và đưa vào Câu hỏi mở.
3. Trước checkpoint chốt, liệt kê bảng nhận định trọng yếu còn thiếu nguồn trực tiếp. Bảng rỗng mới được đề xuất "Duyệt".
4. Không tự nâng mức bằng chứng: hai câu user nói lại lời cùng một người vẫn là một nguồn.
