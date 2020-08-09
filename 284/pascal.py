from typing import List


def pascal(N: int) -> List[int]:
    start = [1]
    if N == 0:
        return []

    for i in range(N - 1):
        start = [0] + start + [0]
        res = []
        for j in range(len(start) - 1):
            res.append(start[j] + start[j + 1])
        start = res

    return start
