# HƯỚNG DẪN VIẾT TÀI LIỆU BA

> **Mục đích:** Chuẩn hóa cách viết để mọi tài liệu BA nhất quán, chuyên nghiệp
> **Áp dụng:** Mọi document trong bộ BA-document-rule

---

## 1. Cấu trúc file chuẩn

Mọi tài liệu BA phải có:

```markdown
# [TÊN TÀI LIỆU] — [TÊN DỰ ÁN]

> **Phiên bản:** [x.y] | **Ngày:** [DD/MM/YYYY]
> **Tác giả:** [Tên BA] | **Trạng thái:** [Draft / In Review / Approved / Baseline]
> **Dự án:** [Tên dự án]

---

## Lịch sử thay đổi

| Phiên bản | Ngày | Người chỉnh | Mô tả thay đổi |
|-----------|------|-------------|----------------|
| 1.0       | ...  | ...         | Phiên bản đầu  |

---

## Phê duyệt

| Vai trò | Tên | Ngày ký | Chữ ký |
|---------|-----|---------|--------|
| BA      | ... | ...     | ...    |
| PM      | ... | ...     | ...    |
| Sponsor | ... | ...     | ...    |

---

[NỘI DUNG CHÍNH]

---

## Phụ lục (nếu có)
## Tài liệu tham chiếu
```

---

## 1.1. Quy tắc Trình bày & Chính tả (Presentation & Spelling Rules) ⭐ NEW v3.3

Để đảm bảo tài liệu đầu ra luôn đạt chuẩn chuyên nghiệp (Production-Ready), yêu cầu áp dụng nghiêm ngặt 6 nguyên tắc sau:

1. **Chính tả & Ngữ pháp (Zero-Tolerance):** Tuyệt đối không sai chính tả, không dùng sai dấu câu, sai quy tắc viết hoa/viết thường. Sử dụng đúng thuật ngữ chuyên ngành đã định nghĩa.
2. **Tiếng Việt có dấu (Vietnamese Diacritics — ZERO-TOLERANCE):** Mọi nội dung hướng đến người đọc tiếng Việt PHẢI dùng tiếng Việt có dấu chuẩn Unicode. Tuyệt đối không viết thân tài liệu dạng "tieng Viet khong dau". Ngoại lệ hợp lệ: tên file, mã requirement/test (`BRQ-01`, `FR-ORD-001`), biến/code, endpoint/API path, database field, command, URL, và thuật ngữ kỹ thuật bắt buộc ASCII.
3. **Trật tự Logic (Structured Layout):** Các phần (sections), phần phụ (sub-sections), bảng biểu phải được sắp xếp vị trí hợp lý, liền mạch theo Template. **KHÔNG ĐƯỢC** trình bày lộn xộn, thiếu tính gắn kết hoặc đặt sai phân mục.
4. **Đánh Số Chỉ Mục (Sequential Numbering — ZERO-TOLERANCE):** Mọi danh sách, điều khoản, headings, và ID phải được đánh số đúng và giữ trình tự chặt chẽ. **Tuyệt đối không** nhảy cóc, không lặp số, không đảo lộn thứ tự. Quy tắc này áp dụng cho **3 loại đánh số**:

   **3a. Heading Numbering (Số thứ tự mục):**
   - ✅ Đúng: `1.` → `1.1` → `1.2` → `2.` → `2.1` → `2.1.1`
   - ❌ Sai: `1.` → `1.1` → `1.3` (nhảy cóc 1.2) | `2.` → `2.1` → `2.1` (lặp) | `3.` → `1.` (đảo)

   **3b. Requirement ID Numbering (Mã yêu cầu):**
   - ✅ Đúng: `BRQ-01` → `BRQ-02` → `BRQ-03` | `US-ORD-001` → `US-ORD-002` → `US-ORD-003`
   - ❌ Sai: `BRQ-01` → `BRQ-03` (nhảy BRQ-02) | `US-ORD-001` → `US-ORD-001` (lặp) | `TC-ORD-001` → `TC-ORD-003` (nhảy TC-ORD-002)
   - **Sub-ID:** `BRQ-06.1` → `BRQ-06.2` → `BRQ-06.3` (tuần tự trong cùng nhóm cha)

   **3c. Test Case / Group Numbering:**
   - ✅ Đúng: Test Group `2.1` → `2.2` → `2.3` | TC: `TC-ORD-001` → `TC-ORD-002` → `TC-ORD-003`
   - ❌ Sai: Test Group `2.1` → `2.3` → `2.5` (nhảy cóc) | `TC-ORD-001` → `TC-ORD-004` (nhảy 002, 003)

   **3d. Quy tắc Re-Index (BẮT BUỘC sau mỗi lần chỉnh sửa):**
   - Khi **thêm** item mới vào giữa danh sách → đánh lại số cho tất cả items phía sau.
   - Khi **xóa** item → đánh lại số cho tất cả items phía sau (không để lại lỗ trống).
   - Khi **di chuyển** item → cập nhật số cả vị trí cũ lẫn mới.
   - **Cross-document:** Nếu thay đổi ID trong 1 tài liệu (VD: đổi `BRQ-05` thành `BRQ-04`) → CẬP NHẬT tất cả tài liệu khác đang tham chiếu ID đó (SRS, Feature Spec, Story Map, UAT Plan).
   - **Trước khi hoàn tất:** Agent PHẢI quét toàn bộ tài liệu vừa sinh/sửa để xác nhận: (1) Không nhảy cóc, (2) Không lặp, (3) Không đảo thứ tự.
