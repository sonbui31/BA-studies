# CẨM NANG 50 KỸ THUẬT PHÂN TÍCH NGHIỆP VỤ CHUẨN BABOK V3
*Tài liệu tra cứu chuyên sâu dành cho Business Analyst, Product Owner và ôn thi CCBA/CBAP.*

---

## 1. TỔNG QUAN

BABOK v3 (A Guide to the Business Analysis Body of Knowledge v3) chuẩn hóa 50 kỹ thuật nền tảng hỗ trợ toàn bộ 6 vùng tri thức (Knowledge Areas). 

Để ứng dụng và ghi nhớ hiệu quả, 50 kỹ thuật được cấu trúc thành 4 nhóm mục đích nghiệp vụ:
1. **Khơi gợi & Tương tác (Elicitation & Collaboration)**: 8 kỹ thuật
2. **Mô hình hóa Quy trình, Hệ thống & Dữ liệu (Modeling & Specifications)**: 17 kỹ thuật
3. **Phân tích Chiến lược & Đánh giá Giải pháp (Strategy & Architecture)**: 11 kỹ thuật
4. **Quản trị, Phân tích Dữ liệu & Ra Quyết định (Governance & Analytics)**: 14 kỹ thuật

---

## 2. BẢNG DANH MỤC 50 KỸ THUẬT THEO NHÓM MỤC ĐÍCH

### Nhóm 1: Khơi Gợi & Tương Tác (Elicitation & Collaboration)

| STT | Tên kỹ thuật | Mục đích nghiệp vụ | Khi nào áp dụng? | Đầu ra chính |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Brainstorming** *(Động não)* | Phát sinh số lượng lớn ý tưởng sáng tạo trong thời gian ngắn mà không phán xét. | Giai đoạn khởi tạo, tìm giải pháp mới, phá vỡ lối mòn tư duy. | Danh mục ý tưởng thô đã phân nhóm. |
| **2** | **Document Analysis** *(Phân tích tài liệu)* | Nghiên cứu hệ thống, quy trình, chính sách và hợp đồng hiện hành. | Khi bắt đầu dự án, trước khi phỏng vấn stakeholder. | Bảng ghi nhận hiện trạng AS-IS, khoảng trống nghiệp vụ. |
| **3** | **Interviews** *(Phỏng vấn)* | Trao đổi trực tiếp 1-1 hoặc 1-nhiều để khai thác thông tin chi tiết. | Khi cần hiểu sâu động cơ, kỳ vọng hoặc nghiệp vụ cá nhân. | Biên bản phỏng vấn, danh sách yêu cầu sơ bộ. |
| **4** | **Observation** *(Quan sát hiện trường)* | Theo dõi thao tác thực tế của người dùng tại nơi làm việc (Active hoặc Passive). | Khi quy trình thao tác tay phức tạp, có nhiều quy tắc ngầm khó diễn đạt bằng lời. | Sơ đồ luồng thao tác thực tế, ghi nhận thời gian chu kỳ. |
| **5** | **Workshops** *(Hội thảo tập trung)* | Tập hợp các bên liên quan đa phòng ban để làm rõ và thống nhất yêu cầu. | Khi các bên có xung đột lợi ích hoặc cần chốt phạm vi nhanh. | Biên bản thống nhất, danh mục yêu cầu đã ký nháy. |
| **6** | **Focus Groups** *(Nhóm thảo luận tập trung)* | Khảo sát ý kiến của một nhóm người dùng đại diện về một chủ đề cụ thể. | Nghiên cứu thị trường, đánh giá cảm nhận về sản phẩm/tính năng mới. | Báo cáo cảm nhận và xu hướng hành vi người dùng. |
| **7** | **Requirements Workshops** *(Hội thảo yêu cầu)* | Phiên làm việc chuyên sâu để chi tiết hóa và chuẩn hóa các yêu cầu phần mềm. | Giai đoạn đặc tả BRD/SRS, làm mịn Product Backlog. | Bản thảo yêu cầu chi tiết (FR, NFR, Business Rules). |
| **8** | **Collaborative Games** *(Trò chơi cộng tác)* | Áp dụng cơ chế game (Product Box, Speed Boat) để kích thích tư duy tập thể. | Khi stakeholder ngại chia sẻ hoặc thiếu động lực trong buổi họp thông thường. | Danh mục nỗi đau (Pains) và mong muốn (Gains) ưu tiên. |

