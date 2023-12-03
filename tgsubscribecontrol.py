import telebot
from telebot.apihelper import ApiTelegramException

bot = telebot.TeleBot("Bot Token Giriniz")

CHAT_ID = -10... #grup idsi giriniz.

def is_subscribed(chat_id, user_id):
    try:
        response = bot.get_chat_member(chat_id, user_id)
        if response.status == 'left':
            return False
        else:
            return True

    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: chat not found':
            return False



@bot.message_handler(commands=['start'])
def send_welcome(message):

    if not is_subscribed(CHAT_ID,message.chat.id):
        bot.send_message(message.chat.id, 'Please subscribe to the channel')
    else:
        bot.send_message(message.chat.id, 'You are subscribed')

bot.polling()