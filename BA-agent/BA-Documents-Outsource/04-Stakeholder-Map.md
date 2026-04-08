# STAKEHOLDER MAP — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026

---

## 1. Đặc thù Outsource

| Yếu tố | Nội bộ | Gia công |
|---------|--------|----------|
| Stakeholder | 1 tổ chức | **2 tổ chức** (KH + NCC) |
| Giao tiếp | Trực tiếp | Từ xa, lệch múi giờ |
| Quyền quyết định | Người đại diện KH quyết nhanh | Cần **phê duyệt chính thức** |
| Báo cáo cấp trên | Nội bộ | Qua **lộ trình báo cáo cấp trên liên tổ chức** |

---

## 2. Danh sách stakeholder

### 2.1 Phía Khách hàng

| # | Tên | Vai trò | Quyền lực | Quan tâm | Chiến lược |
|---|-----|---------|-----------|----------|-----------|
| 1 | [Tên] | Nhà tài trợ (Sponsor) | 🔴 Cao | 🟡 Trung bình | Quản lý chặt — Báo cáo tiến độ, lợi ích đầu tư |
| 2 | [Tên] | Người đại diện KH (Product Owner) | 🔴 Cao | 🔴 Cao | **Đối tác chính** — Giao tiếp hàng ngày |
| 3 | [Tên] | Chuyên gia nghiệp vụ (SME) | 🟡 Trung bình | 🔴 Cao | Hợp tác chặt — Phụ thuộc kiến thức |
| 4 | [Tên] | Đầu mối CNTT | 🟠 Trung bình | 🟠 Trung bình | Giữ thông tin — API, hạ tầng |
| 5 | [Tên] | Người dùng cuối | 🟢 Thấp | 🔴 Cao | Giữ hài lòng — Nghiệm thu, phản hồi |
| 6 | [Tên] | Tài chính/Mua sắm | 🟠 Trung bình | 🟢 Thấp | Theo dõi — Hóa đơn, mốc thanh toán |

### 2.2 Phía Nhà cung cấp

| # | Tên | Vai trò | Quyền lực | Quan tâm | Trách nhiệm chính |
|---|-----|---------|-----------|----------|-------------------|
| 1 | [Tên] | Quản lý dự án (PM) | 🔴 Cao | 🔴 Cao | Tiến độ, ngân sách, giao tiếp KH |
| 2 | [Tên] | Trưởng nhóm Phân tích (BA Lead) | 🟠 TB | 🔴 Cao | Yêu cầu, tài liệu, tham vấn KH |
| 3 | [Tên] | Trưởng nhóm Kỹ thuật (Tech Lead) | 🟠 TB | 🟠 TB | Kiến trúc, rà soát mã nguồn |
| 4 | [Tên] | Quản lý tài khoản | 🔴 Cao | 🟡 TB | Báo cáo cấp trên, quan hệ thương mại |

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
| Video Call | Đúng giờ | PM → QĐ tài khoản |

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
