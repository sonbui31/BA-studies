# SOLUTION EVALUATION GUIDE: Đo giá trị sau khi giải pháp chạy

> **BABOK KA:** Solution Evaluation. Xem [babok-v3-framework.md](../../knowledge-source/babok-v3-framework.md) mục 2.6.
> **Dùng khi:** Viết KPI trong BRD, lên kế hoạch đo sau go-live, chạy review 30/60/90 ngày, hoặc quyết định giữ, chỉnh, mở rộng hay dừng một giải pháp.
> **Liên quan:** `templates/post-implementation-review.md`, `templates/product-analytics-spec.md`.

---

## 1. Nguyên tắc

BA Senior viết KPI với giả định rằng sẽ có người hỏi "con số này đo bằng cách nào, lấy ở đâu, so với cái gì?" sau go-live. KPI không trả lời được ba câu đó chưa phải là KPI.

---

## 2. Benefit Register: mỗi lợi ích một dòng

| Trường | Nội dung | Ví dụ |
|---|---|---|
| ID | `BEN-001` | |
| Lợi ích | Kết quả mong đợi, viết bằng hành vi hoặc số | Giảm số cuộc gọi hỏi tình trạng điểm danh |
| Liên kết | `BRQ-*` hoặc mục tiêu trong BRD | BRQ-04 |
| Chỉ số | Công thức rõ ràng | Số cuộc gọi hỏi điểm danh mỗi tuần |
| Baseline | Giá trị hiện tại và ngày đo, hoặc `[Chưa có, đo trước go-live]` | 150 cuộc/tuần, đo 2 tuần trước go-live |
| Target và hạn | Mức đạt và thời điểm | ≤ 75 cuộc/tuần sau 2 tháng |
| Nguồn dữ liệu | Hệ thống, báo cáo hoặc khảo sát | Nhật ký cuộc gọi văn phòng |
| Người đo | Vai trò chịu trách nhiệm | Admin trường |
| Tần suất | Khi nào đo | Hằng tuần trong 8 tuần đầu |
| Chủ sở hữu lợi ích | Người hưởng lợi cam kết thay đổi hành vi | Hiệu trưởng |

Quy tắc: không có baseline thì không viết target dạng "giảm X%". Ghi rõ việc cần làm trước go-live để có baseline.

---

## 3. Chọn chỉ số

| Loại | Dùng để | Ví dụ | Chú ý |
|---|---|---|---|
| Leading (dẫn dắt) | Cảnh báo sớm trong 2–6 tuần đầu | Tỷ lệ kích hoạt tài khoản, tỷ lệ mở thông báo | Chưa chứng minh giá trị |
| Lagging (kết quả) | Chứng minh giá trị | Giảm cuộc hỏi, tỷ lệ phụ huynh rút học | Chậm, nhiều yếu tố khác tác động |
| Guardrail (chặn) | Phát hiện tác hại phụ | Khiếu nại về quyền riêng tư, tỷ lệ nhận diện sai | Luôn có ít nhất một |
| Vanity | Không dùng | Số lượt tải app | Không gắn với quyết định nào |

Mỗi mục tiêu kinh doanh có ít nhất một chỉ số kết quả và một guardrail.

---

## 4. Kiểm tra tính nhất quán của bộ KPI

Chạy các kiểm tra này trước khi gửi BRD. Chúng bắt được lỗi mà đọc lướt không thấy.

