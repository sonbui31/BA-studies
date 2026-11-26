# CHANGELOG — BA-Agent Framework

> Tất cả thay đổi đáng chú ý của framework sẽ được ghi nhận tại đây.
> Format: [Semantic Versioning](https://semver.org/) — MAJOR.MINOR.PATCH

---

## [3.11.0] — 2026-11-26

Wireframe và mockup thành ảnh thật trong SRS; rà soát toàn dự án sau 3.10 và sửa các lỗi tìm được (script, rule template còn vẽ quy trình bằng Mermaid, nội dung bộ mẫu lệch nhau).

### Added
- `so_do.md` mục 13 và `core/screen-inventory-guide.md`: wireframe/mockup bằng Figma, StitchMCP hoặc HTML offline; ảnh `wireframes/SCR-xx-<tên>.png` nhúng vào SRS kèm dòng nguồn; mã `SCR-xx` giống nhau ở Screen Inventory, SRS và tên ảnh. Hướng dẫn mô tả công cụ theo năng lực (tên lệnh MCP đổi theo phiên bản) và nói rõ bước cần người làm (export PNG từ Figma, hoặc Figma REST API khi có token).
- `scripts/wireframe_tool.py`: `render` chụp HTML wireframe thành PNG bằng Chrome/Edge headless (không cần Node, không gửi dữ liệu ra ngoài); `check` báo ảnh thiếu file, tên ảnh không theo mã, mã không có trong Screen Inventory, dòng trỏ nhầm ảnh màn hình khác, ảnh thiếu dòng nguồn, ảnh thừa, mã được nhắc mà không có dòng. Chạy trong CI trên hai bộ mẫu.
- Bộ mẫu: Outsource 6 wireframe (SCR-01 đến SCR-07, SCR-06 ghi lý do không cần) thay mã `S-0xx`/`Figma/AP-0xx` không khớp nhau trong SRS, RTM và Story Map; Product 2 wireframe ở `05-SRS-Lite.md` mục 2.7.
- Curated SRS template mục 2.9.3: bảng danh mục ảnh màn hình nối `SCR-xx` với FR.
- `tests/test_wireframes.py` (10 test); `test_bpmn.py` thêm kiểm tra không đường nối nào xuyên qua ô, lệnh sinh lại ảnh không lọt vào bản Word, id XML hợp lệ, spec sai thoát mã 2, đọc file nhiều pool và cổng event-based, trang ngang trong Word; `test_diagrams.py` thêm kiểm tra cổng Process Diagram và Human Sign-off.

### Fixed
- `bpmn_tool.py`: đường nối không còn vẽ xuyên qua ô (chọn tuyến ít va chạm nhất); khe nhãn nhánh tính đúng bề rộng cổng; dòng `"row"` đặt trong spec không bị ô tự xếp đè lên; gọi `layout` nhiều lần cho cùng kết quả; id XML trùng sau chuẩn hóa hoặc bắt đầu bằng chữ số bị chặn; node trỏ tới lane không có báo lỗi thay vì traceback; `check` đọc cổng event-based/complex, transaction, mọi pool của collaboration, sự kiện biên không nằm trong `flowNodeRef`; thư mục không có `.bpmn` hoặc XML hỏng thoát mã 2; vẽ ảnh quá 180 giây báo lỗi thay vì traceback.
- `bpmn_render.mjs`: `--scale` sai, file không đọc được, không mở được trình duyệt đều thoát mã 2 kèm hướng dẫn.
- `md_to_docx.py`: hai ảnh rộng liền nhau không còn trang dọc trắng ở giữa; ảnh rộng cuối tài liệu không tạo trang trắng; ảnh không còn cao quá trang ngang; trang bìa riêng và đánh số lại từ 1 chỉ giữ ở section đầu; `--mmdc` sai đường dẫn báo lỗi thay vì lặng lẽ dùng mmdc khác; ảnh có dòng chú thích ngay dưới (cùng đoạn) vẫn được tách thành hình riêng, ảnh rộng và chú thích nằm chung trang ngang.
- `md_to_docx.py`, `diagram_check.py --render`, `bpmn_tool.py`: không truyền `--browser` thì tự dùng Chrome/Edge đã cài (biến `BA_MERMAID_BROWSER`, `PUPPETEER_EXECUTABLE_PATH`, rồi đường dẫn cài đặt thường gặp). Trước đây cài công cụ Node với `PUPPETEER_SKIP_DOWNLOAD=1` mà quên `--browser` thì sơ đồ Mermaid trong Word giữ dạng mã.
- `diagram_check.py`: hiểu nhãn viết trong mũi tên (`A -- Có --> B`); sơ đồ có front-matter `---` được kiểm tra và `--fix` chèn dòng khai báo sau front-matter; `--fix` không xóa nhãn chỉ gồm emoji và không sửa ví dụ Mermaid nằm trong khối code khác.
- `preflight_check.py` Process Diagram: không còn đạt nhờ ảnh bất kỳ (logo), chữ `.bpmn` trong câu văn hoặc khối code, liên kết tới file không tồn tại; N/A chỉ khi có nhãn `[LỐI AGILE LITE]` ở đầu tài liệu. Human Sign-off: thấy bảng ký dưới mục con, bỏ dòng có ngày giả (`00/00/0000`) hoặc thiếu tên, không đếm `[CẦN XÁC NHẬN]` trong khối code, câu "không còn …" và ví dụ trong backtick.
- Tài liệu mẫu: lệnh sinh lại ảnh BPMN chuyển vào chú thích HTML nên không lọt vào bản Word giao khách.
- Rule và template còn vẽ quy trình bằng Mermaid `subgraph` (`as-is-process.md`, `process-flow.md`, `process-decomposition-guide.md`, `clinical-workflow-map.md`, `aml-kyc-process.md`, `impact-analysis-guide.md`) chuyển sang BPMN 2.0; `templates/brd.md` thêm mục quy trình As-Is/To-Be; giới hạn số bước thống nhất (Mermaid 12 nút, BPMN khoảng 15 hoạt động); định nghĩa cấp L0–L3 do `process-decomposition-guide.md` giữ; `CLAUDE.md` ghi Hard Gate 1–8.
- Bộ Outsource: một bộ số chi phí, lợi ích, ROI thống nhất giữa BRD mục 3 và 9; Vision & Scope và Stakeholder Map điền đủ; mã điểm đau PD-01 đến PD-04 định nghĩa một chỗ; sơ đồ P1, P2, P3 và tổng quan khớp FR/BR (thêm BR-006 duyệt hai cấp theo nguyên giá, FR-TRF-003, US-TRF-003, TC-TRF-004; nhánh từ chối, phản đối, chi phí bảo trì vượt ngưỡng); ngày SRS và CR-001 khớp Change Log.
- Bộ Product: chỉ trạng thái công khai mới gửi thông báo; số lần gửi lại ghi một cách; thêm nhánh `Declined`, lane Customer Success, nhánh không có gợi ý trùng và chặn gộp khác workspace; OKR 60% thống nhất; BRD, User Flow viết lại bằng tiếng Việt.

---

## [3.10.0] — 2026-11-21

Quy trình nghiệp vụ chuyển từ Mermaid BPMN-lite sang BPMN 2.0 thật (định dạng bpmn.io), theo yêu cầu vẽ đúng chuẩn.

### Added
- `scripts/bpmn_tool.py` (Python thuần): `build` sinh BPMN 2.0 XML có bố cục (pool, lane, luồng trái sang phải, nhãn cổng đặt phía không có đường ra, đoạn dọc chạy trong khe giữa các cột) từ bản mô tả JSON; `check` kiểm tra mô hình trên mọi file `.bpmn`, kể cả bản sửa tay; tô màu điểm đau bằng phần mở rộng màu của bpmn.io.
- `scripts/bpmn_render.mjs`: vẽ `.bpmn` thành PNG/SVG bằng bpmn-js; báo lỗi khi bpmn-js đọc file có cảnh báo.
- `scripts/package.json`: cài công cụ Node tùy chọn (bpmn-js, puppeteer-core, mermaid-cli) bằng một lệnh.
- Sơ đồ BPMN 2.0 (`.json`, `.bpmn`, `.png`), 13 sơ đồ: bộ Outsource 7 (tổng quan As-Is/To-Be trong BRD mục 6 với quy trình con thu gọn và cổng bao hàm; P1 Điều chuyển, P2 Kiểm kê, P3 Bảo trì), bộ Product 5 (As-Is/To-Be trong BRD; vòng phản hồi, gộp feedback trùng, cập nhật trạng thái trong User Flow), ví dụ duyệt hoàn tiền trong `diagrams/`. Task vẽ thành task thường, không biểu tượng (bật lại bằng `"task_icons": true`). Nhãn đặt bằng cách thử vị trí ứng viên, tránh ô, đường nối, biên lane và nhãn khác.
- `md_to_docx.py`: ảnh rộng nằm trên trang ngang riêng.
- `tests/test_bpmn.py` (10 test): sinh và đọc lại XML, lỗi và cảnh báo mô hình, sơ đồ mẫu khớp bản mô tả và có ảnh, tài liệu có liên kết `.bpmn` cạnh mỗi ảnh, vẽ thật bằng bpmn-js khi có Node, trang ngang trong Word.

### Changed
- `so_do.md` mục 4: BPMN 2.0 là chuẩn cho quy trình nghiệp vụ (ký hiệu, bản mô tả JSON, quy tắc mô hình, cách sửa không trộn JSON với sửa tay, draw.io); Mermaid BPMN-lite chỉ để phác thảo (mục 4.5).
- `04-Process-Flow.md` và BRD (Outsource), BRD và User Flow mục 1.2, 3.2, 3.3 (Product), curated template BRD mục 1.8, `bpmn-modeling-standard.md`, `SKILL.md` mục 5, agent, workflow: dùng ảnh BPMN kèm liên kết `.bpmn`.

---

## [3.9.0] — 2026-11-21

Đánh giá phần sơ đồ: vẽ thử 57 sơ đồ bằng mermaid-cli. 4 sơ đồ template không vẽ được; template SRS hiện `<<include>>` thành `<>`; ví dụ mẫu có lỗi nghiệp vụ; mọi sơ đồ dùng theme mặc định; bộ tài liệu mẫu không có BPMN dù Hard Gate 1 đòi; xuất Word ra mã thay vì hình.

### Added
- `scripts/diagram_check.py`: kiểm tra sơ đồ theo `so_do.md`, `--fix` cho phần máy móc, `--render` vẽ thử bằng mermaid-cli.
- `md_to_docx.py`: vẽ sơ đồ Mermaid thành ảnh khi có mermaid-cli (`--diagrams`, `--mmdc`, `--browser`), cảnh báo rõ khi sơ đồ phải giữ dạng mã.
- `preflight_check.py`: check `Process Diagram` cho BRD (Hard Gate 1).
- `BA-Documents-Outsource/04-Process-Flow.md`: 3 quy trình As-Is/To-Be bám BRD/SRS (BR-002, BR-003, BR-004, BR-005), bảng khoảng cách, phê duyệt.
- `tests/test_diagrams.py` (10 test), gồm kiểm tra mọi sơ đồ trong tài liệu mẫu, curated template và `so_do.md` đạt chuẩn.

### Changed
- `so_do.md` viết lại thành file chủ duy nhất về sơ đồ: khối khai báo giao diện, bộ lớp màu, mười quy tắc, BPMN-lite, điều kiện bắt buộc BPMN 2.0 thật, ví dụ đã vẽ thử. `BA-document-rule/core/diagram-guide.md` chỉ còn trỏ về đây.
- Curated template: BRD có khung sơ đồ As-Is/To-Be; Use Case của SRS dùng hình viên thuốc, đường nối không mũi tên, `≪include≫`.
- `bpmn-modeling-standard.md`: phân biệt cổng XOR/AND/OR, sự kiện chờ, cách thể hiện trong BPMN-lite.
- BRD và User Flow bộ Product, BRD bộ Outsource: sơ đồ ký tự chuyển sang Mermaid.
- 33 sơ đồ trong core guide và template: thêm khối khai báo chuẩn, bỏ emoji, `\n` thành `<br/>` (chạy `diagram_check.py --fix`).

### Fixed
- 4 template có `{{...}}` ở tên entity, tên trạng thái hoặc ngày (`data-model.md`, `srs.md`, `vision-scope.md`, `procurement-bidding-spec.md`) nên không vẽ được.
- Ví dụ trong `so_do.md`: Sequence trả 400 rồi vẫn chạy tiếp; State từ chối hoàn tiền luôn về PROCESSING, PENDING không có lối hết hạn; Activity dùng "Gọi API" trong sơ đồ nghiệp vụ; nhánh song song không có điểm hợp; mục đánh số nhảy 10 → 12.
- Bộ Outsource ghi BRD là Baseline đã ký khi chưa có sơ đồ quy trình (vi phạm Hard Gate 1); nay quy trình đã vẽ và có phê duyệt riêng.

---

## [3.8.0] — 2026-11-21

Chạy scripts lên ba bộ tài liệu thật (`projects/QLTS`, `projects/vClassio_app`) cho thấy bản 3.7 chỉ đúng trên tài liệu mẫu do chính bộ kit viết: phần lớn cảnh báo trên tài liệu thật là sai, và strict canonical đếm 0 FR, 0 US, 0 TC cho dự án dùng ID riêng. Bản này sửa công cụ cho tài liệu thật và bổ sung phần việc của người.

### Added
- `ba-scheme.json` cho từng bộ tài liệu: định dạng ID riêng theo loại, vai trò file, tác nhân của dự án. `traceability_scan.py --scheme project` (canonical cộng định dạng đã khai báo); `preflight_check.py`, `quality_rubric.py`, `reindex_markdown.py`, `docx_feedback.py` đọc cùng file.
- `scripts/id_migrate.py`: đổi ID riêng sang canonical theo quy tắc, xem trước mặc định, chặn khi hai ID đổi về một hoặc ID mới script không đọc được, bỏ qua tài liệu đã ký, sinh `ID-MIGRATION.md`.
- `scripts/md_to_docx.py`: xuất Word theo mẫu của khách (`--template`: style, header/footer, khổ giấy, numbering), nhúng ảnh PNG/JPEG. `scripts/docx_feedback.py`: gom Track Changes và comment, gắn về ID; `--baseline` so với bản Markdown, bắt cả sửa không bật Track Changes.
- `BA-document-rule/core/human-accountability.md`: phân vai AI và người, H1–H6 (người chịu trách nhiệm, xác nhận bằng văn bản, làm việc với người thật, review độc lập, ký baseline, duyệt CR), trạng thái tài liệu. **Hard Gate 8:** không ghi Baseline khi bảng Phê duyệt chưa có họ tên và ngày.
- `preflight_check.py`: check `Human Sign-off` cho tài liệu tự nhận đã chốt. `persona_review_check.py`: báo cáo Tier 3 phải có người thật review (`Loại rà soát: ... người thật: <tên>`).
- `BA-document-rule/core/pilot-protocol.md` (pilot công cụ P1, pilot quy trình P2) và bản ghi P1 `tests/golden/real_project_tool_run_2026-11-21.md`.
- `ba_bundle_audit.py`: báo lỗi khi một câu luật dài bị chép sang nhiều file luật.
- Fixture `tests/fixtures/real_world_patterns/` và 30 test mới (`test_real_world_patterns.py`, `test_docx_roundtrip.py`).

### Fixed
- Cảnh báo sai trên tài liệu thật (chi tiết 15 mẫu trong bản ghi pilot): ma trận có cột tên hoặc cột BR đứng đầu bị coi là định nghĩa trùng; ID con `FR-TEA-003.1` gộp thành ID cha; danh sách tổng quan cộng heading chi tiết bị báo trùng; bảng nhóm theo cột đầu; bảng thuộc tính `| ID | ... |` không được đọc; liên kết viết ở dòng dưới định nghĩa bị bỏ; ma trận trong file Story không nối BRQ → FR; chuỗi hai tầng BR → SR → FR; BR định nghĩa trong SRS; BRQ chép vào ma trận SRS che lỗi BRQ chưa định nghĩa.
- `quality_rubric.py` chấm dòng tiêu đề thay cho mô tả bên dưới; chấm cả dòng chỉ nhắc tới ID; không nhận tác nhân của ngành.
- `preflight_check.py` đếm ký tự trong inline code là placeholder; check "BRD Completed" chỉ dựa vào tên file.
- Tài liệu mẫu: BRD và SRS Outsource ghi "Đã phê duyệt" trong lịch sử nhưng header ghi Draft và bảng ký để trống; nay là Baseline có chữ ký (dữ liệu minh họa). BRD Product ghi "Approved" khi còn nhận định chờ xác nhận; nay là Trình duyệt 0.2.
- `workflows/ba-workflow.md` bước 6.6 bảo "auto-fix re-index toàn bộ", trái với việc reindex bỏ qua tài liệu đã ký.

### Changed
- `agents/ba-specialist.md` (22 KB → 9 KB) và `workflows/ba-workflow.md` không chép lại luật; trỏ về file chủ trong `SKILL.md`.
- `extract_ids_from_line` trả ID theo thứ tự đọc và bỏ ID nằm lồng trong ID dài hơn.
- Mô phỏng vai trò được gọi đúng tên là tự rà soát; review độc lập theo H4.

---

## [3.7.0] — 2026-11-21

### Added
- **Phân loại yêu cầu đầu vào** (`BA-document-rule/core/intake-triage.md`, `SKILL.md` mục 0): 5 lối L0 hỏi đáp, L1 review một artifact, L2 viết một artifact lẻ, L3 Change Request, L4 dự án mới. Lối L0–L2 xử lý ngay trong lượt đầu, dùng kiểm tra đầu vào thay cho Hard Gate; chỉ L4 chạy đủ 6 bước. Có quy tắc nâng lối khi việc nhỏ chạm tiền, quyền, dữ liệu nhạy cảm.
- **Nguồn yêu cầu và Hard Gate 7** (`BA-document-rule/core/evidence-source-gate.md`): Sổ nguồn, phân biệt nguồn trực tiếp/gián tiếp bên cạnh mức E1–E4, thông tin người chat ghi `SRC-CHAT`, danh sách nhận định trọng yếu, kế hoạch elicitation ở Bước 1. Không ghi "đã chốt" khi nhận định trọng yếu chỉ có nguồn gián tiếp; gate chặn việc chốt, không chặn việc viết nháp.
- **Chốt theo lát cắt** (`BA-document-rule/core/slice-baselining.md`): chốt nền chung của BRD, rồi từng lát cắt dọc qua Gate 1–4 và 7 độc lập; Sổ lát cắt; quy tắc khi thay đổi lan sang lát đã chốt; dự án outsource giá cố định vẫn ký phạm vi trên toàn bộ BRD.
- `preflight_check.py`: check `Evidence Sources` cho BRD theo Tier.
- 3 golden case phán đoán senior: viết AC nhanh không đòi bộ tài liệu, quy tắc chỉ có nguồn gián tiếp, chốt theo lát cắt khi một module còn chờ.
- Tài liệu mẫu: Sổ nguồn và cột "Nguồn · Mức" trong BRD Outsource và Product, mỗi bộ có một nhận định gián tiếp được đánh dấu để minh họa gate.

### Changed
- `SKILL.md`: Bước 5 kiểm tra theo Tier thay vì chạy mọi kiểm tra cho mọi tài liệu; luồng theo lượt tách lối L0–L3 khỏi lối L4; checkpoint liệt kê nhận định trọng yếu còn thiếu nguồn trực tiếp trước khi đề xuất Duyệt.
- `rigor-tiers.md` mục 2: thêm dòng review vai trò, nguồn yêu cầu, cách chốt, kiểm tra sau mỗi tài liệu.
- `workflows/ba-workflow.md`, `agents/ba-specialist.md`: phân loại trước Step 0, Sổ nguồn ở Step 0, chốt theo lát cắt và gate nguồn ở Step 5.

---

## [3.6.0] — 2026-11-21

### Fixed — scripts cho PASS giả hoặc sửa hỏng tài liệu
- `reindex_markdown.py`: không còn đổi số heading kiểu `## 2024 Roadmap` / `### 3 bước` (chỉ số mục `1.`, `1.2` mới là số mục, và chỉ đổi phần cuối nên template `## 1.1`, `## 2.0` giữ nguyên scheme); không đánh lại dãy đang liên tục (trước đây US-010 → US-011 do gom nhóm theo hàng chục); khóa nhóm ID được định nghĩa trong tài liệu đã ký thay vì đổi tham chiếu ở file khác; BRQ con đổi theo BRQ cha; không gộp ID trùng; giữ kiểu xuống dòng; chỉ coi "Baseline" là dấu đã ký khi nằm ở phần đầu tài liệu; mã thoát phản ánh kết quả.
- `traceability_scan.py`: đọc định nghĩa ID ở heading và list; thư mục rỗng hoặc không có định nghĩa → lỗi; `--strict --scheme canonical` báo ID sai scheme (`OFF_SCHEME_ID`) thay vì bỏ qua; kiểm tra từng FR tới US và từng US tới AC/TC ở mọi chế độ; báo Story tham chiếu FR chưa định nghĩa và SRS tham chiếu BRQ chưa định nghĩa (`STALE_REF`); nhận ID 4 chữ số và mã module có chữ số; bảng NFR 4 cột được tính là định nghĩa; bỏ qua khối `~~~`; `TC-NFR-001` không còn sinh ra `NFR-001` giả; BR chưa được enforce báo `ORPHAN_BR`.
- `persona_review_check.py`: không còn crash `UnicodeEncodeError` trên console Windows; căn cứ PASS/ISSUE phải trỏ tới vị trí; phát hiện không có vai trò nào trỏ tới bị báo.
- `preflight_check.py`: câu phủ định ("chưa có glossary") không còn được tính là có; Glossary, As-Is, Traceability phải có heading; MoSCoW đếm giá trị trong bảng; đại từ "ai" không kích hoạt checklist AI; thư mục không có tài liệu nhận diện được → FAIL; đổi tên "Conflict Scan" thành "Compound Requirement Scan" cho đúng việc nó làm.
- `quality_rubric.py`: số phần trăm ("99.9%") được nhận là chỉ số đo; actor và từ mơ hồ khớp nguyên từ ("pm" không còn khớp "development").
- `ba_response_eval.py`: từ viết tắt trùng từ thường (PHI, HIS, CR, KT) chỉ khớp khi viết HOA ("phi chức năng" không còn thỏa check quyền riêng tư).
- `template_schema_check.py`: heading phải đúng cấp; marker NFR phải là ID thật. `media_audit.py`: bỏ qua URL và phần `"title"` của link ảnh. `docx_to_md.py`: không ghi đè file đã có khi thiếu `--force`, giữ thẳng cột với ô gộp, đánh số đúng ảnh dùng lại.
- `ba_bundle_audit.py`: thêm kiểm tra tiêu đề phiên bản cũ, agent trỏ tới skill không tồn tại, đường dẫn gãy trong SKILL.md; không crash encoding.

### Changed
- **Truy vết N:M:** mỗi FR ≥ 1 US, mỗi US ≥ 1 AC/TC. Ràng buộc 1:1 chuyển sang cờ `--one-to-one`. Feature chỉ bắt buộc khi bộ tài liệu có Feature Map (khớp với bộ 4 tài liệu cốt lõi).
- **Review vai trò theo Tier** thay cho 21 vai trò ở mọi tài liệu: Tier 1 = R-BA + vai trò theo loại tài liệu; Tier 2 thêm R-SPONSOR, R-STAFF, R-TIME, R-QA, R-SEC, R-PM; Tier 3 đủ 21; dữ liệu nhạy cảm thêm R-PRIVACY, R-SEC. Báo cáo ghi `Loại tài liệu`, `Tier`, `Dữ liệu nhạy cảm`.
- **SKILL.md gọn lại** (55 KB → 24 KB): ma trận độc giả và quy chuẩn từng loại tài liệu chuyển sang `BA-document-rule/core/document-rulebook.md`; mô tả script chuyển sang `scripts/README.md`; bỏ phần nhắc lại toàn văn Anti-AI. Sửa mâu thuẫn: Stakeholder Map 7 cột (không còn chỗ ghi 6 cột), Data Dictionary 7 cột có đủ cột Độ nhạy cảm, luồng tương tác theo lượt đi đúng thứ tự BRD → SRS → Story → AC.
- `agents/ba-specialist.md`: bỏ phần "điều phối Claude/o4/GPT-5/Gemini" (agent không làm được) và `skills:` trỏ tới skill không tồn tại; thay bằng lượt review độc lập; sửa đường dẫn file Word; sửa chữ bị hỏng trong mục Anti-AI. `workflows/ba-workflow.md`: cùng thay đổi, sửa thứ tự sinh tài liệu.
- **Tài liệu mẫu** `BA-Documents-Outsource/` và `BA-Documents-Product/` chuyển sang scheme canonical (BRQ, FR-MOD, US-MOD, TC-MOD, F01), thêm Tier và nhãn `[TÀI LIỆU MẪU]`, bổ sung bảng BR → FR → TC; cả hai đạt `--scheme canonical --strict`.
- CI chạy thêm template, media, preflight và traceability strict trên fixture và tài liệu mẫu.

### Added
- 33 test mới (tổng 76) cho các lỗi trên, gồm round-trip `reindex --apply`, CLI `persona_review_check` trên console cp1252, và kiểm tra hai bộ tài liệu mẫu đạt canonical strict.
- `BA-document-rule/core/document-rulebook.md`, `scripts/README.md`.

### Removed
- Hai ảnh trùng byte trong `Curated templates/media/` (`BRD_BPMN_XinNghi_ToBe.jpg`, `SRS_Hinh1_UseCase_TongQuan.jpg`); `media/README.md` trỏ sang ảnh đang nhúng.
- Bước CI tìm trong `knowledge-index/chunks.jsonl`: file này không track trong git nên bước đó luôn fail trên CI.

---

## [3.5.5] — 2026-11-21

### Changed
- Bắt buộc kiểm tra đủ 21 vai trò trên **từng tài liệu BA** được tạo hoặc sửa đáng kể; mỗi vai trò có PASS/ISSUE/N/A và căn cứ, vai trò không liên quan phải có lý do N/A.
- Cập nhật protocol, workflow, skill và hướng dẫn để chặn bàn giao khi thiếu độ phủ; vai trò liên quan vẫn được review sâu theo tài liệu và Tier.

### Added
- `scripts/persona_review_check.py` kiểm tra ma trận 21 vai trò, căn cứ, mã phát hiện và liên kết `ISSUE` tới bảng phát hiện.

---

## [3.5.4] — 2026-11-21

### Changed
- `core/persona-simulation.md` — Tổng hợp 21 góc nhìn review tài liệu: 3 góc nhìn mặc định và 18 vai trò mở rộng; chọn theo tài liệu/Tier, ghi phát hiện có bằng chứng và decision owner.
- `core/evaluation-protocol.md`, `SKILL.md`, workflow và hướng dẫn sử dụng — nối review theo vai trò vào trước bước bàn giao. Kết quả mô phỏng không thay người thật sign-off; bỏ logic PASS bằng đa số phiếu.
- Thêm card truy xuất `KB-PERSONA-REVIEW-001` và yêu cầu file giao thức trong bundle audit.

---

## [3.5.3] — 2026-11-21

### Added
- `knowledge-source/ba-update-2026-11-21.md` — Bổ sung hướng dẫn lập BA Work Plan theo task card IIBA, cấu trúc ECBA hiện hành và trạng thái WCAG 3 Working Draft.
- Hai card truy xuất mới cho BA Work Plan và ECBA; mở rộng card accessibility để phân biệt WCAG 2.2 và bản nháp WCAG 3.

### Changed
- Điểm tra cứu chính, source manifest và bundle audit trỏ đến bản cập nhật mới; giữ bản 14/11 làm mốc lịch sử.

---

## [3.5.2] — 2026-11-14

### Added
- `knowledge-source/ba-update-2026-11-14.md` — Đối chiếu nguồn chính thức IIBA, Scrum, Cucumber, ISO, W3C và NIST; hướng dẫn áp dụng cho BA-agent.
- Card tra cứu cho cập nhật chuẩn BA, AC, NFR/accessibility và AI tạo sinh.

### Changed
- Sửa số task BABOK v3 từ 28 thành 30 ở khung kiến thức, knowledge base và card truy xuất.
- Làm rõ số kịch bản AC theo Tier là quy ước nội bộ trong curated template AC, User Story và SKILL; cập nhật template AI để ngưỡng đánh giá và tự động hóa phải dựa trên rủi ro và bằng chứng.

---

## [3.5.1] — 2026-10-26

### Added
- `tests/golden/senior_run_2026-10-26.md` — Ghi nhận lần chạy thử 4 tình huống phán đoán, phương pháp, kết quả và giới hạn.
- `tests/golden/senior_judgement_cases.jsonl` — 4 tình huống mới (13 tất cả), đáp án chấm viết trước khi chạy.

### Changed
- `SKILL.md` — Gate 3 và 4 không chặn phác kịch bản AC dạng `[DỰ THẢO, CHƯA DUYỆT]`; thiếu ngưỡng thì đề xuất giá trị khởi điểm gắn `[Giả định]`.
- `references/elicitation-playbook.md` — Thêm tình huống yêu cầu chất lượng thiếu ngưỡng.

---

## [3.5.0] — 2026-10-26

Nâng chuẩn lên mức Senior BA: thêm phán đoán, độ chặt theo rủi ro, phân tích chiến lược, đo giá trị và kỹ năng làm việc với stakeholder.

### Added
- `core/rigor-tiers.md` — 3 Tier rủi ro (7 câu chấm điểm) quyết định độ sâu tài liệu, số kịch bản AC, review, script; danh sách điều không được nới.
- `core/strategy-analysis-guide.md` — Quy trình 6 bước từ vấn đề đến Go/No-Go, mức bằng chứng E1–E4, ví dụ tính số có điểm hòa vốn và độ nhạy (số giả định).
- `core/solution-evaluation-guide.md` — Benefit Register, leading/lagging/guardrail, kiểm tra nhất quán bộ KPI, lịch review 30/60/90 ngày.
- `core/senior-ba-rubric.md` — 9 chiều × 3 mức, dấu hiệu đỏ, 7 kiểm tra nghĩa giữa FR/US/AC, mẫu prompt LLM-judge.
- `references/elicitation-playbook.md` — Chuẩn bị bằng giả thuyết, bảng tình huống khó, play-back 24 giờ, kịch bản workshop 3 giờ, câu hỏi theo ngành.
- `references/senior-ba-soft-skills.md` — Từ chối yêu cầu, đàm phán lợi ích, báo tin xấu, Decision Memo, giới hạn đạo đức.
- `references/case-study-parent-app.md` — Nhận xét kiểu Senior trên bộ tài liệu Parent App (KPI mâu thuẫn, phương án nhận diện khuôn mặt, phụ thuộc chưa xác nhận).
- `references/vn-regulatory-watchlist.md` — Danh sách chủ đề pháp luật Việt Nam cần hỏi, ghi rõ chưa xác minh.
- `scripts/ai_smell_scan.py` — Quét mẫu "mùi AI" tiếng Việt và tiếng Anh; `Anti_ai_writing_rules.md` Phụ lục A cho tiếng Việt.
- `tests/golden/senior_judgement_cases.jsonl` — 9 tình huống phán đoán; 6 card tri thức mới.

### Changed
- `SKILL.md` — Thêm mục "Chuẩn Senior", Hard Gate 6, bước 0 (Tier) ở Bước 1, Benefit Register ở Bước 6; rút gọn mục sơ đồ và Anti-AI (trỏ về `so_do.md` và `Anti_ai_writing_rules.md`).
- `Curated templates/04-Acceptance-Criteria-Template.md` — Ghi chú số kịch bản AC theo Tier.
- `scripts/ba_bundle_audit.py` — Đưa các file mới vào danh sách bắt buộc.

---

## [3.4.5] — 2026-10-26

### Added
- `knowledge-source/babok-v3-framework.md` — BACCM, 6 Knowledge Area (30 task), phân loại yêu cầu, Underlying Competencies, Perspectives, ánh xạ sang artifact của BA-agent.
- `ba-knowledge-cards.json` — Card `KB-BABOK-001`.
- `core/traceability-validator.md` mục 8 — Bảng ánh xạ scheme ID tự đặt (`BR`/`BRULE`/`SR`/`FR-01.1`) sang canonical và hai phương án xử lý.
- `SKILL.md` — Lối Agile Lite (Mini-Brief thay BRD/SRS) cạnh Hard Gates; nhóm 5 quy tắc Điều 25–27.
- `scripts/ba_response_eval.py` — Scenario `healthcare`, `government`, `startup-mvp`, `inhouse`; 8 golden case mới.
- `projects/vClassio_app/parent_app/MIGRATION-NOTES.md` và `BA-GAP-CHECKLIST.md` mục 7 — Kết quả audit trên dự án thật.

### Changed
- `knowledge-source/50-babok-v3-techniques.md` — Viết lại theo đúng 50 kỹ thuật BABOK v3 (chương 10); kỹ thuật ngoài BABOK (Gap Analysis, Kano, Decision Tree...) chuyển sang mục riêng.
- Số Điều và số bước checklist Anti-AI thống nhất: 27 Điều, checklist 13 bước, trên mọi tài liệu.
- `scripts/ba_response_eval.py` — Token ngắn (`cr`, `kt`, `kyc`, `aml`, `sla`...) khớp theo ranh giới từ, không còn khớp nhầm trong từ dài.
- `templates/brd.md`, `srs.md`, `user-story-map.md` — Thêm ghi chú template bổ trợ; `ba-knowledge-base.md` và `QUICK-START.md` trỏ BRD/SRS/Story/AC về Curated templates.
- `scripts/ba_bundle_audit.py` — `knowledge-index/chunks.jsonl` không còn là file bắt buộc.

### Removed
- `knowledge-index/chunks.jsonl` khỏi git (đưa vào `.gitignore`, vẫn giữ ở máy local). File chứa text trích từ sách và tài liệu bên thứ ba. Các commit cũ vẫn còn file này trong lịch sử.

---

## [3.4.4] — 2026-09-07

### Added
- `scripts/template_schema_check.py` — Runtime schema gate cho 4 curated core templates, kiểm section bắt buộc, marker canonical và legacy marker bị cấm.
- `scripts/media_audit.py` — Audit ảnh trong `Curated templates/media`, kiểm broken image links, undeclared media và stale declarations.
- `tests/fixtures/canonical_full_bundle/` — Fixture canonical đầy đủ BRD/SRS/Feature/Story/Acceptance Criteria dùng `AC-*`.

### Changed
- `scripts/ba_bundle_audit.py` — Đưa `template_schema_check.py` và `media_audit.py` vào danh sách required runtime scripts.
- `tests/test_runtime_scripts.py` — Tăng coverage cho template schema, media inventory và canonical full bundle strict traceability.

### Fixed
- Canonical strict mode giờ nhận `BR-001` business rules như traceable business items, không chỉ nhận `BRQ-*`.

---

## [3.4.3] — 2026-09-07

### Added
- `scripts/traceability_scan.py` — Hỗ trợ `AC-*` như artifact nghiệm thu hợp lệ bên cạnh `TC-*`/`UAT-*`.
- `tests/test_runtime_scripts.py` — Thêm coverage cho `07-Acceptance-Criteria.md`, canonical AC chain, và cardinality mismatch `FR -> nhiều US`.

### Changed
- Chuẩn hóa canonical traceability contract thành `BRQ -> FR/NFR -> Feature -> US -> AC/TC`.
- `scripts/ba_id_utils.py`, `preflight_check.py`, `reindex_markdown.py` — Nhận diện và kiểm tra `AC-*` trong Acceptance Criteria/UAT artifacts.
- Curated templates và tài liệu hướng dẫn — Đồng bộ cách dùng `BRQ-*` cho yêu cầu kinh doanh, `BR-*` cho business rule, và `AC-*` cho Acceptance Criteria.

### Fixed
- File `07-Acceptance-Criteria.md` không còn bị classify nhầm thành `other`.
- Canonical strict mode giờ phát hiện `MISSING_US_FOR_FR`, `MULTIPLE_US_FOR_FR`, `MISSING_AC_FOR_US`, và `MULTIPLE_AC_FOR_US`.

---

## [3.4.2] — 2026-09-03

### Added
- `user-manual-generator/` — Bộ skill tạo tài liệu hướng dẫn sử dụng tiếng Việt (Docusaurus 3.10) cho web app, desktop app, mobile app, hệ thống nội bộ.
  - `SKILL.md` — Rule chính: workflow, evidence rules, structure, quality bar.
  - `references/writing-guide.md` — Quy chuẩn viết tiếng Việt.
  - `references/docusaurus.md` — Hướng dẫn setup/deploy Docusaurus + GitHub Pages.
  - `references/capture-guide.md` — Hướng dẫn chụp screenshot.
  - `references/handoff-template.md` — Template cho thông tin chưa xác minh.
  - `scripts/audit-docs.js` — Script kiểm tra chất lượng tài liệu trước bàn giao.

### Changed
- `SKILL.md` — Thêm routing cho user-manual-generator vào bảng "Read selectively".
- `DOCUMENT-MAP.md` — Thêm section mô tả file và cách dùng user-manual-generator.

---

## [3.4.1] — 2026-05-25

### Added
- `BA-document-rule/references/ba-knowledge-base.md` — Knowledge base BA tự chứa, chắt lọc từ kho học liệu `BA/` để agent dùng được ngay cả khi xoá folder nguồn.
- `BA-document-rule/references/ba-knowledge-cards.json` — Bộ retrieval cards có cấu trúc cho BRD/SRS/UAT/RTM/modeling/data/product/AI/domain.
- `scripts/knowledge_search.py` — Search offline các BA knowledge cards theo query, xuất JSON hoặc Markdown.
- `scripts/build_knowledge_index.py` — Build self-contained `knowledge-index/` từ folder nguồn BA, có chunking và metadata.
- `scripts/knowledge_index_search.py` — BM25 search trên `knowledge-index/chunks.jsonl` mà không đọc lại folder nguồn.
- `scripts/ba_response_eval.py` — Quality gate cho câu trả lời/tài liệu BA theo scenario `outsource`, `product`, và `fintech`.
- `scripts/eval_golden_cases.py` và `tests/golden/ba_response_cases.jsonl` — Golden evaluation suite cho các control coverage quan trọng.
- `scripts/build_semantic_index.py`, `scripts/semantic_index_search.py`, và `requirements-semantic-index.txt` — Optional semantic embedding retrieval bằng SentenceTransformers, hỗ trợ FAISS khi có.
- `knowledge-source/source-manifest.json` và `knowledge-source/download-instructions.md` — Ghi metadata nguồn ngoài git, phục vụ rebuild mà không cần track folder `BA/`.
- `requirements-knowledge-index.txt` — Optional dependencies để rebuild full-text PDF index.

### Changed
- Nối `SKILL.md`, `DOCUMENT-MAP.md`, và `BA-document-rule/README.md` với knowledge base + retrieval cards để agent dùng kiến thức BA đã chắt lọc mà không phụ thuộc runtime vào folder `BA/`.
- Runtime retrieval có 2 tầng: curated cards (`knowledge_search.py`) và source-derived chunks (`knowledge_index_search.py`).
- `knowledge_index_search.py` chuyển sang default hybrid retrieval: BM25-style scoring, query expansion Việt/Anh cho thuật ngữ BA, vector-style cosine scoring, citation fields, và excerpt sạch hơn.
- `build_knowledge_index.py` hỗ trợ page-level citation (`page_start/page_end`) cho PDF được extract bằng `pypdf` trong các lần rebuild tiếp theo.
- Rebuilt `knowledge-index/` with PDF full-text extraction: 35,479 chunks from 992 documents, with 833 PDFs extracted by `pypdf`, 3 by `pdfminer`, and 9 fallback metadata chunks.

---

## [3.4.0] — 2026-05-12

### Added
- `SKILL.md` — Skill entrypoint cho `BA-agent`, định tuyến đọc tài liệu theo nhu cầu và quy tắc execution
- `agents/openai.yaml` — Metadata để bundle này hoạt động như một local skill hoàn chỉnh hơn
- `scripts/ba_bundle_audit.py` — Kiểm tra bundle-level consistency cho version marker, entry files, và legacy ID examples
- `scripts/preflight_check.py` — Script hóa pre-flight cho BRD/SRS/Story/UAT, thay vì chỉ giữ checklist ở markdown
- `scripts/quality_rubric.py` — Script hóa quality rubric và smell detection cho requirement
- `scripts/traceability_scan.py` — Audit traceability thật trên thư mục tài liệu BA, hỗ trợ cả legacy IDs và canonical IDs
- `scripts/reindex_markdown.py` — Re-index heading/ID ở chế độ dry-run mặc định, có thể `--apply` khi đã review
- `tests/test_runtime_scripts.py` — Unit tests tối thiểu cho runtime scripts chính
- `BA-document-rule/core/stakeholder-conflict-resolution.md` — Protocol xử lý requirement conflict + decision ownership + artifact update rules

### Changed
- Đồng bộ bundle chính lên `v3.4.0` thay cho trạng thái nửa `3.3.1`, nửa `3.4`
- Hợp thức hóa `Sequential Index Validation` thành capability chính thức của release `3.4.0`
- Chuẩn hóa ví dụ traceability trong các tài liệu lõi theo dạng `US-ORD-001`, `TC-ORD-001`
- Nối workflow và traceability guide với runtime scripts để agent ưu tiên automation trước khi audit thủ công
- Nối pre-flight và requirement quality vào runtime flow thay vì chỉ mô tả bằng policy
- Nâng `preflight_check.py` từ presence-check sang adequacy-check heuristics cho BRD/SRS/Story/UAT
- Thêm evidence ownership và audit-readiness fields vào các templates regulated-domain

## [3.3.1] — 2026-04-06

### ⭐ Added — Industry Overlays
- **Government Overlay** — Đấu thầu (Luật 22/2023), nghiệm thu nhiều cấp, ATTT (NĐ 85/2016), tích hợp LGSP/NGSP/CSDL QG (`overlays/government/`) [NEW]
- **Healthcare Overlay** — PHI protection (NĐ 13/2023), HL7 FHIR R4, Clinical Workflow Maps, Drug Interaction (DDI), Data Classification Matrix (`overlays/healthcare/`) [NEW]
- **Fintech Overlay** — PCI-DSS v4.0, AML/KYC (Luật 14/2022), Transaction Integrity (ACID + Idempotency), Reconciliation Spec, eKYC Tiering (`overlays/fintech/`) [NEW]

### ⭐ Added — Industry Templates (9 files, `templates/industry/`)
- **regulatory-compliance-matrix.md** — 🏛️🏥💰 Feature → Regulation mapping + Gap Analysis [NEW]
- **procurement-bidding-spec.md** — 🏛️ HSMT + ROM + Đào tạo CBCC [NEW]
- **multi-level-acceptance.md** — 🏛️🏥 Nghiệm thu nhiều cấp + Clinical Validation [NEW]
- **clinical-workflow-map.md** — 🏥 Clinical Pathway + DDI + HL7 FHIR Data Flow [NEW]
- **data-privacy-consent.md** — 🏥💰 Data Classification + Consent Management [NEW]
- **industry-integration-spec.md** — 🏛️🏥💰 LGSP/HL7 FHIR/Open Banking integration [NEW]
- **transaction-recon-spec.md** — 💰 Transaction Lifecycle + Double-entry + Reconciliation [NEW]
- **aml-kyc-process.md** — 💰 eKYC 4-tier + AML Rules + SAR [NEW]
- **security-continuity-plan.md** — 🏛️🏥💰 STRIDE + DR/BCP + ATTT [NEW]

### Changed
- `README.md` — Cập nhật directory tree: overlays 4 → 7
- `DOCUMENT-MAP.md` — Thêm 3 overlays mới vào bảng
- `QUICK-START.md` — Thêm 3 loại dự án mới vào bảng chọn

---

## [3.3] — 2026-04-03

### ⭐ Added — "Viết tốt hơn" (Writing Quality Engine)
- **Requirement Decomposition Patterns** — 4 patterns (CRUD/Lifecycle/Actor/Integration) + Decision Table (`writing-guide.md` §10)
- **AC Pattern Library** — 8 loại scenario: Happy/Negative/Boundary/Permission/State/Concurrency/Integration/Data Volume (`writing-guide.md` §11)
- **Conflict Detection Patterns** — 6 loại mâu thuẫn requirement + Resolution Strategies (`writing-guide.md` §12)
- **Assumption Validation Process** — Lifecycle: Identified→Documented→Validated→Confirmed/Rejected (`writing-guide.md` §13)
- **Requirement Quality Rubric** — 5-point scale + 8 Smell Detector patterns (`core/requirement-quality-rubric.md`) [NEW]
- **Writing Examples Library** — Mẫu viết cho Precondition/Exception/BR/NFR/Integration/TC (`references/writing-examples.md`) [NEW]

### ⭐ Added — "Nghĩ sâu hơn" (Advanced Analysis Engine)
- **Decision Analysis Framework** — 4 tools: Weighted Scoring, Pugh Matrix, CBA/ROI, Decision Tree (`core/decision-analysis-framework.md`) [NEW]
- **NFR Discovery Guide** — 7 câu hỏi + 5 kỹ thuật phát hiện NFR specific (`core/nfr-discovery-guide.md`) [NEW]
- **Process Decomposition Guide** — L0→L1→L2→L3 hierarchy + decomposition rules (`core/process-decomposition-guide.md`) [NEW]
- **Communication Packaging** — 4 package types: Executive Summary/Technical Brief/Test Strategy/Quick Start (`references/communication-packaging.md`) [NEW]

### 🔧 Changed
- **Impact Analysis Guide** — Rewrite toàn bộ (39→180+ dòng): Impact Scoring Matrix + Ripple Effect Tree + Regression Mapping + Decision Flowchart
- **As-Is Process template** — Gap Analysis §5 mở rộng: 5 Gap Types + Prioritization Matrix + Closure Tracking
- **ba-specialist.md** — Skills 12→15; thêm Skill 13 (Decision Analysis), 14 (NFR & Quality), 15 (Packaging & Process)
- **DOCUMENT-MAP.md** — Cập nhật core/ (15→19 files), references/ (5→7 files)
- **Version đồng bộ → v3.3** trên ba-specialist, DOCUMENT-MAP

### 📊 Stats
- Files mới: 6 (`requirement-quality-rubric`, `decision-analysis-framework`, `nfr-discovery-guide`, `process-decomposition-guide`, `writing-examples`, `communication-packaging`)
- Files major update: 3 (`writing-guide`, `impact-analysis-guide`, `as-is-process`)
- Total content added: ~2,500 dòng nội dung mới

---

## [3.2] — 2026-04-03

### ⭐ Added
- **Post-Implementation Review (PIR)** template — Cover BABOK KA#6 (Solution Evaluation)
  - Benefits Realization tracking (OKR Planned vs Actual)
  - Lessons Learned (Keep/Improve/Stop)
  - Technical Debt Assessment
  - User Adoption metrics (DAU, Feature Usage Rate)
- **Anti-Patterns Guide** — 15 sai lầm BA thường gặp + cách tránh (`references/anti-patterns.md`)
- **NFR Traceability** — Mở rộng chain: `NFR-ID → NFR-TC-ID` cho Performance/Security test
- **Bi-Directional Tracing** — Trace ngược TC→US→FR→BRQ, phát hiện Stale References
- **Impact Chain** — Khi BRQ thay đổi → auto-flag tất cả downstream items
- **Risk Response Strategies** — 4 chiến lược Accept/Mitigate/Transfer/Avoid + Decision Flowchart
- **LLM Triage Matrix** — Chọn 1/2/4 LLM theo kích thước dự án (S/M/L)
- **Workflow Rollback Path** — Rõ ràng: step fail → quay lại step nào
- **Effort Estimation per Step** — Bảng S/M/L giờ/ngày per workflow step
- **CHANGELOG.md** — File này, theo dõi thay đổi framework
- **CONTRIBUTING.md** — Quy trình đóng góp + Template PR checklist

### 🔧 Changed
- **Version đồng bộ toàn bộ → v3.2** — README, principles, ba-specialist, workflow, evaluation-protocol, DOCUMENT-MAP
- **USER-GUIDE.md** — "11 Skills" → "12 Skills", thêm Skill 12 (AI/ML Feature Spec)
- **Meeting Minutes template** — Thêm Decision Log + Risk Escalation + Open Items tracking
- **Traceability Validator** — v3.0 → v3.2: thêm ORPHAN_NFR + STALE_REF gap types
- **ba-specialist.md** — v3.1 → v3.2: Updated Primary Objective + Skills Suite header

### 🐛 Fixed
- Version mismatch giữa README.md (v2.6.1) và ba-specialist.md (v3.1) — nay đồng bộ v3.2
- USER-GUIDE thiếu Skill 12 (AI/ML Feature Spec) — đã bổ sung

---

## [3.1] — 2026-03-27

### Added
- **AI/ML Feature Specification** template + Pre-Flight (PFC-AI)
- **Narrative Storytelling** cho Pain Points trong BRD (writing-guide.md Section 9)
- **Business Rule Architecture** với Execution Order + Override Matrix
- **Output Severity Design** cho validation/audit systems
- **System Memory Requirements** cho cross-temporal logic
- **UX Metrics** (Time-to-Decision, Scan-to-Action) trong writing-guide.md
- **Configurable Intelligence** Pattern trong AI Feature Spec
- **Auto-Diagram Engine** — Keyword-to-Diagram routing (10 loại)

---

## [3.0] — 2026-03-20

### Added
- **Elicitation Gate** — MANDATORY Step 0, không bỏ qua
- **Pre-Flight Checklist Engine** — Check trước khi sinh document (PFC-BRD, PFC-SRS, PFC-USM, PFC-UAT)
- **Traceability Validator** — Auto-scan cross-doc gaps
- **As-Is Process** — Bắt buộc trước To-Be
- **Screen Inventory + Wireframe** — Mỗi feature ≥ 1 screen
- **Risk Register** — Thay thế Predictive BA lý thuyết bằng actionable register
- **Multi-LLM → Actionable** — Gắn vai trò cụ thể vào từng bước

### Changed
- Evaluation Protocol → Inline Audit (không chỉ cuối cùng)
- Code Traceability Audit → Actionable output format

---

## [2.6.1] — 2026-03-27

### Added
- Auto-Diagram Engine integration (10 types)
- `so_do.md` — Thư viện Mermaid examples

---

## [2.6] — 2026-03-25

### Added
- Customer Intelligence Guide (elicitation + stakeholder psychology)
- Code-to-Requirement Traceability Audit
- Predictive BA Guide (scope creep forecasting)
- Persona Simulation skill
- Impact Analysis guide

---

## [2.5] — 2026-03-20

### Added
- Multi-LLM Orchestration (Gemini 3, Claude 4.6, GPT-5, o4)
- C-S-K-A Evaluation Matrix
- Overlay system (product/outsource/inhouse/startup)

---

## [2.2] — 2026-03-15

### Added
- Initial BA-document-rule framework
- Core principles (BACCM, BABOK, MoSCoW, INVEST, GWT)
- 12 templates (Vision Scope, BRD, SRS, Story Map, etc.)
- Writing Guide
- Quality Checklist (DoR, DoD)
- Glossary
