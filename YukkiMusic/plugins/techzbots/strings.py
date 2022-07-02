from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
**Hɪ! Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏʀ ᴠɪᴅᴇᴏs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ʙᴀʙʏ 🌟.**
"""

COMMANDS_TEXT = f"""
✨ **Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/mye-ѕυyaυ-07-02"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text=" Aᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴀʏ 🥺 ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="📚 Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/mye-ѕυyaυ-07-02"
            ),                       
        ],        
    ]
)
