from typing import List


def get_change(target: int, coins_available: List[int], coins_so_far: List[int] = []):
    if sum(coins_so_far) == target:
        yield coins_so_far
    elif sum(coins_so_far) > target:
        pass
    elif coins_available == []:
        pass
    else:
        for c in get_change(target, coins_available[:], coins_so_far + [coins_available[0]]):
            yield c
        for c in get_change(target, coins_available[1:], coins_so_far):
            yield c


def make_changes(n: int, coins: List[int]) -> int:
    # candidate denominations must be less than change amount
    candiates = [c for c in coins if c <= n]
    ways = [w for w in get_change(n, candiates)]
    return len(ways)
