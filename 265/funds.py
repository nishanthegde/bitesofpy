IMPOSSIBLE = 'Mission impossible. No one can contribute.'

village = [0, -3, 2, 1, -7, 5, 3, -1, 6]
extreme = [-1, -2, -3, -4, -5, -1, -2, -3]
one = [0, 1, -1, -5, 0, 4, -3, -2]


def max_fund(village: list):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending

    max_ending_here = 0
    max_so_far = 0
    start = 0
    end = 0
    s = 0

    if all(i < 0 for i in village):
        print(IMPOSSIBLE)
        return (0, 0, 0)
    else:
        for i in range(0, len(village)):
            print(i, village[i])
            max_ending_here += village[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                # if i != len(village)-1:
                #     start = i
                start = s
                end = i
            if max_ending_here < 0:
                max_ending_here = 0
                s = i + 1
            print('max:{}, start:{}, end:{}'.format(max_so_far, start, end))


def main():
    print('thank you for looking after my mama :-)...')
    # print(max_fund(village))
    # print(max_fund(extreme))
    print(max_fund(one))


if __name__ == '__main__':
    main()
