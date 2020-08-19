from typing import List


def minimum_number(digits: List[int]) -> int:
    ret = 0

    if digits:
        digits_set = [str(d) for d in sorted(list(set(digits)))]
        return int(''.join(digits_set))

    return ret