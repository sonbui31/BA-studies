# TÀI LIỆU YÊU CẦU KINH DOANH (BRD)
# Dự án Outsource: Hệ thống Quản lý Tài sản Bệnh viện

> **Phiên bản:** 1.0 | **Ngày:** 26/02/2026
> **Tác giả:** Nguyễn Văn A — BA Lead, Nhà cung cấp
> **Khách hàng:** Bệnh viện Đa khoa An Phúc
> **Nhà cung cấp:** Công ty Giải pháp Số Sao Việt
> **Trạng thái:** Draft
> **⚠️ Tài liệu CHỐT PHẠM VI (Baseline) — mọi thay đổi sau khi phê duyệt phải qua quy trình Yêu cầu thay đổi (CR)**

---

## Lịch sử chỉnh sửa

| Phiên bản | Ngày | Thay đổi | Người | Phê duyệt bởi |
|-----------|------|----------|-------|----------------|
| 0.1 | 12/02/2026 | Draft đầu tiên | BA | — |
| 0.2 | 20/02/2026 | Cập nhật theo workshop với Khối Vật tư và CNTT | BA | — |
| 1.0 | 26/02/2026 | **Đã phê duyệt — Chốt phạm vi** | BA | Giám đốc vận hành |

---

## 1. Tóm tắt điều hành

### 1.1. Tóm tắt dự án
Hiện tại bệnh viện đang theo dõi tài sản y tế, thiết bị CNTT, và vật tư giá trị cao bằng Excel rời rạc theo từng khoa. Mỗi đợt kiểm kê cuối tháng, Phòng Vật tư phải hợp nhất nhiều file, đối chiếu giấy bàn giao, rồi gọi điện xác minh với các khoa. Quy trình này chậm, dễ sai, và không cho Ban điều hành thấy ngay tài sản nào đang hỏng, thất lạc, hoặc sắp hết hạn bảo trì.

Dự án này xây dựng một hệ thống quản lý tài sản tập trung để ghi nhận vòng đời tài sản từ mua sắm, bàn giao, điều chuyển, bảo trì, đến thanh lý. Hệ thống phục vụ ba nhóm chính: Phòng Vật tư, các khoa/phòng sử dụng tài sản, và Ban điều hành cần dashboard vận hành.

Đề xuất đầu tư nhằm đạt ba kết quả kinh doanh: giảm ít nhất 70% thời gian kiểm kê tháng, giảm tối thiểu 80% sai lệch giữa sổ theo dõi và tài sản thực tế, và tạo được báo cáo tức thời về tài sản theo khoa, trạng thái, và lịch bảo trì để hỗ trợ quyết định ngân sách.

### 1.2. Mục đích tài liệu
Tài liệu này mô tả **yêu cầu kinh doanh** cho dự án Quản lý Tài sản Bệnh viện, phục vụ:
- Làm cơ sở cho việc **phê duyệt đầu tư** từ Ban lãnh đạo
- Làm baseline cho **hợp đồng outsource** giữa Khách hàng và Nhà cung cấp
- Làm đầu vào cho **SRS** (đặc tả yêu cầu phần mềm chi tiết)

### 1.3. Đối tượng đọc

| Đối tượng | Đọc phần |
|-----------|---------|
| Ban giám đốc / Nhà tài trợ (Sponsor) | Mục 1-3, 7 (Tóm tắt, Luận chứng kinh doanh, Lợi ích đầu tư) |
| Người đại diện KH (Product Owner) / Quản lý kinh doanh | Toàn bộ |
| Quản lý dự án (PM) / Chuyên viên phân tích (BA) Nhà cung cấp | Toàn bộ |
| Đội phát triển Nhà cung cấp | Mục 4-6 (yêu cầu chi tiết) |
| Tài chính / Mua sắm | Mục 3, 7 (Chi phí-Lợi ích, Ngân sách) |
| Pháp lý | Mục 8 (Tuân thủ và giới hạn pháp lý) |

---

## 2. Bối cảnh kinh doanh

### 2.1. Tổ chức
- **Tên tổ chức:** Bệnh viện Đa khoa An Phúc
- **Ngành:** Y tế
- **Quy mô:** 650 nhân sự, 420 giường bệnh, 18 khoa/phòng chuyên môn
- **Vị trí thị trường:** Bệnh viện tư nhân quy mô vừa, đang mở thêm cơ sở vệ tinh

