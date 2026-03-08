import time
from database import users, blocked

user_messages = {}

def register(bot):
    @bot.message_handler(func=lambda m: True)
    def anti_spam(message):
        user_id = message.from_user.id
        if blocked.find_one({"id": user_id}):
            return

        now = time.time()
        if user_id not in user_messages:
            user_messages[user_id] = []
        user_messages[user_id].append(now)
        user_messages[user_id] = [t for t in user_messages[user_id] if now - t < 10]

        if len(user_messages[user_id]) > 8:
            blocked.insert_one({"id": user_id, "until": now + 18000}) # 5 hours block
            bot.reply_to(message,"🚫 Blocked for 5 hours due to spam!")
            user_messages[user_id] = []
            return

        # Chat reward pot
        user = users.find_one({"id": user_id})
        chats = user.get("chat",0) + 1
        reward = 0
        if chats >= 500:
            chats = 0
            reward = 1000
        users.update_one({"id":user_id},{"$set":{"chat":chats},"$inc":{"money":reward}})
        if reward:
            bot.reply_to(message,"🎁 500 chats completed! You got 1000 coins")