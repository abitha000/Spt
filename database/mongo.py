from motor.motor_asyncio import AsyncIOMotorClient
from config.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["SpotifyMusicBot"]

async def add_to_queue(chat_id, track):
    await db.queue.update_one(
        {"chat_id": chat_id},
        {"$push": {"tracks": track}},
        upsert=True
    )

async def get_queue(chat_id):
    queue = await db.queue.find_one({"chat_id": chat_id})
    return queue["tracks"] if queue else []

async def clear_queue(chat_id):
    await db.queue.delete_one({"chat_id": chat_id})
  
