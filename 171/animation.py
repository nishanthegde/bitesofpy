from itertools import cycle
import sys
from time import time, sleep

import pytest

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds: int):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    spinner = cycle(SPINNER_STATES)
    timeout = time() + seconds

    while True:
        if time() > timeout:
            break
        sleep(STATE_TRANSITION_TIME)
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\r')


def main():
    print('thank you for everything...')
    # print(['-', '\\', '|', '/'] * 2)
    # print(SPINNER_STATES[:2])
    # spinner(0.2)
    # actual = capfd.readouterr()[0].strip().split('\r')


if __name__ == '__main__':
    spinner(1)
    main()
