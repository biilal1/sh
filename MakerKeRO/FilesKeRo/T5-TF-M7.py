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
@Client.on_message(filters.command(["قتل","تخ"], ""), group=1024)
async def ceev(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await set_join_must(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/a2c9fa6de45e0fc4fc81e.mp4",
          caption=f"• تم قتل هذا الشخص @{name}\n\n※ بواسطة @{CASER}\n\n ان لله وان اليه راجعون ⚰😭",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المقتول ⚰??", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("القاتل 👿🔪", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("ضيفني في جروب والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=tru")]]))
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//                                
@Client.on_message(filters.command(["بوسه","مح"], ""), group=1025554)
async def cee6v(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await set_join_must(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/f9fca108067895e042f1f.mp4",
          caption=f"••القميل هذا ✨♥ @{CASER}\n\n※ بعتلك بوسه يا 😘♥ @{name} \n\n عيب كده اي المحن ده 😹",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المقبول 👻??", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("القابل 😘🥹", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("ضيفني في جروب والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=tru")]]))         
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["تفو","تف"], ""), group=105524)
async def ceev55(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await set_join_must(client, message):
     return
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.username in caes:
        await message.reply_text("• عذرآ لا تستطيع استخدام الأمر على مطور السورس")
    else:
        caesar = await client.get_chat(message.from_user.id)
        CASER = caesar.username
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.username
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await message.reply_video(
          video="https://telegra.ph/file/7f4c6eebf2f23b41dea45.mp4",
          caption=f"• تم التف علي هذا الشخص @{name}\n\n※ بواسطة @{CASER} \n\n اععع اي القرف ده 🤢",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المتفوف عليه😂💔", url=f"https://t.me/{name}"), 
                                ],[InlineKeyboardButton("التافف 😂👻", url=f"https://t.me/{CASER}"), 
                                ],[InlineKeyboardButton("ضيفني في جروب والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=tru")]])) 