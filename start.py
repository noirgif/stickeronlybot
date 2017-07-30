import telebot

# specify token here
token = ""

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text", "photo", "audio"])
def delete_msg(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass

bot.polling()
