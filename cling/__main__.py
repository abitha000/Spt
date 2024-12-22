from pyrogram import Client, idle  # Import idle separately

from config import API_ID, API_HASH, BOT_TOKEN

# Initialize the bot
app = Client(
    "spotify_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

if __name__ == "__main__":
    print("Bot is starting...")

    # Start the bot
    app.start()
    
    print("Bot is now running. Press Ctrl+C to stop.")

    # Use idle to keep the bot running
    idle()

    # Stop the bot when exiting
    app.stop()
    print("Bot stopped.")
