import time

spam_tracker = {}

SPAM_LIMIT = 5
TIME_WINDOW = 3

def is_spam(user_id):
    now = time.time()

    if user_id not in spam_tracker:
        spam_tracker[user_id] = []

    spam_tracker[user_id].append(now)

    spam_tracker[user_id] = [
        t for t in spam_tracker[user_id] if now - t < TIME_WINDOW
    ]

    if len(spam_tracker[user_id]) > SPAM_LIMIT:
        return True

    return False


def register(bot):
    pass
