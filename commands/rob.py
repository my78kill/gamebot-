from database import users
from systems import xp_rank

RANKS_ORDER = ["Bronze","Silver","Gold","Platinum","Diamond","Heroic"]

def register(bot):
    @bot.message_handler(commands=['rob'])
    def rob(message):
        if not message.reply_to_message:
            bot.reply_to(message,"Reply to a user to rob")
            return

        attacker = users.find_one({"id": message.from_user.id})
        target_id = message.reply_to_message.from_user.id
        target = users.find_one({"id": target_id})

        attacker_rank = RANKS_ORDER.index(attacker["rank"])
        target_rank = RANKS_ORDER.index(target["rank"])

        if target_rank > attacker_rank:
            bot.reply_to(message,"Cannot rob higher rank users!")
            return

        robbed_amount = min(target["money"], 500 + attacker_rank*100)
        users.update_one({"id": target_id},{"$inc":{"money": -robbed_amount}})
        users.update_one({"id": message.from_user.id},{"$inc":{"money": robbed_amount}})

        xp_rank.add_xp(message.from_user.id, 30)

        bot.reply_to(message,f"💰 You robbed {robbed_amount} coins!")