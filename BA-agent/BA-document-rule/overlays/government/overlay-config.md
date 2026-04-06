# OVERLAY: GOVERNMENT PROJECT (Dự án Chính phủ / Khu vực công)

> **Áp dụng:** Dự án CNTT sử dụng ngân sách nhà nước, đấu thầu công, cơ quan nhà nước
> **Đặc điểm:** Đấu thầu, nghiệm thu nhiều cấp, kiểm toán nhà nước, quy trình hành chính chặt chẽ

---

## 1. Tài liệu bắt buộc vs Tùy chọn

| # | Tài liệu | Bắt buộc? | Mức chi tiết | Ghi chú |
|---|----------|----------|-------------|---------|
| 1 | Vision & Scope | ✅ Bắt buộc | **Cao** | Gắn với Tờ trình phê duyệt chủ trương |
| 2 | BRD | ✅ **Bắt buộc** | **Rất cao** | Cơ sở cho HSMT + ước lượng ngân sách |
| 3 | Stakeholder Map | ✅ Bắt buộc | **Cao — nhiều cấp** | Lãnh đạo đơn vị + Ban CNTT + Đơn vị thụ hưởng |
| 4 | Process Flow | ✅ Bắt buộc | Cao | As-Is + To-Be + Gap Analysis (quy trình hành chính) |
| 5 | SRS | ✅ **Bắt buộc** | **Rất cao (20-30 trang)** | Là phụ lục kỹ thuật của HSMT |
| 6 | User Story Map | ✅ Bắt buộc | **Cao — baseline signed** | Scope agreement với Hội đồng |
| 7 | Data Model | ✅ Bắt buộc | **Cao + ATTT** | Kèm phân loại dữ liệu theo mức bảo mật |
| 8 | UAT Plan | ✅ **Bắt buộc** | **Rất cao — formal** | Vận hành thử 30-90 ngày trước nghiệm thu chính thức |
| 9 | Change Log | ✅ **Bắt buộc** | **Cao** | CR = điều chỉnh hợp đồng + phụ lục |
| 10 | Meeting Minutes | ✅ **Bắt buộc** | **Cao — GHI ÂM/HÌNH** | Lưu trữ hồ sơ dự án theo quy định |
| 11 | Handover Checklist | ✅ **Bắt buộc** | **Rất cao** | Bàn giao code + tài liệu + đào tạo CBCC |
| 12 | API Specification | ✅ Bắt buộc | **Cao** | Tích hợp LGSP, NGSP, CSDL quốc gia |
| 13 | Risk Register | ✅ **Bắt buộc** | **Cao** | Bao gồm rủi ro pháp lý + ngân sách |
| 14 | ⭐ Hồ sơ mời thầu (HSMT) | ✅ **Bắt buộc** | **Đặc thù** | Theo Luật Đấu thầu 2023 |
| 15 | ⭐ Biên bản nghiệm thu | ✅ **Bắt buộc** | **Đặc thù** | Sơ bộ + Chính thức, gắn với giải ngân |
| 16 | ⭐ Báo cáo ATTT | ✅ **Bắt buộc** | **Đặc thù** | Đánh giá an toàn thông tin theo cấp độ |
| 17 | ⭐ Kế hoạch đào tạo | ✅ **Bắt buộc** | **Đặc thù** | Đào tạo CBCC sử dụng hệ thống |

---

## 2. Phase bổ sung: ĐẤU THẦU & PHÊ DUYỆT (Phase -1 & 0)

> Dự án CNTT công có 2 giai đoạn TRƯỚC khi bắt đầu mà dự án thường không có.

```
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│ LẬP CHỦ    │──▶│ ĐẤU THẦU   │──▶│ KHỞI ĐỘNG  │──▶│  KHÁM PHÁ  │──▶│ CHI TIẾT   │──▶│ PHÁT TRIỂN │──▶│ VẬN HÀNH   │──▶│ NGHIỆM THU │
│ TRƯƠNG      │   │ & HỢP ĐỒNG │   │  (3 tuần)  │   │ (3-4 tuần) │   │ (3-4 tuần) │   │ (N Sprint) │   │ THỬ (1-3th)│   │ CHÍNH THỨC │
└────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘
```

