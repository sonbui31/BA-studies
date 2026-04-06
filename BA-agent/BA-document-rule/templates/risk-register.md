# RISK REGISTER — Template

> **Tên dự án:** [Tên]
> **Ngày tạo:** [DD/MM/YYYY]
> **Phiên bản:** V1.0
> **Cập nhật bởi:** @ba-specialist

---

## 1. Mục đích

Đăng ký và theo dõi TẤT CẢ rủi ro đã xác định trong suốt vòng đời dự án. Risk Register là tài liệu **sống** — được cập nhật mỗi sprint/phase.

---

## 2. Risk Classification

| Mức rủi ro | Impact × Probability | Hành động |
|------------|:---:|---|
| 🔴 **Critical** | ≥ 15 | Escalate ngay. Phải có mitigation plan TRƯỚC khi tiếp tục. |
| 🟡 **High** | 10-14 | Lên kế hoạch mitigation trong sprint hiện tại. |
| 🟠 **Medium** | 5-9 | Monitor hàng tuần. Có contingency plan. |
| 🟢 **Low** | 1-4 | Accept. Review hàng tháng. |

**Scale:**
- **Impact** (1-5): 1=Negligible, 2=Minor, 3=Moderate, 4=Major, 5=Catastrophic
- **Probability** (1-5): 1=Rare, 2=Unlikely, 3=Possible, 4=Likely, 5=Almost Certain

---

## 3. Risk Register Table

| Risk ID | Phân loại | Mô tả Rủi ro | Impact (1-5) | Prob (1-5) | Score | Level | Trigger | Mitigation Plan | Owner | Status | Updated |
|---------|-----------|--------------|:---:|:---:|:---:|:---:|---|---|---|---|---|
| RSK-01 | Scope | [VD: KH thay đổi yêu cầu Dashboard sau UAT → phình scope sprint cuối] | 4 | 4 | 16 | 🔴 | [VD: KH xem demo lần đầu] | [VD: Wireframe sign-off trước Sprint 3. CR process bắt buộc.] | [PM] | OPEN | [Date] |
| RSK-02 | Technical | [VD: Import 50K dòng Excel bị timeout hoặc lỗi encoding] | 3 | 3 | 9 | 🟠 | [VD: Sprint 2 - test import] | [VD: Batch import + progress bar. Test với file thực tế từ BV.] | [Dev Lead] | OPEN | [Date] |
| RSK-03 | Resource | [VD: Key dev (Backend) nghỉ việc giữa dự án] | 5 | 2 | 10 | 🟡 | [VD: Thông báo nghỉ việc] | [VD: Code review cross-team. Document API spec chi tiết.] | [PM] | OPEN | [Date] |
| RSK-04 | Timeline | [VD: Tích hợp HIS mất thêm 2 sprint do chờ API docs] | 4 | 3 | 12 | 🟡 | [VD: Sprint 3 bắt đầu] | [VD: Yêu cầu HIS API docs từ Sprint 1. Mock API nếu chờ.] | [BA] | OPEN | [Date] |
| RSK-05 | Data | [VD: Dữ liệu Excel hiện tại sai ≥ 10% → import bẩn] | 3 | 4 | 12 | 🟡 | [VD: Data cleansing] | [VD: Data audit trước import. Validate rules. Rollback plan.] | [BA] | OPEN | [Date] |

---

## 4. Risk Heatmap

```
         Impact →
         1    2    3    4    5
    5  [ 5] [10] [15] [20] [25]
P   4  [ 4] [ 8] [12] [16] [20]
r   3  [ 3] [ 6] [ 9] [12] [15]
o   2  [ 2] [ 4] [ 6] [ 8] [10]
b   1  [ 1] [ 2] [ 3] [ 4] [ 5]

🟢 1-4  |  🟠 5-9  |  🟡 10-14  |  🔴 15-25
```

---

## 5. Risk Categories & Common Patterns

| Category | Typical Risks | Where to Look |
|----------|--------------|---------------|
| **Scope** | Feature creep, unclear requirements, KH thay đổi ý | BRD, Feature Spec sign-off status |
| **Technical** | Performance bottleneck, integration failure, security hole | SRS NFRs, Architecture decisions |
| **Timeline** | Dependency delay, underestimation, multi-team coordination | Sprint plan, Gantt chart |
| **Resource** | Key person leave, skill gap, vendor dependency | Team capacity, vendor contracts |
| **Data** | Migration fails, data quality issues, encoding problems | As-Is process, Data sources |
| **Business** | Regulatory change, market shift, sponsor withdrawal | Stakeholder interviews, industry scan |
| **User Adoption** | Resistance to change, training insufficient, UX poor | Change management plan |

