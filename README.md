# Telegram Userbot (Pyrogram) — AFK / Auto-javob rejimi

Bu oddiy Bot API bot emas — bu **sizning shaxsiy Telegram akkountingiz**
orqali ishlaydigan userbot. U sizning nomingizdan xabar yozadi, shu sababli
ehtiyot bo'lib ishlating (pastdagi "Diqqat" bo'limini o'qing).

## 1. API_ID va API_HASH olish

1. https://my.telegram.org ga kiring, telefon raqamingiz bilan tasdiqlang
2. **API development tools** bo'limini oching
3. Ilova yarating (nom/tavsif ixtiyoriy, masalan "MyUserbot")
4. Sizga beriladigan `api_id` va `api_hash` ni saqlab qo'ying

## 2. O'rnatish

```bash
cd userbot
pip install -r requirements.txt
```

## 3. Sozlash

Terminalda quyidagi environment variable larni o'rnating (yoki `config.py`
ichiga to'g'ridan-to'g'ri yozing — lekin bu faylni hech kimga yubormang!):

```bash
export API_ID="1234567"
export API_HASH="abcdef1234567890abcdef1234567890"
```

Windows uchun (PowerShell):
```powershell
$env:API_ID="1234567"
$env:API_HASH="abcdef1234567890abcdef1234567890"
```

## 4. Ishga tushirish

```bash
python main.py
```

Birinchi marta ishga tushirganda u sizdan telefon raqamingiz va Telegramdan
kelgan tasdiqlash kodini so'raydi. Shundan so'ng `userbot.session` fayli
yaratiladi — keyingi safar qayta kod kiritish shart emas.

## 5. Buyruqlar

O'zingizning istalgan chatingizda (masalan, "Saved Messages"da) yozing:

| Buyruq | Vazifa |
|---|---|
| `.afk` | AFK rejimini yoqadi (standart xabar bilan) |
| `.afk Uxlayapman, ertaga javob beraman` | AFK ni sabab bilan yoqadi |
| `.unafk` | AFK rejimini o'chiradi |
| `.ping` | Bot ishlab turganini va tezligini tekshiradi |

AFK yoqilganda, sizga shaxsiy xabar yozgan har bir odamga **faqat bir marta**
avtomatik javob yuboriladi (spam bo'lmasligi uchun), toki siz `.unafk`
qilmaguningizcha.

## ⚠️ Diqqat

- **`userbot.session` faylini hech kimga bermang** — bu fayl orqali kimdir
  to'liq sizning akkountingizga kirib olishi mumkin.
- Telegram ToS (foydalanish shartlari)ga ko'ra, ommaviy spam yoki avtomatik
  ko'plab guruhlarga qo'shilish/xabar yuborish kabi harakatlar akkountingiz
  bloklanishiga sabab bo'lishi mumkin. Ushbu skript faqat shaxsiy,
  o'lchovli (AFK javob) foydalanish uchun mo'ljallangan.
- Kodni istalgancha o'zgartirib, yangi buyruqlar qo'shishingiz mumkin —
  `main.py` ichida har bir buyruq alohida funksiya sifatida yozilgan.
# userbot-afk
