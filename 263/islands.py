grid = [[1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]]

empty = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

bad_map = [[]]


sparse = [[1, 0, 1],
          [0, 1, 0],
          [1, 0, 1]]

circles = [[1, 1, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 0],
           [1, 0, 0, 1, 1, 0],
           [1, 1, 1, 1, 0, 0]]


def mark_islands(i: int, j: int, grid: list):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    grid[i][j] = '#'    # one way to mark visited ones - suggestion.


def is_valid(i: int, j: int, grid: list):
    rows = len(grid)
    cols = len(grid[0])

    return i >= 0 and i < rows and j >= 0 and j < cols


def calculate_continuos_island(i: int, j: int, grid: list):
    if not is_valid(i, j, grid) or grid[i][j] == 0 or grid[i][j] == '#':
        return 0
    else:
        mark_islands(i, j, grid)  # mark as visited
        calculate_continuos_island(i, j + 1, grid)
        calculate_continuos_island(i, j - 1, grid)
        calculate_continuos_island(i + 1, j, grid)
        calculate_continuos_island(i - 1, j, grid)
        return 1


def count_islands(grid: list) -> int:
    rows = len(grid)
    cols = len(grid[0])

    num_islands = 0
    for row in range(rows):
        for col in range(cols):
            # number_of_island += get_island(binaryMatrix, row, col, visited)
            # print(row, col)
            num_islands += calculate_continuos_island(row, col, grid)

    return num_islands


def main():
    print('thank you for everything...')
    # islands = count_islands(grid)
    # print(islands)
    # islands = count_islands(empty)
    # print(islands)
    # islands = count_islands(bad_map)
    # print(islands)
    # islands = count_islands(sparse)
    # print(islands)
    # islands = count_islands(circles)
    # print(islands)


if __name__ == '__main__':
    main()

# import numpy as np

# grid_single = [[1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]
# grid_single1 = [[0, 0, 0, 0, 0, 0, 0, 0]]
# grid_single2 = [[1, 0, 1, 0, 0, 1, 0, 1]]
# grid_single3 = [[1, 1, 1, 1, 1, 1, 1, 1]]
# grid_single4 = [[0, 0, 1, 1, 1, 1, 0, 1]]


# eg = [[1, 1, 0, 0, 1],
#       [1, 1, 0, 0, 1],
#       [0, 1, 0, 0, 0],
#       [1, 0, 0, 0, 1],
#       [1, 0, 0, 0, 0]]

# grid = [[1, 0, 0, 1],
#         [1, 0, 1, 0],
#         [0, 1, 0, 0],
#         [1, 0, 0, 1]]

# empty = [[0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0]]

# bad_map = [[]]


# sparse = [[1, 0, 1],
#           [0, 1, 0],
#           [1, 0, 1]]

# circles = [[1, 1, 0, 0, 0, 1],
#            [1, 0, 0, 0, 0, 1],
#            [1, 0, 0, 0, 1, 1],
#            [1, 0, 0, 0, 1, 0],
#            [1, 0, 0, 1, 1, 0],
#            [1, 1, 1, 1, 0, 0]]


# def count_islands_row(grid_row: np.ndarray) -> int:

#     islands = 0

#     # indices for 1s
#     idx_nz = np.flatnonzero(grid_row)

#     if idx_nz.shape[0] > 0:  # if 1s present
#         islands = 1  # initiate island count

#         # compare each element with next...
#         idx_nz_comp = idx_nz[1:] - idx_nz[:-1]
#         islands += np.count_nonzero(idx_nz_comp != 1)

#     return islands


# def count_islands(grid: list) -> int:
#     """
#     Input: 2D matrix, each item is [x, y] -> row, col.
#     Output: number of islands, or 0 if found none.
#     Notes: island is denoted by 1, ocean by 0 islands is counted by continously
#         connected vertically or horizontically  by '1's.
#     It's also preferred to check/mark the visited islands:
#     - eg. using the helper function - mark_islands().
#     """
#     grid = np.asarray(grid, dtype=np.int32)

#     # print(grid)
#     # var for # of islands
#     islands = 0

#     for i in range(0, grid.shape[0]):
#         if i > 0:
#             grid_temp = grid[i] - grid[i - 1]
#             grid_temp = np.where(grid_temp < 0, 0, grid_temp)
#             print(grid[i], grid[i - 1], grid_temp)
#             islands += count_islands_row(grid_temp)
#             # print(islands)
#             # print(grid_arr_new, count_islands(grid_arr_new))
#         else:
#             islands += count_islands_row(grid[i])
#             # print(islands)

#     return islands


# def mark_islands(i: int, j: int, grid: np.ndarray):
#     """
#     Input: the row, column and grid
#     Output: None. Just mark the visited islands as in-place operation.
#     """

#     grid[i, j] = 9    # one way to mark visited ones - suggestion.
#     # markers = numpy.copy(grid)
#     # print(markers)


# def main():
#     # print('please let there be peace...')
#     # islands = count_islands(grid_single)
#     # print(islands)
#     # islands = count_islands(grid_single1)
#     # print(islands)
#     # islands = count_islands(grid_single2)
#     # print(islands)
#     # islands = count_islands(grid_single3)
#     # print(islands)
#     # islands = count_islands(grid_single4)
#     # print(islands)

#     islands = count_islands(circles)
#     print(islands)

#     # grid_arr = np.asarray(grid, dtype=np.int32)

#     # print(grid_arr)
#     # print(grid_arr.shape)

#     # for i in range(0, grid_arr.shape[0]):
#     #     if i > 0:
#     #         print(grid_arr[i], grid_arr[i - 1])
#     #         grid_arr_new = grid_arr[i] - grid_arr[i - 1]
#     #         grid_arr_new = np.where(grid_arr_new < 0, 0, grid_arr_new)
#     #         print(grid_arr_new, count_islands(grid_arr_new))
#     #     else:
#     #         print(grid_arr[i], count_islands(grid_arr[i]))

#     # a = np.array([-1, 0, 0, 0, -1])
#     # print(a < 0)
#     # a = np.where(a < 0, 0, a)
#     # print(a)

#     # print(grid_arr)

#     # idx_nz = np.flatnonzero(grid_arr)
#     # print(idx_nz)
#     # idx_nz_comp = idx_nz[1:] - idx_nz[:-1]
#     # print(idx_nz_comp)

#     # print(list(np.flatnonzero(islands)))

#     # print(grid)

#     # a = np.asarray([1, 1, 1, 0, 0, 0, 1, 1, 0, 0])
#     # a_ext = np.concatenate(([0], a, [0]))

#     # print(a_ext)
#     # idx = np.flatnonzero(a_ext[1:] != a_ext[:-1])
#     # print(idx)

#     # print([idx[1::2]])
#     # print(a_ext[1:][idx[1::2]])
#     # print(idx[::2])
#     # print(idx[::2] - idx[1::2])

#     # a_ext[1:][idx[1::2]] = idx[::2] - idx[1::2]
#     # print(a_ext[1:-1])
#     # print(a_ext.cumsum()[1:-1])


# if __name__ == '__main__':
#     main()
