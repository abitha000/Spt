from pyrogram import Client, filters
from database.mongo import clear_queue

@Client.on_message(filters.command("end"))
async def end_command(client, message):
    chat_id = message.chat.id
    await clear_queue(chat_id)
    await message.reply_photo(
        "resources/start_img.jpg",
        caption="🛑 **Playback ended and queue cleared.**"
    )
  
