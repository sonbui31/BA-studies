# CASE STUDY: Parent App (vClassio), đọc như một BA Senior

> **Nguồn:** `projects/vClassio_app/parent_app/parent_app_md` (BRD v0.9, SRS) do tác giả dự án viết. Phần dưới là nhận xét của người rà soát dựa trên nội dung đã đọc, không phải quyết định của dự án. Mọi chỗ ghi "chưa thấy" nghĩa là không thấy trong phần đã đọc, cần hỏi lại tác giả trước khi kết luận thiếu.
> **Mục đích:** Cho thấy BA Senior nhìn một bộ tài liệu thật ra sao: điểm đáng giữ, điểm cần hỏi, và cách sửa.

---

## 1. Tóm tắt dự án

Ứng dụng di động cho phụ huynh theo dõi con: sổ liên lạc, thời khóa biểu, học phí, điểm danh bằng nhận diện khuôn mặt (có thông báo thời gian thực kèm ảnh, giờ, vị trí, giáo viên), xin nghỉ, tin tức, lịch sử khóa học. Ngoài phạm vi: thanh toán học phí online, chat hai chiều, sửa dữ liệu điểm danh.

---

## 2. Điểm đáng giữ (cách làm của người có kinh nghiệm)

| Điểm | Vì sao tốt |
|---|---|
| Tách BR → SR → FR, SR viết bằng giọng nhu cầu | Đúng phân tầng BABOK, tránh nhảy từ mục tiêu sang tính năng |
| Change Log ghi lý do từng lần sửa (sửa RACI, tách bảng, đối chiếu nguyên văn elicitation) | Cho thấy kỷ luật quay lại nguồn; người đọc tin được bản cuối |
| Phạm vi có phần Ngoài phạm vi kèm lý do ("giai đoạn này") | Tránh phạm vi phình, có chỗ để quay lại |
| FR-04.1 có luồng ngoại lệ đầy đủ: không nhận diện được thì cho điểm danh thủ công kèm ghi chú; chưa có consent thì chặn nhận diện và cảnh báo School Admin | Hệ thống không phụ thuộc hoàn toàn vào công nghệ có tỷ lệ lỗi |
| Consent đặt thành BRULE-017 và FR-CC.03; GPS chỉ lưu tại thời điểm điểm danh | Xử lý dữ liệu trẻ em theo hướng tối thiểu hóa |
| FR-02.2: đồng bộ thất bại thì giữ dữ liệu cũ | Quyết định đúng về tính toàn vẹn dữ liệu |
| Rủi ro riêng cho dữ liệu khuôn mặt và GPS, có biện pháp | Nhìn thấy rủi ro pháp lý từ sớm |

---

## 3. Những điều BA Senior sẽ hỏi hoặc sửa

### 3.1 KPI không nhất quán và chưa đo được

| Phát hiện | Vì sao là vấn đề | Cách sửa |
|---|---|---|
| BR-001: "≥ 80% phụ huynh truy cập ít nhất 1 lần/tuần". Mục KPI: "≥ 70% phụ huynh sử dụng hằng tháng" | Nếu 80% dùng hằng tuần thì ít nhất 80% dùng hằng tháng. Chỉ số 70% hằng tháng thấp hơn và không còn ràng buộc | Chọn một định nghĩa "phụ huynh hoạt động", dùng cùng mẫu số, bỏ chỉ số dư |
| "Giảm ≥ 50% trao đổi thủ công trong 2 tháng đầu" | Chưa thấy baseline số cuộc gọi hiện tại | Đo 2 tuần trước go-live, ghi baseline vào Benefit Register |
| "Tỷ lệ dữ liệu điểm danh chính xác ≥ 95%" | Không rõ chính xác tính theo đâu: nhận đúng, hay bản ghi cuối cùng đúng sau khi giáo viên sửa tay. 5% sai trên điểm danh trẻ em là nhiều | Tách hai chỉ số: tỷ lệ nhận sai người (guardrail, mục tiêu gần 0) và tỷ lệ phải điểm danh thủ công |
| "≥ 80% phụ huynh xem thông tin điểm danh" | Mẫu số chưa rõ (tất cả phụ huynh hay phụ huynh có con đi học trong kỳ) | Ghi mẫu số trong định nghĩa chỉ số |

Quy trình sửa: `solution-evaluation-guide.md` mục 2 và 4.

### 3.2 Công nghệ nhận diện khuôn mặt: đã so sánh phương án chưa?

BRD ghi nhận công nghệ này đã được xác nhận với stakeholder (Change Log v0.5). Chưa thấy bảng so sánh phương án trong phần đã đọc. BA Senior hỏi và ghi lại:

