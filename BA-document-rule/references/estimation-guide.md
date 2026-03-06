# HƯỚNG DẪN ƯỚC LƯỢNG (Estimation Guide)

> **Mục đích:** Hỗ trợ BA ước lượng effort phục vụ lập kế hoạch

---

## 1. Phương pháp ước lượng

| Phương pháp | Mô tả | Khi nào dùng | Độ chính xác |
|------------|-------|-------------|-------------|
| **T-Shirt Sizing** | XS, S, M, L, XL | Ước lượng sơ bộ, epics | Thấp (±50%) |
| **Story Points** | Fibonacci (1,2,3,5,8,13,21) | Sprint planning, stories | Trung bình (±25%) |
| **Planning Poker** | Team cùng ước lượng, thảo luận | Sprint planning | Trung bình |
| **3-Point** | (O + 4M + P) / 6 | Khi cần range | Cao (±15%) |
| **ROM** | Rough Order of Magnitude | Proposal, pre-project | Thấp (±50%) |

---

## 2. T-Shirt Sizing

| Size | Story Points | Man-days (tham khảo) | Ví dụ |
|------|-------------|---------------------|-------|
| **XS** | 1 | 0.5 ngày | Fix typo, đổi label |
| **S** | 2-3 | 1-2 ngày | CRUD đơn giản, filter list |
| **M** | 5 | 3-5 ngày | Feature trung bình, form + validation |
| **L** | 8-13 | 5-10 ngày | Feature phức tạp, tích hợp API |
| **XL** | 21+ | > 10 ngày | **Cần tách nhỏ** — quá lớn cho 1 story |

---

## 3. Planning Poker — Quy trình

```
1. BA trình bày story + AC
2. Dev team đặt câu hỏi
3. Mỗi người chọn số (Fibonacci) úp xuống
4. Đồng thời lật bài
5. Nếu chênh lệch > 2 bậc → người cao nhất + thấp nhất giải thích → vote lại
6. Consensus → ghi nhận điểm
```

---

## 4. Three-Point Estimation

**Công thức:** `E = (O + 4M + P) / 6`

| Ký hiệu | Ý nghĩa |
|---------|---------|
| **O** (Optimistic) | Best case — mọi thứ suôn sẻ |
| **M** (Most Likely) | Trường hợp phổ biến nhất |
| **P** (Pessimistic) | Worst case — gặp trở ngại |

**Ví dụ:**
```
O = 3 ngày, M = 5 ngày, P = 12 ngày
E = (3 + 4×5 + 12) / 6 = 35/6 ≈ 5.8 ngày
```

---

## 5. Velocity — Tính toán

```
Velocity = Trung bình Story Points hoàn thành / Sprint (3 sprint gần nhất)

Sprint 1: 25 SP
Sprint 2: 30 SP
Sprint 3: 28 SP
→ Velocity = (25 + 30 + 28) / 3 = 27.7 ≈ 28 SP/sprint

Tổng backlog: 140 SP
Số sprint cần: 140 / 28 = 5 sprints
Timeline: 5 × 2 tuần = 10 tuần
```

---

## 6. Tips ước lượng

1. **Ước lượng Relative, không Absolute** — so sánh story này vs story trước, không đoán số ngày
2. **Spike cho unknowns** — không biết → tạo Spike (time-boxed research) trước khi ước lượng
3. **Buffer 20-30%** — cho rủi ro, meetings, context switching
4. **Ước lượng cả testing** — Dev done ≠ Story done
5. **Re-estimate khi scope thay đổi** — CR → tính lại timeline
