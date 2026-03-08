from database import users, blocked
from config import OWNER_ID, ADMINS

def register(bot):
    @bot.message_handler(commands=['block'])
    def block_cmd(message):
        if message.from_user.id not in ADMINS and message.from_user.id != OWNER_ID:
            return
        if not message.reply_to_message:
            bot.reply_to(message,"Reply to user to block")
            return
        target_id = message.reply_to_message.from_user.id
        blocked.insert_one({"id": target_id})
        bot.reply_to(message,"🚫 User blocked from bot")