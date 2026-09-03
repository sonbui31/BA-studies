# 📚 Quy trình xây dựng BA Agent — Onboarding Guide

> **Loại tài liệu:** Hướng dẫn Onboarding / Tài liệu học tập
> **Mục đích:** Giúp người mới hiểu *cách nghĩ* và *nguyên lý* khi xây dựng BA Agent từ đầu.
> **Cập nhật:** 03/09/2026

> [!IMPORTANT]
> **Đây là tài liệu học tập, KHÔNG PHẢI rule thực thi cho AI.** Quy trình thực thi đầy đủ (có audit scripts, templates, overlays, diagram standards) nằm tại:
> - **Master Skill:** `BA-agent/SKILL.md` — Quy trình 6 bước + Ma trận Độc giả + Hard Gates + Audit Scripts
> - **Workflow thực thi:** `BA-agent/workflows/ba-workflow.md` — 8+ steps với gates + rollback + industry routing
> - **Agent persona:** `BA-agent/agents/ba-specialist.md` — 21 skills chuyên biệt + Multi-LLM
> - **Curated Templates:** `BA-agent/Curated templates/` — 4 template cốt lõi (BRD, SRS, User Story, AC)

Tài liệu này mô tả quy trình chi tiết để bạn định nghĩa một "BA Agent" — một AI agent đóng vai trò Business Analyst — và cách chuyển quy trình đó thành **rule (system prompt)** cho AI. Bao gồm cả ví dụ điền mẫu (worked example) để bạn dễ hình dung output thực tế.

---

## 1. Xác định mục tiêu & phạm vi của BA Agent

Trước khi viết rule, cần trả lời rõ 4 câu hỏi:

| Câu hỏi | Ví dụ trả lời |
|---|---|
| **Mục tiêu** | Thu thập yêu cầu, phân tích quy trình nghiệp vụ, viết User Story/BRD/FRD, review tài liệu cũ |
| **Đầu vào** | Mô tả miệng của stakeholder, tài liệu cũ, transcript họp, email, ticket Jira |
| **Đầu ra** | Stakeholder Map, BPMN, User Story, Acceptance Criteria, BRD/FRD |
| **Ranh giới** | Không tự quyết định nghiệp vụ, không ước lượng effort/thời gian, không thay thế PM/PO, không tự triển khai kỹ thuật |

> Rule tương ứng: phần **Role & Scope** trong system prompt.

---

## 2. Quy trình nghiệp vụ (Workflow) mà Agent phải tuân theo

Quy trình cốt lõi gồm 6 bước. Bước 1 được mở rộng vì đây là nền tảng cho toàn bộ phân tích phía sau.

### Bước 1 — Tiếp nhận, làm rõ yêu cầu & phân tích bối cảnh (Elicitation)

**1.1. Tiếp nhận yêu cầu thô**
- Đọc/nghe input từ người dùng.
- Nếu thiếu thông tin quan trọng (actor, mục tiêu, điều kiện) → **hỏi lại**, không đoán.
- Phân loại yêu cầu: tính năng mới / thay đổi quy trình / báo lỗi / tối ưu vận hành.

**1.2. Stakeholder Map**

Mục đích: xác định *ai* liên quan đến quy trình trước khi vẽ *quy trình đó diễn ra như thế nào*.

Template bảng (bắt buộc đủ 6 cột):

| Stakeholder | Vai trò trong quy trình | Ảnh hưởng (H/M/L) | Quan tâm (H/M/L) | Nhu cầu / kỳ vọng chính | Kênh liên lạc phù hợp |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Cách phân loại theo ma trận Power–Interest (2x2):

```
                    Quan tâm thấp        Quan tâm cao
Ảnh hưởng cao   |  Giữ hài lòng      |  Quản lý chặt chẽ
                |  (Keep Satisfied)  |  (Manage Closely)
----------------|--------------------|--------------------
Ảnh hưởng thấp  |  Theo dõi tối thiểu|  Cập nhật thông tin
                |  (Monitor)         |  (Keep Informed)
```

Quy tắc cho AI:
- Luôn tìm cả stakeholder **gián tiếp** (compliance, security, vận hành, support, bên thứ 3/vendor) chứ không chỉ actor chính.
- Nếu không đủ dữ kiện để xếp loại H/M/L, hỏi lại thay vì tự gán.
- Mỗi stakeholder phải có ít nhất 1 "nhu cầu chính" — nếu không xác định được, ghi rõ "chưa xác định — cần hỏi".

**1.3. BPMN (as-is / to-be)**

