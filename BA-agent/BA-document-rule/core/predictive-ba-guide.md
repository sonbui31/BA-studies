# DỰ BÁO BA & QUẢN TRỊ RỦI RO (Predictive BA Guide 2.6)

> **Mục đích:** Sử dụng dữ liệu và trí tuệ nhân tạo để dự báo các rủi ro về phạm vi (Scope) và tiến độ trước khi chúng xảy ra.
> **Triết lý:** Chuyển từ "Phản ứng" (Reactive) sang "Phòng ngừa" (Proactive).

---

## 1. Các mô hình Dự báo (Prediction Models)

### A. Scope Creep Forecast (Dự báo phình phạm vi)
- **Cơ chế:** AI phân tích độ phức tạp của User Stories và lịch sử thay đổi yêu cầu để cảnh báo các vùng có nguy cơ bị Stakeholder "đòi thêm" sau khi sign-off.
- **Cảnh báo:** "Dựa trên mô tả này, tính năng Dashboard có 80% rủi ro bị thay đổi scope liên tục do thiếu Input từ Marketing".

### B. Timeline Delay Predictor (Dự báo chậm tiến độ)
- **Cơ chế:** Đối soát giữa Story Points, độ phức tạp logic (o4 reasoning) và năng suất thực tế của team (velocity) để dự báo ngày hoàn thành thực tế.

### C. Complexity Heatmap (Bản đồ nhiệt độ phức tạp)
- **Cơ chế:** Đánh dấu các section trong SRS mà AI đánh giá là "cực kỳ lắt léo" và dễ gây hiểu lầm giữa BA, Dev và Client.

---

## 2. Quy trình Thực hiện (Prediction Workflow)

1. **Historical Data Input:** Đưa thông tin về các dự án cũ hoặc dữ liệu sơ bộ của dự án hiện tại.
2. **Pattern Matching:** AI so sánh với hàng ngàn mẫu dự án tương tự để tìm rủi ro tiềm ẩn.
3. **Simulation:** Chạy mô phỏng các kịch bản "Nếu... thì..." (ví dụ: Nếu Tech Lead nghỉ việc, nếu Client đổi yêu cầu thanh toán).
4. **Mitigation Proposal:** Đề xuất các phương án dự phòng ngay trong BRD/Vision & Scope.

---

## 3. Lệnh kích hoạt

- `@[ba-specialist] hãy dự báo rủi ro phình scope cho dự án này dựa trên BRD`
- `@[ba-specialist] đánh giá độ phức tạp các stories và dự báo khả năng kịp deadline Q3`
- `@[ba-specialist] tìm các "điểm nóng" dễ gây tranh cãi trong SRS này`
