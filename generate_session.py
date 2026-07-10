"""
Bu skriptni FAQAT O'ZINGIZNING KOMPYUTERINGIZDA (Render'da emas!) ishga tushiring.
U sizdan telefon raqam va SMS kodni so'raydi, so'ngra bitta uzun SESSION STRING
qiymatini chiqaradi. Shu qiymatni Render'dagi environment variable sifatida
saqlaysiz (SESSION_STRING nomi bilan).

Ishlatilishi:
    python generate_session.py
"""

from pyrogram import Client

import config

with Client(
    "session_generator",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    in_memory=True,
) as app:
    session_string = app.export_session_string()
    print("\n" + "=" * 60)
    print("SESSION STRING (buni Render'da SESSION_STRING nomi bilan saqlang):")
    print("=" * 60)
    print(session_string)
    print("=" * 60)
    print("\n⚠️  Bu qiymatni hech kimga bermang — u orqali akkountingizga")
    print("    to'liq kirish mumkin!")
