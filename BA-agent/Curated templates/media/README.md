# Thư mục Media — Curated Templates (Parent App)

Thư mục này chứa toàn bộ hình ảnh sơ đồ thực tế trích xuất và chuẩn hóa từ bộ tài liệu **Parent Mobile App (BRD v1.0, SRS v1.7, User Story v1.2, AC v1.2)**.

---

## 1. Bộ 6 ảnh Template (Thay thế trực tiếp bộ ảnh cũ)

Các ảnh này giữ nguyên tên file gốc để bảo đảm tính tương thích với các tài liệu markdown/Word tham chiếu:

| Tên file                                                      | Loại sơ đồ        | Tên / Mô tả sơ đồ trong Parent App                                                                                    | Ánh xạ mục tài liệu             |
| ------------------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done_image_01.png` | Flowchart / BPMN  | **Quy trình Xin nghỉ học (To-Be)**                                                                                    | BRD Mục 7.2 (Sơ đồ BPMN)        |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done_image_02.png` | UML Use Case      | **Use Case Diagram tổng quan hệ thống Parent App**                                                                    | SRS Mục 3.1 (Hình 1)            |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done_image_03.png` | Detailed Use Case | **Use Case chi tiết phân hệ Điểm danh** (include/extend: Quét khuôn mặt, GPS, Thông báo, Điểm danh thủ công, Consent) | SRS Mục 3.2 (Hình 2)            |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done_image_04.png` | ERD / Data Model  | **Mô hình thực thể quan hệ Parent App** (HocSinh, PhuHuynh, GiaoVien, LopHoc, DiemDanh, DonXinNghi, HocPhi)           | SRS Mục 6 (Data Requirements)   |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done_image_05.png` | UI Wireframe      | **Màn hình thông báo & thống kê điểm danh di động**                                                                   | SRS Mục 4.4 (FR-04.2 / FR-04.3) |
| `Template-tai-lieu-BA-BRD-SRS-UserStory-AC_done_image_06.png` | Package Use Case  | **Module/Package Use Case Diagram** (Gói Theo dõi học tập, Gói Tương tác, Gói Vận hành trường)                        | SRS Mục 3 & Phụ lục             |

---

## 2. Bộ ảnh chi tiết bổ sung từ SRS & BRD

| Tên file                               | Loại sơ đồ       | Chi tiết nghiệp vụ                                                                                         | Vị trí trong Docs    |
| -------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------- | -------------------- |
| `BRD_BPMN_XinNghi_ToBe.jpg`            | BPMN / Flowchart | Quy trình phụ huynh gửi đơn xin nghỉ → hệ thống validate → giáo viên duyệt/từ chối → thông báo phụ huynh   | BRD Mục 7.2          |
| `SRS_Hinh1_UseCase_TongQuan.jpg`       | Use Case Diagram | Use Case tổng quan phân rã theo 3 Actor chính: Phụ huynh, Giáo viên, School Admin                          | SRS Mục 3.1 (Hình 1) |
| `SRS_Hinh3_UseCase_XinNghi.jpg`        | Use Case Diagram | Use Case chi tiết phân hệ Xin nghỉ (Validate, Duyệt, Báo kết quả)                                          | SRS Mục 3.3 (Hình 3) |
| `SRS_Hinh4_Activity_DiemDanh.jpg`      | Activity Diagram | Sơ đồ hoạt động quy trình điểm danh có rẽ nhánh Consent & kiểm tra ngưỡng nhận diện khuôn mặt              | SRS Mục 3.4 (Hình 4) |
| `SRS_Hinh6_Activity_DangKyKhoaHoc.jpg` | Activity Diagram | Luồng đăng ký khóa học: kiểm tra slot (DB transaction), xử lý race condition, duyệt qua Vclassio           | SRS Mục 3.6 (Hình 6) |
| `SRS_Hinh6_Sequence_XinNghi.jpg`       | Sequence Diagram | Tuần tự tương tác 4 đối tượng: Phụ huynh App, Backend API, Database, Push Notification khi tạo & duyệt đơn | SRS Mục 3.7 (Hình 6) |
| `SRS_Hinh7_Sequence_DiemDanh.jpg`      | Sequence Diagram | Tuần tự tương tác: Giáo viên App, Backend API, Face Recognition AI, Database, Push Notification            | SRS Mục 3.8 (Hình 7) |
