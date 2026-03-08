import telebot
from config import BOT_TOKEN
from keep_alive import keep_alive

from commands import start, help, status, attack, kill, rob, give, bank, claim, shield, block
from systems import shop, inventory, xp_rank, chat_reward, anti_spam

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

shop.register(bot)
inventory.register(bot)

keep_alive()
bot.infinity_polling()
