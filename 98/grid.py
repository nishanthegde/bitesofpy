import test_grid as tg
import re
import numpy as np

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    # print(grid)

    grid_list = [l for l in grid.splitlines() if l]
    grid_list = [re.split(' - |    |   ||', r) for r in grid_list][::2]
    grid_list = [[int(float(j)) for j in i] for i in grid_list]

    grid_mat = np.array(grid_list)

    return grid_mat


def main():
    print("thank you for everything...")
    print(print_sequence_route(tg.small_grid).shape)
    print(type(print_sequence_route(tg.intermediate_grid)))
    print(print_sequence_route(tg.big_grid).shape)


if __name__ == "__main__":
    main()