---

### Nhóm 2: Mô Hình Hóa Quy Trình, Hệ Thống & Dữ Liệu (Modeling & Specifications)

| STT | Tên kỹ thuật | Mục đích nghiệp vụ | Khi nào áp dụng? | Đầu ra chính |
| :---: | :--- | :--- | :--- | :--- |
| **9** | **Process Modeling** *(Mô hình hóa quy trình)* | Trực quan hóa các bước thực hiện công việc tuần tự qua BPMN hoặc Flowchart. | Phân tích hiện trạng (AS-IS) và thiết kế quy trình tương lai (TO-BE). | Sơ đồ quy trình Swimlane BPMN 2.0. |
| **10** | **Use Cases** *(Trường hợp sử dụng)* | Mô tả chuỗi tương tác chi tiết giữa Actor và hệ thống để đạt mục tiêu cụ thể. | Đặc tả phần mềm hướng đối tượng, làm cơ sở kiểm thử chức năng. | Tài liệu đặc tả Use Case (Luồng chính, Luồng phụ, Ngoại lệ). |
| **11** | **Use Case Diagrams** *(Sơ đồ Use Case)* | Thể hiện tổng quan ranh giới hệ thống, các Actor và Use Case. | Giới thiệu bức tranh chức năng tổng thể cho Tech Lead và PO. | Sơ đồ Use Case chuẩn UML. |
| **12** | **Scenarios and Use Cases** *(Kịch bản)* | Xây dựng câu chuyện ngữ cảnh cụ thể khi người dùng tương tác với hệ thống. | Làm rõ kịch bản biên, kịch bản lỗi phát sinh trong thực tế. | Bảng kịch bản tương tác từng bước. |
| **13** | **User Stories** *(Câu chuyện người dùng)* | Mô tả yêu cầu theo cấu trúc người dùng: *"Là ai, tôi muốn gì, để làm gì"*. | Phát triển phần mềm theo mô hình Agile/Scrum. | Thẻ User Story chuẩn INVEST. |
| **14** | **State Diagrams** *(Sơ đồ trạng thái)* | Mô hình hóa các trạng thái và điều kiện chuyển dịch của một đối tượng dữ liệu. | Quản lý vòng đời đơn hàng, vé hỗ trợ, hồ sơ ứng viên. | Sơ đồ State Machine (Enum chuẩn). |
| **15** | **Sequence Diagrams** *(Sơ đồ tuần tự)* | Trực quan hóa việc truyền nhận thông điệp giữa các thành phần theo thời gian. | Thiết kế tích hợp API, vi dịch vụ (Microservices), xử lý bất đồng bộ. | Sơ đồ Sequence Diagram chuẩn UML. |
| **16** | **Data Flow Diagrams (DFD)** *(Sơ đồ luồng dữ liệu)* | Mô tả sự di chuyển của dữ liệu qua các tiến trình xử lý và kho lưu trữ. | Phân tích kiến trúc dữ liệu và điểm vào/ra của hệ thống. | Sơ đồ DFD cấp 0, cấp 1. |
| **17** | **Data Modeling** *(Mô hình hóa dữ liệu)* | Định nghĩa các thực thể, thuộc tính và mối quan hệ giữa dữ liệu (ERD). | Thiết kế cơ sở dữ liệu quan hệ cho Tech Lead và Database Architect. | Sơ đồ ERD (Conceptual, Logical, Physical). |
| **18** | **Data Dictionary & Glossary** *(Từ điển dữ liệu)* | Định nghĩa chi tiết kiểu dữ liệu, độ dài, quy tắc kiểm tra và giải thích thuật ngữ. | Chuẩn hóa ngôn ngữ chung giữa nghiệp vụ và kỹ thuật. | Bảng Data Dictionary 7 cột và bảng Glossary. |
| **19** | **Interface Analysis** *(Phân tích giao diện/điểm chạm)* | Xác định các điểm giao tiếp giữa các hệ thống, thiết bị hoặc người dùng. | Dự án tích hợp hệ thống ngoài (Cổng thanh toán, ERP, CRM). | Bản đặc tả Interface Spec, hợp đồng API. |
| **20** | **Documenting Interface Analysis** | Lập tài liệu chi tiết hóa kết quả phân tích điểm giao tiếp kỹ thuật. | Bàn giao cho đội ngũ phát triển Backend và Tích hợp. | Tài liệu API Contract, bảng mapping trường dữ liệu. |
| **21** | **Interface Mockups** *(Bản vẽ giao diện)* | Bản vẽ tĩnh thể hiện cấu trúc bố cục, vị trí nút bấm và nội dung màn hình. | Xác nhận layout và trải nghiệm người dùng với Product Manager. | Wireframe hoặc Mockup Figma. |
| **22** | **Prototyping** *(Bản mẫu thử nghiệm)* | Tạo mô hình mô phỏng tương tác động để người dùng bấm thử nghiệm luồng. | Kiểm thử tính khả dụng (Usability Testing) trước khi viết mã nguồn. | Clickable Prototype (Figma, Axure). |
| **23** | **Storyboarding** *(Bảng cốt truyện)* | Chuỗi hình ảnh trực quan hóa hành trình trải nghiệm của khách hàng theo thời gian. | Thiết kế trải nghiệm khách hàng (Customer Journey), thuyết trình ý tưởng. | Bộ tranh Storyboard trực quan. |
| **24** | **Documenting Business Rules** | Văn bản hóa các quy tắc vận hành độc lập với phần mềm (chiết khấu, điều kiện vay). | Đảm bảo tính tuân thủ chính sách và bảo vệ tính toàn vẹn của nghiệp vụ. | Danh mục Business Rules (`BR-*`) chi tiết. |
| **25** | **Non-Functional Requirements (NFR)** | Đặc tả các chỉ số chất lượng hệ thống: bảo mật, hiệu năng, tính sẵn sàng. | Thiết lập tiêu chuẩn nghiệm thu hạ tầng và kiểm thử tải. | Bảng NFRs định lượng có SLA rõ ràng. |

