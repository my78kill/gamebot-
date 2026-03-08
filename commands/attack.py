from database import users
import random
from systems import xp_rank

GUN_DAMAGE = {"pistol":40,"akm":60,"awm":100}

def register(bot):
    @bot.message_handler(commands=['attack'])
    def attack(message):
        if not message.reply_to_message:
            bot.reply_to(message,"Reply to a user to attack")
            return

        attacker = users.find_one({"id": message.from_user.id})
        if not attacker["guns"]:
            bot.reply_to(message,"No guns!")
            return

        target_id = message.reply_to_message.from_user.id
        target = users.find_one({"id": target_id})
        if target["shield"] > 0:
            bot.reply_to(message,"Target has shield! Cannot attack.")
            return

        gun = random.choice(attacker["guns"])
        damage = GUN_DAMAGE[gun]
        new_health = max(0, target["health"] - damage)
        users.update_one({"id": target_id},{"$set":{"health": new_health}})

        xp_rank.add_xp(message.from_user.id, 10)

        bot.reply_to(message,
f"""
⚔ Attack Successful!
Weapon: {gun}
Damage: {damage}
Target Health: {new_health}
""")