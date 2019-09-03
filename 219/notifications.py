from datetime import date, timedelta

from itertools import islice

# TODAY = date.today()
TODAY = date(2019, 8, 25)


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):

    v = start_date + timedelta(num_days)

    for i in range(num_bites):
        yield v

    start_date += timedelta(num_days)

    while True:
        v = start_date + timedelta(num_days)
        for i in range(num_bites):
            yield v

        start_date += timedelta(num_days)

# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         print(n)
#         yield start_date + timedelta(n)


# def main():
#     print('dance ...')

#     gen = gen_bite_planning(num_bites=2, num_days=3, start_date=TODAY)
#     # for _ in range(10):
#     #     # print(type(next(gen)))
#     #     print(next(gen))
#     # print(next(gen))
#     # print(next(gen))
#     # print(next(gen))

#     # start_date = date(2019, 8, 1)
#     # end_date = date(2019, 8, 10)

#     # gen = daterange(start_date, end_date)

#     # for _ in range(9):
#     #     print(next(gen))

#     gen = gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY)

#     actual = list(islice(gen, 10))

#     expected = [date(2019, 8, 26), date(2019, 8, 27),
#                 date(2019, 8, 28), date(2019, 8, 29),
#                 date(2019, 8, 30), date(2019, 8, 31),
#                 date(2019, 9, 1), date(2019, 9, 2),
#                 date(2019, 9, 3), date(2019, 9, 4)]

#     assert actual == expected

#     gen = gen_bite_planning(num_bites=2, num_days=3, start_date=TODAY)
#     actual = list(islice(gen, 10))
#     expected = [date(2019, 8, 28), date(2019, 8, 28),
#                 date(2019, 8, 31), date(2019, 8, 31),
#                 date(2019, 9, 3), date(2019, 9, 3),
#                 date(2019, 9, 6), date(2019, 9, 6),
#                 date(2019, 9, 9), date(2019, 9, 9)]
#     assert actual == expected

#     gen = gen_bite_planning(num_bites=1, num_days=2, start_date=TODAY)
#     actual = list(islice(gen, 10))
#     expected = [date(2019, 8, 27), date(2019, 8, 29),
#                 date(2019, 8, 31), date(2019, 9, 2),
#                 date(2019, 9, 4), date(2019, 9, 6),
#                 date(2019, 9, 8), date(2019, 9, 10),
#                 date(2019, 9, 12), date(2019, 9, 14)]
#     assert actual == expected


# if __name__ == '__main__':
#     main()