| Kiểm tra | Câu hỏi | Ví dụ lỗi |
|---|---|---|
| Nhất quán số học | Hai chỉ số có thể cùng đúng không? | "≥ 80% truy cập mỗi tuần" nhưng "≥ 70% dùng mỗi tháng": nếu 80% dùng mỗi tuần thì tối thiểu 80% dùng mỗi tháng, nên chỉ số thứ hai không còn ràng buộc |
| Mẫu số | Tỷ lệ này chia cho ai? | "≥ 80% phụ huynh xem thông tin điểm danh" chia cho tổng phụ huynh, phụ huynh có tài khoản, hay phụ huynh có con điểm danh trong kỳ? |
| Định nghĩa "dùng" | Mở app một lần có tính không? | Nên định nghĩa: có ít nhất một hành động có ý nghĩa |
| Đo được | Hệ thống có log để đo không? | KPI cần event chưa được thiết kế trong `product-analytics-spec.md` |
| Thời hạn | Đo ở thời điểm nào sau go-live? | Không có hạn thì không có ngày đánh giá |
| Độ chính xác | "Chính xác ≥ 95%" đo bằng gì? | Cần định nghĩa mẫu kiểm tra, ai kiểm, tính cả nhận sai người hay chỉ bỏ sót |
| Gắn với quyết định | Số này đạt hoặc không đạt thì làm gì? | Không dẫn tới quyết định nào thì bỏ |

---

## 5. Lịch đánh giá sau go-live

| Mốc | Câu hỏi | Dữ liệu | Quyết định có thể |
|---|---|---|---|
| Tuần 2 | Người dùng đăng nhập và làm được tác vụ chính không? | Kích hoạt, lỗi, hỗ trợ | Sửa lỗi chặn, bổ sung hướng dẫn |
| Ngày 30 | Có dùng lặp lại không? | Tỷ lệ quay lại, phản hồi | Chỉnh luồng, điều chỉnh truyền thông |
| Ngày 60 | Chỉ số kết quả bắt đầu dịch chuyển chưa? | So với baseline | Tiếp tục, chỉnh, hoặc tăng nguồn lực |
| Ngày 90 | Giải pháp có tạo ra giá trị đã hứa? | Benefit Register | Giữ, mở rộng, thu hẹp hoặc dừng |

Quyết định ở ngày 90 chỉ có bốn lựa chọn: **giữ nguyên**, **chỉnh** (đổi hành vi, quy trình, thiết kế), **mở rộng** (thêm phạm vi, người dùng), **dừng**. Mỗi lựa chọn kèm lý do và dữ liệu.

---

## 6. Phân tích giới hạn

Khi chỉ số không đạt, tìm nguyên nhân theo thứ tự:

1. **Giải pháp:** tính năng thiếu, lỗi, khó dùng.
2. **Tổ chức:** người dùng chưa đổi quy trình, thiếu đào tạo, không có người sở hữu, dữ liệu đầu vào không đủ.
3. **Giả định sai:** vấn đề không lớn như tưởng, hoặc nhóm người dùng khác dự kiến.
4. **Đo sai:** baseline hoặc cách đo không đáng tin.

Không kết luận "giải pháp thất bại" khi chưa loại trừ nhóm 2 và 4. Nhiều dự án đạt kỹ thuật nhưng không đạt giá trị vì tổ chức chưa đổi cách làm.

---

## 7. Lỗi thường gặp

| Lỗi | Cách tránh |
|---|---|
| KPI viết sau go-live | Viết Benefit Register trong BRD, đo baseline trước go-live |
| Đo quá sớm rồi kết luận | Dùng leading indicator cho 4 tuần đầu, lagging cho tuần 8 trở đi |
| Quy kết nhân quả không có cơ sở | Dùng nhóm đối chứng, so trước/sau cùng điều kiện, hoặc ghi rõ "tương quan" |
| Không có guardrail | Thêm chỉ số tác hại phụ (khiếu nại, lỗi nhận sai, rủi ro dữ liệu) |
| Không ai sở hữu lợi ích | Gán Chủ sở hữu lợi ích là người của bên nghiệp vụ, không phải đội dự án |

---

## 8. Checklist

```
☐ Mỗi mục tiêu kinh doanh có Benefit Register: chỉ số, baseline, target, hạn, nguồn, người đo
☐ Baseline đã có hoặc có kế hoạch đo trước go-live
☐ Bộ KPI qua kiểm tra nhất quán số học, mẫu số, định nghĩa "dùng"
☐ Có ít nhất một guardrail
☐ Sự kiện cần log đã nằm trong đặc tả analytics
☐ Có lịch review tuần 2, ngày 30, 60, 90 và người chủ trì
☐ Có quy tắc quyết định: giữ, chỉnh, mở rộng, dừng
```
