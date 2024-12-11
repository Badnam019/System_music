from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @lll_BADNAM_BABY_lll
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("❍𝐒ʏsᴛᴇᴍ 𝐌ᴜsɪᴄ❍", url="https://t.me/SYSTEM_BOT_UPDATE"),
          InlineKeyboardButton("❛-Ɱɽ ⌯ 𝐁ᴀᴅ֟፝ɴᴀᴍ᭄↝𝐱𝐃", url="https://t.me/lll_BADNAM_BABY_lll"),
          ],
               [
                InlineKeyboardButton("❍𝐒ʏsᴛᴇᴍ 𝐌ᴜsɪᴄ❍", url=f"https://t.me/SYSTEM_BOT_UPDATE"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"@system_music_prorobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/4z6upe.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
