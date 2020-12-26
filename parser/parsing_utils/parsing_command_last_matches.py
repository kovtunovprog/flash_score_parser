import logging
import time


def parsing_command_last_matches(web_driver, command: int, period: int):
    """
    Проводит парсинг результатов последних матчей комманд по периодам
    :param web_driver:
    :param command:
    :param period:
    :return:
    """
    logging.info('Парсинг последних матчей комманд')
    time.sleep(5)
    command_period_result = None
    wrappers = web_driver.find_elements_by_class_name('h2h-wrapper')
    if command == 1:
        command_1 = wrappers[0].find_element_by_xpath("//tbody/tr[1]/td[5]/span")
        web_driver.execute_script("arguments[0].click();", command_1)

    if command == 2:
        command_2 = wrappers[1].find_element_by_xpath("//tbody/tr[1]/td[5]/span")
        web_driver.execute_script("arguments[0].click();", command_2)
    time.sleep(5)
    window = web_driver.window_handles[2]
    web_driver.switch_to.window(window)

    time.sleep(5)
    sum_content = web_driver.find_element_by_id('tab-match-summary')
    period_result = sum_content.find_elements_by_class_name("detailMS__headerScore")
    if period == 1:
        command_period_result = period_result[0].text
    if period == 2:
        command_period_result = period_result[0].text
    if period == 3:
        command_period_result = period_result[0].text

    window = web_driver.window_handles[1]
    web_driver.close()
    web_driver.switch_to.window(window)
    return command_period_result
