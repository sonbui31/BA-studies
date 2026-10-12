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
| **Sprint 1** | Nền tảng & Auth | US-AUTH-001, US-AUTH-002, US-AUTH-003 | [X] SP | Ưu tiên hạ tầng xác thực, phân quyền |
| **Sprint 2** | Module lõi A | US-MODA-001, US-MODA-002, US-MODA-003 | [X] SP | Tính năng cốt lõi cho end-user |
| **Sprint 3** | Module lõi B | US-MODB-001, US-MODB-002, US-MODB-003 | [X] SP | Tính năng cốt lõi cho admin |
| **Sprint 4** | Tích hợp & Nâng cao | US-INT-001, US-INT-002, US-INT-003 | [X] SP | Tích hợp hệ thống ngoài, AI/ML (tách riêng để giảm rủi ro) |
| **Sprint 5** | Tính năng bổ trợ | US-SUP-001, US-SUP-002, US-SUP-003 | [X] SP | Tính năng Should/Could |
| **Sprint 6** | Hoàn thiện & UAT | US-UAT-001, US-UAT-002 | [X] SP | Bug fix, polish, UAT |

---

## 3.2 Bảng tổng hợp User Stories
*Overview toàn bộ backlog — dùng cho Sprint Planning và Progress Tracking.*

| Mã US | Tiêu đề | Priority | Story Points | Sprint | Dependencies | Nguồn gốc FR | Trạng thái |
|---|---|---|---|---|---|---|---|
| **US-AUTH-001** | [Tiêu đề ngắn gọn] | Must | [X] SP | Sprint 1 | - | FR-AUTH-001 | To Do |
| **US-AUTH-002** | [Tiêu đề ngắn gọn] | Must | [X] SP | Sprint 1 | US-AUTH-001 | FR-AUTH-002 | To Do |
| **US-MODA-001** | [Tiêu đề ngắn gọn] | Should | [X] SP | Sprint 2 | US-AUTH-001 | FR-MODA-001 | To Do |
| **US-MODB-001** | [Tiêu đề ngắn gọn] | Could | [X] SP | Sprint 4 | US-MODA-001 | FR-MODB-001 | To Do |

> **Hướng dẫn Story Points:** 1 SP = task rất đơn giản (vài giờ) · 3 SP = đơn giản · 5 SP = trung bình · 8 SP = phức tạp · 13 SP = rất phức tạp (cần tách nhỏ)

---

---

## 3.3 Template User Story Chuẩn & Tiêu chuẩn INVEST

> 🔴 **4 Input Bắt buộc trước khi viết (Cấm AI tự suy đoán):**
> 1. **Persona / Vai trò cụ thể:** Phải có trạng thái và vai trò rõ ràng (VD: *"Học viên Digital School đã đăng ký và xác thực email"*, không dùng *"User"*).
> 2. **Goal đo lường được:** Hành động thao tác cụ thể, không dùng động từ mơ hồ (`manage`, `handle`, `do` - vi phạm Điều 25 Anti-AI).
> 3. **Business Value thực tế:** Trả lời trực tiếp câu hỏi: *"Nếu không có tính năng này thì người dùng hoặc doanh nghiệp mất gì?"* (Không lặp lại nội dung của Goal).
> 4. **Ngữ cảnh / Phân hệ:** Thuộc Module nào trong SRS và quy trình To-Be nào trong BPMN.

