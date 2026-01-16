# Telegram Bulk Quiz Bot

Bu bot sizdagi test `.txt` faylni qabul qiladi va avtomatik ravishda Telegram **quiz poll** savollarini chatga yuboradi.

Ishlash tartibi: **har safar faqat 1 ta savol** yuboradi. Keyingi savol faqat user javob bergandan keyin yoki **30 soniya** vaqt tugagandan so‘ng yuboriladi.

## 1) Bot yaratish

1. Telegram’da `@BotFather` → `/newbot`
2. Bot tokenni oling

## 2) O‘rnatish

```zsh
cd /home/azimov/Desktop/operatsion/telegram_bulk_quiz_bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3) Ishga tushirish

```zsh
cd /home/azimov/Desktop/operatsion
export BOT_TOKEN='PASTE_YOUR_TOKEN'
export TESTS_DIR="Ma'ruza/tests_txt"
python3 -m telegram_bulk_quiz_bot.bot
```

Eslatma: `telegram_bulk_quiz_bot/.env.example` faqat namuna. Xohlasangiz `cp telegram_bulk_quiz_bot/.env.example .env` qilib olib, tokenni yozing va keyin yuqoridagi `export` lar orqali ishga tushiring.

Alternativ (agar xohlasangiz):

```zsh
python3 telegram_bulk_quiz_bot/bot.py
```

Xavfsizlik: tokenni hech qachon kodga yozmang. Agar tokenni chatga yuborib qo‘ygan bo‘lsangiz, `@BotFather` orqali yangisini oling (rotate) va eskisini bekor qiling.

## 4) Foydalanish

- Botga `/start` bosing — menyu chiqadi
- Test tanlash: `/menu` (tugmalar orqali)
- Yoki komandalar:
  - `/list` — `TESTS_DIR` ichidagi testlar ro‘yxati
  - `/send 01` yoki `/send 01-operatsion-tizim-asosiy-tushunchalar` — shu testni boshlaydi
  - `/stop` — aktiv testni to‘xtatadi (keyin boshqa testni tanlaysiz)

Eslatma: bu bot **faqat** `TESTS_DIR` ichidagi tayyor testlar bilan ishlaydi.

Tavsiya: bot bilan **private chat**da ishlang (natija va xatolar DM’da qulay chiqadi).

## TXT format

Har savol:

- `? 1. Savol matni`
- `+ A) ...` (to‘g‘ri)
- `- B) ...` (noto‘g‘ri)

Eslatma: Telegram quiz poll bir savol = bitta xabar. Bot buni avtomatik ketma-ket yuboradi.

## Feedback (xatolarni ko‘rsatish)

Foydalanuvchi savolga javob berganda bot DM’da quyidagicha yozadi:

- "Natija: to‘g‘ri."
- yoki "Natija: noto‘g‘ri... To‘g‘ri: ..."

Test tugaganda bot yakuniy natijani ham yuboradi (masalan `18/20`) va xato savollar ro‘yxatini chiqaradi.
Bir testni xohlagancha qayta ishlash mumkin — `/menu` dan qayta tanlang.