5. **Nhất quán & Liệu cơm gắp mắm Thuật ngữ (Audience-Aware Terminology):** 
   - **Tài liệu Kinh doanh (BRD, Vision):** Dùng từ ngữ phổ thông, dễ hiểu cho người ngoài ngành, tránh nhồi nhét thuật ngữ kỹ thuật (VD: dùng "Khách hàng", "Hệ thống lưu trữ lịch sử").
   - **Tài liệu Kỹ thuật (SRS, API Spec, US):** Được phép/Nên dùng thuật ngữ chuyên ngành Tech để Dev/QC hiểu chính xác (VD: dùng "End-User", "Audit Log", "Cronjob").
   - **Tuy nhiên:** Phải duy trì sự nhất quán tuyệt đối *trong cùng một phân lớp tài liệu*. (VD: Trong tài liệu kỹ thuật, nếu đã thống nhất dùng "End-User" thì không đoạn khác lại tự đổi thành "Customer". Tương tự ở BRD, dùng "Khách hàng" thì 100% dùng "Khách hàng").
6. **Văn phong Chỉn chu & Chuyên nghiệp (Polished Professionalism):** Mọi câu từ phải được trau chuốt kỹ lưỡng. Sử dụng giọng văn trang trọng (formal), khách quan. Không dùng văn nói, tiếng lóng, từ cảm thán hoặc cách hành văn lủng củng. Câu cú phải gọn gàng, súc tích, đi thẳng vào trọng tâm.
7. **Chống "Mùi AI" (Zero AI Writing Smell — ZERO-TOLERANCE):** Toàn bộ văn bản đầu ra phải tuân thủ nghiêm ngặt Bộ 24 Điều cấm và Checklist 10 bước trong `BA-agent/Anti_ai_writing_rules.md`. Cấm dùng từ vựng sáo rỗng (`crucial`, `robust`, `delve`, `deep dive`, `pivotal`, `enhance`), câu chuyển ý dập khuôn (`Additionally`, `In summary`), đối lập giả (`Not just X, but Y`), phân tích rỗng (mệnh đề `, highlighting...`), giọng chatbot phục vụ (`Of course!`, `Certainly!`) và định dạng ChatGPT máy móc.

---

## 2. Quy tắc đặt tên file

### Format: `[STT]-[Tên-tài-liệu].md`

| Tài liệu | Tên file | Ví dụ |
|-----------|----------|-------|
| Process Framework | `00-BA-Process-Framework.md` | |
| Vision & Scope | `01-Vision-Scope.md` | |
| BRD | `02-BRD.md` | |
| Stakeholder Map | `03-Stakeholder-Map.md` | |
| Process Flow | `04-Process-Flow.md` | |
| SRS | `05-SRS.md` | |
| User Story Map | `06-User-Story-Map.md` | |
| Data Model | `07-Data-Model.md` | |
| UAT Plan | `08-UAT-Plan.md` | |
| Change Log | `09-Change-Log.md` | |
| Meeting Minutes | `10-Meeting-Minutes.md` | |
| Handover Checklist | `11-Handover-Checklist.md` | |
| API Specification | `12-API-Specification.md` | |

