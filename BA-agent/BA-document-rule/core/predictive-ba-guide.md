# DỰ BÁO BA & QUẢN TRỊ RỦI RO (Predictive BA Guide 3.0)

> **Mục đích:** Phát hiện và quản trị rủi ro dự án một cách **actionable** — không dựa trên "hàng ngàn mẫu dự án" mà dựa trên **patterns thực tế** phát hiện từ tài liệu đang viết.
> **Triết lý v3.0:** "Detect from Facts, not Predict from Theory"
> **Output chính:** Risk Register (`../BA-document-rule/templates/risk-register.md`)

---

## 1. Risk Detection Patterns (Actionable v3.0)

Agent PHẢI quét tài liệu dự án và tự phát hiện rủi ro dựa trên patterns sau:

### A. Scope Creep Indicators

| Pattern phát hiện trong tài liệu | Risk Level | Auto-Generated Risk |
|---|:---:|---|
| BRD có > 15 BRQs + timeline < 3 tháng | 🔴 | "Scope quá lớn. Đề xuất: MoSCoW → defer `Could` items." |
| Feature Spec: module nào có > 8 sub-features | 🟡 | "Module [X] phức tạp. Risk: thiếu thời gian dev + test." |
| User Story không gán Sprint | 🟡 | "Stories chưa plan timeline → risk deadline không kiểm soát." |
| Stakeholder > 5 roles + chưa có RACI | 🔴 | "Nhiều stakeholders + không rõ quyền quyết định → risk conflict." |
| OKR target quá cao so với As-Is baseline (>10x improvement) | 🟡 | "Mục tiêu không thực tế. Verify lại với stakeholder." |

### B. Technical Risk Indicators

| Pattern | Risk Level | Auto-Generated Risk |
|---|:---:|---|
| SRS nói "tích hợp với [system X]" nhưng không có API spec | 🔴 | "Integration risk: thiếu API documentation → chờ partner." |
| NFR <= 3 items | 🟡 | "Thiếu NFRs. Risk: sản phẩm hoạt động nhưng UX/perf kém." |
| SRS Performance target ("< 2s") nhưng không có load test plan | 🟡 | "Perf NFR chưa verifiable. Thêm load test vào UAT." |
| Data entities > 10 nhưng không có ERD | 🔴 | "Schema phức tạp nhưng chưa model → risk data integrity." |

### C. Data & Migration Risk Indicators

| Pattern | Risk Level | Auto-Generated Risk |
|---|:---:|---|
| BRD nói "import từ Excel" nhưng không có Data Migration Plan | 🔴 | "Migration risk: chưa có mapping, cleansing, rollback plan." |
| Dữ liệu nguồn > 10K records | 🟡 | "Volume lớn → cần batch import + progress tracking." |
| Multiple data sources (Excel + DB legacy + Paper) | 🔴 | "Multi-source merge → high risk data conflicts." |

### D. Change Management Risk Indicators

| Pattern | Risk Level | Auto-Generated Risk |
|---|:---:|---|
| Không có Training Plan / User Guide | 🟡 | "Risk: low adoption. Users sẽ quay lại cách cũ." |
| Người dùng cuối > 50 nhưng UAT chỉ 2-3 test cases per module | 🟡 | "Thiếu test coverage cho diverse user scenarios." |

---

## 2. Quy trình Thực hiện (v3.0)

### Step 1: Input Analysis (Automatic)
- Agent đọc tài liệu đã có (BRD, SRS, Feature Spec, etc.)
- Quét patterns từ Section 1 ở trên
- **LLM:** OpenAI o4 — reasoning + edge case detection

### Step 2: Risk Register Generation
- Tạo Risk Register từ template (`risk-register.md`)
- Mỗi risk có: Description, Impact, Probability, Score, Mitigation, Owner
- **LLM:** o4 — severity assessment | GPT-5 — mitigation suggestions

### Step 3: "What-If" Scenario Analysis
- Cho các 🔴 Critical risks, agent sinh **3 kịch bản** (tốt nhất, trung bình, xấu nhất)
- VD: "Nếu integration API delay 2 sprint → ảnh hưởng feature F05, F16 → UAT chậm 1 tháng"
- **LLM:** o4 — causal reasoning

### Step 4: Continuous Monitoring
- Risk Register là tài liệu **sống** — cập nhật mỗi sprint
- Agent tự quét lại khi nhận document mới hoặc Change Request

---

## 3. Complexity Heatmap

Agent đánh dấu các sections "nóng" trong SRS:

```markdown
## 🌡️ Complexity Heatmap

| Section | Complexity | Risk | Why |
|---------|:---:|:---:|---|
| F05: CRUD Tài sản | 🟢 Low | 🟢 | Logic CRUD đơn giản |
| F16: Capacity Tracking | 🔴 High | 🟡 | Công thức tính phức tạp, nhiều edge cases |
| F20: Tích hợp HIS | 🔴 High | 🔴 | Phụ thuộc external system + chưa có API |
| F08: Báo cáo | 🟡 Medium | 🟡 | Nhiều biến thể báo cáo, UI phức tạp |
```

---

## 4. Lệnh kích hoạt

```
@ba-specialist tạo risk register cho dự án [tên] dựa trên BRD/SRS
@ba-specialist quét rủi ro scope creep cho Feature Spec này  
@ba-specialist phân tích "What-If": nếu integration HIS delay 2 sprint
@ba-specialist tìm complexity hotspots trong SRS
@ba-specialist cập nhật risk register — thêm risk mới từ Change Request
```
