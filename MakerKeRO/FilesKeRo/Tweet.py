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

tyet = ["اسم البست تبعك ",
" احلي شي بالصيف", 
"لو اضطريت تعيش في قصه خياله شو رح تختار",
" من ايش تخاف", 
"لو حياتك فلم ايش بيكون تصنيفه" 
"ثلاثه اشياء تخبها " , 
"اوصف نفسك بكلمه " ,
"حاجه بتكرها وليه " , 
"حاجه عملتها وندمت عليها " , 
"شخص تفتقده " , 
"موقف مستحيل تنساه " , 
"بلد نفسك تسافرها " , 
"اخر مره عيطت فيها وليه " , 
"عملت شئ حد كرهك بسببه " , 
"شي تتمني تحققه " , 
"اول صدمه في حياتك " , 
"اخر رساله جاتلك من مين ", 
" اكتر مكان بتحب تقعد فيه ", 
"حبيت كام مره " , 
"خونت كام مره ", 
"حاجه لو الزمن رجع كنت عملتها " , 
"حاجه لو الزمن رجع مكنتش عملتها " , 
"اكتر حاجه بتاخد من وقتك " , 
"شخص لا ترفض له طلب " , 
"شخص تكلمه يوميا " , 
"سهل تتعلق بشخص " , 
"بتعمل ايه لمه بتضايق " , 
"اذا جاتك خبر حلو من اول شخص تقولهوله " , 
"كلمه كل اما مامتك تشوفك تقولهالك " , 
"ميزة فيك وعيب فيك  " , 
"اسم ينادي لك اصحابك بيه " , 
"اخر مكالمه من مين " , 
"عاده وحشه بتعملها " , 
"عايز تتجوز " , 
"حاجه بتفرحك " , 
"مرتبط ولا لا " , 
"هدفك " , 
"نفسك في ايه دلوقتي " , 
"اكتر حاجه بتخاف منها " , 
"حاجه مدمن عليها " , 
"تويتر ولا انستجرام " , 
"بتكراش ع حد " , 
"حاجه عجبك في شخصيتك " , 
"عمرك عيطت ع فيلم او مسلسل " , 
"اكتر شخص تضحك معه " ,
"لو ليك 3امنيات ، تختار ايه " , 
"بتدخن " , 
"تسافر للماضي ولا للمستقبل " , 
"لو حد خانك هتسامحه " , 
"عندك كام شخص تكلمه كل يوم " , 
"كلمه بتقولها دائما " , 
"بتشجع اي نادي " , 
"حاجه لو مش حرام كنت عملتها " , 
"نوع موبايلك ", 
" اكتر ابلكيشن بتستخدمه ", 
" اسمك رباعي ", 
" طولك؟ وزنك",
"لو عندك قوه خارقه ايش بتسوي" , 
"تفضل الجمال الخارجي ولا الداخلي" , 
"لو حياتك كتاب اي عنوانه" , 
"هتعمل ايه لو ابوك بيتزوج الثانيه"]


#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["كت","تويت","كت تويت"], ""))
async def bott6456(client: Client, message: Message):
      barto = random.choice(tyet)
      await message.reply(f"{barto}") 