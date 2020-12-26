def main():
    import logging
    from utils import on_startup_notify

    try:
        on_startup_notify()
    except Exception as err:
        logging.info(err)

    import threading
    from loader import bot
    from utils import parsing_process

    parsing_thead = threading.Thread(target=parsing_process)
    parsing_thead.start()
    bot.polling()


if __name__ == '__main__':
    main()
