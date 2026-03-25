# CÔNG CỤ KHUYẾN NGHỊ CHO BA

> **Mục đích:** Tham khảo công cụ phù hợp cho từng mục đích

---

## 1. Theo mục đích sử dụng

| Mục đích | Công cụ miễn phí | Công cụ trả phí | Ghi chú |
|---------|-----------------|----------------|---------|
| **Quản lý yêu cầu** | Trello, GitHub Issues | Jira, Azure DevOps, Linear | Jira phổ biến nhất |
| **Tài liệu** | Google Docs, Notion (free) | Confluence, Notion (team) | Confluence + Jira = combo |
| **Wireframe** | Draw.io, Excalidraw | Figma, Balsamiq, Axure | Figma miễn phí cho cá nhân |
| **Process Flow** | Draw.io, Mermaid (markdown) | Lucidchart, Bizagi Modeler | Mermaid = tích hợp trong markdown |
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
| Diagram | **Mermaid** (trong markdown) | Không cần tool riêng |

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
| Process | **Bizagi** hoặc **Camunda** | BPMN standards |

---

## 3. Mermaid Quick Reference

> Dùng trong Markdown files — không cần tool bên ngoài.

| Loại | Syntax | Dùng cho |
|------|--------|---------|
| Flowchart | `` ```mermaid flowchart TD `` | Process Flow, Activity |
| Sequence | `` ```mermaid sequenceDiagram `` | API flow, Integration |
| ERD | `` ```mermaid erDiagram `` | Data Model |
| State | `` ```mermaid stateDiagram-v2 `` | Entity lifecycle |
| Gantt | `` ```mermaid gantt `` | Timeline |
| Journey | `` ```mermaid journey `` | User Journey |

> Chi tiết cú pháp: xem `core/diagram-guide.md`
