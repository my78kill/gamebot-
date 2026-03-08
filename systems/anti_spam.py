import time

spam = {}

def check(user_id):

    now = time.time()

    if user_id not in spam:
        spam[user_id] = []

    spam[user_id].append(now)

    spam[user_id] = [t for t in spam[user_id] if now-t < 5]

    if len(spam[user_id]) > 7:
        return now + 21600

    return None
