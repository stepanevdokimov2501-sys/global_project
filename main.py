import telebot
import random
from config import token
from logic import *

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Я бот, который рассказывает о глобальном потеплении и помогает узнать, как с ним бороться.

Мои команды:
/info - информация о потеплении
/causes - причины потепления
/effects - последствия
/solutions - способы борьбы
/tips - полезные советы
/fact - рандомные факты
""")


@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, """\
Глобальное потепление - это постепенное повышение средней температуры на Земле.

Главная причина этой проблемы - увеличение количества парниковых газов в атмосфере.Из-за этого меняется климат планеты.
""")


@bot.message_handler(commands=['causes'])
def causes(message):
    bot.reply_to(message, """\
Основные причины глобального потепления:

1. Выбросы заводов и предприятий.
2. Выхлопные газы автомобилей.
3. Вырубка лесов.
4. Сжигание угля, нефти и газа.
5. Сельское хозяйство.
""")


@bot.message_handler(commands=['effects'])
def effects(message):
    bot.reply_to(message, """\
Последствия глобального потепления:

1. Таяние ледников.
2. Повышение уровня океана.
3. Засухи и жара.
4. Лесные пожары.
5. Изменение климата.
6. Ухудшение условий жизни животных.
""")


@bot.message_handler(commands=['solutions'])
def solutions(message):
    bot.reply_to(message, """\
Как бороться с глобальным потеплением:

1. Использовать солнечную и ветровую энергию.
2. Сажать деревья.
3. Меньше пользоваться автомобилями.
4. Экономить электричество.
5. Перерабатывать отходы.
6. Защищать леса.
""")


@bot.message_handler(commands=['tips'])
def tips(message):
    bot.reply_to(message, """\
Несколько полезных советов:

1. Выключай свет, когда выходишь из комнаты.
2. Не оставляй мусор на улице.
3. Используй многоразовые пакеты.
4. Экономь воду.
5. По возможности ходи пешком.
6. Сортируй мусор.
""")


@bot.message_handler(commands=["fact"])
def random_fact(message):
    bot.reply_to(message, f"Интересный факт: {get_fact()}")


bot.infinity_polling()
