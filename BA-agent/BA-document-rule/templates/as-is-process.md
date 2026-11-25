# AS-IS PROCESS DOCUMENTATION — Template

> **Tên dự án:** [Tên]
> **Ngày tạo:** [DD/MM/YYYY]
> **Phiên bản:** V1.0
> **Người viết:** @ba-specialist

---

## 1. Mục đích

Tài liệu hóa quy trình **hiện tại** (As-Is) mà tổ chức đang vận hành TRƯỚC khi có hệ thống mới. Đây là baseline để:
- Đo lường cải thiện (Before → After)
- Phát hiện pain points thực sự (không suy đoán)
- Đảm bảo hệ thống mới (To-Be) giải quyết đúng vấn đề

---

## 2. Tổng quan Quy trình Hiện tại

| # | Tên Quy trình | Người thực hiện | Tần suất | Công cụ hiện tại | Thời gian TB |
|---|---------------|-----------------|----------|-------------------|-------------|
| 1 | [VD: Nhập tài sản mới] | [VD: KTTS] | [VD: 10 lần/tuần] | [VD: Excel + Giấy] | [VD: 30 phút/lần] |
| 2 | [VD: Kiểm kê định kỳ] | [VD: Tổ kiểm kê] | [VD: 6 tháng/lần] | [VD: Sổ tay + Giấy] | [VD: 2 tuần] |
| ... | ... | ... | ... | ... | ... |

---

## 3. Chi tiết Từng Quy Trình

### 3.1 Quy trình: [Tên quy trình 1]

**Mô tả:** [Tóm tắt 1-2 dòng quy trình hiện tại]

**Sơ đồ quy trình As-Is (BPMN 2.0):**

> Vẽ bằng BPMN 2.0 theo `so_do.md` mục 4: một pool cho tổ chức, mỗi vai trò một lane, mỗi bước nằm trong đúng một lane. Bước làm tay ngoài hệ thống ghi `"type": "manual"`. Bước gây điểm đau ghi `"highlight": "pain"` và mã PP-xx (bảng điểm đau ở mục 4 dưới đây) trong tên bước. Viết bản mô tả `diagrams/<tên>-asis.json`, rồi sinh `.bpmn` và ảnh bằng `bpmn_tool.py build diagrams/<tên>-asis.json --png diagrams/<tên>-asis.png`. Sơ đồ chưa được SME xác nhận thì ghi `[CẦN XÁC NHẬN]` cạnh tên sơ đồ. Mermaid chỉ dùng để phác thảo nhanh trong buổi trao đổi (`so_do.md` mục 4.5), không thay sơ đồ này.

Khung bản mô tả (ví dụ nhập tài sản mới; thay bằng quy trình thật):

```json
{
  "id": "nhap_tai_san_asis",
  "name": "As-Is: Nhập tài sản mới",
  "pool": "[Tên tổ chức]",
  "lanes": [
    {"id": "ktts", "name": "Kế toán tài sản"},
    {"id": "ke_toan", "name": "Kế toán"},
    {"id": "tai_chinh", "name": "Phòng Tài chính"}
  ],
  "nodes": [
    {"id": "start", "type": "start", "name": "Nhận biên bản mua sắm", "lane": "ktts"},
    {"id": "a1", "type": "manual", "name": "Ghi vào sổ quản lý tài sản (PP-01)", "lane": "ktts", "highlight": "pain"},
    {"id": "a2", "type": "manual", "name": "Lập phiếu nhập kho giấy", "lane": "ke_toan"},
    {"id": "a3", "type": "manual", "name": "Ký duyệt phiếu nhập", "lane": "tai_chinh"},
    {"id": "g1", "type": "xor", "name": "Phiếu đủ chữ ký?", "lane": "tai_chinh"},
    {"id": "a4", "type": "manual", "name": "Ghi sổ kế toán trên Excel", "lane": "ke_toan"},
    {"id": "end_ok", "type": "end", "name": "Tài sản đã vào sổ", "lane": "ke_toan"},
    {"id": "end_back", "type": "end", "name": "Phiếu bị trả lại", "lane": "tai_chinh"}
  ],
  "flows": [
    ["start", "a1"], ["a1", "a2"], ["a2", "a3"], ["a3", "g1"],
    ["g1", "a4", "Đủ"], ["g1", "end_back", "Thiếu"], ["a4", "end_ok"]
  ]
}
```

