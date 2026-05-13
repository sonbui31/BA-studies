# USER STORY MAP — DỰ ÁN OUTSOURCE
# Dự án Hệ thống Quản lý Tài sản Bệnh viện

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

### EPIC 1: Danh mục và Đăng ký tài sản

#### Tính năng 1.1: Tạo và phân loại tài sản

| Mã | Story | Tiêu chí chấp nhận | Ref BRD | Ref FR | Ưu tiên | Ước lượng (SP) | Sprint | Wireframe |
|----|-----------|---------------------|---------|--------|---------|----------------|--------|-----------|
| US-001 | As a **Nhân viên Vật tư**, I want **tạo hồ sơ tài sản mới** so that **mọi tài sản có hồ sơ chuẩn ngay khi tiếp nhận** | **Happy:** Given tôi có quyền tạo tài sản<br>**When** nhập đủ trường bắt buộc và bấm Lưu<br>**Then** hệ thống tạo tài sản mới và ghi audit log<br><br>**Negative:** Given mã tài sản đã tồn tại<br>**When** tôi lưu hồ sơ<br>**Then** hệ thống báo trùng mã<br><br>**Boundary:** Given tôi để trống chu kỳ bảo trì cho thiết bị quan trọng<br>**When** lưu hồ sơ<br>**Then** hệ thống chặn lưu | BRD-101 | FR-101 | P0 | 5 | S1 | Figma/AP-001 |
| US-002 | As a **Nhân viên Vật tư**, I want **sinh và in barcode** so that **tài sản được kiểm kê nhanh và chính xác** | **Happy:** Given hồ sơ tài sản đã được tạo<br>**When** tôi chọn Sinh mã<br>**Then** hệ thống tạo barcode và file in tem<br><br>**Exception:** Given dịch vụ in tem lỗi<br>**When** tôi gửi lệnh in<br>**Then** hệ thống báo lỗi nhưng không mất hồ sơ tài sản | BRD-102 | FR-102 | P0 | 3 | S1 | Figma/AP-002 |
| US-003 | As a **Nhân viên Vật tư**, I want **phân loại tài sản theo nhóm** so that **hệ thống áp dụng đúng quy tắc bảo trì và báo cáo** | **Happy:** Given danh mục nhóm tài sản hợp lệ<br>**When** tôi chọn nhóm thiết bị<br>**Then** hệ thống hiển thị đúng trường nghiệp vụ bắt buộc<br><br>**Permission:** Given nhóm tài sản bị vô hiệu hóa<br>**When** tôi chọn nhóm đó<br>**Then** hệ thống không cho lưu | BRD-103 | FR-103 | P1 | 3 | S1 | Figma/AP-002 |

**Ghi chú cho đội phát triển:**
- [Ghi chú kỹ thuật hoặc nghiệp vụ mà Dev cần biết]
- Barcode phải theo format `BVAP-<group>-<running number>`.
- Không cho sửa `asset_code` sau khi đã có kiểm kê hoặc điều chuyển phát sinh.

---

#### Tính năng 1.2: Quản lý danh mục và quyền truy cập

| Mã | Story | Tiêu chí chấp nhận | Ref BRD | Ref FR | Ưu tiên | Ước lượng (SP) | Sprint | Wireframe |
|----|-----------|---------------------|---------|--------|---------|----------------|--------|-----------|
| US-004 | As a **Quản trị**, I want **quản lý danh mục khoa và nhóm tài sản** so that **dữ liệu master luôn đúng** | **Happy:** Given tôi có quyền cấu hình<br>**When** tôi thêm hoặc sửa danh mục<br>**Then** hệ thống cập nhật danh mục cho các form nghiệp vụ<br><br>**Negative:** Given danh mục đang được asset active tham chiếu<br>**When** tôi vô hiệu hóa danh mục<br>**Then** hệ thống chặn thao tác | BRD-101 | FR-104 | P0 | 3 | S1 | Figma/AP-003 |
| US-005 | As a **Quản trị**, I want **phân quyền theo vai trò** so that **người dùng chỉ thao tác trong phạm vi được cấp** | **Happy:** Given role matrix đã cấu hình<br>**When** người dùng đăng nhập<br>**Then** hệ thống chỉ hiển thị đúng quyền chức năng<br><br>**Permission:** Given người dùng khoa truy cập màn hình cấu hình<br>**When** mở URL trực tiếp<br>**Then** hệ thống từ chối truy cập | BRD-201 | FR-105 | P0 | 5 | S1 | Figma/AP-004 |

