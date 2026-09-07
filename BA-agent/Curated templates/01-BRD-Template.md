# 1. BRD — Business Requirements Document
*Dành cho Khách hàng & Stakeholders — 100% ngôn ngữ nghiệp vụ, CẤM thuật ngữ kỹ thuật.*

---

## 1.1 Thông tin chung

| Mục | Chi tiết |
|---|---|
| **Tên dự án** | [Tên dự án] |
| **Loại tài liệu** | Business Requirements Document (BRD) |
| **Phiên bản** | [x.x] Draft |
| **Tác giả** | [Tên chuyên viên BA] |
| **Business Owner** | [Tên & chức vụ người chủ quản nghiệp vụ] |
| **Ngày tạo** | [DD-MM-YYYY] |

### Nhật ký thay đổi (Change Log)
| Version | Ngày | Nội dung thay đổi | Người sửa |
|---|---|---|---|
| 0.1 | [DD-MM-YYYY] | Bản BRD draft ban đầu | [Tên BA] |

---

## 1.2 Bối cảnh & Mục tiêu kinh doanh

- **Bối cảnh (Background / Pain points):**
  - [Mô tả hiện trạng và vấn đề đang gặp phải của doanh nghiệp/người dùng]
- **Mục tiêu kinh doanh (Business Objectives):**
  - [Mục tiêu 1: Cụ thể, định lượng được]
  - [Mục tiêu 2: Cụ thể, định lượng được]

---

## 1.3 Phạm vi (Scope)

- **Trong phạm vi (In-scope):**
  - [Tính năng / Nghiệp vụ 1]
  - [Tính năng / Nghiệp vụ 2]
- **Ngoài phạm vi (Out-of-scope):**
  - [Hạng mục không làm hoặc chuyển giai đoạn 2]

---

## 1.4 Stakeholders

| Vai trò | Tên / Bộ phận | Trách nhiệm chính |
|---|---|---|
| **Sponsor** | [Tên] | Duyệt ngân sách, mục tiêu kinh doanh |
| **Business Owner** | [Tên] | Xác nhận quy trình nghiệp vụ |
| **End-User Representative** | [Tên/Nhóm] | Góp ý trải nghiệm thực tế |
| **Tech Lead / PM** | [Tên] | Đánh giá tính khả thi và kế hoạch |

### Ma trận RACI — Vận hành nghiệp vụ
*Phân quyền trách nhiệm cho các hoạt động nghiệp vụ hàng ngày.*

| Hoạt động nghiệp vụ | Sponsor | Business Owner | End-User | Tech Lead |
|---|---|---|---|---|
| [Hoạt động 1: VD Tiếp nhận yêu cầu] | I | A | R | C |
| [Hoạt động 2: VD Phê duyệt quy trình] | A | R | I | C |
| [Hoạt động 3: VD Vận hành hàng ngày] | I | C | R | I |

### Ma trận RACI — Hoạt động dự án
*Phân quyền trách nhiệm cho các hoạt động triển khai dự án.*

| Hoạt động dự án | Sponsor | Business Owner | BA | Dev Lead | QA Lead |
|---|---|---|---|---|---|
| Phê duyệt BRD / SRS | A | R | R | C | I |
| Thiết kế UI/UX | I | C | R | C | I |
| Phát triển & Code review | I | I | C | A/R | C |
| UAT & Nghiệm thu | A | R | R | C | R |
| Go-live & Deployment | A | I | I | R | R |

> **Chú thích:** R = Responsible (Thực hiện) · A = Accountable (Chịu trách nhiệm) · C = Consulted (Tham vấn) · I = Informed (Được thông báo)

---

## 1.5 Yêu cầu nghiệp vụ (Business Requirements — BR)

| Mã YC | Mô tả yêu cầu nghiệp vụ | Độ ưu tiên (MoSCoW) | Ghi chú |
|---|---|---|---|
| **BR-001** | [Yêu cầu nghiệp vụ 1] | Must | [Ghi chú nếu có] |
| **BR-002** | [Yêu cầu nghiệp vụ 2] | Must | - |
| **BR-003** | [Yêu cầu nghiệp vụ 3] | Should | - |
| **BR-004** | [Yêu cầu nghiệp vụ 4] | Could | - |

---

## 1.6 Yêu cầu các bên liên quan (Stakeholder Requirements — SR)
*Phân tầng theo chuẩn BABOK: BR (mục tiêu kinh doanh) → SR (nhu cầu cụ thể từ từng nhóm stakeholder).*