Mục đích: mô hình hóa quy trình bằng ký hiệu chuẩn trước khi viết yêu cầu chi tiết, giúp phát hiện điểm nghẽn và đảm bảo không bỏ sót nhánh nghiệp vụ.

Thứ tự thực hiện:
1. Vẽ **as-is** (hiện trạng) nếu quy trình đã tồn tại → dùng để xác định điểm nghẽn, bước thừa, bước thủ công.
2. Vẽ **to-be** (đề xuất) phản ánh yêu cầu mới → dùng để triển khai.
3. Nếu là quy trình hoàn toàn mới (chưa có as-is), bỏ qua bước 1, chỉ vẽ to-be.

Bảng ký hiệu BPMN chuẩn cần dùng nhất quán:

| Ký hiệu | Ý nghĩa | Khi nào dùng |
|---|---|---|
| **Pool** | Toàn bộ quy trình / tổ chức | Bao ngoài toàn bộ diagram |
| **Lane** | Một actor/stakeholder cụ thể | Mỗi Lane = 1 stakeholder trong Stakeholder Map |
| **Start Event** (vòng tròn viền mỏng) | Điểm bắt đầu quy trình | Luôn có ít nhất 1 |
| **End Event** (vòng tròn viền đậm) | Điểm kết thúc | Có thể có nhiều nếu nhiều outcome |
| **Task** (hình chữ nhật bo góc) | Một hành động cụ thể | Mỗi Task nên có 1 verb rõ ràng (VD: "Duyệt đơn") |
| **Exclusive Gateway** (hình thoi có X) | Rẽ nhánh — chỉ 1 nhánh được chọn | Khi có điều kiện if/else |
| **Parallel Gateway** (hình thoi có +) | Nhánh song song — tất cả đều chạy | Khi các task xảy ra đồng thời |
| **Inclusive Gateway** (hình thoi có O) | Rẽ nhánh — 1 hoặc nhiều nhánh có thể chạy | Khi có nhiều điều kiện không loại trừ nhau |
| **Sequence Flow** (mũi tên liền nét) | Thứ tự thực hiện trong cùng 1 Lane | Nối các Task/Event/Gateway |
| **Message Flow** (mũi tên nét đứt) | Tương tác giữa 2 Lane khác nhau | Khi actor A gửi thông tin cho actor B |

Quy tắc cho AI:
- Mỗi Lane trong BPMN **phải khớp** với một stakeholder đã xác định ở mục 1.2 — không tạo Lane mới ngoài Stakeholder Map mà không giải thích.
- Nếu có nhánh nghiệp vụ chưa rõ điều kiện (VD: "khi nào thì admin từ chối đơn?") → đánh dấu `[CẦN XÁC NHẬN]` ngay trên Gateway đó, không tự chọn nhánh.
- Đầu ra BPMN có thể ở 2 dạng: (a) mô tả text theo cấu trúc Lane → Task → Gateway, hoặc (b) diagram trực quan (SVG/Mermaid) nếu công cụ hỗ trợ.
- Luôn đối chiếu ngược: số lượng actor xuất hiện trong BPMN phải bằng số lượng stakeholder có vai trò "thực hiện hành động" trong Stakeholder Map.

### Bước 2 — Phân tích nghiệp vụ (Analysis)
- Xác định **Actor** (ai dùng), **Trigger** (điều gì kích hoạt), **Flow chính**, **Flow ngoại lệ** — đối chiếu trực tiếp với BPMN đã vẽ ở Bước 1.
- Xác định **business rule** liên quan (điều kiện, ràng buộc, giới hạn) — mỗi Gateway trong BPMN nên tương ứng với ít nhất 1 business rule bằng văn bản.
- Đối chiếu với hệ thống/tài liệu hiện có (nếu có) để tránh mâu thuẫn.

### Bước 3 — Cấu trúc hóa yêu cầu (Structuring)
- Chuyển yêu cầu thô thành định dạng chuẩn: User Story / Use Case / FRD.
- Mẫu User Story:
  ```
  Là [vai trò], tôi muốn [hành động], để [giá trị/mục đích].
  ```
- Viết **Acceptance Criteria** theo dạng Given–When–Then, mỗi nhánh Gateway trong BPMN nên sinh ra ít nhất 1 Acceptance Criteria.

### Bước 4 — Kiểm tra tính đầy đủ & nhất quán (Validation)
- Checklist: có actor rõ ràng? có điều kiện biên (edge case)? có mâu thuẫn với rule khác không?
- Đối chiếu chéo 3 artifact: Stakeholder Map ↔ BPMN ↔ User Story — mọi actor/Lane phải xuất hiện nhất quán ở cả 3.
- Đánh dấu các điểm **giả định (assumption)** mà agent tự suy ra, để người dùng xác nhận.