### Phase -1: Lập chủ trương đầu tư

| Hoạt động | Output | Người phụ trách |
|-----------|--------|----------------|
| Xác định nhu cầu CNTT | Tờ trình nhu cầu | Đơn vị thụ hưởng |
| Lập đề cương sơ bộ | Đề cương + Dự toán sơ bộ | BA + Chuyên viên CNTT |
| Thẩm định chủ trương | Kết luận thẩm định | Hội đồng thẩm định |
| Phê duyệt chủ trương | Quyết định phê duyệt | Lãnh đạo cấp có thẩm quyền |

### Phase 0: Đấu thầu & Ký hợp đồng

| Hoạt động | Output | Người phụ trách |
|-----------|--------|----------------|
| Lập HSMT (Hồ sơ mời thầu) | HSMT đã phê duyệt | Bên mời thầu + BA |
| Phát hành HSMT | Thông báo trên Mạng đấu thầu QG | Bên mời thầu |
| Nhận & đánh giá HSDT | Báo cáo đánh giá | Tổ chuyên gia |
| Phê duyệt kết quả lựa chọn nhà thầu | QĐ phê duyệt | Chủ đầu tư |
| Thương thảo & ký hợp đồng | Hợp đồng đã ký | PM + Pháp chế |
| Bảo lãnh thực hiện HĐ | Thư bảo lãnh | Nhà thầu |

---

## 3. Điều chỉnh quy trình

### Thời lượng

| Phase | Government | So với Outsource |
|-------|----------|-----------------|
| Phase -1 (Chủ trương) | 1-6 tháng | **Mới — không có ở outsource** |
| Phase 0 (Đấu thầu) | 1-3 tháng | **Dài hơn nhiều** (quy trình pháp lý) |
| Inception | 3 tuần | +1 tuần (cơ cấu tổ chức phức tạp) |
| Discovery | 3-4 tuần | +1 tuần (nhiều stakeholder levels) |
| Elaboration | 3-4 tuần | +1-2 tuần (SRS là phụ lục HSMT) |
| Delivery | N Sprints | Có thể hybrid Waterfall (ngân sách năm) |
| Vận hành thử | **1-3 tháng** | **Mới — bắt buộc** trước nghiệm thu |
| Nghiệm thu chính thức | **2-4 tuần** | **Nhiều cấp** (sơ bộ → chính thức) |

### ⚠️ 7 Quy tắc vàng Government

1. **Tuân thủ Luật Đấu thầu 2023** → Mọi gói thầu > 100 triệu phải qua Mạng đấu thầu QG
2. **Hồ sơ = pháp lý** → Mọi văn bản phải có số, ngày, chữ ký, con dấu
3. **Không scope creep trả miệng** → CR = Phụ lục hợp đồng + phê duyệt lại ngân sách
4. **Bảo mật cấp Nhà nước** → Phân loại dữ liệu: Công khai / Nội bộ / Mật / Tối mật
5. **Đào tạo CBCC** → Hệ thống mới PHẢI kèm đào tạo + hướng dẫn sử dụng
6. **ATTT bắt buộc** → Đánh giá an toàn thông tin theo cấp độ (NĐ 85/2016)
7. **Kiểm toán sẵn sàng** → Hồ sơ lưu trữ ≥ 10 năm, sẵn sàng giải trình

---

## 4. Nghiệm thu & Thanh toán — Gắn với Quy trình Nhà nước

