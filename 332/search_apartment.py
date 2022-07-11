from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    # return list of apartments
    ret = []

    if len(buildings) == 0:
        return None
    else:
        max_so_far = buildings[0]
        # check for west facing apartments
        if direction == 'W':
            ret.append(0)
            for i in range(1, len(buildings)):
                if buildings[i] > buildings[i - 1] and buildings[i] > max_so_far:
                    max_so_far = buildings[i]
                    ret.append(i)
        else:
            # check for east facing apartments
            max_so_far = buildings[len(buildings) - 1]
            for i in range(buildings[len(buildings) - 1], 0, -1):
                print(i)
            #     if buildings[i] < buildings[i - 1]:
            #         ret.append(i - 1)
            # ret.append(len(buildings) - 1)
    return ret


def main():
    print('thank you for looking after mama and naia')


if __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]
    main()