---

## 6. Agent Auto-Detection Rules

Khi phân tích tài liệu dự án, agent PHẢI tự phát hiện rủi ro dựa trên patterns sau:

| Pattern phát hiện được | Risk tự động tạo |
|----------------------|------------------|
| BRD có > 15 BRQs + deadline < 3 tháng | RSK: Scope quá lớn cho timeline |
| SRS nói "tích hợp với hệ thống X" nhưng không có API spec | RSK: Integration delay |
| Feature Spec nói "Virtual Scroll cho 10K dòng" nhưng NFR không có load test | RSK: Performance risk |
| User Story có > 5 stories gán cho Sprint 1 | RSK: Sprint 1 overload |
| BRD nói "import từ Excel" nhưng không có Data Migration Plan | RSK: Data migration failure |
| Không có Change Management / Training plan | RSK: Low user adoption |

---

## 7. Risk Response Strategies ⭐ NEW v3.2

> **Mục đích:** Mỗi risk PHẢI có 1 trong 4 chiến lược phản ứng. Không chỉ ghi "monitor".

### 7.1 Strategy Matrix

| Strategy | Khi nào dùng | Ví dụ | Cost |
|----------|-------------|-------|:---:|
| **🟢 Accept** | Impact thấp HOẶC probability thấp. Chi phí xử lý > chi phí rủi ro | "Font chữ có thể hiển thị khác trên Safari — chấp nhận, fix nếu user report" | Thấp |
| **🔵 Mitigate** | Có thể giảm Impact HOẶC Probability bằng hành động cụ thể | "Thêm retry mechanism cho API timeout → giảm probability từ 4→2" | Trung bình |
| **🟡 Transfer** | Chuyển trách nhiệm cho bên khác (bảo hiểm, vendor, outsource) | "Chuyển integration risk cho partner bằng SLA trong hợp đồng" | Trung bình-Cao |
| **🔴 Avoid** | Thay đổi scope/approach để loại bỏ hoàn toàn rủi ro | "Bỏ tính năng import 50K dòng realtime → chuyển sang batch import" | Cao (scope change) |

### 7.2 Response Decision Flowchart

```
Risk Score ≥ 15 (Critical)?
├── YES → Avoid hoặc Mitigate NGAY. Escalate cho Sponsor
│         ├── Avoid nếu: có thể thay đổi scope mà không ảnh hưởng Must features
│         └── Mitigate nếu: không thể thay đổi scope → giảm probability/impact
│
├── Score 10-14 (High)?
│   └── Mitigate hoặc Transfer
│         ├── Mitigate nếu: team kiểm soát được
│         └── Transfer nếu: phụ thuộc bên ngoài (vendor, partner)
│
├── Score 5-9 (Medium)?
│   └── Mitigate hoặc Accept
│         ├── Mitigate nếu: chi phí thấp
│         └── Accept nếu: chi phí mitigate > chi phí risk
│
└── Score 1-4 (Low)?
    └── Accept + Monitor
```

### 7.3 Risk Response trong Risk Register Table

Thêm cột **Response Strategy** khi điền Risk Register:

| Risk ID | Score | Level | Response | Action | Owner |
|---|:---:|:---:|:---:|---|---|
| RSK-01 | 16 | 🔴 | 🔴 **Avoid** | Bỏ realtime import → batch | PM |
| RSK-02 | 12 | 🟡 | 🔵 **Mitigate** | Thêm retry + timeout config | Dev Lead |
| RSK-03 | 10 | 🟡 | 🟡 **Transfer** | SLA trong hợp đồng partner | PM |
| RSK-04 | 4 | 🟢 | 🟢 **Accept** | Monitor hàng tháng | BA |

---

## 8. Review & Update Protocol

| Phase | Reviewer | Frequency | Action |
|-------|----------|-----------|--------|
| Sprint Planning | PM + BA | Mỗi sprint | Review risks liên quan đến sprint scope |
| Sprint Retro | Full team | Mỗi sprint kết thúc | Đánh giá risks đã hiện thực hóa chưa |
| Phase Gate | Sponsor | Mỗi Phase kết thúc | Approve mitigations cho phase tiếp |
| Go-Live | Toàn team | Trước Go-Live | Final risk review + contingency activation |

---

## 9. Lệnh kích hoạt

```
@ba-specialist tạo risk register cho dự án [tên] dựa trên BRD
@ba-specialist phân tích rủi ro scope creep cho Feature Spec này
@ba-specialist cập nhật risk register — RSK-03 đã xảy ra, chuyển sang REALIZED
@ba-specialist tìm rủi ro ẩn trong SRS mà chưa có trong Risk Register
```