---

### EPIC 2: Điều chuyển và Kiểm kê

#### Tính năng 2.1: Điều chuyển tài sản

| Mã | Story | Tiêu chí chấp nhận | Ref BRD | Ref FR | Ưu tiên | Ước lượng (SP) | Sprint | Wireframe |
|----|-----------|---------------------|---------|--------|---------|----------------|--------|-----------|
| US-011 | As a **Người dùng khoa**, I want **tạo yêu cầu điều chuyển tài sản** so that **tài sản được chuyển đúng quy trình** | **Happy:** Given tài sản đang active<br>**When** tôi tạo yêu cầu điều chuyển<br>**Then** hệ thống tạo yêu cầu ở trạng thái Pending Approval<br><br>**Negative:** Given tài sản đang bảo trì<br>**When** tôi tạo yêu cầu<br>**Then** hệ thống chặn thao tác | BRD-201 | FR-201 | P0 | 5 | S2 | Figma/AP-010 |
| US-012 | As a **Trưởng khoa/Vật tư**, I want **xác nhận giao và nhận tài sản** so that **trách nhiệm sở hữu được cập nhật rõ** | **Happy:** Given yêu cầu điều chuyển đã được duyệt<br>**When** cả hai bên xác nhận<br>**Then** hệ thống cập nhật khoa sở hữu mới<br><br>**Exception:** Given một bên chưa xác nhận sau 48 giờ<br>**When** yêu cầu quá hạn<br>**Then** hệ thống gửi cảnh báo SLA | BRD-201 | FR-202 | P0 | 5 | S2 | Figma/AP-011 |

#### Tính năng 2.2: Kiểm kê tài sản

| Mã | Story | Tiêu chí chấp nhận | Ref BRD | Ref FR | Ưu tiên | Ước lượng (SP) | Sprint | Wireframe |
|----|-----------|---------------------|---------|--------|---------|----------------|--------|-----------|
| US-021 | As a **Nhân viên Vật tư**, I want **mở đợt kiểm kê theo khoa** so that **bệnh viện kiểm kê theo kỳ có kiểm soát** | **Happy:** Given danh sách tài sản khoa đã sẵn sàng<br>**When** tôi tạo đợt kiểm kê<br>**Then** hệ thống sinh danh sách kiểm kê theo khoa<br><br>**Boundary:** Given barcode không khớp<br>**When** tôi quét tài sản<br>**Then** hệ thống đánh dấu cần xác minh | BRD-202 | FR-203 | P0 | 8 | S3 | Figma/AP-012 |
| US-022 | As a **Nhân viên Vật tư**, I want **phân loại chênh lệch kiểm kê** so that **mọi lệch kiểm kê có hướng xử lý rõ** | **Happy:** Given có tài sản lệch kiểm kê<br>**When** tôi chốt kết quả<br>**Then** hệ thống yêu cầu chọn loại lệch `Mất/Hỏng/Sai vị trí/Chờ xác minh` | BRD-203 | FR-203 | P0 | 3 | S3 | Figma/AP-013 |

### EPIC 3: Bảo trì và Dashboard điều hành

| Mã | Story | Tiêu chí chấp nhận | Ref BRD | Ref FR | Ưu tiên | Ước lượng (SP) | Sprint | Wireframe |
|----|-----------|---------------------|---------|--------|---------|----------------|--------|-----------|
| US-031 | As a **Nhân viên Vật tư**, I want **lập lịch bảo trì tự động** so that **thiết bị không bị trễ hạn bảo trì** | **Happy:** Given tài sản có chu kỳ bảo trì<br>**When** đến mốc cảnh báo<br>**Then** hệ thống tạo nhắc việc và gửi email cảnh báo | BRD-301 | FR-301 | P0 | 5 | S4 | Figma/AP-020 |
| US-032 | As a **Nhân viên Vật tư**, I want **ghi nhận kết quả bảo trì** so that **lịch sử sửa chữa và chi phí được lưu lại** | **Happy:** Given có work item bảo trì mở<br>**When** tôi hoàn tất và cập nhật kết quả<br>**Then** hệ thống tính lại ngày bảo trì kế tiếp | BRD-301 | FR-302 | P0 | 5 | S4 | Figma/AP-021 |
| US-033 | As a **Ban điều hành**, I want **xem dashboard tài sản** so that **tôi ra quyết định mua mới, điều chuyển, thanh lý kịp thời** | **Happy:** Given tôi có quyền executive dashboard<br>**When** mở màn hình dashboard<br>**Then** hệ thống hiển thị số lượng, giá trị, trạng thái, tài sản sắp bảo trì, tài sản lệch kiểm kê | BRD-303 | FR-303 | P1 | 5 | S4 | Figma/AP-022 |