### 2.2. Hiện trạng
| # | Vấn đề hiện tại | Ảnh hưởng | Mức độ |
|---|-----------------|-----------|--------|
| 1 | Mỗi khoa giữ một file Excel riêng để theo dõi tài sản | Kiểm kê tháng mất 24-30 giờ công, sai lệch trung bình 12% | 🔴 Nghiêm trọng |
| 2 | Không có mã định danh thống nhất cho tài sản khi điều chuyển giữa khoa | Mất dấu tài sản, phát sinh tranh cãi trách nhiệm bàn giao | 🟠 Cao |
| 3 | Lịch bảo trì thiết bị theo dõi bằng email và lịch cá nhân | Bỏ lỡ 2-3 lịch bảo trì/tháng, tăng rủi ro dừng thiết bị | 🟠 Cao |
| 4 | Ban điều hành không có dashboard tình trạng tài sản theo thời gian thực | Quyết định mua mới và thanh lý dựa trên báo cáo chậm 5-7 ngày | 🟡 Trung bình |

### 2.3. Trạng thái mong muốn
```
HIỆN TẠI (AS-IS)                    TƯƠNG LAI (TO-BE)
──────────────────                   ──────────────────
Excel + Email + Giấy       ───▶     Hệ thống quản lý tài sản tập trung
Kiểm kê 3 ngày/tháng       ───▶     Kiểm kê bán tự động trong 1 ngày
Sai lệch 12%               ───▶     Sai lệch < 2%
Báo cáo thủ công 5-7 ngày  ───▶     Dashboard theo thời gian gần thực
Lịch bảo trì rời rạc       ───▶     Cảnh báo bảo trì theo SLA
```

### 2.4. Động lực thay đổi
- **Kinh doanh:** Giảm chi phí thất thoát và thời gian kiểm kê, chuẩn bị mở cơ sở thứ hai
- **Công nghệ:** Chuẩn hóa quản lý tài sản trên một nền tảng duy nhất, thay thế file rời
- **Pháp quy:** Cần lưu vết bàn giao, bảo trì, và thanh lý để phục vụ kiểm tra nội bộ/audit
- **Cạnh tranh:** Bệnh viện cùng phân khúc đã có dashboard thiết bị và quy trình bảo trì số hóa

---

## 3. Luận chứng kinh doanh & Phân tích chi phí-lợi ích

### 3.1. Tóm tắt luận chứng

| Tiêu chí | Chi tiết |
|----------|---------|
| **Vấn đề** | Bệnh viện không kiểm soát được vòng đời tài sản theo thời gian thực, gây thất thoát và chậm bảo trì |
| **Giải pháp** | Triển khai hệ thống quản lý tài sản tập trung có kiểm kê, điều chuyển, bảo trì, dashboard |
| **Chi phí ước tính** | 2.45 tỷ VND trong 3 năm |
| **Lợi ích ước tính** | 1.62 tỷ VND/năm từ tiết kiệm thời gian, giảm thất thoát, giảm dừng thiết bị |
| **Thời gian hoàn vốn** | 22 tháng |
| **Khuyến nghị** | **Tiến hành** nếu bệnh viện cam kết chuẩn hóa mã tài sản và bố trí đầu mối dữ liệu tại mỗi khoa |

### 3.2. Chi phí

| # | Hạng mục | Loại | Năm 1 | Năm 2 | Năm 3 |
|---|----------|------|-------|-------|-------|
| 1 | Phát triển phần mềm (NCC) | Một lần | 1.350.000.000 VND | — | — |
| 2 | Giấy phép phần mềm (barcode, monitoring) | Định kỳ | 60.000.000 VND | 60.000.000 VND | 60.000.000 VND |
| 3 | Hạ tầng / Đám mây | Định kỳ | 120.000.000 VND | 132.000.000 VND | 145.000.000 VND |
| 4 | Đào tạo nhân viên | Một lần | 90.000.000 VND | — | — |
| 5 | Chuyển đổi dữ liệu | Một lần | 180.000.000 VND | — | — |
| 6 | Bảo trì hàng năm (sau bảo hành) | Định kỳ | — | 160.000.000 VND | 160.000.000 VND |
| 7 | Nhân sự nội bộ (PO, quản trị) | Định kỳ | 75.000.000 VND | 75.000.000 VND | 75.000.000 VND |
| | **TỔNG** | | **1.875.000.000 VND** | **427.000.000 VND** | **440.000.000 VND** |

