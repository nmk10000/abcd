import telebot
from telebot import types

TOKEN = '1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI'
bot = telebot.TeleBot(TOKEN)

def extract_unique_code(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None


def in_storage(unique_code):
    # (pseudo-code) Should check if a unique code exists in storage
    return True


def get_username_from_storage(unique_code):
    # (pseudo-code) Does a query to the storage, retrieving the associated username
    # Should be replaced by a real database-lookup.
    return "ABC" if in_storage(unique_code) else None


def save_chat_id(chat_id, username):
    # (pseudo-code) Save the chat_id->username to storage
    # Should be replaced by a real database query.
    pass


@bot.message_handler(commands=['start'])
def send_welcome(message):
    unique_code = extract_unique_code(message.text)
    if unique_code:  # if the '/start' command contains a unique_code
        username = get_username_from_storage(unique_code)
        if username:  # if the username exists in our database
            save_chat_id(message.chat.id, username)
            reply = "Hello {0}, how are you?".format(username)
        else:
            reply = "I have no clue who you are..."
    else:
        reply = "Please visit me via a provided URL from the website."
    bot.reply_to(message, reply)


bot.polling()
