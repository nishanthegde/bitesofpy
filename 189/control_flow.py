IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def _contins_digit(input: str)-> bool:
    for s in input:
        if s.isdigit():
            return True
    return False


def filter_names(names: list) -> list:
    ret = []

    for n in names:
        if n.lower()[:1] == QUIT_CHAR:
            break
        if n.lower()[:1] != IGNORE_CHAR and not _contins_digit(n):
            ret.append(n)

    return ret[:MAX_NAMES]


# def main():
#     print('thank you for everything...')
#     print(filter_names(['bob']))
#     print(filter_names(['quit', 'ana']))
#     print(filter_names(['t2im', '1quinton', 'a3na', '4']))
#     print(filter_names(['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry']))
#     print(filter_names(['bob', 'ana', 'quinton']))
#     print(filter_names(['tim', 'ana', 'quinton']))


# if __name__ == '__main__':
#     main()
