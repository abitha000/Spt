from pyrogram import Client
from config.config import API_ID, API_HASH, BOT_TOKEN, ASSISTANT_SESSIONS
from modules import *

app = Client("SpotifyMusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

assistants = [
    Client(name=f"assistant_{i}", api_id=API_ID, api_hash=API_HASH, session_string=session)
    for i, session in enumerate(ASSISTANT_SESSIONS)
]

async def start_assistants():
    for assistant in assistants:
        await assistant.start()

if __name__ == "__main__":
    app.start()
    app.loop.run_until_complete(start_assistants())
    print("Spotify Music Bot is running...")
    app.idle()
  
