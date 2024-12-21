from pyrogram import Client, filters
from database.mongo import get_queue, add_to_queue

@Client.on_message(filters.command("skip"))
async def skip_command(client, message):
    chat_id = message.chat.id
    queue = await get_queue(chat_id)

    if not queue:
        await message.reply("❌ **The queue is empty.**")
        return

    # Remove the first track in the queue
    skipped_track = queue.pop(0)
    await add_to_queue(chat_id, queue)  # Update the queue in the database

    # Play the next track
    if queue:
        next_track = queue[0]
        await message.reply(f"⏩ **Skipped:** {skipped_track['name']}.\n🎵 Now playing: {next_track['name']} by {next_track['artist']}.")
    else:
        await message.reply(f"⏩ **Skipped:** {skipped_track['name']}.\nThe queue is now empty.")

