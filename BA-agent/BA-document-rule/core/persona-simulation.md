# REVIEW TÀI LIỆU THEO GÓC NHÌN STAKEHOLDER

> **Mục đích:** Dùng các góc nhìn có nhiệm vụ rõ ràng để tìm chỗ tài liệu chưa đủ cho quyết định, triển khai, sử dụng và vận hành. Đây là **mô phỏng để chuẩn bị review**; kết luận nghiệp vụ, pháp lý, kỹ thuật và sign-off thuộc người có thẩm quyền.
> **Nguồn nền:** [IIBA — nhóm stakeholder trong Core Standard](https://www.iiba.org/globalassets/standards-and-resources/core-standard/iiba-core-standard.pdf), [IIBA — Plan Stakeholder Engagement](https://www.iiba.org/contentassets/68282b0837a84197a67ff3aa7c828488/task-card-plan-stakeholder-engagement.pdf). IIBA không yêu cầu dự án nào cũng có đủ mọi vai trò. Một người có thể đảm nhận nhiều vai trò. Các vai trò như Product Owner, người dùng ít thời gian và người dùng cần hỗ trợ tiếp cận là cách repo chia nhỏ góc nhìn để review, không phải danh mục chuẩn của IIBA.
> **Quan hệ:** Bổ sung cho `evaluation-protocol.md`, `senior-ba-rubric.md` và `references/communication-packaging.md`. Không thay thế kiểm tra ID, đánh giá chất lượng requirement hay UAT với người dùng thật.
> **Đây là tự rà soát.** Cùng một mô hình vừa viết vừa đóng vai người đọc thì không phải review độc lập. Review độc lập (người thật, hoặc phiên AI riêng với Tier 2) theo `human-accountability.md` H4; Tier 3 cần ít nhất một người thật ghi tên vào báo cáo.

---

## 1. Ba góc nhìn về quyết định và sử dụng

| Mã | Vai trò review | Mục tiêu và giới hạn | Câu hỏi kiểm tra | Tài liệu thường đọc |
|---|---|---|---|---|
| `R-SPONSOR` | **Sếp / Sponsor ra quyết định** | Cần hiểu giá trị, chi phí, rủi ro và quyết định đang chờ; không tự đi vào API hay database | Vấn đề có bằng chứng? Có baseline, phương án, chi phí và điều kiện dừng? Tôi phải duyệt điều gì, trước ngày nào? | Vision, Business Case, BRD, Executive Summary |
| `R-STAFF` | **Nhân viên trực tiếp làm việc** | Cần thực hiện quy trình hàng ngày với đúng quyền và trách nhiệm | Tôi bắt đầu từ đâu, nhập gì, bàn giao cho ai? Thiếu dữ liệu, bị từ chối hoặc bị gián đoạn thì làm gì? | As-Is/To-Be, User Story, SRS liên quan, UAT, hướng dẫn sử dụng |
| `R-TIME` | **Người dùng ít thời gian / ít kiên nhẫn** | Muốn hoàn thành tác vụ chính nhanh; phản ánh chi phí thao tác, không gán tính cách tiêu cực cho người dùng | Tôi có hiểu bước tiếp theo trong lần đầu dùng? Bước nào lặp, trường nào không cần, lỗi nào khiến tôi bỏ cuộc? Có cách tiếp tục khi dừng giữa chừng? | User Flow, prototype, User Story, AC, Quick Start |

`R-SPONSOR` là người giữ góc nhìn quyết định; nếu quyết định về ngân sách hoặc phạm vi thuộc người khác thì ghi đúng **decision owner** trong dự án. `R-STAFF` có thể là nhân viên nội bộ, đại lý hoặc người vận hành nghiệp vụ. `R-TIME` là **bối cảnh sử dụng**, có thể trùng với `R-STAFF` hoặc khách hàng; nó không tự đại diện cho toàn bộ người dùng.

## 2. Các góc nhìn chuyên môn và kiểm soát

Đây là 18 góc nhìn còn lại trong danh mục 21 vai trò. Số vai trò bắt buộc cho từng tài liệu phụ thuộc Tier (mục 3). Không dựng phản đối chỉ để đủ số vai.

| Mã | Vai trò | Khi cần review sâu | Câu hỏi chính |
|---|---|---|---|
| `R-CFO` | Tài chính / CFO | Có ngân sách, ROI, tiết kiệm hoặc chi phí vận hành | Chi phí vòng đời và giả định tài chính có nguồn? Nếu lợi ích không đạt thì quyết định ra sao? |
| `R-MANAGER` | Trưởng bộ phận / chủ quy trình | Đổi phân công, kiểm soát, SLA nội bộ | Ai chịu trách nhiệm từng bước? Quy trình mới tạo thêm việc hay điểm nghẽn nào? |
| `R-PO` | Product Owner / chủ sản phẩm | Có backlog, MVP, ưu tiên hoặc thử nghiệm | Story nào tạo giá trị trước? Có thể hoãn gì mà vẫn đạt mục tiêu? |
| `R-CUSTOMER` | Khách hàng / người mua dịch vụ | Bán hàng, hợp đồng, cam kết dịch vụ | Phạm vi và kết quả cam kết có rõ? Cách khiếu nại, hủy hoặc đổi yêu cầu có rõ? |
| `R-SME` | Chuyên gia nghiệp vụ | Quy tắc ngành, ngoại lệ, thuật ngữ đặc thù | Rule có đúng thực tế? Có trường hợp hiếm nào làm sai kết luận? |
| `R-PM` | Quản lý dự án / delivery | Có mốc phụ thuộc, nguồn lực hoặc bàn giao nhiều bên | Ai cung cấp đầu vào và khi nào? Quyết định trễ ảnh hưởng mốc nào? |
| `R-TECH` | Kiến trúc sư / Dev Lead | SRS, API, dữ liệu, tích hợp, NFR | Có đủ điều kiện, trạng thái, lỗi và ngưỡng để thiết kế, ước lượng và xây dựng? |
| `R-QA` | QA / người kiểm thử | FR, AC, UAT, nghiệm thu | Kết quả đạt/trượt có quan sát được? Có dữ liệu test, boundary, quyền và ngoại lệ liên quan? |
| `R-PARTNER` | Nhà cung cấp / đối tác tích hợp | API, dữ liệu hoặc SLA qua ranh giới tổ chức | Ai sở hữu hợp đồng, phiên bản, timeout, lỗi, đối soát và trách nhiệm khi sự cố? |
| `R-OPS` | Vận hành hệ thống | Go-live, monitoring, cutover, sự cố | Cần theo dõi gì, khôi phục ra sao, ai trực và khi nào rollback? |
| `R-SUPPORT` | Hỗ trợ khách hàng / helpdesk | Người dùng cần hỗ trợ hoặc có nhiều lỗi thao tác | Khi nhận ticket, tôi biết trạng thái, nguyên nhân có thể và tuyến chuyển tiếp không? |
| `R-TRAINER` | Đào tạo / quản lý thay đổi | Quy trình mới ảnh hưởng nhiều nhân viên | Ai cần học gì, khi nào; làm sao biết họ thực hiện được sau đào tạo? |
| `R-DATA` | Chủ dữ liệu / người làm báo cáo | Báo cáo, KPI, migration, dữ liệu nhạy cảm | Định nghĩa chỉ số, nguồn chuẩn, chất lượng, quyền truy cập và thời hạn lưu có rõ? |
| `R-SEC` | Bảo mật | Xác thực, phân quyền, tích hợp, dữ liệu nhạy cảm | Tài sản cần bảo vệ, quyền tối thiểu, abuse case, log và phản ứng sự cố đã được nêu? |
| `R-PRIVACY` | Pháp chế / quyền riêng tư / compliance nội bộ | Dữ liệu cá nhân, nghĩa vụ hợp đồng hoặc pháp lý | Căn cứ nào cần kiểm chứng? Ai xác nhận, dữ liệu dùng cho mục đích nào và lưu bao lâu? |
| `R-REGULATOR` | Cơ quan quản lý / bên kiểm toán bên ngoài | Dự án có yêu cầu kiểm toán hoặc nghĩa vụ báo cáo được xác nhận | Chứng cứ, quyền phê duyệt và lịch sử thay đổi có truy được? Điều khoản áp dụng do ai xác nhận? |
| `R-ACCESS` | Người dùng cần hỗ trợ tiếp cận | Sản phẩm dùng qua web/app, đặc biệt tác vụ thiết yếu | Có làm được bằng bàn phím và công nghệ hỗ trợ? Thông tin lỗi, tiêu điểm, thời hạn thao tác có cản trở không? |
| `R-BA` | BA reviewer độc lập | Trước sign-off hoặc khi các vai trò đưa nhận xét mâu thuẫn | Phát hiện nào có bằng chứng? FR/US/AC/KPI có cùng nghĩa? Ai có quyền chốt xung đột? |

Các vai trò `R-PRIVACY` và `R-REGULATOR` đặt **câu hỏi cần xác minh**; mô phỏng không được khẳng định dự án tuân thủ luật. `R-ACCESS` nêu rủi ro trong tài liệu; mức đáp ứng accessibility phải được kiểm tra trên sản phẩm bởi người/công cụ phù hợp.

## 3. Quy tắc bắt buộc cho từng tài liệu

1. Với **mỗi tài liệu BA được tạo hoặc sửa đáng kể**, ghi tên/đường dẫn, phiên bản, loại tài liệu, Tier, có dữ liệu nhạy cảm hay không và người thật có quyền duyệt. Một bộ nhiều tài liệu cần **một bảng đánh giá riêng cho từng tài liệu**.
2. **Số vai trò bắt buộc theo Tier** (Tier lấy từ `rigor-tiers.md`, ghi ở đầu tài liệu):

   | Tier | Vai trò bắt buộc trong ma trận |
   |---|---|
   | Tier 1 | `R-BA` + nhóm vai trò đọc sâu theo loại tài liệu (bảng dưới) |
   | Tier 2 | Tier 1 + `R-SPONSOR`, `R-STAFF`, `R-TIME`, `R-QA`, `R-SEC`, `R-PM` |
   | Tier 3 | Đủ 21 vai trò ở mục 1–2 |
   | Mọi Tier, khi có dữ liệu cá nhân nhạy cảm | Thêm `R-PRIVACY`, `R-SEC` |

   Mỗi vai trò bắt buộc có đúng một dòng với kết quả `PASS`, `ISSUE` hoặc `N/A`. Căn cứ của `PASS`/`ISSUE` phải trỏ tới vị trí (mục, bảng, dòng hoặc ID). `N/A` chỉ dùng sau khi đã xét phạm vi và nêu lý do cụ thể, không dùng vì thiếu thời gian. Có thể thêm vai trò không bắt buộc khi thấy liên quan; vai trò được thêm cũng phải đủ căn cứ. Báo cáo không ghi Tier được kiểm như Tier 3.
3. Với vai trò có liên quan, đọc sâu phần phù hợp, đặt nhiệm vụ thực tế, đối chiếu ID/đoạn và ghi phát hiện có bằng chứng. `ISSUE` phải trỏ tới ID phát hiện ở bảng bên dưới, và mỗi phát hiện phải được ít nhất một vai trò trỏ tới.
4. Sau khi sửa, kiểm tra lại vai trò bị ảnh hưởng; cập nhật ma trận cho **phiên bản tài liệu cuối**. Thiếu vai trò bắt buộc, `PENDING`, căn cứ trống hoặc `ISSUE` không có phát hiện tương ứng thì chưa được báo hoàn tất. `BLOCK` và `ASK` chưa được giải quyết phải được nêu rõ khi bàn giao, không được biến thành `PASS`.

| Loại tài liệu (ghi ở dòng `Loại tài liệu:`) | Vai trò đọc sâu, bắt buộc từ Tier 1 |
|---|---|
| Vision, Business Case, BRD | `R-CFO`, `R-PO`, `R-MANAGER`, `R-CUSTOMER` |
| BPMN, quy trình, SOP | `R-MANAGER`, `R-SME`, `R-TRAINER` |
| SRS, API, Data Model | `R-TECH`, `R-DATA`, `R-SEC`, `R-PARTNER` |
| User Story, AC, UAT | `R-PO`, `R-QA`, `R-SME`, `R-ACCESS` |
| Go-live, handover, manual | `R-OPS`, `R-SUPPORT`, `R-TRAINER`, `R-ACCESS` |
| Dữ liệu cá nhân, tài chính, sức khỏe, trẻ em (`Dữ liệu nhạy cảm: Có`) | `R-PRIVACY`, `R-SEC`; thêm `R-REGULATOR` khi có nghĩa vụ được xác nhận |

Một vai trò có thể có hai cách dùng: **người thật tham gia review** hoặc **AI mô phỏng trước buổi review**. Ghi rõ cách dùng trong báo cáo. AI mô phỏng không tạo ra ý kiến thật của nhân viên, khách hàng hoặc cơ quan quản lý. Ma trận đủ vai trò bắt buộc chứng minh **độ phủ đánh giá**, không chứng minh mọi stakeholder đã đồng ý.

## 4. Giao thức đánh giá 4 bước

### Bước 1 — Chuẩn bị

- Đọc tài liệu mục tiêu và các tài liệu liên kết cần thiết; ghi phiên bản, phạm vi, Tier.
- Xác định vai trò bắt buộc theo Tier và loại tài liệu (mục 3); viết một nhiệm vụ cụ thể cho vai trò cần review sâu. Ví dụ `R-STAFF`: "xử lý một đơn bị từ chối sau khi đã nhập xong"; `R-TIME`: "hoàn thành tác vụ chính lần đầu mà không đọc manual".
- Không tự tạo dữ liệu sản phẩm, lời nói stakeholder, chi phí, luật áp dụng hoặc hành vi giao diện chưa có bằng chứng.

### Bước 2 — Đọc và đặt câu hỏi

Với từng vai trò, hỏi: **Tôi cần quyết định/làm gì? Tài liệu đã cho đủ thông tin chưa? Nếu làm sai sẽ ảnh hưởng gì?** Mỗi phát hiện trỏ tới heading, ID, dòng hoặc đoạn cụ thể. Phân loại `FACT` (mâu thuẫn/thiếu rõ trong tài liệu), `INFERENCE` (rủi ro suy ra), `OPEN QUESTION` (cần người thật xác nhận). Không có bằng chứng thì đưa vào Open Questions, không ghi thành lỗi chắc chắn.

### Bước 3 — Phản hồi và sửa

- Gộp phát hiện trùng nhau, nhưng giữ tên các vai trò bị ảnh hưởng.
- BA kiểm tra lại tài liệu nguồn; sửa lỗi mô tả có căn cứ. Quy tắc nghiệp vụ, mức chấp nhận rủi ro, luật hoặc phạm vi chưa rõ thì chuyển **decision owner** xác nhận trước khi chốt.
- Nếu hai vai trò mâu thuẫn, dùng `stakeholder-conflict-resolution.md`; không lấy đa số phiếu để ghi đè một rủi ro nghiêm trọng.
- Tổng hợp thành một bản tài liệu phù hợp với **mục đích và người đọc chính**: quyết định nào cần thấy trước, nhân viên cần làm được việc gì, người dùng ít thời gian cần giảm bước nào, nhóm triển khai cần mức chi tiết nào. Ghi rõ lựa chọn, đánh đổi, tác động và người có quyền quyết; sửa bản tài liệu rồi review lại các vai trò bị ảnh hưởng.

### Bước 4 — Báo cáo và kiểm tra độ phủ

| Mức | Ý nghĩa | Xử lý |
|---|---|---|
| `BLOCK` | Mâu thuẫn hoặc thiếu thông tin khiến quyết định/triển khai không an toàn, không kiểm thử được, hoặc có rủi ro pháp lý/bảo mật cần xác nhận | Chuyển người có quyền quyết; chưa ghi tài liệu là đã duyệt |
| `FIX` | Có lỗi rõ trong tài liệu nhưng có thể sửa bằng thông tin đã xác nhận | Sửa đúng mục và review lại phần bị ảnh hưởng |
| `ASK` | Có câu hỏi hợp lý nhưng chưa đủ bằng chứng kết luận | Ghi Open Question, owner, hạn trả lời |
| `NOTE` | Cải tiến cách trình bày hoặc trải nghiệm, không chặn quyết định hiện tại | Đưa vào backlog hoặc hướng dẫn viết |

**Trạng thái của lượt mô phỏng:** `Không phát hiện vấn đề`, `Cần sửa`, hoặc `Chờ quyết định`. Đây là trạng thái review của BA-agent, **không phải phê duyệt hay sign-off của stakeholder**. Không chấm điểm tổng hoặc bỏ phiếu đa số để xóa một mục `BLOCK`.

Chạy `python BA-agent/scripts/persona_review_check.py <bao-cao-review.md>` cho **từng báo cáo của từng tài liệu**. Lệnh đọc `Tier`, `Loại tài liệu` và `Dữ liệu nhạy cảm` ở đầu báo cáo, rồi trả mã lỗi khi thiếu vai trò bắt buộc, lặp, sai kết quả, căn cứ không trỏ tới vị trí, N/A chung chung, `ISSUE` không có ID phát hiện hoặc phát hiện không vai trò nào trỏ tới. Gate này chỉ kiểm tra hình thức và độ phủ; BA vẫn phải đọc chất lượng căn cứ và xử lý rủi ro.

## 5. Mẫu báo cáo ngắn

```markdown
# Review tài liệu theo vai trò: [Tên tài liệu, phiên bản]
Tài liệu: [đường dẫn file và phiên bản] | Loại tài liệu: [BRD / SRS / User Story / ...] | Tier: [1/2/3] | Dữ liệu nhạy cảm: [Có/Không] | Người duyệt thật: [Vai trò/tên]
Loại rà soát: [Tự rà soát (AI) / Review độc lập (phiên AI riêng) / Review độc lập (người thật: tên, vai trò)]; ghi rõ cho từng vai trò nếu khác nhau
Trạng thái: [Không phát hiện vấn đề / Cần sửa / Chờ quyết định]

## Độ phủ vai trò

> Ví dụ dưới đây là Tier 3 (đủ 21 dòng). Tier 1/2 chỉ cần các vai trò bắt buộc ở mục 3.

| Mã vai trò | Kết quả | Căn cứ / lý do | ID phát hiện |
|---|---|---|---|
| R-SPONSOR | PASS | [Mục/ID tài liệu và lý do đủ cho quyết định] | — |
| R-STAFF | ISSUE | [Vị trí tài liệu và tác động] | RV-01 |
| R-TIME | PASS | [Tác vụ chính, vị trí kiểm tra] | — |
| R-CFO | N/A | [Lý do tài liệu không chứa quyết định tài chính] | — |
| R-MANAGER | PENDING | [Điền sau khi đánh giá] | — |
| R-PO | PENDING | [Điền sau khi đánh giá] | — |
| R-CUSTOMER | PENDING | [Điền sau khi đánh giá] | — |
| R-SME | PENDING | [Điền sau khi đánh giá] | — |
| R-PM | PENDING | [Điền sau khi đánh giá] | — |
| R-TECH | PENDING | [Điền sau khi đánh giá] | — |
| R-QA | PENDING | [Điền sau khi đánh giá] | — |
| R-PARTNER | PENDING | [Điền sau khi đánh giá] | — |
| R-OPS | PENDING | [Điền sau khi đánh giá] | — |
| R-SUPPORT | PENDING | [Điền sau khi đánh giá] | — |
| R-TRAINER | PENDING | [Điền sau khi đánh giá] | — |
| R-DATA | PENDING | [Điền sau khi đánh giá] | — |
| R-SEC | PENDING | [Điền sau khi đánh giá] | — |
| R-PRIVACY | PENDING | [Điền sau khi đánh giá] | — |
| R-REGULATOR | PENDING | [Điền sau khi đánh giá] | — |
| R-ACCESS | PENDING | [Điền sau khi đánh giá] | — |
| R-BA | PENDING | [Điền sau khi đánh giá] | — |

## Phát hiện

| ID | Vai trò | Mức | Loại bằng chứng | Vị trí/ID tài liệu | Phát hiện và tác động | Đề xuất | Owner/hạn |
|---|---|---|---|---|---|---|---|
| RV-01 | R-STAFF, R-TIME | ASK | OPEN QUESTION | US-ORD-01, AC-ORD-01 | Chưa thấy cách tiếp tục sau khi mạng mất lúc xác nhận | Hỏi PO và nhân viên quy trình; bổ sung AC nếu cần | PO / [ngày] |

Quyết định cần người thật xác nhận: [Danh sách hoặc "Không có"]
Phần đã sửa và cần review lại: [Danh sách hoặc "Không có"]
Lựa chọn tối ưu cho người đọc chính và đánh đổi: [Nêu thay đổi, lợi ích, chi phí/rủi ro và decision owner]
Giới hạn mô phỏng: [Thiếu prototype, chưa phỏng vấn người dùng, ...]
```

Ví dụ `RV-01` chỉ minh họa cấu trúc báo cáo; không phải kết luận về một dự án trong repo.

## 6. Lệnh sử dụng

```text
@ba-specialist review BRD này theo vai trò bắt buộc của Tier 2; xuất ma trận PASS/ISSUE/N/A có căn cứ và xử lý phát hiện.
@ba-specialist review SRS thanh toán (Tier 3, dữ liệu nhạy cảm) qua đủ 21 vai trò; đọc sâu R-TECH, R-QA, R-SEC và R-OPS.
@ba-specialist kiểm tra độ phủ vai trò cho từng tài liệu UAT; không bàn giao nếu còn thiếu vai trò bắt buộc hoặc PENDING.
```

Khi không có tài liệu dự án thật, có thể dùng tình huống giả lập để luyện phản biện nhưng phải gắn nhãn `[VÍ DỤ GIẢ ĐỊNH]` cho mọi dữ liệu và kết luận.
