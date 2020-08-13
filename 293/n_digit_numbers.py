from typing import List, TypeVar

T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    ret = list()
    if n < 1:
        raise ValueError
    else:
        x_er = 10 ** (n - 1)
        print(x_er)

    for ele in numbers:
        if ele // x_er <= 0:
            ret.append(int(round(ele * x_er, 0)))
        elif ele // x_er > 10:
            ret.append(int(str(ele)[:-(len(str(ele // x_er))-1)]))
            # ret.append(int(round(ele % (x_er * 10), 0)))
        else:
            ret.append(ele)

    return ret
