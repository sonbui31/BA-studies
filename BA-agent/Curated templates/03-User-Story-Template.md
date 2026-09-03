# 3. User Story Template
*Dành cho Agile / Scrum Team — Góc nhìn người dùng (chuẩn INVEST).*

---

## 3.1 Template User Story Chuẩn

```text
Mã User Story: US-[MODULE]-[XXX]
Tiêu đề: [Tiêu đề hành động ngắn gọn]

Là một [Vai trò / Actor],
Tôi muốn [Hành động / Thao tác trên hệ thống],
Để [Giá trị nghiệp vụ / Lợi ích đạt được].

Độ ưu tiên: [Must / High / Medium / Low]
Mức độ phức tạp: [Đơn giản | Trung bình | Phức tạp]
  • Đơn giản: Thao tác đọc dữ liệu (view-only), ít logic.
  • Trung bình: Có validate form, xử lý ngoại lệ, thông báo.
  • Phức tạp: Tích hợp hệ thống ngoài, bất đồng bộ, nhiều nhánh rẽ.

Sprint: [Sprint X]
Dependencies: [Danh sách User Story phụ thuộc liên quan]
Liên kết Acceptance Criteria: [AC-xxx]

Definition of Done (DoD):
  [ ] Code đã merge vào branch chính, pass code review
  [ ] Unit test + Integration test đạt coverage >= 80%
  [ ] Toàn bộ Acceptance Criteria pass trên môi trường Staging
  [ ] API đã cập nhật vào Swagger / Postman collection
  [ ] QA sign-off, không còn bug mức Critical / Major
```

---

## 3.2 Ví dụ thực chiến

```text
Mã User Story: US-APT-021
Tiêu đề: Đặt lịch khám theo bác sĩ và khung giờ mong muốn

Là một khách hàng đã đăng nhập,
Tôi muốn chọn bác sĩ và khung giờ khám còn trống,
Để tôi chủ động sắp xếp thời gian mà không cần gọi điện chờ lễ tân xác nhận.

Độ ưu tiên: High
Mức độ phức tạp: Trung bình
Sprint: Sprint 5
Dependencies: US-AUTH-018 (Đăng nhập OTP), US-DOC-019 (Xem danh sách bác sĩ)
Liên kết Acceptance Criteria: AC-APT-021

Definition of Done (DoD):
  [ ] Code đã merge vào branch main, pass code review
  [ ] Unit test + Integration test cho FR-001 đạt coverage >= 80%
  [ ] Toàn bộ AC-APT-021 pass trên môi trường Staging
  [ ] API đã cập nhật vào Swagger / Postman collection
  [ ] QA sign-off, không còn bug mức Critical/Major
```
