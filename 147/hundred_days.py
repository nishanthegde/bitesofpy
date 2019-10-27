from datetime import date, timedelta

from dateutil.rrule import DAILY, rrule, MO, TU, WE, TH, FR

TODAY = date(year=2018, month=11, day=29)


OTHER_START_DATE = TODAY + timedelta(days=55)


def get_hundred_weekdays(start_date: date = TODAY) -> list:
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    ret = list(rrule(freq=DAILY, count=100, dtstart=start_date, byweekday=(MO, TU, WE, TH, FR)))
    return [d.date() for d in ret]


# def main():
#     print('thank you ...')
#     days = get_hundred_weekdays(start_date=TODAY)
#     # print(len(days))
#     # print(days[0])
#     assert len(days) == 100
#     assert days[0] == TODAY
#     assert days[-1] == date(2019, 4, 17)
#     assert days[1] == date(2018, 11, 30)
#     assert days[2] == date(2018, 12, 3)
#     fri_index = days.index(date(2019, 1, 18))
#     assert days[fri_index + 1] == date(2019, 1, 21)

#     days = get_hundred_weekdays(start_date=OTHER_START_DATE)
#     assert len(days) == 100
#     # check start and end dates
#     assert days[0] == OTHER_START_DATE
#     assert days[-1] == date(2019, 6, 11)
#     # check if weekends are not included
#     assert days[2] == date(2019, 1, 25)
#     assert days[3] == date(2019, 1, 28)
#     fri_index = days.index(date(2019, 6, 7))
#     assert days[fri_index + 1] == date(2019, 6, 10)


# if __name__ == '__main__':
#     main()
