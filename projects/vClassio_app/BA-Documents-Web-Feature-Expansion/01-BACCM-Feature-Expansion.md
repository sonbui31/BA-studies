# BACCM ANALYSIS
# Mo rong tinh nang web quan ly trung tam dao tao

> **Phien ban:** 1.0  
> **Ngay:** 27/07/2026  
> **Trang thai:** Draft  
> **Pham vi:** Quan ly hoc sinh, quan ly giao vien, voucher khoa hoc, tinh chinh hoc phi, BTVN

---

## 1. Executive Summary

He thong web hien tai can duoc mo rong de dap ung day du nghiep vu van hanh trung tam dao tao sau khi hoc sinh dang ky khoa hoc. Cac nhu cau moi tap trung vao 5 nhom:

1. Quan ly hoc sinh: so lien lac, nhat ky cham soc, diem thi.
2. Quan ly giao vien: tinh luong dua tren cham cong khuon mat/lich day, giao viec, nhac viec, khoa SLA.
3. Voucher giam gia khoa hoc.
4. Tinh chinh hoc phi: cho phep sua hoc phi va ap voucher.
5. Muc BTVN: giao bai, nop bai, cham/nhan xet, theo doi trang thai.

Muc tieu BA cua tai lieu nay la xac dinh ro **Need, Change, Solution, Stakeholder, Value, Context** theo mo hinh BACCM, lam co so de viet BRD/SRS/User Story Map cho giai doan trien khai.

---

## 2. BACCM Overview

| BACCM Element | Phan tich |
|---|---|
| **Need - Nhu cau** | Trung tam can quan ly tap trung hoc sinh, giao vien, hoc phi, voucher, BTVN va cong viec noi bo. Hien tai cac nghiep vu nhu so lien lac, cham soc hoc sinh, diem thi, giao viec, tinh luong, SLA, ap voucher va chinh hoc phi chua duoc ho tro day du hoac con phu thuoc thao tac thu cong. |
| **Change - Su thay doi** | Mo rong web tu he thong quan ly khoa hoc/hoc phi co ban thanh nen tang van hanh dao tao toan dien, co lien ket du lieu giua hoc sinh, lop hoc, giao vien, hoc phi, voucher, BTVN va task noi bo. |
| **Solution - Giai phap** | Bo sung cac module: Quan ly hoc sinh mo rong, Quan ly giao vien mo rong, Voucher khoa hoc, Dieu chinh hoc phi, BTVN. Cac module can co phan quyen, audit log, thong bao, trang thai xu ly va lien ket voi du lieu san co. |
| **Stakeholder - Ben lien quan** | Admin, quan ly trung tam, giao vien, hoc sinh, phu huynh, nhan vien cham soc, tu van vien, ke toan, HR/nhan su. |
| **Value - Gia tri** | Giam thao tac thu cong, tang minh bach hoc phi va luong, cai thien viec cham soc hoc sinh, theo doi ket qua hoc tap, tang ti le hoan thanh BTVN, kiem soat deadline/SLA va nang cao hieu qua van hanh. |
| **Context - Boi canh** | He thong da co cau hinh hoc phi va cham cong khuon mat. Can phat trien tiep cac nghiep vu phat sinh trong qua trinh dao tao va van hanh hang ngay. |

---

## 3. Project Context

### 3.1. Current State

| Khu vuc | Hien trang |
|---|---|
| Hoc phi | Da co cau hinh hoc phi, nhung chua cho chinh sua hoc phi theo tung truong hop va chua ap voucher giam gia. |
| Cham cong giao vien | Da co cham cong khuon mat. |
| Quan ly hoc sinh | Can bo sung so lien lac, nhat ky cham soc va diem thi. |
| Quan ly giao vien | Can bo sung tinh luong, giao viec, nhac viec va SLA. |
| BTVN | Chua co muc rieng de giao, nop, cham va theo doi bai tap ve nha. |
| Voucher | Chua co module voucher giam gia khoa hoc. |

