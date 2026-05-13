# STAKEHOLDER CONFLICT RESOLUTION — Giải quyết Xung đột Yêu cầu

> **Mục đích:** Xử lý mâu thuẫn giữa Sponsor, PO, Ops, Compliance, Dev Lead, và End-User trước khi conflict lan sang BRD/SRS/UAT.
> **Khi dùng:** Khi có 2+ stakeholder đưa ra yêu cầu không thể cùng đúng, hoặc cùng đúng nhưng không thể cùng ưu tiên.

---

## 1. Conflict Types

| Type | Ví dụ | Hậu quả nếu không xử lý |
|---|---|---|
| **Priority Conflict** | Sponsor muốn release nhanh, Ops muốn thêm controls | Scope mơ hồ, UAT nổ |
| **Policy Conflict** | Compliance cấm một flow mà Product muốn giữ | FR đúng theo user, sai theo luật |
| **Workflow Conflict** | Ops muốn 4 bước kiểm soát, End-User muốn 1 bước | AC mâu thuẫn |
| **Metric Conflict** | CFO muốn giảm cost, Architect muốn HA cao | NFR không thực tế |
| **Ownership Conflict** | Không rõ ai có quyền chốt | Sign-off treo |

---

## 2. Resolution Protocol

1. **Log conflict**
   Ghi 1 dòng riêng cho từng conflict, không để lẫn trong meeting notes.
2. **Classify decision owner**
   Business, Legal/Compliance, Operational, Technical, hoặc Financial.
3. **Freeze wording**
   Không chỉnh BRD/SRS cho tới khi owner quyết.
4. **Prepare trade-off summary**
   Viết 3 phần: option, benefit, cost/risk.
5. **Record final ruling**
   Ghi quyết định cuối cùng, owner, ngày, lý do, artifact bị ảnh hưởng.

---

## 3. Decision Ownership Matrix

| Conflict Area | Primary Decider | Must Consult | Artifact to Update |
|---|---|---|---|
| Business priority | Sponsor / PO | PM, BA | BRD, Story Map |
| Compliance / privacy | Compliance | Security, BA | BRD, SRS, Regulatory Matrix |
| Operational workflow | Ops Manager | End-User, BA | Process Flow, SRS, UAT |
| Technical constraint | Tech Lead / Architect | BA, PM | SRS, NFR, Data Model |
| Budget / ROI | CFO / Sponsor | PM, BA | BRD, Decision Log |

---

## 4. Conflict Log Template

| Conflict ID | Issue | Stakeholders | Options | Decision Owner | Due Date | Status |
|---|---|---|---|---|---|---|
| CON-001 | MFA bắt buộc hay adaptive MFA | Product, Security, Compliance | A/B/C | CISO | 14/05/2026 | Open |

### Detailed Decision Record

| Field | Content |
|---|---|
| Conflict ID | CON-001 |
| Decision area | Security / UX |
| Business goal at risk | Conversion |
| Control goal at risk | Account takeover |
| Option A | Always-on MFA |
| Option B | Adaptive MFA |
| Option C | No MFA |
| Final ruling | Option B |
| Rationale | Giảm fraud nhưng không giết conversion |
| Approved by | CISO + Product Owner |
| Affected artifacts | BRD-104, FR-AUTH-006, NFR-SEC-002, UAT-SEC-004 |

---

## 5. Update Rules After Resolution

- Nếu conflict đổi **business scope**: update BRD trước.
- Nếu conflict đổi **behavior**: update SRS rồi Story Map.
- Nếu conflict đổi **control/testability**: update UAT + compliance matrix.
- Nếu conflict chưa chốt: đánh dấu `PENDING DECISION`, không được ghi như requirement đã approved.
