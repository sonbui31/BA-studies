# Bản ghi pilot công cụ (P1) trên dự án thật — 21/11/2026

> **Mức:** P1 theo `BA-document-rule/core/pilot-protocol.md`: chạy scripts lên bộ tài liệu thật đã có, phân loại cảnh báo đúng/sai, sửa script. Không sửa tài liệu dự án; chỉ thêm `ba-scheme.json` vào thư mục dự án.
> **Không chứng minh:** quy trình có giúp dự án ít làm lại hơn. Việc đó cần pilot P2 với BA và người duyệt thật, chưa chạy.
> **Bộ tài liệu:** `projects/QLTS` (nội bộ, quản lý tài sản bệnh viện), `projects/vClassio_app/parent_app/parent_app_md`, `projects/vClassio_app/BA-Documents-Web-Feature-Expansion`. Bản ghi chỉ nêu ID và số đếm, không chép nội dung tài liệu.

---

## 1. Trước khi sửa (scripts bản 3.7)

| Bộ tài liệu | Traceability (quét thường) | Strict canonical | Preflight |
|---|---|---|---|
| QLTS | Hàng chục `INDEX_DUPLICATE` (US13, US14, US20, F05...) + 29 `ORPHAN_BRQ` | 29 BRQ; 0 FR, 0 US, 0 TC | 40 PASS / 18 FAIL |
| vClassio parent | 8 `ORPHAN_BR` + `INDEX_DUPLICATE` (BR-001 lặp 8 lần) | 8 BR; 0 FR, 0 US, 0 TC | 31 PASS / 19 FAIL |
| vClassio Expansion | 20 FR "trùng" + 107 `ORPHAN_FR` | 20 FR; 0 BRQ, 0 US, 0 TC | 11 PASS / 5 FAIL |

Mở từng dòng bị báo trùng đã lấy mẫu: **tất cả là cảnh báo sai.**

## 2. Các mẫu viết thật mà scripts đọc sai (đã sửa, có fixture và test)

| # | Mẫu viết trong tài liệu thật | Scripts 3.7 hiểu thành | Sửa ở 3.8 |
|---|---|---|---|
| 1 | Ma trận truy vết có cột tên: `\| US13 \| Công suất thiết bị \| BRQ-07 \| F16 \| TC-10-C \|` | Định nghĩa US13 lần hai | Bảng dưới heading "Truy vết/Ma trận" hoặc header nêu ≥ 3 loại ID là ma trận |
| 2 | Ma trận có cột BR đứng đầu: `\| BR-001, BR-004 \| SR-01 \| ... \|` | BR-001 định nghĩa nhiều lần | Như trên |
| 3 | ID con `FR-TEA-003.1` | `FR-TEA-003` lặp 4 lần | Nhận ID con, nối với ID cha |
| 4 | Danh sách tổng quan `F05. Quản lý tài sản` rồi heading `### F05 — ...` | Trùng | Trùng chỉ tính trong cùng kiểu (hai heading, hai dòng bảng định nghĩa) |
| 5 | Bảng nhóm theo cột đầu `\| F05 \| EX-1A \|`, `\| F05 \| EX-1B \|` | Trùng | Cột đầu không phải cột ID và có ID lặp thì cả bảng là bảng nhóm |
| 6 | Bảng thuộc tính `\| ID \| FR-VOU-004 \|`, `\| Truy vết \| BRQ-VOU-005 \|` | Không thấy định nghĩa, không thấy liên kết | Đọc ô thứ hai; dòng dưới thuộc về ID đó |
| 7 | Liên kết ở dòng dưới định nghĩa: `### US20: ...` rồi `> Related BRQ-ID: BRQ-02.1` | US mồ côi | Khối định nghĩa: heading/list ID sở hữu các dòng bên dưới |
| 8 | Ma trận BRQ → FR nằm trong file Story | Mất liên kết BRQ → FR | Dòng ma trận nối cả chuỗi, ở file nào cũng vậy |
| 9 | Hai tầng nghiệp vụ BR → SR → FR | BR mồ côi | Trong ma trận, thứ tự cột là thứ tự chuỗi |
| 10 | BR viết trong SRS (`BR-SRS-003`) | Tham chiếu tới ID chưa định nghĩa | SRS được định nghĩa BR; số thứ tự chỉ xét ở tài liệu gốc của loại ID |
| 11 | ID riêng: `F14`, `US20`, `Rule-4`, `TC-03-A`, `AC1-A`, `SR-01`, `BRULE-001`, `BRQ-TEA-005`, `FR-QR-PRINT-01` | Không nhận ra, hoặc nhận sai loại | `ba-scheme.json` + `--scheme project` |
| 12 | FR dạng tiêu đề + dòng `Mô tả:` / bảng `\| Mô tả \| ... \|` | Rubric chấm câu tiêu đề, báo Missing Actor | Rubric đọc mô tả và Actor dưới tiêu đề |
| 13 | Tác nhân của ngành (`KTTS`, `Phụ huynh`, `Giáo viên`) | Missing Actor | Khai báo `actors` trong `ba-scheme.json`; trường Actor tường minh luôn được tính |
| 14 | Inline code `` `[ADMIN, KTTS]` ``, regex `` `[0-9a-f]{8}` `` | 50 placeholder còn sót | Bỏ qua inline code |
| 15 | File BACCM đóng vai BRD | "Không có BRD" | Khai báo vai trò file trong `ba-scheme.json` |

