class script(object):
    START_TXT = """<b>Hello {}, I'm {} 👋</b>
    
<b>I'm an advanced file store bot with these features:</b>
- File storage & sharing
- Clone bot creation
- Stream/download links
- URL shortener support
- Auto delete
- Smooth UI</b>"""

    CAPTION = """<b>📂 File Name: {file_name}

⚙️ Size: {file_size}</b>"""

    SHORTENER_API_MESSAGE = """<b>To add/update your Shortener API:</b>

<code>/api your_api_key</code>

<b>Current Website:</b> {base_site}
<b>Current API:</b> <code>{shortener_api}</code>

<b>To remove API:</b> <code>/api None</code>"""

    CLONE_START_TXT = """<b>Hello {}, I'm {} 👋</b>

<b>I'm a file store bot with clone feature.</b>

To create your own clone bot, use /clone command."""

    ABOUT_TXT = """<b>🤖 Bot Name: {}</b>

<b>📝 Language:</b> <a href="https://www.python.org">Python 3</a>
<b>📚 Library:</b> <a href="https://docs.pyrogram.org">Pyrogram</a>
<b>🧑‍💻 Developer:</b> <a href="tg://user?id={}">Click Here</a>"""

    CABOUT_TXT = """<b>🤖 Bot Name: {}</b>

<b>📝 Language:</b> Python 3
<b>📚 Library:</b> Pyrogram
<b>🧑‍💻 Developer:</b> <a href="tg://user?id={}">Click Here</a>"""

    CLONE_TXT = """<b>Clone Bot Creation:</b>

1. Send <code>/newbot</code> to @BotFather
2. Choose a name & username
3. Get your bot token
4. Forward the token to me
5. I'll create your clone bot"""

    HELP_TXT = """<b>Available Commands:</b>

🔹 /link - Get shareable file link
🔹 /batch - Create batch links
🔹 /clone - Create clone bot
🔹 /base_site - Set URL shortener domain
🔹 /api - Set shortener API key
🔹 /deletecloned - Delete clone bot
🔹 /broadcast - Broadcast message (Owner only)"""

    CHELP_TXT = """<b>Basic Commands:</b>

🔹 /link - Get file link
🔹 /base_site - Set shortener domain
🔹 /api - Set API key
🔹 /broadcast - Broadcast message"""

    LOG_TEXT = """<b>New User:</b>

ID: <code>{}</code>
Name: {}"""

    RESTART_TXT = """<b>Bot Restarted</b>

📅 Date: <code>{}</code>
⏰ Time: <code>{}</code>
🌐 Timezone: <code>Asia/Kolkata</code>"""
