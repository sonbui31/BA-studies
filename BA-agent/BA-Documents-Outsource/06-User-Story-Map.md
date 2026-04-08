# USER STORY MAP — DỰ ÁN OUTSOURCE
# Dự án [Tên dự án]

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **⚠️ Chốt phạm vi (Baseline):** Sau khi KH phê duyệt, thêm/bỏ story = Yêu cầu thay đổi (CR)

---

## 1. Hướng dẫn — Story Map trong Outsource

### So sánh cách viết: Nội bộ vs Gia công

| Yếu tố | Nội bộ | Gia công |
|---------|--------|----------|
| Mức chi tiết | Vừa đủ, hỏi thêm khi cần | **Chi tiết cao** — Dev không ngồi cạnh để hỏi |
| Định dạng TC | "Chấp nhận khi..." (không chính thức) | **BDD Gherkin** (Given/When/Then) — rõ ràng, kiểm thử được |
| Edge case | Thêm dần khi dev hỏi | **Ghi từ đầu** — Dev sẽ xây đúng theo đặc tả |
| Ref Wireframe | Tùy chọn | **Bắt buộc** — mỗi story phải liên kết đến wireframe |
| Ước lượng | Story points | Story points + **quy đổi man-day** (cho thanh toán) |

### Luồng trạng thái Story (Gia công)

```
Nháp → Phân tích xong → KH duyệt → Trong Sprint → Dev xong → QC đã test → PO chấp nhận
                          ↑                                                      │
                          │              Nếu PO từ chối                         │
                          └─────────────────────────────────────────────────────┘
```

---

## 2. Phân rã Epic & Tính năng

### EPIC 1: [Tên Epic — VD: Xác thực & Quản lý người dùng]

#### Tính năng 1.1: [Đăng ký người dùng]

| Mã | Story | Tiêu chí chấp nhận | Ưu tiên | Ước lượng (SP) | Sprint | Wireframe |
|----|-----------|---------------------|---------|----------------|--------|-----------|
| US-001 | Là **[Vai trò]**, tôi muốn **[hành động]** để **[giá trị]** | **Given** [ngữ cảnh]<br>**When** [hành động]<br>**Then** [kết quả]<br><br>**Given** [ngữ cảnh lỗi]<br>**When** [hành động sai]<br>**Then** [xử lý lỗi] | P0 | 5 | S1 | [Figma#S-001] |
| US-002 | Là **[Vai trò]**, tôi muốn **[hành động]** để **[giá trị]** | **Given** ...<br>**When** ...<br>**Then** ... | P0 | 3 | S1 | [Figma#S-002] |
| US-003 | Là **[Vai trò]**, tôi muốn **[hành động]** để **[giá trị]** | **Given** ...<br>**When** ...<br>**Then** ... | P1 | 5 | S2 | [Figma#S-003] |

**Ghi chú cho đội phát triển:**
- [Ghi chú kỹ thuật hoặc nghiệp vụ mà Dev cần biết]
- [Phụ thuộc API: cần [API bên thứ 3] cho tính năng này]

---

#### Tính năng 1.2: [Đăng nhập & Xác thực]

| Mã | Story | Tiêu chí chấp nhận | Ưu tiên | Ước lượng (SP) | Sprint | Wireframe |
|----|-----------|---------------------|---------|----------------|--------|-----------|
| US-010 | Là **[Vai trò]**, tôi muốn **[hành động]** để **[giá trị]** | **Given** ...<br>**When** ...<br>**Then** ... | P0 | 3 | S1 | [Figma#S-010] |
| US-011 | Là **[Vai trò]**, tôi muốn **[hành động]** để **[giá trị]** | **Given** ...<br>**When** ...<br>**Then** ... | P0 | 5 | S1 | [Figma#S-011] |

---

### EPIC 2: [Tên Epic — VD: Module nghiệp vụ chính]

_(Thêm Epics tương tự)_

---

## 3. Phân bổ Phiên bản & Sprint

```
╔══════════════════════════════════════════════════════════════╗
║ PHIÊN BẢN 1 (MVP) — Sprint 1-4                              ║
║ 💰 Mốc thanh toán M2 (25%)                                      ║
║                                                              ║
║  S1: Xác thực + CRUD cơ bản                [XX SP]          ║
║  S2: Tính năng module chính                 [XX SP]          ║
║  S3: Dashboard + Báo cáo              [XX SP]          ║
║  S4: Tích hợp + Sửa lỗi + UAT              [XX SP]          ║
╠══════════════════════════════════════════════════════════════╣
║ PHIÊN BẢN 2 — Sprint 5-8                                    ║
║ 💰 Mốc thanh toán M3 (25%)                                      ║
║                                                              ║
║  S5: Tính năng nâng cao                     [XX SP]          ║
║  S6: Module bổ sung                         [XX SP]          ║
║  S7: Hoàn thiện + Edge case           [XX SP]          ║
║  S8: Tích hợp đầy đủ + UAT                 [XX SP]          ║
╠══════════════════════════════════════════════════════════════╣
║ VẬN HÀNH + BẢO HÀNH                                         ║
║ 💰 Mốc thanh toán M4 (15%)                                      ║
║                                                              ║
║  Triển khai sản xuất                                         ║
║  Bảo hành: 30-90 ngày                                       ║
║  Sửa lỗi (Nghiêm trọng/Lớn)                                ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 4. Tóm tắt ước lượng

### Quy đổi Story Points → Man-day

| Sprint | Tổng SP | Tốc độ (SP/Sprint) | Man-day | Trạng thái |
|--------|---------|---------------------|-----------|-----------|
| S1 | [XX] | — | [XX] | Lên kế hoạch |
| S2 | [XX] | [Thực tế từ S1] | [XX] | Lên kế hoạch |
| S3 | [XX] | [Trung bình lăn] | [XX] | Lên kế hoạch |
| S4 | [XX] | [Trung bình lăn] | [XX] | Lên kế hoạch |
| **Tổng PB1** | **[XX]** | | **[XX]** | |
| S5-S8 | [XX] | | [XX] | Lên kế hoạch |
| **Tổng PB2** | **[XX]** | | **[XX]** | |
| **TỔNG CỘNG** | **[XX]** | | **[XX]** | |

> **Tỷ lệ quy đổi:** 1 SP ≈ [X] giờ công (hiệu chỉnh sau Sprint 1)
> **⚠️ Lưu ý gia công:** Ước lượng man-day ảnh hưởng trực tiếp đến chi phí — phải xem xét kỹ với KH

---

## 5. Theo dõi trạng thái Backlog

| Mã | Story | Sprint | Dev | QC | PO chấp nhận | Ghi chú |
|----|-----------|--------|-----|-----|-------------|---------|
| US-001 | [Tiêu đề] | S1 | ☐ | ☐ | ☐ | |
| US-002 | [Tiêu đề] | S1 | ☐ | ☐ | ☐ | |
| US-010 | [Tiêu đề] | S1 | ☐ | ☐ | ☐ | |
| US-020 | [Tiêu đề] | S2 | ☐ | ☐ | ☐ | |

---

## 6. Phê duyệt — Chốt phạm vi bản đồ câu chuyện

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Người đại diện KH (Product Owner) | Khách hàng | | | |
| Quản lý dự án (PM) | Nhà cung cấp | | | |
| Trưởng nhóm Phân tích (BA Lead) | Nhà cung cấp | | | |

> **Quy tắc:** Thêm/xóa/thay đổi story sau khi chốt phạm vi (baseline) → Yêu cầu thay đổi → đánh giá ảnh hưởng chi phí
