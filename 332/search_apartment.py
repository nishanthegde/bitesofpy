from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    # return list of apartments
    ret = []

    if len(buildings) == 0:
        return None
    else:
        # check for west facing apartments
        if direction == 'W':
            ret.append(0)
            max_so_far = buildings[0]
            for i in range(1, len(buildings)):
                if buildings[i] > buildings[i - 1] and buildings[i] > max_so_far:
                    max_so_far = buildings[i]
                    ret.append(i)
        else:
            # check for east facing apartments
            ret.append(len(buildings) - 1)
            max_so_far = buildings[len(buildings) - 1]
            for i in range(len(buildings)-1, 0, -1):
                if buildings[i - 1] > buildings[i] and buildings[i - 1] > max_so_far:
                    max_so_far = buildings[i-1]
                    ret.append(i - 1)
                # print(i)
            #     if buildings[i] < buildings[i - 1]:
            #         ret.append(i - 1)
            # ret.append(len(buildings) - 1)
            ret = ret[::-1]

    return ret
