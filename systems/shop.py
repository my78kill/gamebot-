from database import users

guns = {
    "knife": {"price": 500, "damage": 10},
    "pistol": {"price": 2000, "damage": 40},
    "akm": {"price": 8000, "damage": 60},
    "awm": {"price": 12000, "damage": 100}
}

MEDICO = {
"bandage":{"price":1000,"heal":50},
"medkit":{"price":5000,"heal":100}
}

SHIELDS = {"1d":500,"3d":800,"7d":3000}

def register(bot):
    @bot.message_handler(commands=['shop'])
    def shop_cmd(message):
        bot.reply_to(message,
f"""
🛒 SHOP
🔫 Guns
Pistol - 2000 (40 dmg)
AKM - 8000 (60 dmg)
AWM - 12000 (100 dmg)

💊 Medico
Bandage - 1000 (Heal 50)
Medkit - 5000 (Heal 100)

🛡 Shield
1 Day - 500
3 Days - 800
7 Days - 3000

Buy using:
/buy item
""")
