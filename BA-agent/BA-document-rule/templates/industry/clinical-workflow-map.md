# CLINICAL WORKFLOW MAP — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Áp dụng:** 🏥 Healthcare only
> **Mục đích:** Document quy trình y khoa chi tiết cho từng Clinical Pathway

---

## 1. Clinical Pathways Index

| # | Pathway | Module HIS | Stakeholder chính | Status |
|---|---------|-----------|-------------------|:------:|
| 1 | {{Ngoại trú (OPD)}} | Tiếp nhận, Khám, CLS, Kê đơn, Thanh toán | BS phòng khám | ☐ |
| 2 | {{Nội trú (IPD)}} | Nhập viện, Theo dõi, Phẫu thuật, Xuất viện | BS điều trị + ĐD | ☐ |
| 3 | {{Cấp cứu (ER)}} | Phân loại, Xử trí, Chuyển khoa/viện | BS cấp cứu | ☐ |
| 4 | {{Cận lâm sàng (CLS)}} | Chỉ định, Lấy mẫu, XN, Trả KQ | KTV + BS | ☐ |
| 5 | {{Dược (Pharmacy)}} | Kê đơn, Duyệt, Cấp phát, DDI check | Dược sĩ | ☐ |

---

## 2. Pathway Template

> Copy section này cho MỖI pathway ở trên.

### 2.X Pathway: {{TÊN PATHWAY}}

#### Tổng quan

| Hạng mục | Chi tiết |
|---------|---------|
| **Trigger** | {{VD: Bệnh nhân đến phòng khám}} |
| **End state** | {{VD: BN nhận thuốc + ra về}} |
| **Actors** | {{Tiếp nhận, BS, ĐD, KTV, Dược sĩ, Thu ngân}} |
| **SLA** | {{VD: Thời gian khám trung bình ≤ 15 phút}} |

#### Luồng chính (Clinical Flow)

| Bước | Actor | Hành động | Hệ thống hỗ trợ | Output | Rủi ro y khoa |
|:----:|-------|----------|-----------------|--------|:-------------:|
| 1 | Tiếp nhận | {{Đăng ký BN, kiểm tra BHYT}} | {{Module Tiếp nhận}} | {{Phiếu khám}} | — |
| 2 | Bác sĩ | {{Khám, ghi nhận triệu chứng}} | {{Module Khám bệnh}} | {{Bệnh án}} | — |
| 3 | Bác sĩ | {{Chỉ định xét nghiệm}} | {{Module CLS}} | {{Phiếu chỉ định}} | ⚠️ Sai chỉ định |
| 4 | KTV | {{Lấy mẫu, thực hiện XN}} | {{Module LIS}} | {{Kết quả XN}} | ⚠️ Nhầm mẫu |
| 5 | Bác sĩ | {{Đọc KQ, chẩn đoán (ICD-10)}} | {{Module Chẩn đoán}} | {{Mã ICD}} | ⚠️ Sai chẩn đoán |
| 6 | Bác sĩ | {{Kê đơn thuốc}} | {{Module Kê đơn + DDI}} | {{Đơn thuốc}} | 🔴 DDI / Sai liều |
| 7 | Dược sĩ | {{Duyệt đơn, cấp phát}} | {{Module Dược}} | {{Thuốc}} | ⚠️ Sai thuốc |
| 8 | Thu ngân | {{Tính viện phí, thanh toán}} | {{Module Billing}} | {{Hóa đơn}} | — |

#### Luồng ngoại lệ (Exception)

| ID | Tại bước | Điều kiện | Xử lý | Rủi ro |
|----|:-------:|----------|-------|:------:|
| EX-1 | 3 | BN dị ứng thuốc cản quang | Cảnh báo + Chọn phương pháp khác | 🔴 |
| EX-2 | 6 | DDI phát hiện tương tác thuốc | Popup cảnh báo + BS xác nhận / đổi thuốc | 🔴 |
| EX-3 | 4 | Kết quả XN bất thường nguy hiểm | Alert tức thì cho BS + ĐD trực | 🔴 |

#### Sơ đồ quy trình (BPMN 2.0)

> Vẽ bằng BPMN 2.0 theo `so_do.md` mục 4: mỗi actor ở bảng trên một lane, bước hệ thống HIS tự làm đặt trong lane "Hệ thống HIS". Tối đa khoảng 15 bước một sơ đồ (`so_do.md` mục 4.4); pathway dài hơn thì tách quy trình con (ví dụ "Cận lâm sàng" thành sơ đồ riêng). Viết `diagrams/<tên>.json`, sinh `.bpmn` và ảnh bằng `bpmn_tool.py build diagrams/<tên>.json --png diagrams/<tên>.png`.

Bản mô tả cho ví dụ pathway Ngoại trú:

