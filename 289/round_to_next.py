from random import choice

def round_to_next(number: int, multiple: int):
    ret = number

    while ret % multiple != 0:
        if multiple >= 0:
            ret += 1
        else:
            ret -= 1

    return ret
