# CẨM NANG ƯỚC LƯỢNG ĐỘ PHỨC TẠP YÊU CẦU (REQUIREMENTS COMPLEXITY ESTIMATION)
*Hướng dẫn thực hành các phương pháp ước lượng quy mô, nỗ lực và thời gian phân tích dành cho BA và PO.*

---

## 1. TỔNG QUAN & TẦM QUAN TRỌNG

Ước lượng sai thời gian và độ phức tạp trong giai đoạn phân tích yêu cầu dẫn đến sự sụp đổ dây chuyền trong toàn bộ dự án:
- Developer thiếu thời gian viết code dẫn đến nợ kỹ thuật (Technical Debt).
- Tester bị ép tiến độ dẫn đến bỏ sót lỗi trên môi trường kiểm thử.
- Mốc thời gian Go-live bị phá vỡ hoặc sản phẩm ra mắt bị cắt giảm tính năng cốt lõi.

### 3 Mục tiêu ước lượng của BA/PO
1. **Estimate Effort & Time (Nỗ lực & Thời gian):** Dự đoán tổng số giờ làm việc cần thiết để BA hoàn thành việc khơi gợi, mô hình hóa, viết tài liệu (BRD, SRS), tổ chức review, hỗ trợ Dev và nghiệm thu UAT.
2. **Estimate Scope & Complexity (Phạm vi & Độ phức tạp):** Đánh giá độ khó kỹ thuật, các ràng buộc dữ liệu, mức độ rủi ro và các hệ thống phụ thuộc của từng hạng mục (Epic, User Story, Use Case).
3. **Estimate Size (Dung lượng Backlog):** Định lượng tổng quy mô của danh mục yêu cầu để phục vụ việc lập kế hoạch Release, phân bổ Sprint và đàm phán ngân sách với khách hàng.

---

## 2. BỘ 9 KỸ THUẬT ƯỚC LƯỢNG THỰC CHIẾN

### 1. Expert Judgment (Ước lượng theo kinh nghiệm chuyên gia)
- **Bản chất:** Dựa trên trực giác và bài học thực tế của Senior BA, Technical Architect hoặc Chuyên gia nghiệp vụ (SME).
- **Khi nào áp dụng:** Dự án mới tinh, công nghệ chưa từng triển khai nội bộ, thiếu hoàn toàn dữ liệu lịch sử.
- **Ưu điểm:** Nhanh, linh hoạt, chi phí chuẩn bị bằng 0.
- **Hạn chế:** Mang tính chủ quan, phụ thuộc năng lực cá nhân, khó tái lập và khó bảo vệ số liệu trước khách hàng.
- **Ví dụ:** *"Với quy mô module Quản lý kho này, dựa trên kinh nghiệm các dự án tương đương, BA cần khoảng 5 ngày làm việc để hoàn thiện tài liệu SRS."*

---

### 2. Analogous Estimation (Ước lượng so sánh tương tự)
- **Bản chất:** Lấy số liệu thực tế đã tiêu tốn từ một tính năng hoặc dự án tương đương trong quá khứ để làm thước đo tham chiếu.
- **Khi nào áp dụng:** Khi tổ chức đã có kho dữ liệu lịch sử (Historical Data) và hệ thống mới có nhiều điểm tương đồng.
- **Công thức suy diễn:**
  $$\text{Effort mới} = \text{Effort cũ} \times \text{Hệ số điều chỉnh (Complexity Ratio)}$$
- **Ví dụ:** Module Thanh toán QR Code mới tương tự module Chuyển khoản ngân hàng đã làm ở dự án trước, nhưng ít luồng ngoại lệ hơn $\rightarrow$ Lấy 80% thời gian của module cũ (cũ mất 40h $\rightarrow$ mới ước tính 32h).

---

### 3. Top-Down Estimation (Ước lượng từ trên xuống)
- **Bản chất:** Bắt đầu bằng việc ước lượng tổng ngân sách thời gian cho toàn bộ giai đoạn phân tích, sau đó chia tỷ lệ phần trăm xuống từng nhóm công việc cụ thể.
- **Khi nào áp dụng:** Giai đoạn đầu dự án (Early Planning), khi báo giá thầu hoặc khi khách hàng ấn định một ngân sách thời gian cố định.
- **Ví dụ phân bổ tỷ lệ:** Tổng quỹ thời gian phân tích là **100 giờ**:
  - Khơi gợi & Khảo sát nghiệp vụ: 40% (40 giờ)
  - Thiết kế Wireframe & UI Layout: 30% (30 giờ)
  - Đặc tả Business Rules & Data Model: 20% (20 giờ)
  - Hỗ trợ Review & Ký duyệt UAT: 10% (10 giờ)

---