---

### Nhóm 3: Phân Tích Chiến Lược & Đánh Giá Giải Pháp (Strategy & Architecture)

| STT | Tên kỹ thuật | Mục đích nghiệp vụ | Khi nào áp dụng? | Đầu ra chính |
| :---: | :--- | :--- | :--- | :--- |
| **26** | **SWOT Analysis** | Phân tích Điểm mạnh, Điểm yếu, Cơ hội và Thách thức của tổ chức. | Định hình chiến lược sản phẩm, đánh giá khả năng cạnh tranh. | Ma trận 4 ô SWOT. |
| **27** | **Benchmarking & Market Analysis** | Đối sánh quy trình và hiệu suất nội bộ với đối thủ cạnh tranh và tiêu chuẩn ngành. | Tìm kiếm khoảng cách để cải tiến hoặc xác định tính năng tạo lợi thế. | Báo cáo phân tích đối thủ cạnh tranh. |
| **28** | **Business Capability Analysis** | Đánh giá năng lực cốt lõi của doanh nghiệp cần bổ sung để đạt mục tiêu mới. | Tái cấu trúc tổ chức, chuyển đổi số toàn diện. | Bản đồ năng lực doanh nghiệp (Capability Map). |
| **29** | **Business Cases** | Xây dựng tài liệu giải trình hiệu quả kinh tế và tính khả thi của dự án. | Đệ trình Ban Giám đốc hoặc Nhà tài trợ phê duyệt ngân sách. | Hồ sơ Business Case (Chi phí, Lợi ích, ROI, Rủi ro). |
| **30** | **Business Model Canvas** | Trực quan hóa 9 khối thành phần cốt lõi cấu thành mô hình kinh doanh. | Khởi tạo sản phẩm mới, tái định vị mô hình vận hành. | Bảng Canvas 9 ô chuẩn Osterwalder. |
| **31** | **Cost-Benefit Analysis** | Đo lường chi phí đầu tư so sánh với lợi ích tài chính thu về trong vòng đời dự án. | Lựa chọn phương án triển khai tối ưu giữa nhiều giải pháp. | Bảng tính tài chính (NPV, IRR, Payback Period). |
| **32** | **Gap Analysis** | Phân tích khoảng cách giữa hiện trạng (AS-IS) và trạng thái mong muốn (TO-BE). | Xác định chính xác phạm vi công việc cần thực hiện. | Bảng Gap Matrix (Hiện trạng, Mục tiêu, Hành động). |
| **33** | **Functional Decomposition** | Phân rã chức năng lớn phức tạp thành các module và tính năng con nhỏ hơn. | Quản lý phạm vi dự án, lập cấu trúc phân rã công việc (WBS). | Cây phân rã chức năng (Decomposition Tree). |
| **34** | **Organization Modeling** | Phân tích cấu trúc thứ bậc, phòng ban và tuyến báo cáo trong tổ chức. | Xác định các đơn vị chịu ảnh hưởng khi triển khai quy trình mới. | Sơ đồ cơ cấu tổ chức (Org Chart). |
| **35** | **Role Modeling** | Định nghĩa vai trò, thẩm quyền và trách nhiệm của từng vị trí trong hệ thống. | Thiết lập phân quyền truy cập người dùng (RBAC Matrix). | Ma trận phân quyền chức năng và dữ liệu. |
| **36** | **Vendor Assessment** | Đánh giá và chấm điểm năng lực của các nhà cung cấp giải pháp bên ngoài. | Ra quyết định Tự xây dựng (Build) hay Mua sẵn (Buy). | Bảng chấm điểm nhà cung cấp có trọng số. |

