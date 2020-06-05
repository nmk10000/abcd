import telebot

bot = telebot.TeleBot("1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
