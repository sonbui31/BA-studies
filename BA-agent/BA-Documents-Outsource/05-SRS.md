# ĐẶC TẢ YÊU CẦU PHẦN MỀM (SRS)
# Dự án Gia công: Hệ thống Quản lý Tài sản Bệnh viện

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Trạng thái:** Baseline 1.0 — đã ký mục 8 ngày 05/03/2026; bản 1.1 là nháp theo CR-001, chờ duyệt
> **Người chịu trách nhiệm:** Nguyễn Văn A — BA Lead
> **Hợp đồng tham chiếu:** HD-AP-2026-018
> **Tier:** 2 — điểm rủi ro 3/7 (câu 3, 5, 7): hợp đồng outsource giá cố định có mốc thanh toán gắn nghiệm thu, tích hợp SSO và máy in barcode chưa xác nhận; hệ thống không lưu dữ liệu sức khỏe người bệnh
> **Nhãn:** [TÀI LIỆU MẪU] — ví dụ minh họa cấu trúc, không phải dự án thật
> **⚠️ Đây là tài liệu CHỐT PHẠM VI (Baseline) — mọi thay đổi sau khi phê duyệt phải qua quy trình Yêu cầu thay đổi (CR)**

---

## 1. Tổng quan

### 1.1. Mục đích
Đặc tả yêu cầu phần mềm chi tiết cho dự án **Quản lý Tài sản Bệnh viện** — đủ để đội phát triển NCC phát triển mà **giảm thiểu cần giao tiếp thời gian thực** với KH (đặc điểm gia công).

### 1.2. Đối tượng đọc

| Đối tượng | Đọc phần |
|-----------|---------|
| Người đại diện KH (PO) / Nhà tài trợ (Sponsor) | Mục 1-4, 7 (phạm vi, tính năng, phê duyệt) |
| Đội phát triển NCC | Mục 2-6 (chi tiết chức năng, yêu cầu phi chức năng, dữ liệu, API) |
| QC NCC | Mục 2-3, 5 (tiêu chí chấp nhận, NFR, quy tắc xác nhận) |
| BA NCC | Toàn bộ |

### 1.3. Tài liệu tham chiếu

| Tài liệu | Mã/Link | Phiên bản |
|-----------|---------|-----------|
| Tầm nhìn & Phạm vi | 01-Vision-Scope.md | v1.0 đã ký |
| BRD | 02-BRD.md | v1.0 đã ký |
| Quy trình nghiệp vụ | 04-Process-Flow.md | v1.0 đã ký |
| Story Map | 06-User-Story-Map.md | v1.0 |
| Wireframe/Prototype | Figma / AP Asset v7 | v7 |

### 1.4. Thuật ngữ & Viết tắt

| Thuật ngữ | Giải thích |
|-----------|------------|
| Tài sản | Thiết bị, máy móc, tài sản CNTT hoặc vật tư giá trị cao cần theo dõi vòng đời |
| Khoa sở hữu | Khoa/phòng chịu trách nhiệm sử dụng tài sản tại thời điểm hiện tại |
| Đợt kiểm kê | Phiên kiểm kê có ngày bắt đầu, ngày khóa sổ, và người phê duyệt |

### 1.5. Tổng quan kiến trúc

```mermaid
%%{init: {"theme": "base", "fontFamily": "Arial, Helvetica, sans-serif", "themeVariables": {"fontSize": "15px", "primaryColor": "#FFFFFF", "primaryBorderColor": "#4A5568", "primaryTextColor": "#1A202C", "lineColor": "#4A5568", "secondaryColor": "#F7FAFC", "tertiaryColor": "#F7FAFC", "clusterBkg": "#F7FAFC", "clusterBorder": "#A0AEC0", "edgeLabelBackground": "#FFFFFF", "actorBkg": "#EBF8FF", "actorBorder": "#2B6CB0", "noteBkgColor": "#FFF8E1", "noteBorderColor": "#B7791F"}}}%%
flowchart LR
    User[Người dùng khoa / Vật tư / Ban điều hành]
    Web[Web App]
    API[Backend API]
    DB[(Asset DB)]
    Job[Scheduler / Notification]
    Audit[(Audit Log)]

    User --> Web
    Web --> API
    API --> DB
    API --> Audit
    Job --> API
    Job --> DB
```

### 1.6. Bối cảnh dữ liệu