---

### Nhóm 4: Quản Trị, Phân Tích Dữ Liệu & Ra Quyết Định (Governance & Analytics)

| STT | Tên kỹ thuật | Mục đích nghiệp vụ | Khi nào áp dụng? | Đầu ra chính |
| :---: | :--- | :--- | :--- | :--- |
| **37** | **Decision Analysis** | Đánh giá định lượng các phương án giải pháp dựa trên ma trận tiêu chí có trọng số. | Chọn giải pháp kiến trúc, công nghệ hoặc quy trình tối ưu. | Ma trận quyết định đa tiêu chí (Decision Matrix). |
| **38** | **Decision Trees** | Trực quan hóa các phương án rẽ nhánh và hệ quả xác suất/tài chính tương ứng. | Đưa ra quyết định trong điều kiện có nhiều rủi ro bất định. | Sơ đồ cây quyết định. |
| **39** | **Root Cause Analysis (RCA)** | Tìm kiếm nguyên nhân gốc rễ của vấn đề (Fishbone Ishikawa, 5 Whys). | Xử lý lỗi hệ thống nghiêm trọng, tối ưu quy trình nghẽn. | Biểu đồ xương cá, báo cáo 5 Whys. |
| **40** | **Risk Analysis & Management** | Nhận diện, phân tích xác suất/tác động và lập kế hoạch ứng phó rủi ro. | Quản trị dự án từ đầu đến khi bàn giao nghiệm thu. | Sổ đăng ký rủi ro (Risk Register / RAID Log). |
| **41** | **Dependency Modeling** | Lập bản đồ phụ thuộc giữa các yêu cầu, module và hệ thống bên ngoài. | Sắp xếp thứ tự ưu tiên Sprint, quản trị đường găng dự án. | Ma trận hoặc đồ thị liên kết phụ thuộc. |
| **42** | **Metrics and KPIs** | Xác lập các chỉ số định lượng đo lường mức độ thành công của giải pháp. | Đánh giá sau triển khai (Post-implementation Review). | Bộ chỉ số đo lường hiệu quả (KPIs, OKRs). |
| **43** | **Kano Model Analysis** | Phân loại tính năng sản phẩm theo mức độ hài lòng của khách hàng. | Ưu tiên Backlog sản phẩm (Cơ bản, Hiệu năng, Đột phá). | Biểu đồ phân bổ tính năng Kano. |
| **44** | **Acceptance & Evaluation Criteria** | Xác định tiêu chuẩn định lượng để nghiệm thu sản phẩm hoặc chuyển giai đoạn. | Bàn giao phần mềm giữa Dev, QA và Khách hàng. | Tiêu chí chấp thuận (Definition of Done, AC). |
| **45** | **Backlog Management** | Tiếp nhận, làm mịn, phân loại và sắp xếp độ ưu tiên danh mục công việc. | Vận hành sản phẩm liên tục trong môi trường Scrum/Kanban. | Product Backlog được sắp xếp thứ tự ưu tiên. |
| **46** | **Estimation** | Dự đoán quy mô, nỗ lực, chi phí và thời gian cần thiết để thực hiện công việc. | Lập kế hoạch dự án, phân bổ nguồn lực và báo giá. | Bản ước lượng (Story Points, Man-days, Chi phí). |
| **47** | **Problem Tracking** | Ghi nhận, phân loại và theo dõi tiến độ xử lý các lỗi/khúc mắc phát sinh. | Vận hành dự án hàng ngày, hỗ trợ giai đoạn UAT. | Nhật ký theo dõi vấn đề (Issue Log / Bug Tracker). |
| **48** | **Data Mining** | Khai phá kho dữ liệu lớn để tìm kiếm quy luật, hành vi bất thường hoặc xu hướng. | Phát hiện gian lận, xây dựng mô hình dự báo kinh doanh. | Báo cáo phân tích dữ liệu, mô hình phân cụm. |
| **49** | **Social Media Analysis** | Thu thập và phân tích phản hồi, cảm xúc của công chúng trên mạng xã hội. | Nghiên cứu thương hiệu, đo lường sự đón nhận tính năng mới. | Báo cáo phân tích cảm xúc (Sentiment Analysis). |
| **50** | **Data Migration Planning** | Lập kế hoạch chuyển đổi, làm sạch, ánh xạ và di chuyển dữ liệu sang hệ thống mới. | Khi thay thế phần mềm cũ (Legacy System Replacement). | Kế hoạch di chuyển dữ liệu (Data Migration Spec). |

