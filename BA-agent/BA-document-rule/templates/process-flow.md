# PROCESS FLOW — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft

---

## 1. Tổng quan quy trình

| # | Quy trình | As-Is | To-Be | Mức ưu tiên |
|---|----------|-------|-------|------------|
| 1 | {{Tên quy trình}} | ☐ Đã mô tả | ☐ Đã mô tả | Must / Should |

---

## 2. Quy trình {{Tên quy trình 1}}

### 2.1 As-Is — Quy trình hiện tại

> Mô tả cách hoạt động HIỆN TẠI (trước khi có hệ thống).

**Tóm tắt:** {{Mô tả ngắn quy trình hiện tại}}

**Pain points:**
- ❌ {{Pain point 1}}
- ❌ {{Pain point 2}}

> Vẽ bằng BPMN 2.0 theo `so_do.md` mục 4. Viết bản mô tả `diagrams/{{tên}}-asis.json`, sinh `.bpmn` và ảnh bằng `bpmn_tool.py build diagrams/{{tên}}-asis.json --png diagrams/{{tên}}-asis.png`. Bước gây điểm đau ghi `"highlight": "pain"`. Sơ đồ chưa được SME xác nhận thì ghi `[CẦN XÁC NHẬN]` cạnh tên sơ đồ.

Khung bản mô tả (đủ trường xem `so_do.md` mục 4.2):

```json
{
  "id": "{{ten}}_asis", "name": "As-Is: {{Tên quy trình}}", "pool": "{{Tên tổ chức}}",
  "lanes": [{"id": "vt1", "name": "{{Vai trò 1}}"}, {"id": "vt2", "name": "{{Vai trò 2}}"}],
  "nodes": [
    {"id": "start", "type": "start", "name": "{{Sự kiện kích hoạt}}", "lane": "vt1"},
    {"id": "a1", "type": "manual", "name": "{{Bước 1}}", "lane": "vt1"},
    {"id": "a2", "type": "manual", "name": "{{Bước 2 gây điểm đau}}", "lane": "vt2", "highlight": "pain"},
    {"id": "g1", "type": "xor", "name": "{{Điều kiện}}?", "lane": "vt2"},
    {"id": "end_ok", "type": "end", "name": "{{Kết quả khi đạt}}", "lane": "vt2"},
    {"id": "end_no", "type": "end", "name": "{{Kết quả khi không đạt}}", "lane": "vt2"}
  ],
  "flows": [["start", "a1"], ["a1", "a2"], ["a2", "g1"], ["g1", "end_ok", "Có"], ["g1", "end_no", "Không"]]
}
```

Chèn vào tài liệu:

```markdown
![As-Is: {{Tên quy trình}}](diagrams/{{tên}}-asis.png)

Bản chuẩn BPMN 2.0: [`diagrams/{{tên}}-asis.bpmn`](diagrams/{{tên}}-asis.bpmn), mở và sửa bằng bpmn.io hoặc Camunda Modeler. Ô viền đỏ là bước gây điểm đau.

<!-- Sinh lại ảnh (chạy trong thư mục bộ tài liệu): python ../scripts/bpmn_tool.py build diagrams/{{tên}}-asis.json --png diagrams/{{tên}}-asis.png -->
```

### 2.2 Gap Analysis — So sánh As-Is vs To-Be

| Bước | As-Is (hiện tại) | Vấn đề | To-Be (tương lai) | Cải tiến |
|------|-----------------|--------|-------------------|---------|
| {{Bước 1}} | {{Cách làm hiện tại}} | {{Vấn đề}} | {{Cách làm mới}} | {{Lợi ích}} |

### 2.3 To-Be — Quy trình tương lai

> Mô tả cách hoạt động SAU KHI có hệ thống.

**Cải tiến chính:**
- ✅ {{Cải tiến 1}}
- ✅ {{Cải tiến 2}}

> Cùng pool và cùng tên lane với As-Is. Bước hệ thống tự làm đặt trong lane "Hệ thống" (`"type": "service"`); bước mới so với As-Is ghi `"highlight": "new"`; cổng rẽ nhánh theo quy tắc nghiệp vụ ghi mã BR trong tên cổng. Sinh bằng `bpmn_tool.py build diagrams/{{tên}}-tobe.json --png diagrams/{{tên}}-tobe.png`.

Chèn vào tài liệu:

```markdown
![To-Be: {{Tên quy trình}}](diagrams/{{tên}}-tobe.png)

Bản chuẩn BPMN 2.0: [`diagrams/{{tên}}-tobe.bpmn`](diagrams/{{tên}}-tobe.bpmn), mở và sửa bằng bpmn.io hoặc Camunda Modeler.

<!-- Sinh lại ảnh (chạy trong thư mục bộ tài liệu): python ../scripts/bpmn_tool.py build diagrams/{{tên}}-tobe.json --png diagrams/{{tên}}-tobe.png -->
```

---

## 3. Quy ước sơ đồ

> Quy trình giao khách vẽ bằng BPMN 2.0; ký hiệu, bản mô tả `.json` và quy tắc mô hình nằm ở `BA-agent/so_do.md` mục 4. Phác thảo nhanh bằng Mermaid (BPMN-lite, mục 4.5) chỉ dùng trong buổi trao đổi, không đưa vào tài liệu giao khách.

| Thành phần BPMN 2.0 | `type` trong `.json` | Dùng cho |
|-----------|------|---------|
| Pool, Lane | `"pool"`, `"lanes"` | Tổ chức chủ quy trình; mỗi lane một vai trò chịu trách nhiệm |
| Start Event | `start`, `start_timer`, `start_message` | Sự kiện kích hoạt |
| End Event | `end` | Mỗi kết quả nghiệp vụ một sự kiện kết thúc |
| Task | `user`, `manual`, `service`, `send`, `business_rule` | Bước công việc |
| Exclusive Gateway (X) | `xor` | Rẽ đúng một nhánh, tên là câu hỏi |
| Parallel Gateway (+) | `and` | Các nhánh chạy cùng lúc, có cặp tách và hợp |
| Inclusive Gateway (O) | `or` | Một hoặc nhiều nhánh theo điều kiện |
| Boundary Timer | `boundary_timer` | Quá hạn mà bước chưa xong |

### 8 câu hỏi vàng khi thu thập quy trình

```
1. Quy trình BẮT ĐẦU khi nào?           → Start
2. BƯỚC TIẾP THEO là gì?                 → Flow
3. Có trường hợp ĐI KHÁC ĐƯỜNG không?    → Decision ◇
4. AI thực hiện bước này?                 → Lane
5. Nếu LỖI xảy ra thì sao?              → Exception
6. Quy trình KẾT THÚC khi nào?           → End
7. Bước nào HỆ THỐNG TỰ LÀM?            → Automation
8. Cần THÔNG TIN GÌ từ bước trước?       → Data flow
```

---

## ✅ Review Checklist

```
☐ Mọi quy trình chính đều có As-Is + To-Be
☐ Gap Analysis so sánh rõ ràng
☐ Diagram có Start + End
☐ Decision node có ĐỦ nhánh
☐ Mỗi bước nằm trong lane của vai trò chịu trách nhiệm
☐ Happy path đi thẳng, exception rẽ ngang
☐ Pain points As-Is được giải quyết ở To-Be
☐ bpmn_tool.py check diagrams không còn lỗi; ảnh .png khớp bản .bpmn
```