### 3.3. Lợi ích

#### Lợi ích định lượng

| # | Lợi ích | Cách tính | Giá trị/năm |
|---|---------|-----------|-------------|
| 1 | Giảm thời gian kiểm kê | 24 giờ công/tháng × 12 tháng × 350.000 VND/giờ | 100.800.000 VND/năm |
| 2 | Giảm thất thoát/sai lệch tài sản | Giảm 80% trên mức thất thoát 600.000.000 VND/năm | 480.000.000 VND/năm |
| 3 | Giảm thời gian xử lý điều chuyển/bàn giao | 180 yêu cầu/tháng × tiết kiệm 45 phút × 180.000 VND/giờ | 291.600.000 VND/năm |
| 4 | Giảm dừng thiết bị do trễ bảo trì | Tránh 18 ca dừng/năm × 25.000.000 VND/ca | 450.000.000 VND/năm |
| 5 | Giảm công tổng hợp báo cáo cho Ban điều hành | 5 ngày/tháng × 8 giờ × 300.000 VND/giờ | 144.000.000 VND/năm |
| | **TỔNG LỢI ÍCH/NĂM** | | **1.466.400.000 VND** |

#### Lợi ích định tính
- ✅ Nâng cao trải nghiệm khách hàng → tăng trung thành
- ✅ Ra quyết định nhanh hơn dựa trên dữ liệu
- ✅ Nâng cao hình ảnh thương hiệu (ưu tiên số hóa)
- ✅ Sẵn sàng mở rộng quy mô
- ✅ Tuân thủ quy định

### 3.4. Phân tích ROI

```
                    Năm 0       Năm 1       Năm 2       Năm 3
                    ──────      ──────      ──────      ──────
Đầu tư:           -1.620.000.000   —            —            —
Chi phí vận hành:    —         -255.000.000  -427.000.000  -440.000.000
Lợi ích:             —         +1.173.000.000 +1.466.400.000 +1.612.000.000
                    ──────      ──────      ──────      ──────
Lợi ích ròng:     -1.620.000.000 +918.000.000 +1.039.400.000 +1.172.000.000
Lũy kế:           -1.620.000.000 -702.000.000 +337.400.000 +1.509.400.000
                                             ▲
                                     Điểm hòa vốn
                                     (~22 tháng)

ROI (3 năm) = (Tổng lợi ích - Tổng chi phí) / Tổng chi phí × 100
           = (4.251.400.000 - 2.742.000.000) / 2.742.000.000 × 100
           = 55,0%
```

**Sensitivity analysis**

| Kịch bản | Giả định chính | ROI 3 năm | Quyết định |
|---|---|---:|---|
| Best case | Chuẩn hóa dữ liệu hoàn tất trong 4 tuần, adoption > 90% | 71% | Nên triển khai ngay |
| Base case | Chuẩn hóa dữ liệu trong 8 tuần, adoption 80% | 55% | Tiến hành |
| Worst case | Dữ liệu sạch chậm, adoption 60%, bảo trì bị chậm 1 quý | 28% | Chỉ triển khai nếu có PMO + owner dữ liệu |

---

## 4. Phạm vi dự án

### 4.1. Mục tiêu dự án

| # | Mục tiêu | KPI | Chỉ tiêu | Thời hạn |
|---|----------|-----|----------|----------|
| O1 | Chuẩn hóa danh mục và vòng đời tài sản toàn viện | % tài sản có mã định danh hợp lệ | ≥ 98% | 31/08/2026 |
| O2 | Rút ngắn quy trình kiểm kê tháng | Thời gian hoàn tất kiểm kê | ≤ 1 ngày làm việc | 30/09/2026 |
| O3 | Kiểm soát bảo trì và điều chuyển tài sản có SLA | % yêu cầu được xử lý đúng SLA | ≥ 95% | 31/10/2026 |

**Tiêu chí thành công:**
1. 100% tài sản mới được tạo mã và gắn khoa sở hữu tại thời điểm bàn giao.
2. Dashboard cho Ban điều hành hiển thị được tồn kho, trạng thái, tài sản sắp bảo trì, tài sản thất lạc.
3. Mỗi yêu cầu điều chuyển hoặc bảo trì đều có log người tạo, người duyệt, người nhận, thời gian hoàn tất.

