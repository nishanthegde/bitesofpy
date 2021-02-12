IMPOSSIBLE = 'Mission impossible. No one can contribute.'

village = [0, -3, 2, 1, -7, 5, 3, -1, 6]
extreme = [-1, -2, -3, -4, -5, -1, -2, -3]
one = [0, 1, -1, -5, 0, 4, -3, -2]
penniless = [0, 0, 0, 0, 1, -5, -2, -1, -3]
poverty = [0, -3, 2, 1, -7, 5, 3, -1, 6]
some = [2, -3, 2, 1, -7, -5, 3, -6, 18, 7, 13, 12]
community = [3, 2, 6, 4, 7, 5, -8, -9, 3, 8, 4, -12, 3, -10, -15,
             2, 6, -10, 6, 3, -1, 5, -5, -8, 11, 7, -9, -5, -6, -2,
             7, 8, 11, 8, 6, -1, -6, 9, 8, 6, -3, 4, -8, 3, -4, 1,
             2, 8, -2, 9, -3, 8, -10, -8, 5, -4, -6, 5, -1, 4, 2,
             2, 7, 3, -2, 5, 1, 4, -7, 5, 8, 4, 2, 10, -24, -10, -9,
             -2, 1, 6, 1, 3, -44, 3, 6, -1, 9, -6, 5, 4, 3, 6, -1,
             0, 11, 4, 8, 16, -33, 8, -2, 4, 5, 3, 2, -8, -7, -5,
             0, 2, 5, -2, 4, 1, 2, 4, 2, -5, 7, 4, 5, -2, 7, 5, -8]


def max_fund(village: list):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending

    max_ending_here = 0
    max_so_far = 0
    start = 0
    end = 0
    reset = False

    if all(i < 0 for i in village):
        print(IMPOSSIBLE)
        return (0, 0, 0)
    else:
        for i in range(0, len(village)):

            print(i, village[i])
            max_ending_here += village[i]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                if reset and max_so_far == 0:
                    start = i
                end = i
                print('max swap', start)
                reset = False

            if max_ending_here < 0:
                max_ending_here = 0
                reset = True
                if i < len(village) - 1:
                    start = i + 1
                print('max reset', start)

            print('max_so_far:{}, max_ending_here:{}'.format(max_so_far, max_ending_here))
            print('')

        return (max_so_far, min(start + 1, end + 1), end + 1)


def main():
    print('thank you for looking after my mama :-)...')
    # print(max_fund(village))
    # print(max_fund(extreme))
    print(max_fund(one))
    # print(max_fund(penniless))
    # print(max_fund(poverty))
    # print(max_fund(some))
    # print(max_fund(community))


if __name__ == '__main__':
    main()
