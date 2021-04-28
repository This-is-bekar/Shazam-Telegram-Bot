from bot import bot, max_file


from pyrogram import filters, types
import os


@bot.on_message(filters.audio | filters.video | filters.voice)
async def voice_handler(_, message):
    file_size = message.audio or message.video or message.voice
    if max_file < file_size.file_size :
        await message.reply_text(
            "**⚠️ Maksimum fayl ölçüsü əldə edildi.**"
        )
        return
    file = await message.download(f'{bot.rnd_id()}.mp3')
    r = (await bot.recognize(file)).get('track', None)
    os.remove(file)
    if r is None:
        await message.reply_text(
            '**⚠️ Səsi tanıya bilmirəm**'
        )
        return
    out = f'**Mahnının adı**: `{r["title"]}`\n'
    out += f'**Sənətçi**: `{r["subtitle"]}`\n'
    buttons = types.InlineKeyboardMarkup(
        [
            [
                types.InlineKeyboardButton(
                    '🎼 Oxşar mahnılar',
                    switch_inline_query_current_chat=f'related {r["key"]}',
                ),
                types.InlineKeyboardButton(
                    '🔗 Paylaş',
                    url=f'{r["share"]["html"]}'
                )
            ],
            [
                types.InlineKeyboardButton(
                    '🎵 Dinləmək',
                    url=f'{r["url"]}'
                )
            ],
            [
                types.InlineKeyboardButton(
                    f'💿 {r["subtitle"]} - dən daha çox musiqi',
                    switch_inline_query_current_chat=f'tracks {r["artists"][0]["id"]}',
                )
            ]
            
        ]
    )
    await message.reply_photo(
        r['images']['coverarthq'],
        caption=out,
        reply_markup=buttons
    )
