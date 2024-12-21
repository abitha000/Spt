from pyrogram import Client, filters

@Client.on_message(filters.command("resume"))
async def resume_command(client, message):
    await message.reply_photo(
        "resources/resume_img.jpg",
        caption="▶️ **Playback resumed.**"
    )
  
