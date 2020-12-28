import logging
import time


def check_period_results(element):
    """
    Проверяет счет матча и время
    :param element:
    :return: bool
    """
    period = 0
    time.sleep(5)
    stage = element.find_element_by_class_name('event__stage--block')
    logging.info('LIVE: Проверка результатов в периоде конкретного матча')
    if 'период' in str(stage.text):
        period_str = stage.text[0]
        minutes = stage.text[10:]
        period_1_condition = str(period_str) == '1'
        period_2_condition = str(period_str) == '2'
        period_3_condition = str(period_str) == '3'

        minutes_condition = 8 < int(minutes) < 12

        if not period_1_condition and not period_2_condition and not period_3_condition:
            return False
        if period_1_condition:
            period = 1
        if period_2_condition:
            period = 2
        if period_3_condition:
            period = 3
        if not minutes_condition:
            return False
    else:
        return False

    match_results = element.find_elements_by_class_name(f'event__part--{period}')

    results_list = []

    for command_result in match_results:
        results_list.append(command_result.text)

    if results_list and int(results_list[0]) == 0 and int(results_list[1]) == 0:
        return period
    else:
        return False