from database import users
import time
from systems import xp_rank

def register(bot):
    @bot.message_handler(commands=['claim'])
    def claim(message):
        user = users.find_one({"id":message.from_user.id})
        now = time.time()
        last = user.get("last_claim",0)
        if now - last < 86400:
            bot.reply_to(message,"⏳ You already claimed today")
            return
        users.update_one({"id":message.from_user.id},{"$inc":{"money":100},"$set":{"last_claim":now}})
        xp_rank.add_xp(message.from_user.id, 20)
        bot.reply_to(message,"🎁 Claimed 100 coins for today!")