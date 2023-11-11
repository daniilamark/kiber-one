import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

stage = 0
print("~~~ Бот запущен ~~~")


@bot.message_handler(commands=['start'])
def start_quest(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton(text='Попытаться обойти его',
                                          callback_data='Вариант 1-1')
    itembtn2 = types.InlineKeyboardButton(text='Пойти вглубь леса', callback_data='Вариант 1-2')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id,
                     "Вы просыпаетесь на окраине леса и не понимаете как здесь оказались. "
                     "Вы думаете, что нужно как-то вернуться домой, но что-то притягивает вас вглубь зарослей.",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answering(call):
    if stage == 0:
        quest_stage1(call.message, call.data)
    elif stage == 1:
        quest_stage2(call.message, call.data)
    elif stage == 2:
        quest_stage3(call.message, call.data)
    elif stage == 3:
        quest_stage4(call.message, call.data)
    elif stage == 4:
        quest_stage5(call.message, call.data)


def quest_stage1(message, variant):
    if variant == "Вариант 1-1":
        # bot.send_message(message.chat.id, "Кругом одни болота...")
        markup = types.InlineKeyboardMarkup(row_width=1)
        itembtn1 = types.InlineKeyboardButton(text='Найти палку',
                                              callback_data='Вариант 1-3')
        itembtn2 = types.InlineKeyboardButton(text='Вернуться в лес', callback_data='Вариант 1-4')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id,
                         "Кругом одни болота...",
                         reply_markup=markup)

    elif variant == "Вариант 1-2":
        bot.send_message(message.chat.id, "В вас начали кидаться шишками белки")
        global stage
        stage = 1

    elif variant == "Вариант 1-3":
        bot.send_message(message.chat.id, "Вариант 1-3")
    elif variant == "Вариант 1-4":
        bot.send_message(message.chat.id, "Вариант 1-4")





def quest_stage2(message, variant):
    bot.send_message(message.chat.id, "2 уровень")


def quest_stage3(message, variant):
    pass


def quest_stage4(message, variant):
    pass


def quest_stage5(message, variant):
    pass


bot.infinity_polling()
