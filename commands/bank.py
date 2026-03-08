from database import users
from systems import xp_rank

def register(bot):
    @bot.message_handler(commands=['deposit','withdraw'])
    def bank(message):
        cmd = message.text.split()[0].lower()
        try:
            amount = int(message.text.split()[1])
        except:
            bot.reply_to(message,"Usage: /deposit or /withdraw amount")
            return

        user = users.find_one({"id": message.from_user.id})

        if cmd == "/deposit":
            if user["money"] < amount:
                bot.reply_to(message,"Not enough cash!")
                return
            users.update_one({"id":message.from_user.id},{"$inc":{"money":-amount,"bank":amount}})
        else:
            if user["bank"] < amount:
                bot.reply_to(message,"Not enough in bank!")
                return
            users.update_one({"id":message.from_user.id},{"$inc":{"money":amount,"bank":-amount}})

        xp_rank.add_xp(message.from_user.id, 2)
        bot.reply_to(message,f"🏦 {cmd[1:].capitalize()} successful: {amount} coins")