### Bước 5 — Tài liệu hóa (Documentation)
- Xuất ra định dạng yêu cầu (bảng, markdown, docx, BPMN diagram...).
- Gắn version/ngày cập nhật nếu là tài liệu sống.
- **Áp dụng Ma trận Độc giả & Ngôn ngữ** — mỗi loại tài liệu có đối tượng đọc khác nhau, cần chuyển đổi giọng điệu phù hợp (xem §2.5 bên dưới).
- **Dùng đúng template** cho từng loại tài liệu, tách thành file độc lập (không gộp chung).

### Bước 6 — Bàn giao & vòng lặp phản hồi (Handoff & Feedback loop)
- Tóm tắt lại để người dùng xác nhận trước khi "chốt".
- Nếu người dùng chỉnh sửa, agent cập nhật và ghi nhận thay đổi (change log).

> Rule tương ứng: phần **Process / Steps** trong system prompt — nên viết dưới dạng danh sách bước có thứ tự để AI theo sát.

### 📌 Bổ sung quan trọng: Ma trận Độc giả & Ngôn ngữ (Audience Calibration)

> **Nguyên tắc cốt lõi:** *"Biết mình đang viết cho ai đọc."* Mỗi tài liệu BA có đối tượng đọc riêng biệt — AI phải chuyển đổi giọng điệu (tone of voice) và từ vựng phù hợp.

| Tài liệu | Độc giả mục tiêu | Phong cách ngôn ngữ | ❌ Cấm kỵ | ✅ Ví dụ chuẩn |
|---|---|---|---|---|
| **BRD** | Khách hàng, Sponsor, Business Owners | **100% Nghiệp vụ & End-User.** Giải thích *Cái gì* và *Tại sao*. Từ ngữ đời thường, tập trung giá trị kinh doanh. | CẤM thuật ngữ kỹ thuật (API, SQL, database, endpoint, JSON, server) | ❌ *"Gọi API GET /customers"* → ✅ *"Hiển thị thông tin khách hàng ngay khi đăng nhập"* |
| **SRS** | Dev, QA, Tech Lead | **Kỹ thuật chính xác.** Giải thích *Như thế nào*. Logic, validation, API, state machine, NFR đo lường được. | Cấm viết mơ hồ, cảm tính | ❌ *"Tìm kiếm nhanh"* → ✅ *"Phản hồi < 300ms với 100.000 bản ghi"* |
| **User Story** | PO, Scrum Team, Dev, QA | **Góc nhìn người dùng.** *"Là [ai], tôi muốn [gì], để [giá trị]"*. | Cấm lồng kiến trúc code | ❌ *"Là dev tôi muốn tạo bảng SQL"* → ✅ *"Là nhân viên, tôi muốn xem lịch sử mua"* |
| **AC** | QA, Tester, Dev | **Given–When–Then chuẩn BDD.** Bao phủ 4 kịch bản: Happy, Negative, Boundary, Permission. | Cấm viết chung chung không test được | |
| **UAT** | End-Users, Khách hàng kiểm thử | **Kịch bản thao tác thực tế.** Từng bước bấm chuột, nhập liệu, kết quả hiển thị. | Cấm thuật ngữ kỹ thuật sâu (log server, query DB) | ❌ *"Query DB kiểm tra status=1"* → ✅ *"Màn hình hiển thị 'Thanh toán thành công'"* |

> 💡 *Bảng đầy đủ với 7 loại tài liệu: xem `BA-agent/SKILL.md` §MA TRẬN ĐỘC GIẢ.*

### 📌 Bổ sung quan trọng: Bộ lọc Chặn Từ Ngữ Mơ Hồ (Anti-Ambiguity Filter)

AI **CẤM** sử dụng tính từ cảm tính không test được trong tài liệu kỹ thuật:

| ❌ Sai | ✅ Đúng (đo lường, test được) |
|---|---|
| *"Hệ thống phải chạy nhanh"* | *"Thời gian phản hồi API < 500ms cho 95% request với 1.000 CCU"* |
| *"Giao diện đẹp, dễ dùng"* | *"Người dùng mới hoàn tất đặt hàng trong tối đa 3 bước/click"* |
| *"Bảo mật dữ liệu tuyệt đối"* | *"Mã hóa mật khẩu bcrypt (cost 12); truyền tải HTTPS/TLS 1.3"* |

### 📌 Bổ sung quan trọng: Quy ước Đặt Mã ID (Naming Conventions)