Fixture: `tests/fixtures/real_world_patterns/`; test: `tests/test_real_world_patterns.py`.

## 3. Sau khi sửa (scripts 3.8, có `ba-scheme.json`)

| Bộ tài liệu | Định nghĩa đọc được (BRQ/BR · FR · US · TC) | Chuỗi đủ | Lỗi còn lại | Preflight |
|---|---|---|---|---|
| QLTS | 36 · 17 · 33 · 82 | 21 / 36 | 27: 15 `ORPHAN_BRQ`, 4 `ORPHAN_FR`, 5 `MISSING_US_FOR_FR`, 3 `STALE_REF` | 37 PASS / 13 FAIL |
| vClassio parent | 34 · 22 · 19 · 19 | 31 / 34 | 13: 10 `ORPHAN_NFR`, 1 `ORPHAN_BR`, 1 `ORPHAN_BRQ`, 1 `MISSING_TC` | 34 PASS / 16 FAIL |
| vClassio Expansion | 45 · 107 · 0 · 0 | 0 / 45 | 57: 35 `MISSING_STORY`, 10 `ORPHAN_BR`, 10 `ORPHAN_NFR`, 2 `STALE_REF` | 21 PASS / 11 FAIL |

`--scheme project --strict` cho QLTS và vClassio parent ra cùng số lỗi với quét thường (định dạng đã khai báo đủ).

## 4. Lỗi còn lại có thật không

Lấy mẫu theo từng loại lỗi, mở đúng dòng trong tài liệu. Tất cả mẫu đã mở là lỗi thật:

| Bộ tài liệu | Lỗi | Kiểm chứng |
|---|---|---|
| QLTS | `STALE_REF FR-F08-01`, `FR-F15-01`, `FR-F18-01`; `ORPHAN_BRQ BRQ-01` "chỉ nối tới FR-F15-01 chưa định nghĩa" | Ma trận BRD và Story Map dùng mã `FR-Fxx-01`, SRS không định nghĩa mã nào như vậy |
| QLTS | `MISSING_US_FOR_FR FR-IMP-01` | Không có trong Story Map hay UAT Plan |
| vClassio parent | `ORPHAN_BR BR-008` | Có trong bảng mục tiêu BRD, không SR nào nhận |
| vClassio parent | `ORPHAN_NFR NFR-03` | Chỉ xuất hiện trong SRS, không có kịch bản kiểm thử |
| vClassio Expansion | `STALE_REF BRQ-VOU-005`, `BRQ-VOU-006` | SRS trỏ tới, BACCM chỉ có BRQ-VOU-001 đến 004 |
| vClassio Expansion | `ORPHAN_BR BR-RULE-001..010` | Chỉ có trong BACCM, SRS không FR nào thực thi |
| vClassio Expansion | `MISSING_STORY` | Bộ này chưa có tài liệu User Story |

Chưa đọc hết 97 lỗi còn lại; mẫu đã mở không có cảnh báo sai. Preflight còn FAIL ở các mục nội dung (As-Is, biên bản elicitation, kiểu AC, chất lượng câu FR viết không có "phải"); đó là yêu cầu của chính bộ quy tắc, dự án có thể không theo.

## 5. Việc tiếp theo

1. Pilot P2 (`pilot-protocol.md` mục 3) với một epic thật, có người duyệt thật.
2. Báo cho chủ dự án các lỗi thật ở mục 4; quyết định sửa tài liệu hay ghi nhận.
3. Thêm mẫu viết mới vào fixture mỗi khi gặp cảnh báo sai.
