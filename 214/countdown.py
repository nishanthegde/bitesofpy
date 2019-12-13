from itertools import islice


def countdown():
    """Write a generator that counts from 100 to 1"""
    for i in range(100, 0, -1):
        yield i


def simple_generator_function():
    yield 1
    yield 2
    yield 3


# def main():
#     # print('thank you for my life...')
#     our_generator = simple_generator_function()

#     # print(next(our_generator))
#     # print(next(our_generator))
#     # print(next(our_generator))

#     cd = countdown()
#     for _ in range(101):
#         print(next(cd))


# if __name__ == '__main__':
#     main()
