from database import blocked
from config import OWNER_ID, ADMINS

def register(bot):

    @bot.message_handler(commands=['block'])
    def block_cmd(message):

        if message.from_user.id not in ADMINS and message.from_user.id != OWNER_ID:
            bot.reply_to(message, "❌ Admin only command")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "Reply to a user to block")
            return

        target_id = message.reply_to_message.from_user.id

        # prevent blocking owner/admin
        if target_id == OWNER_ID or target_id in ADMINS:
            bot.reply_to(message, "❌ Cannot block owner/admin")
            return

        # check if already blocked
        if blocked.find_one({"id": target_id}):
            bot.reply_to(message, "⚠ User already blocked")
            return

        blocked.insert_one({"id": target_id})

        bot.reply_to(message, "🚫 User blocked from bot")

    @bot.message_handler(commands=['unblock'])
    def unblock_cmd(message):

        if message.from_user.id not in ADMINS and message.from_user.id != OWNER_ID:
            bot.reply_to(message, "❌ Admin only command")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "Reply to a user to unblock")
            return

        target_id = message.reply_to_message.from_user.id

        blocked.delete_one({"id": target_id})

        bot.reply_to(message, "✅ User unblocked")
