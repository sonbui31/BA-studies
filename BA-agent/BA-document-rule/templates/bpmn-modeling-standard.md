# BPMN MODELING STANDARD — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Chuẩn hóa cách vẽ và review quy trình BPMN/Swimlane để tài liệu As-Is/To-Be rõ actor, event, task, gateway, exception và handoff.

## 2. Notation Rules

| Thành phần | Dùng khi | Quy tắc đặt tên |
|------------|----------|-----------------|
| Start Event | Bắt đầu quy trình | Sự kiện kích hoạt, không phải hành động |
| Task | Một actor thực hiện một hành động | Động từ + đối tượng |
| Gateway | Có nhánh điều kiện | Câu hỏi Yes/No hoặc điều kiện rõ |
| End Event | Kết thúc quy trình | Kết quả nghiệp vụ |
| Pool/Lane | Phân tách tổ chức/role | Tên phòng ban hoặc role |

## 3. Process Decomposition

| Level | Nội dung | Khi nào dừng |
|-------|----------|--------------|
| L0 | End-to-end value stream | Dùng cho sponsor |
| L1 | Major process | Dùng cho BRD/process flow |
| L2 | Activity groups | Dùng cho SRS/workshop |
| L3 | Task-level detail | Dùng khi cần AC/test case |

## 4. Gateway Checklist

| Gateway ID | Câu hỏi điều kiện | Nhánh Yes | Nhánh No | Default Path | Exception |
|------------|-------------------|-----------|----------|--------------|-----------|
| GW-001 | {{Điều kiện có đạt không?}} | {{}} | {{}} | {{}} | {{}} |

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
☐ Gateway có điều kiện và nhánh rõ ràng
☐ Exception path được thể hiện, không chỉ happy path
☐ Handoff giữa lane có data/artifact cụ thể
☐ L0-L3 không bị trộn trong cùng một sơ đồ
```
