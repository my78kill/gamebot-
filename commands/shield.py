from database import users
from systems import xp_rank

def register(bot):
    @bot.message_handler(commands=['shield'])
    def shield(message):
        user = users.find_one({"id": message.from_user.id})
        if user["money"] < 500:
            bot.reply_to(message,"Not enough coins for shield")
            return
        users.update_one({"id": message.from_user.id},{"$inc":{"money":-500,"shield":1}})
        xp_rank.add_xp(message.from_user.id, 5)
        bot.reply_to(message,"🛡 Shield activated! You are protected")