# 3. User Story Template
*Dành cho Agile / Scrum Team — Góc nhìn người dùng (chuẩn INVEST).*

---

## 3.0 Thông tin chung

| Mục | Chi tiết |
|---|---|
| **Tên dự án** | [Tên dự án] |
| **Loại tài liệu** | User Stories |
| **Phiên bản** | [x.x] Draft |
| **Tác giả** | [Tên chuyên viên BA] |
| **Ngày tạo** | [DD-MM-YYYY] |
| **Nguồn gốc** | Phân rã từ BRD v[x.x] + SRS v[x.x] |

### Nhật ký thay đổi (Change Log)
| Version | Ngày | Nội dung thay đổi | Người sửa |
|---|---|---|---|
| 1.0 | [DD-MM-YYYY] | Khởi tạo User Stories từ SRS v[x.x] | [Tên BA] |

---

## 3.1 Sprint Roadmap
*Lộ trình phân bổ User Stories theo Sprint. Sắp xếp theo chiến lược: nền tảng trước → tính năng chính → tính năng nâng cao → tính năng rủi ro cao (riêng sprint để giảm impact).*

| Sprint | Chủ đề | User Stories | Tổng SP | Ghi chú chiến lược |
|---|---|---|---|---|
| **Sprint 1** | Nền tảng & Auth | US-01, US-02, US-03 | [X] SP | Ưu tiên hạ tầng xác thực, phân quyền |
| **Sprint 2** | Module lõi A | US-04, US-05, US-06 | [X] SP | Tính năng cốt lõi cho end-user |
| **Sprint 3** | Module lõi B | US-07, US-08, US-09 | [X] SP | Tính năng cốt lõi cho admin |
| **Sprint 4** | Tích hợp & Nâng cao | US-10, US-11, US-12 | [X] SP | Tích hợp hệ thống ngoài, AI/ML (tách riêng để giảm rủi ro) |
| **Sprint 5** | Tính năng bổ trợ | US-13, US-14, US-15 | [X] SP | Tính năng Should/Could |
| **Sprint 6** | Hoàn thiện & UAT | US-16, US-17 | [X] SP | Bug fix, polish, UAT |

---

## 3.2 Bảng tổng hợp User Stories
*Overview toàn bộ backlog — dùng cho Sprint Planning và Progress Tracking.*

| Mã US | Tiêu đề | Priority | Story Points | Sprint | Dependencies | Nguồn gốc FR | Trạng thái |
|---|---|---|---|---|---|---|---|
| **US-01** | [Tiêu đề ngắn gọn] | Must | [X] SP | Sprint 1 | - | FR-CC-01 | To Do |
| **US-02** | [Tiêu đề ngắn gọn] | Must | [X] SP | Sprint 1 | US-01 | FR-A01 | To Do |
| **US-03** | [Tiêu đề ngắn gọn] | Should | [X] SP | Sprint 2 | US-01 | FR-A02, FR-A03 | To Do |
| **US-04** | [Tiêu đề ngắn gọn] | Could | [X] SP | Sprint 4 | US-02, US-03 | FR-B01 | To Do |

> **Hướng dẫn Story Points:** 1 SP = task rất đơn giản (vài giờ) · 3 SP = đơn giản · 5 SP = trung bình · 8 SP = phức tạp · 13 SP = rất phức tạp (cần tách nhỏ)

---

## 3.3 Template User Story Chuẩn

```text
Mã User Story: US-[XXX]
Tiêu đề: [Tiêu đề hành động ngắn gọn]

Là một [Vai trò / Actor],
Tôi muốn [Hành động / Thao tác trên hệ thống],
Để [Giá trị nghiệp vụ / Lợi ích đạt được].

Độ ưu tiên: [Must / Should / Could / Won't]
Story Points: [1 / 2 / 3 / 5 / 8 / 13]
Mức độ phức tạp: [Đơn giản | Trung bình | Phức tạp]
  • Đơn giản: Thao tác đọc dữ liệu (view-only), ít logic.
  • Trung bình: Có validate form, xử lý ngoại lệ, thông báo.
  • Phức tạp: Tích hợp hệ thống ngoài, bất đồng bộ, nhiều nhánh rẽ.

Sprint: [Sprint X]
Nguồn gốc: [FR-xxx] (từ SRS)
Dependencies: [Danh sách User Story phụ thuộc liên quan]
Liên kết Acceptance Criteria: [AC-xxx]

Definition of Done (DoD) — Chung:
  [ ] Code đã merge vào branch chính, pass code review
  [ ] Unit test + Integration test đạt coverage >= 80%
  [ ] Toàn bộ Acceptance Criteria pass trên môi trường Staging
  [ ] API đã cập nhật vào Swagger / Postman collection
  [ ] QA sign-off, không còn bug mức Critical / Major

DoD bổ sung (nếu story phức tạp):
  [ ] [Điều kiện riêng: VD Test với 3 điều kiện ánh sáng khác nhau]
  [ ] [Điều kiện riêng: VD Load test 500 CCU đồng thời]
```

---

## 3.4 Ví dụ thực chiến

```text
Mã User Story: US-APT-021
Tiêu đề: Đặt lịch khám theo bác sĩ và khung giờ mong muốn

Là một khách hàng đã đăng nhập,
Tôi muốn chọn bác sĩ và khung giờ khám còn trống,
Để tôi chủ động sắp xếp thời gian mà không cần gọi điện chờ lễ tân xác nhận.

Độ ưu tiên: Must
Story Points: 8
Mức độ phức tạp: Phức tạp
Sprint: Sprint 2
Nguồn gốc: FR-001 (Đặt lịch khám — SRS v1.7)
Dependencies: US-AUTH-018 (Đăng nhập OTP), US-DOC-019 (Xem danh sách bác sĩ)
Liên kết Acceptance Criteria: AC-APT-021

Definition of Done (DoD) — Chung:
  [ ] Code đã merge vào branch main, pass code review
  [ ] Unit test + Integration test cho FR-001 đạt coverage >= 80%
  [ ] Toàn bộ AC-APT-021 pass trên môi trường Staging
  [ ] API đã cập nhật vào Swagger / Postman collection
  [ ] QA sign-off, không còn bug mức Critical/Major

DoD bổ sung:
  [ ] Load test: 500 user đồng thời đặt cùng 1 khung giờ, không bị double-booking
  [ ] Test race condition với 2 device cùng account
```
