# 14-mavzu: Sinxronizatsiya va uzilishlar (interrupts) — test

## Variantli savollar (A/B/C/D)

1. Sinxronizatsiya nimaga kerak?

- A) CPUni sovitish va unga yaqin yordamchi vazifalarni bajarish
- B) Bir nechta jarayon/oqimning resurslardan muvofiqlashgan holda foydalanishi
- C) Diskni bo‘lish hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) Internetni tezlatish va unga yaqin yordamchi vazifalarni bajarish

2. Uzilish (interrupt) nimani anglatadi?

- A) Monitor yorqinligi va unga yaqin yordamchi vazifalarni bajarish
- B) CPU e’tiborini boshqa hodisaga buruvchi signal (tashqi/ichki)
- C) Fayl kengaytmasi va unga yaqin yordamchi vazifalarni bajarish
- D) Printer rang sozlamasi va qurilmalarni ulash hamda drayverlarni boshqarish

3. “Maskable interrupt” nimasi bilan farq qiladi?

- A) Uni OS/CPU vaqtincha bloklashi (mask) mumkin
- B) Uni hech qachon bloklab bo‘lmaydi va unga yaqin yordamchi vazifalarni bajarish
- C) Diskga tegishli hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) GPUga tegishli va unga yaqin yordamchi vazifalarni bajarish

4. “Non-maskable interrupt (NMI)” odatda qachon ishlatiladi?

- A) Juda muhim xatolar/holatlar (masalan, apparat nosozligi) uchun
- B) Oddiy klaviatura bosishida va unga yaqin yordamchi vazifalarni bajarish
- C) Brauzer ochilganda va unga yaqin yordamchi vazifalarni bajarish
- D) Fayl ko‘chirilganda va unga yaqin yordamchi vazifalarni bajarish

5. Interrupt handling jarayonida “interrupt handler/ISR” nima qiladi?

- A) Veb sahifa ochadi va unga yaqin yordamchi vazifalarni bajarish
- B) Uzilish sababini qayta ishlaydi va kerakli xizmatni bajaradi
- C) Diskni formatlaydi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) CPUni o‘chiradi va unga yaqin yordamchi vazifalarni bajarish

6. Nega kritik kod bo‘lagida uzilishlarni vaqtincha o‘chirib qo‘yish (ba’zi tizimlarda) ishlatiladi?

- A) Grafikni chizish uchun va oynali interfeys elementlarini boshqarish
- B) Interrupt/preemption sababli umumiy ma’lumot buzilishini kamaytirish uchun
- C) Internet tezligi uchun va unga yaqin yordamchi vazifalarni bajarish
- D) Printer tezligi uchun va qurilmalarni ulash hamda drayverlarni boshqarish

7. “Barrier synchronization” nimani anglatadi?

- A) Oqimlar ma’lum nuqtada bir-birini kutib, keyin birgalikda davom etadi
- B) Disk bo‘limi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Tarmoq firewall va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) Fayl shifrlash va unga yaqin yordamchi vazifalarni bajarish

8. Uzilishlar schedulingga qanday ta’sir qiladi?

- A) Hech ta’sir qilmaydi va unga yaqin yordamchi vazifalarni bajarish
- B) ISR preemptionni tetiklab, kontekst almashishga olib kelishi mumkin
- C) Diskga ta’sir qiladi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) GUIga ta’sir qiladi va oynali interfeys elementlarini boshqarish

9. “Interrupt vector” nimaga xizmat qiladi?

- A) Uzilishlar uchun handler manzillarini/jadvalini ko‘rsatish
- B) Disk bo‘limi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Tarmoq protokoli va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) GUI element va oynali interfeys elementlarini boshqarish

10. “Interrupt latency” nimani anglatadi?

- A) Uzilish kelib, handler ishga tushguncha bo‘lgan kechikish
- B) Disk aylanishi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Internet ping va unga yaqin yordamchi vazifalarni bajarish
- D) Monitor kechikishi va unga yaqin yordamchi vazifalarni bajarish

11. “Critical section”da uzilishlarni o‘chirishning xavfi qaysi?

- A) Muhim hodisalar kechikishi va real vaqt talablariga zarar
- B) Disk hajmi oshishi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) RAM yo‘qolishi va xotiradan foydalanishni nazorat qilish
- D) Printer rang va qurilmalarni ulash hamda drayverlarni boshqarish

12. “Race condition” uzilishlar bilan qachon bog‘liq bo‘lishi mumkin?

- A) ISR va asosiy kod bir xil resursga sinxronizatsiyasiz murojaat qilsa
- B) Internet bo‘lsa va unga yaqin yordamchi vazifalarni bajarish
- C) Disk bo‘lsa hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) Hech qachon va unga yaqin yordamchi vazifalarni bajarish

13. “Interrupt storm” nimaga o‘xshaydi?

- A) Juda ko‘p uzilishlar kelib, CPU ko‘p vaqtini ISRga sarflashi
- B) Diskni formatlash hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) RAMni ko‘paytirish va xotiradan foydalanishni nazorat qilish
- D) Monitor o‘chishi va unga yaqin yordamchi vazifalarni bajarish

14. “Polling” uzilishlarga alternativ sifatida nimani anglatadi?

- A) Qurilma holatini davriy tekshirish
- B) Fayl siqish va unga yaqin yordamchi vazifalarni bajarish
- C) DNS sozlash va unga yaqin yordamchi vazifalarni bajarish
- D) GUI chizish va oynali interfeys elementlarini boshqarish

15. “Synchronization”ning to‘g‘ri natijasi qaysi?

- A) Umumiy ma’lumotlar yaxlitligi saqlanadi
- B) Disk bo‘limi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Internet uziladi va unga yaqin yordamchi vazifalarni bajarish
- D) Printer qotadi va qurilmalarni ulash hamda drayverlarni boshqarish

## To‘g‘ri / Noto‘g‘ri

16. Interruptlar yordamida K/Ch (I/O) hodisalari tugaganini OTga xabar qilish mumkin.

- A) To‘g‘ri
- B) Noto‘g‘ri

17. Sinxronizatsiya bo‘lmasa ham, umumiy ma’lumotlar doim to‘g‘ri qoladi.

- A) To‘g‘ri
- B) Noto‘g‘ri

18. Polling odatda CPUni ko‘proq band qilishi mumkin.

- A) To‘g‘ri
- B) Noto‘g‘ri

19. ISR (interrupt handler) odatda juda og‘ir va uzoq ishlashi tavsiya etiladi.

- A) To‘g‘ri
- B) Noto‘g‘ri

20. Interrupt latency real vaqt tizimlarida muhim ko‘rsatkich bo‘lishi mumkin.

- A) To‘g‘ri
- B) Noto‘g‘ri

## Javoblar kaliti

1. B
2. B
3. A
4. A
5. B
6. B
7. A
8. B
9. A
10. A
11. A
12. A
13. A
14. A
15. A
16. A
17. B
18. A
19. B
20. A
