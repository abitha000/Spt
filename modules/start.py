from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_photo(
        "resources/start_img.jpg",
        caption="🎵 **Welcome to the Spotify Music Bot!**\nUse `/play` to start playing music."
    )
  
