class script(object):
    START_TXT = """<b>ʜᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ {} 👋, ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ + ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ + sᴛʀᴇᴀᴍ / ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴇᴀᴛᴜʀᴇ + ᴄᴜꜱᴛᴏᴍ ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ ꜱᴜᴘᴘᴏʀᴛ + ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ʙᴇꜱᴛ ᴜɪ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ </b>"""

    CAPTION = """<b>📂 ғɪʟᴇɴᴀᴍᴇ : {file_name}

⚙️ sɪᴢᴇ : {file_size}

Jᴏɪɴ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ](https://t.me/brutualincognito)</b>""" 

    SHORTENER_API_MESSAGE = """<b>Tᴏ ᴀᴅᴅ ᴏʀ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ Sʜᴏʀᴛɴᴇʀ Wᴇʙsɪᴛᴇ API, /api (ᴀᴘɪ)
            
<b>Ex: /api 𝟼LZǫ𝟾𝟻𝟷sXᴏғғғPHᴜɢɪKQǫ

<b>Cᴜʀʀᴇɴᴛ Wᴇʙsɪᴛᴇ: {base_site}

Cᴜʀʀᴇɴᴛ Sʜᴏʀᴛᴇɴᴇʀ API:</b> `{shortener_api}`

If You Want To Remove Api Then Copy This And Send To Bot - `/api None`"""

    CLONE_START_TXT = """<b>ʜᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ {} 👋, ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ + ᴄᴜꜱᴛᴏᴍ ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ ꜱᴜᴘᴘᴏʀᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ʙᴇꜱᴛ ᴜɪ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ᴛʜᴇɴ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ᴄʟᴏɴᴇ ʙᴏᴛ ғʀᴏᴍ ᴍʏ <a href=https://t.me/vj_botz>ᴘᴀʀᴇɴᴛ</a></b>"""

    ABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ + ᴄᴜsᴛᴏᴍ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ɪᴛ ᴍᴇᴀɴs ᴀɴʏ ᴜsᴇʀ ᴄᴀɴ sᴇᴛ ʜɪs ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀɴᴅ + ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ.

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/Kingvj01>𝐓𝐞𝐜𝐡 𝐕𝐉</a>

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/VJ_Bot_Disscussion>𝐕𝐉 𝐒𝐮𝐩𝐩𝐨𝐫𝐭</a>

📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/vj_botz>𝐕𝐉 𝐔𝐩𝐝𝐚ᴛᴇ</a></b>
"""

    CABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ + ᴄᴜsᴛᴏᴍ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ɪᴛ ᴍᴇᴀɴs ᴀɴʏ ᴜsᴇʀ ᴄᴀɴ sᴇᴛ ʜɪs ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀɴᴅ + ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ.

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=tg://user?id={}>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>
"""

    CLONE_TXT = """<b>ʜᴇʟʟᴏ {} 👋

First Send /clone command then follow below steps.
    
1) sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather
2) ɢɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.
3) ɢɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.
4) ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.
5) ꜰᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.

ᴛʜᴇɴ ɪ ᴀᴍ ᴛʀʏ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄᴏᴘʏ ʙᴏᴛ ᴏғ ᴍᴇ ғᴏʀ ʏᴏᴜ ᴏɴʟʏ 😌</b>"""

    HELP_TXT = """<b><u>💢 HOW TO USE THE BOT ☺️</u>

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /batch - sᴇɴᴅ ғɪʀsᴛ ʟɪɴᴋ ᴏғ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ᴛʜᴇɴ ʟᴀsᴛ ᴘᴏsᴛ ʟɪɴᴋ ᴀɴᴅ ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ.
ᴇx - /batch https://t.me/vj_botz/25 https://t.me/vj_botz/30