### 3.2. Target State

| Khu vuc | Trang thai mong muon |
|---|---|
| Hoc sinh | Moi hoc sinh co ho so hoc tap gom so lien lac, lich su cham soc, diem thi va BTVN. |
| Giao vien | Giao vien co du lieu cham cong, lich day, task, nhac viec, SLA va bang luong. |
| Hoc phi | Hoc phi co the duoc dieu chinh co kiem soat, ap voucher hop le va luu lich su thay doi. |
| Voucher | Voucher duoc cau hinh theo khoa hoc/dieu kien thoi gian/so lan su dung va duoc ap vao hoc phi. |
| BTVN | Giao vien giao bai, hoc sinh nop bai, he thong theo doi deadline va trang thai cham bai. |

---

## 4. Stakeholder Analysis

| Stakeholder | Nhu cau | Pain Point | Mong doi |
|---|---|---|---|
| Admin | Quan ly cau hinh, phan quyen va du lieu he thong. | Kho kiem soat thay doi neu khong co audit log. | Co quyen cau hinh module, voucher, hoc phi, SLA. |
| Quan ly trung tam | Theo doi van hanh hoc sinh, giao vien, cong viec va doanh thu. | Du lieu phan tan, kho danh gia hieu qua. | Dashboard/trang tong hop ve hoc phi, cham soc, task, SLA, luong. |
| Giao vien | Quan ly lop, diem thi, BTVN, lich day va cong viec duoc giao. | Phai ghi diem/BTVN/nhan xet thu cong. | Nhap diem, giao BTVN, nhan nhac viec, xem bang luong. |
| Hoc sinh | Theo doi hoc phi, diem thi, BTVN va thong bao. | Khong co mot noi tap trung de xem bai tap/diem/thong bao. | Xem va nop BTVN, xem diem, nhan thong bao. |
| Phu huynh | Theo doi qua trinh hoc va thong tin lien lac. | Phu thuoc tin nhan/trao doi ngoai he thong. | Xem so lien lac, diem thi, BTVN, nhan xet/cham soc. |
| Nhan vien cham soc | Ghi nhan lich su cham soc va follow-up. | De quen lich hen, mat lich su tuong tac. | Tao nhat ky cham soc, nhac follow-up, theo doi trang thai. |
| Ke toan | Quan ly hoc phi, voucher, dieu chinh phi, bang luong. | Tinh tien/giam gia/luong thu cong de sai sot. | Tinh dung hoc phi sau voucher, luu lich su dieu chinh, tinh luong minh bach. |
| HR/Nhan su | Theo doi cong viec, cham cong, SLA va luong giao vien/nhan vien. | Kho tong hop du lieu tu nhieu nguon. | Co du lieu cham cong, task, SLA va bang luong tap trung. |

---

## 5. Scope By Module

## 5.1. Quan ly hoc sinh

### 5.1.1. So lien lac

| Muc | Noi dung |
|---|---|
| Muc tieu | Ghi nhan trao doi giua trung tam, giao vien, hoc sinh va phu huynh. |
| Actor chinh | Giao vien, CS, phu huynh, hoc sinh, quan ly. |
| Input | Hoc sinh, lop/khoa hoc, noi dung lien lac, nguoi tao, file dinh kem neu co. |
| Output | Ban ghi so lien lac, lich su trao doi, thong bao cho nguoi lien quan. |
| Gia tri | Minh bach trao doi, de tra cuu lich su hoc tap/cham soc. |

### 5.1.2. Nhat ky cham soc

| Muc | Noi dung |
|---|---|
| Muc tieu | Theo doi qua trinh cham soc hoc sinh/khach hang theo tung lan tuong tac. |
| Actor chinh | CS, tu van vien, quan ly. |
| Input | Hoc sinh/lead, loai tuong tac, noi dung cham soc, ket qua, lich hen tiep theo, nguoi phu trach. |
| Output | Lich su cham soc, task follow-up, trang thai xu ly. |
| Gia tri | Khong mat thong tin, giam bo sot follow-up, nang cao chat luong cham soc. |