### 4.2. Trong phạm vi

#### Nhóm chức năng 1: Danh mục và Đăng ký tài sản
**Nhu cầu kinh doanh:** Chuẩn hóa nguồn dữ liệu gốc để mọi khoa dùng cùng một mã tài sản và trạng thái.

| Mã BRD | Yêu cầu kinh doanh | Mô tả | Ưu tiên | Business outcome | Ref HĐ |
|--------|---------------------|--------|---------|--------|
| BRD-101 | Tạo hồ sơ tài sản tập trung | Mỗi tài sản có mã, loại, khoa sở hữu, trạng thái, ngày mua, bảo hành | Bắt buộc | Dữ liệu gốc thống nhất | HĐ 2.1 |
| BRD-102 | Gắn mã định danh và barcode | Tài sản phải được gắn mã duy nhất để kiểm kê và tra cứu nhanh | Bắt buộc | Giảm thất lạc | HĐ 2.1 |
| BRD-103 | Phân loại tài sản theo nhóm và mức độ quan trọng | Thiết bị y tế, CNTT, nội thất, vật tư giá trị cao có quy tắc quản lý khác nhau | Nên có | Báo cáo và SLA bảo trì chính xác | HĐ 2.1 |

#### Nhóm chức năng 2: Điều chuyển, bàn giao, và kiểm kê
**Nhu cầu kinh doanh:** Kiểm soát trách nhiệm sở hữu tài sản theo khoa và theo người nhận bàn giao.

| Mã BRD | Yêu cầu kinh doanh | Mô tả | Ưu tiên | Business outcome | Ref HĐ |
|--------|---------------------|--------|---------|--------|
| BRD-201 | Điều chuyển tài sản có phê duyệt | Mỗi lần chuyển khoa phải có người yêu cầu, người duyệt, người nhận và thời gian bàn giao | Bắt buộc | Giảm tranh chấp trách nhiệm | HĐ 2.2 |
| BRD-202 | Kiểm kê theo khoa và đợt | Cho phép tạo đợt kiểm kê, chốt kết quả, và ghi nhận lệch | Bắt buộc | Rút ngắn kiểm kê tháng | HĐ 2.2 |
| BRD-203 | Xử lý lệch kiểm kê | Cho phép ghi nhận mất, hỏng, chờ xác minh, và người chịu trách nhiệm | Nên có | Audit trail rõ | HĐ 2.2 |

#### Nhóm chức năng 3: Bảo trì và Báo cáo điều hành
**Nhu cầu kinh doanh:** Giảm dừng thiết bị và giúp Ban điều hành ra quyết định ngân sách.

| Mã BRD | Yêu cầu kinh doanh | Mô tả | Ưu tiên | Business outcome | Ref HĐ |
|--------|---------------------|--------|---------|------------------|--------|
| BRD-301 | Quản lý lịch bảo trì | Theo dõi kỳ bảo trì định kỳ, trạng thái thực hiện, nhà cung cấp | Bắt buộc | Giảm dừng thiết bị | HĐ 2.3 |
| BRD-302 | Cảnh báo tài sản đến hạn bảo trì/thanh lý | Gửi cảnh báo cho Vật tư và khoa sở hữu trước hạn | Bắt buộc | Chủ động vận hành | HĐ 2.3 |
| BRD-303 | Dashboard điều hành | Tổng hợp tài sản theo khoa, trạng thái, giá trị, bảo trì, thất lạc | Nên có | Quyết định ngân sách nhanh | HĐ 2.3 |

### 4.3. Ngoài phạm vi

| # | Hạng mục | Lý do loại trừ | Xem xét lại khi |
|---|----------|----------------|-----------------|
| 1 | Tích hợp ERP kế toán | Hạn chế phạm vi giai đoạn 1 | Khi hoàn thành chuẩn hóa mã tài sản |
| 2 | Ứng dụng di động offline đầy đủ | Chi phí cao, phụ thuộc hạ tầng mạng nội bộ | Giai đoạn 2 |
| 3 | Tự động nhận dạng tài sản bằng AI/camera | Chưa có nhu cầu rõ và thiếu dữ liệu huấn luyện | Khi đã có kho ảnh tài sản chuẩn |

