# NHẬT KÝ THAY ĐỔI & QUẢN LÝ CR — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

> **⚠️ Gia công: Mọi thay đổi yêu cầu sau SRS baseline = Yêu cầu thay đổi (CR) = có ẢNH HƯỞNG CHI PHÍ**

---

## 1. Quy trình quản lý thay đổi — Gia công

### 1.1 Tại sao CR quan trọng hơn nội bộ?

| Nội bộ | Gia công |
|--------|----------|
| Thay đổi = cập nhật story, chạy sprint tiếp | Thay đổi = **ảnh hưởng hợp đồng, ngân sách, tiến độ** |
| PO quyết định nhanh | KH phải **phê duyệt chi phí** trước khi NCC triển khai |
| Ít tranh cãi | Có thể dẫn đến **tranh chấp** nếu không quản lý tốt |

### 1.2 Quy trình CR

```
Khách hàng đề xuất thay đổi
        │
        ▼
┌───────────────────┐
│ 1. BA ghi nhận CR │ ← Trong 24 giờ
│    (Ghi vào bảng) │
└─────────┬─────────┘
          │
┌─────────▼────────────┐
│ 2. BA + Trưởng nhóm  │
│    Phân tích ảnh hưởng│ ← 1-3 ngày (tùy phức tạp)
│    - Khối lượng (NC)  │
│    - Chi phí ($)      │
│    - Ảnh hưởng tiến độ│
│    - Rủi ro           │
└─────────┬────────────┘
          │
┌─────────▼──────────┐
│ 3. Gửi mẫu CR      │
│    cho KH xem xét   │ ← Email chính thức + Jira ticket
└─────────┬──────────┘
          │
    ┌─────┴──────┐
    │            │
┌───▼─────┐ ┌───▼──────┐ ┌──────────┐
│Approved│ │ Rejected  │ │ Deferred │
│→ Thêm  │ │→ Ghi lý  │ │→ Backlog │
│  vào    │ │   do     │ │  pha 2   │
│  Sprint │ └──────────┘ └──────────┘
│+ Cập   │
│  nhật   │
│  HĐ    │
│  chi phí│
└─────────┘
```

---

## 2. Phân loại CR & Thẩm quyền

| Loại | Ảnh hưởng khối lượng | Ảnh hưởng chi phí | Phê duyệt bởi | SLA phản hồi |
|------|---------------------|-------------------|---------------|-------------|
| 🟢 **Giao diện** | < 0.5 NC | Miễn phí (thiện chí) | BA | 1 ngày |
| 🟡 **Nhỏ** | 0.5 - 3 NC | Tính chi phí | PO KH | 2-3 ngày |
| 🟠 **Lớn** | 3 - 10 NC | Tính chi phí + dịch tiến độ | PO KH + PM | 5 ngày |
| 🔴 **Thay đổi phạm vi** | > 10 NC | Sửa đổi hợp đồng | **Sponsor KH** | 10 ngày |

> **Ngân sách thiện chí:** NCC có thể cho phép [X] NC miễn phí cho CR giao diện
> Số lượng cụ thể ghi trong hợp đồng.

---

## 3. Mẫu yêu cầu thay đổi

