from typing import List


def get_indices(items: List[str], element: str) -> List[int]:
    indices = []

    for i in range(len(items)):
        if element == items[i]:
            indices.append(i)

    return indices


def sum_indices(items: List[str]) -> int:
    tot_ind = 0

    for i in range(len(items)):
        tot_ind += sum([k for k in get_indices(items, items[i]) if k <= i])

    return tot_ind
