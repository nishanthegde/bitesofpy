import logging
from typing import Callable

# DEBUG = logging.DEBUG
# INFO = logging.INFO
# WARNING = logging.WARNING
# ERROR = logging.ERROR
# CRITICAL = logging.CRITICAL


def test_func():
    return True


logger = logging.getLogger('simple_example')

DEBUG = logger.setLevel(logging.DEBUG)
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


LOG_LEVEL = {
    "debug": DEBUG,
    "info": INFO,
    "warning": WARNING,
    "error": ERROR,
    "critical": CRITICAL,
}


def log_it(level: Callable, msg: str) -> None:

    # create logger
    logger = logging.getLogger('simple_example')

    if logging.getLogger().level == 10:
        logging.debug(msg)
    elif logging.getLogger().level == 20:
        logging.info(msg)
    elif logging.getLogger().level == 30:
        logging.warning(msg)
    elif logging.getLogger().level == 40:
        logging.error(msg)
    elif logging.getLogger().level == 50:
        logging.critical(msg)


def Geek():
    return 5


def main():
    print('thank you for everything ...')
    # logger = logging.getLogger(__name__)
    # logging.getLogger('test')
    # print(logger)
    for level in LOG_LEVEL:
        print(callable(LOG_LEVEL[level]))

    # # an object is created of Geek()
    # let = Geek
    # print(callable(let))

    # # a test variable
    # num = 5 * 5
    # print(callable(num))


if __name__ == "__main__":
    # log_it(DEBUG, "This is a debug message.")
    # log_it(INFO, "This is an info message.")
    # log_it(WARNING, "This is a warning message.")
    # log_it(ERROR, "This is an error message.")
    # log_it(CRITICAL, "This is a critical message.")
    main()