### 4.4. Giả định

| # | Giả định | Nếu KHÔNG đúng thì... | Người xác nhận |
|---|----------|----------------------|----------------|
| A1 | Mỗi khoa cử 1 đầu mối xác nhận dữ liệu tài sản | Chậm chuẩn hóa dữ liệu, trễ timeline migration | Trưởng khoa |
| A2 | Danh mục tài sản hiện tại có thể làm sạch trong tối đa 8 tuần | Scope migration tăng, cần CR | Phòng Vật tư |
| A3 | Bệnh viện chấp nhận quy trình phê duyệt điều chuyển 2 bước | Không chốt được workflow chính | Ban điều hành |

### 4.5. Ràng buộc

| # | Ràng buộc | Loại | Ảnh hưởng |
|---|-----------|------|-----------|
| C1 | Ngân sách tối đa 1,35 tỷ cho build giai đoạn 1 | Tài chính | Không bao gồm mobile offline và ERP integration |
| C2 | Go-live trước đợt kiểm kê Q4/2026 | Tiến độ | Phải ưu tiên module đăng ký, điều chuyển, kiểm kê trước |
| C3 | Log bàn giao và lịch sử trạng thái phải lưu tối thiểu 5 năm | Audit / Tuân thủ | Ảnh hưởng thiết kế dữ liệu và lưu trữ |
| C4 | Hệ thống phải triển khai trên hạ tầng cloud của NCC, truy cập qua VPN site-to-site | Kỹ thuật | Giới hạn phương án kiến trúc và monitoring |

**Dữ liệu lịch sử và retention**

- Hồ sơ điều chuyển, kiểm kê, và bảo trì phải lưu tối thiểu 5 năm để phục vụ đối soát và kiểm tra nội bộ.
- Khi tài sản chuyển sang trạng thái `Disposed`, hệ thống vẫn phải giữ toàn bộ lịch sử sở hữu, bảo trì, và kiểm kê.
- Dashboard điều hành phải phân biệt dữ liệu hiện tại với dữ liệu lịch sử theo kỳ tháng/quý/năm.

### 4.6. Business Rules & Decision Policies

| Mã BR | Quy tắc nghiệp vụ | Lý do kinh doanh | Ảnh hưởng |
|---|---|---|---|
| BR-001 | Mỗi tài sản chỉ có một mã định danh duy nhất trên toàn viện | Tránh trùng lặp và lệch kiểm kê | Đăng ký, kiểm kê, báo cáo |
| BR-002 | Điều chuyển tài sản giữa hai khoa chỉ hoàn tất khi có xác nhận của cả bên giao và bên nhận | Khóa trách nhiệm sở hữu | Điều chuyển, audit |
| BR-003 | Tài sản đang ở trạng thái `Chờ thanh lý` không được cấp phát lại | Tránh dùng lại tài sản rủi ro | Điều chuyển, kiểm kê |
| BR-004 | Thiết bị y tế mức độ quan trọng cao phải có lịch bảo trì bắt buộc và cảnh báo trước tối thiểu 15 ngày | Giảm dừng thiết bị | Bảo trì |
| BR-005 | Mọi chênh lệch kiểm kê phải được phân loại `Mất / Hỏng / Sai vị trí / Chờ xác minh` trước khi chốt đợt kiểm kê | Chuẩn hóa xử lý lệch | Kiểm kê, dashboard |

### 4.7. Business Rule Architecture

- **Execution order:** Đăng ký tài sản -> bàn giao sở hữu -> sử dụng/vận hành -> điều chuyển -> kiểm kê -> bảo trì/thanh lý.
- **Override matrix:** Quy tắc kiểm kê không được ghi đè quy tắc sở hữu; chỉ Trưởng phòng Vật tư hoặc người được ủy quyền mới được xác nhận chênh lệch cuối cùng.
- **Decision owner:** Phòng Vật tư quyết định chuẩn mã tài sản; Ban điều hành quyết định ngưỡng tài sản cần phê duyệt điều chuyển.

---

## 5. Phân tích stakeholder

### 5.1. Các stakeholder chính