Chèn vào tài liệu:

```markdown
![As-Is: <Tên quy trình>](diagrams/<tên>-asis.png)

Bản chuẩn BPMN 2.0: [`diagrams/<tên>-asis.bpmn`](diagrams/<tên>-asis.bpmn), mở và sửa bằng bpmn.io hoặc Camunda Modeler. Ô viền đỏ là bước gây điểm đau.

<!-- Sinh lại ảnh (chạy trong thư mục bộ tài liệu): python ../scripts/bpmn_tool.py build diagrams/<tên>-asis.json --png diagrams/<tên>-asis.png -->
```

Lệnh sinh lại ảnh nằm trong chú thích HTML vì đó là việc nội bộ của BA; `md_to_docx.py` bỏ chú thích nên bản Word giao khách không có lệnh này.

**Các bước chi tiết:**

| Bước | Người thực hiện | Hành động | Input | Output | Thời gian | Vấn đề |
|------|-----------------|-----------|-------|--------|-----------|--------|
| 1 | [Role] | [Mô tả hành động] | [Tài liệu/dữ liệu đầu vào] | [Kết quả] | [Thời gian] | [Pain point nếu có] |
| 2 | ... | ... | ... | ... | ... | ... |

---

## 4. Pain Point Analysis (Phân tích Điểm đau)

| # | Pain Point | Mức độ | Ảnh hưởng | Tần suất | Bằng chứng |
|---|-----------|:------:|-----------|----------|-----------|
| PP-01 | [VD: Nhập trùng tài sản do không kiểm tra được trùng trên Excel] | 🔴 High | [VD: Sai lệch sổ sách 5-10%] | [VD: Hàng tuần] | [VD: Transcript phỏng vấn KTTS / Số liệu kiểm kê Q3] |
| PP-02 | [VD: Mất 2 tuần kiểm kê do dùng giấy] | 🟡 Medium | [VD: Tốn nhân sự 5 người x 2 tuần] | [VD: 6 tháng/lần] | [VD: Báo cáo kiểm kê 2024] |
| ... | ... | ... | ... | ... | ... |

---

## 5. Gap Analysis Framework (As-Is → To-Be) ⭐ ENHANCED v3.3

> **Mục đích:** Phân loại gaps theo 5 categories → ưu tiên hóa → theo dõi closure.

### 5.1 Gap Classification (5 loại)

| # | As-Is (Hiện tại) | To-Be (Mong muốn) | Gap Type | Gap Description | BRQ liên quan | Priority |
|---|-------------------|-------------------|:--------:|-----------------|:-------------:|:--------:|
| GAP-01 | Nhập tài sản bằng Excel, không validation | Nhập trên PM với auto-validate | 🔧 **Process** | Cần form nhập có business rules | BRQ-01 | Must |
| GAP-02 | Kiểm kê bằng sổ giấy | Kiểm kê bằng QR + Mobile | 🖥️ **Technology** | Cần HHT/Mobile + QR Scanner | BRQ-06 | Must |
| GAP-03 | Không ai biết data quality | Có data cleansing trước migration | 👤 **People** | Cần hire/train Data Analyst | — | Should |
| GAP-04 | Data Excel thiếu trường, trùng mã | Data clean, unique, đầy đủ | 📊 **Data** | ETL + Cleansing + Migration plan | BRQ-08 | Must |
| GAP-05 | Không log ai sửa gì khi nào | Audit trail đầy đủ 5 năm | 📜 **Compliance** | Cần audit logging infrastructure | BRQ-10 | Must |

### 5.2 Gap Type Legend

