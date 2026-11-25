# CÔNG CỤ KHUYẾN NGHỊ CHO BA

> **Mục đích:** Tham khảo công cụ phù hợp cho từng mục đích

---

## 1. Theo mục đích sử dụng

| Mục đích | Công cụ miễn phí | Công cụ trả phí | Ghi chú |
|---------|-----------------|----------------|---------|
| **Quản lý yêu cầu** | Trello, GitHub Issues | Jira, Azure DevOps, Linear | Jira phổ biến nhất |
| **Tài liệu** | Google Docs, Notion (free) | Confluence, Notion (team) | Confluence + Jira = combo |
| **Wireframe** | Draw.io, Excalidraw | Figma, Balsamiq, Axure | Figma miễn phí cho cá nhân |
| **Process Flow (BPMN 2.0)** | `bpmn_tool.py`, bpmn.io, Camunda Modeler | Bizagi Modeler, Signavio | File `.bpmn` là bản chuẩn (`so_do.md` mục 4); draw.io chỉ khi khách bắt buộc, khi đó `.drawio` là bản chuẩn |
| **ERD** | dbdiagram.io, Draw.io | DataGrip, Navicat | dbdiagram.io miễn phí |
| **API Docs** | Swagger UI, Postman | Stoplight, ReadMe | Swagger/OpenAPI = chuẩn |
| **Giao tiếp** | Google Meet, Discord | Slack, Teams, Zoom | Teams nếu dùng Microsoft |
| **Whiteboard** | Excalidraw, Google Jamboard | Miro, FigJam | Miro cho workshop |
| **User Story Map** | Miro (free plan) | StoriesOnBoard, Avion | Miro linh hoạt nhất |
| **Mind Map** | XMind (free), Markmap | MindMeister, Miro | Dùng khi brainstorm |

---

## 2. Stack khuyến nghị theo quy mô

### Team nhỏ (1-5 người)

| Mục đích | Công cụ | Lý do |
|---------|---------|-------|
| Quản lý | **Trello** hoặc **Notion** | Đơn giản, miễn phí |
| Tài liệu | **Notion** hoặc **Google Docs** | Collaboration tốt |
| Wireframe | **Figma** (free) | Miễn phí, powerful |
| Quy trình nghiệp vụ | **BPMN 2.0** qua `bpmn_tool.py`, sửa bằng bpmn.io | `.bpmn` mở được ở mọi công cụ BPMN; sinh từ bản mô tả `.json` |
| Sơ đồ khác | **Mermaid** (trong markdown) | Không cần tool riêng |

### Team trung bình (5-20 người)

| Mục đích | Công cụ | Lý do |
|---------|---------|-------|
| Quản lý | **Jira** | Agile boards, sprint tracking |
| Tài liệu | **Confluence** | Tích hợp Jira, structured |
| Wireframe | **Figma** | Team collaboration |
| Workshop | **Miro** | Virtual whiteboard |

### Team lớn / Enterprise

| Mục đích | Công cụ | Lý do |
|---------|---------|-------|
| Quản lý | **Azure DevOps** hoặc **Jira** | Enterprise features |
| Tài liệu | **Confluence** | Spaces, permissions |
| Wireframe | **Figma** (Organization) | Design system |
| Process | **Camunda Modeler** hoặc **Bizagi** | Mở và sửa file `.bpmn` (BPMN 2.0) do `bpmn_tool.py` sinh |

---

## 3. Mermaid Quick Reference

> Dùng trong Markdown files — không cần tool bên ngoài.

| Loại | Syntax | Dùng cho |
|------|--------|---------|
| Flowchart | `` ```mermaid flowchart TD `` | Decision Flowchart, user flow một người dùng, phác thảo nhanh (quy trình giao khách vẽ BPMN 2.0) |
| Sequence | `` ```mermaid sequenceDiagram `` | API flow, Integration |
| ERD | `` ```mermaid erDiagram `` | Data Model |
| State | `` ```mermaid stateDiagram-v2 `` | Entity lifecycle |
| Gantt | `` ```mermaid gantt `` | Timeline |
| Journey | `` ```mermaid journey `` | User Journey |

> Chuẩn vẽ và cú pháp: `BA-agent/so_do.md`; kiểm tra bằng `scripts/diagram_check.py`