| # | Stakeholder | Vai trò | Kỳ vọng | Mức ảnh hưởng |
|---|--------------|---------|---------|---------------|
| 1 | Giám đốc vận hành | Nhà tài trợ (Sponsor) | ROI, giảm thất thoát, có dashboard | 🔴 Rất cao |
| 2 | Trưởng phòng Vật tư | Product Owner nghiệp vụ | Quy trình kiểm kê và điều chuyển chạy đúng | 🔴 Rất cao |
| 3 | Điều dưỡng trưởng / đại diện khoa | Người dùng chính | Thao tác nhanh, ít bước, rõ trách nhiệm | 🟠 Cao |
| 4 | Trưởng phòng CNTT | Giám sát kỹ thuật | Bảo mật, phân quyền, vận hành ổn định | 🟠 Cao |
| 5 | Kế toán tài sản | Người dùng phụ trợ | Đối chiếu giá trị và hồ sơ thanh lý | 🟡 Trung bình |
| 6 | Kiểm soát nội bộ | Stakeholder audit | Có log, có bằng chứng, truy xuất được | 🟠 Cao |

**Conflict-prone stakeholders**
- Sponsor muốn go-live trước Q4/2026; CNTT muốn thêm thời gian hardening.
- Vật tư muốn 1 bước xác nhận điều chuyển; các khoa muốn tối giản thao tác.
- Kiểm soát nội bộ yêu cầu log đầy đủ; người dùng khoa muốn sửa nhanh hơn.

_(Chi tiết: xem `03-Stakeholder-Map.md` và `../BA-document-rule/core/stakeholder-conflict-resolution.md`)_

---

## 6. Tổng quan quy trình nghiệp vụ

### 6.1. Quy trình hiện tại (As-Is) — Tóm tắt

```
Khoa phát sinh tài sản mới -> gửi email/phiếu cho Phòng Vật tư -> Vật tư cập nhật file Excel tổng -> tài sản được sử dụng tại khoa -> điều chuyển ghi tay/email -> cuối tháng kiểm kê từng khoa -> Vật tư tổng hợp chênh lệch và làm báo cáo Excel
```

**Điểm nghẽn chính:**
1. 🔴 Không có mã duy nhất nên một tài sản có thể xuất hiện dưới nhiều tên khác nhau.
2. 🟠 Điều chuyển và nhận bàn giao không để lại luồng xác nhận chuẩn.
3. 🟡 Báo cáo điều hành phải chờ hợp nhất file từ nhiều khoa.

### 6.2. Quy trình tương lai (To-Be) — Tóm tắt

```
Tạo hồ sơ tài sản trong hệ thống -> gán khoa sở hữu và barcode -> sử dụng/vận hành tại khoa -> điều chuyển qua workflow 2 bước -> theo dõi bảo trì/cảnh báo -> kiểm kê theo đợt -> dashboard điều hành cập nhật theo thời gian gần thực
```

**Cải tiến:**
- ✅ Kiểm kê tháng giảm từ 3 ngày xuống còn 1 ngày.
- ✅ Điều chuyển có log đầy đủ người giao, người nhận, thời gian hoàn tất.
- ✅ Thiết bị đến hạn bảo trì được cảnh báo trước tối thiểu 15 ngày.

_(Chi tiết: xem `04-Process-Flow.md`)_

---

## 7. Yêu cầu phi chức năng (Tóm tắt)

| Danh mục | Yêu cầu | Chỉ tiêu |
|----------|---------|----------|
| **Hiệu năng** | NFR-01, NFR-02 | Tải trang ≤ 3 giây, API p95 ≤ 500ms |
| **Khả dụng** | NFR-04 | Uptime ≥ 99.5% |
| **Bảo mật** | NFR-06, NFR-07, NFR-08 | JWT + RBAC + TLS/AES-256 |
| **Kiểm toán** | NFR-10 | Log CRUD và điều chuyển/bàn giao |
| **Mở rộng** | NFR-05 | Hỗ trợ tăng 10x số tài sản trong 3 năm |
| **Tuân thủ** | NFR-17 | Bảo vệ dữ liệu và audit nội bộ |
| **Khả dụng** | NFR-11, NFR-12 | Responsive + hỗ trợ đa trình duyệt |

_(Chi tiết: xem `05-SRS.md` Mục 3)_

---

## 8. Rủi ro

