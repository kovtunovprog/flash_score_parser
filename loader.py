import telebot
import logging

from data import config


bot = telebot.TeleBot(config.BOT_TOKEN)

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)


