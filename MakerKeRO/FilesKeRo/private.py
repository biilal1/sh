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
@Client.on_message(filters.text)
async def bott(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    if message.text == BOT_NAME:
      bar = random.choice(bot).format(BOT_NAME)
      await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**")
    message.continue_propagation()
    
    
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//   
@Client.on_message(filters.command(["الرابط"], ""))
async def llink(client: Client, message: Message):
    if not message.from_user.username in ["Y_J_J_J"]:
      return
    chat_id = message.text.split(None, 1)[1].strip()
    invitelink = (await client.export_chat_invite_link(chat_id))
    await message.reply_text("**♪ رابط المجموعة  💎 .**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرابط", url=f"{invitelink}")]]))
    
        
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(~filters.private)
async def booot(client: Client, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(client, chat_id):
       try:
        await add_served_chat(client, chat_id)
        chats = len(await get_served_chats(client))
        bot_username = client.me.username
        dev = await get_dev(bot_username)
        username = f"https://t.me/{message.chat.username}" if message.chat.username else None
        mention = message.from_user.mention if message.from_user else message.chat.title
        await client.send_message(dev, f"**تم تفعيل محادثة جديدة تلقائياً واصبحت {chats} محادثة**\nNew Group : [{message.chat.title}]({username})\nId : {message.chat.id} \nBy : {mention}")
        await client.send_message(chat_id, f"**تم رفع البوت بنجاح ايها العضو اللطيف 🥷**")
        return 
       except:
          pass
    message.continue_propagation()                