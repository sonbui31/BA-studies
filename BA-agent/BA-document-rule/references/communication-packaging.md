# COMMUNICATION PACKAGING — Đóng gói Thông tin cho Từng Đối tượng (v3.3)

> **Mục đích:** Cùng 1 nội dung phân tích, BA cần "đóng gói" khác nhau cho từng đối tượng.
> **Vấn đề:** BA thường viết 1 bản rồi gửi cho tất cả → Sponsor không đọc SRS, Dev không đọc BRD.

---

## 1. Communication Matrix — Ai cần gì?

| Đối tượng | Quan tâm | Không quan tâm | Format ưu tiên | Độ dài |
|-----------|---------|---------------|----------------|:------:|
| **CEO / Sponsor** | ROI, Timeline, Risk, Go/No-Go | Technical details, API spec | Executive Summary 1-2 trang | ≤ 2 pages |
| **Product Owner** | Features, User flow, Priority, Trade-offs | Infrastructure, DB schema | Feature Brief + Prototype | 3-5 pages |
| **Dev Lead** | Architecture, API, Data Model, NFR | Business justification, ROI | Technical Brief + Diagrams | 5-10 pages |
| **QC Lead** | Test cases, Acceptance Criteria, Test data | Why we build this | Test Strategy + AC Checklist | 3-5 pages |
| **End User** | How to use, Training steps, FAQs | System architecture | Quick Start Guide + Video | ≤ 3 pages |
| **IT Ops** | Deployment, Monitoring, SLA, DR | Business rules | Runbook + SLA Dashboard | 2-3 pages |

---

## 2. Templates cho 4 Package Types

### 📋 2.1 Executive Summary (Cho CEO / Sponsor)

```markdown
# 📋 EXECUTIVE SUMMARY: [Tên Dự Án]
> **Ngày:** [DD/MM/YYYY] | **BA:** [Tên] | **Phiên bản:** [X.Y]

## Vấn đề
[2-3 câu mô tả pain point — dùng Narrative Storytelling (xem writing-guide §9)]

## Giải pháp đề xuất
[1 câu mô tả giải pháp ở mức cao nhất]

## ROI dự kiến
| Chi phí đầu tư | Tiết kiệm/năm | Payback |
|:-:|:-:|:-:|
| {{X}} triệu | {{Y}} triệu | {{N}} tháng |

## Timeline
| Milestone | Ngày | Status |
|-----------|------|:------:|
| Kick-off | {{date}} | ✅ |
| Go-live | {{date}} | ⏳ |

## Rủi ro Top 3
| # | Risk | Impact | Mitigation |
|---|------|:------:|------------|
| 1 | {{Risk}} | 🔴 | {{Action}} |

## Quyết định cần
- [ ] Phê duyệt ngân sách {{X}} triệu
- [ ] Chọn phương án: A hoặc B (xem phân tích đính kèm)
```

> **Quy tắc viết cho CEO:**
> - Không dùng thuật ngữ kỹ thuật (API, database, RBAC)
> - Mỗi số liệu phải có **so sánh**: "Giảm 60% thời gian" thay vì "Response < 3s"
> - Tối đa **1 trang A4** cho phần chính, phụ lục riêng

---

### 🔧 2.2 Technical Brief (Cho Dev Lead)

```markdown
# 🔧 TECHNICAL BRIEF: [Tên Feature/Module]
> **SRS Reference:** [Link] | **API Spec:** [Link] | **Data Model:** [Link]

## Architecture Decision
[Kiến trúc đã chọn + lý do — tham chiếu Decision Analysis nếu có]

## Key Technical Requirements
| FR/NFR ID | Name | Constraint | Impact on Code |
|-----------|------|-----------|---------------|
| FR-AST-01 | Thêm tài sản | Validate trùng Mã TS < 500ms | Cần DB index on asset_code |
| NFR-PERF-01 | API Response | p95 < 500ms @ 500 users | Cần caching + pagination |

## Data Model Changes
[ERD hoặc ALTER TABLE statements]

## API Endpoints
| Method | Path | Purpose | Auth |
|--------|------|---------|------|
| POST | /v1/assets | Tạo tài sản | Bearer + role:admin |

## Integration Points
[Hệ thống nào cần tích hợp? Contract + Timeout + Fallback]

## Open Questions for Dev
- [ ] Redis hay Memcached cho caching layer?
- [ ] Auto-generate Mã TS hay user nhập?
```

