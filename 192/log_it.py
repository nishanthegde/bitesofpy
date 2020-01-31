import logging
from typing import Callable
# import pytest
# import test_log_it


DEBUG = ""logger.setLevel(logging.DEBUG)""
INFO = logger.setLevel(logging.INFO)
WARNING = logger.setLevel(logging.WARNING)
ERROR = logger.setLevel(logging.ERROR)
CRITICAL = logger.setLevel(logging.CRITICAL)


def log_it(level: Callable, msg: str) -> None:

    logger.debug(msg)
    # if level == 'debug':


def main():
    print('thank you for everything ...')

    # for level in test_log_it.LOG_LEVEL:
    #     print(type(test_log_it.LOG_LEVEL[level]))
    # assert callable(test_log_it.LOG_LEVEL[level])
    # assert callable(DEBUG)
    # print(type(DEBUG))
    # log_it("debug", "This is a debug message")
    # caplog.set_level(logging.DEBUG)

    logger = logging.getLogger('pybites_logger')
    logging.basicConfig(format='%(name)s-%(levelname)s-%(message)s')
    logger.setLevel(logging.DEBUG)
    print(type(logger.error('This is a debug message')))


if __name__ == "__main__":
    main()
