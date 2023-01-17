from config import settings

import telebot

from telebot import types

bot = telebot.TeleBot(token=settings['TOKEN'], parse_mode='html')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_photo(message.chat.id,
                   photo=settings['photo_hello'],
                   caption=settings['caption_hello'.format(message.from_user)],
                   )

# https://t.me/studentsuperhttps://t.me/+e7cXDs8cJd0xZThi

@bot.chat_member_handler()
def chat_member_handler(message: telebot.types.Message):
    status = message.new_chat_member.status

    if status == 'left':
        bot.send_photo(photo=settings['photo_leave'],
                       chat_id=message.new_chat_member.user.id,
                       caption=settings['caption_leave'])

@bot.message_handler(content_types=['text'])
def send_message(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Вернуться на канал!", url='https://t.me/studentsuper')
    markup.add(button1)
    bot.send_photo(message.chat.id,
                   photo=settings['photo_answer'],
                   caption=settings['caption_answer'],
                   reply_markup=markup
                   )

bot.infinity_polling(allowed_updates=telebot.util.update_types)
