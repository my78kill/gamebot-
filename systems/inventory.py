from database import users

def register(bot):

    @bot.message_handler(commands=['use'])
    def use_item(message):

        args = message.text.split()

        if len(args) < 2:
            bot.reply_to(message, "⚠ Usage: /use bandage or /use medkit")
            return

        item = args[1].lower()
        user = users.find_one({"id": message.from_user.id})

        if not user:
            bot.reply_to(message, "❌ Use /start first")
            return

        health = user.get("health", 100)

        if item == "bandage":

            if user.get("bandage", 0) < 1:
                bot.reply_to(message, "💊 You don't have a bandage!")
                return

            heal = 50
            new_health = min(100, health + heal)
            actual_heal = new_health - health

            users.update_one(
                {"id": message.from_user.id},
                {"$set": {"health": new_health}, "$inc": {"bandage": -1}}
            )

            bot.reply_to(
                message,
                f"💊 Bandage used! Health +{actual_heal}\n❤️ Health: {new_health}/100"
            )

        elif item == "medkit":

            if user.get("medkit", 0) < 1:
                bot.reply_to(message, "🧰 You don't have a medkit!")
                return

            heal = 100
            new_health = min(100, health + heal)
            actual_heal = new_health - health

            users.update_one(
                {"id": message.from_user.id},
                {"$set": {"health": new_health}, "$inc": {"medkit": -1}}
            )

            bot.reply_to(
                message,
                f"🧰 Medkit used! Health +{actual_heal}\n❤️ Health: {new_health}/100"
            )

        else:
            bot.reply_to(message, "❌ Unknown item\nUse: /use bandage or /use medkit")
