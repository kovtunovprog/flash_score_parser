import logging

from parser import selenium_parsing


def parsing_process():
    logging.info('Начинаю парсинг')
    while True:
        selenium_parsing()
