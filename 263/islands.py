import numpy as np


grid = [[1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]]


def count_islands(grid: list) -> int:
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # grid = np.asarray(grid, dtype=np.int32)

    # number of islands = 0         # var. for the counts
    islands = 0

    # loop through grid
    for i in range(len(grid)):
        print(grid[i][0])
        if grid[i][0] == 1:
            mark_islands(i, 0, grid)

    # mark_islands(r, c, grid)
    return islands
    # return np.asarray(grid, dtype=np.int32)


def mark_islands(i: int, j: int, grid: list):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    grid[i][j] = '#'      # one way to mark visited ones - suggestion.
    # markers = numpy.copy(grid)
    # print(markers)


def main():
    print('thank you for everything...')
    print(count_islands(grid))
    print(grid)


if __name__ == '__main__':
    main()
