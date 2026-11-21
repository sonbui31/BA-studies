# FEATURE MAP
# SignalDesk

> **Phiên bản:** 1.0 | **Ngày:** 12/05/2026
> **Mục đích:** Chuẩn hóa lớp Feature để truy vết BRQ/BR -> FR -> Feature -> US -> TC.

---

## 1. Danh sách Feature

| Feature ID | Feature | Module | Business Ref | Business Rule |
|---|---|---|---|---|
| F01 | Public feedback portal | POR | BRQ-01 | BR-001 |
| F02 | Feedback inbox and triage | TRI | BRQ-02 | — |
| F03 | Duplicate merge | TRI | BRQ-02 | BR-002 |
| F04 | Status notification | STS | BRQ-03 | BR-003, BR-005 |
| F05 | Release notes feed | REL | BRQ-04, BRQ-05 | BR-004 |

> F06 (Saved filters, GĐ3+) chưa có FR nên chưa đưa vào Feature Map; xem `02-BRD.md` Mục 6.

## 2. Phân rã FR → Feature → US → TC

| FR | Feature | Story | Test |
|---|---|---|---|
| FR-POR-001 | F01 | US-POR-001 | TC-POR-001 |
| FR-POR-002 | F01 | US-POR-002 | TC-POR-002 |
| FR-TRI-001 | F02 | US-TRI-001 | TC-TRI-001 |
| FR-TRI-002 | F03 | US-TRI-002 | TC-TRI-002 |
| FR-STS-001 | F04 | US-STS-001 | TC-STS-001, TC-STS-002 |
| FR-STS-002 | F04 | US-STS-001 | TC-STS-001 |
| FR-REL-001 | F05 | US-REL-001 | TC-REL-001 |
