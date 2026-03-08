def register(bot):

    @bot.message_handler(commands=['help'])
    def help_cmd(message):

        bot.reply_to(message, """
📖 **Battle Game Commands**

⚔ **Combat**
/attack - Attack a player using your gun
/kill - Instantly kill a player (requires AWM)
/rob - Steal money from another player

💰 **Economy**
/give - Send money to another player
/deposit - Store money in bank
/withdraw - Take money from bank
/claim - Claim daily reward

🛒 **Shop & Items**
/shop - View shop items
/use bandage - Heal 50 HP
/use medkit - Fully restore health

🛡 **Protection**
/shield - Activate protection shield

📊 **Player Info**
/status - View your profile
/leaderboard - See richest players

👑 **Admin**
/block - Block a user from the game
""")
