# NFR DISCOVERY GUIDE — Kỹ Thuật Phát Hiện Yêu Cầu Phi Chức Năng (v3.3)

> **Mục đích:** Dạy BA CÁCH TÌM NFR — không chỉ fill template sẵn.
> **Vấn đề:** 80% BA copy-paste "Response < 3s, 99.9% uptime" cho MỌI dự án. NFR cần SPECIFIC cho từng project.
> **BABOK KA:** Requirements Analysis & Design Definition

---

## 1. NFR Discovery Matrix — 7 Câu hỏi Khám phá

> **Quy tắc:** Hỏi 7 câu này với Tech Lead + Product Owner + End User → suy ra NFR cụ thể.

| # | Câu hỏi Discovery | NFR Category suy ra | Ví dụ Output |
|---|-------------------|--------------------|--------------------|
| 1 | "Có bao nhiêu user dùng đồng thời vào giờ cao điểm?" | **Performance** (Concurrent Users) | NFR-PERF: Support 500 concurrent users |
| 2 | "Nếu hệ thống sập 1 giờ, thiệt hại bao nhiêu tiền/uy tín?" | **Availability** (RTO, Uptime) | NFR-AVA: 99.9% uptime, RTO ≤ 30 min |
| 3 | "Dữ liệu hệ thống có PII (CMND, SĐT, y tế) không?" | **Security** (Encryption, Compliance) | NFR-SEC: AES-256 at-rest, TLS 1.3 in-transit |
| 4 | "User ở Việt Nam hay toàn cầu? Dùng 3G hay WiFi?" | **Performance** (Latency, CDN) | NFR-PERF: Latency < 200ms cho user VN |
| 5 | "Dữ liệu tăng bao nhiêu GB/tháng? Bao nhiêu năm lưu trữ?" | **Scalability** (Storage, Growth) | NFR-SCA: Support 100GB/year, retention 7 years |
| 6 | "Có quy định pháp lý nào bắt buộc? (GDPR, HIPAA, Thông tư...)" | **Compliance** (Audit, Logging) | NFR-COMP: Audit trail 5 years, HIPAA compliant |
| 7 | "User kinh nghiệm IT thế nào? Có training không?" | **Usability** (Learning Curve) | NFR-USA: Task completion ≤ 3 clicks for basic ops |

---

## 2. NFR Elicitation Techniques (5 phương pháp)

### 2.1 Stakeholder Interview — Kỹ thuật "What If" 

```
"Nếu hệ thống chậm 10 giây, anh/chị có chấp nhận không?" → Performance
"Nếu mất dữ liệu 1 ngày, thiệt hại bao nhiêu?" → Backup/RPO
"Nếu hacker xâm nhập, dữ liệu nào TUYỆT ĐỐI không được lộ?" → Security
"Nếu số user tăng gấp 5 năm sau, hệ thống có chịu được không?" → Scalability
"User mới không training, có tự dùng được không?" → Usability
```

### 2.2 Benchmark Analysis — So sánh với hệ thống tương đương

| Hệ thống tham chiếu | NFR của họ | Áp dụng cho dự án |
|---------------------|----------|-----------------|
| {{Competitor/Similar system}} | API Response < 500ms | NFR-PERF-01: API < 500ms (p95) |
| {{Industry standard}} | 99.9% uptime (SLA) | NFR-AVA-01: 99.9% uptime |
| {{Compliance framework}} | OWASP Top 10 compliant | NFR-SEC-01: Pass OWASP scan |

### 2.3 Historical Data — Học từ dự án cũ

```
Dự án cũ bị phạt SLA vì response > 5s → NFR-PERF: Response < 2s (buffer 60%)
Dự án cũ bị hack vì không mã hóa → NFR-SEC: Mã hóa AES-256 tất cả PII
Dự án cũ user than khó dùng → NFR-USA: SUS score ≥ 70
```

### 2.4 Regulatory Scan — Quét quy định pháp lý

| Lĩnh vực | Quy định | NFR bắt buộc |
|----------|---------|-------------|
| Y tế | Thông tư 46/2018 | Lưu trữ hồ sơ 10 năm, audit trail |
| Tài chính | Circular 09/2020 | Two-factor auth, transaction logging |
| E-commerce | NĐ 52/2013 | Bảo vệ thông tin người tiêu dùng |
| Chung | PDPA/GDPR | Right to erasure, consent management |

### 2.5 Failure Mode Analysis — Nghĩ ngược từ failure

| What if...? | Failure Mode | NFR ngăn chặn |
|------------|-------------|---------------|
| Server bị sập | Downtime | NFR-AVA: Auto-failover < 30s |
| Database bị xóa | Data Loss | NFR-BAK: Daily backup, RPO ≤ 1h |
| DDoS attack | Service Denial | NFR-SEC: Rate limiting, WAF |
| Disk đầy | Storage Failure | NFR-MON: Alert khi disk > 80% |
| Dependency timeout | Integration Failure | NFR-RES: Circuit breaker, retry 3x |

---

## 3. NFR Prioritization — Không phải NFR nào cũng bằng nhau

| Priority | Criteria | Ví dụ |
|:--------:|---------|-------|
| **P1 — Blocker** | Thiếu → hệ thống không thể go-live | Security authentication, Data backup |
| **P2 — Critical** | Thiếu → go-live nhưng SLA bị vi phạm | Performance, Availability |
| **P3 — Important** | Thiếu → user experience giảm | Usability, Accessibility |
| **P4 — Nice-to-have** | Thiếu → không ảnh hưởng ngay | Monitoring dashboards, Auto-scaling |

---

## 4. NFR Specification Template

Mỗi NFR viết theo format:

```markdown
| Thuộc tính | Chi tiết |
|-----------|---------|
| **ID** | NFR-[CAT]-[NNN] |
| **Category** | Performance / Security / Availability / Usability / Scalability / Compliance |
| **Statement** | Hệ thống PHẢI [hành vi] trong điều kiện [context] với target [metric] |
| **Metric** | [Số đo cụ thể] |
| **Target** | [Giá trị mục tiêu] |
| **Measurement** | [Cách đo: tool, phương pháp] |
| **Priority** | P1 / P2 / P3 / P4 |
| **Trace** | BRQ-[xxx] |
| **Discovery Method** | Interview / Benchmark / Regulatory / Failure Mode |
```

**Ví dụ đầy đủ:**
```
NFR-PERF-001:
  Statement: API PHẢI trả response trong điều kiện 500 concurrent users
  Metric: Response time (p95)
  Target: < 500ms
  Measurement: Load test với k6/JMeter
  Priority: P2
  Trace: BRQ-03 ("Hệ thống phải nhanh")
  Discovery: Interview Tech Lead — "500 y bác sĩ dùng cùng lúc ca sáng"
```

---

## 5. Lệnh Kích hoạt

```
@ba-specialist khám phá NFR cho dự án [X] dùng 7 câu hỏi discovery
@ba-specialist scan regulatory requirements cho lĩnh vực [Y tế / Tài chính / ...]
@ba-specialist phân tích failure modes cho hệ thống [Z]
@ba-specialist đánh giá NFR coverage trong SRS hiện tại
```
