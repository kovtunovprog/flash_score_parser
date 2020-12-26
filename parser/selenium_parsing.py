import logging
import time

from selenium import webdriver

from data.config import parsing_url
from parser.parsing_utils import check_period_results
from parser.parsing_utils import parsing_command_last_matches
from utils.notify_admins import parsing_notify


def selenium_parsing():
    """
    Основная функция парсинга, в случае
    :return:
    """
    web_driver = webdriver.Chrome()
    try:
        logging.info('Старт сессии парсинга')
        web_driver.get(parsing_url)
        period = None

        live_button = web_driver.find_element_by_xpath("//div[@class='tabs__tab' or @class='selected']")
        live_button.click()
        logging.info('Переход к LIVE-матчам')
        matches_id_dict = {}
        matches = web_driver.find_elements_by_class_name('event__match')

        for match in matches:
            period = check_period_results(match)
            if period:
                matches_id_dict[match.get_attribute('id')] = period

        if matches_id_dict:
            for match_id, period_num in matches_id_dict.items():
                time.sleep(2)
                match = web_driver.find_element_by_id(match_id)
                web_driver.execute_script("arguments[0].click();", match)

                window = web_driver.window_handles[1]
                web_driver.switch_to.window(window)
                logging.info('Меняем окно')

                h2b = web_driver.find_element_by_id('a-match-head-2-head')
                web_driver.execute_script("arguments[0].click();", h2b)
                logging.info('Переходим к H2H')

                time.sleep(1)
                command_last_match_period_result_1 = parsing_command_last_matches(web_driver, 1, period)
                logging.info('Переходим на страницу подробной информации о последней игре команды 1')
                web_driver.back()

                command_last_match_period_result_2 = parsing_command_last_matches(web_driver, 1, period)
                logging.info('Переходим на страницу подробной информации о последней игре команды 2')
                web_driver.back()
                logging.info('Возвращаемся к H2H')

                if str(command_last_match_period_result_1) == '0 - 0' \
                        or str(command_last_match_period_result_2) == '0 - 0':
                    logging.info(f'Отправка сообщения в телеграм по игре {web_driver.current_url}')
                    parsing_notify(web_driver.current_url)

                logging.info('Возвращаемся к LIVE-резултатам матча')

                window = web_driver.window_handles[0]
                web_driver.close()
                web_driver.switch_to.window(window)
    except Exception as err:
        logging.info(err)
    web_driver.close()
