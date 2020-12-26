import logging

from data.config import admins
from loader import bot


def on_startup_notify():
    for admin in admins:
        try:
            bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)


def parsing_notify(results):
    for admin in admins:
        try:
            bot.send_message(admin, results)

        except Exception as err:
            logging.exception(err)
