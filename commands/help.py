def register(bot):
    @bot.message_handler(commands=['help'])
    def help_cmd(message):
        bot.reply_to(message,
"""
🎮 Game Commands:
/status
/attack
/kill
/rob
/give
/deposit / /withdraw
/claim

🛒 Shop:
/shop
/use bandage
/use medkit

🛡 Protection:
/shield

Admin Commands:
/block
""")
