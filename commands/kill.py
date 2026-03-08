import time
from database import users

def register(bot):

    @bot.message_handler(commands=['kill'])
    def kill(message):

        if not message.reply_to_message:
            bot.reply_to(message,"Reply to a player to kill.")
            return

        attacker = users.find_one({"id": message.from_user.id})
        target_id = message.reply_to_message.from_user.id
        target = users.find_one({"id": target_id})

        if "awm" not in attacker["guns"]:
            bot.reply_to(message,"You need AWM to use /kill")
            return

        users.update_one(
            {"id": target_id},
            {"$set": {"health": 0, "dead_until": time.time() + 18000}}
        )

        bot.reply_to(message,"💀 Player killed! He will revive in 5 hours.")
