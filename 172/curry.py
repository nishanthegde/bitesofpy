from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places


def rounder(what, places):
    if places == 0:
        return int(round(what, places))
    else:
        return round(what, places)


rounder_int = partial(rounder, places=0)
rounder_detailed = partial(rounder, places=4)


# def f(a, b, c, x):
#     return 1000 * a + 100 * b + 10 * c + x


# g = partial(f, 2, 1, 3)


# def main():

#     assert rounder_int(1.3434587383) == 1
#     assert rounder_int(10.42342) == 10
#     assert rounder_int(1.99) == 2

#     assert rounder_detailed(1.344587383) == 1.3446
#     assert rounder_detailed(10.42342) == 10.4234
#     assert rounder_detailed(1.99) == 1.9900


# if __name__ == '__main__':
#     main()
