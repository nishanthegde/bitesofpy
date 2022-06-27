from typing import Sequence

TYPE_ERROR_MSG = "Unsupported input type: use either a list or a tuple"
VALUE_ERROR_MSG = "Unsupported input value: citations cannot be neither empty nor None"


def h_index(citations: Sequence[int]) -> int:
    """Return the highest number of papers h having at least h citations"""
    if not isinstance(citations, (list)) and not isinstance(citations, (tuple)) and citations is not None:
        raise TypeError(TYPE_ERROR_MSG)
    elif not citations or len(citations) == 0:
        raise ValueError(VALUE_ERROR_MSG)
    elif sum(1 for i in citations if not isinstance(i, (int))) > 0:
        raise ValueError(VALUE_ERROR_MSG)
    else:
        if sum(1 for i in citations if i < 0) > 0:
            raise ValueError(VALUE_ERROR_MSG)

    h = 1
    while 1:
        if not sum(1 for i in citations if i >= h) >= h:
            break
        h += 1

    return h - 1


def i10_index(citations: Sequence[int]) -> int:
    """Return the number of papers having at least 10 citations"""

    if not isinstance(citations, (list)) and not isinstance(citations, (tuple)) and citations is not None:
        raise TypeError(TYPE_ERROR_MSG)
    elif not citations or len(citations) == 0:
        raise ValueError(VALUE_ERROR_MSG)
    elif sum(1 for i in citations if not isinstance(i, (int))) > 0:
        raise ValueError(VALUE_ERROR_MSG)
    else:
        if sum(1 for i in citations if i < 0) > 0:
            raise ValueError(VALUE_ERROR_MSG)

    return sum(1 for i in citations if i >= 10)