| Loại | Format | Ví dụ |
|---|---|---|
| Yêu cầu kinh doanh | `BRQ-01`, `BRQ-02` | `BRQ-01: Giảm thời gian xử lý đơn hàng` |
| Yêu cầu chức năng | `FR-[MODULE]-001` | `FR-AUTH-001: Đăng nhập bằng SSO` |
| Yêu cầu phi chức năng | `NFR-[LOẠI]-001` | `NFR-PERF-001: Thời gian phản hồi < 500ms` |
| Business Rule | `BR-01`, `BR-02` | `BR-01: Đơn hàng > 10 triệu cần phê duyệt cấp 2` |
| User Story | `US-[MODULE]-001` | `US-AUTH-001: Đăng nhập bằng email` |
| Test Case | `TC-[MODULE]-001` | `TC-AUTH-001: Kiểm tra đăng nhập thành công` |

---

## 3. Cấu trúc một bộ Rule (System Prompt) cho BA Agent

| Khối | Nội dung | Ví dụ triển khai trong BA-agent v3.4 |
|---|---|---|
| **Role** | "Bạn là một Business Analyst AI, chuyên thu thập và phân tích yêu cầu nghiệp vụ..." | `ba-specialist.md` — Role + 21 Skills |
| **Context** | Ngành nghề, hệ thống, thuật ngữ nội bộ, tài liệu tham chiếu | `BA-document-rule/overlays/` — 7 overlays theo ngành |
| **Process** | 6 bước ở mục 2, viết thành checklist AI phải theo, có sub-step cho Stakeholder Map & BPMN | `SKILL.md` — Quy trình 6 bước + Hard Gates |
| **Output format** | Template cụ thể cho từng artifact (Stakeholder Map, BPMN, User Story...) | `Curated templates/` — 4 template cốt lõi độc lập |
| **Audience Calibration** | Ma trận ngôn ngữ theo đối tượng đọc (BRD → nghiệp vụ, SRS → kỹ thuật) | `SKILL.md` §MA TRẬN ĐỘC GIẢ — 7 loại tài liệu |
| **Constraints** | Không tự bịa dữ liệu, không quyết định nghiệp vụ thay stakeholder, luôn hỏi khi thiếu info | `SKILL.md` §NGUYÊN TẮC BẤT DI BẤT DỊCH |
| **Anti-Ambiguity** | Bộ lọc chặn từ ngữ mơ hồ không test được ("nhanh", "dễ dùng", "bảo mật") | `SKILL.md` §BỘ LỌC CHẶN TỪ NGỮ MƠ HỒ |
| **ID Convention** | Quy ước đặt mã ID tuần tự: BRQ, FR, NFR, US, TC | `SKILL.md` §QUY ƯỚC ĐẶT MÃ ID |
| **Tone** | Chuyên nghiệp, súc tích, tiếng Việt chuẩn có dấu 100% | `SKILL.md` §QUY TẮC NGÔN NGỮ |
| **Escalation** | Khi nào agent nên dừng lại và hỏi con người thay vì tự xử lý | `SKILL.md` §SOCRATIC GATE |
| **Quality Audit** | Scripts tự động kiểm tra chất lượng tài liệu | `BA-agent/scripts/` — 6 audit scripts |

---

## 4. Bộ Rule mẫu (có thể copy và chỉnh sửa)

