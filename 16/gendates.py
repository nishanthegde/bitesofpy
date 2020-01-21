from datetime import datetime
from datetime import timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    a = PYBITES_BORN
    hundred_day_counter = 0
    num_years_completed = 0
    flag = False
    while True:
        hundred_day_counter += 1
        if hundred_day_counter > 3:
            hundred_day_counter = 0
            a += timedelta(days=(65 - (num_years_completed * 35)))
            num_years_completed += 1
            flag = True
        else:
            if not flag:
                a += timedelta(days=100)
            else:
                a += timedelta(num_years_completed * 35)
                hundred_day_counter = 0
                flag = False
        yield a


def fib_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    print('thank you for everything that you have given me...')
    # print(list(islice(fib_gen(), 3)))
    print(list(islice(gen_special_pybites_dates(), 10)))
    # print(datetime(2019, 1, 23, 0, 0) - datetime(2018, 11, 19, 0, 0))

 # expected = [datetime(2017, 3, 29, 0, 0),
 #                datetime(2017, 7, 7, 0, 0),
 #                datetime(2017, 10, 15, 0, 0),
 #                datetime(2017, 12, 19, 0, 0),  # PyBites 1 year old
 #                datetime(2018, 1, 23, 0, 0),
 #                datetime(2018, 5, 3, 0, 0),
 #                datetime(2018, 8, 11, 0, 0),
 #                datetime(2018, 11, 19, 0, 0),
 #                datetime(2018, 12, 19, 0, 0),  # PyBites 2 years old
 #                datetime(2019, 2, 27, 0, 0)]


if __name__ == '__main__':
    main()
