from telebot import TeleBot

# TOKEN = "8418024003:AAGJiRQSK1TPoSlG2eboH80FBoNJZzWEIis"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)


bot.infinity_polling()