import numpy as np

grid_single = [[1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]
grid_single1 = [[0, 0, 0, 0, 0, 0, 0, 0]]
grid_single2 = [[1, 0, 1, 0, 0, 1, 0, 1]]
grid_single3 = [[1, 1, 1, 1, 1, 1, 1, 1]]
grid_single4 = [[0, 0, 1, 1, 1, 1, 0, 1]]

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
    grid = np.asarray(grid, dtype=np.int32)

    # var for # of islands
    islands = 0

    # indices for 1s
    idx_nz = np.flatnonzero(grid)

    if idx_nz.shape[0] > 0:  # if 1s present
        islands = 1  # initiate island count

        # compare each element with next...
        idx_nz_comp = idx_nz[1:] - idx_nz[:-1]
        islands += np.count_nonzero(idx_nz_comp != 1)

    return islands


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
    islands = count_islands(grid_single4)
    print(islands)
    # print(list(np.flatnonzero(islands)))

    # print(grid)

    # a = np.asarray([1, 1, 1, 0, 0, 0, 1, 1, 0, 0])
    # a_ext = np.concatenate(([0], a, [0]))

    # print(a_ext)
    # idx = np.flatnonzero(a_ext[1:] != a_ext[:-1])
    # print(idx)

    # print([idx[1::2]])
    # print(a_ext[1:][idx[1::2]])
    # print(idx[::2])
    # print(idx[::2] - idx[1::2])

    # a_ext[1:][idx[1::2]] = idx[::2] - idx[1::2]
    # print(a_ext[1:-1])
    # print(a_ext.cumsum()[1:-1])


if __name__ == '__main__':
    main()