- `Asset` là thực thể gốc của hệ thống.
- `AssetTransfer`, `AssetMaintenance`, và `InventorySession` là các thực thể nghiệp vụ chính phát sinh từ `Asset`.
- Mọi thay đổi trạng thái tài sản phải ghi audit log và người thao tác.

---

## 2. Yêu cầu chức năng

> **Quy ước ưu tiên:**
> - **P0 (Bắt buộc):** Phải có, ảnh hưởng mốc thanh toán
> - **P1 (Nên có):** Quan trọng, nên có trước vận hành
> - **P2 (Có thể):** Tốt nếu có, có thể hoãn sang giai đoạn sau

### 2.1. Module 1: Danh mục và Đăng ký tài sản

**Goal:** Chuẩn hóa hồ sơ tài sản và mã định danh ngay từ thời điểm tạo mới.
**Actors:** Nhân viên Vật tư, Quản trị, Điều dưỡng trưởng khoa.
**Dependencies:** Danh mục khoa/phòng, danh mục nhóm tài sản, phân quyền người dùng.

#### Tính năng 1.1: Tạo hồ sơ tài sản

| Mã | Yêu cầu | Mô tả chi tiết | Ưu tiên | Source BRQ | Primary Actor | Ref Wireframe |
|----|---------|-----------------|---------|------------|---------------|---------------|
| FR-AST-001 | Tạo hồ sơ tài sản mới | Precondition: người dùng có quyền `asset.create`. Trigger: người dùng mở form tạo tài sản. Main flow: nhập thông tin nhận diện, nhóm tài sản, khoa sở hữu, ngày mua, giá trị, bảo hành. Exception: thiếu trường bắt buộc hoặc mã tài sản trùng. Postcondition: tài sản ở trạng thái `Available` và có mã duy nhất. | P0 | BRQ-01 | Nhân viên Vật tư | S-001 |
| FR-AST-002 | Tạo mã barcode cho tài sản | Precondition: FR-AST-001 thành công. Trigger: người dùng chọn `Sinh mã`. Main flow: hệ thống tạo barcode; hệ thống gắn barcode vào hồ sơ tài sản; hệ thống trả file in tem cho người dùng. Exception: lỗi kết nối dịch vụ in tem. Postcondition: hồ sơ tài sản lưu barcode cùng trạng thái in tem. | P0 | BRQ-02 | Nhân viên Vật tư | S-002 |
| FR-AST-003 | Phân loại tài sản theo nhóm | Precondition: danh mục nhóm tài sản có sẵn. Trigger: người dùng chọn nhóm tài sản. Main flow: hệ thống áp dụng rule hiển thị trường phù hợp theo loại. Exception: nhóm tài sản bị vô hiệu hóa. Postcondition: tài sản có classification phục vụ báo cáo và SLA bảo trì. | P1 | BRQ-03 | Nhân viên Vật tư | S-003 |

**Quy tắc nghiệp vụ:**
- BR-001: Mỗi tài sản chỉ có một mã định danh duy nhất trong toàn viện. Ref BRQ-01.
- BR-004: Thiết bị y tế nhóm quan trọng phải khai báo chu kỳ bảo trì. Ref BRQ-07.

**Quy tắc xác nhận:**
- VR-101: `asset_code` là bắt buộc và không được trùng.
- VR-102: `purchase_date` không được lớn hơn ngày hiện tại.
- VR-103: Nếu `asset_group = medical_device_critical` thì `maintenance_cycle_days` là bắt buộc.

**Tiêu chí chấp nhận (FR-AST-001):**
```gherkin
Scenario: Happy path - tạo tài sản mới
  Given nhân viên Vật tư đã đăng nhập và có quyền tạo tài sản
  When người dùng nhập đầy đủ thông tin hợp lệ và bấm Lưu
  Then hệ thống tạo hồ sơ tài sản mới ở trạng thái Available
    And ghi audit log với người tạo và thời gian tạo

Scenario: Negative - trùng mã tài sản
  Given đã tồn tại tài sản với mã AP-TS-0001
  When người dùng nhập lại mã AP-TS-0001
  Then hệ thống chặn lưu
    And hiển thị thông báo "Mã tài sản đã tồn tại"

Scenario: Boundary - thiếu chu kỳ bảo trì cho thiết bị quan trọng
  Given người dùng chọn nhóm tài sản là thiết bị y tế quan trọng
  When người dùng để trống chu kỳ bảo trì
  Then hệ thống không cho lưu

Scenario: Permission - người dùng khoa không có quyền tạo tài sản
  Given người dùng thuộc vai trò Người dùng khoa
  When truy cập chức năng tạo tài sản
  Then hệ thống từ chối truy cập
```