---

## 3. Phân bổ Phiên bản & Sprint

```
╔══════════════════════════════════════════════════════════════╗
║ PHIÊN BẢN 1 (MVP) — Sprint 1-4                              ║
║ 💰 Mốc thanh toán M2 (25%)                                      ║
║                                                              ║
║  S1: Danh mục + Đăng ký tài sản              [19 SP]        ║
║  S2: Điều chuyển tài sản                      [10 SP]        ║
║  S3: Kiểm kê + xử lý lệch                     [11 SP]        ║
║  S4: Bảo trì + Dashboard + UAT               [15 SP]        ║
╠══════════════════════════════════════════════════════════════╣
║ PHIÊN BẢN 2 — Sprint 5-8                                    ║
║ 💰 Mốc thanh toán M3 (25%)                                      ║
║                                                              ║
║  S5: Mobile optimization                      [8 SP]         ║
║  S6: Tích hợp kế toán tài sản                 [13 SP]        ║
║  S7: Nâng cấp analytics + edge cases          [8 SP]         ║
║  S8: Tích hợp đầy đủ + UAT mở rộng            [10 SP]        ║
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
| S1 | 19 | — | 24 | Kế hoạch |
| S2 | 10 | 18-20 | 13 | Kế hoạch |
| S3 | 11 | 18-20 | 14 | Kế hoạch |
| S4 | 15 | 18-20 | 19 | Kế hoạch |
| **Tổng PB1** | **55** | | **70** | |
| S5-S8 | 39 | | 50 | Kế hoạch |
| **Tổng PB2** | **39** | | **50** | |
| **TỔNG CỘNG** | **94** | | **120** | |

> **Tỷ lệ quy đổi:** 1 SP ≈ 6-7 giờ công hữu hiệu, hiệu chỉnh sau Sprint 1
> **⚠️ Lưu ý gia công:** Ước lượng man-day ảnh hưởng trực tiếp đến chi phí — phải xem xét kỹ với KH

---

## 5. Theo dõi trạng thái Backlog

| # | Mã Story | Story | Sprint | Dev | QC | PO chấp nhận | Ghi chú |
|----|-----------|--------|-----|-----|-------------|---------|---------|
| 1 | US-001 | Tạo hồ sơ tài sản | S1 | ☐ | ☐ | ☐ | UAT-001 |
| 2 | US-002 | Sinh barcode | S1 | ☐ | ☐ | ☐ | UAT-002 |
| 3 | US-011 | Tạo yêu cầu điều chuyển | S2 | ☐ | ☐ | ☐ | UAT-011 |
| 4 | US-012 | Xác nhận giao/nhận | S2 | ☐ | ☐ | ☐ | UAT-012 |
| 5 | US-021 | Mở đợt kiểm kê | S3 | ☐ | ☐ | ☐ | UAT-021 |
| 6 | US-031 | Lập lịch bảo trì | S4 | ☐ | ☐ | ☐ | UAT-031 |

---

### 5.1. Traceability Matrix

| Ref BRD | Ref FR | Story | Wireframe | UAT Ref |
|---|---|---|---|---|
| BRD-101 | FR-101 | US-001 | Figma/AP-001 | UAT-001 |
| BRD-102 | FR-102 | US-002 | Figma/AP-002 | UAT-002 |
| BRD-201 | FR-201, FR-202 | US-011, US-012 | Figma/AP-010, AP-011 | UAT-011, UAT-012 |
| BRD-202 | FR-203 | US-021 | Figma/AP-012 | UAT-021 |
| BRD-301 | FR-301, FR-302 | US-031, US-032 | Figma/AP-020, AP-021 | UAT-INT-01, UAT-031 |

---

## 6. Phê duyệt — Chốt phạm vi bản đồ câu chuyện

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Người đại diện KH (Product Owner) | Khách hàng | | | |
| Quản lý dự án (PM) | Nhà cung cấp | | | |
| Trưởng nhóm Phân tích (BA Lead) | Nhà cung cấp | | | |

> **Quy tắc:** Thêm/xóa/thay đổi story sau khi chốt phạm vi (baseline) → Yêu cầu thay đổi → đánh giá ảnh hưởng chi phí