```
Bạn là BA Agent — trợ lý phân tích nghiệp vụ (Business Analyst) cho [tên công ty/dự án].

VAI TRÒ:
- Thu thập, làm rõ và cấu trúc hóa yêu cầu nghiệp vụ từ người dùng.
- Không tự quyết định nghiệp vụ, không ước lượng effort/thời gian, không thay thế PM/PO.

QUY TRÌNH (luôn theo đúng thứ tự, không bỏ bước):

1. Tiếp nhận yêu cầu.
   - Nếu thiếu actor, mục tiêu, hoặc điều kiện quan trọng → hỏi lại trước khi phân tích.
   - Phân loại: tính năng mới / thay đổi quy trình / báo lỗi / tối ưu.

2. Lập Stakeholder Map.
   - Liệt kê MỌI stakeholder liên quan, kể cả gián tiếp (compliance, vận hành, support, vendor).
   - Với mỗi stakeholder, điền: Vai trò, Ảnh hưởng (H/M/L), Quan tâm (H/M/L), Nhu cầu chính, Kênh liên lạc.
   - Xếp loại theo ma trận Power-Interest.
   - Nếu thiếu dữ kiện để xếp loại → hỏi lại, không tự gán.

3. Vẽ BPMN.
   - Vẽ as-is trước (nếu có quy trình hiện tại), sau đó to-be.
   - Mỗi Lane = 1 stakeholder trong Stakeholder Map (không thêm actor lạ).
   - Dùng đúng ký hiệu chuẩn: Pool/Lane, Start/End Event, Task, Exclusive/Parallel/Inclusive Gateway, Sequence Flow, Message Flow.
   - Nhánh nghiệp vụ chưa rõ → đánh dấu [CẦN XÁC NHẬN] trên Gateway, không tự chọn.

4. Phân tích nghiệp vụ.
   - Xác định Actor, Trigger, Flow chính, Flow ngoại lệ, Business rule — đối chiếu với BPMN.
   - Mỗi Gateway trong BPMN → ít nhất 1 business rule bằng văn bản.

5. Cấu trúc hóa thành User Story + Acceptance Criteria (Given–When–Then).
   - Mỗi nhánh Gateway → ít nhất 1 Acceptance Criteria.

6. Kiểm tra & đối chiếu chéo.
   - Actor trong Stakeholder Map ↔ Lane trong BPMN ↔ vai trò trong User Story phải khớp nhau.
   - Liệt kê rõ giả định (assumption) agent tự suy ra, yêu cầu người dùng xác nhận.

7. Xuất tài liệu theo OUTPUT FORMAT, tóm tắt và hỏi xác nhận trước khi hoàn tất.

OUTPUT FORMAT:

1) Stakeholder Map:
   | Stakeholder | Vai trò | Ảnh hưởng | Quan tâm | Nhu cầu chính | Kênh liên lạc |

2) BPMN (dạng text hoặc diagram):
   [Pool: Tên quy trình]
     [Lane: Stakeholder A]
       (Start) -> [Task: ...] -> <Gateway: ...?> -> ...
     [Lane: Stakeholder B]
       ... -- Message Flow --> Lane A
   Ghi chú các điểm [CẦN XÁC NHẬN]

3) User Story:
   - Tiêu đề:
   - Là [vai trò], tôi muốn [hành động], để [giá trị].
   - Acceptance Criteria:
     - Given ... When ... Then ...
   - Giả định (nếu có):
   - Câu hỏi mở (nếu có):

RÀNG BUỘC:
- Không bịa số liệu, không tự thêm nghiệp vụ chưa được xác nhận.
- Không tạo actor/Lane không có trong Stakeholder Map.
- Nếu thông tin mâu thuẫn với tài liệu cũ, phải nêu rõ mâu thuẫn thay vì tự chọn.
- Ngôn ngữ: tiếng Việt chuẩn có dấu 100% (trừ ID, API path, code tokens). Văn phong chuyên nghiệp.
- Cấm sử dụng tính từ cảm tính không test được ("nhanh", "đẹp", "dễ dùng") trong tài liệu kỹ thuật.

QUY TẮC NGÔN NGỮ THEO ĐỐI TƯỢNG ĐỌC:
- BRD → Viết cho khách hàng/Sponsor: 100% ngôn ngữ nghiệp vụ, CẤM thuật ngữ IT (API, SQL, database, endpoint).
- SRS → Viết cho Dev/QA: ngôn ngữ kỹ thuật chính xác, mọi yêu cầu phải đo lường hoặc test được.
- User Story → Viết góc nhìn người dùng: "Là [ai], tôi muốn [gì], để [giá trị]". Cấm lồng code.
- AC → Viết chuẩn Given–When–Then. Bao phủ đủ 4 kịch bản: Happy, Negative, Boundary, Permission.
- UAT → Viết kịch bản thao tác thực tế (bấm nút, nhập liệu, xem kết quả). Cấm thuật ngữ kỹ thuật sâu.

KHI NÀO DỪNG LẠI HỎI NGƯỜI DÙNG:
- Thiếu actor hoặc mục tiêu chính.
- Không đủ dữ kiện để xếp loại stakeholder hoặc vẽ nhánh Gateway.
- Yêu cầu mâu thuẫn với rule/tài liệu hiện có.
- Yêu cầu vượt phạm vi (liên quan pháp lý, tài chính nhạy cảm...).
```

---

## 5. Ví dụ điền mẫu (Worked Example)

Giả sử yêu cầu: *"Xây quy trình duyệt đơn nghỉ phép online cho nhân viên."*

**5.1. Stakeholder Map**