```json
{
  "id": "opd_tobe", "name": "Pathway Ngoại trú (OPD)", "pool": "[Tên bệnh viện]",
  "lanes": [
    {"id": "tiep_nhan", "name": "Tiếp nhận"}, {"id": "bac_si", "name": "Bác sĩ"},
    {"id": "ktv", "name": "Kỹ thuật viên xét nghiệm"}, {"id": "he_thong", "name": "Hệ thống HIS"},
    {"id": "duoc", "name": "Dược sĩ"}, {"id": "thu_ngan", "name": "Thu ngân"}
  ],
  "nodes": [
    {"id": "start", "type": "start", "name": "Bệnh nhân đến phòng khám", "lane": "tiep_nhan"},
    {"id": "t1", "type": "user", "name": "Đăng ký bệnh nhân", "lane": "tiep_nhan"},
    {"id": "g1", "type": "xor", "name": "Có thẻ BHYT?", "lane": "tiep_nhan"},
    {"id": "t2", "type": "service", "name": "Tra cứu thẻ BHYT", "lane": "he_thong"},
    {"id": "t3", "type": "user", "name": "Thu phí dịch vụ", "lane": "thu_ngan"},
    {"id": "m1", "type": "xor", "name": "", "lane": "bac_si"},
    {"id": "t4", "type": "user", "name": "Khám và ghi nhận triệu chứng", "lane": "bac_si"},
    {"id": "g2", "type": "xor", "name": "Cần xét nghiệm?", "lane": "bac_si"},
    {"id": "t5", "type": "user", "name": "Chỉ định xét nghiệm", "lane": "bac_si"},
    {"id": "t6", "type": "manual", "name": "Lấy mẫu và thực hiện xét nghiệm", "lane": "ktv"},
    {"id": "t7", "type": "user", "name": "Trả kết quả xét nghiệm", "lane": "ktv"},
    {"id": "m2", "type": "xor", "name": "", "lane": "bac_si"},
    {"id": "t8", "type": "user", "name": "Chẩn đoán theo ICD-10", "lane": "bac_si"},
    {"id": "m3", "type": "xor", "name": "", "lane": "bac_si"},
    {"id": "t9", "type": "user", "name": "Kê đơn thuốc", "lane": "bac_si"},
    {"id": "t10", "type": "business_rule", "name": "Kiểm tra tương tác thuốc (mục 3)", "lane": "he_thong"},
    {"id": "g3", "type": "xor", "name": "Có tương tác thuốc?", "lane": "he_thong"},
    {"id": "t11", "type": "send", "name": "Cảnh báo bác sĩ", "lane": "he_thong"},
    {"id": "t12", "type": "user", "name": "Duyệt đơn và cấp phát thuốc", "lane": "duoc"},
    {"id": "t13", "type": "user", "name": "Tính viện phí và thanh toán", "lane": "thu_ngan"},
    {"id": "end", "type": "end", "name": "Bệnh nhân nhận thuốc và ra về", "lane": "thu_ngan"}
  ],
  "flows": [
    ["start", "t1"], ["t1", "g1"], ["g1", "t2", "Có"], ["g1", "t3", "Không"], ["t2", "m1"], ["t3", "m1"],
    ["m1", "t4"], ["t4", "g2"], ["g2", "t5", "Có"], ["g2", "m2", "Không"], ["t5", "t6"], ["t6", "t7"], ["t7", "m2"],
    ["m2", "t8"], ["t8", "m3"], ["m3", "t9"], ["t9", "t10"], ["t10", "g3"],
    ["g3", "t11", "Có"], ["g3", "t12", "Không"], ["t11", "m3"], ["t12", "t13"], ["t13", "end"]
  ]
}
```

Chèn vào tài liệu: ảnh `![Pathway <tên>](diagrams/<tên>.png)`, ngay dưới là câu "Bản chuẩn BPMN 2.0: [`diagrams/<tên>.bpmn`](diagrams/<tên>.bpmn), mở và sửa bằng bpmn.io hoặc Camunda Modeler.", lệnh sinh lại ảnh để trong chú thích HTML (`so_do.md` mục 4.3).

---

## 3. Drug-Drug Interaction (DDI) Rules

| # | Loại tương tác | Severity | Hành động hệ thống | BS có thể override? |
|---|---------------|:--------:|-------------------|:-------------------:|
| 1 | Chống chỉ định tuyệt đối | 🔴 Critical | BLOCK + Alert | ❌ Không |
| 2 | Tương tác nghiêm trọng | 🟠 Major | WARNING + Lý do bắt buộc | ✅ Có (ghi lý do) |
| 3 | Tương tác trung bình | 🟡 Moderate | INFO popup | ✅ Có |
| 4 | Tương tác nhẹ | 🔵 Minor | Log only | — |

---

## 4. Data Flow per Pathway

| Từ | Đến | Dữ liệu | Chuẩn | Frequency |
|----|-----|---------|-------|:---------:|
| HIS | LIS | Chỉ định XN (Order) | HL7 FHIR `ServiceRequest` | Per event |
| LIS | HIS | Kết quả XN | HL7 FHIR `DiagnosticReport` | Per event |
| HIS | Pharmacy | Đơn thuốc | HL7 FHIR `MedicationRequest` | Per event |
| HIS | BHYT | Hồ sơ thanh toán | API BHYT (XML) | Batch daily |

---

## ✅ Review Checklist

```
☐ Tất cả pathways chính đã có workflow map (sơ đồ BPMN 2.0, bpmn_tool.py check không còn lỗi)
☐ Mỗi pathway có: Trigger, End state, Actors, SLA
☐ Rủi ro y khoa đã ghi rõ per bước → Patient Safety
☐ DDI rules đã spec severity + override policy
☐ Exception flow cover ≥ 3 scenarios per pathway
☐ Data flow mapping giữa modules theo chuẩn HL7 FHIR
☐ Clinical Validation sign-off (xem multi-level-acceptance.md)
```
