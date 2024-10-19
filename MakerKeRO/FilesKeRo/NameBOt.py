import random
from pyrogram import Client, filters, idle
from pyromod import listen
from pyrogram import Client as app
from time import time
from config import OWNER, OWNER_NAME, VIDEO
from FilesKeRo.info import (is_served_chat, add_served_chat, is_served_user, add_served_user, get_served_chats, get_served_users, del_served_chat, joinch)
from FilesKeRo.Data import (get_dev, get_bot_name, set_bot_name, get_logger, get_group, get_channel, get_dev_name, get_groupsr, get_channelsr, get_userbot)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, User, ChatPrivileges, ReplyKeyboardRemove, CallbackQuery
from pyrogram import enums
from FilesKeRo.Data import get_channel, get_dev , OWNER, set_join_must
from pyrogram.enums import ChatType, ChatMemberStatus, ParseMode, ChatMemberStatus
import os
import re
import textwrap
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch


#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
async def gen_bot(client, username, photo):
        if os.path.isfile(f"{username}.png"):
           return f"{username}.png"
        users = len(await get_served_users(client))
        chats = len(await get_served_chats(client))
        url = f"https://www.youtube.com/watch?v=gKA2XFkJZhI"
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"thumb{username}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"{photo}")
        Mostafa = Image.open(f"{photo}")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = Mostafa.width / 2
        Ycenter = Mostafa.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = Mostafa.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("font2.ttf", 40)
        font2 = ImageFont.truetype("font2.ttf", 70)
        arial = ImageFont.truetype("font2.ttf", 30)
        name_font = ImageFont.truetype("font.ttf", 30)
        draw.text(
            (600, 150),
            "Music Player BoT",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        draw.text(
            (600, 340),
            f"Dev : KeRo",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        draw.text(
            (600, 280),
            f"Playing Music & Video",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )

        draw.text(
            (600, 400),
            f"user : {users}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 450),
            f"chats : {chats}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Version : 0.1.5",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"BoT : t.me\{username}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"thumb{username}.png")
        except:
            pass
        background.save(f"{username}.png")
        return f"{username}.png"

#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//

selections = [
    "اسمي {} يصحبي",
    "يسطا قولتلك اسمي {} الاه",
    "نعم يحب ",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {}",
    "تعرف بالله هحبك اكتر لو ناديتلي {}",
    "اي ي معلم مين مزعلك",
    "متصلي علي النبي كدا ",
    "مش فاضيلك نصايه وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج ع اخوك",
    "انجز عايزني اشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا ",
    "ورحمه ابويا اسمي {}",
]
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["بوت", "البوت"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**")
    
    
    
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command("تعين اسم البوت", ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id,"**♪ ارسل اسم البوت الجديد  💎 .**", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("**♪ تم تعين اسم البوت بنجاح  💎 .**")

#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command("تعين لوجو السورس", ""))
async def set_vi_so(client: Client, message):
   NAME = await client.ask(message.chat.id,"**♪ ارسل رابط لوجو السورس  💎 .\n♪ مثال ⟨ https://telegra.ph/file/5052303e233d674acebd1.jpg ⟩  💎 .**", filters=filters.text, timeout=30)
   VID_SO = NAME.text
   bot_username = client.me.username
   await set_video_source(bot_username, VID_SO)
   await message.reply_text("**♪ تم تعين لوجو السورس  بنجاح  💎 .**")
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================// 
@Client.on_message(filters.command("تعين يوزر مطور السورس", ""))
async def set_dev_username(client: Client, message):
   NAME = await client.ask(message.chat.id,"**♪ ارسل معرف المطور الجديد  💎 .**", filters=filters.text, timeout=300)
   CH_DEV_USER = NAME.text
   bot_username = client.me.username
   await set_dev_user(bot_username, CH_DEV_USER)
   await message.reply_text("**♪ تم تعين المطور بنجاح  💎 .**")    