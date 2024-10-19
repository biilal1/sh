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
@Client.on_message(filters.command(["/start","رجوع للقائمة الرئيسيه"], ""))
async def start(client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([
["السورس","قسم التفعيل والتعطيل"],
["قسم التعيين","قسم البوت"],
["قسم المساعد","قسم الاذاعه"],
["تحديث البوت","الغاء الامر"]], resize_keyboard=True)
   return await message.reply_text("**اهلا بك ، عزيزي المطور الاساسي .**", reply_markup=kep,quote=True)
 else:
  kep = ReplyKeyboardMarkup([
["مطور البوت", "مطور السورس"],
["السورس","بنج"],
["رمزيات","استوري"],
["صور انمي","الاوامر"],
["تويت", "صراحه"],
["نكته","احكام"],
[" لو خيروك","انصحني"],
["اوقات الصلاه"],
["اذكار","كتابات"],
["حروف","بوت"],
["قران الكريم","استوري قران"],
["رمزيات بنات","المزيد من الصور"]], resize_keyboard=True)
  await message.reply_text("**صلي علي النبي وتبسم ♥️✨**", reply_markup=kep,quote=True)
  username = client.me.username
  if os.path.isfile(f"{username}.png"):
    photo = f"{username}.png"
  else:
    bot = await client.get_me()
    if not bot.photo:
       button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")]]
       return await client.send_message(message.chat.id, "ѕᴇʟᴇᴄᴛ ʏᴏụʀ ʟᴀɴɢụᴀɢᴇ ♪", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    username = client.me.username
    photo = await gen_bot(client, username, photo)
  button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")]]
  await client.send_photo(message.chat.id, photo=photo, caption="الرجاء الضغط علي اللغة اذا كانت اللغة العربية او باللغة الانجلزية\n\nᴘʟᴇᴀѕᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʟᴀɴɢụᴀɢᴇ ɪғ ɪᴛ ɪѕ ᴀʀᴀʙɪᴄ ᴏʀ ᴇɴɢʟɪѕʜ", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["قسم التعيين"], ""))
async def cast(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["تعين اسم البوت"],
["تعين قناة البوت","تعين مجموعة البوت"],
["تعين قناة السورس","تعين مجموعة السورس"],
["تعين لوجو السورس","تعين يوزر مطور السورس"], 
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text("**♪ مرحبا بك في قسم ⟨ التعيين ⟩ ⚡ .**", reply_markup=kep)
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command("قسم البوت", ""))
async def K_o_c_1(client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  chat = message.chat.id
  uesr = message.chat.username
  if chat == dev or uesr in OWNER:
    kep = ReplyKeyboardMarkup([
["الاحصائيات","المكالمات النشطه"],
["المجموعات","المستخدمين"],
["تغير مكان سجل التشغيل"],
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text(f"**♪ مرحبا بك في قسم ⟨ البوت ⟩  💎 .**", reply_markup=kep)
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
bot = [
  "معاك يشق",
  "يسطا شغال شغال متقلقش",
  "بحبك يعم قول عايز اي",
  "يبني هتقول عايز اي ولا اسيبك وامشي ",
  "قلب {} من جوه",
  "نعم يقلب {} ",
  "قرفتني والله بس بحبك بقا اعمل اي",
  "خلاص هزرنا وضحكنا انطق بقا عايز اي ؟",
  "قوول يقلبو ",
  "طب بذمتك لو انت بوت ترضا حد يقرفقك كدا؟",
]
  
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["/help", "الاوامر", "اوامر"], ""))
async def starhelp(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bot = await client.get_me()
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    await message.reply_photo(
        photo=photo,
        caption=f"",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("اللغة العربية 🇪🇬", callback_data="arbic")
                        ],
                        [   
                            InlineKeyboardButton("English language 🇺🇲", callback_data="english")
                        ],
                        [
                            InlineKeyboardButton("اضف البوت الي مجموعتك ❤️", url="https://t.me/{bot.username}?startgroup=true")
                        ],
                    ]                         
                )
		  )
    try:
      os.remove(photo)
    except:
       pass
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["صور انمي", "صورة انمي", "صوره انمي", "انمي"], ""))
async def keroooo(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["المزيد من الصور","صور حزينه"], ""))
async def keroo(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/PVVVV/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["صور بنات", "صورة لبنت", "انمي بنات", "بنات","رمزيات بنات"], ""))
async def kero(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/otsoo3/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["صور", "صوره", "صورة", "رمزيه", "رمزية", "رمزيات"], ""))
async def keroooooo(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/Picture_elnqyb/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["صور", "صوره", "صورة", "رمزيه", "رمزية", "رمزيات"], ""))
async def voece(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/ELNQYBMUSIC/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["ستوري","استوري","حلات واتس"], ""))
async def voece(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/videi_FilesKeRo/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["ستوري قران","استوري قران","حلات واتس قران"], ""))
async def qurann(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/a9li91/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    ) 
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@app.on_message(filters.command(["ق", "قران", "قران كريم", "سوره"], ""))
async def qurann2(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/alkoraan4000/{rl}"
    await client.send_photo(message.chat.id,url,caption="**♪ 𝙾𝚆𝙽𝙴𝚁 ➧ @Y_J_J_J  💎 .**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )