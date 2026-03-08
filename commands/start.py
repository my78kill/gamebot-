from database import users
import time

def register(bot):

    @bot.message_handler(commands=['start'])
    def start_cmd(message):

        user_id = message.from_user.id
        name = message.from_user.first_name

        user = users.find_one({"id": user_id})

        if not user:
            users.insert_one({
                "id": user_id,
                "name": name,
                "money": 1000,
                "bank": 0,
                "health": 100,
                "xp": 0,
                "rank": "Bronze",
                "guns": [],
                "bandage": 0,
                "medkit": 0,
                "shield": 0,
                "dead_until": 0,
                "chat": 0
            })

        bot.reply_to(message, f"""
🎮 **Welcome to Battle Arena**

Hello **{name}** 👋

🔥 **Game Features**
• Attack other players
• Rob money from enemies
• Kill players with powerful guns
• Buy weapons & healing items
• Rank system with XP
• Global leaderboard
• Bank system

⚔ **Start your journey now!**

Type **/help** to see all commands.
""")
