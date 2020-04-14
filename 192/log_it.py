import logging
from typing import Callable


def set_debug_level():
    logging.getLogger().setLevel("DEBUG")


def set_info_level():
    logging.getLogger().setLevel("INFO")


def set_warning_level():
    logging.getLogger().setLevel("WARNING")


def set_error_level():
    logging.getLogger().setLevel("ERROR")


def set_critical_level():
    logging.getLogger().setLevel("CRITICAL")


DEBUG = set_debug_level
INFO = set_info_level
WARNING = set_warning_level
ERROR = set_error_level
CRITICAL = set_critical_level


def log_it(level: Callable, msg: str) -> None:

    logger = logging.getLogger('pybites_logger')

    if level == DEBUG:
        logger.debug(msg)
    elif level == INFO:
        logger.info(msg)
    elif level == WARNING:
        logger.warning(msg)
    elif level == ERROR:
        logger.error(msg)
    elif level == CRITICAL:
        logger.critical(msg)


def main():
    print('thank you for everything... ')
    print(callable(DEBUG))


if __name__ == "__main__":
    main()
    log_it(DEBUG, "This is a debug message.")
    # log_it(INFO, "This is an info message.")
    # log_it(WARNING, "This is a warning message.")
    # log_it(ERROR, "This is an error message.")
    # log_it(CRITICAL, "This is a critical message.")
