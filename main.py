import telebot
from config import BOT_TOKEN
from keep_alive import keep_alive
from database import blocked

from commands import start, help, status, attack, kill, rob, give, bank, claim, shield, block, leaderboard, addmoney
from systems import shop, inventory
from systems.chat_reward import process_chat   # ← yaha import

bot = telebot.TeleBot(BOT_TOKEN)

# Register commands
start.register(bot)
help.register(bot)
status.register(bot)
attack.register(bot)
kill.register(bot)
rob.register(bot)
give.register(bot)
bank.register(bot)
claim.register(bot)
shield.register(bot)
block.register(bot)
leaderboard.register(bot)
addmoney.register(bot)

shop.register(bot)
inventory.register(bot)

# Chat reward system
@bot.message_handler(func=lambda m: True)
def chat_handler(message):

    process_chat(
        message.from_user.id,
        message.from_user.first_name
    )

# Start keep alive server
keep_alive()

print("Bot is running...")

bot.infinity_polling(skip_pending=True)
