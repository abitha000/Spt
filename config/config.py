import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "24401235"))
API_HASH = os.getenv("API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7705751598:AAFyX6YrCCWTZQ2hSFHd2hCHYsnSjWKvQ90")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1001975396715"))
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://avineyjr004:Team_HDSTR@cluster0.oxbmm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "566027c77614413ea026aecc9ae66431")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "8ff250d41eeb4199b10eb12b96d79f18")
ASSISTANT_SESSIONS = os.getenv("ASSISTANT_SESSIONS").split()  # Space-separated session strings
