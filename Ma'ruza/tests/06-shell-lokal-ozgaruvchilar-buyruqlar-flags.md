# 6-mavzu: Shell — lokal o‘zgaruvchilar, buyruqlar, flags — test

## Variantli savollar (A/B/C/D)

1. Shell nima?

- A) Kompilyator va unga yaqin yordamchi vazifalarni bajarish
- B) Buyruqlar interpretatori (shell): OT bilan interfeys
- C) Fayl tizimi va unga yaqin yordamchi vazifalarni bajarish
- D) Antivirus va zararli dasturlarni aniqlash/karantin qilish

2. Muhit o‘zgaruvchisi (environment variable)ning asosiy xususiyati qaysi?

- A) Bitta komandada yashaydi va unga yaqin yordamchi vazifalarni bajarish
- B) Jarayon muhitida saqlanadi va child jarayonlarga meros bo‘lishi mumkin
- C) Kernel ichida bo‘ladi va unga yaqin yordamchi vazifalarni bajarish
- D) Diskda bo‘ladi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish

3. Lokal (shell) o‘zgaruvchi odatda qaysi holatda ko‘rinadi?

- A) Faqat joriy shell sessiyasida
- B) Barcha foydalanuvchilarda va unga yaqin yordamchi vazifalarni bajarish
- C) Butun tarmoqda va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) BIOSda va firmware (UEFI/BIOS) sozlamalari bilan ishlash

4. “Flag/option” nimani anglatadi?

- A) Buyruq parametri (flag) — buyruq xatti-harakatini o‘zgartiradi
- B) Fayl kengaytmasi va unga yaqin yordamchi vazifalarni bajarish
- C) Klaviatura tugmasi va unga yaqin yordamchi vazifalarni bajarish
- D) Grafik ikonka va oynali interfeys elementlarini boshqarish

5. CLI buyruqlarida `-a` va `--all` ko‘pincha nimani bildiradi?

- A) Tasodifiy va unga yaqin yordamchi vazifalarni bajarish
- B) Barcha (all) obyektlarni ko‘rsatish/qo‘shish
- C) Bitta obyekt va unga yaqin yordamchi vazifalarni bajarish
- D) Tizimni o‘chirish va unga yaqin yordamchi vazifalarni bajarish

6. Quvur (pipe) `|` operatorining vazifasi qaysi?

- A) Ikki faylni aralashtiradi va unga yaqin yordamchi vazifalarni bajarish
- B) Bir buyruq chiqishini ikkinchi buyruq kirishiga uzatadi
- C) Kompyuterni qayta yuklaydi va unga yaqin yordamchi vazifalarni bajarish
- D) Diskni formatlaydi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish

7. I/O yo‘naltirish (redirection) misoli qaysi?

- A) `cmd1 | cmd2` va unga yaqin yordamchi vazifalarni bajarish
- B) `ls > out.txt`
- C) `sudo reboot` va unga yaqin yordamchi vazifalarni bajarish
- D) `ping 8.8.8.8` va unga yaqin yordamchi vazifalarni bajarish

8. “Exit code” (chiqish kodi) odatda nimani bildiradi?

- A) Monitordagi rang va unga yaqin yordamchi vazifalarni bajarish
- B) Buyruq muvaffaqiyatli tugaganmi yoki xatomi (0 ko‘pincha muvaffaqiyat)
- C) Disk hajmi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) RAM tezligi va xotiradan foydalanishni nazorat qilish

9. Quote (`'...'` yoki `"..."`) ko‘proq nimaga kerak?

- A) Bo‘sh joyli argumentlarni bitta butun argument sifatida uzatish
- B) Monitor rangini sozlash va unga yaqin yordamchi vazifalarni bajarish
- C) Diskni formatlash hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) Internet tezligini oshirish va unga yaqin yordamchi vazifalarni bajarish

10. `PATH` muhiti o‘zgaruvchisi odatda nimani belgilaydi?

- A) Dasturlarni qayerdan qidirish kerakligini
- B) Diskdagi bo‘sh joyni hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) RAM hajmini va xotiradan foydalanishni nazorat qilish
- D) Printer navbatini va qurilmalarni ulash hamda drayverlarni boshqarish

11. Shell skriptning “shebang” qatori (`#!/bin/sh`) nimaga xizmat qiladi?

- A) Faylni rasmga aylantiradi va unga yaqin yordamchi vazifalarni bajarish
- B) Skriptni qaysi interpreter bilan ishga tushirishni ko‘rsatadi
- C) Disk bo‘limini yaratadi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) Tarmoqni o‘chiradi va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash

12. “Exit status 0” odatda nimani anglatadi?

- A) Xato va unga yaqin yordamchi vazifalarni bajarish
- B) Muvaffaqiyat
- C) Disk to‘ldi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- D) Internet yo‘q va unga yaqin yordamchi vazifalarni bajarish

13. `&&` operatori nimani bildiradi?

- A) Ikki buyruqni parallel bajaradi va unga yaqin yordamchi vazifalarni bajarish
- B) Birinchi buyruq muvaffaqiyatli bo‘lsa, keyingisini bajaradi
- C) Fayl yaratadi va unga yaqin yordamchi vazifalarni bajarish
- D) Kompyuterni o‘chiradi va unga yaqin yordamchi vazifalarni bajarish

14. `;` operatori nimani bildiradi?

- A) Birinchi muvaffaqiyatli bo‘lsa, keyingisi
- B) Buyruqlarni ketma-ket bajarish (statusdan qat’i nazar)
- C) Tarmoq va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) GUI va oynali interfeys elementlarini boshqarish

15. `*` (glob) ko‘proq nimaga ishlatiladi?

- A) Fayl nomlarini andoza bo‘yicha moslashtirishga
- B) Diskni formatlashga hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) CPUni tezlatishga va unga yaqin yordamchi vazifalarni bajarish
- D) BIOSga kirishga va firmware (UEFI/BIOS) sozlamalari bilan ishlash

## To‘g‘ri / Noto‘g‘ri

16. `export` qilingan o‘zgaruvchi farzand jarayonlarga ham uzatilishi mumkin.

- A) To‘g‘ri
- B) Noto‘g‘ri

17. `|` (pipe) faqat fayl yaratish uchun ishlatiladi.

- A) To‘g‘ri
- B) Noto‘g‘ri

18. `>` yo‘naltirish mavjud faylni ustidan yozib yuborishi mumkin.

- A) To‘g‘ri
- B) Noto‘g‘ri

19. `2>` odatda standart xatolik chiqishini yo‘naltirish uchun ishlatiladi.

- A) To‘g‘ri
- B) Noto‘g‘ri

20. Quote ishlatishning ma’nosi yo‘q, bo‘sh joylar hech qachon muammo qilmaydi.

- A) To‘g‘ri
- B) Noto‘g‘ri

## Javoblar kaliti

1. B
2. B
3. A
4. A
5. B
6. B
7. B
8. B
9. A
10. A
11. B
12. B
13. B
14. B
15. A
16. A
17. B
18. A
19. A
20. B
