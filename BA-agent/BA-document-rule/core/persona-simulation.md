# GIAO THỨC MÔ PHỎNG PERSONA (Stakeholder Simulation v3.4)

> **BABOK KA:** Elicitation & Collaboration + Requirements Life Cycle Management
> **Mục đích:** "Stress-test" yêu cầu nghiệp vụ thông qua góc nhìn của các Stakeholder khác nhau **trước khi** trình bày thực tế.
> **Triết lý:** Phát hiện 80% phản đối từ trước khi ngồi xuống bàn họp — tiết kiệm 1-2 vòng review.

---

## 1. Danh sách Persona AI

| # | Persona | Vai trò | Trọng tâm Audit | "Tính cách" AI | Câu hỏi đặc trưng |
|---|---------|---------|-----------------|----------------|-------------------|
| 1 | **Skeptic CFO** | Giám đốc tài chính | ROI, Chi phí, Rủi ro tài chính | Khắt khe, thực tế | "Tiền ở đâu? Bao lâu hoàn vốn?" |
| 2 | **Grumpy Architect** | Kiến trúc sư trưởng | Tech Debt, Scalability, Security | Thẳng thắn, bi quan | "Cái này scale được không? 5 năm nữa thì sao?" |
| 3 | **Lazy End-User** | Người dùng cuối | Usability, Số bước, Học phí | Dễ nản, muốn nhanh | "Mấy bước? Nhiều quá, tôi quay lại Excel" |
| 4 | **Rigid Compliance** | Chuyên gia pháp chế | PDPA/GDPR, Audit trail | Cẩn thận, bám luật | "Điều khoản nào cho phép lưu dữ liệu này?" |
| 5 | **Hostile Sponsor** | Ban lãnh đạo (không ủng hộ) | Timeline, Scope, Resource | Thiếu kiên nhẫn | "Sao lâu thế? Cắt bớt scope được không?" |
| 6 | **Silent Department Head** | Trưởng phòng (ít nói) | Impact to team, Change mgmt | Thụ động, lo ngại | *Im lặng — cần chủ động hỏi cụ thể* |

---

## 2. Quy Trình Mô Phỏng — "The Gauntlet"

### 2.1 Protocol 4 bước

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  1. INPUT    │────▶│ 2. SIMULATE  │────▶│ 3. REBUTTAL  │────▶│ 4. VERDICT   │
│              │     │              │     │              │     │              │
│ Cung cấp     │     │ Persona hỏi  │     │ BA trả lời   │     │ Approve /    │
│ BRD/SRS      │     │ ≥ 3 câu hóc  │     │ hoặc sửa doc │     │ Revise       │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

### 2.2 Chi tiết từng bước

**Bước 1 — INPUT:**
- BA cung cấp section/feature cần test
- Chỉ định persona (1 hoặc nhiều)
- Mục tiêu: "tìm điểm yếu" hoặc "validate tổng thể"

**Bước 2 — SIMULATE:**
- Persona đặt **≥ 3 câu hỏi hóc búa** dựa trên trọng tâm audit
- Câu hỏi phải **cụ thể, có reference đến nội dung document**
- Không hỏi chung chung ("có risk không?") — phải chỉ rõ ("BR-003 nói xử lý 100 đơn/ngày, nhưng NFR-PERF-001 chỉ yêu cầu 50 concurrent users — mâu thuẫn?")

**Bước 3 — REBUTTAL:**
- BA trả lời từng câu hỏi
- Nếu không trả lời được → **cập nhật document** ngay
- Mỗi câu trả lời phải có evidence (dữ liệu, reference doc, stakeholder quote)

**Bước 4 — VERDICT:**
- Persona đưa ra 1 trong 3 kết quả:

| Verdict | Ý nghĩa | Hành động |
|---------|---------|-----------|
| ✅ **APPROVED** | Không có vấn đề nghiêm trọng | Tiến hành bước tiếp |
| 🟡 **CONDITIONALLY APPROVED** | Có vấn đề nhỏ, chấp nhận nếu fix | Fix → re-submit section đó |
| 🔴 **REJECTED** | Có lỗ hổng nghiêm trọng | Rewrite section → re-run full Gauntlet |

---

## 3. Scoring Matrix — C-R-F Model

Mỗi persona đánh giá 3 tiêu chí:

| Tiêu chí | Mô tả | Thang điểm |
|----------|-------|:----------:|
| **C — Completeness** | Có đủ thông tin cho persona ra quyết định? | 1-5 |
| **R — Risk Coverage** | Rủi ro liên quan đến persona đã address chưa? | 1-5 |
| **F — Feasibility** | Phương án có khả thi từ góc nhìn persona? | 1-5 |

**Quy tắc:**
- **≥ 12/15:** APPROVED
- **9-11/15:** CONDITIONALLY APPROVED
- **≤ 8/15:** REJECTED

---

## 4. Ví dụ Output — CFO Audit BRD

### Input
> "Audit BRD dự án QLTS — focus mục 3 (Luận chứng kinh doanh) và mục 4 (Phạm vi)"

### CFO Simulation

