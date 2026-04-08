# QUY TRÌNH NGHIỆP VỤ (Hiện tại / Tương lai) — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Lưu ý:** Quy trình As-Is dựa trên thông tin Khách hàng cung cấp. BA Nhà cung cấp phải xác nhận lại.

---

## 1. Hướng dẫn sử dụng

### Đặc thù outsource khi vẽ quy trình:

| Yếu tố | Nội bộ | Gia công |
|---------|--------|----------|
| Nguồn thông tin | Ngồi cạnh người dùng, quan sát | Phỏng vấn từ xa, chia sẻ màn hình, ghi hình |
| Xác nhận | Đi thực tế (Gemba) | Video call + ghi màn hình + KH xác nhận qua email |
| Phê duyệt | Không chính thức | **Chính thức** — KH ký vào Quy trình trước khi đội phát triển bắt đầu |
| Thay đổi | Cập nhật luôn | Yêu cầu thay đổi (CR) nếu ảnh hưởng phạm vi/khối lượng |

### Cách thu thập quy trình khi gia công (từ xa):
1. **Phỏng vấn:** Video call với Chuyên gia nghiệp vụ (SME), ghi hình lại
2. **Chia sẻ màn hình:** Yêu cầu Chuyên gia NV thao tác hệ thống cũ qua chia sẻ màn hình
3. **Xem xét tài liệu:** KH gửi SOP, biểu mẫu, ảnh chụp
4. **Bảng câu hỏi:** Gửi form câu hỏi cho KH điền (bất đồng bộ)
5. **Workshop:** Phiên Miro/FigJam — cộng tác (trực tiếp)

---

## 2. Mẫu quy trình

> Sử dụng mẫu dưới đây cho mỗi quy trình nghiệp vụ trong dự án.

### Quy trình: [Tên quy trình]
**Chuyên gia nghiệp vụ (SME) cung cấp thông tin:** [Tên, vai trò]
**Ngày phỏng vấn:** [DD/MM/YYYY]
**Link bản ghi:** [Link video nếu có]

#### 2.1 HIỆN TẠI (Quy trình hiện tại — As-Is)

```
[Vẽ sơ đồ quy trình hiện tại]

Ví dụ:
Tác nhân 1           Hệ thống cũ / Thủ công       Tác nhân 2
   │                       │                         │
   │  Bước 1: ...         │                         │
   │──────────────────────▶│                         │
   │                       │  Bước 2: ...            │
   │                       │────────────────────────▶│
   │                       │                         │
   │  ◄── Bước 3: ...     │                         │
   │                       │                         │
```

**Điểm đau:**
- 🔴 [Điểm đau nghiêm trọng — ảnh hưởng lớn]
- 🟠 [Điểm đau lớn — thường xuyên gặp]
- 🟡 [Điểm đau nhỏ — phiền nhưng chấp nhận được]

**Số liệu hiện tại (nếu có):**
- Thời gian xử lý trung bình: ___
- Số lượng giao dịch/ngày: ___
- Tỷ lệ lỗi: ___%
- Số bước thủ công: ___

---

#### 2.2 TƯƠNG LAI (Quy trình mới — To-Be)

```
[Vẽ sơ đồ quy trình mới với hệ thống]

Tác nhân 1           Hệ thống mới                Tác nhân 2
   │                       │                         │
   │  Bước 1: ...         │                         │
   │──────────────────────▶│                         │
   │                       │  Tự động: ...           │
   │                       │────────────────────────▶│
   │                       │                         │
   │  ◄── Thông báo       │                         │
   │                       │                         │
```

**Cải tiến so với hiện tại:**
- ✅ [Cải tiến 1 — KPI cụ thể]
- ✅ [Cải tiến 2]
- ✅ [Cải tiến 3]

**Điểm cần Khách hàng xác nhận:**
- ⚠️ [Quy trình mới thay đổi cách làm hiện tại — KH đã đồng ý? C/K]
- ⚠️ [Quy tắc nghiệp vụ nào cần xác nhận?]

---

## 3. Danh sách quy trình cần vẽ

| # | Tên quy trình | Module | Ưu tiên | Trạng thái | KH phê duyệt |
|---|--------------|--------|---------|-----------|-------------|
| P1 | [Quy trình chính 1] | Module 1 | P0 | ☐ Nháp | ☐ Chờ |
| P2 | [Quy trình chính 2] | Module 1 | P0 | ☐ Nháp | ☐ Chờ |
| P3 | [Quy trình 3] | Module 2 | P1 | ☐ Chưa bắt đầu | ☐ Chờ |
| P4 | [Quy trình 4] | Module 2 | P1 | ☐ Chưa bắt đầu | ☐ Chờ |
| P5 | [Quy trình 5] | Module 3 | P2 | ☐ Chưa bắt đầu | ☐ Chờ |

---

## 4. Phân tích khoảng cách

| # | Lĩnh vực | Hiện tại | Tương lai | Khoảng cách | Giải pháp | Trong phạm vi? |
|---|----------|----------|-----------|-------------|-----------|---------------|
| 1 | [Lĩnh vực 1] | [Trạng thái hiện tại] | [Trạng thái tương lai] | [Thiếu gì] | [Cách giải quyết] | ✅ Có |
| 2 | [Lĩnh vực 2] | [Trạng thái hiện tại] | [Trạng thái tương lai] | [Thiếu gì] | [Cách giải quyết] | ✅ Có |
| 3 | [Lĩnh vực 3] | [Trạng thái hiện tại] | [Trạng thái tương lai] | [Thiếu gì] | [Cách giải quyết] | ❌ Cần CR |

> ⚠️ **Lưu ý outsource:** Nếu khoảng cách nằm **ngoài phạm vi hợp đồng** → ghi rõ "Cần CR" → đánh giá chi phí trước khi cam kết

---

## 5. Phê duyệt quy trình

| Quy trình | Phiên bản | Người đại diện KH (PO) | Ngày | Ghi chú |
|-----------|-----------|--------------------------|------|---------|
| P1: [Tên] | v1.0 | ☐ Đã phê duyệt | | |
| P2: [Tên] | v1.0 | ☐ Đã phê duyệt | | |
| P3: [Tên] | v1.0 | ☐ Đã phê duyệt | | |

> **Sau khi phê duyệt:** Quy trình trở thành **Bản chốt phạm vi (Baseline)**. Thay đổi = Yêu cầu thay đổi (CR).
