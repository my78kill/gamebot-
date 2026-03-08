from database import users
from systems import xp_rank

def register(bot):

    @bot.message_handler(commands=['deposit', 'withdraw'])
    def bank(message):

        parts = message.text.split()

        if len(parts) < 2:
            bot.reply_to(message, "⚠ Usage:\n/deposit amount\n/withdraw amount")
            return

        cmd = parts[0].lower()

        try:
            amount = int(parts[1])
        except:
            bot.reply_to(message, "❌ Amount must be a number")
            return

        if amount <= 0:
            bot.reply_to(message, "❌ Amount must be greater than 0")
            return

        user = users.find_one({"id": message.from_user.id})

        if not user:
            bot.reply_to(message, "❌ Use /start first")
            return

        if cmd == "/deposit":

            if user["money"] < amount:
                bot.reply_to(message, "💸 Not enough cash!")
                return

            users.update_one(
                {"id": message.from_user.id},
                {"$inc": {"money": -amount, "bank": amount}}
            )

            bot.reply_to(message, f"🏦 Deposited {amount} coins")

        elif cmd == "/withdraw":

            if user["bank"] < amount:
                bot.reply_to(message, "🏦 Not enough money in bank!")
                return

            users.update_one(
                {"id": message.from_user.id},
                {"$inc": {"money": amount, "bank": -amount}}
            )

            bot.reply_to(message, f"🏦 Withdrawn {amount} coins")

        xp_rank.add_xp(message.from_user.id, 2)
