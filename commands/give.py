from database import users
from systems import xp_rank

def register(bot):
    @bot.message_handler(commands=['give'])
    def give(message):
        if not message.reply_to_message:
            bot.reply_to(message,"Reply to a user to give money")
            return

        try:
            amount = int(message.text.split()[1])
        except:
            bot.reply_to(message,"Usage: !give amount")
            return

        giver = users.find_one({"id": message.from_user.id})
        if giver["money"] < amount:
            bot.reply_to(message,"Not enough money!")
            return

        receiver_id = message.reply_to_message.from_user.id
        users.update_one({"id": message.from_user.id},{"$inc":{"money": -amount}})
        users.update_one({"id": receiver_id},{"$inc":{"money": amount}})

        xp_rank.add_xp(message.from_user.id, 5)

        bot.reply_to(message,f"💰 You gave {amount} coins")