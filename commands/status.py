from database import users

def register(bot):

    @bot.message_handler(commands=['status'])
    def status(message):

        user = users.find_one({"id": message.from_user.id})

        if not user:
            bot.reply_to(message, "❌ You are not registered. Use /start first.")
            return

        guns = ", ".join(user.get("guns", []))
        if not guns:
            guns = "None"

        bot.reply_to(
            message,
f"""
👤 Name: {user.get('name')}
❤️ Health: {user.get('health')}
💰 Money: {user.get('money')}
🏦 Bank: {user.get('bank')}

🔫 Guns: {guns}

💊 Bandage: {user.get('bandage')}
🧰 Medkit: {user.get('medkit')}
🛡 Shield: {user.get('shield')}

🏆 Rank: {user.get('rank')}
⭐ XP: {user.get('xp')}
"""
        )
