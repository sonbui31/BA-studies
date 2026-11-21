# CHỐT THEO LÁT CẮT (SLICE BASELINING)

> **Vấn đề:** Chuỗi "BRD chốt hết rồi mới viết SRS, SRS xong mới viết Story" bắt cả dự án chờ phần chậm nhất. Trong thực tế, viết SRS thường làm lộ lỗi của BRD, và đội phát triển cần bắt đầu khi một phần đã rõ.
> **Cách làm:** Chốt theo **lát cắt dọc** (một luồng nghiệp vụ hoặc module, đủ BRQ → FR → US → AC) thay vì chốt theo **loại tài liệu**. Các Hard Gate vẫn giữ nguyên, nhưng áp dụng cho từng lát cắt.
> **Áp dụng:** Lối L4 (`intake-triage.md`), Tier 2–3. Tier 1 thường đi Agile Lite nên không cần.

---

## 1. Lát cắt là gì

Một lát cắt là phần nhỏ nhất **giao được và nghiệm thu được độc lập**:

- Một luồng nghiệp vụ end-to-end ("Điều chuyển tài sản giữa hai khoa") hoặc một module ("Kiểm kê").
- Có đủ: BRQ liên quan, business rule (BR) và Gateway của luồng, FR/NFR, User Story, AC/TC, dữ liệu và tích hợp mà luồng chạm tới.
- Có người chốt rõ ràng (chủ quy trình hoặc PO của phần đó).

Không phải lát cắt: "toàn bộ phần màn hình", "tất cả API", "các NFR". Đó là lát ngang; chốt theo lát ngang không giúp giao sớm.

---

## 2. Nền chung phải chốt trước mọi lát cắt

Lát cắt chỉ được bắt đầu khi **nền chung** của BRD đã được xác nhận:

1. Problem Statement, mục tiêu kinh doanh và KPI chính.
2. Phạm vi tổng (In/Out) và danh sách lát cắt dự kiến.
3. Stakeholder Map và người ra quyết định.
4. BPMN tổng quan (Level 0–1) thể hiện các lát cắt nằm ở đâu trong quy trình.
5. Quy tắc dùng chung cho nhiều lát cắt (phân quyền, trạng thái dùng chung, dữ liệu master).

Với **dự án outsource giá cố định**, phạm vi hợp đồng vẫn là toàn bộ BRD đã ký. Chốt theo lát cắt chỉ áp dụng cho phần chi tiết (SRS, Story, AC) bên trong phạm vi đó.

---

## 3. Hard Gate áp dụng theo lát cắt

| Gate | Áp dụng cho lát cắt A nghĩa là |
|---|---|
| Gate 1 (BRD) | Nền chung đã chốt + phần BRD của lát A (BRQ, BR, As-Is/To-Be của luồng A) đã được xác nhận |
| Gate 2 (SRS) | Viết SRS cho lát A khi phần BRD của A đã chốt; không chờ lát B |
| Gate 3, 4 (Story, AC) | Không còn `[CẦN XÁC NHẬN]` trong BPMN **của luồng A** |
| Gate 7 (nguồn) | Nhận định trọng yếu **của lát A** có nguồn trực tiếp (`evidence-source-gate.md`) |

Lát B còn mở không chặn lát A, trừ khi A phụ thuộc vào quyết định của B (khi đó ghi phụ thuộc trong Sổ lát cắt và chờ).

---

## 4. Sổ lát cắt (Slice Register)

Đặt trong BRD, ngay sau phần Phạm vi:

| Lát cắt | Phạm vi | BRQ / BR | BRD | SRS | Story | AC | Phụ thuộc | Người chốt | Ngày chốt |
|---|---|---|---|---|---|---|---|---|---|
| S1 — Đăng ký tài sản | Tạo, sửa, tra cứu hồ sơ tài sản | BRQ-01, BRQ-02; BR-001 | Đã chốt | Đã chốt | Đã chốt | Đang viết | — | Trưởng phòng Vật tư | 05/03/2026 |
| S2 — Điều chuyển | Điều chuyển và bàn giao giữa khoa | BRQ-03; BR-002, BR-003 | Đã chốt | Đang viết | — | — | Hạn mức duyệt (BR-002) | Giám đốc vận hành | — |

Trạng thái: `Chưa bắt đầu` · `Đang viết` · `Chờ xác nhận` · `Đã chốt` · `Cần cập nhật` (khi lát khác thay đổi phần dùng chung).

---

## 5. Thay đổi lan sang lát đã chốt

- Khi viết lát B mà phải đổi quy tắc, dữ liệu hoặc trạng thái dùng chung: đánh dấu các lát đã chốt bị ảnh hưởng là `Cần cập nhật`, cập nhật ngược về BRD (Reverse Sync), ghi Change Log, và báo người chốt của lát đó.
- Sau baseline hợp đồng, thay đổi phạm vi đi qua Change Request như bình thường.
- Chạy `traceability_scan.py` trên toàn bộ thư mục sau mỗi lần chốt một lát cắt, để chắc lát mới không làm gãy chuỗi của lát cũ.

---

## 6. Khi nào không nên chốt theo lát cắt

- Các lát cắt dùng chung quá nhiều quy tắc chưa rõ, tách ra chỉ tạo thêm vòng sửa: chốt nền chung trước, rồi chốt theo tài liệu.
- Hợp đồng hoặc cơ quan quản lý yêu cầu nộp và duyệt trọn bộ tài liệu một lần (một số dự án nhà nước): viết theo lát cắt cho nhanh, nhưng trình duyệt trọn bộ.