**Câu 1:** *"Mục 3.4 ghi ROI 3 năm = 180%. Nhưng chi phí bảo trì hàng năm (mục 3.2 dòng 6) ghi '$[___]' — chưa điền. Nếu bảo trì là 20% chi phí phát triển/năm thì ROI giảm còn bao nhiêu?"*

**Câu 2:** *"BR-005 yêu cầu dashboard realtime. NFR-03 yêu cầu ≥500 concurrent users. Hai cái này kết hợp cần infra mạnh hơn — chi phí hosting (mục 3.2 dòng 3) có tính chưa?"*

**Câu 3:** *"Mục 3.3 dòng 3 ghi 'Giảm 2 nhân sự thủ công' = tiết kiệm X triệu/năm. Nhân sự đó sẽ sa thải hay chuyển vị trí? Nếu chuyển vị trí thì tiết kiệm = 0, ROI sai."*

### Scoring
| Tiêu chí | Điểm | Lý do |
|----------|:----:|-------|
| Completeness | 3/5 | Chi phí bảo trì chưa điền, hosting chưa tính realtime |
| Risk Coverage | 2/5 | Không có sensitivity analysis, không có worst-case scenario |
| Feasibility | 4/5 | ROI logic hợp lý nếu số liệu đúng |
| **TOTAL** | **9/15** | **🟡 CONDITIONALLY APPROVED** |

### Recommendations
1. Điền chi phí bảo trì → tính lại ROI
2. Thêm sensitivity analysis (best/worst/expected case)
3. Clarify "giảm nhân sự" = sa thải hay chuyển vị trí

---

## 5. Multi-Persona Session — "Board Meeting"

### Khi nào dùng
- Trước sign-off BRD/SRS
- Khi document ảnh hưởng ≥ 3 departments
- Khi có conflict giữa stakeholders (CFO muốn cắt scope, PO muốn thêm feature)

### Protocol

```
1. BA trình bày Executive Summary (3-5 phút)
2. Mỗi persona hỏi 2 câu (rotation — CFO → Architect → User → Compliance)
3. BA trả lời tất cả
4. Round 2: Personas challenge CÂU TRẢ LỜI (cross-examination)
5. Vote: mỗi persona cho Approve/Conditional/Reject
6. Majority rule: ≥ 3/4 Approve → PASS
```

### Output Template

```markdown
## 🏛️ BOARD MEETING SIMULATION REPORT

**Tài liệu:** [BRD/SRS v1.0]
**Personas:** CFO, Architect, End-User, Compliance
**Ngày:** [DD/MM/YYYY]

### Kết quả bỏ phiếu
| Persona | Vote | C | R | F | Tổng |
|---------|:----:|:-:|:-:|:-:|:----:|
| CFO | 🟡 | 3 | 2 | 4 | 9 |
| Architect | ✅ | 4 | 4 | 3 | 11 |
| End-User | ✅ | 5 | 3 | 4 | 12 |
| Compliance | 🔴 | 2 | 1 | 3 | 6 |

**Kết quả:** 2 Approve, 1 Conditional, 1 Reject → **🟡 CONDITIONAL**

### Top 3 Issues phải fix
1. [Issue từ Compliance — thiếu consent management]
2. [Issue từ CFO — ROI chưa tính bảo trì]
3. [Issue từ Architect — không có fallback cho API integration]

### Action Items
- [ ] Fix issue 1 → re-submit cho Compliance
- [ ] Fix issue 2 → update mục 3.4
- [ ] Fix issue 3 → thêm NFR fallback
```

---

## 6. Lệnh Kích Hoạt

### Single Persona
```
@ba-specialist hãy đóng vai CFO để phản biện BRD mục 3 (Luận chứng kinh doanh)
@ba-specialist dùng Grumpy Architect mode — tìm rủi ro kỹ thuật trong SRS mục 2
@ba-specialist mô phỏng Lazy End-User — review User Story US-ORD-001 đến US-ORD-005
```

### Multi-Persona (Board Meeting)
```
@ba-specialist chạy Board Meeting với CFO + Architect + End-User cho BRD v1.0
@ba-specialist stress-test SRS với đủ 6 personas — focus mục 3 (FR) và mục 4 (NFR)
```

### Quick Validation
```
@ba-specialist quick persona check: BRD mục 4.2 (phạm vi) — CFO + PO
```

---

## 7. Tham Chiếu Chéo

| Persona gặp vấn đề | Tham chiếu đến |
|---------------------|---------------|
| CFO hỏi về ROI | `templates/brd.md` → §3.4, `core/decision-analysis-framework.md` |
| Architect hỏi về scalability | `templates/srs.md` → §4 (NFR), `core/nfr-discovery-guide.md` |
| End-User phàn nàn UX | `core/writing-guide.md` → §5 (UX Metrics), `core/screen-inventory-guide.md` |
| Compliance hỏi về data | Healthcare: `overlays/healthcare/overlay-config.md` → §3 (PHI) |
| Hostile Sponsor | `core/customer-intelligence-guide.md` → §6.2 (Hostile Stakeholder) |
| Nhiều personas mâu thuẫn nhau | `core/stakeholder-conflict-resolution.md` |