| Mốc | % | Điều kiện |
|------|---|----------|
| M0: Ký hợp đồng | 15-20% (tạm ứng) | HĐ đã ký + Bảo lãnh thực hiện |
| M1: Sign-off thiết kế (SRS) | 15% | Hội đồng phê duyệt thiết kế |
| M2: Nghiệm thu sơ bộ Release 1 | 25% | Biên bản nghiệm thu sơ bộ |
| M3: Hoàn thành vận hành thử | 25% | Báo cáo vận hành thử + ATTT |
| M4: Nghiệm thu chính thức | 15-20% | Biên bản nghiệm thu + QĐ nghiệm thu |

> ⚠️ **Thanh toán theo năm ngân sách.** Cuối năm tài chính (31/12) phải giải ngân đủ, không được chuyển nguồn tùy ý.

---

## 5. An toàn Thông tin (ATTT) — Đặc thù Government

### Phân cấp bảo mật (NĐ 85/2016)

| Cấp | Đối tượng | Yêu cầu BA |
|:---:|----------|-----------|
| 1 | Hệ thống CNTT nội bộ thông thường | ATTT cơ bản |
| 2 | Xử lý dữ liệu công dân | Audit log + Mã hóa + Access control |
| 3 | Hệ thống trọng yếu (tài chính, y tế, hạ tầng) | Đánh giá ATTT bởi đơn vị chuyên môn |
| 4 | An ninh quốc gia | Kiểm tra an ninh + Chứng nhận ATTT |

### Tích hợp bắt buộc

| Hệ thống | Mô tả | Giao thức |
|----------|-------|----------|
| LGSP | Nền tảng chia sẻ dữ liệu cấp tỉnh | REST/SOAP + LGSP Gateway |
| NGSP | Nền tảng chia sẻ dữ liệu quốc gia | REST + Xác thực PKI |
| CSDL Quốc gia dân cư | Dữ liệu công dân | API C06 Bộ Công an |
| MĐT Quốc gia | Mạng đấu thầu | Theo quy định |

---

## 6. Phase Gate bổ sung

### Lập chủ trương → Đấu thầu
- [ ] Quyết định phê duyệt chủ trương đầu tư
- [ ] Dự toán ngân sách được bố trí
- [ ] Đề cương chi tiết được thẩm định

### Đấu thầu → Khởi động
- [ ] Hợp đồng đã ký bởi cả 2 bên
- [ ] Bảo lãnh thực hiện HĐ
- [ ] Nhóm dự án phân công (CĐT + Nhà thầu)
- [ ] Kế hoạch triển khai được phê duyệt
- [ ] Tạm ứng hợp đồng ✅

### Phát triển → Vận hành thử
- [ ] Tất cả tính năng đã hoàn thành
- [ ] Nghiệm thu sơ bộ đạt
- [ ] Báo cáo ATTT đạt cấp yêu cầu
- [ ] Đào tạo CBCC hoàn thành
- [ ] Dữ liệu migration (nếu có) thành công

### Vận hành thử → Nghiệm thu chính thức
- [ ] Vận hành ổn định ≥ 30 ngày (hoặc theo HĐ)
- [ ] Tỷ lệ lỗi nghiêm trọng = 0
- [ ] Báo cáo vận hành thử được phê duyệt
- [ ] Hồ sơ bàn giao đầy đủ
- [ ] Hội đồng nghiệm thu họp & ký biên bản

---

## 7. Templates đặc thù — Dùng từ `templates/industry/`

| Template | Mô tả | Dùng tại Phase |
|----------|-------|:-------------:|
| `regulatory-compliance-matrix.md` | Map feature → quy định (ATTT, Luật ĐT) | Discovery |
| `procurement-bidding-spec.md` | HSMT + ROM + Đào tạo CBCC | Phase -1 & 0 |
| `multi-level-acceptance.md` | Nghiệm thu sơ bộ → vận hành thử → chính thức | Closure |
| `industry-integration-spec.md` | Tích hợp LGSP / NGSP / CSDL QG dân cư | Elaboration |
| `security-continuity-plan.md` | STRIDE + DR/BCP + ATTT NĐ 85/2016 | Elaboration |

