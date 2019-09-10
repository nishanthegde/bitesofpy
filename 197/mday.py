from datetime import date


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    # loop over every day in May of the year

    count = 0

    for i in range(1, 32):
        d = date(year, 5, i)
        if d.weekday() == 6:
            count += 1
        if count == 2:
            return d


# def main():
#     print(get_mothers_day_date(2021))


# if __name__ == '__main__':
#     main()
