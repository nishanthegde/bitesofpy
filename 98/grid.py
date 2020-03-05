import test_grid as tg
import re
import numpy as np

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def check_neighbors_val(grid_array: np.array, val: int, center: tuple) -> tuple:
    # check 4 neighbors for next value and return tuple of indices of new center and direction

    center_row_idx = center[0]
    center_col_idx = center[1]

    # print(grid_array.shape)

    if center_col_idx < grid_array.shape[1] - 1 and grid_array[center_row_idx, center_col_idx + 1] == val + 1:
        center_col_idx = center_col_idx + 1
        direction = RIGHT
    if center_col_idx > 0 and grid_array[center_row_idx, center_col_idx - 1] == val + 1:
        center_col_idx = center_col_idx - 1
        direction = LEFT
    if center_row_idx < grid_array.shape[0] - 1 and grid_array[center_row_idx + 1, center_col_idx] == val + 1:
        center_row_idx = center_row_idx + 1
        direction = DOWN
    if center_row_idx > 0 and grid_array[center_row_idx - 1, center_col_idx] == val + 1:
        center_row_idx = center_row_idx - 1
        direction = UP

    return (center_row_idx, center_col_idx, direction)


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    # print(grid)

    grid_list = [l for l in grid.splitlines() if l]
    grid_list = [re.split(' - |    |   ||', r) for r in grid_list][::2]
    # grid_list = [re.split(' - |\\s*|   ||', r) for r in grid_list][::2]
    grid_list = [[int(float(j)) for j in i] for i in grid_list]

    grid_array = np.array(grid_list)
    num_elements = (grid_array.shape[0] * grid_array.shape[1])

    elements = [e for e in range(START_VALUE, num_elements)]

    # list to store (element,direction from previous element)
    grid_line = list()

    st_idx = 0

    for i, e in enumerate(elements):

        start_idx_tuple = np.where(grid_array == e)
        start_idx_coord = list(zip(start_idx_tuple[0], start_idx_tuple[1]))

        # assign row index and col index for START_VALUE to center
        center_row_idx = start_idx_coord[0][0]
        center_col_idx = start_idx_coord[0][1]

        # get current direction
        current_dir = check_neighbors_val(grid_array, e, (center_row_idx, center_col_idx))[2]

        # get previous direction
        if i > 0:
            previous_dir = grid_line[-1]
            # print(previous_dir, current_dir)
        # previous_dir = grid_line[-1]

        grid_line.append(e)
        grid_line.append(current_dir)

        # print(i, grid_line)

        if i > 0:
            # check if previous direction is equal to current direction
            if previous_dir != current_dir:
                print(' '.join(map(str, grid_line[st_idx::2])) + ' ' + current_dir)
                st_idx = len(grid_line)

        if i == (num_elements - 2):
            print((' '.join(map(str, grid_line[st_idx::2])) + ' ' + str(num_elements)).strip())

    return grid_array


def main():
    print("thank you for everything...")
    # print(print_sequence_route(tg.very_small_grid))
    # print(print_sequence_route(tg.small_grid))
    # print(print_sequence_route(tg.intermediate_grid))
    # print(print_sequence_route(tg.big_grid))


if __name__ == "__main__":
    main()