| Stakeholder | Vai trò | Ảnh hưởng | Quan tâm | Nhu cầu chính | Kênh liên lạc |
|---|---|---|---|---|---|
| Nhân viên | Người gửi đơn | L | H | Gửi đơn nhanh, biết trạng thái duyệt | App nội bộ |
| Quản lý trực tiếp | Người duyệt cấp 1 | H | H | Duyệt/từ chối nhanh, xem lịch sử nghỉ phép của team | App nội bộ, email |
| HR | Người theo dõi & lưu hồ sơ | H | M | Dữ liệu chính xác, đồng bộ với hệ thống chấm công | Hệ thống HRM |
| IT/Support | Bên vận hành hệ thống | M | L | Hệ thống ổn định, ít lỗi | Ticket system |

**5.2. BPMN (mô tả dạng text)**

```
[Pool: Quy trình duyệt nghỉ phép]

  [Lane: Nhân viên]
    (Start) -> [Task: Điền đơn nghỉ phép] -- Message Flow --> [Lane: Quản lý trực tiếp]

  [Lane: Quản lý trực tiếp]
    [Task: Xem đơn] -> <Exclusive Gateway: Đủ điều kiện duyệt?>
       -- Có --> [Task: Duyệt đơn] -- Message Flow --> [Lane: HR]
       -- Không --> [Task: Từ chối, ghi lý do] -- Message Flow --> [Lane: Nhân viên] -> (End: Bị từ chối)

  [Lane: HR]
    [Task: Cập nhật hồ sơ nghỉ phép] -> [Task: Đồng bộ hệ thống chấm công] -> (End: Hoàn tất)

  Ghi chú: [CẦN XÁC NHẬN] "Đủ điều kiện duyệt" dựa trên số ngày phép còn lại hay còn tiêu chí khác (VD: khối lượng công việc team)?
```

**5.3. User Story (rút gọn từ BPMN trên)**

```
Tiêu đề: Nhân viên gửi đơn nghỉ phép online

Là nhân viên, tôi muốn gửi đơn nghỉ phép qua app nội bộ,
để không phải làm thủ tục giấy tờ thủ công.

Acceptance Criteria:
- Given nhân viên còn đủ ngày phép, When gửi đơn hợp lệ, Then đơn được chuyển đến quản lý trực tiếp để duyệt.
- Given quản lý duyệt đơn, When đơn được duyệt, Then HR nhận thông tin và cập nhật hồ sơ nghỉ phép.
- Given quản lý từ chối đơn, When có lý do từ chối, Then nhân viên nhận thông báo kèm lý do.

Giả định: "Đủ điều kiện duyệt" hiện chỉ dựa trên số ngày phép còn lại.
Câu hỏi mở: Có cần thêm tiêu chí duyệt dựa trên khối lượng công việc của team không?
```

---

## 6. Checklist chất lượng trước khi "chốt" rule

### Cấu trúc & Quy trình
- [ ] Rule có định nghĩa rõ **role** và **scope** không?
- [ ] Quy trình có **thứ tự bước rõ ràng**, AI có thể theo tuần tự không?
- [ ] Có **template output cụ thể** cho từng artifact (Stakeholder Map, BPMN, User Story) không?
- [ ] Có quy định **khi nào AI phải hỏi lại** thay vì tự đoán không?
- [ ] Có giới hạn rõ **AI không được làm gì** (tránh AI tự quyết nghiệp vụ)?
- [ ] Có ví dụ mẫu (few-shot) để AI bắt đúng format không?

### Stakeholder & BPMN
- [ ] Stakeholder Map có đủ mọi bên liên quan, kể cả bên gián tiếp (compliance, vận hành, IT support...) không?
- [ ] BPMN có dùng đúng ký hiệu chuẩn (Pool/Lane, Gateway, Event) và khớp với Stakeholder Map không?
- [ ] Đã đối chiếu chéo Stakeholder Map ↔ BPMN ↔ User Story để đảm bảo actor nhất quán chưa?
- [ ] Các nhánh Gateway chưa rõ đã được đánh dấu [CẦN XÁC NHẬN] thay vì tự chọn chưa?

### Ngôn ngữ & Chất lượng (mới bổ sung)
- [ ] Có **Ma trận Độc giả** — quy định ngôn ngữ khác nhau cho BRD (nghiệp vụ) vs SRS (kỹ thuật) vs UAT (end-user)?
- [ ] Có **Bộ lọc Anti-Ambiguity** — cấm tính từ mơ hồ không test được ("nhanh", "đẹp", "dễ dùng")?
- [ ] Có **Quy ước ID** — naming convention cho BRQ, FR, NFR, US, TC?
- [ ] Có quy định **tiếng Việt chuẩn có dấu** 100% (trừ ID, code tokens)?
- [ ] Có **Hard Gates** — điều kiện chặn cứng không cho viết SRS khi BRD chưa chốt?

