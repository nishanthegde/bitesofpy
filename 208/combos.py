from itertools import combinations


def find_number_pairs(numbers, N=10):

    ret = []

    for tup in list(combinations(numbers, 2)):
        if tup[0] + tup[1] == N:
            ret.append(tup)

    return ret


def _sort_all(ret):
    return sorted(
        [tuple(sorted(n)) for n in ret]
    )


# def main():

#     print('here...')

#     actual = find_number_pairs([2, 3, 5, 4, 6])
#     actual = find_number_pairs([9, 1, 3, 8, 7])
#     actual = find_number_pairs([0.24, 0.36, 0.04, 0.06, 0.33, 0.08, 0.20, 0.27, 0.3, 0.31,
#                                 0.76, 0.05, 0.08, 0.08, 0.67, 0.09, 0.66, 0.79, 0.95], 1)
#     actual = find_number_pairs([9, 1, 3, 8, 7], 0)
#     actual = find_number_pairs([-9, 29, 11, 10, 9, 3, -1, 21], 20)
#     actual = find_number_pairs([1.69, 1.82, 2.91, 4.67, 4.81, 3.05, 5.82, 5.06,
#                                 4.28, 6.36, 5.19, 4.57], 10)

#     print(_sort_all(actual))


# if __name__ == '__main__':
#     main()