| Type | Icon | Mô tả | Action thường thấy |
|------|:----:|-------|------------------|
| **Process** | 🔧 | Bước thủ công cần tự động hóa | Automate, redesign workflow |
| **Technology** | 🖥️ | Hạ tầng / tool không đáp ứng | Upgrade, migrate, integrate |
| **People** | 👤 | Thiếu skill, role, hoặc headcount | Train, hire, outsource |
| **Data** | 📊 | Dữ liệu thiếu, trùng, không sạch | Cleanse, migrate, standardize |
| **Compliance** | 📜 | Chưa tuân thủ quy định nội bộ/pháp lý | Implement controls, logging |

### 5.3 Gap Prioritization Matrix

| Gap ID | As-Is Score (1-5) | To-Be Score (1-5) | Gap Size | Fix Effort (S/M/L) | Business Value (H/M/L) | Priority |
|:------:|:--:|:--:|:--:|:--:|:--:|:--------:|
| GAP-01 | 2 | 5 | **3** | M | H | 🔴 Must |
| GAP-02 | 1 | 5 | **4** | L | H | 🔴 Must |
| GAP-03 | 1 | 3 | **2** | M | M | 🟡 Should |

> **Quy tắc:** Gap Size = To-Be - As-Is. Size ≥ 3 + Business Value = H → Must

### 5.4 Gap Closure Tracking (dùng trong PIR)

| Gap ID | Planned Close Date | Actual Close Date | % Closed | Evidence |
|:------:|:------------------:|:-----------------:|:--------:|----------|
| GAP-01 | Sprint 2 | Sprint 2 | 100% | Form nhập + validation live |
| GAP-02 | Sprint 4 | — | 0% | Chưa bắt đầu |

---

## 6. Metrics Baseline (Số liệu Cơ sở)

> **Quan trọng:** Các số liệu này sẽ được dùng để đo lường hiệu quả SAU khi triển khai hệ thống mới.

| Metric ID | Tên chỉ số | Giá trị Hiện tại (As-Is) | Mục tiêu (To-Be) | Phương pháp đo | OKR liên quan |
|-----------|-----------|:---:|:---:|---|---|
| M-01 | Thời gian nhập 1 tài sản | [VD: 30 phút] | [VD: 5 phút] | [VD: Stopwatch test] | OKR-01 |
| M-02 | Tỷ lệ lỗi dữ liệu | [VD: 10%] | [VD: < 1%] | [VD: Đối soát Excel vs thực tế] | OKR-02 |
| M-03 | Thời gian kiểm kê toàn bệnh viện | [VD: 14 ngày] | [VD: 3 ngày] | [VD: Báo cáo kiểm kê] | OKR-03 |

---

## 7. So sánh As-Is và To-Be

> Mỗi quy trình có hai sơ đồ BPMN 2.0 riêng, `diagrams/<tên>-asis` và `diagrams/<tên>-tobe`, cùng pool và cùng tên lane để người đọc đặt cạnh nhau. Không gộp As-Is và To-Be vào một sơ đồ. Trong To-Be, bước mới ghi `"highlight": "new"` (ô viền xanh). Chèn từng sơ đồ theo mẫu ở mục 3.1, rồi tóm tắt khác biệt bằng bảng dưới.

| Bước As-Is | Bước To-Be | Thay đổi | Điểm đau được giải quyết |
|---|---|---|---|
| [VD: Ghi sổ tay rồi chép vào Excel] | [VD: Nhập trên phần mềm, kiểm tra trùng mã khi lưu] | [VD: Bỏ một lần nhập lại] | [PP-xx] |
| [VD: Gửi email xin duyệt, chờ ký 1-3 ngày] | [VD: Người duyệt nhận thông báo và duyệt trên phần mềm] | [VD: Bước mới, `"highlight": "new"`] | [PP-xx] |

---

## 8. Phụ lục

### A. Nguồn thông tin
- [ ] Phỏng vấn: [Ai? Ngày nào?]
- [ ] Quan sát thực tế: [Ở đâu? Bao lâu?]
- [ ] Tài liệu hiện có: [File nào?]
- [ ] Số liệu thống kê: [Nguồn?]

### B. Ký hiệu
| Ký hiệu | Ý nghĩa |
|---------|---------|
| 🔴 | Pain Point nghiêm trọng |
| 🟡 | Pain Point trung bình |
| 🟢 | Hoạt động tốt, giữ nguyên |