### 4. Bottom-Up Estimation (Ước lượng từ dưới lên)
- **Bản chất:** Phân rã cấu trúc công việc (WBS) thành các tác vụ cực nhỏ (dưới 8 giờ), ước lượng chi tiết từng tác vụ rồi cộng dồn lên cấp dự án.
- **Khi nào áp dụng:** Khi đã có bản phân rã tính năng chi tiết, trước khi ký hợp đồng thi công hoặc trước khi chốt kế hoạch Sprint.
- **Ưu điểm:** Độ chính xác cao nhất, bám sát khối lượng công việc thực tế.
- **Hạn chế:** Đòi hỏi nhiều thời gian và công sức để bóc tách ban đầu.
- **Ví dụ bảng tính:**
  - Họp phỏng vấn kế toán trưởng: 2 giờ
  - Vẽ sơ đồ BPMN quy trình duyệt chi: 3 giờ
  - Soạn thảo Business Rules tính thuế: 4 giờ
  - Viết tài liệu User Story & AC: 5 giờ
  - $\rightarrow$ Tổng nỗ lực hoàn thành: 14 giờ.

---

### 5. Three-Point Estimation (Ước lượng 3 điểm theo kỹ thuật PERT)
- **Bản chất:** Giảm thiểu rủi ro cảm tính bằng cách tính toán giá trị kỳ vọng dựa trên phân phối xác suất hình chuông (Beta Distribution).
- **3 Chỉ số đầu vào:**
  - $O$ *(Optimistic):* Thời gian ngắn nhất khi mọi điều kiện thuận lợi hoàn hảo.
  - $M$ *(Most Likely):* Thời gian khả thi nhất trong điều kiện làm việc bình thường.
  - $P$ *(Pessimistic):* Thời gian dài nhất khi mọi rủi ro xấu nhất đồng loạt xảy ra.
- **Công thức tính giá trị kỳ vọng (Expected Effort):**
  $$E = \frac{O + 4M + P}{6}$$
- **Công thức tính độ lệch chuẩn (Đo lường mức độ rủi ro):**
  $$\sigma = \frac{P - O}{6}$$
- **Ví dụ:** Viết tài liệu đặc tả chức năng Đồng bộ ngân hàng:
  - $O = 6$ giờ, $M = 8$ giờ, $P = 16$ giờ.
  - Giá trị kỳ vọng: $E = \frac{6 + 4 \times 8 + 16}{6} = \frac{54}{6} = 9$ giờ.
  - Độ lệch chuẩn: $\sigma = \frac{16 - 6}{6} = 1.67$ giờ.
  - Khoảng tin cậy 95%: $9 \pm (2 \times 1.67) \rightarrow [5.66 \text{ giờ} - 12.34 \text{ giờ}]$.

---

### 6. Planning Poker (Ước lượng bài Poker trong Agile)
- **Bản chất:** Toàn bộ thành viên nhóm phát triển (Product Owner, BA, Developer, Tester) cùng tham gia bỏ phiếu kín để xác định độ phức tạp tương đối của từng User Story.
- **Quy ước thang điểm (Dãy số Fibonacci chuẩn hóa):**
  $$1, 2, 3, 5, 8, 13, 20, 40, 100$$
- **Vai trò của BA:** BA trình bày nghiệp vụ, giải thích tiêu chí chấp thuận (AC) và trả lời các thắc mắc logic của đội kỹ thuật trước khi bỏ phiếu.
- **Xử lý bất đồng thuận:** Nếu điểm số chênh lệch lớn (người ra 3 điểm, người ra 13 điểm), người cho điểm cao nhất và thấp nhất phải giải thích lý do, sau đó cả nhóm thảo luận và bỏ phiếu lại lượt 2.

---

### 7. T-Shirt Sizing (Quy đổi theo cỡ áo)
- **Bản chất:** Phân loại quy mô yêu cầu theo các cấp độ trực quan (XS, S, M, L, XL) thay vì gán số giờ cụ thể ngay từ đầu.
- **Bảng quy chuẩn chuyển đổi tham khảo:**

| Size | Định nghĩa độ phức tạp | Thời gian BA phân tích | Story Points tương đương |
| :---: | :--- | :---: | :---: |
| **XS** | Chỉnh sửa văn bản, thêm 1 trường dữ liệu đơn giản, không đổi logic | 2–4 giờ | 1 SP |
| **S** | Tính năng CRUD đơn giản trên một bảng dữ liệu độc lập | 1–2 ngày | 2–3 SP |
| **M** | Tính năng có kiểm tra logic, validate nghiệp vụ, gửi thông báo | 3–5 ngày | 5 SP |
| **L** | Module tích hợp bên thứ ba, xử lý bất đồng bộ, nhiều nhánh rẽ | 1–2 tuần | 8 SP |
| **XL** | Phân hệ lõi phức tạp, tác động toàn bộ kiến trúc hệ thống | > 2 tuần *(Bắt buộc chia nhỏ)* | $\ge 13$ SP *(Phải tách Epic)* |

---