| Phương án | Điều cần biết |
|---|---|
| Nhận diện khuôn mặt | Tỷ lệ chấp nhận sai và từ chối sai mục tiêu là bao nhiêu? Chất lượng thiết bị giáo viên? Dữ liệu trẻ em lưu ở đâu, bao lâu? |
| Giáo viên chạm tên học sinh kèm ảnh nhóm và GPS | Có đáp ứng mục tiêu "yên tâm" của phụ huynh không? Rủi ro pháp lý thấp hơn nhiều |
| Thẻ QR hoặc NFC | Học sinh nhỏ có mang theo không? |
| Quét mã khi vào cổng | Không phù hợp nếu điểm danh theo lớp |

Việc cần làm là ghi vào BRD người quyết định, phương án đã so sánh, lý do chọn, và điều kiện lùi về phương án nhẹ hơn. Với Tier 3 (dữ liệu sinh trắc của trẻ em), đây là mục bắt buộc (xem `rigor-tiers.md`).

### 3.3 Chỉ tiêu nhận diện chưa có số

FR-04.1 dùng "ngưỡng cấu hình" cho độ tương đồng. Hai điều cần cố định trước khi dev:

- Tỷ lệ chấp nhận sai (nhận nhầm em A thành em B, rồi gửi thông báo sai cho phụ huynh) tối đa bao nhiêu? Đây là guardrail, quan trọng hơn tỷ lệ nhận đúng.
- Điều kiện kiểm thử: số học sinh, điều kiện ánh sáng, thiết bị nào, ai nghiệm thu.

Nếu chưa trả lời được, ghi `[Open Question]` kèm người trả lời và hạn, đưa vào NFR là "cần định lượng", không để "ngưỡng cấu hình" che khoảng trống.

### 3.4 Phụ thuộc chưa xác nhận

FR-02.2 ghi cơ chế kết nối School Management System "chưa xác nhận". Đây là phụ thuộc có thể quyết định lịch dự án (thời khóa biểu, lớp, học sinh đều phụ thuộc nguồn này). BA Senior:

- Đưa vào RAID Log dưới dạng Dependency, có owner và hạn.
- Hỏi: hệ thống nguồn có API không, hay chỉ xuất file? Ai quản trị? Tần suất cập nhật?
- Đặt vào Giả định (hiện có "dữ liệu được cung cấp đầy đủ") và xác định ai chịu trách nhiệm nếu giả định sai.

### 3.5 Phê duyệt và stakeholder

Bảng Stakeholder và bảng Phê duyệt để trống tên. Change Log v0.2 ghi đã điền `TBD`, bảng chưa có. Với BRD cần ký, Sponsor chưa xác định thì chưa có người chịu trách nhiệm quyết định các chuyện ở mục 3.2 và 3.4. Điền vai trò cụ thể hoặc ghi `[CHƯA XÁC ĐỊNH]` kèm hạn.

### 3.6 Truy vết giữa hai scheme

Dự án dùng `BR`, `SR`, `BRULE`, `FR-01.1`; framework dùng `BRQ`, `BR`, `FR-MOD-001`. Xem `core/traceability-validator.md` mục 8 và `projects/vClassio_app/parent_app/MIGRATION-NOTES.md`. Một BA Senior giữ SR (vì hữu ích) và ghi rõ scheme trong Change Log thay vì ép đổi sang canonical.

### 3.7 Rủi ro chưa thấy

Danh sách rủi ro tốt về dữ liệu và thông báo. Các rủi ro BA Senior bổ sung để hỏi:

| Rủi ro | Mức cảnh báo |
|---|---|
| Giáo viên không đủ thời gian điểm danh bằng mặt cho mọi học sinh (lớp đông, đầu giờ) | Cao, ảnh hưởng chất lượng dữ liệu |
| Phụ huynh không đồng ý consent | Cao, quyết định tỷ lệ học sinh dùng được nhận diện; cần luồng thủ công mặc định |
| Thông báo ảnh trẻ em gửi nhầm phụ huynh | Cao, hậu quả danh tiếng và pháp lý |
| Thiết bị giáo viên (camera, GPS) không đủ chuẩn | Trung bình. Change Log v0.9 ghi đã thêm giả định này, nhưng danh sách Giả định trong bản đã đọc không có dòng đó; cần đối chiếu và gán owner |
| Nhà trường đổi quy trình nghỉ, duyệt đơn | Trung bình |

---

## 4. Bài học áp dụng cho dự án khác

1. **Viết KPI cùng lúc với yêu cầu**, vì chỉ số sinh ra sau thường mâu thuẫn với chỉ số cũ.
2. **Mỗi công nghệ rủi ro cao cần bảng phương án và guardrail.** Không dựa vào "đã xác nhận với stakeholder".
3. **Phụ thuộc bên ngoài chưa xác nhận là rủi ro số một.** Đưa lên đầu RAID Log.
4. **Giữ phần tốt của scheme riêng** khi nó phục vụ dự án (tầng SR), và ghi rõ cách ánh xạ.
5. **Không để chỗ trống ở bảng phê duyệt.** Không có tên thì chưa có người quyết định.
