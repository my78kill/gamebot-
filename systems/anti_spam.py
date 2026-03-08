import time

user_last_message = {}

SPAM_TIME = 1.5
BLOCK_TIME = 6 * 60 * 60  # 6 hours

def is_spam(user_id):

    now = time.time()

    last = user_last_message.get(user_id)

    if last and (now - last) < SPAM_TIME:
        return now + BLOCK_TIME

    user_last_message[user_id] = now

    return None
