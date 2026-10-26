# STRATEGY ANALYSIS GUIDE: Từ vấn đề đến khuyến nghị Go / No-Go

> **BABOK KA:** Strategy Analysis. Xem [babok-v3-framework.md](../../knowledge-source/babok-v3-framework.md) mục 2.4.
> **Dùng khi:** Sponsor hoặc PO đưa ra một giải pháp ("làm app", "mua hệ thống X", "thêm AI") và chưa ai chứng minh vấn đề đáng giải quyết, hoặc khi cần xin ngân sách.
> **Đầu ra:** Problem Statement có bằng chứng, hiện trạng và gap, tối thiểu 3 phương án (có Do Nothing), bảng so sánh có giả định, khuyến nghị kèm điều kiện dừng. Điền vào `templates/business-case.md`.

---

## 1. Nguyên tắc

Business Case của BA Senior trả lời được năm câu hỏi. Nếu thiếu một câu, tài liệu chưa đủ để xin quyết định.

1. Vấn đề này có thật không, bằng chứng ở mức nào?
2. Nếu không làm gì thì chuyện gì xảy ra, và mất bao nhiêu mỗi tháng chờ?
3. Có cách rẻ hơn giải quyết 70% vấn đề không?
4. Con số nào trong phương án được chọn đang là giả định, và nếu giả định sai thì kết luận có đổi không?
5. Ai quyết định, theo ngưỡng nào, và khi nào dừng?

---

## 2. Quy trình 6 bước

### Bước 1: Viết lại vấn đề, tách khỏi giải pháp

| Kiểm tra | Câu hỏi | Dấu hiệu đạt |
|---|---|---|
| Không chứa giải pháp | Câu mô tả có từ app, AI, hệ thống, nền tảng không? | Không có; chỉ có hành vi, chi phí, rủi ro |
| Có người chịu ảnh hưởng | Ai gặp vấn đề, tần suất bao nhiêu? | Có nhóm người và con số tần suất |
| Có hậu quả đo được | Mất thời gian, tiền, khách hay rủi ro nào? | Có đơn vị đo |
| Có baseline | Hiện tại đo thế nào? | Có số, hoặc ghi rõ "chưa có baseline, cần đo trong 2 tuần" |
| Có chủ sở hữu | Ai đau nhất khi vấn đề tiếp diễn? | Có tên vai trò, người này sẵn sàng cam kết nguồn lực |

Ví dụ viết lại: "Cần app cho phụ huynh" thành "Mỗi tuần văn phòng trường nhận khoảng X cuộc hỏi tình trạng điểm danh và đơn nghỉ, mỗi cuộc mất Y phút, phụ huynh không có cách tự tra cứu".

### Bước 2: Phân tích hiện trạng theo mức bằng chứng

Mỗi nhận định về hiện trạng gắn một mức bằng chứng. Business Case chỉ được đứng trên E3 và E4.

| Mức | Nguồn | Ví dụ | Giá trị |
|:-:|---|---|---|
| E1 | Một người nói | "Phụ huynh hay hỏi lắm" | Gợi ý, cần kiểm chứng |
| E2 | Nhiều người nói giống nhau | 5/6 giáo viên nói mất nhiều thời gian | Khá tin, chưa có số |
| E3 | Quan sát trực tiếp hoặc mẫu nhỏ | Đếm cuộc gọi trong 2 tuần | Dùng được cho Business Case |
| E4 | Dữ liệu hệ thống hoặc đo đủ lớn | Log tổng đài 12 tháng | Chắc nhất |

Khi chỉ có E1–E2, việc đầu tiên là thiết kế cách đo (đếm, ghi nhật ký, khảo sát), không phải viết giải pháp.

### Bước 3: Mô tả trạng thái tương lai bằng kết quả

Mỗi kết quả có metric, baseline, target, thời hạn và cách đo. Không viết "nâng cao trải nghiệm". Viết "giảm số cuộc hỏi tình trạng điểm danh từ X xuống Y mỗi tuần sau 2 tháng".

### Bước 4: Lập phương án, tối thiểu 3

| Loại | Vai trò |
|---|---|
| Do Nothing | Baseline để so. Tính chi phí chờ: vấn đề kéo dài một năm mất bao nhiêu |
| Phương án nhẹ không cần phát triển | Quy trình, biểu mẫu, công cụ có sẵn (Zalo OA, Google Form, báo cáo Excel). Thường giải quyết một phần lớn vấn đề |
| Phương án đầy đủ | Build, Buy hoặc Hybrid |

Nếu không có phương án nhẹ trong danh sách, BA chưa làm xong bước này. Sponsor thường chưa nghĩ đến nó.

### Bước 5: So sánh bằng số, kèm giả định và độ nhạy

- Mỗi con số ghi nguồn hoặc nhãn `[Giả định]`. Giả định nào làm kết luận đảo chiều thì đưa lên đầu bảng.
- Tính 3 năm (hoặc vòng đời thực tế), gồm chi phí vận hành, đào tạo, hỗ trợ, không chỉ chi phí xây.
- Tính điểm hòa vốn: phải đạt mức lợi ích nào để phương án đáng làm. Mức đó có đạt được không?
- Chạy độ nhạy: đổi giả định quan trọng nhất ±30%, kết luận có đổi không?
- Lợi ích tài chính và lợi ích khó quy đổi (an toàn, niềm tin, tuân thủ) trình bày riêng. Không ép mọi thứ ra tiền, cũng không bỏ qua chúng.

