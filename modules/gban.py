from pyrogram import Client, filters
from database.mongo import db

@Client.on_message(filters.command(["gban", "ungban"]))
async def gban_handler(client, message):
    if not message.from_user.is_sudo:  # Check if the user is a sudo user
        await message.reply("❌ **You do not have permission to use this command.**")
        return

    if len(message.command) < 2:
        await message.reply_photo(
            "resources/start_img.jpg", 
            caption="❌ **Usage:** /gban <user_id> or /ungban <user_id>"
        )
        return

    user_id = int(message.command[1])
    if message.command[0] == "gban":
        await db.banned_users.insert_one({"user_id": user_id})
        await message.reply_photo(
            "resources/start_img.jpg", 
            caption=f"🚫 **Globally banned user:** {user_id}"
        )
    else:
        await db.banned_users.delete_one({"user_id": user_id})
        await message.reply_photo(
            "resources/start_img.jpg", 
            caption=f"✅ **User unbanned globally:** {user_id}"
        )
