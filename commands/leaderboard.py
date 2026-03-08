from database import users

def register(bot):

    @bot.message_handler(commands=['leaderboard'])
    def leaderboard(message):

        top = users.find().sort("money",-1).limit(10)

        text = "🏆 Global Leaderboard\n\n"

        rank = 1
        for u in top:
            text += f"{rank}. {u['name']} - 💰 {u['money']}\n"
            rank += 1

        bot.reply_to(message,text)