```markdown
═══════════════════════════════════════════════════
           MẪU YÊU CẦU THAY ĐỔI — CR-[NNN]
═══════════════════════════════════════════════════

**Ngày gửi:** ___/___/______
**Người gửi:** [Tên — KH/NCC]
**Ưu tiên:** 🟢 Giao diện | 🟡 Nhỏ | 🟠 Lớn | 🔴 Thay đổi phạm vi

─────────────────────────────────────────────────

## 1. Mô tả thay đổi
[Mô tả chi tiết điều cần thay đổi]

## 2. Lý do kinh doanh
[Tại sao cần thay đổi? Ảnh hưởng gì nếu KHÔNG thay đổi?]

## 3. Hành vi hiện tại (SRS Baseline)
[Hệ thống hiện tại / đặc tả hiện tại hoạt động thế nào]
**Tham chiếu SRS:** FR-[XXX] / Mục [X.X]

## 4. Hành vi mong muốn
[Sau thay đổi, mong muốn hệ thống hoạt động thế nào]

─────────────────── NHÀ CUNG CẤP ĐIỀN ──────────────────

## 5. Phân tích ảnh hưởng

| Hạng mục | Đánh giá |
|----------|---------|
| **Modules ảnh hưởng** | [Danh sách modules] |
| **Stories ảnh hưởng** | [Mã US] |
| **Thay đổi mô hình dữ liệu?** | Có / Không — [chi tiết] |
| **Thay đổi API?** | Có / Không — [chi tiết] |
| **Kịch bản KT cần cập nhật** | [N kịch bản] |
| **Tài liệu cần cập nhật** | [SRS, Bản đồ story, ...] |

## 6. Ước lượng khối lượng & Chi phí

| Vai trò | Khối lượng (NC) | Đơn giá ($/NC) | Chi phí ($) |
|---------|----------------|----------------|------------|
| BA | [X] | [Giá] | [Tổng] |
| Dev | [X] | [Giá] | [Tổng] |
| QC | [X] | [Giá] | [Tổng] |
| **Tổng** | **[X]** | | **$[Tổng]** |

## 7. Ảnh hưởng tiến độ
- Thời hạn hiện tại: [Ngày]
- Thời hạn mới (nếu duyệt): [Ngày]
- Trì hoãn: [N ngày]

## 8. Rủi ro
[Rủi ro kỹ thuật hoặc nghiệp vụ nếu thực hiện CR]

─────────────────────── QUYẾT ĐỊNH ──────────────────────

## 9. Quyết định

| Quyết định | Bởi | Ngày | Ghi chú |
|-----------|-----|------|---------|
| ☐ **Approved** — tiến hành | | | Ngân sách bổ sung: $[X] |
| ☐ **Approved** — trong ngân sách hiện tại | | | Giảm phạm vi: [cắt gì] |
| ☐ **Rejected** | | | Lý do: |
| ☐ **Hoãn** sang Giai đoạn/Phiên bản [X] | | | |

**Chữ ký:**
PO KH: _____________ Ngày: ___/___/______
PM NCC: _____________ Ngày: ___/___/______

═══════════════════════════════════════════════════
```

---

## 4. Nhật ký yêu cầu thay đổi

| Mã CR | Ngày | Người yêu cầu | Mô tả | Loại | Khối lượng (NC) | Chi phí ($) | Ảnh hưởng tiến độ | Trạng thái | Sprint | Duyệt bởi |
|-------|------|---------------|-------|------|----------------|------------|-------------------|-----------|--------|-----------|
| CR-001 | | | | | | | | Chờ | | |
| CR-002 | | | | | | | | | | |
| CR-003 | | | | | | | | | | |

---

## 5. Bảng tổng hợp CR

### Theo trạng thái

| Trạng thái | Số lượng | Tổng NC | Tổng chi phí |
|-----------|---------|---------|-------------|
| Approved | — | — | — |
| Rejected | — | — | — |
| Chờ | — | — | — |
| Hoãn | — | — | — |
| **Tổng** | — | — | — |

### Ảnh hưởng ngân sách

```
Ngân sách gốc (Hợp đồng):   $___________
Tổng chi phí CR đã duyệt:  + $___________
                            ─────────────
Tổng ngân sách dự án:        $___________
Còn lại:                     $___________
```

---

## 6. Giải quyết tranh chấp (Khi KH và NCC không đồng ý)

### Phân loại tranh cãi thường gặp

| Tranh cãi | Cách giải quyết |
|-----------|----------------|
| "Đây là lỗi, không phải CR" | So sánh với **SRS baseline**: có trong đặc tả = lỗi, không có = CR |
| "Tôi đã nói trong cuộc họp rồi" | Kiểm tra **Biên bản họp + Bản ghi**: có ghi = phạm vi, không ghi = CR |
| "Tính năng này đương nhiên phải có" | Kiểm tra **BRD & SRS**: có ghi = lỗi, ngầm hiểu nhưng không ghi = CR (thương lượng) |
| "Chi phí quá cao cho thay đổi nhỏ" | Cung cấp **Phân tích ảnh hưởng chi tiết** — minh bạch khối lượng |

### Escalation Path
```
Cấp 1: BA ↔ PO KH               → Rà soát SRS baseline
Cấp 2: PM NCC ↔ PM KH            → Thương lượng chi phí/phạm vi
Cấp 3: QĐ tài khoản ↔ Sponsor → Quyết định thương mại
Cấp 4: Pháp lý (nếu cần)         → Tham chiếu hợp đồng
```