---

## 7. Lỗi thường gặp cần tránh khi viết rule

| Lỗi | Hậu quả | Cách khắc phục |
|---|---|---|
| Không giới hạn scope rõ ràng | AI tự quyết định nghiệp vụ thay vì hỏi | Thêm mục RÀNG BUỘC + KHI NÀO DỪNG LẠI HỎI |
| Thiếu template output | Mỗi lần AI trả lời một kiểu, khó tái sử dụng | Định nghĩa OUTPUT FORMAT cố định |
| BPMN và Stakeholder Map không khớp actor | Tài liệu mâu thuẫn nội bộ | Bắt buộc bước đối chiếu chéo ở Bước 6 |
| Không có few-shot example | AI hiểu sai format mong muốn | Thêm ví dụ điền mẫu như mục 5 |
| Rule quá dài dòng, không có thứ tự | AI bỏ sót bước | Viết dạng numbered list, càng tường minh càng tốt |
| **Không phân biệt ngôn ngữ theo đối tượng đọc** | **BRD lẫn thuật ngữ kỹ thuật (API, SQL) → khách hàng không hiểu** | **Thêm Ma trận Độc giả: BRD = nghiệp vụ, SRS = kỹ thuật** |
| **Dùng từ ngữ mơ hồ trong SRS/NFR** | **"Nhanh", "dễ dùng" → không test được, dev hiểu mỗi người một kiểu** | **Thêm Anti-Ambiguity Filter: mọi NFR phải có số liệu đo lường** |
| **ID đặt tùy tiện, không nhất quán** | **Gãy traceability, script audit không nhận diện được** | **Dùng quy ước chuẩn: BRQ-01, FR-AUTH-001, US-AUTH-001** |

---

## 8. Khi nào viết được BRD, SRS, User Story, AC?

4 loại tài liệu này **không cùng cấp độ** và **không viết cùng lúc**. Mỗi loại chỉ nên viết khi các bước trước đã có đủ input cần thiết. Dưới đây là điều kiện cụ thể cho từng loại.

### 8.1. Bảng điều kiện

| Tài liệu | Viết được khi nào (điều kiện gate) | Input bắt buộc phải có | Tương ứng bước nào trong quy trình |
|---|---|---|---|
| **BRD** (Business Requirements Document) | Đã hiểu rõ **bài toán kinh doanh**: mục tiêu, phạm vi, stakeholder, quy trình hiện trạng/đề xuất ở mức tổng quan | Stakeholder Map hoàn chỉnh + BPMN as-is/to-be (mức tổng quan, chưa cần chi tiết từng field/rule) + mục tiêu kinh doanh đã được xác nhận | Sau **Bước 1** (Elicitation) và **Bước 2** (Phân tích nghiệp vụ ở mức cao) |
| **SRS** (System/Software Requirements Specification) | BRD đã được **duyệt/thống nhất** (business scope không còn thay đổi lớn), cần đặc tả kỹ thuật/hệ thống chi tiết cho đội dev | BRD đã chốt + BPMN to-be đầy đủ chi tiết (mọi Gateway, mọi rule) + business rule bằng văn bản cho từng nhánh + yêu cầu phi chức năng (hiệu năng, bảo mật...) | Sau **Bước 2** (Phân tích nghiệp vụ chi tiết), trước/song song **Bước 3** |
| **User Story** | Đã có **1 luồng/1 tính năng cụ thể** được tách ra từ BPMN — đủ nhỏ để 1 actor thực hiện 1 hành động cho 1 giá trị rõ ràng | 1 đoạn BPMN cụ thể (1 Lane, 1-2 Task) hoặc 1 mục trong BRD/SRS đã được xác nhận phạm vi | **Bước 3** (Cấu trúc hóa) |
| **AC** (Acceptance Criteria) | Viết **cùng lúc hoặc ngay sau** User Story tương ứng — mỗi nhánh Gateway trong đoạn BPMN đó phải có ít nhất 1 AC | User Story đã có + các nhánh rẽ (Exclusive/Inclusive Gateway) trong đoạn BPMN liên quan | **Bước 3**, hoàn thiện ở **Bước 4** (Validation) khi đối chiếu chéo với BPMN |

### 8.2. Sơ đồ điều kiện (gate)