| Mã SR | Stakeholder | Nhu cầu (viết theo giọng "Cần…" / "Muốn…") | MoSCoW | BR liên quan |
|---|---|---|---|---|
| **SR-01** | [Nhóm stakeholder 1] | Cần [nhu cầu cụ thể] | Must | BR-001 |
| **SR-02** | [Nhóm stakeholder 1] | Muốn [nhu cầu cụ thể] | Should | BR-001 |
| **SR-03** | [Nhóm stakeholder 2] | Cần [nhu cầu cụ thể] | Must | BR-002 |
| **SR-04** | [Nhóm stakeholder 2] | Muốn [nhu cầu cụ thể] | Could | BR-003 |

---

## 1.7 Luật nghiệp vụ (Business Rules)
*Tách riêng với BR/SR để không lẫn với chức năng hệ thống.*

| Mã Rule | Nội dung luật vận hành / Ràng buộc chính sách |
|---|---|
| **BRULE-01** | [Nội dung luật 1: VD Một khung giờ chỉ được gán cho đúng 1 lịch hẹn] |
| **BRULE-02** | [Nội dung luật 2: VD Giữ chỗ tạm thời tối đa 5 phút] |
| **BRULE-03** | [Nội dung luật 3: VD Chỉ được hủy/đổi lịch trước giờ hẹn tối thiểu 2 giờ] |
| **BRULE-04** | [Nội dung luật 4: VD Tối đa 3 lịch hẹn đang chờ khám cùng lúc] |

---

## 1.8 Quy trình nghiệp vụ (As-Is / To-Be)

### As-Is (Hiện tại)
- [Mô tả quy trình thủ công hiện tại và các điểm nghẽn]

### To-Be (Đề xuất)
- [Mô tả quy trình mới được tối ưu hóa]
- *(Chèn sơ đồ Context Diagram hoặc Activity / Swimlane Diagram)*

---

## 1.9 Ràng buộc & Giả định

- **Ràng buộc:** [Ngân sách, thời hạn hoàn thành, quy định pháp lý]
- **Giả định:** [Các điều kiện giả định cần các bên xác nhận]

---

## 1.10 Rủi ro & Giải pháp

| Rủi ro | Mức độ ảnh hưởng (Cao / TB / Thấp) | Giải pháp giảm thiểu |
|---|---|---|
| [Rủi ro 1: Thay đổi thói quen người dùng] | Cao | [Đào tạo, duy trì song song kênh cũ 1 thời gian] |
| [Rủi ro 2: Tiến độ tích hợp bên thứ ba] | Trung bình | [Chốt hợp đồng SLA sớm từ đầu dự án] |

---

## 1.11 Tiêu chí thành công (KPI)

- [Chỉ số 1: Giảm 50% thời gian xử lý thủ công]
- [Chỉ số 2: Tăng 20% mức độ hài lòng của khách hàng]

---

## 1.12 Ma trận vây vết (BR ↔ SR Traceability)
*Đảm bảo mỗi BR được phủ bởi ít nhất 1 SR, và mỗi SR đều truy ngược về BR.*

| Mã BR | Mã SR liên quan | Trạng thái phủ |
|---|---|---|
| **BR-001** | SR-01, SR-02 | ✅ Đã phủ |
| **BR-002** | SR-03 | ✅ Đã phủ |
| **BR-003** | SR-04 | ✅ Đã phủ |
| **BR-004** | *(chưa có SR)* | ⚠️ Cần bổ sung |

---

## 1.13 Từ điển thuật ngữ nghiệp vụ
*Giải thích các thuật ngữ chuyên ngành (domain-specific) — KHÔNG phải thuật ngữ kỹ thuật.*

| Thuật ngữ | Giải thích |
|---|---|
| [Thuật ngữ 1] | [Định nghĩa rõ ràng trong ngữ cảnh dự án] |
| [Thuật ngữ 2] | [Định nghĩa rõ ràng trong ngữ cảnh dự án] |

---

## 1.14 Phê duyệt (Sign-off)

| Vai trò | Người phê duyệt | Ngày duyệt | Trạng thái |
|---|---|---|---|
| **Sponsor** | [Tên] | [DD/MM/YYYY] | Đã duyệt / Chờ duyệt |
| **Business Owner** | [Tên] | [DD/MM/YYYY] | Đã duyệt / Chờ duyệt |