### 5.1.3. Diem thi

| Muc | Noi dung |
|---|---|
| Muc tieu | Quan ly ket qua hoc tap theo hoc sinh/lop/khoa/bai thi. |
| Actor chinh | Giao vien, hoc sinh, phu huynh, quan ly dao tao. |
| Input | Bai thi, diem, thang diem, nhan xet, nguoi nhap, ngay nhap. |
| Output | Bang diem, lich su sua diem, thong bao diem neu can. |
| Gia tri | Theo doi tien bo hoc tap va lam co so danh gia chat luong dao tao. |

## 5.2. Quan ly giao vien

### 5.2.1. Tinh luong

| Muc | Noi dung |
|---|---|
| Muc tieu | Tinh luong giao vien dua tren du lieu cham cong khuon mat, lich day, buoi day va cau hinh luong. |
| Actor chinh | Ke toan, HR, quan ly, giao vien. |
| Input | Du lieu cham cong, lich day, don gia/buoi/gio, phu cap, khau tru, KPI neu co. |
| Output | Bang luong nhap, bang luong da duyet, lich su dieu chinh luong. |
| Gia tri | Giam sai sot tinh luong, minh bach thu nhap, tiet kiem thoi gian ke toan. |

### 5.2.2. Giao viec va nhac viec

| Muc | Noi dung |
|---|---|
| Muc tieu | Giao va theo doi cong viec cho giao vien/nhan su. |
| Actor chinh | Quan ly, giao vien, nhan vien noi bo. |
| Input | Ten viec, mo ta, nguoi nhan, deadline, uu tien, tep dinh kem, lien ket hoc sinh/lop neu co. |
| Output | Task, trang thai task, thong bao nhac viec, lich su cap nhat. |
| Gia tri | Tang trach nhiem, giam quen viec, theo doi tien do ro rang. |

### 5.2.3. Khoa SLA

| Muc | Noi dung |
|---|---|
| Muc tieu | Kiem soat thoi han xu ly task/cham soc/cong viec noi bo. |
| Actor chinh | Quan ly, CS, giao vien, nhan vien. |
| Input | Loai viec, SLA, deadline, trang thai, nguoi phu trach. |
| Output | Canh bao sap qua han, vi pham SLA, khoa thao tac neu rule yeu cau. |
| Gia tri | Nang cao chat luong dich vu va tinh ky luat van hanh. |

## 5.3. Voucher giam gia khoa hoc

| Muc | Noi dung |
|---|---|
| Muc tieu | Tao va ap dung chinh sach giam gia linh hoat cho khoa hoc. |
| Actor chinh | Marketing, tu van vien, ke toan, quan ly. |
| Input | Ma voucher, ten voucher, loai giam gia, gia tri giam, khoa hoc ap dung, ngay hieu luc, so lan su dung. |
| Output | Voucher hop le, lich su ap dung voucher, so tien duoc giam. |
| Gia tri | Tang chuyen doi ban khoa hoc va minh bach uu dai. |

## 5.4. Tinh chinh hoc phi

| Muc | Noi dung |
|---|---|
| Muc tieu | Cho phep chinh sua hoc phi da cau hinh theo tung hoc sinh/khoa/lop co kiem soat. |
| Actor chinh | Ke toan, tu van vien, quan ly, admin. |
| Input | Hoc phi goc, so tien dieu chinh, voucher, ly do chinh sua, nguoi thuc hien. |
| Output | Hoc phi sau dieu chinh, so tien giam, so tien con lai, audit log. |
| Gia tri | Linh hoat thuong mai nhung van dam bao kiem soat va truy vet. |

## 5.5. Muc BTVN

