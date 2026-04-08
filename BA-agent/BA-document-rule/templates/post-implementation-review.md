# POST-IMPLEMENTATION REVIEW (PIR) — Template

> **Tên dự án:** {{Tên dự án}}
> **Ngày review:** {{DD/MM/YYYY}}
> **Phiên bản:** V1.0
> **Thực hiện bởi:** {{Tên BA / PM}}
> **Trạng thái:** Draft / Approved

---

## 1. Mục đích

Đánh giá toàn diện kết quả dự án SAU KHI go-live, bao gồm:
- Mức độ đạt OKR/KPI so với kế hoạch
- Lessons Learned cho dự án tiếp theo
- Technical Debt cần xử lý
- User Adoption và feedback thực tế

> **Khi nào thực hiện:** 30-90 ngày sau Go-Live (đủ data thực tế)

---

## 2. Benefits Realization — So sánh Kế hoạch vs Thực tế

### 2.1 OKR/KPI Achievement

| # | OKR / KPI | Baseline (trước dự án) | Target (BRD) | Actual (sau go-live) | Đạt? | Ghi chú |
|---|-----------|:---:|:---:|:---:|:---:|---|
| 1 | {{VD: Thời gian xử lý đơn hàng}} | {{15 phút}} | {{< 3 phút}} | {{2.5 phút}} | ✅ | Vượt target |
| 2 | {{VD: Tỷ lệ lỗi data entry}} | {{8%}} | {{< 2%}} | {{3.5%}} | ⚠️ | Gần target — cần cải thiện validation UX |
| 3 | {{VD: User adoption rate}} | {{0%}} | {{> 80% trong 30 ngày}} | {{65%}} | ❌ | Cần thêm training rounds |

### 2.2 Business Value Delivered

| Loại giá trị | Kế hoạch | Thực tế | Variance | Nguyên nhân |
|---|---|---|:---:|---|
| **Cost Saving** | {{500M VND/năm}} | {{350M VND/năm}} | -30% | {{Chưa tự động hoàn toàn module X}} |
| **Revenue Impact** | {{Tăng 20%}} | {{Tăng 15%}} | -5% | {{Adoption chậm hơn dự kiến}} |
| **Efficiency Gain** | {{Giảm 60% manual work}} | {{Giảm 55%}} | -5% | {{2 quy trình chưa migrate}} |
| **Risk Reduction** | {{Giảm 90% lỗi nghiệm thu}} | {{Giảm 85%}} | -5% | {{Edge case chưa cover}} |

### 2.3 Unplanned Benefits (Giá trị ngoài kế hoạch)

- {{VD: Team chủ động đề xuất cải tiến quy trình khác nhờ có data dashboard}}
- {{VD: Giảm 30% thời gian onboarding nhân viên mới nhờ quy trình chuẩn hóa}}

---

## 3. Scope Delivery — Đã giao vs Kế hoạch

| # | Feature / Epic | BRD Scope | Đã deliver? | Ghi chú |
|---|---|---|:---:|---|
| F01 | {{Dashboard Tổng quan}} | Must | ✅ | 100% |
| F02 | {{CRUD Tài sản}} | Must | ✅ | 100% |
| F03 | {{Báo cáo Xuống cấp}} | Should | ⚠️ | 80% — thiếu export PDF |
| F04 | {{Tích hợp HIS}} | Could | ❌ | Defer → Phase 2 |

### 3.1 Scope Summary

| Metric | Số lượng | Tỷ lệ |
|---|:---:|:---:|
| Total Features (BRD) | {{20}} | 100% |
| Delivered (Done) | {{16}} | {{80%}} |
| Partial (> 50%) | {{2}} | {{10%}} |
| Deferred | {{2}} | {{10%}} |
| Scope Added (CR) | {{3}} | — |

---

## 4. Timeline & Budget

### 4.1 Timeline

| Phase | Planned | Actual | Variance | Nguyên nhân |
|---|---|---|:---:|---|
| Inception | {{2 tuần}} | {{2 tuần}} | 0 | — |
| Discovery | {{3 tuần}} | {{3.5 tuần}} | +0.5 tuần | {{KH delay feedback}} |
| Elaboration | {{3 tuần}} | {{4 tuần}} | +1 tuần | {{Integration spec phức tạp hơn}} |
| Delivery | {{12 tuần}} | {{14 tuần}} | +2 tuần | {{CR thêm 3 features}} |
| Go-Live | {{1 tuần}} | {{1.5 tuần}} | +0.5 tuần | {{Data migration issue}} |
| **TOTAL** | **{{21 tuần}}** | **{{25 tuần}}** | **+4 tuần** | — |

### 4.2 Budget (nếu applicable)

| Hạng mục | Budget | Actual | Variance |
|---|:---:|:---:|:---:|
| Development | {{X}} | {{Y}} | {{Z}}% |
| Infrastructure | {{X}} | {{Y}} | {{Z}}% |
| 3rd Party / License | {{X}} | {{Y}} | {{Z}}% |

---

## 5. Quality Metrics

