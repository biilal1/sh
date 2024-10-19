from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "KeRo",
    api_id="9671629",
    api_hash="be5c84e9dc1ca0e2b53d54b71e575124",
    bot_token="7064480810:AAHZn4ID-aUs6yaxA6XU-JBl8syJxPHLAZM",
    plugins=dict(root="MakerKeRo")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    USER = "BDB0B"
    await bot.send_message(USER, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
