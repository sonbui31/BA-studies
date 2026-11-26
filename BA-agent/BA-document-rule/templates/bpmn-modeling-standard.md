# BPMN MODELING STANDARD — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Chuẩn hóa cách vẽ và review quy trình để tài liệu As-Is/To-Be rõ actor, event, task, gateway, exception và handoff.

**Công cụ của dự án này:** BPMN 2.0, file `.bpmn` (bpmn.io / Camunda Modeler) theo `so_do.md` mục 4, sinh và kiểm tra bằng `scripts/bpmn_tool.py`. [Nếu khách bắt buộc draw.io: ghi lý do; khi đó `.drawio` là bản chuẩn.] Mermaid BPMN-lite chỉ dùng để phác thảo trong lúc trao đổi (`so_do.md` mục 4.5).

## 2. Notation Rules

| Thành phần | Dùng khi | Quy tắc đặt tên | Phác thảo Mermaid (BPMN-lite) |
|------------|----------|-----------------|---------------------|
| Start Event | Bắt đầu quy trình | Sự kiện kích hoạt, không phải hành động | `S(("..."))` lớp `startEvt` |
| Timer / Message Event | Chờ thời gian hoặc chờ tin nhắn | "Chờ: 48 giờ", "Nhận email xác nhận" | `W(["..."])` hoặc điều kiện trong gateway |
| Task | Một vai trò thực hiện một hành động | Động từ + đối tượng | `T["<b>Vai trò</b><br/>..."]` lớp `role1`…`role4`, hệ thống lớp `sys` |
| Exclusive Gateway (XOR) | Đúng một nhánh được đi | Câu hỏi; mỗi nhánh có nhãn điều kiện, phủ hết khả năng | `G{"Câu hỏi?"}` lớp `gateway` |
| Parallel Gateway (AND) | Các nhánh chạy cùng lúc | Luôn có cặp tách và hợp | `P1{"+"}` … `P2{"+"}` |
| Inclusive Gateway (OR) | Một hoặc nhiều nhánh | Ghi rõ điều kiện từng nhánh | Không có trong BPMN-lite: tách thành nhiều XOR hoặc vẽ BPMN 2.0 |
| End Event | Kết thúc quy trình | Kết quả nghiệp vụ; mỗi kết quả một sự kiện | `E((("...")))` lớp `endEvt` |
| Pool/Lane | Phân tách tổ chức/role | Tên phòng ban hoặc role | Màu và tên in đậm của bước (chỉ khi phác thảo); quy trình giao khách luôn vẽ BPMN 2.0 có pool/lane |

## 3. Process Decomposition

Định nghĩa L0–L3, tài liệu nào dùng level nào và quy tắc dừng phân rã: `core/process-decomposition-guide.md` (file chủ). Bảng dưới ghi level áp dụng cho dự án này.

| Level | Tên (theo process-decomposition-guide) | Đặt ở | Quy trình của dự án |
|-------|----------------------------------------|-------|---------------------|
| L0 | Value Chain | Vision & Scope | {{}} |
| L1 | Process Group | Vision & Scope, BRD | {{}} |
| L2 | Process Detail (BPMN 2.0 có pool/lane) | BRD, Process Flow, SRS | {{}} |
| L3 | Task/Work Instruction | SRS, User Story/AC, UAT | {{}} |

## 4. Gateway Checklist

| Gateway ID | Loại (XOR/AND/OR) | Câu hỏi điều kiện | Các nhánh và điều kiện | Nhánh mặc định | BR quyết định | Exception |
|------------|----------------|-------------------|------------------------|----------------|---------------|-----------|
| GW-001 | XOR | {{Điều kiện có đạt không?}} | {{Có: ... / Không: ...}} | {{}} | {{BR-xxx}} | {{}} |

## 5. Exception Catalog

| Exception ID | Xảy ra tại bước | Điều kiện | Hành động hệ thống/người dùng | SLA |
|--------------|-----------------|-----------|-------------------------------|-----|
| EX-001 | {{Task}} | {{}} | {{}} | {{}} |

## 6. Handoff Matrix

| From Lane | To Lane | Artifact/Data chuyển giao | Điều kiện chuyển | Risk |
|-----------|---------|---------------------------|------------------|------|
| {{Role A}} | {{Role B}} | {{}} | {{}} | {{}} |

## Review Checklist

```
☐ Mỗi task có đúng một owner/lane
☐ Gateway có điều kiện và nhánh rõ ràng; cổng song song có điểm hợp
☐ Chờ thời gian có hạn và có hành động khi quá hạn
☐ `bpmn_tool.py check diagrams` không còn lỗi; ảnh PNG đã xuất lại sau lần sửa cuối
☐ Exception path được thể hiện, không chỉ happy path
☐ Handoff giữa lane có data/artifact cụ thể
☐ L0-L3 không bị trộn trong cùng một sơ đồ
```
