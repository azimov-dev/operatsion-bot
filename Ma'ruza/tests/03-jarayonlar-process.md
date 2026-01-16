# 3-mavzu: Operatsion tizimlarda jarayonlar (process) — test

## Variantli savollar (A/B/C/D)

1. Jarayon (process) nima?

- A) Dastur fayli (.exe) va unga yaqin yordamchi vazifalarni bajarish
- B) Bajarilayotgan dastur + uning holati va resurslari
- C) CPU registrlari va unga yaqin yordamchi vazifalarni bajarish
- D) RAM bo‘lagi va xotiradan foydalanishni nazorat qilish

2. PCB (Process Control Block) nimani saqlaydi?

- A) Tarmoq parolini va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- B) Jarayon holati, registrlar, rejalashtirish ma’lumoti, xotira ko‘rsatkichlari va h.k.
- C) Fayl nomlarini va unga yaqin yordamchi vazifalarni bajarish
- D) GPU sozlamalari va unga yaqin yordamchi vazifalarni bajarish

3. Jarayon holatlarining klassik to‘plamiga qaysilar kiradi?

- A) New, Ready, Running, Waiting/Blocked, Terminated
- B) Red, Green, Blue va unga yaqin yordamchi vazifalarni bajarish
- C) Start, Stop, Pause va unga yaqin yordamchi vazifalarni bajarish
- D) Zip, Rar, 7z va unga yaqin yordamchi vazifalarni bajarish

4. “Jarayon iyerarxiyasi” nimani anglatadi?

- A) Jarayonlar faqat bitta darajada bo‘ladi
- B) Ota (parent) va farzand (child) jarayonlar munosabati
- C) Disk kataloglari hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) Tarmoq topologiyasi va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash

5. “Stack” odatda nimaga ishlatiladi?

- A) Dinamik obyektlarni uzoq muddat saqlash
- B) Funksiya chaqiriqlari, lokal o‘zgaruvchilar, qaytish manzili
- C) Fayllarni doimiy saqlash va unga yaqin yordamchi vazifalarni bajarish
- D) Tarmoq paketlari navbati va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash

6. “Heap” odatda nimaga ishlatiladi?

- A) Dinamik xotira ajratish (malloc/new) uchun
- B) Registrlarni saqlash va unga yaqin yordamchi vazifalarni bajarish
- C) Interrupt vektorlar va unga yaqin yordamchi vazifalarni bajarish
- D) BIOS jadvali va firmware (UEFI/BIOS) sozlamalari bilan ishlash

7. “Kontekst almashish” jarayonida qaysi ish bajariladi?

- A) Monitor yorqinligi o‘zgaradi va unga yaqin yordamchi vazifalarni bajarish
- B) Joriy jarayon konteksti saqlanib, boshqa jarayon konteksti tiklanadi
- C) Internet tezligi o‘lchanadi va unga yaqin yordamchi vazifalarni bajarish
- D) Disk defragmentatsiya qilinadi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish

8. Jarayon yaratishning umumiy natijasi qaysi?

- A) Yangi jarayon uchun PCB va adres makoni (yoki ulashilgan) yaratiladi
- B) Yadro o‘chib qoladi va unga yaqin yordamchi vazifalarni bajarish
- C) RAM butunlay formatlanadi va xotiradan foydalanishni nazorat qilish
- D) CPU chastotasi doim oshadi va unga yaqin yordamchi vazifalarni bajarish

9. “Context” tarkibiga odatda nimalar kiradi?

- A) Registrlar, dastur hisoblagichi (PC), stek ko‘rsatkichlari va h.k.
- B) Klaviatura holati va unga yaqin yordamchi vazifalarni bajarish
- C) Brauzer kesh va unga yaqin yordamchi vazifalarni bajarish
- D) Disk sektori hamda diskdagi ma'lumotlarni tashkil etish/tekshirish

10. “Scheduler” jarayonlar bilan bog‘liq qaysi vazifani bajaradi?

- A) Jarayonlarni CPUda bajarish tartibini tanlash
- B) Fayllarni shifrlash va unga yaqin yordamchi vazifalarni bajarish
- C) Printer rangini sozlash va qurilmalarni ulash hamda drayverlarni boshqarish
- D) Monitor rejimini o‘zgartirish va unga yaqin yordamchi vazifalarni bajarish

11. “Zombie process” (zombi jarayon) odatda nimani anglatadi?

- A) Hali tugamagan jarayon va unga yaqin yordamchi vazifalarni bajarish
- B) Tugagan, lekin ota jarayon tomonidan statusi olinmagan jarayon
- C) Hech qachon yaratilmaydigan jarayon
- D) GUI jarayon va oynali interfeys elementlarini boshqarish

12. “Orphan process” (yetim jarayon) nimaga o‘xshaydi?

- A) Ota jarayoni tugab ketgan, child jarayon davom etayotgan holat
- B) Disk bo‘limi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Drayver va qurilmalarni ulash hamda drayverlarni boshqarish
- D) Internet sessiya va unga yaqin yordamchi vazifalarni bajarish

13. “Fork/exec” modeli nimani bildiradi?

- A) Yangi jarayon yaratish va keyin yangi dastur tasvirini yuklash
- B) Fayl ko‘chirish va unga yaqin yordamchi vazifalarni bajarish
- C) Tarmoq sozlash va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) BIOS yangilash va firmware (UEFI/BIOS) sozlamalari bilan ishlash

14. “Heap fragmentation” nima?

- A) Disk bo‘limi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- B) Dinamik xotira bo‘lak-bo‘lak bo‘lib, samarali ajratish qiyinlashishi
- C) CPU qizishi va unga yaqin yordamchi vazifalarni bajarish
- D) Tarmoq uzilishi va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash

15. “Process termination” (jarayon yakunlanishi) sababi bo‘lishi mumkin:

- A) Normal tugash yoki xato/kill signali
- B) Elektr uzilishi va unga yaqin yordamchi vazifalarni bajarish
- C) Disk to‘lishi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) Monitor o‘chishi va unga yaqin yordamchi vazifalarni bajarish

## To‘g‘ri / Noto‘g‘ri

16. Jarayon “Waiting/Blocked” holatda bo‘lsa, u CPUda bajarilmoqda.

- A) To‘g‘ri
- B) Noto‘g‘ri

17. Stack odatda LIFO tamoyiliga asoslanadi.

- A) To‘g‘ri
- B) Noto‘g‘ri

18. PCB jarayonni boshqarish uchun kerak bo‘lgan ma’lumotlarni saqlashi mumkin.

- A) To‘g‘ri
- B) Noto‘g‘ri

19. Heap odatda funksiyalar chaqirig‘i chuqurligi bilan bevosita bog‘liq.

- A) To‘g‘ri
- B) Noto‘g‘ri

20. Kontekst almashish juda arzon bo‘lib, hech qanday xarajatga ega emas.

- A) To‘g‘ri
- B) Noto‘g‘ri

## Javoblar kaliti

1. B
2. B
3. A
4. B
5. B
6. A
7. B
8. A
9. A
10. A
11. B
12. A
13. A
14. B
15. A
16. B
17. A
18. A
19. B
20. B