**Sequence flow**

```mermaid
%%{init: {"theme": "base", "fontFamily": "Arial, Helvetica, sans-serif", "themeVariables": {"fontSize": "15px", "primaryColor": "#FFFFFF", "primaryBorderColor": "#4A5568", "primaryTextColor": "#1A202C", "lineColor": "#4A5568", "secondaryColor": "#F7FAFC", "tertiaryColor": "#F7FAFC", "clusterBkg": "#F7FAFC", "clusterBorder": "#A0AEC0", "edgeLabelBackground": "#FFFFFF", "actorBkg": "#EBF8FF", "actorBorder": "#2B6CB0", "noteBkgColor": "#FFF8E1", "noteBorderColor": "#B7791F"}}}%%
sequenceDiagram
    participant U as Nhân viên Vật tư
    participant W as Web App
    participant A as Asset API
    participant D as Asset DB
    participant L as Audit Log
    U->>W: Nhập thông tin tài sản
    W->>A: POST /assets
    A->>D: kiểm tra mã trùng + lưu dữ liệu
    D-->>A: asset_id
    A->>L: ghi log tạo tài sản
    A-->>W: success + asset_id
    W-->>U: Hiển thị hồ sơ tài sản
```

---

#### Tính năng 1.2: Quản lý danh mục và phân quyền truy cập

| Mã | Yêu cầu | Mô tả chi tiết | Ưu tiên | Source BRQ | Primary Actor | Ref Wireframe |
|----|---------|-----------------|---------|------------|---------------|---------------|
| FR-ADM-001 | Quản lý danh mục khoa/phòng và nhóm tài sản | Precondition: người dùng có quyền cấu hình. Trigger: vào màn hình cấu hình. Main flow: tạo/sửa/vô hiệu hóa danh mục. Exception: không cho vô hiệu hóa khi còn asset active tham chiếu. Postcondition: danh mục mới có hiệu lực cho các form nghiệp vụ. | P0 | BRQ-01 | Quản trị | S-004 |
| FR-ADM-002 | Phân quyền theo vai trò | Precondition: role matrix đã được cấu hình. Trigger: người dùng đăng nhập. Main flow: hệ thống cấp quyền theo vai trò. Exception: vai trò bị vô hiệu hóa. Postcondition: người dùng chỉ thấy chức năng được cấp. | P0 | BRQ-04 | Quản trị | S-005 |

---

### 2.2. Module 2: Điều chuyển và Kiểm kê

**Goal:** Khóa trách nhiệm sở hữu tài sản và rút ngắn thời gian kiểm kê.
**Actors:** Người dùng khoa, Trưởng khoa, Nhân viên Vật tư.
**Dependencies:** Asset master, role matrix, barcode.

#### Tính năng 2.1: Điều chuyển tài sản

| Mã | Yêu cầu | Mô tả chi tiết | Ưu tiên | Source BRQ | Primary Actor | Ref Wireframe |
|----|---------|-----------------|---------|------------|---------------|---------------|
| FR-TRF-001 | Tạo yêu cầu điều chuyển | Precondition: tài sản đang active và có khoa sở hữu. Trigger: người dùng khoa hoặc Vật tư tạo yêu cầu điều chuyển. Main flow: chọn tài sản, khoa nhận, lý do, ngày dự kiến. Exception: tài sản đang bảo trì hoặc ở trạng thái `PendingDisposal` theo BR-003. Postcondition: yêu cầu ở trạng thái `Pending Approval`. | P0 | BRQ-04 | Người dùng khoa | S-010 |
| FR-TRF-002 | Xác nhận giao và nhận bàn giao | Precondition: FR-TRF-001 đã được phê duyệt. Trigger: bên giao xác nhận theo BR-002, sau đó bên nhận xác nhận. Main flow: hệ thống ghi nhận xác nhận của bên giao; hệ thống ghi nhận xác nhận của bên nhận; hệ thống cập nhật khoa sở hữu mới. Exception: quá hạn xác nhận hoặc một bên từ chối. Postcondition: hệ thống cập nhật lịch sử sở hữu và audit log. | P0 | BRQ-04 | Trưởng khoa / Vật tư | S-011 |
| FR-INV-001 | Tạo đợt kiểm kê và chốt chênh lệch | Precondition: Nhân viên Vật tư có danh sách tài sản active của khoa. Trigger: Nhân viên Vật tư mở đợt kiểm kê. Main flow: quét barcode hoặc đánh dấu thủ công, ghi lệch theo BR-005, gửi xác nhận. Exception: tài sản không tìm thấy hoặc barcode sai. Postcondition: đợt kiểm kê có báo cáo lệch và trạng thái khóa sổ. | P0 | BRQ-05, BRQ-06 | Nhân viên Vật tư | S-012 |

