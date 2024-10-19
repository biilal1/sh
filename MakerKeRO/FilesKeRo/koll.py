from pyrogram import filters, Client
import asyncio
import pyrogram
from typing import Optional
from pyrogram import Client, enums, filters
import pyrogram
from pyrogram import Client as client
import asyncio
from pyrogram import Client, idle
from random import randint
from typing import Optional
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, AlreadyJoinedError
from pyrogram.errors import ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.raw.base import GroupCallParticipant
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, EditGroupCallParticipant
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat, InputUserSelf, GroupCallParticipant
from pyrogram.types import Message
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from datetime import datetime
import requests
import pytz
from pyrogram.errors import ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant
from config import user, dev, call, logger, logger_mode, botname, appp
from FilesKeRo.Data import get_call, get_userbot, get_dev, get_logger , get_channel , devchannel

@Client.on_message(filters.command("مين في الكول", ""))
async def ghsdh_user(client, message):
    bot_username = client.me.username
    hoss = await get_call(bot_username)    
    hh = await message.reply("استنا اطلع اشوف مين في الكول✨♥") 
    try:
     await hoss.join_group_call(message.chat.id, AudioPiped("./FilesKeRo/KeroMenFecall.mp3"), stream_type=StreamType().pulse_stream)
     text="😎🥰 الاشخاص المتواجدين في الكول:\n\n"
     participants = await hoss.get_participants(message.chat.id)
     k =0
     for participant in participants:
      info = participant
      if info.muted == False:
       mut="يتحدث 🗣"
      else:
       mut="ساكت 🔕"
      user = await client.get_users(participant.user_id)
      k +=1
      text +=f"{k}➤{user.mention}➤{mut}\n"
      text += f"\nعددهم : {len(participants)}\n✔️"    
     await hh.edit_text(f"{text}")
     await hoss.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
     await message.reply(f"حبيبي الكول مش مفتوح اصلااا\n😜")
    except TelegramServerError:
     await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n😜")
    except AlreadyJoinedError:
     text="😎🥰 الاشخاص المتواجدين في الكول:\n\n"
     participants = await hoss.get_participants(message.chat.id)
     k =0
     for participant in participants:
      info = participant
      if info.muted == False:
       mut="يتحدث 🗣"
      else:
       mut="ساكت 🔕"
      user = await client.get_users(participant.user_id)
      k +=1
      text +=f"{k}➤{user.mention}➤{mut}\n"
      text += f"\nعددهم : {len(participants)}\n✔️"    
      await hh.edit_text(f"{text}")
      
async def get_group_call(
    client: Client, message: Message, err_message: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.reply_text(f"{err_message}")
    return False
