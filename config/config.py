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
ASSISTANT_SESSIONS = os.getenv("ASSISTANT_SESSIONS", "BQF0VVMABbv538Zl2NunpHHNA9Bpz5m9MkBHogKvjTMwuWtLlTS_YW21rChFgha9urSUXGHvDjDL5wmkT4olM4Dg0IiPjyCmZPhH6qLtCqdPp4cMPDnDIfsTlZJTt5aXrmuXpxASaVUqjVkJyEXQj5V1gypJ1RxtCHdSYhoh3sP_pdsa9WxPFpWNMqhvWJ_hDvW9TWMBVDjULjCUBSWKTti4v_xn-u-F8raTeudeDjsXhTablN0PlFNqhWXApUFFD60gRCS7A1W8WUY868RIIDiACdoOylj27jR5d1QwaPKUoglUpPQ9UHJkPFtKGviqsZTCiVSILKWGUU52eMVBgXvORivuLgAAAAGwd90wAA").split()  # Space-separated session strings
