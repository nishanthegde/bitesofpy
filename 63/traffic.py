from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple('State', 'color command timeout')


def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    return cycle([-1, 1])


if __name__ == '__main__':
    print('thank you for everything...')
    # print a sample of 10 states if run as standalone program
    # for state in islice(traffic_light(), 10):
    #     print(f'{state.command}! The light is {state.color}')
    #     sleep(state.timeout)
    it = traffic_light()
    print(len(list(islice(it, 100, 217))))
