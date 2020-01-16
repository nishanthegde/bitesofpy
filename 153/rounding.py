from typing import List
import math


def round_up_or_down(transactions: List, up: bool=True) -> List:
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    if up:
        return [math.ceil(t) for t in transactions]
    else:
        return [math.floor(t) for t in transactions]


def main():
    print('thank you for everything...')
    transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
    transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33]
    print(round_up_or_down(transactions2))
    print(round_up_or_down(transactions1, False))


if __name__ == '__main__':
    main()
