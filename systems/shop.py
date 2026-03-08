from database import users

guns = {
    "knife": {"price": 500, "damage": 10},
    "pistol": {"price": 2000, "damage": 40},
    "akm": {"price": 8000, "damage": 60},
    "awm": {"price": 12000, "damage": 100}
}

MEDICO = {
    "bandage": {"price": 1000, "heal": 50},
    "medkit": {"price": 5000, "heal": 100}
}

SHIELDS = {
    "shield1": 500,
    "shield3": 800,
    "shield7": 3000
}

def register(bot):

    @bot.message_handler(commands=['shop'])
    def shop_cmd(message):

        bot.reply_to(message,
"""
🛒 SHOP

🔫 Guns
knife - 500 (10 dmg)
pistol - 2000 (40 dmg)
akm - 8000 (60 dmg)
awm - 12000 (100 dmg)

💊 Medico
bandage - 1000 (heal 50)
medkit - 5000 (heal 100)

🛡 Shield
shield1 - 500 (1 day)
shield3 - 800 (3 days)
shield7 - 3000 (7 days)

Buy using:
/buy item
"""
)

    @bot.message_handler(commands=['buy'])
    def buy_item(message):

        args = message.text.split()

        if len(args) < 2:
            bot.reply_to(message, "Usage: /buy item")
            return

        item = args[1].lower()

        user = users.find_one({"id": message.from_user.id})

        if not user:
            bot.reply_to(message, "Use /start first")
            return

        money = user.get("money", 0)

        # BUY GUN
        if item in guns:

            price = guns[item]["price"]

            if money < price:
                bot.reply_to(message, "💸 Not enough money")
                return

            users.update_one(
                {"id": message.from_user.id},
                {
                    "$inc": {"money": -price},
                    "$push": {"guns": item}
                }
            )

            bot.reply_to(message, f"🔫 You bought {item}")

        # BUY MEDICO
        elif item in MEDICO:

            price = MEDICO[item]["price"]

            if money < price:
                bot.reply_to(message, "💸 Not enough money")
                return

            users.update_one(
                {"id": message.from_user.id},
                {
                    "$inc": {
                        "money": -price,
                        item: 1
                    }
                }
            )

            bot.reply_to(message, f"💊 You bought {item}")

        # BUY SHIELD
        elif item in SHIELDS:

            price = SHIELDS[item]

            if money < price:
                bot.reply_to(message, "💸 Not enough money")
                return

            users.update_one(
                {"id": message.from_user.id},
                {
                    "$inc": {"money": -price, "shield": 1}
                }
            )

            bot.reply_to(message, "🛡 Shield activated")

        else:
            bot.reply_to(message, "❌ Item not found")
