from bot import bot
from pyrogram import filters


@bot.on_message(
    filters.command("start")
)
async def alive(_, message):
    await message.reply(
        f"Salam {message.from_user.mention}, Bu qeyri-rəsmi bir Shazam Telegram Botudur.\n\nℹ️ Mənə audio, video və ya səsli qeyd göndərə bilərsiniz, Sizə shazamla nəticələrini göndərəcəm.."
    )