**Quy tắc nghiệp vụ:**
- BR-002: Điều chuyển chỉ hoàn tất khi bên giao và bên nhận cùng xác nhận.
- BR-005: Chênh lệch kiểm kê phải được phân loại trước khi khóa sổ.

**Tiêu chí chấp nhận (FR-TRF-002)**
```gherkin
Scenario: Happy path - điều chuyển hoàn tất
  Given yêu cầu điều chuyển đã được phê duyệt
  When bên giao và bên nhận cùng xác nhận
  Then hệ thống cập nhật khoa sở hữu mới
    And ghi lịch sử điều chuyển

Scenario: Negative - tài sản đang bảo trì
  Given tài sản ở trạng thái Under Maintenance
  When người dùng tạo yêu cầu điều chuyển
  Then hệ thống chặn tạo yêu cầu

Scenario: Exception - quá hạn xác nhận
  Given yêu cầu điều chuyển đã quá hạn 48 giờ
  When bên nhận chưa xác nhận
  Then hệ thống cảnh báo cho Vật tư và Trưởng khoa
```

---

### 2.3. Module 3: Bảo trì và Báo cáo điều hành

**Goal:** Giảm dừng thiết bị và hỗ trợ quyết định ngân sách.
**Actors:** Nhân viên Vật tư, Ban điều hành, Kỹ sư bảo trì.

| Mã | Yêu cầu | Mô tả chi tiết | Ưu tiên | Source BRQ | Primary Actor | Ref Wireframe |
|----|---------|-----------------|---------|------------|---------------|---------------|
| FR-MNT-001 | Lập lịch bảo trì định kỳ | Precondition: tài sản có chu kỳ bảo trì. Trigger: hệ thống scheduler chạy hằng ngày. Main flow: xác định tài sản sắp đến hạn theo BR-004, tạo nhắc việc. Exception: tài sản đang dừng sử dụng hoặc chờ thanh lý. Postcondition: có work item bảo trì và cảnh báo. | P0 | BRQ-07, BRQ-08 | Scheduler / Vật tư | S-020 |
| FR-MNT-002 | Ghi nhận kết quả bảo trì | Precondition: Nhân viên Vật tư hoặc kỹ sư có lịch bảo trì mở. Trigger: Nhân viên Vật tư hoặc kỹ sư cập nhật kết quả. Main flow: nhập ngày thực hiện, nội dung, chi phí, trạng thái. Exception: chi phí vượt ngưỡng cần phê duyệt. Postcondition: lịch sử bảo trì cập nhật, hạn bảo trì kế tiếp được tính lại. | P0 | BRQ-07, BRQ-08 | Nhân viên Vật tư | S-021 |
| FR-RPT-001 | Dashboard điều hành | Precondition: hệ thống đã ghi nhận dữ liệu nghiệp vụ. Trigger: Ban điều hành mở dashboard. Main flow: hệ thống hiển thị tổng số tài sản, tổng giá trị, tài sản sắp bảo trì, tài sản lệch kiểm kê theo bộ lọc khoa/thời gian. Exception: người dùng không có quyền executive dashboard. Postcondition: dashboard lưu bộ lọc cuối cùng của người dùng. | P1 | BRQ-09 | Ban điều hành | S-022 |

### 2.4. Mô hình dữ liệu tóm tắt

| Entity | Purpose | Key fields |
|---|---|---|
| Asset | Hồ sơ tài sản gốc | asset_id, asset_code, asset_group, owner_department_id, status |
| AssetTransfer | Lịch sử điều chuyển | transfer_id, asset_id, from_department_id, to_department_id, approved_at |
| InventorySession | Phiên kiểm kê | session_id, department_id, started_at, closed_at, status |
| InventoryResult | Kết quả từng tài sản trong đợt kiểm kê | session_id, asset_id, result_type, comment |
| MaintenanceOrder | Phiếu/lịch bảo trì | maintenance_id, asset_id, due_date, completed_at, vendor |

