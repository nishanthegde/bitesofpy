from functools import lru_cache


@lru_cache(maxsize=None)
def cached_fib(n: int) -> int:

    a = 0
    b = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


# def main():
#     print('thank you for everything ...')

#     for i in range(0, 100):
#         print(cached_fib(i))


# if __name__ == '__main__':
#     main()
