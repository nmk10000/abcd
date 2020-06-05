import telebot
from telebot import types

TOKEN = '1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI'
bot = telebot.TeleBot(TOKEN)

kb = types.InlineKeyboardMarkup(row_width=2)

words = {
'Meager' : 'Lacking in quantity',
'Asylum' : 'Shelter',
'Irk' : 'To annoy',
'Kudos' : 'Great glory'
}


def compare(message, word, definition):
    if definition == words[word]:
        bot.send_message(message.from_user.id, 'Correct!')
    else:
        bot.send_message(message.from_user.id, 'Wrong!')


for item in words.items():
    kb.add(types.InlineKeyboardButton(item[0], callback_data = item[0]))



@bot.message_handler(commands=['start', 's'])
def post_random_article(message):
    word = 'Meager'
    bot.send_message(message.from_user.id, word, reply_markup = kb)

bot.polling()
