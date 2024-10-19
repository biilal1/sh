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
@Client.on_message(filters.command(["/ping", "بنج"], ""))
async def ping_pong(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    start = time()
    m_reply = await message.reply_text("**pinging...**")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")