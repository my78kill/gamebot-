from database import users
from systems import xp_rank

def register(bot):
    @bot.message_handler(commands=['kill'])
    def kill(message):
        if not message.reply_to_message:
            bot.reply_to(message,"Reply to a user to kill")
            return

        attacker = users.find_one({"id": message.from_user.id})
        if "awm" not in attacker["guns"]:
            bot.reply_to(message,"You need AWM to kill! (100 dmg weapon)")
            return

        target_id = message.reply_to_message.from_user.id
        target = users.find_one({"id": target_id})

        if target["shield"] > 0:
            bot.reply_to(message,"Target has shield! Cannot kill.")
            return

        new_health = max(0, target["health"] - 100)
        users.update_one({"id": target_id},{"$set":{"health": new_health}})

        xp_rank.add_xp(message.from_user.id, 50)

        bot.reply_to(message,f"💀 Kill executed! Target health: {new_health}")