# DANH SÁCH VĂN BẢN PHÁP LUẬT VIỆT NAM CẦN HỎI KHI ĐẶC TẢ

> **Trạng thái: CHƯA XÁC MINH.** Danh sách lập ngày 26/10/2026 từ kiến thức của người soạn, chưa đối chiếu với nguồn chính thức. Tên văn bản, số hiệu, ngày hiệu lực và văn bản sửa đổi có thể đã thay đổi.
> **Không phải tư vấn pháp lý.** Mục đích là giúp BA biết cần hỏi ai và hỏi gì, không phải kết luận dự án có tuân thủ hay không.
> **Quy tắc dùng:** Không trích số điều, số khoản hay mức phạt trong BRD/SRS từ file này. Nhờ pháp chế hoặc luật sư xác nhận văn bản hiện hành, rồi ghi nguồn và ngày kiểm tra vào mục Tuân thủ của SRS (`templates/industry/regulatory-compliance-matrix.md`).

---

## 1. Cách BA sử dụng

1. Xác định lĩnh vực và loại dữ liệu của dự án (mục 2).
2. Với mỗi dòng áp dụng, ghi một câu hỏi vào Open Questions kèm người trả lời (pháp chế, bảo mật, hoặc Sponsor) và hạn.
3. Khi có câu trả lời, ghi vào Regulatory Compliance Matrix: văn bản, điều khoản áp dụng, yêu cầu hệ thống, FR/NFR tương ứng, người xác nhận, ngày.
4. Mọi yêu cầu xuất phát từ pháp luật gắn nhãn `[Pháp lý: tên văn bản]`.
5. Tier tối thiểu là 2 khi câu hỏi liên quan đến dữ liệu cá nhân hoặc chế tài (xem `core/rigor-tiers.md`).

---

## 2. Danh sách theo chủ đề

| Chủ đề | Văn bản (cần xác minh) | Câu hỏi BA đặt ra |
|---|---|---|
| Dữ liệu cá nhân | Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân | Dữ liệu nào là nhạy cảm? Cần consent ở bước nào, lưu bằng chứng ra sao? Có phải lập hồ sơ đánh giá tác động xử lý dữ liệu không? Thời hạn lưu và xóa là bao lâu? |
| Dữ liệu cá nhân | Luật Bảo vệ dữ liệu cá nhân (ban hành năm 2025, theo hiểu biết của người soạn có hiệu lực từ 2026) và văn bản hướng dẫn | Văn bản này thay thế hoặc bổ sung điều gì so với Nghị định 13/2023? Hướng dẫn thi hành đã ban hành chưa? |
| Trẻ em | Luật Trẻ em 2016 và văn bản hướng dẫn; quy định về dữ liệu cá nhân của trẻ em trong văn bản bảo vệ dữ liệu | Ai đồng ý thay trẻ? Độ tuổi nào cần cả sự đồng ý của trẻ? Có hạn chế thu ảnh, sinh trắc học, vị trí của trẻ không? |
| An ninh mạng | Luật An ninh mạng 2018 và nghị định hướng dẫn | Dữ liệu có phải lưu trong nước không? Doanh nghiệp có nghĩa vụ báo cáo hoặc lưu log theo yêu cầu không? |
| An toàn thông tin | Luật An toàn thông tin mạng 2015; Nghị định 85/2016/NĐ-CP về hệ thống thông tin theo cấp độ | Hệ thống thuộc cấp độ nào? Yêu cầu kỹ thuật và quản lý tương ứng? |
| Giao dịch điện tử | Luật Giao dịch điện tử 2023 | Chữ ký số, hợp đồng điện tử, thông điệp dữ liệu có giá trị pháp lý ở bước nào? |
| Hóa đơn, kế toán | Quy định về hóa đơn điện tử (Nghị định 123/2020/NĐ-CP, Thông tư 78/2021/TT-BTC và văn bản sửa đổi) | Hóa đơn lập khi nào, ai ký, tích hợp với cơ quan thuế ra sao? |
| Phòng chống rửa tiền, KYC | Luật Phòng, chống rửa tiền 2022; quy định của Ngân hàng Nhà nước về định danh khách hàng | Mức xác thực nào theo hạn mức giao dịch? Hồ sơ lưu bao lâu? Báo cáo giao dịch đáng ngờ do ai thực hiện? |
| Xác thực sinh trắc học trong ngân hàng | Quy định của Ngân hàng Nhà nước về xác thực sinh trắc học khi giao dịch (cần xác minh số hiệu) | Ngưỡng giao dịch nào phải xác thực sinh trắc? Thiết bị nào được chấp nhận? |
| Thương mại điện tử, người tiêu dùng | Nghị định 52/2013/NĐ-CP và văn bản sửa đổi; Luật Bảo vệ quyền lợi người tiêu dùng 2023 | Điều khoản hoàn, hủy, đổi trả; thông tin phải hiển thị; cách giải quyết khiếu nại |
| Y tế | Luật Khám bệnh, chữa bệnh 2023 và văn bản hướng dẫn về hồ sơ bệnh án điện tử | Ai được xem hồ sơ? Thời gian lưu? Điều kiện hồ sơ điện tử có giá trị pháp lý? |
| Mua sắm, đấu thầu công | Luật Đấu thầu 2023 và nghị định hướng dẫn | Hình thức lựa chọn nhà thầu, hồ sơ mời thầu yêu cầu gì về tài liệu và nghiệm thu? |
| Sở hữu trí tuệ, bản quyền | Luật Sở hữu trí tuệ | Quyền sở hữu mã nguồn, tài liệu, dữ liệu sau bàn giao thuộc ai? |

---

## 3. Mẫu dòng trong Open Questions

```
OQ-014 [Pháp lý] Dữ liệu khuôn mặt của học sinh có cần lập hồ sơ đánh giá tác động xử lý dữ liệu cá nhân trước khi thu thập không?
Người trả lời: Pháp chế trường / luật sư dự án
Hạn: [DD/MM/YYYY]
Ảnh hưởng nếu chưa có câu trả lời: FR-CC.03, FR-04.1, BRULE-016/017 chưa chốt; không đưa vào Sprint 1
```

---

## 4. Mẫu ghi nhận sau khi xác nhận

| Văn bản (tên, số hiệu) | Điều khoản áp dụng | Yêu cầu hệ thống | FR/NFR | Người xác nhận | Ngày kiểm tra |
|---|---|---|---|---|---|
| [Điền sau khi pháp chế xác nhận] | | | | | |

Cập nhật bảng này khi văn bản được sửa đổi. Gắn ngày kiểm tra gần nhất vào Change Log của SRS.
