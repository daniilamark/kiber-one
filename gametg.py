import random
import telebot
from telebot import types

from config import TOKEN

print("~~~ Бот запущен ~~~")
# pip install pyTelegramBotAPI

# связываю прогу с ботом по ТОКЕНУ - в кавычках оязательно
bot = telebot.TeleBot(TOKEN)
answer_pool = ["Камень", "Ножницы", "Бумага"]


@bot.message_handler(commands=['game'])
def game_reply(message):
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton(text='Камень', callback_data='Камень')
    itembtn2 = types.InlineKeyboardButton(text='Ножницы', callback_data='Ножницы')
    itembtn3 = types.InlineKeyboardButton(text='Бумага', callback_data='Бумага')
    itembtn4 = types.InlineKeyboardButton(text='Заново', callback_data='Заново')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выбери ответ:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answering(call):
    if call.data == "Заново":
        game_reply(call.message)
        return

    bot_answer = answer_pool[random.randint(0, 2)]
    bot.send_message(call.message.chat.id, 'мой ответ: ' + bot_answer)
    result = answer_pool.index(call.data) - answer_pool.index(bot_answer)
    if result == -1 or result == 2:
        bot.send_message(call.message.chat.id, "Ты выиграл")
    elif result == 0:
        bot.send_message(call.message.chat.id, "Ничья")
    else:
        bot.send_message(call.message.chat.id, "Я выиграл")
    bot.send_message(call.message.chat.id, '🎮')


# бот ожидает ответ
bot.infinity_polling()
