import re
from collections import Counter


def get_index_different_char(chars):

    alnum_list = [bool(re.match('^[a-zA-Z0-9]+$', str(e))) for e in chars]

    c = Counter(alnum_list)

    minority = c.most_common()[-1:][0][0]

    return alnum_list.index(minority)


# def main():

#     print('here ...')
#     ret = get_index_different_char(['A', 'f', '.', 'Q', 2])
#     print(ret)

#     ret = get_index_different_char(['.', '{', ' ^', '%', 'a'])
#     print(ret)

#     ret = get_index_different_char(list(range(1, 9)) + ['}'] + list('abcde'))
#     print(ret)


# if __name__ == '__main__':
#     main()
