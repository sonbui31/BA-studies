# AML / KYC PROCESS — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Áp dụng:** 💰 Fintech only
> **Mục đích:** Đặc tả quy trình eKYC + Giám sát giao dịch đáng ngờ (AML)

---

## 1. eKYC Tiering

### 1.1 Tier Definitions

| Tier | Xác minh yêu cầu | Hạn mức GD/ngày | Hạn mức GD/tháng | Use case |
|:----:|-----------------|:----------------:|:-----------------:|---------|
| 0 | Email + SĐT | ≤ {{1M}} | ≤ {{5M}} | Demo, xem thông tin |
| 1 | CCCD (OCR) + Selfie (Face match) | ≤ {{20M}} | ≤ {{200M}} | Cá nhân thông thường |
| 2 | Video call + Proof of address | ≤ {{100M}} | ≤ {{1B}} | Business / High-value |
| 3 | Xác minh tại chỗ + GPKD + Đại diện PL | Không giới hạn | Không giới hạn | Enterprise / Merchant |

### 1.2 eKYC Flow (Tier 1 — Phổ biến nhất)

> Luồng eKYC có ba bên (người dùng, hệ thống eKYC, bộ phận Tuân thủ) nên vẽ bằng BPMN 2.0 theo `so_do.md` mục 4, không vẽ Mermaid. Viết `diagrams/<tên>.json`, sinh `.bpmn` và ảnh bằng `bpmn_tool.py build diagrams/<tên>.json --png diagrams/<tên>.png`; chèn ảnh và liên kết `.bpmn` theo `so_do.md` mục 4.3. Ngưỡng so khớp và số lần thử lấy từ bảng mục 1.3 và Business Rule của dự án.

Bản mô tả:

```json
{
  "id": "ekyc_tier1", "name": "eKYC Tier 1", "pool": "{{Tên tổ chức}}",
  "lanes": [{"id": "nguoi_dung", "name": "Người dùng"}, {"id": "he_thong", "name": "Hệ thống eKYC"}, {"id": "tuan_thu", "name": "Bộ phận Tuân thủ"}],
  "nodes": [
    {"id": "start", "type": "start", "name": "Người dùng bắt đầu đăng ký", "lane": "nguoi_dung"},
    {"id": "t1", "type": "user", "name": "Nhập thông tin cơ bản", "lane": "nguoi_dung"},
    {"id": "m1", "type": "xor", "name": "", "lane": "nguoi_dung"},
    {"id": "t2", "type": "user", "name": "Chụp CCCD hai mặt", "lane": "nguoi_dung"},
    {"id": "t3", "type": "service", "name": "Đọc thông tin CCCD (OCR)", "lane": "he_thong"},
    {"id": "g1", "type": "xor", "name": "Đọc được CCCD?", "lane": "he_thong"},
    {"id": "m2", "type": "xor", "name": "", "lane": "nguoi_dung"},
    {"id": "t4", "type": "user", "name": "Chụp ảnh chân dung", "lane": "nguoi_dung"},
    {"id": "t5", "type": "service", "name": "So khớp khuôn mặt với ảnh CCCD", "lane": "he_thong"},
    {"id": "g2", "type": "xor", "name": "Khớp từ {{85%}}?", "lane": "he_thong"},
    {"id": "g3", "type": "xor", "name": "Đã thử đủ 3 lần?", "lane": "he_thong"},
    {"id": "t6", "type": "service", "name": "Kiểm tra người thật (liveness)", "lane": "he_thong"},
    {"id": "g4", "type": "xor", "name": "Đạt liveness?", "lane": "he_thong"},
    {"id": "t7", "type": "service", "name": "Đối chiếu danh sách cấm vận", "lane": "he_thong"},
    {"id": "g5", "type": "xor", "name": "Trùng danh sách?", "lane": "he_thong"},
    {"id": "t8", "type": "send", "name": "Chặn đăng ký và báo bộ phận Tuân thủ", "lane": "he_thong"},
    {"id": "m3", "type": "xor", "name": "", "lane": "tuan_thu"},
    {"id": "t9", "type": "user", "name": "Xét duyệt hồ sơ thủ công", "lane": "tuan_thu"},
    {"id": "end_ok", "type": "end", "name": "KYC đạt, tài khoản lên Tier 1", "lane": "he_thong"},
    {"id": "end_block", "type": "end", "name": "Đăng ký bị chặn", "lane": "he_thong"},
    {"id": "end_review", "type": "end", "name": "Hồ sơ có kết luận thủ công", "lane": "tuan_thu"}
  ],
  "flows": [
    ["start", "t1"], ["t1", "m1"], ["m1", "t2"], ["t2", "t3"], ["t3", "g1"],
    ["g1", "m2", "Có"], ["g1", "m1", "Không, chụp lại"], ["m2", "t4"], ["t4", "t5"], ["t5", "g2"],
    ["g2", "t6", "Có"], ["g2", "g3", "Không"], ["g3", "m2", "Chưa"], ["g3", "m3", "Đủ 3 lần"],
    ["t6", "g4"], ["g4", "t7", "Đạt"], ["g4", "m3", "Không đạt"], ["t7", "g5"],
    ["g5", "end_ok", "Không trùng"], ["g5", "t8", "Trùng"], ["t8", "end_block"], ["m3", "t9"], ["t9", "end_review"]
  ]
}
```

