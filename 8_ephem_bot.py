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


def greet_user(update, context):
    print('/start command initiated')
    update.message.reply_text('Hello dear friend! You have called the "/start" command')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    print('I have been started')
    logging.info('Bot is initiated')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    # main()
    # TODO unlock main()
    # TODO create dict {'mercury': ephem.mercury.....}
    # TODO call constellation as ephem.constellation(dict['mercury'](date.today()))

    m = ephem.Mars(date.today())
    print(ephem.constellation(m))

    dict = {'mars': ephem.Mars}
    const = ephem.constellation(dict['mars'](date.today()))
    print(const)
