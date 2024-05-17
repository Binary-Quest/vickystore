#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6843471498:AAGsUOLkWJDWZdKeAIkZJLFLF1cdC47JzV4")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16575077"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1c8c0bcb55c14e0fd8078058966b6a11")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002101416464"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1702061654"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://BinaryQuest:Binary-01234@cluster0.snovwft.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hᴇʟʟᴏ {first} 🖤\n\nI ᴀᴍ ʏᴏᴜʀ ᴡᴀɪꜰᴜ.. 🥵\n\n-> ʏᴏᴜ ᴄᴀɴ ᴜɴᴅʀᴇss ᴍᴇ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴅᴇᴏꜱ ᴀɴᴅ ʟɪɴᴋꜱ sʜᴀʀᴇᴅ ʙʏ ᴠɪᴄᴋʏ ʙʜᴀɪʏᴀ😈\n\n\n☟︎︎︎  C......Ⓟ︎  ᴋ!ᴅ$  ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTI1NzU0MDA2NDAzMTI0OC0yNjg1NjMxNzk2MTIzNTI'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ M⍟M - S⍟N small ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTY1MTM2NTkyMDcwMTYwLTc3MTYxODA5MDY3NzI4'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ M⍟M - S⍟N ʏᴏᴜɴɢ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTc4MTYzOTEwNDg0MTkyLTg0MTc2NTE4OTgyOTc2'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ ɪɴᴄᴇ$ᴛ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTI3MTU2OTQ4Mzg2MTc0NC0yODA1ODgzOTY2MDk5MjA'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Tᴇ€N ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTk0MTk3NTMzMTQ3NjE2LTEwMTIxMjI0MzA2Mjg2NA'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ R---P ғ0ʀᴄᴇᴅ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTEwMjIxNDM0NDQ3OTMyOC0xMDkyMjkwNTQzOTQ1NzY'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ GⒶ︎ʏ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTExMDIzMTE1NTgxMTA0MC0xMTgyNDc5NjcxNDI3NTI'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ sⒾ︎s - ʙʀⓄ︎ ☟︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTExOTI1MDA2ODU1OTIxNi0xMjgyNjg5ODEzMDczOTI'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Hɪᴅᴅᴇɴ ᴄᴀᴍ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTI4MTU5MDQ5ODAyNjM4NC0yODc2MDMxMDY1MjUxNjg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Sɴᴀᴘᴄʜᴀᴛ ʟᴇ@ᴋ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTI4ODYwNTIwNzk0MTYzMi0zMDA2MzA0MjQ5MzkyMDA'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Tᴀᴍɪʟ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTMwMTYzMjUyNjM1NTY2NC0zMDk2NDkzMzc2ODczNzY'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Mᴀʟʟᴜ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTMxMDY1MTQzOTEwMzg0MC0zMTU2NjE5NDYxODYxNjA'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Kᴀɴɴᴀᴅᴀ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTMxNjY2NDA0NzYwMjYyNC0zMTk2NzAzNTE4NTIwMTY'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Tᴇʟᴜɢᴜ  ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTMyMDY3MjQ1MzI2ODQ4MC0zMjQ2ODA4NTg5MzQzMzY'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Dʀᴜ‌𝑔  𝑓𝑼ᴄᴋ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTMyNTY4Mjk2MDM1MDgwMC0zMjc2ODcxNjMxODM3Mjg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎  D€Sɪ - ɪɴᴅ  ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTQ2ODk4MzQ2MjkwNTE1Mi01MDMwNTQ5MTEwNjQ5Mjg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ ᴍɪx ᴅᴇs! 2024 ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTUwNDA1NzAxMjQ4MTM5Mi01MjAwOTA2MzUxNDQ4MTY'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ D€S! G!ʀʟs ᴀʟʙᴜᴍ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTcyNDUxOTMyNDEwMzQ3Mi03MjU1MjE0MjU1MTk5MzY'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n☟︎︎︎ Mᴇᴍʙᴇʀsʜɪᴘ ᴜᴘᴅᴀᴛᴇ ☟︎︎︎ <a href='https://t.me/Link_providerr_bot?start=Z2V0LTcyNjUyMzUyNjkzNjQwMC03Mjc1MjU2MjgzNTI4NjQ'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n\nɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇs ᴀɴᴅ ᴇɴᴊᴏʏ 🥀</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7111311972").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Tʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴏᴜʀ ʙᴏᴛ 🖤\nBᴀᴄᴋᴜᴘ ~ https://t.me/+hiP5wprGfB5iMzA0 ☠️"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
