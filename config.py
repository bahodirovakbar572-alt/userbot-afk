"""
Konfiguratsiya fayli.
API_ID va API_HASH ni https://my.telegram.org saytidan oling:
1. Saytga kirib, telefon raqamingiz bilan tasdiqlang
2. "API development tools" bo'limiga o'ting
3. Yangi ilova yarating (nom va tavsif ixtiyoriy)
4. api_id va api_hash ni shu yerga qo'ying
"""

import os

# Agar oddiy ishga tushirayotgan boʻlsangiz, os.environ shart emas:
API_ID = 34142096  # Raqam shaklida (int) bo'lishi kerak, qo'shtirnoqsiz
API_HASH = "abf8fc4aa3e632cd6b4054b5ee8388a0"  # Qo'shtirnoq ichida string shaklida
SESSION_NAME = "userbot"

CMD_PREFIX = "."


DEFAULT_AFK_MESSAGE = "🌙 Hozir band/uyqudaman, tez orada javob beraman.\n⏱ AFK: {time} dan beri"
