from database import users
from systems import xp_rank

def register(bot):

    @bot.message_handler(commands=['give'])
    def give(message):

        if not message.reply_to_message:
            bot.reply_to(message, "⚠ Reply to a user to give money\nUsage: /give amount")
            return

        try:
            amount = int(message.text.split()[1])
        except:
            bot.reply_to(message, "⚠ Usage: /give amount")
            return

        if amount <= 0:
            bot.reply_to(message, "❌ Amount must be greater than 0")
            return

        giver_id = message.from_user.id
        receiver_id = message.reply_to_message.from_user.id

        if giver_id == receiver_id:
            bot.reply_to(message, "❌ You cannot give money to yourself")
            return

        giver = users.find_one({"id": giver_id})

        if not giver or giver["money"] < amount:
            bot.reply_to(message, "💸 Not enough money!")
            return

        receiver = users.find_one({"id": receiver_id})

        if not receiver:
            users.insert_one({
                "id": receiver_id,
                "name": message.reply_to_message.from_user.first_name,
                "money": 0,
                "bank": 0,
                "health": 100,
                "xp": 0,
                "rank": "Bronze",
                "guns": [],
                "bandage": 0,
                "medkit": 0,
                "shield": 0,
                "chat": 0
            })

        users.update_one({"id": giver_id}, {"$inc": {"money": -amount}})
        users.update_one({"id": receiver_id}, {"$inc": {"money": amount}})

        xp_rank.add_xp(giver_id, 5)

        bot.reply_to(
            message,
            f"💰 {message.from_user.first_name} gave {amount} coins to {message.reply_to_message.from_user.first_name}"
        )