| Muc | Noi dung |
|---|---|
| Muc tieu | Quan ly bai tap ve nha theo lop, buoi hoc, giao vien va hoc sinh. |
| Actor chinh | Giao vien, hoc sinh, phu huynh, quan ly dao tao. |
| Input | Tieu de BTVN, noi dung, lop/hoc sinh, deadline, file/link, diem/nhan xet. |
| Output | BTVN duoc giao, bai nop, trang thai nop bai, diem/nhan xet. |
| Gia tri | Tang tuong tac hoc tap ngoai gio va theo doi muc do hoan thanh bai tap. |

---

## 6. Business Requirements

## 6.1. Quan ly hoc sinh

| ID | Business Requirement | Uu tien | Stakeholder |
|---|---|---|---|
| BRQ-STU-001 | He thong phai cho phep tao so lien lac cho tung hoc sinh theo lop hoac khoa hoc. | Must | Giao vien, CS, phu huynh |
| BRQ-STU-002 | He thong phai cho phep xem lich su so lien lac theo hoc sinh. | Must | Giao vien, phu huynh, quan ly |
| BRQ-STU-003 | He thong phai luu nhat ky cham soc hoc sinh kem nguoi phu trach, ket qua xu ly va lich hen tiep theo. | Must | CS, tu van vien, quan ly |
| BRQ-STU-004 | He thong phai cho phep giao vien nhap diem thi theo hoc sinh, lop va bai thi. | Must | Giao vien, quan ly dao tao |
| BRQ-STU-005 | He thong phai luu lich su chinh sua diem thi gom nguoi sua, thoi gian sua va ly do sua. | Should | Quan ly dao tao |

## 6.2. Quan ly giao vien

| ID | Business Requirement | Uu tien | Stakeholder |
|---|---|---|---|
| BRQ-TEA-001 | He thong phai tinh luong giao vien dua tren cau hinh luong, du lieu cham cong khuon mat va lich day. | Must | Ke toan, HR, giao vien |
| BRQ-TEA-002 | He thong phai cho phep quan ly tao va giao viec cho giao vien hoac nhan su noi bo. | Must | Quan ly, giao vien |
| BRQ-TEA-003 | He thong phai gui nhac viec truoc deadline va khi cong viec qua han. | Should | Quan ly, giao vien, nhan vien |
| BRQ-TEA-004 | He thong phai ap dung SLA theo loai cong viec va ghi nhan vi pham SLA. | Should | Quan ly, CS, giao vien |
| BRQ-TEA-005 | He thong phai cho phep quan ly/ke toan duyet bang luong truoc khi khoa ky luong. | Must | Ke toan, quan ly |

## 6.3. Voucher khoa hoc

| ID | Business Requirement | Uu tien | Stakeholder |
|---|---|---|---|
| BRQ-VOU-001 | He thong phai cho phep tao voucher giam gia khoa hoc. | Must | Marketing, quan ly |
| BRQ-VOU-002 | He thong phai kiem tra dieu kien voucher truoc khi ap dung vao hoc phi. | Must | Ke toan, tu van vien |
| BRQ-VOU-003 | He thong phai gioi han so lan su dung voucher theo cau hinh. | Must | Marketing, ke toan |
| BRQ-VOU-004 | He thong phai luu lich su ap dung voucher theo hoc sinh, khoa hoc va hoc phi. | Must | Ke toan, quan ly |

## 6.4. Tinh chinh hoc phi

| ID | Business Requirement | Uu tien | Stakeholder |
|---|---|---|---|
| BRQ-FEE-001 | He thong phai cho phep nguoi co quyen chinh sua hoc phi da cau hinh. | Must | Ke toan, quan ly |
| BRQ-FEE-002 | He thong phai yeu cau nhap ly do khi chinh sua hoc phi. | Must | Ke toan, quan ly |
| BRQ-FEE-003 | He thong phai cho phep ap voucher hop le vao hoc phi. | Must | Ke toan, tu van vien |
| BRQ-FEE-004 | He thong phai tu dong tinh hoc phi sau giam gia va so tien con lai can thanh toan. | Must | Ke toan, hoc sinh/phu huynh |
| BRQ-FEE-005 | He thong phai luu audit log cho moi lan thay doi hoc phi va ap voucher. | Must | Admin, quan ly, ke toan |

