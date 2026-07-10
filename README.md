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

## 6. Render.com'ga bepul deploy qilish

Render'ga deploy qilishdan oldin ikkita narsani yodda tuting:

- Render fayl tizimi vaqtinchalik, shuning uchun `.session` fayl o'rniga
  **session string** ishlatiladi.
- Render bepul tarifida faqat **Web Service** ishlaydi (background worker
  emas), shuning uchun `main.py` ichiga kichik "health-check" http server
  qo'shilgan — bu shart, aks holda Render deploy'ni muvaffaqiyatsiz deb hisoblaydi.
- ⚠️ Bepul tarifda servis 15 daqiqa faolliksiz qolsa **uxlab qoladi** va
  keyingi so'rov kelganda qayta uyg'onadi (bu paytda userbot vaqtincha
  ulanishdan uziladi). Buni oldini olish uchun bepul "UptimeRobot" kabi
  xizmat orqali har 10-14 daqiqada Render URL'ingizga so'rov yuborib turishingiz
  mumkin (monitor turi: HTTP(s), interval: 10-14 daqiqa).

### Qadamlar:

**1) Session string oling (faqat lokal kompyuteringizda):**

```bash
python generate_session.py
```

Bu sizdan telefon raqam va SMS kodni so'raydi (agar avval `userbot.session`
fayli orqali kirgan bo'lsangiz, endi kod so'ramasligi ham mumkin). Oxirida
uzun bir qatorli **SESSION_STRING** chiqadi — uni nusxalab, xavfsiz joyga
saqlab qo'ying.

**2) Kodni GitHub'ga yuklang**

Loyihani (barcha fayllarni) o'zingizning GitHub repositoryingizga push qiling.

**3) Render'da yangi Web Service yarating**

1. https://render.com saytiga kiring (GitHub akkount bilan ro'yxatdan o'ting)
2. **New +** → **Web Service** ni tanlang
3. GitHub repositoryingizni ulang
4. Quyidagilarni kiriting:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Instance Type:** Free
5. **Environment** bo'limida quyidagi environment variable larni qo'shing:
   - `API_ID` → sizning api_id
   - `API_HASH` → sizning api_hash
   - `SESSION_STRING` → 1-qadamda olingan session string
6. **Create Web Service** tugmasini bosing

Render avtomatik ravishda kodni build qilib, ishga tushiradi. Loglarda
`"Userbot ishga tushmoqda..."` va `"Health-check server ... portda ishga
tushdi"` degan xabarlarni ko'rsangiz — hammasi tayyor, botingiz ishlayapti!

## ⚠️ Diqqat

- **`userbot.session` faylini hech kimga bermang** — bu fayl orqali kimdir
  to'liq sizning akkountingizga kirib olishi mumkin.
- Telegram ToS (foydalanish shartlari)ga ko'ra, ommaviy spam yoki avtomatik
  ko'plab guruhlarga qo'shilish/xabar yuborish kabi harakatlar akkountingiz
  bloklanishiga sabab bo'lishi mumkin. Ushbu skript faqat shaxsiy,
  o'lchovli (AFK javob) foydalanish uchun mo'ljallangan.
- Kodni istalgancha o'zgartirib, yangi buyruqlar qo'shishingiz mumkin —
  `main.py` ichida har bir buyruq alohida funksiya sifatida yozilgan.
