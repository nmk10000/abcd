import telebot

bot = telebot.TeleBot("1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  bot.reply_to(message, message.text)