### 2.5. State machine

```mermaid
%%{init: {"theme": "base", "fontFamily": "Arial, Helvetica, sans-serif", "themeVariables": {"fontSize": "15px", "primaryColor": "#FFFFFF", "primaryBorderColor": "#4A5568", "primaryTextColor": "#1A202C", "lineColor": "#4A5568", "secondaryColor": "#F7FAFC", "tertiaryColor": "#F7FAFC", "clusterBkg": "#F7FAFC", "clusterBorder": "#A0AEC0", "edgeLabelBackground": "#FFFFFF", "actorBkg": "#EBF8FF", "actorBorder": "#2B6CB0", "noteBkgColor": "#FFF8E1", "noteBorderColor": "#B7791F"}}}%%
stateDiagram-v2
    [*] --> Available
    Available --> Assigned
    Assigned --> PendingTransfer
    PendingTransfer --> Assigned
    Assigned --> UnderMaintenance
    UnderMaintenance --> Assigned
    Assigned --> PendingDisposal
    PendingDisposal --> Disposed
```

### 2.6. Ma trận thực thi quy tắc nghiệp vụ (BR → FR → TC)

| Mã BR | Quy tắc (tóm tắt) | FR thực thi | Cách thực thi | Kịch bản kiểm chứng |
|---|---|---|---|---|
| BR-001 | Mỗi tài sản có một mã định danh duy nhất | FR-AST-001, FR-AST-002 | VR-101 chặn trùng `asset_code`; barcode sinh từ mã duy nhất | TC-AST-001, TC-AST-002 |
| BR-002 | Điều chuyển chỉ hoàn tất khi bên giao và bên nhận cùng xác nhận | FR-TRF-002 | Khoa sở hữu chỉ đổi sau xác nhận thứ hai | TC-TRF-002 |
| BR-003 | Tài sản `Chờ thanh lý` không được cấp phát lại | FR-TRF-001 | Chặn tạo yêu cầu điều chuyển khi tài sản ở trạng thái `PendingDisposal` | TC-TRF-003 |
| BR-004 | Thiết bị y tế quan trọng phải có lịch bảo trì và cảnh báo trước tối thiểu 15 ngày | FR-AST-001, FR-MNT-001 | VR-103 bắt buộc chu kỳ bảo trì; scheduler tạo cảnh báo trước hạn 15 ngày | TC-AST-003, TC-MNT-001 |
| BR-005 | Chênh lệch kiểm kê phải được phân loại trước khi khóa sổ | FR-INV-001 | Không cho chốt đợt kiểm kê khi còn dòng lệch chưa phân loại | TC-INV-001 |

---

## 3. Yêu cầu phi chức năng