## 6.5. BTVN

| ID | Business Requirement | Uu tien | Stakeholder |
|---|---|---|---|
| BRQ-HW-001 | He thong phai cho phep giao vien tao BTVN cho lop, nhom hoc sinh hoac hoc sinh cu the. | Must | Giao vien |
| BRQ-HW-002 | He thong phai cho phep hoc sinh nop BTVN truoc deadline. | Must | Hoc sinh, giao vien |
| BRQ-HW-003 | He thong phai hien thi trang thai BTVN gom chua nop, da nop, nop muon va da cham. | Must | Giao vien, hoc sinh, phu huynh |
| BRQ-HW-004 | He thong phai cho phep giao vien nhan xet hoac cham diem BTVN. | Should | Giao vien, hoc sinh |
| BRQ-HW-005 | He thong phai nhac hoc sinh/phu huynh khi BTVN sap den han hoac qua han. | Should | Hoc sinh, phu huynh |

---

## 7. Business Rules

| ID | Rule | Applies to |
|---|---|---|
| BR-RULE-001 | Chi nguoi co quyen moi duoc tao, sua hoac xoa voucher. | Voucher |
| BR-RULE-002 | Voucher chi duoc ap dung khi con hieu luc va chua vuot gioi han su dung. | Voucher, Hoc phi |
| BR-RULE-003 | Moi lan chinh sua hoc phi bat buoc co ly do va duoc luu audit log. | Hoc phi |
| BR-RULE-004 | Neu hoc phi da duoc khoa/chot, chi Admin hoac Quan ly moi co quyen mo khoa de sua. | Hoc phi |
| BR-RULE-005 | Bang luong sau khi duyet/khoa khong duoc sua truc tiep neu khong co thao tac mo khoa co quyen. | Tinh luong |
| BR-RULE-006 | Task qua SLA phai duoc danh dau vi pham SLA va thong bao cho nguoi phu trach/quan ly. | Giao viec, SLA |
| BR-RULE-007 | Diem thi sau khi cong bo neu sua phai co ly do va luu lich su. | Diem thi |
| BR-RULE-008 | BTVN nop sau deadline phai duoc gan trang thai nop muon. | BTVN |
| BR-RULE-009 | Nhat ky cham soc khong duoc xoa vat ly; neu can, chi duoc an/vo hieu hoa theo quyen quan ly. | Nhat ky cham soc |
| BR-RULE-010 | So lien lac gui cho phu huynh/hoc sinh phai luu nguoi tao, thoi gian tao va doi tuong nhan. | So lien lac |

---

## 8. MoSCoW Priority

| Priority | Tinh nang |
|---|---|
| **Must** | Chinh sua hoc phi, ap voucher vao hoc phi, voucher khoa hoc, nhat ky cham soc, BTVN co ban, nhap diem thi, tinh luong co ban. |
| **Should** | So lien lac, nhac viec, giao viec, nhan xet/cham BTVN, lich su sua diem, duyet/khoa bang luong. |
| **Could** | Khoa SLA tu dong, dashboard SLA, dashboard luong, thong bao phu huynh nang cao, bao cao tien do BTVN. |
| **Won't v1** | Workflow phe duyet nhieu cap phuc tap, cong thuc luong qua nang cao, tich hop thanh toan/voucher voi ben thu ba, AI cham bai/nhan xet tu dong. |

---

## 9. Functional Decomposition

