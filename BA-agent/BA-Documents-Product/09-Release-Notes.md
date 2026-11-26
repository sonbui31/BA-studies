# RELEASE NOTES
# SignalDesk

> **Cập nhật liên tục theo mỗi Release**
> Thay thế Change Log truyền thống — Product dùng Release Notes hướng đến user.

---

## Template cho mỗi Release

---

## v{{X.Y.Z}} — {{DD/MM/YYYY}}

### 🚀 New Features
- **{{Feature Name}}**: {{Mô tả ngắn, user-friendly — không dùng thuật ngữ kỹ thuật}}
- **{{Feature Name}}**: {{Mô tả}}

### 🔧 Improvements
- {{Cải tiến 1}}
- {{Cải tiến 2}}

### 🐛 Bug Fixes
- Fix: {{Mô tả bug đã sửa — từ góc nhìn user}}
- Fix: {{Mô tả}}

### ⚠️ Breaking Changes (nếu có)
- {{Thay đổi có thể ảnh hưởng đến user/API}}

### 📊 Metrics Impact (Nội bộ)
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| {{metric}} | {{value}} | {{value}} | {{+/-X%}} |

---

## Change Request Log (Nội bộ)

> Cho nội bộ team — tracking scope changes.

| CR-ID | Ngày | Người đề xuất | Mô tả | Impact | Status |
|-------|------|--------------|-------|--------|--------|
| CR-001 | | | | | |

### CR Form (Khi cần)

```markdown
### CR-[NNN]: [Tiêu đề]

**Người đề xuất:** ___
**Source:** User feedback / Data insight / Competitor / Internal

**Mô tả thay đổi:**
[Điều cần thay đổi]

**Data/Evidence:**
[Dữ liệu hỗ trợ — analytics, user quotes, support tickets]

**Impact:**
- OKR affected: {{OKR}}
- User Stories affected: {{US-IDs}}
- Sprint: {{Sprint number}}

**Decision:**
☐ Ship it | ☐ Defer | ☐ Rejected
```

---

## Lịch sử Release

Chưa có bản nào phát hành; bảng dưới là kế hoạch theo `02-BRD.md` mục 11 và `06-User-Story-Map.md` (Release Mapping). Ngày thật ghi khi phát hành.

| Version | Date | Highlights | Type |
|---------|------|------------|------|
| v0.9.0 | Dự kiến sau Sprint 4 | Beta kín cho 5% workspace: portal, gợi ý và gộp feedback trùng, thông báo đổi trạng thái, release note gắn feedback | Beta |
| v1.0.0 | Dự kiến sau 2 tuần beta kín và 1 tuần beta mở (20% workspace) | Ra mắt cho 100% workspace khi đạt KR kích hoạt | Major |
| v1.1.0 | Dự kiến sau Sprint 5 | Saved filters (F06) | Minor |