---

## 3. 14 CHIẾN LƯỢC GHI NHỚ PHẢN XẠ (HỌC NHANH - NHỚ LÂU)

1. **Grouping (Gom nhóm nghiệp vụ):** Nhớ theo 4 nhóm mục đích lớn (Khơi gợi 8, Mô hình hóa 17, Chiến lược 11, Quản trị 14) thay vì cố nhớ 50 kỹ thuật rời rạc.
2. **Chunking (Chia nhỏ danh mục):** Chia lộ trình học thành 5 tuần, mỗi tuần dung nạp đúng 10 kỹ thuật.
3. **Flashcards:** Dùng thẻ 2 mặt: Mặt trước ghi tên kỹ thuật $\leftrightarrow$ Mặt sau ghi 3 dòng: *Mục đích, Khi nào dùng, Đầu ra chính*.
4. **Visual Mind Map:** Vẽ bản đồ tư duy nối 50 kỹ thuật vào 6 Vùng tri thức của BABOK v3.
5. **Create Stories (Gắn vào câu chuyện dự án):** Tưởng tượng hành trình làm một dự án thật từ đầu đến cuối: *"Tiếp nhận dự án dùng SWOT & Business Case $\rightarrow$ Khơi gợi dùng Interview & Observation $\rightarrow$ Mô hình hóa dùng BPMN & Use Case $\rightarrow$ Thiết kế giao diện dùng Mockup $\rightarrow$ Nghiệm thu dùng Acceptance Criteria"*.
6. **Practice with Examples:** Áp dụng tối thiểu 1 lần mỗi kỹ thuật vào tài liệu thực tế của công việc.
7. **Teach Someone Else (Feynman Technique):** Giải thích nguyên lý kỹ thuật cho Junior BA hoặc đồng nghiệp trong 3 phút. Nếu giải thích không gãy gọn là chưa nắm chắc.
8. **Mnemonics (Từ khóa viết tắt):** Ghép chữ cái đầu của các nhóm thành từ khóa gợi nhớ.
9. **Acrostics (Thơ vần):** Tạo các câu văn ngắn có nghĩa từ chữ cái đầu của các kỹ thuật trọng tâm.
10. **Regular Review (Chu kỳ ngắt quãng):** Ôn tập theo nhịp 1 ngày $\rightarrow$ 3 ngày $\rightarrow$ 7 ngày $\rightarrow$ 30 ngày.
11. **Associations (Liên tưởng đời thường):** Gắn kỹ thuật trừu tượng với hành động quen thuộc (VD: *Observation giống như quan sát giao thông để đặt đèn đỏ; Functional Decomposition giống như rã xe máy ra từng phụ tùng*).
12. **Multi-sensory Learning:** Đọc tài liệu, vẽ sơ đồ tay ra giấy A4, nói to thành tiếng định nghĩa.
13. **Online Quiz & Mock Tests:** Làm đề trắc nghiệm tình huống CCBA/CBAP để rèn luyện phản xạ chọn kỹ thuật đúng theo bối cảnh đề bài.
14. **Spaced Repetition App (Anki):** Nạp toàn bộ 50 kỹ thuật vào app Anki để thuật toán tự động nhắc lại đúng thời điểm não bộ sắp quên.