| Module | Feature ID | Feature | Business Requirement |
|---|---|---|---|
| Quan ly hoc sinh | F-STU-001 | So lien lac | BRQ-STU-001, BRQ-STU-002 |
| Quan ly hoc sinh | F-STU-002 | Nhat ky cham soc | BRQ-STU-003 |
| Quan ly hoc sinh | F-STU-003 | Diem thi | BRQ-STU-004, BRQ-STU-005 |
| Quan ly giao vien | F-TEA-001 | Tinh luong giao vien | BRQ-TEA-001, BRQ-TEA-005 |
| Quan ly giao vien | F-TEA-002 | Giao viec | BRQ-TEA-002 |
| Quan ly giao vien | F-TEA-003 | Nhac viec va SLA | BRQ-TEA-003, BRQ-TEA-004 |
| Voucher | F-VOU-001 | Quan ly voucher khoa hoc | BRQ-VOU-001, BRQ-VOU-002, BRQ-VOU-003, BRQ-VOU-004 |
| Hoc phi | F-FEE-001 | Chinh sua hoc phi | BRQ-FEE-001, BRQ-FEE-002, BRQ-FEE-005 |
| Hoc phi | F-FEE-002 | Ap voucher vao hoc phi | BRQ-FEE-003, BRQ-FEE-004, BRQ-FEE-005 |
| BTVN | F-HW-001 | Giao va theo doi BTVN | BRQ-HW-001, BRQ-HW-002, BRQ-HW-003, BRQ-HW-004, BRQ-HW-005 |

---

## 10. Suggested User Stories

| Story ID | User Story | Priority | Linked BRQ |
|---|---|---|---|
| US-STU-001 | As a teacher, I want to create communication notes for a student so that parents and the center can track learning-related updates. | Must | BRQ-STU-001 |
| US-STU-002 | As a CS staff, I want to log care activities for a student so that follow-up history is not lost. | Must | BRQ-STU-003 |
| US-STU-003 | As a teacher, I want to enter exam scores for students so that learning outcomes are tracked by class and course. | Must | BRQ-STU-004 |
| US-TEA-001 | As an accountant, I want to calculate teacher salary from attendance and teaching schedule so that payroll is accurate. | Must | BRQ-TEA-001 |
| US-TEA-002 | As a manager, I want to assign tasks to teachers or staff so that work ownership and deadline are clear. | Must | BRQ-TEA-002 |
| US-TEA-003 | As a manager, I want the system to remind overdue tasks so that SLA violations are reduced. | Should | BRQ-TEA-003, BRQ-TEA-004 |
| US-VOU-001 | As a marketing user, I want to create course vouchers so that the center can run discount campaigns. | Must | BRQ-VOU-001 |
| US-FEE-001 | As an accountant, I want to edit tuition with a reason so that special tuition cases are handled with audit trail. | Must | BRQ-FEE-001, BRQ-FEE-002 |
| US-FEE-002 | As an accountant, I want to apply a valid voucher to tuition so that the payable amount is calculated correctly. | Must | BRQ-FEE-003, BRQ-FEE-004 |
| US-HW-001 | As a teacher, I want to assign homework to a class so that students know what to complete before the deadline. | Must | BRQ-HW-001 |
| US-HW-002 | As a student, I want to submit homework online so that the teacher can review my work. | Must | BRQ-HW-002 |

---

## 11. High-Level Data Entities

