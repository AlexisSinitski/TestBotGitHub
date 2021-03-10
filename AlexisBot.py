import telebot

import config
login(config.username)

bot = telebot.TeleBot('username')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты отправил мне сообщение /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой повелитель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, мой создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAMLYEPAlVRtudKWRDLzRStf9-4XUfcAAlgJAAK_jJAEAb1ed8oNPLQeBA')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
