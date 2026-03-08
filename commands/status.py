from database import users

def register(bot):
    @bot.message_handler(commands=['status'])
    def status(message):
        user = users.find_one({"id": message.from_user.id})
        bot.reply_to(message,
f"""
👤 Name: {user['name']}
❤️ Health: {user['health']}
💰 Money: {user['money']}
🏦 Bank: {user['bank']}
🔫 Guns: {user['guns']}
💊 Medico: Bandage({user['bandage']}), Medkit({user['medkit']})
🛡 Shield: {user['shield']}
🏆 Rank: {user['rank']}
⭐ XP: {user['xp']}
""")