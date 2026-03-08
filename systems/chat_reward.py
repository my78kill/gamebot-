from database import users
from systems.anti_spam import is_spam
import time

def process_chat(user_id, name):

    # spam check
    spam_time = is_spam(user_id)

    if spam_time:
        users.update_one(
            {"id": user_id},
            {"$set": {"blocked_until": spam_time}}
        )
        return "🚫 Spam detected! You are blocked for 6 hours."

    user = users.find_one({"id": user_id})

    if not user:
        users.insert_one({
            "id": user_id,
            "name": name,
            "health": 100,
            "money": 0,
            "bank": 0,
            "xp": 0,
            "rank": "Bronze",
            "guns": [],
            "bandage": 0,
            "medkit": 0,
            "shield": 0,
            "chat": 0,
            "blocked_until": 0
        })
        user = users.find_one({"id": user_id})

    # block check
    if user.get("blocked_until", 0) > time.time():
        return None

    # 1 coin per message
    users.update_one(
        {"id": user_id},
        {
            "$inc": {
                "money": 1,
                "chat": 1
            }
        }
    )

    return None