| Entity | Mo ta | Lien quan |
|---|---|---|
| Student | Thong tin hoc sinh. | So lien lac, cham soc, diem thi, hoc phi, BTVN |
| Parent | Thong tin phu huynh/nguoi lien he. | So lien lac, thong bao, BTVN |
| Teacher | Thong tin giao vien. | Cham cong, lich day, luong, task, BTVN, diem thi |
| Course | Khoa hoc. | Voucher, hoc phi, lop hoc |
| Class | Lop hoc. | Hoc sinh, giao vien, diem thi, BTVN |
| TuitionFee | Hoc phi cua hoc sinh/khoa/lop. | Dieu chinh hoc phi, voucher, thanh toan |
| Voucher | Ma giam gia khoa hoc. | Hoc phi, khoa hoc, hoc sinh |
| VoucherUsage | Lich su ap dung voucher. | Voucher, hoc phi, hoc sinh |
| CareLog | Nhat ky cham soc. | Student, CS staff, task follow-up |
| CommunicationBook | So lien lac. | Student, parent, teacher, class |
| Exam | Bai thi/ky thi. | Diem thi, lop, khoa |
| ExamScore | Diem thi cua hoc sinh. | Student, exam, teacher |
| Homework | BTVN duoc giao. | Class, teacher, deadline |
| HomeworkSubmission | Bai nop cua hoc sinh. | Student, homework, score/comment |
| Task | Cong viec noi bo. | Teacher/staff, reminder, SLA |
| SLAConfig | Cau hinh SLA theo loai viec. | Task, care log |
| Payroll | Bang luong. | Teacher, attendance, teaching schedule |
| PayrollAdjustment | Dieu chinh luong. | Payroll, accountant, manager |

---

## 12. NFR Considerations

| ID | Non-functional Area | Requirement |
|---|---|---|
| NFR-001 | Security | He thong phai phan quyen theo vai tro: Admin, Quan ly, Giao vien, CS, Ke toan, Hoc sinh, Phu huynh. |
| NFR-002 | Auditability | Cac thao tac nhay cam nhu sua hoc phi, ap voucher, sua diem, khoa luong phai co audit log. |
| NFR-003 | Notification | He thong phai ho tro thong bao cho nhac viec, BTVN sap qua han, cham soc follow-up va SLA. |
| NFR-004 | Data Integrity | Voucher, hoc phi, bang luong va diem thi phai dam bao tinh nhat quan khi chinh sua. |
| NFR-005 | Performance | Cac man hinh danh sach hoc sinh, task, hoc phi va BTVN phai co loc/tim kiem de dung duoc khi du lieu tang. |
| NFR-006 | Privacy | Thong tin hoc sinh, phu huynh, diem thi, hoc phi va luong giao vien phai chi hien thi cho nguoi co quyen. |

---

## 13. Assumptions

| ID | Gia dinh | Impact neu sai |
|---|---|---|
| ASM-001 | He thong da co du lieu hoc sinh, giao vien, khoa hoc, lop hoc va hoc phi co ban. | Can bo sung data foundation truoc khi lam feature. |
| ASM-002 | Cham cong khuon mat da co du lieu co the truy xuat cho tinh luong. | Module tinh luong se can integration bo sung. |
| ASM-003 | Voucher ap dung vao hoc phi theo tung hoc sinh hoac hoa don hoc phi. | Can thay doi thiet ke neu voucher ap theo nhom/lop/khoa. |
| ASM-004 | Chinh sua hoc phi can audit log va phan quyen, chua mac dinh can workflow duyet nhieu cap. | Neu can duyet nhieu cap, scope se tang. |
| ASM-005 | BTVN co the bat dau voi noi dung text/file/link, chua can cham bai tu dong. | Neu can cham tu dong, can module AI/rubric rieng. |
| ASM-006 | SLA ap dung cho task va cham soc, chua ro khoa thao tac hay chi canh bao. | Can chot rule truoc khi implement. |

---

## 14. Open Questions

