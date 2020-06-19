
IMPOSSIBLE = 'Mission impossible. No one can contribute.'

# community = [3, 2, 6, 4, 7, 5, -8, -9, 3, 8, 4, -12, 3, -10, -15,
#              2, 6, -10, 6, 3, -1, 5, -5, -8, 11, 7, -9, -5, -6, -2,
#              7, 8, 11, 8, 6, -1, -6, 9, 8, 6, -3, 4, -8, 3, -4, 1,
#              2, 8, -2, 9, -3, 8, -10, -8, 5, -4, -6, 5, -1, 4, 2,
#              2, 7, 3, -2, 5, 1, 4, -7, 5, 8, 4, 2, 10, -24, -10, -9,
#              -2, 1, 6, 1, 3, -44, 3, 6, -1, 9, -6, 5, 4, 3, 6, -1,
#              0, 11, 4, 8, 16, -33, 8, -2, 4, 5, 3, 2, -8, -7, -5,
#              0, 2, 5, -2, 4, 1, 2, 4, 2, -5, 7, 4, 5, -2, 7, 5, -8]

# one = [0, 1, -1, -5, 0, 4, -3, -2]
# penniless = [0, 0, 0, 0, 1, -5, -2, -1, -3]
# poverty = [0, -3, 2, 1, -7, 5, 3, -1, 6]
# some = [2, -3, 2, 1, -7, -5, 3, -6, 18, 7, 13, 12]
# extreme = [-1, -2, -3, -4, -5, -1, -2, -3]
# nothing = []
# geeks = [-2, -3, 4, -1, -2, 1, 5, -3]


def max_fund(village: list) -> tuple:
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending

    best_sum = 0  # best sum collected
    sum_so_far = 0  # sum collected so far
    starting = 0
    ending = 0

    if not village:
        print(IMPOSSIBLE)
        return (0, 0, 0)

    for i, e in enumerate(village):

        sum_so_far = sum_so_far + e

        if sum_so_far < 0:

            sum_so_far = 0

            if i != len(village) - 1:
                # end of string is not reached reset starting
                starting = 0
            else:
                if starting == 0 and ending > 0:
                    starting = prev_starting

        if sum_so_far > 0:

            if starting == 0:
                starting = i + 1
                prev_starting = starting

        if best_sum < sum_so_far:

            best_sum = sum_so_far

            if starting != 0:
                ending = i + 1
            # else:
                # starting = i + 1
        # print(i, e, sum_so_far, best_sum, "starting ={}".format(starting), "ending ={}".format(ending))

    if ending == 0:
        # print('here')
        ending = starting

    return (best_sum, starting, ending)


# def main():
#     print('thank you for the wave today... ')
#     print(max_fund(one))
#     print(max_fund(penniless))
#     print(max_fund(poverty))
#     print(max_fund(community))
#     print(max_fund(some))
#     print(max_fund(extreme))


# if __name__ == '__main__':
#     main()