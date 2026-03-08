from database import users

def register(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        user = users.find_one({"id": message.from_user.id})
        if not user:
            users.insert_one({
                "id": message.from_user.id,
                "name": message.from_user.first_name,
                "money": 1000,
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
        bot.reply_to(message, f"""
🎮 Welcome {message.from_user.first_name} to Battle Game Bot!

⚔ Attack players, kill, rob
🏦 Bank system, claim daily
🛒 Shop & buy guns/medico/shields
💬 Chat reward system

Type !help to see all commands
""")