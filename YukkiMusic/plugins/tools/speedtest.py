#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import os

import speedtest
import wget
from pyrogram import filters

from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("Tᴇsᴛɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴇᴅ")
        test.download()
        m = m.edit("Tᴇsᴛɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅ")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("Sʜᴀʀɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs")
        path = wget.download(result["share"])
    except Exception as e:
        return m.edit(e)
    return result, path


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("Rᴜɴɴɪɴɢ sᴘᴇᴇᴅ ᴛᴇsᴛ")
    loop = asyncio.get_event_loop()
    result, path = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**Cʟɪᴇɴᴛ:**</u>
**__Isᴘ:__** {result['client']['isp']}
**__Cᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**Sᴇʀᴠᴇʀ:**</u>
**__Nᴀᴍᴇ:__** {result['server']['name']}
**__Cᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__Sᴘᴏɴsᴇʀ:__** {result['server']['sponsor']}
**__Lᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__Pᴏɴɢ📍:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
