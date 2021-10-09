from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """

    if len(buildings) == 0:
        return []

    if direction == 'E':
        buildings.reverse()

    views = []
    highest_floor = buildings[0]

    for i, b in enumerate(buildings):
        if i == 0:
            views.append(1)
        else:
            if b > highest_floor:
                highest_floor = b
                views.append(1)
            else:
                views.append(0)
        prev_floor_ht = b

    if direction == 'E':
        views = [i - j for j, e in enumerate(views) if e == 1]
    else:
        views = [j for j, e in enumerate(views) if e == 1]

    return sorted(views)