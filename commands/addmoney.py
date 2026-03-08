from database import users
from config import ADMINS, OWNER_ID

def register(bot):

    @bot.message_handler(commands=['addmoney'])
    def add_money(message):

        # admin or owner check
        if message.from_user.id not in ADMINS and message.from_user.id != OWNER_ID:
            bot.reply_to(message, "❌ Admin only command")
            return

        if not message.reply_to_message:
            bot.reply_to(message, "Reply to a user\nUsage: /addmoney amount")
            return

        try:
            amount = int(message.text.split()[1])
        except:
            bot.reply_to(message, "Usage: /addmoney amount")
            return

        user_id = message.reply_to_message.from_user.id

        users.update_one(
            {"id": user_id},
            {"$inc": {"money": amount}},
            upsert=True
        )

        bot.reply_to(
            message,
            f"💰 Added {amount} coins to {message.reply_to_message.from_user.first_name}"
        )