---

### ✅ 2.3 Test Strategy Brief (Cho QC Lead)

```markdown
# ✅ TEST STRATEGY BRIEF: [Tên Module]
> **Story Map Reference:** [Link] | **UAT Plan:** [Link]

## Test Scope
| In Scope | Out of Scope |
|----------|-------------|
| CRUD Tài sản | Payment integration |
| Permission checks | Third-party API load test |

## AC Coverage Summary
| Story | AC Count | Types Covered | Priority |
|-------|:--------:|:------------:|:--------:|
| US-AST-001 | 5 | Happy, Neg, Boundary, Perm, Concurrency | P1 |

## Test Data Requirements
| Data Set | Volume | Source | Preparation |
|----------|:------:|--------|-------------|
| Asset list | 1000 records | Generated | Faker.js script |
| User accounts | 5 roles × 2 users | Manual | Pre-created in staging |

## Sign-off Criteria
- [ ] 100% Must stories: All TCs PASS
- [ ] ≥ 90% Should stories: All TCs PASS
- [ ] 0 Critical / 0 High severity bugs open
- [ ] Performance test PASS (NFR-PERF targets met)
```

---

### 📖 2.4 Quick Start Guide (Cho End User)

```markdown
# 📖 HƯỚNG DẪN SỬ DỤNG NHANH: [Tên Module]
> **Thời gian đọc:** 5 phút | **Dành cho:** [Role]

## Bạn có thể làm gì?
✅ Thêm tài sản mới
✅ Tìm kiếm tài sản theo mã/tên
✅ Xem lịch sử bảo trì

## Bắt đầu trong 3 bước

### Bước 1: Đăng nhập
Mở trình duyệt → Vào [URL] → Nhập tài khoản được cấp

### Bước 2: Thêm tài sản
Menu trái → "Tài sản" → Nút "＋ Thêm mới" → Điền form → "Lưu"

### Bước 3: Tìm tài sản
Thanh tìm kiếm → Gõ mã hoặc tên → Enter → Click vào kết quả

## FAQ
**Q: Quên mật khẩu?** → Nhấn "Quên mật khẩu" ở trang đăng nhập
**Q: Không thấy nút "Thêm mới"?** → Liên hệ Admin để cấp quyền
**Q: Lỗi "Mã trùng"?** → Mã tài sản đã tồn tại, kiểm tra lại hoặc đổi mã

## Hỗ trợ
📧 Email: support@company.com | 📞 Hotline: 1900-xxxx
```

---

## 3. Khi nào tạo Package nào?

| Project Phase | Package cần tạo | Gửi cho |
|:------------:|----------------|---------|
| **Initiation** | Executive Summary | Sponsor → Approve/Reject |
| **Analysis** | — | — (tài liệu BA nội bộ) |
| **Design** | Technical Brief | Dev Lead → Estimate + Plan |
| **Pre-UAT** | Test Strategy Brief | QC Lead → Plan test |
| **Go-Live** | Quick Start Guide | End Users → Training |
| **Post-Go-Live** | PIR Summary | Sponsor → Lessons Learned |

---

## 4. Transformation Rules — Từ tài liệu BA → Package

| Từ | Section | Biến thành | Trong Package |
|----|---------|----------|--------------|
| **BRD** | Pain Points (§2.2) | Narrative 2-3 câu | Executive Summary |
| **BRD** | ROI (§7.2) | Bảng ROI 3 dòng | Executive Summary |
| **SRS** | FR list (§3) | Key constraints only | Technical Brief |
| **SRS** | NFR (§4) | Impact on code | Technical Brief |
| **Story Map** | ACs | Coverage summary | Test Strategy |
| **SRS** | Use Case (§3) | Step-by-step | Quick Start Guide |

> **Quy tắc:** BA KHÔNG viết lại nội dung — chỉ **extract + repackage** từ tài liệu đã có.

---

## 5. Lệnh Kích hoạt

```
@ba-specialist tạo Executive Summary từ BRD [file] cho Sponsor
@ba-specialist tạo Technical Brief từ SRS [file] cho Dev Lead
@ba-specialist tạo Test Strategy Brief từ Story Map [file] cho QC
@ba-specialist tạo Quick Start Guide cho module [X] từ SRS
```
