"""
Pyrogram asosidagi Telegram Userbot - AFK (Away From Keyboard) rejimi.

Ishlatilishi:
    .afk [xabar]   -> AFK rejimini yoqadi (ixtiyoriy sabab bilan)
    .afk           -> AFK rejimini standart xabar bilan yoqadi
    .unafk         -> AFK rejimini o'chiradi
    .ping          -> Bot ishlab turganini tekshirish

AFK yoqilganda, sizga shaxsiy (private) xabar yozgan har bir odamga
faqat BIR MARTA avtomatik javob beriladi (spam bo'lmasligi uchun),
so'ngra siz .unafk buyrug'ini bergunimizcha ular yana yozsa jim turadi.
"""

import time
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

import config

app = Client(
    config.SESSION_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
)

# ---- Holat (state) ----
afk_state = {
    "active": False,
    "reason": "",
    "since": None,          # datetime
}

already_replied = set()    # AFK vaqtida allaqachon javob berilgan user_id lar


def format_afk_duration() -> str:
    if not afk_state["since"]:
        return ""
    delta = datetime.now() - afk_state["since"]
    minutes = int(delta.total_seconds() // 60)
    if minutes < 1:
        return "hozirgina"
    if minutes < 60:
        return f"{minutes} daqiqa"
    hours = minutes // 60
    rem_min = minutes % 60
    return f"{hours} soat {rem_min} daqiqa"


# ---------------------------------------------------------------------
# BUYRUQLAR (faqat SIZ o'zingizga yozganingizda ishlaydi - "outgoing")
# ---------------------------------------------------------------------

@app.on_message(filters.me & filters.command("afk", prefixes=config.CMD_PREFIX))
async def afk_on(client: Client, message: Message):
    reason = message.text.split(maxsplit=1)
    custom_reason = reason[1] if len(reason) > 1 else ""

    afk_state["active"] = True
    afk_state["reason"] = custom_reason
    afk_state["since"] = datetime.now()
    already_replied.clear()

    text = "✅ AFK rejimi yoqildi."
    if custom_reason:
        text += f"\nSabab: {custom_reason}"

    await message.edit_text(text)


@app.on_message(filters.me & filters.command("unafk", prefixes=config.CMD_PREFIX))
async def afk_off(client: Client, message: Message):
    was_active = afk_state["active"]
    duration = format_afk_duration() if was_active else ""

    afk_state["active"] = False
    afk_state["reason"] = ""
    afk_state["since"] = None
    already_replied.clear()

    if was_active:
        await message.edit_text(f"👋 AFK rejimi o'chirildi. (Davomiyligi: {duration})")
    else:
        await message.edit_text("AFK allaqachon o'chirilgan edi.")


@app.on_message(filters.me & filters.command("ping", prefixes=config.CMD_PREFIX))
async def ping(client: Client, message: Message):
    start = time.time()
    sent = await message.edit_text("🏓 Pong...")
    elapsed = (time.time() - start) * 1000
    await sent.edit_text(f"🏓 Pong! `{elapsed:.2f} ms`")


# ---------------------------------------------------------------------
# AVTO-JAVOB LOGIKASI (boshqalar sizga yozganda)
# ---------------------------------------------------------------------

@app.on_message(filters.private & ~filters.me & ~filters.bot)
async def auto_reply(client: Client, message: Message):
    if not afk_state["active"]:
        return

    user_id = message.from_user.id if message.from_user else None
    if user_id is None or user_id in already_replied:
        return

    already_replied.add(user_id)

    duration = format_afk_duration()
    text = config.DEFAULT_AFK_MESSAGE.format(time=duration)
    if afk_state["reason"]:
        text += f"\n💬 Sabab: {afk_state['reason']}"

    await message.reply_text(text)


if __name__ == "__main__":
    print("Userbot ishga tushmoqda...")
    app.run()
