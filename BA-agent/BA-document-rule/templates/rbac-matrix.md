# RBAC MATRIX — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Tác giả:** {{Tên BA}} | **Trạng thái:** Draft
> **Dự án:** {{Tên dự án}}

---

## 1. Mục đích

Tài liệu này định nghĩa vai trò, quyền truy cập, phạm vi dữ liệu và quy tắc phân quyền để Dev/QC triển khai và kiểm thử nhất quán.

## 2. Role Catalog

| Role ID | Role Name | Mô tả | Người dùng điển hình | Cấp dữ liệu |
|---------|-----------|-------|----------------------|-------------|
| ROLE-001 | {{Admin}} | {{Mô tả}} | {{}} | All |
| ROLE-002 | {{Manager}} | {{Mô tả}} | {{}} | Department |
| ROLE-003 | {{Viewer}} | {{Mô tả}} | {{}} | Own / Assigned |

## 3. Permission Catalog

| Permission ID | Module | Action | Mô tả | Trace FR |
|---------------|--------|--------|-------|----------|
| PERM-001 | {{Module}} | Create | {{}} | FR-{{MOD}}-001 |
| PERM-002 | {{Module}} | Read | {{}} | FR-{{MOD}}-002 |
| PERM-003 | {{Module}} | Update | {{}} | FR-{{MOD}}-003 |
| PERM-004 | {{Module}} | Delete / Deactivate | {{}} | FR-{{MOD}}-004 |
| PERM-005 | {{Module}} | Approve | {{}} | FR-{{MOD}}-005 |

## 4. Role-Permission Matrix

| Permission | Admin | Manager | Staff | Viewer | Ghi chú |
|------------|:-----:|:-------:|:-----:|:------:|---------|
| PERM-001 Create {{Entity}} | ✅ | ✅ | ✅ | ❌ | {{}} |
| PERM-002 Read {{Entity}} | ✅ | ✅ | ✅ | ✅ | Theo data scope |
| PERM-003 Update {{Entity}} | ✅ | ✅ | Own | ❌ | {{}} |
| PERM-004 Delete {{Entity}} | ✅ | ❌ | ❌ | ❌ | Soft delete nếu có lịch sử |
| PERM-005 Approve {{Entity}} | ✅ | ✅ | ❌ | ❌ | Không tự approve nếu là người tạo |

## 5. Data Scope Rules

| Rule ID | Role | Scope | Điều kiện | Exception |
|---------|------|-------|-----------|-----------|
| DS-001 | Admin | All records | Luôn áp dụng | Audit log vẫn giới hạn theo policy |
| DS-002 | Manager | Department records | User thuộc phòng ban | Cross-department cần approval |
| DS-003 | Staff | Own / Assigned records | Người tạo hoặc được giao | {{}} |

## 6. Segregation of Duties

| Rule ID | Mô tả | Áp dụng cho | Hành vi hệ thống |
|---------|-------|-------------|------------------|
| SOD-001 | Người tạo không được tự phê duyệt | {{Workflow}} | Disable nút Approve và ghi audit |
| SOD-002 | Người sửa cấu hình không được duyệt cấu hình đó | {{Admin Config}} | Yêu cầu approver khác |

## 7. Negative Permission Test Cases

| TC ID | Given | When | Then |
|-------|-------|------|------|
| TC-RBAC-001 | User không có PERM-004 | Gọi API delete | API trả 403 và ghi audit |
| TC-RBAC-002 | Staff truy cập record ngoài scope | Mở URL trực tiếp | Hệ thống trả 403/404 theo security policy |

## Review Checklist

```
☐ Mọi role có mô tả và data scope
☐ Mọi permission trace về FR
☐ Có rule Segregation of Duties nếu có phê duyệt
☐ Có negative test cho quyền bị từ chối
☐ API, UI và UAT dùng cùng một Permission ID
```
