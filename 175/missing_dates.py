from datetime import date, timedelta
from random import shuffle


# def _create_dates(missing, year=2019, month=2):
#     """Helper function to build up test cases.

#        Returns a list of dates omitting days given
#        in the missing argument.

#        You can optionally specify year and month.
#     """
#     first = date(year=year, month=month, day=1)
#     last = first.replace(month=month + 1) - timedelta(days=1)

#     # always yield first and last, for the in between dates
#     # only the ones not in missing
#     yield first

#     for day in range(first.day + 1, last.day):
#         if day not in missing:
#             yield first.replace(day=day)

#     yield last

# def _find_missing(l: list) -> list:
#     return [x for x in range(l[0], l[-1] + 1) if x not in l]


def get_missing_dates(dates: list) -> list:
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    # missing = _find_missing([d.day for d in dates])
    # date(day=d,month)
    d = sorted(dates)
    full_set = set(d[0] + timedelta(x) for x in range((d[-1] - d[0]).days + 1))

    missing = sorted(full_set - set(d))
    return missing


# def main():
#     print('thank you for the ocean...')
#     # date_range = [date(year=2019, month=2, day=n) for n in range(1, 11, 2)]
#     # print(date_range)
#     # print(get_missing_dates(date_range))
#     missing = list(range(1, 31))  # list(range(2, 12, 2))  # [2, 7, 11]
#     month = 6
#     my_date_range = list(_create_dates(missing=missing, month=month))
#     # print(my_date_range)
#     start, end = my_date_range[0].day, my_date_range[-1].day
#     # print(start, end)

#     shuffle(my_date_range)

#     # get days from return sequence
#     actual = sorted(d.day for d in get_missing_dates(my_date_range))
#     expected = sorted(d for d in missing if d not in (start, end))

#     print(actual)
#     print(expected)


# if __name__ == '__main__':
#     main()