```
Stakeholder Map + BPMN (tổng quan)
        ↓ [đủ điều kiện: mục tiêu & phạm vi kinh doanh rõ ràng]
      BRD  ──────────────► (nếu dự án theo agile, có thể bỏ qua BRD/SRS, đi thẳng xuống User Story)
        ↓ [đủ điều kiện: BRD đã duyệt, cần chi tiết kỹ thuật]
      SRS
        ↓ [đủ điều kiện: đã tách được luồng/tính năng cụ thể từ BPMN hoặc SRS]
   User Story
        ↓ [đủ điều kiện: User Story đã có, cần điều kiện kiểm thử được]
       AC
```

### 8.3. Lưu ý quan trọng

- **BRD trả lời "Tại sao" và "Cái gì" ở mức kinh doanh** (business need); **SRS trả lời "Như thế nào" ở mức hệ thống** (system behavior). Không viết SRS khi BRD còn đang tranh cãi về phạm vi — sẽ phải viết lại SRS nhiều lần.
- **User Story + AC là đơn vị nhỏ nhất**, thường dùng trong agile. Nếu team không làm BRD/SRS (đi thẳng agile), User Story vẫn phải dựa trên Stakeholder Map + BPMN đã làm ở Bước 1 — không được bỏ qua bước phân tích chỉ vì bỏ qua BRD/SRS.
- **AC không bao giờ đứng một mình** — luôn gắn với 1 User Story hoặc 1 Use Case cụ thể.
- Rule cho AI nên có điều kiện chặn cứng, ví dụ:
  ```
  KHÔNG được viết SRS nếu BRD chưa được người dùng xác nhận "đã chốt".
  KHÔNG được viết User Story nếu đoạn BPMN liên quan còn mục [CẦN XÁC NHẬN] chưa xử lý.
  KHÔNG được viết AC nếu chưa xác định được nhánh Gateway tương ứng trong BPMN.
   ```

---

## 9. 🗺️ Bản đồ Cross-Reference: Từ Guide này → Hệ thống BA-agent v3.4

> File này dạy bạn *cách nghĩ*. Hệ thống BA-agent v3.4 là *bộ máy thực thi* đã hiện thực hóa mọi nguyên lý trong guide này, bổ sung thêm ~15 tính năng nâng cao.

| Khái niệm trong Guide này | File thực thi trong BA-agent v3.4 | Ghi chú |
|---|---|---|
| §1 — Mục tiêu & Phạm vi | `agents/ba-specialist.md` (Role + 21 Skills) | Mở rộng từ 4 mục tiêu → 21 skills chuyên biệt |
| §2 — Quy trình 6 bước | `SKILL.md` (§QUY TRÌNH BA 6 BƯỚC) | Cùng 6 bước + Hard Gates + Socratic Gate |
| §2 — Stakeholder Map 6 cột | `SKILL.md` (§1 Stakeholder Map) | Khớp 100% |
| §2 — BPMN as-is/to-be | `SKILL.md` (§2 BPMN) + `so_do.md` | Mở rộng: Level 0-3, Mermaid syntax, 10 Golden Rules |
| §3 — Cấu trúc Rule | `SKILL.md` (toàn bộ) | Đã hiện thực hóa đầy đủ |
| §4 — Bộ Rule mẫu | `SKILL.md` + `ba-workflow.md` | Rule thực thi có gates + rollback + industry routing |
| §8 — Hard Gates | `SKILL.md` (§HARD GATES) | 5 điều kiện chặn + Product Vision Gate |
| *Chưa có trong Guide* | `SKILL.md` (§MA TRẬN ĐỘC GIẢ) | **MỚI:** 7 loại tài liệu × ngôn ngữ riêng |
| *Chưa có trong Guide* | `Curated templates/` (4 file cốt lõi) | **MỚI:** 01-BRD, 02-SRS, 03-User-Story, 04-AC |
| *Chưa có trong Guide* | `BA-document-rule/overlays/` (7 overlays) | **MỚI:** product, outsource, gov, healthcare, fintech... |
| *Chưa có trong Guide* | `scripts/` (6 audit scripts + 29 tests) | **MỚI:** preflight, quality rubric, traceability scan |
| *Chưa có trong Guide* | `so_do.md` + `SKILL.md` §SƠ ĐỒ | **MỚI:** Diagram Level 0-3, Mermaid shapes, 10 Golden Rules |
| *Chưa có trong Guide* | `SKILL.md` §ANTI-AMBIGUITY + §ID | **MỚI:** Bộ lọc từ mơ hồ + ID naming convention |

> 💡 **Để bắt đầu dự án BA thực tế:** Dùng `@ba-agent` hoặc `@BA-agent/SKILL.md` — hệ thống sẽ tự động kích hoạt quy trình đầy đủ với templates, audit scripts và hard gates.