| Mã | Danh mục | Yêu cầu | Chỉ tiêu | Cách xác minh | Nguồn BRQ |
|----|----------|---------|----------|---------------|-----------|
| NFR-PERF-001 | **Hiệu năng** | Dashboard tài sản phải tải xong trong mạng nội bộ | ≤ 3 giây | Lighthouse / synthetic monitoring | BRQ-09 |
| NFR-PERF-002 | **Hiệu năng** | API đọc/ghi tài sản phải phản hồi trong thời gian ngắn | ≤ 500ms (p95) | Báo cáo load test | BRQ-01 |
| NFR-PERF-003 | **Hiệu năng** | Hệ thống phải chịu tải đồng thời | ≥ 250 người dùng | Kiểm thử K6/JMeter | BRQ-05 |
| NFR-AVL-001 | **Khả dụng** | Khi đo theo tháng vận hành 06:00-22:00, hệ thống phải duy trì uptime cho người dùng | ≥ 99.5% uptime/tháng | Công cụ giám sát | BRQ-04 |
| NFR-SCAL-001 | **Mở rộng** | Khi số lượng tài sản tăng từ 15.000 đến 150.000, hệ thống phải giữ thời gian tra cứu một tài sản | ≤ 3 giây và không cần đổi mô hình dữ liệu | Rà soát kiến trúc | BRQ-01 |
| NFR-SEC-001 | **Bảo mật** | Người dùng quản trị phải xác thực bằng cơ chế MFA và token hợp lệ | SSO nội bộ hoặc local auth với JWT và MFA | Kiểm tra bảo mật | BRQ-04 |
| NFR-SEC-002 | **Bảo mật** | Hệ thống phải phân quyền theo vai trò và chặn truy cập trái quyền | 6 vai trò cốt lõi, không lộ chức năng trái quyền | Kịch bản kiểm thử | BRQ-04 |
| NFR-SEC-003 | **Bảo mật** | Dữ liệu phải được mã hóa | TLS 1.2+ khi truyền, AES-256 khi lưu | Quét bảo mật | BRQ-01 |
| NFR-SEC-004 | **Bảo mật** | Khi quét bản phát hành trước go-live, hệ thống không được còn lỗ hổng mức nghiêm trọng hoặc cao | 0 lỗi Critical/High theo OWASP ZAP | Quét OWASP ZAP | BRQ-01 |
| NFR-AUD-001 | **Kiểm toán** | Khi người dùng tạo, sửa, xóa, điều chuyển, kiểm kê, hoặc bảo trì tài sản, hệ thống phải lưu audit log | Tối thiểu 5 năm | Rà soát nhật ký | BRQ-04, BRQ-06 (C3) |
| NFR-USAB-001 | **Khả năng sử dụng** | Giao diện phải hiển thị đúng bố cục trên di động, máy tính bảng, và máy tính | Di động, máy tính bảng, máy tính | Kiểm thử trình duyệt | BRQ-05 |
| NFR-USAB-002 | **Khả năng sử dụng** | Khi truy cập bằng trình duyệt chuẩn, các màn hình P0 phải hiển thị đúng và thao tác được | Chrome, Safari, Firefox, Edge - 2 phiên bản mới nhất | Kiểm thử đa trình duyệt | BRQ-01 |
| NFR-REL-001 | **Tin cậy** | Hệ thống phải sao lưu dữ liệu định kỳ | Hằng ngày, giữ 30 ngày | Kiểm thử sao lưu | BRQ-01 |
| NFR-REL-002 | **Tin cậy** | Hệ thống phải phục hồi sau thảm họa | RTO ≤ 4 giờ, RPO ≤ 1 giờ | Diễn tập DR | BRQ-01 |
| NFR-MAINT-001 | **Bảo trì** | Mã nguồn phải đạt chất lượng nội bộ | SonarQube Quality Gate đạt | Báo cáo CI | BRQ-01 (chất lượng bàn giao theo HĐ) |
| NFR-MAINT-002 | **Bảo trì** | Mã nguồn phải có kiểm thử tối thiểu | ≥ 80% unit test | Báo cáo CI | BRQ-01 (chất lượng bàn giao theo HĐ) |
| NFR-COMP-001 | **Tuân thủ** | Dữ liệu và retention log phải tuân thủ quy định nội bộ bệnh viện | Log tối thiểu 5 năm | Danh mục tuân thủ | BRQ-06 (C3) |

### 3.1. Áp dụng NFR theo module

| Phạm vi áp dụng | NFR | Rủi ro nếu không đạt |
|---|---|---|
| Dashboard, tra cứu, điều chuyển, kiểm kê | NFR-PERF-001, NFR-PERF-002, NFR-PERF-003 | Người dùng bỏ hệ thống, quay lại Excel |
| Tất cả module | NFR-SEC-001, NFR-SEC-002, NFR-SEC-003, NFR-AUD-001 | Rò rỉ dữ liệu, sai quyền, không audit được |
| Toàn hệ thống | NFR-REL-001, NFR-REL-002 | Mất dữ liệu tài sản, gián đoạn vận hành |

---

## 4. Phân quyền (RBAC)

### 4.1. Định nghĩa vai trò

| Vai trò | Mô tả | Tạo bởi |
|---------|--------|---------|
| **Quản trị tối cao** | Toàn quyền, quản lý hệ thống | Cài đặt sẵn |
| **Quản trị** | Quản lý người dùng, cấu hình | Quản trị tối cao |
| **Quản lý** | Xem báo cáo, phê duyệt | Quản trị |
| **Nhân viên** | Thao tác nghiệp vụ chính | Quản trị |
| **Người xem** | Chỉ đọc | Quản trị |
| **Khách hàng** | Tự đăng ký, truy cập hạn chế | Tự đăng ký |

