# STAKEHOLDER MAP — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026

---

## 1. Đặc thù Outsource

| Yếu tố | Nội bộ | Gia công |
|---------|--------|----------|
| Stakeholder | 1 tổ chức | **2 tổ chức** (KH + NCC) |
| Giao tiếp | Trực tiếp | Từ xa, lệch múi giờ |
| Quyền quyết định | PO quyết nhanh | Cần **sign-off chính thức** |
| Escalation | Nội bộ | Qua **escalation path liên tổ chức** |

---

## 2. Danh sách stakeholder

### 2.1 Phía Khách hàng

| # | Tên | Vai trò | Quyền lực | Quan tâm | Chiến lược |
|---|-----|---------|-----------|----------|-----------|
| 1 | [Tên] | Sponsor | 🔴 Cao | 🟡 Trung bình | Quản lý chặt — Báo cáo tiến độ, ROI |
| 2 | [Tên] | Product Owner (PO) | 🔴 Cao | 🔴 Cao | **Đối tác chính** — Giao tiếp hàng ngày |
| 3 | [Tên] | SME (SME) | 🟡 Trung bình | 🔴 Cao | Hợp tác chặt — Phụ thuộc kiến thức |
| 4 | [Tên] | Đầu mối CNTT | 🟠 Trung bình | 🟠 Trung bình | Giữ thông tin — API, hạ tầng |
| 5 | [Tên] | Người dùng cuối | 🟢 Thấp | 🔴 Cao | Giữ hài lòng — UAT, phản hồi |
| 6 | [Tên] | Tài chính/Mua sắm | 🟠 Trung bình | 🟢 Thấp | Theo dõi — Hóa đơn, payment milestone |

### 2.2 Phía Nhà cung cấp

| # | Tên | Vai trò | Quyền lực | Quan tâm | Trách nhiệm chính |
|---|-----|---------|-----------|----------|-------------------|
| 1 | [Tên] | Project Manager | 🔴 Cao | 🔴 Cao | Tiến độ, ngân sách, giao tiếp KH |
| 2 | [Tên] | BA Lead | 🟠 TB | 🔴 Cao | Yêu cầu, tài liệu, tham vấn KH |
| 3 | [Tên] | Tech Lead | 🟠 TB | 🟠 TB | Kiến trúc, rà soát mã nguồn |
| 4 | [Tên] | Quản lý tài khoản | 🔴 Cao | 🟡 TB | Escalation, quan hệ thương mại |

---

## 3. Lưới Quyền lực / Mức quan tâm

```
    Quyền lực CAO  │  Giữ hài lòng         │  Quản lý chặt chẽ
                    │  (Sponsor KH,   │  (PO KH, PM NCC,
                    │   QĐ tài khoản NCC)   │   BA Lead)
                    │                        │
    ────────────────┼────────────────────────┼──────────────────
                    │                        │
    Quyền lực THẤP │  Theo dõi              │  Giữ thông tin
                    │  (Tài chính, Pháp lý)  │  (SME, Người dùng,
                    │                        │   Đội Dev)
                    │                        │
                    └────────── Mức quan tâm ─────────── CAO
```

---

## 4. Ma trận giao tiếp

| Người nhận | Kênh | Tần suất | Nội dung | Người gửi |
|-----------|------|----------|---------|-----------|
| PO KH | Video Call | 2 lần/tuần | Đồng bộ yêu cầu, làm rõ | BA NCC |
| Sponsor KH | Email | 2 tuần/lần | Báo cáo tiến độ, rủi ro | PM NCC |
| Sponsor KH | Video Call | Hàng tháng | Xem xét dự án cấp điều hành | PM NCC |
| SME KH | Slack/Teams | Khi cần | Câu hỏi nghiệp vụ | BA NCC |
| CNTT KH | Email/Jira | Khi cần | Vấn đề API, hạ tầng | Dev NCC |
| Toàn bộ stakeholder | Email | Mỗi Sprint | Báo cáo Sprint | PM NCC |
| Người dùng cuối | Demo | Mỗi phiên bản | Demo Sprint, phản hồi UAT | BA + Dev NCC |

### SLA phản hồi

| Kênh | Thời gian phản hồi | Escalation nếu quá hạn |
|------|--------------------|----------------------|
| Email | 24 giờ (ngày làm việc) | PM → PM |
| Slack/Teams | 4 giờ (giờ hành chính) | BA → PM |
| Jira | 24 giờ (ngày làm việc) | BA → PM |
| Video Call | Đúng giờ | PM → QĐ tài khoản |

---

## 5. Escalation Path

```
Cấp 1: BA (NCC) ↔ PO (KH)              — Vấn đề yêu cầu/kỹ thuật
          ↓ nếu không giải quyết trong 2 ngày
Cấp 2: PM (NCC) ↔ PM/Quản lý (KH)      — Vấn đề quy trình/tiến độ
          ↓ nếu không giải quyết trong 3 ngày
Cấp 3: QĐ tài khoản (NCC) ↔ Sponsor (KH) — Vấn đề thương mại
          ↓ nếu không giải quyết trong 5 ngày
Cấp 4: Pháp lý (NCC) ↔ Pháp lý (KH)    — Tham chiếu hợp đồng
```

---

## 6. Ma trận sẵn sàng của Khách hàng

> ⚠️ **Đặc thù outsource:** NCC **phụ thuộc** vào sự sẵn sàng của KH.
> Nếu KH không phản hồi đúng hạn → dự án bị trì hoãn → **KHÔNG phải lỗi NCC.**

| Vai trò KH | Sẵn sàng tối thiểu | Nếu KHÔNG sẵn sàng |
|-----------|-------------------|-------------------|
| PO | ≥ 4 giờ/ngày | ⚠️ Trì hoãn quyết định → ảnh hưởng tiến độ Sprint |
| SME | 2-3 giờ/tuần | ⚠️ Trì hoãn phân tích → yêu cầu không chính xác |
| CNTT | Phản hồi trong 48 giờ | ⚠️ Chặn tích hợp, triển khai |
| Sponsor | 2 giờ/2 tuần | ⚠️ Trì hoãn phê duyệt → chặn payment milestone |

> **Quy tắc:** Ghi rõ SLA sẵn sàng của KH trong hợp đồng. Trì hoãn từ phía KH = gia hạn tiến độ tương ứng.
