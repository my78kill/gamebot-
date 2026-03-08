from database import users
from systems.anti_spam import is_spam
from systems.xp_rank import add_xp

CHAT_LIMIT = 500
REWARD = 1000

def process_chat(user_id, name):

    # spam check
    if is_spam(user_id):
        return

    user = users.find_one({"_id": user_id})

    if not user:
        users.insert_one({
            "_id": user_id,
            "name": name,
            "health": 100,
            "money": 0,
            "bank": 0,
            "xp": 0,
            "rank": "Bronze",
            "guns": [],
            "medico": {},
            "shield": 0,
            "chat_count": 0
        })
        user = users.find_one({"_id": user_id})

    chat_count = user.get("chat_count", 0) + 1

    # reward system
    if chat_count >= CHAT_LIMIT:
        users.update_one(
            {"_id": user_id},
            {
                "$inc": {
                    "money": REWARD
                },
                "$set": {
                    "chat_count": 0
                }
            }
        )

        add_xp(user_id, 10)
        return f"🎁 {name} ko 500 chats complete hone par **{REWARD} coins** mile!"

    else:
        users.update_one(
            {"_id": user_id},
            {
                "$set": {
                    "chat_count": chat_count
                }
            }
        )

    return None