| Metric | Target | Actual | Đánh giá |
|---|:---:|:---:|:---:|
| Bug density (bugs/feature) | < 3 | {{2.5}} | ✅ |
| Critical bugs at go-live | 0 | {{0}} | ✅ |
| UAT pass rate (first run) | > 85% | {{78%}} | ⚠️ |
| Regression issues | < 5 | {{3}} | ✅ |
| SLA uptime (30 ngày đầu) | > 99.5% | {{99.2%}} | ⚠️ |

---

## 6. User Adoption & Feedback

### 6.1 Adoption Metrics

| Metric | Target | Actual (30 ngày) | Actual (90 ngày) |
|---|:---:|:---:|:---:|
| **DAU** (Daily Active Users) | {{80%}} | {{50%}} | {{75%}} |
| **Feature Usage Rate** (avg features used/user) | {{5+}} | {{3}} | {{5}} |
| **Training Completion** | {{100%}} | {{85%}} | {{95%}} |
| **Support Tickets (go-live)** | {{< 20/tuần}} | {{35/tuần}} | {{12/tuần}} |

### 6.2 User Feedback Summary

| Nguồn | Positive | Negative | Top Request |
|---|---|---|---|
| {{Survey post-launch}} | {{Dashboard đẹp, dễ dùng}} | {{Export chậm, thiếu shortcut}} | {{Thêm bulk edit}} |
| {{Support tickets}} | {{CRUD nhanh}} | {{Import Excel lỗi Unicode}} | {{Fix encoding}} |
| {{Interview 1-on-1}} | {{Giảm workload rõ rệt}} | {{Training chưa đủ}} | {{Video tutorial}} |

---

## 7. Technical Debt Assessment

| # | Hạng mục | Severity | Mô tả | Impact nếu không fix | Khuyến nghị |
|---|---|:---:|---|---|---|
| 1 | {{Performance}} | 🔴 | {{Báo cáo > 10K dòng load > 5s}} | {{User frustration, timeout}} | {{Thêm pagination + cache}} |
| 2 | {{Code Quality}} | 🟡 | {{Module X coverage < 40%}} | {{Regression risk}} | {{Tăng coverage lên 70%}} |
| 3 | {{Security}} | 🟡 | {{API chưa rate limiting}} | {{DDoS vulnerability}} | {{Implement rate limiter}} |
| 4 | {{Infra}} | 🟠 | {{Single DB instance}} | {{SPOF}} | {{Setup replica}} |

---

## 8. Lessons Learned

### 8.1 Điều làm tốt (Keep Doing)

| # | Lesson | Impact |
|---|---|---|
| 1 | {{Pre-Flight Checklist giảm iteration từ 4 → 2 vòng}} | Tiết kiệm ~2 tuần |
| 2 | {{Wireframe trước code → giảm rework UI 70%}} | Dev không phải sửa lại |
| 3 | {{Daily standup 15 phút nghiêm ngặt}} | Communication tốt |

### 8.2 Điều cần cải thiện (Improve)

| # | Lesson | Root Cause | Mitigation cho lần sau |
|---|---|---|---|
| 1 | {{KH thay đổi requirement Phase Delivery}} | {{BRD phê duyệt chưa đủ chặt}} | {{Double-confirm trước Sprint 1}} |
| 2 | {{Integration test muộn → phát hiện lỗi muộn}} | {{Test env chưa sẵn sàng}} | {{Setup test env từ Sprint 1}} |
| 3 | {{Data migration gần go-live mới test}} | {{Thiếu migration plan sớm}} | {{Test migration từ Sprint 2}} |

### 8.3 Điều nên tránh (Stop Doing)

| # | Anti-Pattern | Hậu quả | Thay bằng |
|---|---|---|---|
| 1 | {{Skip As-Is documentation}} | {{To-Be không fit}} | {{Mandatory As-Is trước To-Be}} |
| 2 | {{UAT chỉ 2 ngày cuối}} | {{Bug phát hiện muộn}} | {{Rolling UAT mỗi sprint}} |

---

## 9. Recommendations — Tiếp theo

### 9.1 Quick Wins (thực hiện ngay)
- [ ] {{Fix Unicode encoding cho Import Excel}}
- [ ] {{Tạo video tutorial cho 3 flows chính}}
- [ ] {{Thêm bulk edit cho module Tài sản}}

### 9.2 Phase 2 Features
- [ ] {{Tích hợp HIS (deferred từ Phase 1)}}
- [ ] {{Mobile App cho kiểm kê hiện trường}}
- [ ] {{AI-powered anomaly detection cho báo cáo xuống cấp}}

### 9.3 Infrastructure Improvements
- [ ] {{Database replica + backup automation}}
- [ ] {{Rate limiting + WAF}}
- [ ] {{Monitoring + alerting (Grafana/Sentry)}}

---

## 10. Phê duyệt

| Vai trò | Tên | Đồng ý? | Ngày | Ghi chú |
|---|---|:---:|---|---|
| BA | {{Tên}} | ☐ | | |
| PM | {{Tên}} | ☐ | | |
| Dev Lead | {{Tên}} | ☐ | | |
| Người đại diện KH (Product Owner) | {{Tên}} | ☐ | | |
| Nhà tài trợ (Sponsor) | {{Tên}} | ☐ | | |

---

*Template v3.2 — BA-Agent Framework*