### Quy tắc khác
- **Tên bằng tiếng Anh** — dễ đồng bộ, tránh lỗi encoding
- **Dùng PascalCase với dấu gạch ngang** — `Vision-Scope.md`, không phải `vision scope.md`
- **Đánh số để giữ thứ tự** — 00, 01, 02... theo trình tự quy trình BA

---

## 3. Versioning — Quản lý phiên bản

| Trạng thái | Version | Ý nghĩa |
|-----------|---------|---------|
| **Draft** | 0.x | Đang viết, chưa review |
| **In Review** | 0.x | Đã gửi review, chờ feedback |
| **Approved** | 1.0 | Đã được phê duyệt lần đầu |
| **Baseline** | 1.0 ✓ | Đã ký, là cơ sở cho CR tracking |
| **Updated** | 1.x | Cập nhật nhỏ (không thay đổi scope) |
| **Major Update** | 2.0 | Thay đổi lớn (cần re-approve) |

**Quy tắc:**
- `0.1 → 0.2 → 0.3` = draft iterations
- `0.x → 1.0` = approved / signed-off
- `1.0 → 1.1` = minor update (typo, clarification)
- `1.x → 2.0` = major change (scope change, CR impact)

---

## 4. Ngôn ngữ & Giọng văn

### Quy tắc tiếng Việt có dấu

- Tài liệu BA viết cho khách hàng, PO, Sponsor, Dev/QC Việt Nam phải dùng tiếng Việt có dấu đầy đủ.
- Không sinh các câu như "He thong phai hien thi danh sach don hang"; phải viết "Hệ thống phải hiển thị danh sách đơn hàng".
- Chỉ dùng không dấu/ASCII khi ngữ cảnh kỹ thuật yêu cầu: `02-BRD.md`, `FR-ORD-001`, `POST /orders`, `order_id`, `npm run test`, URL, biến, bảng database, hoặc code block.

### Ngôn ngữ theo đối tượng đọc

| Đối tượng | Ngôn ngữ | Ví dụ |
|-----------|---------|-------|
| **Sponsor / C-level** | Kinh doanh, không kỹ thuật | "Giảm 50% thời gian xử lý" |
| **Product Owner** | Nghiệp vụ + user-centric | "Khách hàng có thể đặt hàng trong 3 bước" |
| **Dev / Tech Lead** | Kỹ thuật, cụ thể | "API POST /orders trả về 201 + order_id" |
| **QC / Tester** | Scenario-based | "GIVEN ... WHEN ... THEN ..." |

### Quy tắc viết

| ✅ Nên | ❌ Tránh |
|--------|---------|
| "Hệ thống **phải** hiển thị..." (SHALL) | "Hệ thống nên hiển thị..." (mơ hồ) |
| "Thời gian phản hồi **< 3 giây**" | "Hệ thống phải nhanh" |
| "**Khi** user nhấn Submit" | "User sẽ nhấn Submit" |
| Câu ngắn, 1 ý / 1 câu | Câu dài lê thê, 3 mệnh đề |
| Active voice: "Hệ thống gửi email" | Passive: "Email được gửi bởi hệ thống" |

### Từ khóa yêu cầu (RFC 2119)

| Từ khóa | Ý nghĩa | Dùng khi |
|---------|---------|---------|
| **PHẢI** / **SHALL** | Bắt buộc, không thương lượng | Functional requirement cốt lõi |
| **NÊN** / **SHOULD** | Khuyến nghị mạnh | Requirement quan trọng nhưng có workaround |
| **CÓ THỂ** / **MAY** | Tùy chọn | Nice-to-have feature |
| **KHÔNG ĐƯỢC** / **SHALL NOT** | Cấm | Security, compliance requirement |

### Quy tắc chống "mùi AI" (Anti-AI Writing Rules — Zero-Tolerance)

