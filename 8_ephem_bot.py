"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
from datetime import date

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)
planet = 0

planet_dict = {
    'mercury': ephem.Mercury,
    'venus': ephem.Venus,
    'mars': ephem.Mars,
    'jupiter': ephem.Jupiter,
    'saturn': ephem.Saturn,
    'uranus': ephem.Uranus,
    'neptune': ephem.Neptune,
}


def greet_user(update, context):
    print('/start command initiated')
    update.message.reply_text('Hello dear friend! You have called the "/start" command')


def check_planet(update, context):
    print('/planet command initiated')
    update.message.reply_text('Please define a planet name and I can tell you where it is located.')
    global planet
    planet = 1


def talk_to_me(update, context):
    user_text = update.message.text
    global planet
    print(user_text)
    if planet:
        if planet_dict.get(user_text.lower(), 0) != 0:
            const = ephem.constellation(planet_dict[user_text.lower()](date.today()))[1]
            const = f'{user_text.capitalize()} is currently ({date.today()}) at {const}'
        else:
            const = 'There is no such planet'
        update.message.reply_text(const)
        planet = 0
    else:
        update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', check_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    print('I have been started')
    logging.info('Bot is initiated')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
