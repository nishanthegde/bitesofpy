from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:

    def __init__(self, limit):
        self.limit = limit
        self.x = 1

    def __iter__(self):
        # self.x = 1
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration

        self.x = x + 1
        return '{} egg'.format(choice(COLORS))


# def main():
#     print('thank you for all that you have given me...')
#     # print(COLORS)
#     # print(choice(COLORS))

#     # for egg in EggCreator(20):
#     #     print(egg)

#     # eg = EggCreator(10)
#     # assert type(eg) == EggCreator

#     # ec = EggCreator(2)
#     # assert len(list(ec)) == 2
#     # ec = EggCreator(5)
#     # assert len(list(ec)) == 5

#     # # print(list(ec))

#     # ec = EggCreator(2)
#     # # # print(list(ec))
#     # next_egg = next(ec)
#     # assert next_egg.split()[0] in COLORS
#     # print(next_egg.split()[0])

#     # ec = EggCreator(2)
#     # next(ec)
#     # next(ec)
#     # next(ec)

#     ec = EggCreator(20)
#     output1 = list(ec)
#     ec = EggCreator(20)
#     output2 = list(ec)
#     assert output1 != output2


# if __name__ == '__main__':
#     main()