Mọi văn bản tài liệu BA bắt buộc tuân thủ 100% hướng dẫn tại `BA-agent/Anti_ai_writing_rules.md`:
- **Cấm từ vựng sáo rỗng (Điều 1, 5, 6, 8, 9, 22):** `additionally, crucial, robust, delve, deep dive, pivotal, enhance, tapestry, serves as, stands as...`
- **Cấm câu dập khuôn & đối lập giả (Điều 2, 3, 4, 7, 11, 13):** Không mở đầu câu bằng liên từ công thức; không dùng `Not just X, but Y`; không dùng "Rule of Three" máy móc; không gắn mệnh đề `-ing` rỗng sau fact.
- **Cấm giọng chatbot & định dạng ChatGPT (Điều 10, 12, 14, 15, 16, 17, 18, 23):** Cấm câu meta chào hỏi (`Certainly!`, `Of course!`); cấm bullet `- **Label:**` lặp lại máy móc; cấm emoji trước heading; cấm heading và kết luận thừa.
- **Cấm thông tin không kiểm chứng (Điều 19, 20, 21):** Xóa sạch placeholder chưa điền, mã hệ thống kỹ thuật và không bịa nguồn trích dẫn.

---

## 5. Viết Requirement — Checklist SMART

Mỗi requirement phải đạt:

| Tiêu chí | Câu hỏi kiểm tra | ❌ Ví dụ sai | ✅ Ví dụ đúng |
|----------|-------------------|-------------|-------------|
| **S**pecific | Cụ thể, rõ ràng? | "Quản lý đơn hàng" | "Hiển thị danh sách đơn hàng với filter theo status" |
| **M**easurable | Đo lường được? | "Load nhanh" | "Thời gian load < 3 giây cho 95% request" |
| **A**chievable | Khả thi? | "AI dự đoán chính xác 100%" | "AI suggest với accuracy >= 80%" |
| **R**elevant | Liên quan đến goal? | "Đổi logo mỗi ngày" | "Dashboard hiển thị KPI doanh thu" |
| **T**ime-bound | Có deadline hoặc time constraint? | "Cần xong sớm" | "Triển khai trước 01/07/2026" |

### UX Metrics — Mở rộng SMART cho trải nghiệm người dùng

> ⭐ **NEW v3.1:** Các metric đo lường UX có thể dùng trong BRD/SRS.

| Metric | ❌ Mơ hồ | ✅ SMART | Cách đo |
|--------|---------|---------|--------|
| **Time-to-Decision** | "UI phải trực quan" | "User ra quyết định Approve/Reject trong ≤ 5 giây khi nhìn dashboard" | Usability test: Stopwatch + Eye tracking |
| **Time-to-Complete** | "Thao tác phải đơn giản" | "User hoàn thành task upload file trong ≤ 3 clicks" | Click counting test |
| **Error Recovery Time** | "Hệ thống dễ sửa lỗi" | "User phục hồi từ thao tác sai trong ≤ 10 giây (Undo/Back)" | Usability test |
| **Scan-to-Action** | "Báo cáo dễ đọc" | "User tìm được dòng lỗi trong bảng ≤ 100 dòng trong ≤ 3 giây" | Eye tracking / Stopwatch |
| **Learning Curve** | "Dễ học" | "User mới hoàn thành task cơ bản sau ≤ 15 phút training" | Onboarding test |

> **Quy tắc:** Mọi NFR liên quan UX trong BRD/SRS **NÊN** có ít nhất 1 UX Metric đo lường được.

---

## 6. Requirement ID — Hệ thống đánh mã

### Format: `[Prefix]-[Module]-[Number]`

| Prefix | Loại | Ví dụ |
|--------|------|-------|
| `FR` | Functional Requirement | `FR-ORD-001` |
| `NFR` | Non-Functional Requirement | `NFR-PERF-001` |
| `BR` | Business Rule | `BR-PRICE-001` |
| `US` | User Story | `US-ORD-001` |
| `UC` | Use Case | `UC-ORD-001` |

### Traceability Chain

```
BRD (BR-001) → SRS (FR-ORD-001) → User Story (US-ORD-001) → Test Case (TC-ORD-001)
```

> Mỗi requirement PHẢI trace được ngược về business need và xuôi đến test case.

---

## 7. Sử dụng Diagram

### Quy tắc chung

1. **Luôn kèm diagram** — văn bản mô tả + diagram minh họa
2. **1 diagram = 1 mục đích** — không gộp Use Case + Activity vào 1 sơ đồ
3. **Dùng Mermaid** trong markdown — dễ version control, dễ edit
4. **Đánh label rõ ràng** — mũi tên phải có nhãn, node phải có tên
5. **Giới hạn kích thước** — tối đa 7-10 node chính / diagram

### Khi nào dùng diagram nào

