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
@Client.on_message(filters.command("رتبتي", ""))
async def bt(client: Client, message: Message):
  try:
     if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
     userr = message.from_user
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     if userr.username in OWNER :
         await message.reply_text("**♪  رتبتك هي : مطور السورس  💎 .**")
         return
     if userr.username in ["Y_J_J_J"]:
         await message.reply_text("**♪ رتبتك هي : المطور كيرو الحاكم  💎 .**")
         return
     if userr.username in ["N_7_K"]:
         await message.reply_text("**♪ رتبتك هي : المطور ابوحميد 💎 .**")
         return
     if userr.username in ["H_H_H_P"]:
         await message.reply_text("**♪ رتبتك هي : المطور مشاكس 💎 .**")
         return         
     if userr.id == dev:
        return await message.reply_text("**♪ رتبتك هي : المطور الاساسي  💎 .**")
     user = await message._client.get_chat_member(message.chat.id, message.from_user.id)
     if user.status == enums.ChatMemberStatus.OWNER:
         await message.reply_text("**♪ رتبتك هي : المالك  💎 .**")
         return
     if user.status == enums.ChatMemberStatus.ADMINISTRATOR:
         await message.reply_text("**♪ رتبتك هي : الادمن  💎 .**")
         return 
     else:
         await message.reply_text("**♪ رتبتك هي : العضو  💎 .**")
  except:
    pass