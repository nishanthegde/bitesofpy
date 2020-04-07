from functools import wraps
import random

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def inner(*args, **kwargs):
        _tries = 1
        while _tries <= MAX_RETRIES:
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                print(exc)
            _tries += 1
        raise MaxRetriesException
    return inner


@retry
def get_two_numbers(numbers):
    """Give a list of items pick 2 random ones,
       if both are not ints raise a ValueError
    """
    chosen = random.sample(numbers, 2)
    if not all(type(i) == int for i in chosen):
        raise ValueError('not all ints')


def main():
    print('thank you for everything')
    # get_two_numbers(['a', 'b'])
    # get_two_numbers([1, 2, 3])
    # pretty = make_pretty(ordinary)
    # pretty()
    # ordinary()
    docstring = get_two_numbers.__doc__
    print(docstring)


if __name__ == '__main__':
    main()
