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



ahkam =  ["  ♪ صورة وجهك او رجلك او خشمك او يدك ؟ ",
"  ♪ اصدر اي صوت يطلبه منك الاعبين ؟ ",
"  ♪ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
"  ♪ روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبينالحد الاقصى 3 رسائل ؟ ",
"  ♪ قول نكتة ولازم احد الاعبين يضحك اذا ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
"  ♪ سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك ؟ ",
"  ♪ ذي المرة لك لا تعيدها ؟ ",
"  ♪ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
"  ♪ صور اي شيء يطلبه منك الاعبين ؟ ",
"  ♪ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
"  ♪ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
"  ♪ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوته ؟ ",
"  ♪ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
"  ♪ روح عند اي احد بالخاص و قول له انك تحبه و الخ ؟ ",
"  ♪ اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص ؟ ",
"  ♪ قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
"  ♪ سامحتك خلاص مافيه عقاب لك  ؟ ",
"  ♪ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
"  ♪ غير اسمك الى اسم من اختيار الاعبين الي معك ؟ ",
"  ♪ اتصل على امك و قول لها انك تحبها  ؟ ",
"  ♪ لا يوجد سؤال لك سامحتك  ؟ ",
"  ♪ قل لواحد ماتعرفه عطني كف ؟ ",
"  ♪ منشن الجميع وقل انا اكرهكم ؟ ",
"  ♪ اتصل لاخوك و قول له انك سويت حادث و الخ.... ؟ ",
"  ♪ روح المطبخ و اكسر صحن  ؟ ",
"  ♪ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف ؟ ",
"  ♪ قول لاي بنت موجود في الروم كلمة حلوه ؟ ",
"  ♪ تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني ؟ ",
"  ♪ لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر ؟ ",
"  ♪ قول قصيدة  ؟ ",
"  ♪ تكلم باللهجة السودانية الين يجي دورك مرة ثانية ؟ ",
"  ♪ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
"  ♪ اول واحد تشوفه عطه كف ؟ ",
"  ♪ سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين ؟ ",
"  ♪ سامحتك خلاص مافيه عقاب لك  ؟ ",
"  ♪ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
"  ♪ روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك ؟ ",
"  ♪ تاخذ عقابين ؟ ",
"  ♪ قول اسم امك افتخر بأسم امك ؟ ",
"  ♪ ارمي اي شيء قدامك على اي احد موجود او على نفسك ؟ ",
"  ♪ اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك ؟ ",
"  ♪ اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه ؟ ",
"  ♪ تتصل على الوالدهو تقول لها خطفت شخص ؟ ",
"  ♪ تتصل على الوالدهو تقول لها تزوجت با سر ؟ ",
"  ♪ اتصل على الوالدهو تقول لهااحب وحده ؟ ",
"  ♪ تتصل على شرطي تقول له عندكم مطافي ؟ ",
"  ♪ خلاص سامحتك ؟ ",
"  ♪ تصيح في الشارع انامجنوون ؟ ",
"  ♪ تروح عند شخص وقول له احبك ؟"]
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================// 
@Client.on_message(filters.command(["حكم", "احكام"], ""))
async def bott987766(client: Client, message: Message):
      bar = random.choice(ahkam)
      await message.reply(f"{bar}") 