| Cần trả lời | Loại diagram | Tài liệu |
|-------------|-------------|----------|
| Ai tương tác với hệ thống? | Context Diagram | Vision & Scope |
| User làm gì? | Use Case Diagram | BRD, SRS |
| Quy trình chạy thế nào? | Activity/Swimlane | Process Flow |
| Hệ thống gọi nhau thế nào? | Sequence Diagram | SRS |
| Trạng thái chuyển thế nào? | State Diagram | SRS, Data Model |
| Dữ liệu quan hệ thế nào? | ERD | Data Model |
| Trải nghiệm user end-to-end? | User Journey | Vision & Scope |
| Quy tắc rẽ nhánh? | Decision Flowchart | SRS (BR) |
| Timeline dự án? | Gantt Chart | Vision & Scope |

> Chi tiết cú pháp và ví dụ: xem `core/diagram-guide.md`

---

## 8. Review & Approval Workflow

```
BA viết (Draft 0.1)
    ↓
BA self-review (BACCM Checklist)
    ↓
Peer review (BA khác hoặc QC)
    ↓
Technical review (Dev Lead — cho SRS/Data Model)
    ↓
Stakeholder review (PO / Sponsor)
    ↓
Sign-off → Version 1.0 (Baseline)
```

### Review Checklist tối thiểu

```
☐ Đúng template format (header, version, approval table)
☐ BACCM check pass (6/6 yếu tố)
☐ Requirement viết chuẩn SMART
☐ Diagram đi kèm (nếu applicable)
☐ Traceability: requirement có ID, link được
☐ Ngôn ngữ phù hợp đối tượng đọc
☐ Không còn placeholder / TODO
☐ Spelling & grammar check
```

---

## 9. Kỹ thuật Narrative Pain Points (Storytelling cho BRD) ⭐ NEW v3.1

> **Mục đích:** Biến Pain Points từ "bảng dữ liệu khô khan" thành "câu chuyện thuyết phục" — khiến Sponsor/C-level **cảm nhận** được vấn đề, không chỉ **đọc** được vấn đề.
> **Khi nào dùng:** Section "Vấn đề hiện tại" trong BRD, Vision & Scope.

### 9.1 Cấu trúc Story: Actor → Action → Failure → Consequence Chain

| Element | Mô tả | Ví dụ |
|---------|-------|-------|
| **Actor** | Ai đang chịu đau? (dùng chức danh thật, không trừu tượng) | "Trưởng phòng Kế hoạch" |
| **Action** | Hành động cụ thể hàng ngày đang làm | "dò từng dòng giữa 2 file Excel" |
| **Failure Point** | Điểm sai xảy ra — cụ thể, có dữ kiện | "Hợp đồng ghi pH, nhưng Kế hoạch gõ thiếu" |
| **Consequence Chain** | Hậu quả nối tiếp (≥ 2 bước, mỗi bước nghiêm trọng hơn) | "→ Đội không lấy mẫu → Phạt HĐ → Tốn chi phí lấy bù" |

### 9.2 Ví dụ So sánh

**❌ Cách viết cũ (chỉ dùng bảng):**

| # | Vấn đề | Ảnh hưởng | Tần suất |
|---|--------|-----------|----------|
| 1 | Thiếu mẫu trong kế hoạch | Phạt hợp đồng | Hàng tháng |

**✅ Cách viết mới (Narrative + Bảng):**

> **Thiếu mẫu — Rủi ro chí mạng #1:**
> Nhân viên nhìn vào Hợp đồng để lập Kế hoạch quan trắc chi tiết. Trưởng phòng phải dò từng dòng giữa 2 file bằng mắt thường. Hợp đồng bảo đo pH, nhưng Kế hoạch gõ thiếu. Đội hiện trường ra đến nơi mới phát hiện → không lấy mẫu → Phạt hợp đồng, tốn chi phí đi lấy bù.

| # | Pain Point | Severity | Ảnh hưởng tài chính | Tần suất |
|---|-----------|:------:|-----------------|----------|
| PP-01 | Thiếu mẫu do kiểm tra thủ công | 🔴 | ~{{X}} triệu/lần | {{Y}} lần/năm |

### 9.3 Quy tắc Viết Narrative Pain Points

