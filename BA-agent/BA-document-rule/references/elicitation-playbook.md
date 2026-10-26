# ELICITATION PLAYBOOK: Khơi gợi yêu cầu khi người đối diện không hợp tác lý tưởng

> **Bổ sung cho:** `elicitation-techniques.md` (chọn kỹ thuật). File này nói cách làm khi gặp tình huống thật.
> **BABOK KA:** Elicitation and Collaboration, các task Prepare, Conduct, Confirm.

---

## 1. Chuẩn bị: đi vào buổi họp với giả thuyết

Một buổi phỏng vấn không có giả thuyết dễ thành buổi nghe kể chuyện. Trước mỗi buổi, viết sẵn:

| Mục | Nội dung |
|---|---|
| Mục tiêu | Kết thúc buổi này tôi cần biết điều gì mà hiện tại chưa biết? |
| Giả thuyết | 3 điều tôi nghĩ là đúng và cần kiểm chứng |
| Tài liệu đã đọc | Quy trình, biểu mẫu, báo cáo cũ của người này |
| Vị thế người đối diện | Quyết định, thực hiện hay chịu ảnh hưởng? Lợi ích của họ là gì, họ mất gì nếu thay đổi? |
| Câu hỏi bắt buộc | Tối đa 5, xếp theo độ quan trọng; nếu hết giờ thì hỏi đủ 5 câu này |
| Bằng chứng cần xin | Biểu mẫu thật, ảnh màn hình, file Excel đang dùng, 3 trường hợp gần nhất |

---

## 2. Mẫu câu hỏi

| Mục đích | Câu hỏi | Vì sao hiệu quả |
|---|---|---|
| Lấy quy trình thật | "Hãy kể tôi nghe lần gần nhất anh/chị xử lý việc này, từ lúc nhận đến lúc xong." | Chuyện cụ thể tránh được mô tả lý tưởng hóa |
| Tìm ngoại lệ | "Lần nào việc này không suôn sẻ? Chuyện gì xảy ra?" | Ngoại lệ là nơi phần lớn business rule nằm |
| Tìm workaround | "Có bước nào anh/chị làm khác với quy trình trên giấy không?" | Workaround là tín hiệu yêu cầu bị thiếu |
| Đo mức đau | "Việc này tốn bao lâu mỗi tuần? Nếu bỏ nó, chuyện gì xảy ra?" | Chuyển cảm giác thành số |
| Kiểm tra giải pháp áp đặt | "Nếu có cách khác không cần [giải pháp họ nêu], anh/chị cần đạt được gì?" | Tách nhu cầu khỏi giải pháp |
| Tìm tác động ngầm | "Ngoài anh/chị, còn ai bị ảnh hưởng nếu bước này đổi?" | Bổ sung stakeholder bị bỏ sót |
| Tìm người quyết | "Nếu hai phòng ban không đồng ý, ai là người chốt?" | Xác định quyền quyết định sớm |
| Kết thúc | "Tôi nên hỏi thêm ai? Có điều gì tôi chưa hỏi mà anh/chị thấy quan trọng?" | Mở thêm nguồn và điểm mù |

Tránh câu hỏi dẫn ("Chắc anh/chị cần báo cáo tự động đúng không?"). Tránh câu hỏi đóng khi chưa hiểu bối cảnh.

---

## 3. Tình huống khó và cách xử lý

| Tình huống | Dấu hiệu | Cách xử lý |
|---|---|---|
| Nêu giải pháp thay vì nhu cầu | "Cần tích hợp AI", "cần app" | Ghi lại như giả thuyết. Hỏi: "Việc gì đang không làm được mà anh/chị mong giải pháp này giải quyết?" Gắn cờ Solution Bias |
| "Cái gì cũng quan trọng" | Mọi yêu cầu đều Must | Đưa tình huống đánh đổi: "Nếu chỉ kịp làm một trong hai thứ này cho đợt 1, anh/chị chọn gì?" Dùng ngân sách giả (cho 100 điểm, chia vào các yêu cầu) |
| Người im lặng trong workshop | Gật đầu nhưng không nói | Hỏi riêng sau buổi; dùng ghi giấy kín (brainwriting) trước khi thảo luận |
| Người có chức vụ cao áp đảo | Mọi người chờ họ nói trước | Cho người cấp thấp nói trước; thu ý kiến bằng giấy; để người cao nói sau cùng |
| Lời nói khác việc làm | Nói quy trình A, thực tế làm B | Quan sát trực tiếp, xin mẫu dữ liệu thật; không phán xét, ghi cả hai và hỏi nguyên nhân |
| SME bận, hẹn không đến | Hủy lịch liên tục | Rút buổi còn 20 phút, gửi trước câu hỏi, gửi bản nháp quy trình để họ sửa thay vì kể; báo Sponsor nếu rủi ro lịch |
| Yêu cầu đổi liên tục | Mỗi tuần một hướng | Hỏi mục tiêu gốc; ghi log thay đổi; đưa vào `change-log.md`; hỏi ai chịu trách nhiệm chốt |
| Hai người mâu thuẫn | Mỗi người nói điều ngược | Không chọn phe. Ghi thành xung đột (CON-xxx), xác định người quyết định theo `stakeholder-conflict-resolution.md` |
| Người không biết mình cần gì | "Anh làm giúp tôi cái nào tốt nhất" | Dùng prototype giấy hoặc kịch bản mẫu để họ phản ứng; hỏi "cái này gần hay xa với điều anh/chị nghĩ?" |
| Thông tin nhạy cảm, pháp lý | Dữ liệu trẻ em, sức khỏe, tài chính | Dừng, ghi nhận, hỏi đơn vị pháp chế hoặc bảo mật trước khi đặc tả; không tự quyết |
| Stakeholder chống thay đổi | "Cách cũ đang ổn" | Hỏi họ mất gì và được gì; đưa họ vào thiết kế quy trình mới; đo hiệu quả bằng dữ liệu của chính họ |

