"""
Konfiguratsiya fayli.
API_ID va API_HASH ni https://my.telegram.org saytidan oling:
1. Saytga kirib, telefon raqamingiz bilan tasdiqlang
2. "API development tools" bo'limiga o'ting
3. Yangi ilova yarating (nom va tavsif ixtiyoriy)
4. api_id va api_hash ni shu yerga qo'ying
"""

import os

API_ID = int(os.environ.get("API_ID", "0"))          # my.telegram.org dan olingan api_id
API_HASH = os.environ.get("API_HASH", "")             # my.telegram.org dan olingan api_hash

# Agar environment variable bilan ishlash noqulay bo'lsa, shu ikki qatorni
# yuqoridagilar o'rniga to'g'ridan-to'g'ri yozib qo'yishingiz mumkin, masalan:
# API_ID = 1234567
# API_HASH = "abcdef1234567890abcdef1234567890"
# (Bu holatda faylni hech kimga yubormang!)
SESSION_NAME = "userbot"                              # session fayli nomi (o'zgartirmasa ham bo'ladi)

# Render/server'ga deploy qilganda ishlatiladi (generate_session.py orqali olinadi)
SESSION_STRING = os.environ.get("SESSION_STRING", "")

# Render "Web Service" porti (Render o'zi PORT env variable orqali beradi)
PORT = int(os.environ.get("PORT", "8080"))

# AFK xabari ichida ishlatiladigan buyruq prefiksi
CMD_PREFIX = "."

# Standart AFK xabari (ichida {time} - qancha vaqt AFK ekanligi qo'yiladi)
DEFAULT_AFK_MESSAGE = "🌙 Hozir band/uyqudaman, tez orada javob beraman.\n⏱ AFK: {time} dan beri"
