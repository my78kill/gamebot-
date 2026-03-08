from database import users

def register(bot):

    @bot.message_handler(commands=['use'])
    def use(message):

        args = message.text.split()

        if len(args) < 2:
            return bot.reply_to(message,"Usage: /use bandage")

        item = args[1].lower()

        user = users.find_one({"id":message.from_user.id})

        if item == "bandage":

            if user["bandage"] <= 0:
                return bot.reply_to(message,"No bandage.")

            users.update_one({"id":user["id"]},{
                "$inc":{"health":50,"bandage":-1}
            })

            bot.reply_to(message,"🩹 Bandage used +50 HP")

        elif item == "medkit":

            if user["medkit"] <= 0:
                return bot.reply_to(message,"No medkit.")

            users.update_one({"id":user["id"]},{
                "$set":{"health":100},
                "$inc":{"medkit":-1}
            })

            bot.reply_to(message,"❤️ Medkit used full heal")
