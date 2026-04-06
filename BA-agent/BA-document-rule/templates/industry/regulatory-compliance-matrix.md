# REGULATORY COMPLIANCE MATRIX — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Áp dụng:** 🏛️ Government · 🏥 Healthcare · 💰 Fintech
> **Mục đích:** Map từng feature/module → quy định pháp lý tương ứng → xác nhận tuân thủ

---

## 1. Landscape quy định áp dụng

> Liệt kê TẤT CẢ quy định có liên quan đến dự án.

| # | Quy định | Cơ quan ban hành | Phạm vi áp dụng | Hiệu lực |
|---|---------|-----------------|-----------------|---------|
| 1 | {{VD: Luật 22/2023 Đấu thầu}} | {{Quốc hội}} | {{Đấu thầu CNTT công}} | {{01/01/2024}} |
| 2 | {{VD: NĐ 13/2023 BVDLCN}} | {{Chính phủ}} | {{Xử lý dữ liệu cá nhân}} | {{01/07/2023}} |
| 3 | {{VD: PCI-DSS v4.0}} | {{PCI Council}} | {{Xử lý card data}} | {{31/03/2025}} |

---

## 2. Feature → Regulation Mapping

> Với MỖI feature/module, xác định quy định nào áp dụng và yêu cầu tuân thủ cụ thể.

| Feature / Module | Quy định | Điều khoản cụ thể | Yêu cầu tuân thủ | Status |
|-----------------|---------|-------------------|------------------|:------:|
| {{Đăng ký tài khoản}} | {{NĐ 13/2023}} | {{Điều 11 — Đồng ý xử lý DLCN}} | {{Hiển thị consent form, ghi nhận thời gian đồng ý}} | ☐ |
| {{Thanh toán}} | {{PCI-DSS v4.0}} | {{Req 3 — Protect stored data}} | {{Tokenize card, never store CVV}} | ☐ |
| {{Báo cáo}} | {{QĐ 2345/NHNN}} | {{Xác thực sinh trắc học}} | {{Face ID cho GD > 10 triệu}} | ☐ |

---

## 3. Gap Analysis

| # | Gap | Quy định vi phạm | Mức độ | Giải pháp đề xuất | Effort | Owner |
|---|-----|------------------|:------:|-------------------|:------:|-------|
| 1 | {{Chưa có consent form}} | {{NĐ 13/2023 Đ11}} | 🔴 | {{Thêm consent management}} | {{M}} | {{BA}} |

---

## 4. Compliance Checklist per Ngành

### 🏛️ Government

```
☐ Đánh giá ATTT theo cấp độ (NĐ 85/2016)
☐ Tích hợp LGSP/NGSP nếu chia sẻ dữ liệu liên cơ quan
☐ Dữ liệu công dân → xác minh qua CSDL QG dân cư
☐ Hồ sơ lưu trữ ≥ 10 năm (sẵn sàng kiểm toán)
☐ Tuân thủ quy trình đấu thầu (Luật 22/2023)
```

### 🏥 Healthcare

```
☐ PHI được mã hóa at-rest (AES-256) + in-transit (TLS 1.3)
☐ Context-based access control (khoa + ca trực)
☐ Immutable audit log cho truy cập PHI (retention ≥ 10 năm)
☐ Consent management per data category (NĐ 13/2023)
☐ Clinical validation bởi bác sĩ chuyên khoa
☐ HL7 FHIR R4 compliance cho integration
```

### 💰 Fintech

```
☐ PCI-DSS Level 1 nếu xử lý card data
☐ AML/KYC theo Luật 14/2022
☐ Xác thực sinh trắc học cho GD > 10 triệu (QĐ 2345/NHNN)
☐ Transaction data retention ≥ 10 năm
☐ Idempotency cho mọi payment API
☐ Reconciliation T+1 với đối tác thanh toán
```

---

## 5. Audit Readiness

| Hạng mục | Người chịu trách nhiệm | Tần suất review | Lần review gần nhất | Status |
|---------|----------------------|----------------|---------------------|:------:|
| {{Security audit}} | {{Security team}} | {{Hàng quý}} | {{DD/MM/YYYY}} | ✅ / ⏳ / ❌ |
| {{Compliance review}} | {{Compliance officer}} | {{Hàng tháng}} | {{DD/MM/YYYY}} | ✅ / ⏳ / ❌ |

---

## ✅ Review Checklist

```
☐ Tất cả features đã mapped → quy định
☐ Không feature nào "không biết quy định nào áp dụng"
☐ Gap analysis hoàn thành + giải pháp có owner
☐ Compliance checklist đã tích theo ngành
☐ Audit readiness plan có schedule
```
