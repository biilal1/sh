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



hroof = [" مدينة بحرف ♪ ع  ",
" حيوان ونبات بحرف ♪ خ  ", 
" اسم بحرف ♪ ح  ", 
" اسم ونبات بحرف ♪ م  ", 
" دولة عربية بحرف ♪ ق  ", 
" جماد بحرف ♪ ي  ", 
" نبات بحرف ♪ ج  ", 
" اسم بنت بحرف ♪ ع  ", 
" اسم ولد بحرف ♪ ع  ", 
" اسم بنت وولد بحرف ♪ ث  ", 
" جماد بحرف ♪ ج  ",
" حيوان بحرف ♪ ص  ",
" دولة بحرف ♪ س  ",
" نبات بحرف ♪ ج  ",
" مدينة بحرف ♪ ب  ",
" نبات بحرف ♪ ر  ",
" اسم بحرف ♪ ك  ",
" حيوان بحرف ♪ ظ  ",
" جماد بحرف ♪ ذ  ",
" مدينة بحرف ♪ و  ",
" اسم بحرف ♪ م  ",
" اسم بنت بحرف ♪ خ  ",
" اسم و نبات بحرف ♪ ر  ",
" نبات بحرف ♪ و  ",
" حيوان بحرف ♪ س  ",
" مدينة بحرف ♪ ك  ",
" اسم بنت بحرف ♪ ص  ",
" اسم ولد بحرف ♪ ق  ",
" نبات بحرف ♪ ز  ",
"  جماد بحرف ♪ ز  ",
"  مدينة بحرف ♪ ط  ",
"  جماد بحرف ♪ ن  ",
"  مدينة بحرف ♪ ف  ",
"  حيوان بحرف ♪ ض  ",
"  اسم بحرف ♪ ك  ",
"  نبات و حيوان و مدينة بحرف ♪ س  ", 
"  اسم بنت بحرف ♪ ج  ", 
"  مدينة بحرف ♪ ت  ", 
"  جماد بحرف ♪ ه  ", 
"  اسم بنت بحرف ♪ ر  ", 
" اسم ولد بحرف ♪ خ  ", 
" جماد بحرف ♪ ع  ",
" حيوان بحرف ♪ ح  ",
" نبات بحرف ♪ ف  ",
" اسم بنت بحرف ♪ غ  ",
" اسم ولد بحرف ♪ و  ",
" نبات بحرف ♪ ل  ",
"مدينة بحرف ♪ ع  ",
"دولة واسم بحرف ♪ ب  "]


#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["ح", "حروف", "الحروف", "حرف"], ""))
async def booyt(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(hroof)
    barto = random.choice(hrooof)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id)
    await ask.reply_text(f"**{barto}**")
   except:
       pass
