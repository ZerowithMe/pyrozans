# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Dam-PyroBot

from pyrogram import idle
from uvloop import install

from config import BOT_VER
from Cilik import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from Cilik.helpers.misc import git, heroku

MSG_ON = """
✅ **PyroDam Activated.**

**🤖 Userbot Version -** `{}`
**Ketik** `.dam` **untuk Mengecheck Bot**
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("killuaroom")
            await bot.join_chat("diarydam")
            await bot.join_chat("damssyx")
            await bot.join_chat("CilikProject")
            await bot.join_chat("CilikSupport")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Dam").info("Starting PyroDam")
    LOGGER("Dam").info(f"Total Clients = {len(bots)} Users")
    install()
    git()
    heroku()
    LOGGER("Dam").info(f"PyroDam v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    LOOP.run_until_complete(main())