| ID | Cau hoi | Owner de chot | Can truoc |
|---|---|---|---|
| OQ-001 | Voucher ap dung theo khoa hoc, lop, hoc sinh hay tung hoa don/hoc phi? | Product + Ke toan | SRS voucher |
| OQ-002 | Co cho ap nhieu voucher tren mot hoc phi khong? | Product + Ke toan | Business rules hoc phi |
| OQ-003 | Chinh sua hoc phi co can phe duyet truoc khi co hieu luc khong? | Quan ly + Ke toan | Sprint planning |
| OQ-004 | Cong thuc luong giao vien tinh theo gio day, buoi day, doanh thu lop, KPI hay ket hop? | HR + Ke toan | SRS tinh luong |
| OQ-005 | Du lieu cham cong khuon mat hien co gom nhung truong nao va co map voi lich day khong? | Engineering + HR | Thiet ke payroll |
| OQ-006 | SLA se khoa thao tac that hay chi canh bao/ghi nhan vi pham? | Quan ly van hanh | SRS task/SLA |
| OQ-007 | BTVN hoc sinh nop tren web bang file, link, text hay tat ca? | Dao tao + Giao vien | SRS BTVN |
| OQ-008 | Phu huynh co tai khoan rieng de xem so lien lac/diem/BTVN khong? | Product | UX scope |
| OQ-009 | Diem thi co can cong bo cho hoc sinh/phu huynh hay chi noi bo? | Dao tao | Business rules diem |
| OQ-010 | Nhat ky cham soc co can tao task follow-up tu dong khong? | CS manager | Task integration |

---

## 15. Risks

| ID | Risk | Probability | Impact | Mitigation |
|---|---|---:|---:|---|
| RSK-001 | Scope qua rong neu lam tat ca module cung luc. | Cao | Cao | Chia MVP theo Must/Should, uu tien hoc phi/voucher/BTVN/cham soc. |
| RSK-002 | Cong thuc tinh luong phuc tap va thay doi theo tung giao vien. | Trung binh | Cao | Lam cau hinh cong thuc co ban truoc, them adjustment/audit log. |
| RSK-003 | Voucher va chinh hoc phi co the gay sai lech doanh thu neu thieu audit. | Trung binh | Cao | Bat buoc permission, audit log, history before/after. |
| RSK-004 | SLA khoa thao tac co the lam gian doan van hanh neu rule chua chuan. | Trung binh | Trung binh | Bat dau bang warning/escalation truoc khi khoa cung. |
| RSK-005 | Phu huynh/hoc sinh khong dung portal neu thong bao khong ro. | Trung binh | Trung binh | Thiet ke notification va trang xem don gian. |

---

## 16. Suggested MVP Release Plan

| Phase | Scope | Muc tieu |
|---|---|---|
| Phase 1 - Core finance & learning | Voucher, ap voucher vao hoc phi, chinh sua hoc phi, BTVN co ban, nhap diem thi. | Giai quyet pain point hoc phi va hoc tap truc tiep. |
| Phase 2 - Care & operations | Nhat ky cham soc, so lien lac, giao viec, nhac viec. | Tang nang luc cham soc va van hanh hang ngay. |
| Phase 3 - Payroll & SLA | Tinh luong tu cham cong/lich day, duyet bang luong, SLA warning/khoa. | Kiem soat nhan su, chi phi va chat luong xu ly. |

---

## 17. RTM Draft

| BRQ | Feature | User Story |
|---|---|---|
| BRQ-STU-001, BRQ-STU-002 | F-STU-001 | US-STU-001 |
| BRQ-STU-003 | F-STU-002 | US-STU-002 |
| BRQ-STU-004, BRQ-STU-005 | F-STU-003 | US-STU-003 |
| BRQ-TEA-001, BRQ-TEA-005 | F-TEA-001 | US-TEA-001 |
| BRQ-TEA-002 | F-TEA-002 | US-TEA-002 |
| BRQ-TEA-003, BRQ-TEA-004 | F-TEA-003 | US-TEA-003 |
| BRQ-VOU-001, BRQ-VOU-002, BRQ-VOU-003, BRQ-VOU-004 | F-VOU-001 | US-VOU-001 |
| BRQ-FEE-001, BRQ-FEE-002, BRQ-FEE-005 | F-FEE-001 | US-FEE-001 |
| BRQ-FEE-003, BRQ-FEE-004, BRQ-FEE-005 | F-FEE-002 | US-FEE-002 |
| BRQ-HW-001, BRQ-HW-002, BRQ-HW-003, BRQ-HW-004, BRQ-HW-005 | F-HW-001 | US-HW-001, US-HW-002 |