### 8. Function Point Analysis - FPA (Phân tích điểm chức năng)
- **Bản chất:** Định lượng quy mô phần mềm dựa trên các chức năng nghiệp vụ mà người dùng nhìn thấy và nhận được, hoàn toàn độc lập với ngôn ngữ lập trình.
- **5 Thành phần chức năng chuẩn hóa (Functional Components):**
  1. *External Inputs (EI):* Màn hình hoặc luồng người dùng nhập dữ liệu vào hệ thống (Thêm mới, Cập nhật).
  2. *External Outputs (EO):* Báo cáo tổng hợp, màn hình xuất dữ liệu có qua giải thuật xử lý tính toán.
  3. *External Inquiries (EQ):* Màn hình tra cứu, xem chi tiết dữ liệu thuần túy (không tính toán phức tạp).
  4. *Internal Logical Files (ILF):* Bảng dữ liệu nội bộ do chính hệ thống lưu trữ và duy trì.
  5. *External Interface Files (EIF):* Tệp dữ liệu hoặc API tham chiếu từ hệ thống ngoài.
- **Quy trình tính toán:**
  $$\text{Unadjusted Function Points (UFP)} = \sum (\text{Số lượng thành phần} \times \text{Trọng số phức tạp})$$
  $$\text{Adjusted Function Points (AFP)} = \text{UFP} \times [0.65 + (0.01 \times \text{VAF})]$$
  *(VAF: Hệ số điều chỉnh giá trị dựa trên 14 đặc tính kỹ thuật chung).*

---

### 9. Use Case Points - UCP (Điểm trường hợp sử dụng)
- **Bản chất:** Phương pháp đo lường quy mô dựa trên mô hình Use Case UML, tính toán trọng số của Actor và Use Case kết hợp các hệ số môi trường kỹ thuật.
- **Công thức tổng quát:**
  $$\text{UCP} = (\text{UAW} + \text{UUCW}) \times \text{TCF} \times \text{ECF}$$
- **Các thành phần tính toán:**
  - **UAW (Unadjusted Actor Weight):**
    - *Simple Actor:* Hệ thống giao tiếp qua API/giao thức chuẩn (Trọng số: 1).
    - *Average Actor:* Hệ thống ngoài giao tiếp qua giao thức tùy biến (Trọng số: 2).
    - *Complex Actor:* Con người tương tác qua giao diện đồ họa GUI (Trọng số: 3).
  - **UUCW (Unadjusted Use Case Weight):**
    - *Simple Use Case:* 1–3 giao dịch thành công (Trọng số: 5).
    - *Average Use Case:* 4–7 giao dịch (Trọng số: 10).
    - *Complex Use Case:* > 7 giao dịch phức tạp (Trọng số: 15).
  - **TCF (Technical Complexity Factor):** Đánh giá 13 yếu tố kỹ thuật (phân tán, bảo mật, hiệu năng).
  - **ECF (Environmental Complexity Factor):** Đánh giá 8 yếu tố môi trường (kinh nghiệm đội ngũ, độ ổn định yêu cầu).

---

## 3. MA TRẬN LỰA CHỌN PHƯƠNG PHÁP THEO MÔ HÌNH DỰ ÁN

| Bối cảnh & Mô hình dự án | Phương pháp khuyến nghị ưu tiên | Phương pháp bổ trợ |
| :--- | :--- | :--- |
| **Dự án Agile / Scrum định kỳ** | Planning Poker (cho User Story) | T-Shirt Sizing (cho Epic/Backlog) |
| **Dự án Waterfall / Hợp đồng cố định giá** | Bottom-Up Estimation (WBS) | Three-Point Estimation (PERT) |
| **Đấu thầu phần mềm doanh nghiệp lớn** | Function Point Analysis (FPA) | Analogous Estimation |
| **Dự án thiết kế theo UML / Use Case** | Use Case Points (UCP) | Expert Judgment |
| **Khảo sát ban đầu (Thiếu dữ liệu)** | Expert Judgment | Top-Down Allocation |

---

## 4. CHECKLIST PHÒNG NGỪA SAI SỐ ƯỚC LƯỢNG (ESTIMATION HYGIENE)

Trước khi ký chốt bất kỳ con số ước lượng nào, BA bắt buộc kiểm tra lại theo danh sách:

1. **Đã bao gồm thời gian họp và làm rõ chưa?** Ước lượng không chỉ gồm thời gian gõ văn bản; phải cộng thêm thời gian họp stakeholder, làm việc với Dev/QA và xử lý vòng lặp phản hồi.
2. **Đã tính toán độ trễ phê duyệt chưa?** Thời gian chờ khách hàng ký nháy (Sign-off) thường chiếm 20–30% tổng thời gian chu kỳ.
3. **Đã tính thời gian viết kịch bản biên và ngoại lệ chưa?** Luồng Happy Path chỉ chiếm 40% khối lượng; 60% nỗ lực còn lại nằm ở việc bóc tách các trường hợp lỗi, race condition và validation.
4. **Đã cộng buffer rủi ro bất định chưa?** Mọi ước lượng điểm đơn (Point estimate) đều tiềm ẩn sai số; luôn thể hiện dưới dạng khoảng thời gian tin cậy kèm hệ số dự phòng ($\pm 15\%$).
