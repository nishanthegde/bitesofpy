def flatten(list_of_lists) -> list:
    if list_of_lists == []:
        return list_of_lists

    if isinstance(list_of_lists[0], list) or isinstance(list_of_lists[0], tuple):
        return flatten(list(list_of_lists[0])) + flatten(list_of_lists[1:])

    return [list_of_lists[0]] + flatten(list_of_lists[1:])


# def main():
#     print('thank you for everything you have given me ...')

#     # inp = [1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
#     # expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # assert list(flatten(inp)) == expected

#     # inp = [1, 2, [3, 4], [5, [6, 7]], [8, [9, [10]]],
#     #        [11, [12, 13], [14, [15, 16, [17, 18, [19, 20]]]]]]
#     # expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
#     #             14, 15, 16, 17, 18, 19, 20]
#     # assert list(flatten(inp)) == expected

#     # inp = ['a', 'b', [1, 2, 3],
#     #        ['c', 'd', ['e', 'f', ['g', 'h']]],
#     #        [4, [5, 6, [7, [8]]]]]
#     # expected = ['a', 'b', 1, 2, 3, 'c', 'd', 'e', 'f', 'g',
#     #             'h', 4, 5, 6, 7, 8]
#     # assert list(flatten(inp)) == expected

#     inp = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
#     # inp = [1, 2, 3, [(4, 5), [6, 7, [8, 9, 10]]]]
#     # inp = [1, 2, 3, (4, 5), [6, 7, [8, 9, 10]]]
#     # inp = [1, 2, 3, 4, 5, [6, 7, [8, 9, 10]]]
#     # inp = [1, 2, 3, 4, 5, 6, 7, [8, 9, 10]]
#     # inp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # print(list(flatten(inp)))
#     assert list(flatten(inp)) == expected


# if __name__ == '__main__':
#     main()