### 4.2. Ma trận phân quyền

| Tính năng | QT tối cao | Quản trị | Quản lý | Nhân viên | Người xem | Khách hàng |
|-----------|-----------|----------|---------|-----------|-----------|-----------|
| Quản lý người dùng | CRUD | CRUD | R | — | — | — |
| Tài sản và danh mục | CRUD | CRUD | CRUD | CRUD | R | R (riêng) |
| Điều chuyển và kiểm kê | CRUD | CRUD | CRU | CR | R | — |
| Báo cáo | Toàn bộ | Toàn bộ | Phòng mình | Cá nhân | — | — |
| Cài đặt | Toàn bộ | Toàn bộ | — | — | — | — |
| Audit Log | R | R | — | — | — | — |

> **Chú thích:** C=Tạo, R=Đọc, U=Sửa, D=Xóa, —=Không truy cập

---

## 5. Yêu cầu tích hợp

### 5.1. API bên ngoài

| # | Hệ thống | Hướng | Giao thức | Xác thực | Chủ quản | Trạng thái |
|---|---------|-------|-----------|----------|----------|-----------|
| INT-01 | Dịch vụ email cảnh báo | Gửi đi | SMTP / API | API Key | NCC | Sandbox sẵn sàng |
| INT-02 | AD/SSO bệnh viện | Nhận vào | OIDC/SAML | Client ID + Secret | CNTT KH | Chờ xác nhận |
| INT-03 | Hệ thống kế toán tài sản (giai đoạn sau) | Hai chiều | REST/SFTP | Service Account | KH | Out of scope PB1 |
| INT-04 | Công cụ monitoring | Gửi đi | Webhook | Token | NCC | Sẵn sàng |
| INT-05 | Máy in barcode | Gửi đi | Local print / service | LAN trusted | KH | Cần khảo sát |

### 5.2. API do NCC xây dựng

