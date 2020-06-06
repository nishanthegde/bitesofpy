from typing import List

# Hint:
# You can define a helper function: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.

def get_others(map_: List, r: int, c: int) -> int:
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total number)
    """
    nums = 0
    over = 0

    if map_[r][c] == 1:
        nums += 1
        if c > 0 and map_[r][c - 1] == 1:
            over += 2
        if r > 0 and map_[r-1][c] == 1:
            over += 2

    # print((nums * 4) - over)
    return (nums * 4) - over


def island_size(map_: List) -> int:
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    rows = len(map_)
    cols = len(map_[0])

    for i in range(0, rows):
        for j in range(0, cols):
            perimeter += get_others(map_, i, j)

    return perimeter


def main():
    print(island_size(rectangle))


if __name__ == '__main__':
    main()
