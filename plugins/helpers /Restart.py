# @Hacker_Jr

import re, asyncio, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import ADMINS
    
@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**Hᴇʏ ×͜× ⏤͟͟͞͞HᴀᴄKᴇʀ Jʀ ᠰ Aʟʟ Mʏ Pʀᴏᴄᴇꜱꜱ Aʀᴇ Sᴛᴏᴘᴘᴇᴅ ⚙️ Wᴀɪᴛ Fᴏʀ 𝟻 Sᴇᴄꜱ 🤷‍♀️**", chat_id=message.chat.id)       
    await asyncio.sleep(5)
    await msg.edit("**⚙️ Rᴇꜱᴛᴀʀᴛᴇᴅ ‼️ \nNᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ 🙃**")
    await asyncio.sleep(7)
    await msg.delete()
    await message.delete()
    os.execl(sys.executable, sys.executable, *sys.argv)
