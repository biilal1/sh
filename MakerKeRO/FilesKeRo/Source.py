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
@Client.on_message(
    filters.command(["/alive", "معلومات", "سورس", "السورس", "• السورس •"], "")
)
async def alive(client: Client, message):
    chat_id = message.chat.id
    ch = await get_channelsr(client.me.username)
    gr = await get_groupsr(client.me.username)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("{𝐠𝐫𝐨𝐮𝐩}", url=f"{gr}"),
                InlineKeyboardButton("{𝐜𝐡𝐧𝐧𝐞𝐥}", url=f"{ch}"),
            ],
            [
                 InlineKeyboardButton(f"{OWNER_NAME}", url=f"https://t.me/{OWNER[0]}")
            ],
            [ 
                 InlineKeyboardButton("اضف البوت الي مجموعتك سورس كيرو❤️", url="https://t.me/{app.username}?startgroup=true")
            ]
        ]
    )

    alive = f"""╭──── • ◈ • ────╮
么 [𝙾𝚆𝙽𝙴𝚁1](t.me/Y_J_J_J) 💎 .
么 [𝙾𝚆𝙽𝙴𝚁2](t.me/H_H_H_P) 💎 .
么 [𝙾𝚆𝙽𝙴𝚁3](t.me/N_7_K) 💎 .
么 [𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒔𝒐𝒖𝒓𝒄𝒆](t.me/OE_YT).
╰──── • ◈ • ────╯
𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼💎 ."""

    await message.reply_video(
        video=VIDEO,
        caption=alive,
        reply_markup=keyboard,
    )

