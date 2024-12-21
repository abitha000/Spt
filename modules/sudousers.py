from pyrogram import Client, filters
from database.mongo import db


@Client.on_message(filters.command(["addsudo", "remsudo"]))
async def sudo_handler(client, message):
    if not message.from_user.is_sudo:
        await message.reply("❌ **You do not have permission to use this command.**")
        return

    if len(message.command) < 2:
        await message.reply_photo(
            "resources/start_img.jpg",
            caption="❌ **Usage:** /addsudo <user_id> or /remsudo <user_id>"
        )
        return

    user_id = int(message.command[1])
    if message.command[0] == "addsudo":
        await db.sudo_users.insert_one({"user_id": user_id})
        await message.reply_photo(
            "resources/start_img.jpg",
            caption=f"✅ **Added sudo user:** {user_id}"
        )
    else:
        await db.sudo_users.delete_one({"user_id": user_id})
        await message.reply_photo(
            "resources/start_img.jpg",
            caption=f"✅ **Removed sudo user:** {user_id}"
        )


@Client.on_message(filters.command("sudolist"))
async def sudo_list(client, message):
    if not message.from_user.is_sudo:
        await message.reply("❌ **You do not have permission to use this command.**")
        return

    sudo_users = await db.sudo_users.find().to_list(length=100)
    if not sudo_users:
        await message.reply("❌ **No sudo users found.**")
        return

    text = "👑 **Sudo Users List:**\n\n"
    for user in sudo_users:
        text += f"➤ `{user['user_id']}`\n"

    await message.reply(text)
      
