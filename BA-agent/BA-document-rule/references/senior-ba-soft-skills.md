# SENIOR BA: ĐÀM PHÁN, TRUYỀN THÔNG VÀ QUẢN LÝ KỲ VỌNG

> **BABOK:** Underlying Competencies (Communication Skills, Interaction Skills, Behavioral Characteristics). Xem [babok-v3-framework.md](../../knowledge-source/babok-v3-framework.md) mục 4.
> **Dùng khi:** Cần từ chối yêu cầu, đàm phán phạm vi, báo cáo tin xấu, xử lý bất đồng giữa nghiệp vụ và kỹ thuật, hoặc trình bày quyết định cho lãnh đạo.

---

## 1. Nguyên tắc hành xử

| Nguyên tắc | Nghĩa là |
|---|---|
| Phục vụ mục tiêu, không phục vụ yêu cầu | Khi yêu cầu không đưa tổ chức tới mục tiêu, BA nói ra, kèm bằng chứng |
| Không bất ngờ | Tin xấu báo sớm, báo bằng số, báo kèm phương án |
| Không chọn phe | Bất đồng đi vào Conflict Log, người quyết định được xác định rõ |
| Không bịa | Thiếu dữ kiện thì ghi `[CHƯA CÓ THÔNG TIN]` và nói rõ cần gì, từ ai, trước ngày nào |
| Ghi lại | Quyết định miệng thành văn bản trong 24 giờ |

---

## 2. Từ chối hoặc đẩy lùi yêu cầu

Công thức: **ghi nhận nhu cầu, nêu hệ quả bằng số, đưa lựa chọn, để người có quyền quyết.**

| Tình huống | Câu nói thiếu hiệu quả | Cách Senior nói |
|---|---|---|
| Thêm tính năng sát hạn | "Không kịp đâu ạ" | "Thêm tính năng này cần khoảng 8 ngày. Hạn hiện tại còn 5 ngày. Có ba lựa chọn: dời hạn, cắt tính năng X, hoặc giao tính năng này ở đợt sau. Anh/chị chọn hướng nào?" |
| Sponsor đưa giải pháp | "Giải pháp này chưa hợp lý" | "Em hiểu mục tiêu là giảm số cuộc gọi. Em đề xuất đo thử 2 tuần để biết số cuộc gọi hiện tại, rồi so ba cách giải quyết. Nếu số liệu ủng hộ app thì mình làm ngay." |
| Yêu cầu mâu thuẫn luật | "Cái này không được làm" | "Yêu cầu này chạm quy định về dữ liệu trẻ em. Em đã ghi vào rủi ro và cần pháp chế xác nhận trước ngày 20. Trong lúc chờ, em đề xuất giữ phần còn lại của chức năng." |
| Dev nói yêu cầu không rõ | "Tại anh viết không rõ" | "Em làm rõ phần này ngay. Anh chỉ giúp em câu nào đang hiểu theo hai cách, em bổ sung ví dụ và AC." |

---

## 3. Đàm phán phạm vi: lợi ích thay vì lập trường

1. Hỏi "để làm gì" đến khi ra lợi ích cuối (ví dụ: "để phụ huynh yên tâm", chứ không phải "để có tính năng bản đồ").
2. Liệt kê các cách khác đạt cùng lợi ích, rẻ nhất lên đầu.
3. Đưa ma trận Giá trị / Nỗ lực / Rủi ro và để các bên cùng đọc.
4. Chốt theo MoSCoW, ghi lại phần Won't và lý do.
5. Với mỗi phần bị cắt, nói rõ khi nào xem xét lại (điều kiện hoặc ngày).

---

## 4. Báo tin xấu

Cấu trúc 5 dòng, gửi trực tiếp cho người cần quyết, không chờ họp.

```
Tình trạng: [Điều đã xảy ra, một câu, kèm số]
Tác động:   [Ảnh hưởng hạn, chi phí, chất lượng, rủi ro]
Nguyên nhân: [Đã biết gì, chưa biết gì]
Lựa chọn:   [A, B, C: mỗi lựa chọn kèm hệ quả]
Đề xuất:    [Chọn gì, cần quyết trước ngày nào]
```

---

## 5. Quản lý kỳ vọng với stakeholder

| Rủi ro kỳ vọng | Biểu hiện | Việc BA làm |
|---|---|---|
| Hiểu "Must" là "mọi thứ trong đợt 1" | Phản đối khi một Must bị lùi | Định nghĩa Must là "không có thì không go-live"; chỉ để tối đa 60% yêu cầu ở mức Must |
| Hiểu prototype là sản phẩm | Hỏi "sao chưa dùng được" | Gắn nhãn "Bản minh họa, chưa có dữ liệu thật" trên mọi prototype |
| Cho rằng BA phải biết mọi thứ | Trách khi thiếu thông tin | Công bố sớm danh sách câu hỏi mở kèm người trả lời và hạn |
| Ký BRD mà không đọc | Phát sinh sau UAT | Họp 30 phút đọc cùng nhau mục phạm vi, KPI, ràng buộc; ghi biên bản |

---

## 6. Truyền thông với lãnh đạo

- Mở bằng kết luận và điều cần quyết, sau đó mới tới bằng chứng.
- Một trang cho quyết định: vấn đề, phương án, khuyến nghị, rủi ro lớn nhất, điều kiện dừng.
- Con số làm tròn có thể bảo vệ được; chi tiết để ở phụ lục.
- Không dùng thuật ngữ IT khi đối tượng đọc là nghiệp vụ (xem Ma trận độc giả trong SKILL.md).

---

## 7. Decision Memo (thay cho dài dòng trong email)

```
Tiêu đề: Quyết định cần chốt: [tên], hạn [ngày]
Bối cảnh: [2 câu]
Phương án: A / B / C, mỗi phương án một dòng kèm chi phí, lợi ích, rủi ro
Khuyến nghị: [chọn gì, vì sao]
Hệ quả nếu không quyết trước hạn: [cụ thể]
Người quyết: [vai trò]
```

Ghi kết quả vào Conflict Log hoặc Decision Log, cập nhật tài liệu bị ảnh hưởng theo `stakeholder-conflict-resolution.md` mục 5.

---

## 8. Giới hạn đạo đức của BA

| Tình huống | Hành xử |
|---|---|
| Bị yêu cầu viết số liệu lợi ích chưa có căn cứ | Từ chối viết như sự thật; ghi `[Giả định]` kèm người đưa giả định |
| Yêu cầu thu dữ liệu cá nhân vượt mức cần thiết | Nêu nguyên tắc tối thiểu hóa dữ liệu, đưa vào rủi ro, yêu cầu pháp chế xác nhận |
| Yêu cầu giấu hạn chế của giải pháp với người dùng | Ghi vào rủi ro và chuyển cho Sponsor; không tự giấu hoặc tự công bố |
| Bị gây áp lực "ký trước, sửa sau" | Nêu hệ quả hợp đồng, đề nghị ký có điều kiện kèm danh sách mục chưa chốt |