1. **Narrative TRƯỚC, Bảng SAU** — Kể chuyện 3-5 câu → bảng tổng hợp để track
2. **Dùng từ ngữ cụ thể của ngành** — pH, NH3, QCVN (không trừu tượng hóa thành "chỉ tiêu")
3. **Consequence Chain ≥ 2 bước** — Mỗi hậu quả nối tiếp phải nghiêm trọng hơn bước trước
4. **Tối đa 3 narratives** — Chọn 3 pain points đau nhất, còn lại dùng bảng
5. **Kết hợp Pain Amplification** — Nếu có số liệu (X triệu/lần, Y giờ/tháng), nhúng vào câu chuyện

### 9.4 Template Câu mở đầu

```markdown
**[Tên Pain Point] — Rủi ro #[số]:**
[Actor] hiện đang [action cụ thể]. Khi [failure point xảy ra],
[hậu quả 1] → [hậu quả 2] → [hậu quả 3 (tài chính/pháp lý)].

Ví dụ:
"Kế toán trưởng hiện đang đối soát 200 hoá đơn/ngày bằng mắt thường.
Khi hoá đơn nhập sai mã thuế (xảy ra ~5%/tháng), hệ thống không cảnh báo
→ Khai thuế sai → Bị phạt thuế 20% giá trị hoá đơn → Ảnh hưởng uy tín doanh nghiệp."
```

---

## 10. Kỹ thuật Phân rã Requirement (Decomposition Patterns) ⭐ NEW v3.3

> **Mục đích:** Hướng dẫn BA cách tách 1 BRQ phức tạp thành N FRs chi tiết, nhất quán.
> **Khi nào dùng:** Khi viết SRS từ BRD — mỗi BRQ cần decompose trước khi viết FR.

### 10.1 CRUD Decomposition (Phổ biến nhất — 70% cases)

**Áp dụng khi:** BRQ yêu cầu "Quản lý [Entity]"

```
BRQ: "Quản lý tài sản" → Tách thành:
  FR-AST-01: Thêm tài sản mới (Create)
  FR-AST-02: Xem danh sách tài sản (Read - List + Filter + Search)
  FR-AST-03: Xem chi tiết 1 tài sản (Read - Detail)
  FR-AST-04: Cập nhật thông tin tài sản (Update)
  FR-AST-05: Xóa / Vô hiệu hóa tài sản (Delete / Soft-delete)
  FR-AST-06: Import tài sản từ Excel (Bulk Create — nếu cần)
  FR-AST-07: Export danh sách tài sản (Bulk Read — nếu cần)
```

### 10.2 Lifecycle Decomposition (Cho entity có trạng thái)

**Áp dụng khi:** Entity có ≥ 3 trạng thái (Draft → Submitted → Approved → Done)

```
BRQ: "Xử lý đơn hàng" → Tách theo State Machine:
  FR-ORD-01: Tạo đơn hàng (Draft → Submitted)
  FR-ORD-02: Phê duyệt đơn (Submitted → Approved / Rejected)
  FR-ORD-03: Giao hàng (Approved → Shipping → Delivered)
  FR-ORD-04: Hủy đơn (Any* → Cancelled) — *define states cho phép hủy
  FR-ORD-05: Trả hàng (Delivered → Returned)
  FR-ORD-06: Lịch sử trạng thái (Audit Trail cho mọi transition)
```

### 10.3 Actor-Based Decomposition (Cho multi-role)

**Áp dụng khi:** ≥ 3 roles sử dụng cùng entity nhưng khác quyền

```
BRQ: "Quản lý báo cáo" → Tách theo actor:
  FR-RPT-01: User xem báo cáo real-time (Viewer — read-only)
  FR-RPT-02: Manager export PDF/Excel (Exporter — read + export)
  FR-RPT-03: Admin cấu hình template báo cáo (Configurator — full CRUD)
  FR-RPT-04: System tự chạy báo cáo định kỳ (Scheduler — cron)
```

### 10.4 Integration Decomposition (Cho kết nối hệ thống ngoài)

**Áp dụng khi:** BRQ yêu cầu "Tích hợp [Hệ thống X]"

```
BRQ: "Tích hợp thanh toán" → Tách theo pattern:
  FR-PAY-01: Gửi yêu cầu thanh toán đến Gateway (Outbound)
  FR-PAY-02: Nhận callback từ Gateway (Inbound/Webhook)
  FR-PAY-03: Retry khi thanh toán thất bại (Error Handling)
  FR-PAY-04: Reconciliation đối soát cuối ngày (Batch)
  FR-PAY-05: Fallback khi Gateway offline (Degradation)
```

