# STAKEHOLDER MAP — DỰ ÁN OUTSOURCE
# Dự án Hệ thống Quản lý Tài sản Bệnh viện

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Người chịu trách nhiệm:** Nguyễn Văn A — BA Lead, Nhà cung cấp
> **Khách hàng:** Bệnh viện Đa khoa An Phúc | **Nhà cung cấp:** Công ty Giải pháp Số Sao Việt
> **Nguồn:** `02-BRD.md` mục 5.1 và Sổ nguồn mục 5.2
> **Nhãn:** [TÀI LIỆU MẪU] — tên người là dữ liệu minh họa, không phải dự án thật

---

## 1. Đặc thù Outsource

| Yếu tố | Nội bộ | Gia công |
|---------|--------|----------|
| Stakeholder | 1 tổ chức | **2 tổ chức** (KH + NCC) |
| Giao tiếp | Trực tiếp | Từ xa (NCC ở Hà Nội, bệnh viện ở TP.HCM), họp video theo lịch |
| Quyền quyết định | Người đại diện KH quyết nhanh | Cần **phê duyệt chính thức** |
| Báo cáo cấp trên | Nội bộ | Qua **lộ trình báo cáo cấp trên liên tổ chức** |

---

## 2. Danh sách stakeholder

### 2.1. Phía Khách hàng

| # | Tên | Vai trò | Quyền lực | Quan tâm | Chiến lược |
|---|-----|---------|-----------|----------|-----------|
| 1 | Trần Minh Đức — Giám đốc vận hành | Nhà tài trợ (Sponsor); duyệt bước hai điều chuyển tài sản từ 50 triệu VND (BR-006) | 🔴 Cao | 🟡 Trung bình | Quản lý chặt — Báo cáo tiến độ, lợi ích đầu tư |
| 2 | Phạm Thu Hà — Trưởng phòng Vật tư | Người đại diện KH (Product Owner); duyệt điều chuyển, khóa sổ kiểm kê, duyệt chi phí bảo trì trên 20 triệu VND | 🔴 Cao | 🔴 Cao | **Đối tác chính** — Giao tiếp hàng ngày |
| 3 | Đặng Văn Hùng — Kỹ sư thiết bị y tế | Chuyên gia nghiệp vụ (SME) bảo trì, SRC-03 | 🟡 Trung bình | 🔴 Cao | Hợp tác chặt — Phụ thuộc kiến thức về chu kỳ bảo trì |
| 4 | Vũ Hoàng Nam — Trưởng phòng CNTT | Đầu mối CNTT, giám sát kỹ thuật | 🟠 Trung bình | 🟠 Trung bình | Giữ thông tin — SSO, VPN, máy in barcode |
| 5 | Nhân viên Vật tư (3 người), Trưởng khoa và Điều dưỡng trưởng 18 khoa | Người dùng cuối | 🟢 Thấp | 🔴 Cao | Giữ hài lòng — Nghiệm thu, phản hồi |
| 6 | Lê Quốc Bảo — Phó phòng Tài chính kế toán | Tài chính/Mua sắm, Kế toán tài sản | 🟠 Trung bình | 🟢 Thấp | Theo dõi — Hóa đơn, mốc thanh toán |
| 7 | Ngô Thị Lan — Trưởng ban Kiểm soát nội bộ | Stakeholder audit | 🟠 Trung bình | 🟠 Trung bình | Giữ thông tin — Log bàn giao, retention 5 năm |

### 2.2. Phía Nhà cung cấp

| # | Tên | Vai trò | Quyền lực | Quan tâm | Trách nhiệm chính |
|---|-----|---------|-----------|----------|-------------------|
| 1 | Đỗ Thanh Tùng | Quản lý dự án (PM) | 🔴 Cao | 🔴 Cao | Tiến độ, ngân sách, giao tiếp KH |
| 2 | Nguyễn Văn A | Trưởng nhóm Phân tích (BA Lead) | 🟠 TB | 🔴 Cao | Yêu cầu, tài liệu, tham vấn KH |
| 3 | Hoàng Gia Khánh | Trưởng nhóm Kỹ thuật (Tech Lead) | 🟠 TB | 🟠 TB | Kiến trúc, rà soát mã nguồn |
| 4 | Trịnh Thu Trang | Trưởng nhóm Kiểm thử (QC Lead) | 🟡 Thấp | 🟠 TB | Kịch bản UAT, hỗ trợ nghiệm thu |
| 5 | Bùi Minh Châu | Quản lý tài khoản | 🔴 Cao | 🟡 TB | Báo cáo cấp trên, quan hệ thương mại |

### 2.3. Vai trò trong quy trình (tên làn trong sơ đồ BPMN)

Các làn trong `02-BRD.md` mục 6 và `04-Process-Flow.md` dùng đúng các tên dưới đây. "Khoa giao" và "Khoa nhận" là vai trò theo từng yêu cầu điều chuyển, không phải một khoa cố định.