```text
Mã User Story: US-[MODULE]-001
Tiêu đề: [Tiêu đề hành động ngắn gọn: Động từ + Danh từ]

Là một [Vai trò / Actor cụ thể kèm trạng thái],
Tôi muốn [Hành động / Thao tác đo lường được trên hệ thống],
Để [Giá trị nghiệp vụ / Lợi ích thực tế thu được].

Độ ưu tiên: [Must / Should / Could / Won't]
Story Points: [1 / 2 / 3 / 5 / 8 / 13] (Nếu > 8 SP ➔ Kích hoạt Story Splitting)
Mức độ phức tạp: [Đơn giản | Trung bình | Phức tạp]
  • Đơn giản: Thao tác đọc dữ liệu (view-only), ít logic.
  • Trung bình: Có validate form, xử lý ngoại lệ, thông báo.
  • Phức tạp: Tích hợp hệ thống ngoài, bất đồng bộ, nhiều nhánh rẽ.

Sprint: [Sprint X]
Nguồn gốc: [FR-MODULE-001] (từ SRS)
Dependencies: [Danh sách User Story phụ thuộc liên quan]
Liên kết Acceptance Criteria: [AC-MODULE-001] (Bắt buộc 4–8 kịch bản)

Bảng Kiểm tra INVEST (INVEST Self-Check Table):
| Tiêu chí | Đánh giá | Ghi chú & Hướng khắc phục (nếu chưa đạt) |
|---|:---:|---|
| **I - Independent** | [✅ / ⚠️] | Độc lập deploy/test; nếu phụ thuộc thì dùng Mock Seed Data hoặc tách story nền tảng. |
| **N - Negotiable** | [✅ / ⚠️] | Là lời mời thảo luận; không trói buộc chi tiết pixel UI hay thuật toán server. |
| **V - Valuable** | [✅ / ⚠️] | Mang lại giá trị đo lường được; phần "Để" giải quyết nỗi đau rõ ràng. |
| **E - Estimable** | [✅ / ⚠️] | Dev đủ ngữ cảnh estimate; nếu công nghệ quá mới thì tạo Spike Story trước. |
| **S - Small** | [✅ / ⚠️] | Vừa vặn trong sprint (≤ 5 ngày dev work, ≤ 8 SP); nếu lớn hơn ➔ Phải Tách Story. |
| **T - Testable** | [✅ / ⚠️] | QA viết được test case rõ ràng với số liệu định lượng, không cảm tính. |

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

### 3.3.1 Quy tắc Chặn Tách Story (Story Splitting Guardrails)

> ⚠️ **Dấu hiệu BẮT BUỘC phải Tách User Story (Split Story):**
> 1. Story có **hơn 8 kịch bản Acceptance Criteria** (quá tải cho 1 lần kiểm thử).
> 2. Đội Dev ước lượng **> 5 ngày làm việc** hoặc Story Points **> 8 SP**.
> 3. Tiêu đề chứa liên từ **"VÀ / AND"** (VD: *"Đăng ký VÀ Đăng nhập"* ➔ Bắt buộc tách đôi).
> 4. Story ôm đồm cả vòng đời **CRUD** (Tạo, Xem, Sửa, Xóa chung 1 story).
> 5. Có nhiều Persona khác nhau cùng thao tác trong 1 Story.

> 🛠️ **4 Kỹ thuật Tách Story Chuẩn:**
> - **Tách theo CRUD Operations:** Tách riêng luồng *Tạo mới (Create)* ➔ *Xem danh sách & Tìm kiếm (Read)* ➔ *Cập nhật (Update)* ➔ *Lưu trữ/Xóa (Archive/Delete)*.
> - **Tách theo Persona / Vai trò:** Tách riêng story cho *Học viên* ➔ *Mentor* ➔ *Admin/Quản trị viên*.
> - **Tách theo Quy tắc Nghiệp vụ (Business Rules):** Tách story cho *Luồng cơ bản (Happy path)* ➔ Story bổ sung cho *Luồng áp dụng mã voucher / Chiết khấu nâng cao / Phân quyền phức tạp*.
> - **Tách theo Loại Dữ liệu (Data Types):** Tách story xử lý *Dữ liệu văn bản chuẩn* ➔ Story xử lý *Tệp đính kèm lớn / Xử lý hình ảnh / Media*.

---

## 3.4 Ví dụ thực chiến

```text
Mã User Story: US-APT-021
Tiêu đề: Đặt lịch khám theo bác sĩ và khung giờ mong muốn

Là một khách hàng đã đăng nhập tài khoản,
Tôi muốn chọn bác sĩ và khung giờ khám còn trống,
Để tôi chủ động sắp xếp thời gian mà không cần gọi điện chờ lễ tân xác nhận.

Độ ưu tiên: Must
Story Points: 8
Mức độ phức tạp: Phức tạp
Sprint: Sprint 2
Nguồn gốc: FR-001 (Đặt lịch khám — SRS v1.7)
Dependencies: US-AUTH-018 (Đăng nhập OTP), US-DOC-019 (Xem danh sách bác sĩ)
Liên kết Acceptance Criteria: AC-APT-021 (Bao gồm 4 kịch bản chuẩn)

Bảng Kiểm tra INVEST:
| Tiêu chí | Đánh giá | Ghi chú |
|---|:---:|---|
| Independent | ✅ | Dùng Test Data có sẵn tài khoản và danh sách bác sĩ để test độc lập |
| Negotiable | ✅ | Chi tiết giao diện chọn giờ để mở cho UI Designer tối ưu |
| Valuable | ✅ | Giúp khách hàng giảm 100% thời gian chờ đợi qua điện thoại |
| Estimable | ✅ | Nghiệp vụ rõ ràng, dev team đã chốt giải pháp Redis Lock |
| Small | ✅ | Đạt ngưỡng 8 SP, hoàn thành trong 1 Sprint |
| Testable | ✅ | Kiểm thử thành công/thất bại bằng trạng thái booking rõ ràng |

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
