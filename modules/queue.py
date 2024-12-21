from pyrogram import Client, filters
from database.mongo import get_queue

@Client.on_message(filters.command("queue"))
async def queue_command(client, message):
    chat_id = message.chat.id
    queue = await get_queue(chat_id)

    if not queue:
        await message.reply_photo(
            "resources/queue_img.jpg", 
            caption="❌ **The queue is empty.**"
        )
        return

    text = "🎵 **Current Queue:**\n\n"
    for idx, track in enumerate(queue, start=1):
        text += f"{idx}. {track['name']} by {track['artist']}\n"

    await message.reply_photo(
        "resources/queue_img.jpg",
        caption=text
    )
  
