from database import users
from systems import xp_rank

RANKS_ORDER = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Heroic"]

def register(bot):

    @bot.message_handler(commands=['rob'])
    def rob(message):

        # reply check
        if not message.reply_to_message:
            bot.reply_to(message, "Reply to a user to rob.")
            return

        attacker_id = message.from_user.id
        target_id = message.reply_to_message.from_user.id

        # self rob prevent
        if attacker_id == target_id:
            bot.reply_to(message, "❌ You can't rob yourself.")
            return

        attacker = users.find_one({"id": attacker_id})
        target = users.find_one({"id": target_id})

        # user exist check
        if not attacker or not target:
            bot.reply_to(message, "User data not found. Ask them to /start the bot.")
            return

        attacker_rank = RANKS_ORDER.index(attacker["rank"])
        target_rank = RANKS_ORDER.index(target["rank"])

        # rank check
        if target_rank > attacker_rank:
            bot.reply_to(message, "❌ You cannot rob a higher rank player.")
            return

        # target money check
        if target["money"] <= 0:
            bot.reply_to(message, "💸 Target has no money to rob.")
            return

        # rob amount
        robbed_amount = min(target["money"], 500 + attacker_rank * 100)

        # update money
        users.update_one(
            {"id": target_id},
            {"$inc": {"money": -robbed_amount}}
        )

        users.update_one(
            {"id": attacker_id},
            {"$inc": {"money": robbed_amount}}
        )

        # add xp
        xp_rank.add_xp(attacker_id, 30)

        bot.reply_to(
            message,
            f"💰 You robbed **{robbed_amount} coins** from {message.reply_to_message.from_user.first_name}!"
        )
