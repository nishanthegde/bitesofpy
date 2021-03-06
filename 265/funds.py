IMPOSSIBLE = 'Mission impossible. No one can contribute.'

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

    sum_ending_here = 0
    best_sum = 0
    start_position = 0
    end_position = 0
    sum_reset = False
    best_sums = []

    if all(i < 0 for i in village):
        print(IMPOSSIBLE)
        return (0, 0, 0)
    else:
        for i in range(0, len(village)):

            # print(i, village[i])
            sum_ending_here += village[i]

            if sum_reset:
                best_sums.append((best_sum, start_position + 1, end_position + 1))
                start_position = i
                end_position = i
                sum_reset = False

            if sum_ending_here <= 0:
                sum_ending_here = 0
                sum_reset = True
            elif (best_sum < sum_ending_here):
                best_sum = sum_ending_here
                end_position = i

            # print('sum_ending_here:{}, start:{}, end:{}, best_sum:{}'.format(sum_ending_here, start_position,
            #                                                                  end_position, best_sum))
            # print('')
        best_sums.append((best_sum, start_position + 1, end_position + 1))

    return(max(sorted(best_sums, key=lambda x: (x[0], x[1], x[2])),key=lambda item:item[0]))