from pyrogram import Client, filters
from utils.spotify import search_song, get_playlist
from database.mongo import add_to_queue
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("play"))
async def play_command(client, message):
    if len(message.command) < 2:
        await message.reply("❌ **Usage:** /play <song name or Spotify URL>")
        return

    query = message.text.split(maxsplit=1)[1]
    chat_id = message.chat.id

    if "playlist" in query:
        tracks = get_playlist(query)
        for track in tracks:
            await add_to_queue(chat_id, track)
        await message.reply(f"✅ **Added {len(tracks)} songs from playlist to queue.**")
        return

    track = search_song(query)
    if not track:
        await message.reply("❌ **Could not find the song on Spotify.**")
        return

    await add_to_queue(chat_id, track)
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("⏸ Pause", callback_data="pause"),
         InlineKeyboardButton("⏩ Skip", callback_data="skip")]
    ])
    await message.reply_photo(
        track["thumbnail"],
        caption=f"🎶 **Playing:** {track['name']} - {track['artist']}",
        reply_markup=buttons
  )
  
