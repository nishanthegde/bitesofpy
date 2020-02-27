import test_grid as tg

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    grid_list = [l for l in grid.splitlines() if l]

    for i, l in enumerate(grid_list):
        if ' {} '.format(START_VALUE) in l:
            print(i, l)

    # return grid_list


def main():
    print("thank you for everything...")
    print(print_sequence_route(tg.small_grid))
    print(print_sequence_route(tg.intermediate_grid))
    print(print_sequence_route(tg.big_grid))


if __name__ == "__main__":
    main()
