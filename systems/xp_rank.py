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

    if not user:
        return None

    current_xp = user.get("xp", 0)
    current_rank = user.get("rank", "Bronze")

    new_xp = current_xp + amount
    new_rank = current_rank

    for rank_name, xp_required in reversed(RANKS):
        if new_xp >= xp_required:
            new_rank = rank_name
            break

    users.update_one(
        {"id": user_id},
        {"$set": {"xp": new_xp, "rank": new_rank}}
    )

    # check if rank changed
    if new_rank != current_rank:
        return new_xp, new_rank, True

    return new_xp, new_rank, False
