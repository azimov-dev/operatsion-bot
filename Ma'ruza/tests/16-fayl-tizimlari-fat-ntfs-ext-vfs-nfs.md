# Mavzu: Fayl tizimlari (FAT/NTFS/ext), kataloglar, VFS/NFS — test

## Variantli savollar (A/B/C/D)

1. Fayl tizimi (file system)ning asosiy vazifasi qaysi?

- A) Internet tezligini oshirish va unga yaqin yordamchi vazifalarni bajarish
- B) Fayllarni/kataloglarni saqlash, nomlash va ularga kirishni boshqarish
- C) CPUni sovitish va unga yaqin yordamchi vazifalarni bajarish
- D) Monitor rangini sozlash va unga yaqin yordamchi vazifalarni bajarish

2. Katalog (directory) nima?

- A) Disk bo‘limi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- B) Fayllar va boshqa kataloglarga havolalar/yozuvlar saqlanadigan tuzilma
- C) Tarmoq protokoli va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) Printer navbati va qurilmalarni ulash hamda drayverlarni boshqarish

3. FAT (File Allocation Table) g‘oyasi nimaga tayangan?

- A) Fayl bloklari zanjirini jadval orqali kuzatish
- B) Shifrlash va unga yaqin yordamchi vazifalarni bajarish
- C) Siqish va unga yaqin yordamchi vazifalarni bajarish
- D) Internet va unga yaqin yordamchi vazifalarni bajarish

4. NTFSning mashhur xususiyatlaridan biri qaysi?

- A) Umuman ruxsatlar (permissions) yo‘q
- B) ACL, journaling va boy meta-ma’lumot imkoniyatlari
- C) RAMda ishlaydi va xotiradan foydalanishni nazorat qilish
- D) Bitta fayl va unga yaqin yordamchi vazifalarni bajarish

5. ext3/ext4da journaling nimaga xizmat qiladi?

- A) Diskni tezlashtirish uchun faqat kesh hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- B) Elektr uzilishi/xato bo‘lganda tiklanishni osonlashtirish
- C) Tarmoq paketlarini filtrlash va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) GPUni boshqarish va unga yaqin yordamchi vazifalarni bajarish

6. “Inode” tushunchasi ko‘proq qaysi oilaga xos?

- A) Unix-like (ext\*) fayl tizimlari
- B) FAT va unga yaqin yordamchi vazifalarni bajarish
- C) URL va unga yaqin yordamchi vazifalarni bajarish
- D) BIOS va firmware (UEFI/BIOS) sozlamalari bilan ishlash

7. VFS (Virtual File System)ning vazifasi qaysi?

- A) Bitta fayl tizimini majburlash va unga yaqin yordamchi vazifalarni bajarish
- B) Turli fayl tizimlari uchun yagona abstraksiya/interfeys berish
- C) Video format va unga yaqin yordamchi vazifalarni bajarish
- D) Printer va qurilmalarni ulash hamda drayverlarni boshqarish

8. NFS (Network File System) nimani ta’minlaydi?

- A) Tarmoq orqali masofaviy fayl tizimini ulash (mount) va ishlatish
- B) CPU scheduling va unga yaqin yordamchi vazifalarni bajarish
- C) RAID parity va unga yaqin yordamchi vazifalarni bajarish
- D) BIOS yangilash va firmware (UEFI/BIOS) sozlamalari bilan ishlash

9. “Mount” (ulash) nimani anglatadi?

- A) Fayl tizimini katalog daraxtiga bog‘lash
- B) Diskni formatlash hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Internetni tezlatish va unga yaqin yordamchi vazifalarni bajarish
- D) CPUni sovitish va unga yaqin yordamchi vazifalarni bajarish

10. “File metadata” nimani o‘z ichiga olishi mumkin?

- A) Egasi, ruxsatlar, vaqtlar (mtime/ctime), o‘lcham
- B) Videokarta modeli va unga yaqin yordamchi vazifalarni bajarish
- C) IP manzil va unga yaqin yordamchi vazifalarni bajarish
- D) BIOS versiya va firmware (UEFI/BIOS) sozlamalari bilan ishlash

11. Journaling fayl tizimida jurnal nimaga yordam beradi?

- A) Nosozlikdan keyin fayl tizimini tezroq izchil holatga keltirish
- B) Diskni kichraytirish hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Internetni uzish va unga yaqin yordamchi vazifalarni bajarish
- D) Printer rangini oshirish va qurilmalarni ulash hamda drayverlarni boshqarish

12. “Permissions” (ruxsatlar) nimani boshqaradi?

- A) Kim o‘qishi/yozishi/bajarishi mumkinligini
- B) Monitor yorqinligini va unga yaqin yordamchi vazifalarni bajarish
- C) Tarmoq ping va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) RAM tezligi va xotiradan foydalanishni nazorat qilish

13. “Hard link” nimaga yaqin?

- A) Bir inodega bir nechta nom (directory entry) ishora qilishi
- B) URL va unga yaqin yordamchi vazifalarni bajarish
- C) RAID va unga yaqin yordamchi vazifalarni bajarish
- D) BIOS va firmware (UEFI/BIOS) sozlamalari bilan ishlash

14. “Symbolic link” nimaga yaqin?

- A) Boshqa fayl yo‘liga ishora qiluvchi maxsus fayl
- B) Disk bo‘limi hamda diskdagi ma'lumotlarni tashkil etish/tekshirish
- C) Tarmoq kartasi va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash
- D) Printer navbati va qurilmalarni ulash hamda drayverlarni boshqarish

15. “Fragmentation” fayl tizimida nimaga olib kelishi mumkin?

- A) Fayl bloklari tarqalib ketib, o‘qish samaradorligi pasayishi
- B) Internet tezligi oshishi va unga yaqin yordamchi vazifalarni bajarish
- C) RAM ko‘payishi va xotiradan foydalanishni nazorat qilish
- D) Monitor tiniqligi va unga yaqin yordamchi vazifalarni bajarish

## To‘g‘ri / Noto‘g‘ri

16. Fayl tizimi faylni disk bloklariga qanday joylashishini (allocation) boshqaradi.

- A) To‘g‘ri
- B) Noto‘g‘ri

17. VFS bo‘lmasa ham, OT bir vaqtning o‘zida bir nechta turli fayl tizimlarini qo‘llay olmaydi.

- A) To‘g‘ri
- B) Noto‘g‘ri

18. NFS orqali masofaviy fayl tizimi lokaldek ko‘rinishi mumkin.

- A) To‘g‘ri
- B) Noto‘g‘ri

19. Permissions faylga kim kirishini cheklay oladi.

- A) To‘g‘ri
- B) Noto‘g‘ri

20. Hard link boshqa disk/partitionlar orasida ham doim ishlayveradi.

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
11. A
12. A
13. A
14. A
15. A
16. A
17. B
18. A
19. A
20. B
