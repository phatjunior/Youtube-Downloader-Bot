from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"На данный момент бот может скачать только одно видео/аудио (сылка на PlayList не работает)"
    await message.reply_text(helptxt)