| # | Nhóm Endpoint | Mô tả | Người sử dụng |
|---|-------------|-------|---------------|
| API-01 | /api/v1/auth/* | Xác thực & phân quyền | Frontend, Di động |
| API-02 | /api/v1/assets/* | Tài sản và danh mục CRUD | Frontend |
| API-03 | /api/v1/transfers-inventories/* | Điều chuyển và kiểm kê CRUD | Frontend |
| API-04 | /api/v1/reports/* | Tạo báo cáo | Frontend, Bộ lập lịch |
| API-05 | /api/v1/webhooks/* | Nhận webhook | Bên thứ 3 |

> **Sản phẩm:** Swagger/OpenAPI spec phải được giao cùng khi phê duyệt SRS.
> **Integration rules:** Timeout mặc định 10 giây; retry tối đa 2 lần cho email/webhook; không retry tự động với thao tác tạo điều chuyển nếu đã ghi dữ liệu nghiệp vụ.

---

## 6. Yêu cầu giao diện

### 6.1. Hệ thống thiết kế

| Hạng mục | Đặc tả | Tham chiếu |
|----------|--------|-----------|
| Màu chính | #0F766E theo quy chuẩn thương hiệu bệnh viện | Tài liệu thương hiệu |
| Kiểu chữ | Inter, kích thước theo thành phần | Hệ thống thiết kế |
| Bộ biểu tượng | Material Icons | — |
| Điểm ngắt responsive | Di động: ≤768px, Máy tính bảng: 769-1024px, Máy tính: ≥1025px | — |

### 6.2. Màn hình chính (Ref Wireframe)

| Mã MH | Tên màn hình | Module | Link Wireframe | Ưu tiên |
|-------|-------------|--------|----------------|---------|
| S-001 | Danh sách tài sản | Danh mục tài sản | Figma/AP-001 | P0 |
| S-002 | Tạo/Sửa hồ sơ tài sản | Danh mục tài sản | Figma/AP-002 | P0 |
| S-003 | Điều chuyển tài sản | Điều chuyển | Figma/AP-010 | P0 |
| S-004 | Kiểm kê theo khoa | Kiểm kê | Figma/AP-011 | P0 |
| S-005 | Dashboard điều hành | Báo cáo | Figma/AP-020 | P1 |

---

## 7. Ma trận truy vết (RTM)

> ⚠️ **Bắt buộc trong gia công:** Đảm bảo mỗi yêu cầu trong BRD/Hợp đồng đều có triển khai + kiểm thử

| Mục BRQ | Mã FR/NFR | Wireframe | Story | Kịch bản KT | Trạng thái |
|---------|-----------|-----------|-------|-------------|-----------|
| BRQ-01 | FR-AST-001 | S-001, S-002 | US-AST-001 | TC-AST-001 | ☐ |
| BRQ-01 | FR-ADM-001 | S-004 | US-ADM-001 | TC-ADM-001 | ☐ |
| BRQ-02 | FR-AST-002 | S-002 | US-AST-002 | TC-AST-002 | ☐ |
| BRQ-03 | FR-AST-003 | S-002 | US-AST-003 | TC-AST-003 | ☐ |
| BRQ-04 | FR-TRF-001 | S-003 | US-TRF-001 | TC-TRF-001, TC-TRF-003 | ☐ |
| BRQ-04 | FR-TRF-002 | S-003 | US-TRF-002 | TC-TRF-002 | ☐ |
| BRQ-04 | FR-ADM-002 | S-005 | US-ADM-002 | TC-ADM-002 | ☐ |
| BRQ-05 | FR-INV-001 | S-004 | US-INV-001 | TC-INV-001 | ☐ |
| BRQ-06 | FR-INV-001 | S-004 | US-INV-002 | TC-INV-001 | ☐ |
| BRQ-07 | FR-MNT-001 | S-005 | US-MNT-001 | TC-MNT-001 | ☐ |
| BRQ-07 | FR-MNT-002 | S-005 | US-MNT-002 | TC-MNT-002 | ☐ |
| BRQ-08 | FR-MNT-001 | S-005 | US-MNT-001 | TC-MNT-001 | ☐ |
| BRQ-09 | FR-RPT-001 | S-005 | US-RPT-001 | TC-RPT-001 | ☐ |
| BRQ-09 | NFR-PERF-001 | S-005 | — | TC-NFR-001 | ☐ |
| BRQ-05 | NFR-PERF-003 | — | — | TC-NFR-001 | ☐ |
| BRQ-01 | NFR-SEC-004 | — | — | TC-NFR-003 | ☐ |

> Nguồn BRQ và kịch bản kiểm thử của toàn bộ 17 NFR: xem Mục 3 (cột Nguồn BRQ) và `08-UAT-Plan.md` Mục 5.4.

---

## 8. Phê duyệt — Chốt phạm vi SRS

> ⚠️ **Phê duyệt SRS = Chốt phạm vi yêu cầu (Baseline) = Cơ sở cho theo dõi Yêu cầu thay đổi (CR)**
> Mọi thay đổi sau thời điểm này PHẢI đi qua quy trình CR (09-Change-Log.md)

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Người đại diện KH (Product Owner) | Khách hàng | Phạm Thu Hà — Trưởng phòng Vật tư | Đã ký (bản giấy lưu PMO) | 05/03/2026 |
| Quản lý CNTT | Khách hàng | Vũ Hoàng Nam — Trưởng phòng CNTT | Đã ký (bản giấy lưu PMO) | 05/03/2026 |
| Quản lý dự án (PM) | Nhà cung cấp | Đỗ Thanh Tùng | Đã ký | 05/03/2026 |
| Trưởng nhóm Phân tích (BA Lead) | Nhà cung cấp | Nguyễn Văn A | Đã ký | 05/03/2026 |
| Trưởng nhóm Kỹ thuật (Tech Lead) | Nhà cung cấp | Hoàng Gia Khánh | Đã ký | 05/03/2026 |

> Chữ ký áp dụng cho bản 1.0. Bản 1.1 chỉ có hiệu lực khi CR-001 được duyệt trong `09-Change-Log.md` (H6). Tên người ký là dữ liệu minh họa của tài liệu mẫu.

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Mã CR | Người |
|-----------|------|----------|-------|-------|
| 0.1 | 27/02/2026 | Draft đầu tiên | — | BA |
| 0.2 | 03/03/2026 | Cập nhật theo phản hồi KH | — | BA |
| 1.0 | 05/03/2026 | **Đã phê duyệt — Chốt phạm vi** (chữ ký ở mục 8) | — | BA |
| 1.1 | 12/03/2026 | Nháp: bổ sung kiểm thử NFR cho hiệu năng, bảo mật, phục hồi và bảo trì; chờ duyệt CR-001 | CR-001 | BA |