### 1.3 eKYC Data Captured

| Field | Source | Validation |
|-------|--------|-----------|
| Họ tên | OCR từ CCCD | Match vs user input |
| Số CCCD | OCR từ CCCD | Check digit validation |
| Ngày sinh | OCR từ CCCD | ≥ 18 tuổi |
| Giới tính | OCR từ CCCD | — |
| Ảnh chân dung | CCCD | — |
| Selfie | Camera | Face match ≥ {{85%}} |
| Liveness score | AI | ≥ {{0.9}} |
| Địa chỉ | User input | Confirm tại Tier 2 |

---

## 2. Customer Due Diligence (CDD)

### 2.1 Risk Scoring

| Factor | Weight | Low (1) | Medium (3) | High (5) |
|--------|:------:|---------|-----------|---------|
| **Quốc tịch** | 20% | Việt Nam | ASEAN | High-risk (FATF list) |
| **Nghề nghiệp** | 15% | Nhân viên VP | Tự kinh doanh | PEP / Chính trị gia |
| **Thu nhập khai báo** | 15% | < 20M/tháng | 20-100M | > 100M |
| **Nguồn tiền** | 20% | Lương | Kinh doanh | Thừa kế / Không rõ |
| **Hành vi GD** | 30% | Phù hợp profile | Đôi khi bất thường | Thường xuyên bất thường |

**Risk Level:** Low (< 2.0) | Medium (2.0-3.5) | High (> 3.5)

### 2.2 Enhanced Due Diligence (EDD) — Khi Risk = High

| # | Action | Thực hiện bởi | Deadline |
|---|--------|:-------------:|:--------:|
| 1 | Request source of funds documentation | Compliance | 7 ngày |
| 2 | Senior management approval | Compliance Manager | 3 ngày |
| 3 | Enhanced monitoring (every transaction flagged) | System (auto) | Ongoing |
| 4 | Periodic review (3 tháng / lần) | Compliance | Recurring |

---

## 3. Transaction Monitoring (AML)

### 3.1 Rule Engine

| Rule ID | Tên | Trigger | Severity | Action |
|---------|-----|---------|:--------:|--------|
| AML-001 | **Velocity** | > {{10}} GD trong 1 giờ | 🟡 Medium | REVIEW |
| AML-002 | **Large Amount** | GD > {{50M}} | 🟡 Medium | REVIEW |
| AML-003 | **Daily Limit** | Tổng GD/ngày > {{200M}} | 🔴 High | BLOCK |
| AML-004 | **Structuring** | > {{5}} GD gần ngưỡng ({{45-49M}}) trong {{24h}} | 🔴 High | BLOCK + SAR |
| AML-005 | **Blacklist** | Match sanctions list (OFAC/UN/VN) | 🔴 Critical | BLOCK + SAR |
| AML-006 | **Geographic** | GD từ/đến high-risk country (FATF) | 🟡 Medium | REVIEW |
| AML-007 | **Dormant** | Tài khoản inactive > {{6 tháng}} + GD lớn đột ngột | 🟡 Medium | REVIEW |
| AML-008 | **Round Amount** | > {{3}} GD tròn số ({{10M, 20M}}) liên tiếp | 🟡 Medium | REVIEW |

### 3.2 Alert Processing Flow

```
Transaction → Rule Engine
    ├── PASS → Continue (no action)
    ├── REVIEW → Queue cho Compliance Officer
    │     ├── CLEAR → Release + Document reason
    │     ├── ESCALATE → Senior Compliance → Decision
    │     └── BLOCK → Freeze account + File SAR
    └── BLOCK (auto) → Freeze account + Alert Compliance + SAR
```

### 3.3 Suspicious Activity Report (SAR)

| Field | Mô tả |
|-------|-------|
| Report ID | SAR-{{YYYY}}-{{NNN}} |
| Subject | Tên + CCCD + Account ID |
| Suspicious activity | {{Mô tả hành vi đáng ngờ}} |
| Supporting evidence | Danh sách GD kèm screenshots |
| Rules triggered | {{AML-004, AML-008}} |
| Risk assessment | {{Low / Medium / High}} |
| Recommended action | {{Continue monitoring / Freeze / Close account}} |
| Filed to | {{Cục Phòng chống rửa tiền — NHNN}} |
| Filed date | {{DD/MM/YYYY}} |

---

## 4. Ongoing Monitoring

| Activity | Frequency | Owner | Tool |
|----------|:---------:|-------|------|
| Rule tuning (false positive review) | Monthly | Compliance + Data team | {{Spreadsheet / Dashboard}} |
| Sanctions list update | Weekly | System (auto) | {{API pull from OFAC/UN}} |
| KYC re-verification | Yearly (Tier 1) / 6 months (High risk) | Compliance | {{Notification + re-KYC flow}} |
| Regulatory report | Quarterly | Compliance Manager | {{Report template}} |

---

## ✅ Review Checklist

```
☐ eKYC tiering xác định rõ hạn mức + xác minh per tier
☐ Face match threshold + liveness score spec
☐ CDD risk scoring factors + weights xác định
☐ EDD process cho High-risk customers
☐ AML rules cover ≥ 6 patterns
☐ Alert processing flow: PASS / REVIEW / BLOCK
☐ SAR template + filing process to NHNN
☐ False positive monitoring plan (monthly)
```
