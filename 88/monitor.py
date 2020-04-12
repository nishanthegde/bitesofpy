from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()

def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    pass


def main():
    print('i am grateful for all that you have given me... ')
    print('kata will be finished tomorrow')
    print(type(violations))


if __name__ == '__main__':
    main()
