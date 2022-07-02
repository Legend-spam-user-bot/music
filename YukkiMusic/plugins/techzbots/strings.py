from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
✨ **Hello MENTION !**

**You can use [{BOT_NAME}](https://t.me/{BOT_USERNAME}) to play Music or Videos in your Group Video Chat.**

💡 **Find out all the Bot's commands and how they work by clicking on the ➤ 📚 Commands button**
"""

COMMANDS_TEXT = f"""
✨ **Hello MENTION !**

**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 Commands", url="https://telegra.ph/mye-ѕυyaυ-07-02"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Add me to Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="📚 Commands", url="https://telegra.ph/mye-ѕυyaυ-07-02"
            ),                       
        ],        
    ]
)