---

## 4. Sau buổi họp: biến ghi chú thành tri thức kiểm chứng được

Trong 24 giờ, gửi lại bản **play-back** cho người tham dự:

1. Những gì tôi hiểu (tối đa 10 gạch đầu dòng, mỗi dòng một nhận định).
2. Những gì tôi chưa chắc (đánh dấu `[CẦN XÁC NHẬN]`).
3. Quyết định đã chốt và người chốt.
4. Việc cần làm: ai, việc gì, hạn.

Mỗi nhận định đưa vào BRD/SRS ghi mức bằng chứng (E1–E4, xem `strategy-analysis-guide.md` mục 2) và nguồn (biên bản, ngày). Nhận định chỉ ở E1 không được ghi thành yêu cầu đã duyệt.

---

## 5. Điều hành workshop: kịch bản 3 giờ cho một quy trình

| Phút | Hoạt động | Quy tắc điều hành |
|---|---|---|
| 0–10 | Mở: mục tiêu, kết quả cần có, quy tắc | Nói rõ ai là người quyết định; không bàn giải pháp trong 60 phút đầu |
| 10–50 | Dựng As-Is trên tường | Người trực tiếp làm việc đó nói; quản lý ngồi nghe |
| 50–80 | Đánh dấu điểm đau và ngoại lệ | Mỗi người dán điểm đau riêng; gom nhóm; đếm tần suất |
| 80–90 | Nghỉ | Dùng để nói riêng với người im lặng |
| 90–130 | To-Be: ý tưởng | Brainwriting trước, thảo luận sau; mỗi ý có người nêu và lợi ích |
| 130–160 | Ưu tiên | Bỏ phiếu chấm (dot voting) hoặc ngân sách giả, hiển thị kết quả công khai |
| 160–180 | Chốt | Đọc lại quyết định, việc cần làm, `[CẦN XÁC NHẬN]` còn lại; hẹn ngày gửi biên bản |

Người điều hành (BA) không đồng thời ghi chép. Có thư ký riêng hoặc ghi âm với sự đồng ý.

---

## 6. Ngân hàng câu hỏi theo ngành (bắt đầu, không thay thế phỏng vấn)

### Giáo dục, trường học
- Ai xác nhận học sinh có mặt, bằng cách nào, mất bao lâu mỗi lớp?
- Khi phụ huynh gọi hỏi, người nhận máy là ai, hỏi nhiều nhất về chuyện gì?
- Dữ liệu học sinh nằm ở đâu hiện nay, ai là người cập nhật, tần suất ra sao?
- Dữ liệu nào liên quan đến trẻ em cần phụ huynh đồng ý bằng văn bản?
- Nếu hệ thống mất mạng trong giờ điểm danh, nhà trường làm gì?

### Fintech, thanh toán
- Giao dịch có những trạng thái nào, trạng thái nào là cuối cùng và không đảo ngược?
- Khi hai bên đối soát lệch, ai chịu trách nhiệm và xử lý trong bao lâu?
- Quy định nào yêu cầu giữ log, giữ bao lâu, ai được xem?
- Khi gửi giao dịch lần hai do timeout, hệ thống phân biệt trùng và mới bằng gì?

### Y tế
- Ai được xem hồ sơ bệnh án, trong trường hợp khẩn cấp có ngoại lệ không?
- Dữ liệu nào đến từ thiết bị hoặc hệ thống bên ngoài (HIS, LIS, PACS)?
- Sai sót ở bước này ảnh hưởng an toàn người bệnh thế nào, ai kiểm tra lại?

### Thương mại điện tử, bán lẻ
- Đơn hàng bị hủy, trả, đổi ở giai đoạn nào thì phải hoàn tiền, ai quyết?
- Khuyến mãi chồng nhau xử lý thứ tự nào?
- Tồn kho lệch giữa kênh xử lý ra sao khi hai người cùng mua món cuối?

### Nội bộ doanh nghiệp (HR, tài chính, vận hành)
- Quy trình phê duyệt hiện có bao nhiêu cấp, cấp nào thực sự đọc nội dung?
- Báo cáo nào được làm hằng tháng nhưng không ai dùng?
- Ai bị tăng việc khi quy trình mới đưa vào, họ có được lợi gì?

---

## 7. Checklist

```
☐ Đã viết mục tiêu, giả thuyết, 5 câu hỏi bắt buộc trước buổi họp
☐ Đã xin ví dụ thật và tài liệu thật, không chỉ lời kể
☐ Đã hỏi ngoại lệ, workaround và tác động đến người khác
☐ Đã gửi play-back trong 24 giờ, có phần [CẦN XÁC NHẬN]
☐ Mỗi nhận định đưa vào yêu cầu có mức bằng chứng và nguồn
☐ Xung đột đã ghi vào Conflict Log, không tự chọn phe
☐ Vấn đề pháp lý, dữ liệu nhạy cảm đã chuyển cho bộ phận phụ trách
```
