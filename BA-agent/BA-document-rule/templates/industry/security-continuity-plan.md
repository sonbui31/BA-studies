# SECURITY & BUSINESS CONTINUITY PLAN — {{TÊN DỰ ÁN}}

> **Phiên bản:** 0.1 | **Ngày:** {{DD/MM/YYYY}}
> **Áp dụng:** 🏛️ Government · 🏥 Healthcare · 💰 Fintech
> **Mục đích:** Security Architecture + DR/BCP + ATTT Assessment

---

## 1. Security Architecture

### 1.1 Threat Model (STRIDE)

| Threat | Mô tả | Component bị ảnh hưởng | Severity | Mitigation |
|--------|-------|----------------------|:--------:|-----------|
| **S**poofing | Giả mạo danh tính | Auth module | 🔴 | MFA, biometric, PKI |
| **T**ampering | Sửa đổi dữ liệu | API, Database | 🔴 | HMAC, digital signature, audit log |
| **R**epudiation | Phủ nhận hành động | Transaction log | 🟡 | Immutable audit trail, timestamp |
| **I**nformation Disclosure | Rò rỉ thông tin | Storage, Network | 🔴 | Encryption, DLP, access control |
| **D**enial of Service | Từ chối dịch vụ | API Gateway | 🟡 | Rate limiting, WAF, CDN |
| **E**levation of Privilege | Leo quyền | Admin panel | 🔴 | RBAC, least privilege, audit |

### 1.2 Security Layers

```
┌─────────────────────────────────────────────────┐
│ LAYER 1: PERIMETER                               │
│   WAF · DDoS Protection · Rate Limiting          │
├─────────────────────────────────────────────────┤
│ LAYER 2: NETWORK                                 │
│   VPN/mTLS · Network Segmentation · Firewall     │
├─────────────────────────────────────────────────┤
│ LAYER 3: APPLICATION                             │
│   Auth (MFA) · RBAC/ABAC · Input Validation      │
├─────────────────────────────────────────────────┤
│ LAYER 4: DATA                                    │
│   Encryption (AES-256) · Tokenization · Masking  │
├─────────────────────────────────────────────────┤
│ LAYER 5: AUDIT                                   │
│   Immutable Logs · SIEM · Alerting               │
└─────────────────────────────────────────────────┘
```

### 1.3 Encryption Requirements

| Data State | Method | Standard | Key Management |
|-----------|--------|----------|:-------------:|
| In-transit | TLS 1.3 | NIST | Certificate rotation (90 ngày) |
| At-rest | AES-256 | NIST | {{KMS / HSM / Vault}} |
| In-use | — | — | Memory protection (nếu cần) |
| Backup | AES-256 | NIST | Separate key from data |

### 1.4 Access Control Matrix

| Role | Module A | Module B | Admin Panel | Audit Logs | Data Export |
|------|:--------:|:--------:|:-----------:|:----------:|:-----------:|
| End User | R/W | R | ❌ | ❌ | ❌ |
| Operator | R/W | R/W | R | R | ❌ |
| Admin | Full | Full | Full | R | R |
| Super Admin | Full | Full | Full | Full | Full |
| Auditor | R | R | R | R | R |

> **Dual Control:** Các hành động {{refund > 10M, user block, config change}} cần ≥ 2 người approve.

---

## 2. Disaster Recovery Plan (DRP)

### 2.1 RPO / RTO Targets

| Tier | Service | RPO | RTO | Ví dụ |
|:----:|---------|:---:|:---:|-------|
| 1 | Core (transaction, khám bệnh) | 0 | ≤ 15 phút | Payment API, HIS core |
| 2 | Important (reporting, admin) | ≤ 1 giờ | ≤ 4 giờ | Dashboard, reports |
| 3 | Normal (static content, docs) | ≤ 24 giờ | ≤ 24 giờ | Knowledge base, FAQ |

### 2.2 DR Architecture

```
┌─────────────────────┐           ┌─────────────────────┐
│   PRIMARY SITE      │           │   DR SITE            │
│   ({{Region A}})    │  ──sync── │   ({{Region B}})     │
│                     │           │                      │
│  App Servers (Active)│          │  App Servers (Standby)│
│  Database (Primary) │──replicate│  Database (Replica)  │
│  Storage (Primary)  │──replicate│  Storage (Replica)   │
└─────────────────────┘           └─────────────────────┘
         │                                  │
         └──────── DNS Failover ────────────┘
```

### 2.3 DR Scenarios & Procedures