| Tên làn | Ai đảm nhận | Quy trình | Quyền chính |
|---|---|---|---|
| Khoa giao | Người dùng khoa đang sở hữu tài sản (thường là Điều dưỡng trưởng) | P1 | Tạo yêu cầu điều chuyển (FR-TRF-001), xác nhận đã giao (FR-TRF-002) |
| Khoa nhận | Trưởng khoa hoặc Điều dưỡng trưởng của khoa nhận tài sản | P1 | Kiểm tra tình trạng, xác nhận hoặc từ chối nhận (FR-TRF-002) |
| Khoa sử dụng | Các khoa đang giữ tài sản | Tổng quan | Sử dụng tài sản, phát sinh yêu cầu điều chuyển |
| Trưởng khoa | Trưởng khoa của khoa được kiểm kê | P2 | Xác nhận hoặc phản đối kết quả kiểm kê (FR-INV-001) |
| Nhân viên Vật tư | 3 nhân viên Phòng Vật tư | P2, P3 | Mở đợt và quét kiểm kê (FR-INV-001), lên lịch bảo trì (FR-MNT-001) |
| Phòng Vật tư | Nhân viên Vật tư và Trưởng phòng Vật tư, dùng ở sơ đồ tổng quan | Tổng quan | Tạo hồ sơ, bàn giao, kiểm kê, ghi trạng thái thanh lý |
| Trưởng phòng Vật tư | Phạm Thu Hà hoặc người được ủy quyền | P1, P2, P3 | Duyệt điều chuyển (FR-TRF-003), khóa sổ kiểm kê, duyệt chi phí bảo trì trên 20 triệu VND (FR-MNT-002) |
| Giám đốc vận hành | Trần Minh Đức | P1 | Duyệt bước hai cho tài sản từ 50 triệu VND (BR-006) |
| Kỹ sư thiết bị y tế | Đặng Văn Hùng và 2 kỹ sư của Tổ thiết bị | P3 | Bảo trì thiết bị, ghi kết quả và chi phí (FR-MNT-002) |
| Hệ thống quản lý tài sản | Bước tự động | P1, P2, P3 | Kiểm tra quy tắc, cảnh báo, ghi lịch sử |

---

## 3. Lưới Quyền lực / Mức quan tâm

```
    Quyền lực CAO  │  Giữ hài lòng         │  Quản lý chặt chẽ
                    |  (Nhà tài trợ KH,   |  (PO KH, PM NCC,
                    |   QĐ tài khoản NCC)   |   BA Lead)
                    │                        │
    ────────────────┼────────────────────────┼──────────────────
                    │                        │
    Quyền lực THẤP │  Theo dõi              │  Giữ thông tin
                    |  (Tài chính, Pháp lý)  |  (Chuyên gia NV, Người dùng,
                    |                        |   Đội Dev)
                    │                        │
                    └────────── Mức quan tâm ─────────── CAO
```

---

## 4. Ma trận giao tiếp

| Người nhận | Kênh | Tần suất | Nội dung | Người gửi |
|-----------|------|----------|---------|-----------|
| Người đại diện KH (PO) | Video Call | 2 lần/tuần | Đồng bộ yêu cầu, làm rõ | BA NCC |
| Nhà tài trợ KH | Email | 2 tuần/lần | Báo cáo tiến độ, rủi ro | PM NCC |
| Nhà tài trợ KH | Video Call | Hàng tháng | Xem xét dự án cấp điều hành | PM NCC |
| Chuyên gia NV (SME) KH | Slack/Teams | Khi cần | Câu hỏi nghiệp vụ | BA NCC |
| CNTT KH | Email/Jira | Khi cần | Vấn đề API, hạ tầng | Dev NCC |
| Toàn bộ stakeholder | Email | Mỗi Sprint | Báo cáo Sprint | PM NCC |
| Người dùng cuối | Demo | Mỗi phiên bản | Demo Sprint, phản hồi UAT | BA + Dev NCC |

### SLA phản hồi

| Kênh | Thời gian phản hồi | Báo cáo cấp trên nếu quá hạn |
|------|--------------------|----------------------|
| Email | 24 giờ (ngày làm việc) | PM → PM |
| Slack/Teams | 4 giờ (giờ hành chính) | BA → PM |
| Jira | 24 giờ (ngày làm việc) | BA → PM |
| Video Call | Đúng giờ | PM → Quản lý tài khoản |

---

## 5. Lộ trình báo cáo cấp trên (Escalation Path)

```
Cấp 1: BA (NCC) ↔ Người đại diện KH (PO)     — Vấn đề yêu cầu/kỹ thuật
          ↓ nếu không giải quyết trong 2 ngày
Cấp 2: PM (NCC) ↔ PM/Quản lý (KH)      — Vấn đề quy trình/tiến độ
          ↓ nếu không giải quyết trong 3 ngày
Cấp 3: QĐ tài khoản (NCC) ↔ Nhà tài trợ (KH) — Vấn đề thương mại
          ↓ nếu không giải quyết trong 5 ngày
Cấp 4: Pháp lý (NCC) ↔ Pháp lý (KH)    — Tham chiếu hợp đồng
```

---

## 6. Ma trận sẵn sàng của Khách hàng

> ⚠️ **Đặc thù outsource:** NCC **phụ thuộc** vào sự sẵn sàng của KH.
> Nếu KH không phản hồi đúng hạn → dự án bị trì hoãn → **KHÔNG phải lỗi NCC.**

| Vai trò KH | Sẵn sàng tối thiểu | Nếu KHÔNG sẵn sàng |
|-----------|-------------------|-------------------|
| Người đại diện KH (PO) | ≥ 4 giờ/ngày | ⚠️ Trì hoãn quyết định → ảnh hưởng tiến độ giai đoạn |
| Chuyên gia nghiệp vụ (SME) | 2-3 giờ/tuần | ⚠️ Trì hoãn phân tích → yêu cầu không chính xác |
| CNTT | Phản hồi trong 48 giờ | ⚠️ Chặn tích hợp, triển khai |
| Nhà tài trợ (Sponsor) | 2 giờ/2 tuần | ⚠️ Trì hoãn phê duyệt → chặn mốc thanh toán |

> **Quy tắc:** Ghi rõ SLA sẵn sàng của KH trong hợp đồng. Trì hoãn từ phía KH = gia hạn tiến độ tương ứng.