| # | Rủi ro | Xác suất | Tác động | Biện pháp giảm thiểu | Chịu trách nhiệm |
|---|--------|----------|----------|----------------------|-------------------|
| R1 | Phát sinh yêu cầu ngoài phạm vi (Scope creep) → vượt ngân sách | Cao | Cao | Chốt phạm vi (Baseline) + quy trình Yêu cầu thay đổi (CR) | Cả hai |
| R2 | Người dùng kháng cự thay đổi | Cao | Trung bình | Cho tham gia sớm, đào tạo, quản lý thay đổi | KH |
| R3 | Tích hợp phức tạp hơn dự kiến | Trung bình | Cao | Thử nghiệm sớm, xem xét API tuần 2 | NCC |
| R4 | Stakeholder chính thay đổi giữa chừng | Thấp | Cao | Ghi nhận quyết định, phê duyệt chính thức | KH |
| R5 | Dữ liệu cũ không sạch | Trung bình | Trung bình | Kiểm tra dữ liệu sớm, KH chịu trách nhiệm chất lượng dữ liệu | KH |

---

## 9. Tóm tắt tiến độ & Ngân sách

### 9.1. Tiến độ tổng quan

| Giai đoạn | Thời lượng | Sản phẩm chính | Mốc |
|-----------|-----------|----------------|-----|
| Khám phá & Thiết kế | 2 tuần | Đặc tả yêu cầu (SRS), Giao diện phác thảo | M1: Phê duyệt đặc tả |
| Phát triển Giai đoạn 1 (Bản cơ bản - MVP) | 6 tuần | Phần mềm hoạt động được | M2: Nghiệm thu GĐ1 |
| Phát triển Giai đoạn 2 | 4 tuần | Đầy đủ tính năng | M3: Nghiệm thu GĐ2 |
| Vận hành + Bảo hành | 2 tuần | Hệ thống chính thức | M4: Kết thúc bảo hành |
| **Tổng** | **14 tuần** | | |

### 9.2. Tóm tắt ngân sách

| Hạng mục | Số tiền |
|----------|---------|
| Phát triển phần mềm (NCC) | 420.000.000 VND |
| Hạ tầng/Hosting (Năm 1) | 60.000.000 VND |
| Đào tạo + Quản lý thay đổi | 40.000.000 VND |
| Dự phòng (10-15%) | 60.000.000 VND |
| **TỔNG** | **580.000.000 VND** |

---

## 10. Ma trận truy vết (BRD → SRS → HĐ)

| Scope Item | Yêu cầu BRD | Tham chiếu SRS | Mục HĐ | User Story | Ưu tiên |
|-------------|-------------|----------------|---------|------------|---------|
| SCOPE-01 | BRD-101 | FR-101, FR-102 | HĐ 2.1 | US-001, US-002 | Bắt buộc |
| SCOPE-02 | BRD-102 | FR-103 | HĐ 2.1 | US-003 | Bắt buộc |
| SCOPE-03 | BRD-201 | FR-201 | HĐ 2.2 | US-011 | Nên có |
| SCOPE-04 | BRD-202 | FR-202, FR-203 | HĐ 2.2 | US-012, US-013 | Có thể |

> **Truy vết đảm bảo:** Mọi yêu cầu kinh doanh đều được triển khai và kiểm thử

---

## 11. Phê duyệt BRD

> ⚠️ **Phê duyệt BRD = Phê duyệt đầu tư + Chốt phạm vi (Baseline)**
> Sau thời điểm này, mọi thay đổi phạm vi phải qua quy trình Yêu cầu thay đổi (CR)

| Vai trò | Bên | Họ tên | Chữ ký | Ngày |
|---------|-----|--------|--------|------|
| Nhà tài trợ (Sponsor) | Khách hàng | | | |
| Người đại diện KH (Product Owner) | Khách hàng | | | |
| Tài chính/Mua sắm | Khách hàng | | | |
| Quản lý dự án (PM) | Nhà cung cấp | | | |
| Trưởng nhóm Phân tích (BA Lead) | Nhà cung cấp | | | |

---

## Phụ lục

- **Phụ lục A:** Bảng thuật ngữ
- **Phụ lục B:** Chi tiết Quy trình nghiệp vụ → xem `04-Process-Flow.md`
- **Phụ lục C:** Chi tiết SRS → xem `05-SRS.md`
- **Phụ lục D:** Hợp đồng → xem tài liệu hợp đồng riêng
- **Phụ lục E:** Ghi chú phỏng vấn stakeholder
