import random
import telebot
from telebot import types

from config import TOKEN

print("~~~ Бот запущен ~~~")
# pip install pyTelegramBotAPI

# Импорт библиотеки


# связываю прогу с ботом по ТОКЕНУ - в кавычках оязательно
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['game'])
def game_reply(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    markup.row(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Выбери ответ:", reply_markup=markup)


# бот ожидает ответ
bot.infinity_polling()
