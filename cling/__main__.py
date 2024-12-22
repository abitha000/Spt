import asyncio
from pyrogram import Client

from .config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "spotify_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():
    await app.start()
    print("Bot is now running. Press Ctrl+C to stop.")
    await asyncio.Event().wait()
    await app.stop()
    print("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())
