import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    intersection = set()

    if args:
        for arg in args:
            if arg:
                if arg == [arg for arg in args if arg][0]:
                    intersection = set(arg)
                intersection = set.intersection(intersection, set(arg))

    return intersection