### Bước 6: Khuyến nghị kèm điều kiện

Khuyến nghị theo mẫu: *"Chọn phương án X vì Y. Điều kiện để tiếp tục: Z. Dừng hoặc đổi hướng nếu sau N tuần chỉ số W chưa đạt V."* Một phương án chỉ có "nên làm" mà không có điều kiện dừng là chưa hoàn chỉnh.

---

## 3. Ví dụ minh họa (số giả định, không phải dữ liệu của dự án nào)

Một trường 600 học sinh. Văn phòng trường nhận cuộc gọi và tin nhắn hỏi tình trạng điểm danh, đơn nghỉ, học phí.

**Giả định đo được (E3):** 150 cuộc/tuần, mỗi cuộc 4 phút, 40 tuần/năm, chi phí nhân sự 60.000 đ/giờ.

| Tính toán | Kết quả |
|---|---|
| Thời gian xử lý mỗi tuần | 150 × 4 = 600 phút = 10 giờ |
| Mỗi năm | 10 × 40 = 400 giờ |
| Chi phí nhân sự mỗi năm | 400 × 60.000 = 24.000.000 đ |

| Phương án | Chi phí 3 năm | Giảm cuộc hỏi (giả định) | Lợi ích thời gian 3 năm | Chênh lệch |
|---|---:|---:|---:|---:|
| A. Do Nothing | 0 | 0% | 0 | 0 |
| B. Zalo OA + Google Form (20 tr setup, 12 tr/năm) | 56 tr | 50% | 36 tr | −20 tr |
| C. Build app (400 tr, 60 tr/năm vận hành) | 580 tr | 70% | 50,4 tr | −529,6 tr |

**Đọc kết quả:**

- Chỉ tính tiết kiệm thời gian nhân sự, không phương án nào có lãi. B gần hòa vốn, C lỗ rất nặng.
- Để C hòa vốn trong 3 năm, lợi ích phải đạt 580 / 3 ≈ 193,3 tr/năm. Phần ngoài tiết kiệm thời gian là 193,3 − 16,8 = 176,5 tr/năm.
- Nếu phần đó đến từ việc giữ chân học sinh (học phí giả định 36 tr/năm), app phải giữ thêm khoảng 176,5 / 36 ≈ 4,9, tức 5 học sinh mỗi năm.
- Đây là một **giả thuyết có thể kiểm chứng**: "app giữ lại được ít nhất 5 học sinh/năm". Rất khó quy kết nhân quả, nên BA ghi rõ cách đo (khảo sát lý do rút học, so sánh tỷ lệ rút giữa lớp dùng và không dùng) hoặc chuyển sang lập luận khác: giá trị đến từ việc bán sản phẩm cho nhiều trường, khi đó phải làm Business Case theo góc nhìn sản phẩm (xem `overlays/product`).

**Khuyến nghị mẫu:** Chạy phương án B trong 8 tuần để đo thật tỷ lệ phụ huynh dùng và mức giảm cuộc hỏi. Chỉ bàn phương án C nếu phụ huynh dùng B ≥ 60% hằng tuần và có bằng chứng cho giả thuyết giữ chân. Dừng B nếu < 30% phụ huynh dùng sau 8 tuần.

Điểm Senior của ví dụ: BA không "bênh" giải pháp đã được yêu cầu. BA chỉ ra điều kiện để nó đáng làm và đề xuất cách kiểm chứng rẻ nhất trước.

---

## 4. Lỗi thường gặp

| Lỗi | Hậu quả | Cách tránh |
|---|---|---|
| Chỉ có một phương án | Business Case thành văn bản biện minh | Bắt buộc có Do Nothing và một phương án nhẹ |
| Quy hết lợi ích ra tiền | Con số vô nghĩa, bị bắt bẻ khi duyệt | Tách lợi ích định lượng và lợi ích khó quy đổi |
| Bỏ chi phí vận hành, đào tạo | Chi phí 3 năm thấp hơn thực tế | Dùng đủ các nhóm chi phí của `business-case.md` mục 4.1 |
| Lợi ích dựa trên giả định duy nhất | Một con số sai làm hỏng kết luận | Chạy độ nhạy, ghi rõ giả định then chốt |
| Không có điều kiện dừng | Dự án tiếp tục dù chỉ số không đạt | Viết ngưỡng dừng ngay trong khuyến nghị |
| Số liệu bịa cho đẹp | Mất uy tín khi bị hỏi nguồn | Ghi `[Giả định]` hoặc `[Chưa có baseline]`, đề xuất cách đo |

---

## 5. Checklist trước khi nộp

```
☐ Problem Statement không chứa giải pháp, có người chịu ảnh hưởng, tần suất, hậu quả
☐ Mỗi nhận định hiện trạng có mức bằng chứng; kết luận dựa trên E3 trở lên
☐ Có Do Nothing, phương án nhẹ và phương án đầy đủ
☐ Chi phí tính đủ vòng đời; lợi ích có cách đo, baseline, target
☐ Có điểm hòa vốn và độ nhạy ±30% cho giả định then chốt
☐ Lợi ích khó quy đổi trình bày riêng, không bị ép thành số
☐ Khuyến nghị có điều kiện tiếp tục và điều kiện dừng
☐ Người quyết định và ngưỡng quyết định đã rõ
```
