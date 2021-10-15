from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Канал", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Сообщить о проблемах", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Привет <b>{message.from_user.first_name}</b> пришли мне ссылку на ютуб видео"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
