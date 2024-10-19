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
array = []
@Client.on_message(filters.command(["@all", "تاك","all"], "") & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("**♪ التاك قيد التشغيل الان  💎 .**")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")
    return
  await message.reply_text("**♪ جاري بدأ المنشن ، لايقاف الامر اضغط /cancel  💎 .**")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("all","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.get_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ›"
       if i == 20:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["/cancel", "ايقاف التاك"], ""))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")
    return
  if message.chat.id not in array:
     await message.reply("**♪ المنشن متوقف بي الفعل  💎 .**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("**♪ تم ايقاف المنشن عزيزي  💎 .**")
    return