### 10.5 Decision Table — Chọn Pattern nào?

| BRQ có đặc điểm... | Pattern phù hợp | Số FR thường sinh |
|---------------------|----------------|:-----------------:|
| Entity cần CRUD cơ bản | CRUD | 5-7 |
| Entity có nhiều trạng thái | Lifecycle | 4-6 |
| Nhiều role sử dụng khác nhau | Actor-Based | 3-5 |
| Kết nối hệ thống ngoài | Integration | 4-5 |
| Phức hợp (CRUD + States + Roles) | **Kết hợp 2-3 patterns** | 8-15 |

> **Quy tắc:** 1 BRQ "Quản lý [X]" trung bình sinh 5-7 FRs. Nếu chỉ sinh 1-2 FR → chưa decompose đủ.

---

## 11. AC Pattern Library — 8 Loại Scenario cho Acceptance Criteria ⭐ NEW v3.3

> **Mục đích:** Đảm bảo Acceptance Criteria cover đầy đủ edge cases, không chỉ Happy/Unhappy.
> **Quy tắc coverage:** Must ≥ 4 loại, Should ≥ 3, Could ≥ 2.

| # | Loại | Template GWT | Ví dụ |
|---|------|-------------|-------|
| 1 | **Happy Path** | GIVEN valid input WHEN action THEN success result | Đăng nhập đúng → vào Dashboard |
| 2 | **Negative Path** | GIVEN invalid input WHEN action THEN error + message cụ thể | Email sai format → "Email không hợp lệ" |
| 3 | **Boundary** | GIVEN input AT boundary WHEN action THEN expected | Password 8 chars → PASS. 7 chars → FAIL |
| 4 | **Permission** | GIVEN role WITHOUT quyền WHEN access THEN 403 + message | Viewer truy cập /admin → "Không có quyền" |
| 5 | **State Transition** | GIVEN entity ở state A WHEN action THEN transition to B | Đơn "Submitted" → Approve → "Approved" |
| 6 | **Concurrency** | GIVEN 2+ users edit cùng lúc WHEN save THEN conflict handled | 2 users edit asset → optimistic lock → notification |
| 7 | **Integration** | GIVEN external system down WHEN call THEN fallback gracefully | Payment timeout → retry 3x → show "Thử lại sau" |
| 8 | **Data Volume** | GIVEN large dataset WHEN action THEN performance met | 10K rows → load < 3s, paginate 50/page |

### Coverage Matrix per MoSCoW

| MoSCoW | Minimum AC types | Bắt buộc | Khuyến nghị thêm |
|--------|:----------------:|----------|------------------|
| **Must** | **≥ 4** | Happy + Negative + Boundary + Permission | State, Integration |
| **Should** | **≥ 3** | Happy + Negative + 1 khác | Boundary hoặc State |
| **Could** | **≥ 2** | Happy + Negative | — |

### Ví dụ áp dụng — US "Thêm tài sản mới"

```gherkin
# AC1 — Happy Path
GIVEN  Admin đã đăng nhập
WHEN   điền form Tài sản (Tên, Mã, Loại, Vị trí) và nhấn Lưu
THEN   Tài sản được tạo, hiển thị trong danh sách, toast "Tạo thành công"

# AC2 — Negative Path
GIVEN  Admin điền form nhưng bỏ trống Mã tài sản
WHEN   nhấn Lưu
THEN   Hiển thị lỗi inline "Mã tài sản là bắt buộc", focus vào field

# AC3 — Boundary
GIVEN  Admin nhập Tên tài sản đúng 200 ký tự (max length)
WHEN   nhấn Lưu
THEN   Tạo thành công. Nhập 201 ký tự → field bị truncate hoặc block

# AC4 — Permission
GIVEN  User có role "Viewer" (không có quyền tạo)
WHEN   truy cập trang Thêm tài sản
THEN   Redirect về Dashboard, toast "Không có quyền thực hiện"

# AC5 — Concurrency
GIVEN  Admin A và Admin B cùng tạo tài sản với Mã TS-001
WHEN   Admin A submit trước, Admin B submit sau
THEN   Admin A thành công, Admin B nhận lỗi "Mã tài sản đã tồn tại"
```

---

## 12. Conflict Detection Patterns — 6 Loại Mâu thuẫn Requirement ⭐ NEW v3.3

