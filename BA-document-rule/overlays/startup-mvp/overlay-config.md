# OVERLAY: STARTUP / MVP

> **Áp dụng:** Startup giai đoạn đầu, MVP, proof of concept
> **Đặc điểm:** Lean, nhanh, tối thiểu tài liệu, validate giả thuyết

---

## 1. Tài liệu — Chỉ giữ những gì CẦN THIẾT

| # | Tài liệu | Bắt buộc? | Ghi chú |
|---|----------|----------|---------|
| 1 | **Lean Canvas** | ✅ Bắt buộc | **Thay Vision & Scope + BRD** (1 trang) |
| 2 | User Story Map | ✅ Bắt buộc | **Chỉ MVP slice** — tối đa 10-15 stories |
| 3 | Process Flow | ⚠️ Khuyến nghị | Chỉ core flow (1-2 diagram) |
| 4 | Data Model | ⚠️ Khuyến nghị | ERD cơ bản, 3-5 entities |
| 5 | API Specification | ☐ Tùy chọn | Postman collection thay Swagger |
| — | SRS, BRD, Stakeholder Map, UAT Plan | ❌ **Bỏ** | Overkill cho MVP |
| — | Change Log, Meeting Minutes | ❌ **Bỏ** | Team nhỏ, talk > doc |
| — | Handover Checklist | ❌ **Bỏ** | Chưa cần |

> **Tổng: 2-4 tài liệu** thay vì 12.

---

## 2. Lean Canvas — 1 trang thay BRD

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│   PROBLEM    │   SOLUTION   │  UNIQUE      │  UNFAIR      │  CUSTOMER    │
│              │              │  VALUE       │  ADVANTAGE   │  SEGMENTS    │
│ Top 3 vấn đề│ Top 3 giải   │  PROPOSITION │              │              │
│              │ pháp         │              │ Điều đối thủ │ Ai là target │
│ 1.           │ 1.           │ Tại sao KH   │ không copy   │ user?        │
│ 2.           │ 2.           │ phải chọn    │ được?        │              │
│ 3.           │ 3.           │ bạn?         │              │ Early        │
│              │              │              │              │ Adopters:    │
├──────────────┤              ├──────────────┤              │              │
│  EXISTING    │              │   KEY        │              │              │
│ ALTERNATIVES │              │   METRICS    │              │              │
│              │              │              │              │              │
│ KH đang giải│              │ AARRR:       │              │              │
│ quyết thế   │              │ - Acquisition│              │              │
│ nào?         │              │ - Activation │              │              │
│              │              │ - Retention  │              │              │
│              │              │ - Revenue    │              │              │
│              │              │ - Referral   │              │              │
├──────────────┼──────────────┼──────────────┼──────────────┤              │
│  CHANNELS    │              │              │              │              │
│              │  COST        │              │  REVENUE     │              │
│ Kênh tiếp   │  STRUCTURE   │              │  STREAMS     │              │
│ cận KH?     │              │              │              │              │
│              │ Chi phí chính│              │ Kiếm tiền    │              │
│              │              │              │ bằng cách    │              │
│              │              │              │ nào?         │              │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

---

## 3. MVP Scope — Razor Sharp

### Build-Measure-Learn Cycle

```
        ┌──────────┐
        │   IDEA   │ ← Lean Canvas
        └────┬─────┘
             ↓
        ┌──────────┐
        │  BUILD   │ ← MVP (2-4 tuần)
        │  (MVP)   │
        └────┬─────┘
             ↓
        ┌──────────┐
        │ MEASURE  │ ← Key Metrics (AARRR)
        └────┬─────┘
             ↓
        ┌──────────┐
        │  LEARN   │ ← Pivot or Persevere?
        └────┬─────┘
             ↓
        (Quay lại IDEA hoặc SCALE)
```

### MVP Scope Checklist

```
☐ Chỉ giải quyết TOP 1 vấn đề (không phải top 3)
☐ Tối đa 3-5 core features
☐ Kano: CHỈ Basic + 1 Excitement (wow factor)
☐ MoSCoW: 100% Must, 0% Should/Could/Won't
☐ Timeline: 2-4 tuần
☐ Team: 1-3 người
```

---

## 4. Khi nào UPGRADE từ Startup → Product overlay?

| Signal | Hành động |
|--------|----------|
| Product-market fit confirmed (retention > 40%) | Chuyển sang Product overlay |
| Team > 5 người | Cần SRS Lite + Process Flow |
| Funding round | Cần BRD/PRD cho investors |
| Khách hàng enterprise | Cần formal docs |
