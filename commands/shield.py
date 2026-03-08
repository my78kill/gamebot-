from database import users
from systems import xp_rank

SHIELD_PRICE = 500

def register(bot):

    @bot.message_handler(commands=['shield'])
    def shield(message):

        user = users.find_one({"id": message.from_user.id})

        if not user:
            bot.reply_to(message, "❌ Use /start first")
            return

        if user.get("shield", 0) >= 1:
            bot.reply_to(message, "🛡 You already have an active shield")
            return

        if user.get("money", 0) < SHIELD_PRICE:
            bot.reply_to(message, "💸 Not enough coins for shield")
            return

        users.update_one(
            {"id": message.from_user.id},
            {"$inc": {"money": -SHIELD_PRICE, "shield": 1}}
        )

        xp_rank.add_xp(message.from_user.id, 5)

        bot.reply_to(message, "🛡 Shield activated! You are now protected.")
