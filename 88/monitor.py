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
def timeit() -> None:
    start = time()
    yield
    elapsed_time = time() - start

    if elapsed_time >= OPERATION_THRESHOLD_IN_SECONDS:
        violations.update({get_today().strftime('%s')})

    if violations[get_today().strftime('%s')] >= ALERT_THRESHOLD:
        # print('ellapsed_time time: {} seconds'.format(elapsed_time))
        print(ALERT_MSG)


def main():

    print('thank you for everything that you have given me')

    with timeit():
        s = [x for x in range(1000000)]
    with timeit():
        s = [x for x in range(100000)]
    with timeit():
        s = [x for x in range(100000)]

    # print(violations[get_today().strftime('%s')])


if __name__ == '__main__':
    main()
