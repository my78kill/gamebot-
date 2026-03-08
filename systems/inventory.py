from database import users

def register(bot):
    @bot.message_handler(commands=['use'])
    def use_item(message):
        args = message.text.split()
        if len(args) < 2:
            bot.reply_to(message,"Usage: /use item")
            return

        item = args[1].lower()
        user = users.find_one({"id": message.from_user.id})

        if item == "bandage":
            if user["bandage"] < 1:
                bot.reply_to(message,"No bandage!")
                return
            heal = 50
            new_health = min(100, user["health"] + heal)
            users.update_one({"id": message.from_user.id},{"$set":{"health":new_health},"$inc":{"bandage":-1}})
            bot.reply_to(message,f"💊 Used bandage! Health +{heal} ({new_health})")
        elif item == "medkit":
            if user["medkit"] < 1:
                bot.reply_to(message,"No medkit!")
                return
            heal = 100
            new_health = min(100, user["health"] + heal)
            users.update_one({"id": message.from_user.id},{"$set":{"health":new_health},"$inc":{"medkit":-1}})
            bot.reply_to(message,f"💊 Used medkit! Health +{heal} ({new_health})")
        else:
            bot.reply_to(message,"Unknown item")