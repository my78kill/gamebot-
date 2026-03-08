from database import users

RANKS = [
    ("Bronze", 0),
    ("Silver", 100),
    ("Gold", 300),
    ("Platinum", 700),
    ("Diamond", 1500),
    ("Heroic", 3000)
]

def add_xp(user_id, amount):
    user = users.find_one({"id": user_id})
    new_xp = user.get("xp", 0) + amount
    new_rank = user.get("rank","Bronze")
    for rank_name, xp_required in reversed(RANKS):
        if new_xp >= xp_required:
            new_rank = rank_name
            break
    users.update_one({"id": user_id},{"$set":{"xp": new_xp, "rank": new_rank}})
    return new_xp, new_rank