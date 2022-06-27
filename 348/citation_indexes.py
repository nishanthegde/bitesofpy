from typing import Sequence

TYPE_ERROR_MSG = "Unsupported input type: use either a list or a tuple"
VALUE_ERROR_MSG = "Unsupported input value: citations cannot be neither empty nor None"


def h_index(citations: Sequence[int]) -> int:
    """Return the highest number of papers h having at least h citations"""
    if not isinstance(citations, (list, tuple)) and citations is not None:
        raise TypeError(TYPE_ERROR_MSG)
    else:
        if not citations or len(citations) == 0 or sum(1 for i in citations if i < 0) > 0:
            raise ValueError(VALUE_ERROR_MSG)


def i10_index(citations: Sequence[int]) -> int:
    """Return the number of papers having at least 10 citations"""

    if not isinstance(citations, (list, tuple)) and citations is not None:
        raise TypeError(TYPE_ERROR_MSG)
    else:
        if not citations or len(citations) == 0 or sum(1 for i in citations if i < 0) > 0:
            raise ValueError(VALUE_ERROR_MSG)

    return sum(1 for i in citations if i >= 10)


def main():
    print('thank you for looking after mama and naia')


if __name__ == '__main__':
    main()