| Scenario | Impact | Detection | Failover Steps | Estimated Time |
|---------|:------:|-----------|---------------|:--------------:|
| Database failure | 🔴 | Health check (30s) | Auto-failover to replica | < 5 phút |
| Application crash | 🟡 | Health check (10s) | Auto-restart + scale up | < 2 phút |
| Region outage | 🔴 | Monitoring alert | DNS switch to DR site | < 15 phút |
| Data corruption | 🔴 | Integrity check | Restore from backup (point-in-time) | < 4 giờ |

---

## 3. Business Continuity Plan (BCP)

### 3.1 Incident Severity Classification

| Level | Mô tả | Response Time | Escalation |
|:-----:|-------|:-------------:|-----------|
| P1 — Critical | Service down, data breach | < 15 phút | CTO + CISO + All hands |
| P2 — Major | Chức năng chính bị ảnh hưởng | < 1 giờ | Engineering Lead + Ops |
| P3 — Minor | Chức năng phụ bị ảnh hưởng | < 4 giờ | On-call engineer |
| P4 — Low | Cosmetic, no impact | Next business day | Backlog |

### 3.2 Incident Response Procedure

```
1. DETECT    → Monitoring alert / User report
2. TRIAGE    → Classify severity (P1-P4)
3. CONTAIN   → Isolate affected service
4. MITIGATE  → Apply fix / rollback / failover
5. RESOLVE   → Verify service restored
6. REVIEW    → Post-mortem within 48h
7. IMPROVE   → Update runbook + monitoring
```

### 3.3 Communication Plan (during incident)

| Audience | Channel | Frequency | Template |
|----------|---------|:---------:|---------|
| Engineering team | Slack War Room | Realtime | — |
| Management | Email + Call | Every 30 phút (P1) | Incident Update |
| Customers | Status page + Email | Every 1 giờ | Customer Advisory |
| Regulator (nếu data breach) | Official letter | Within {{72h}} | Breach Notification |

---

## 4. ATTT Assessment (🏛️ Government)

> ⚠️ Bỏ qua section này nếu không phải dự án Government.

### 4.1 Phân cấp hệ thống (NĐ 85/2016)

| Cấp | Tiêu chí | Yêu cầu ATTT |
|:---:|---------|-------------|
| 1 | CNTT nội bộ thông thường | Tự đánh giá |
| 2 | Xử lý dữ liệu công dân | Đánh giá bởi đơn vị chuyên môn |
| 3 | Hệ thống trọng yếu | Đánh giá + chứng nhận bởi cơ quan có thẩm quyền |
| 4 | An ninh quốc gia | Kiểm tra an ninh đặc biệt |

**Hệ thống này thuộc cấp:** ☐ 1 ☐ 2 ☐ 3 ☐ 4

### 4.2 Checklist ATTT

```
☐ Đánh giá rủi ro ATTT hoàn thành
☐ Phương án bảo đảm ATTT được phê duyệt
☐ Kiểm tra xâm nhập (penetration test) đạt
☐ Quy trình ứng cứu sự cố ATTT ban hành
☐ Nhân sự phụ trách ATTT được chỉ định
☐ Log hệ thống lưu trữ ≥ 6 tháng
☐ Backup + DR đã test
```

---

## 5. DR Drill Schedule

| # | Loại drill | Tần suất | Lần gần nhất | Kết quả | Lần tiếp |
|---|-----------|:--------:|:------------:|:------:|:--------:|
| 1 | Tabletop exercise | Hàng quý | {{DD/MM}} | ✅ / ❌ | {{DD/MM}} |
| 2 | Failover test (DB) | 6 tháng | {{DD/MM}} | ✅ / ❌ | {{DD/MM}} |
| 3 | Full DR drill | Hàng năm | {{DD/MM}} | ✅ / ❌ | {{DD/MM}} |
| 4 | Backup restore test | Hàng quý | {{DD/MM}} | ✅ / ❌ | {{DD/MM}} |

---

## ✅ Review Checklist

```
☐ Threat model (STRIDE) cover tất cả components
☐ Security layers spec đầy đủ (perimeter → audit)
☐ Encryption cho mọi data states (transit + rest + backup)
☐ Access control matrix + dual control cho sensitive ops
☐ RPO/RTO targets per service tier
☐ DR architecture diagram + failover procedures
☐ Incident severity classification + response SLA
☐ Communication plan per audience
☐ ATTT assessment per NĐ 85/2016 (nếu Government)
☐ DR drill schedule (≥ quarterly)
```