> **Mục đích:** Hệ thống hóa các loại mâu thuẫn thường gặp để agent/BA phát hiện sớm.
> **Khi nào dùng:** Sau khi viết xong SRS, TRƯỚC khi chạy Traceability Validator.

### 6 Loại Conflict

| # | Loại | Dấu hiệu | Ví dụ | Detection Rule |
|---|------|----------|-------|---------------|
| 1 | **Contradictory** | FR-A nói "PHẢI X", FR-B nói "KHÔNG ĐƯỢC X" cho cùng entity | "Cho phép xóa tài sản" vs "Không được xóa tài sản có lịch sử" | Scan: PHẢI + KHÔNG ĐƯỢC + cùng keyword entity |
| 2 | **Overlapping** | 2 FRs mô tả cùng 1 chức năng nhưng khác words | FR-01 "Admin tạo user" vs FR-15 "Quản trị viên thêm tài khoản" | Scan: cùng Actor synonym + cùng Entity synonym + khác FR-ID |
| 3 | **Boundary** | 2 NFRs cùng metric nhưng khác target | NFR-01 "API < 3s" vs NFR-15 "API < 500ms" | Scan: cùng metric name + khác numeric value |
| 4 | **Temporal** | Rule đúng ở Phase 1 nhưng conflict Phase 2 | Phase 1: "3 roles" vs Phase 2 data migration cần "5 roles" | Scan: requirements tied to different phases with conflicting values |
| 5 | **Resource** | 2 FRs cần tài nguyên giới hạn đồng thời | "Realtime sync mỗi 5s" + "Batch import 100K rows" → DB lock | Analyze: FRs sharing DB/API/file/queue simultaneously |
| 6 | **Priority** | Must FR vs Must NFR không thể đồng thời đạt | Must "Export 100K rows 1 file" vs Must "Response < 3s" | Cross-check: Must FR output size vs Must NFR timing |

### Conflict Resolution Strategies

| Loại | Strategy |
|------|---------|
| Contradictory | Hỏi PO: rule nào ưu tiên? Thêm precondition phân biệt |
| Overlapping | Merge thành 1 FR duy nhất, xóa duplicate |
| Boundary | Escalate cho Tech Lead: target nào realistic? |
| Temporal | Ghi rõ "Phase 1: X, Phase 2: Y" — version theo phase |
| Resource | Thiết kế queuing / scheduling để tránh đồng thời |
| Priority | Trade-off: giảm scope Must FR hoặc nới NFR target |

---

## 13. Assumption Validation Process ⭐ NEW v3.3

> **Mục đích:** Không chỉ GHI assumption — phải có quy trình KIỂM CHỨNG.
> **Vấn đề thực tế:** 60% assumptions trong BRD không bao giờ được validate → requirement sai.

### Assumption Lifecycle

```
Identified → Documented → Assigned Owner → Validated → Confirmed / Rejected
```

### Validation Methods

| Method | Khi nào dùng | Ví dụ |
|--------|-------------|-------|
| **Ask Stakeholder** | Assumption về nghiệp vụ | "Giả định 100 đơn/ngày" → hỏi KH: "Thực tế bao nhiêu?" |
| **Data Check** | Assumption có thể verify bằng dữ liệu | "Giả định 90% user dùng Chrome" → check analytics |
| **Prototype Test** | Assumption về UX/behavior | "Giả định user hiểu icon" → test 5 users |
| **Expert Review** | Assumption về kỹ thuật | "Giả định API handle 1000 rps" → Dev Lead review |

### Assumption Register (Mở rộng bảng trong BRD)

| ID | Assumption | Status | Owner | Validate by | Method | Result | Impact nếu sai |
|---|-----------|:------:|-------|:-----------:|--------|:------:|----------------|
| ASM-01 | 100 đơn/ngày | ✅ Confirmed | PO | Sprint 1 | Ask | Thực tế 150 | Scale NFR |
| ASM-02 | User biết dùng QR | ⏳ Pending | BA | Sprint 2 | Prototype | — | Cần training |
| ASM-03 | API HIS available | ❌ Rejected | Dev Lead | Sprint 1 | Expert | API chưa có | Delay F04 |

> **Quy tắc:** Mọi assumption với Impact = High **PHẢI** validate trước Sprint 2. Assumption chưa validate → Risk Register.
