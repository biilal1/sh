from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "KeRo",
    api_id="15837209",
    api_hash="fe081df6989a4d79c1004903bb4f23e6",
    bot_token="7529604109:AAESIvco6lcEbVrCaXNv3mJyvmUsk5FPOfA",
    plugins=dict(root="MakerKeRo")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    USER = "Y_J_J_J"
    await bot.send_message(USER, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
