import calendar
from datetime import date, timedelta

# import holidays

ERROR_MSG = (
    "Unambiguous value passed, please specify either start_month or show_workdays"
)
FEDERAL_HOLIDAYS = (
    date(2020, 1, 1),
    date(2020, 1, 20),
    date(2020, 2, 17),
    date(2020, 5, 25),
    date(2020, 7, 3),
    date(2020, 7, 4),
    date(2020, 9, 7),
    date(2020, 10, 12),
    date(2020, 11, 11),
    date(2020, 11, 26),
    date(2020, 12, 25),
)
WFH = (calendar.TUESDAY, calendar.WEDNESDAY)
WEEKENDS = (calendar.SATURDAY, calendar.SUNDAY)
AT_HOME = WFH + WEEKENDS


def four_day_weekends(
        *args,
        start_month: int = 8,
        paid_time_off: int = 200,
        year: int = 2020,
        show_workdays: bool = False
) -> None:
    """Generates four day weekend report

    The four day weekends are calculated from the start_month through the end of the year
    along with the number of work days for the same time period. The reports takes into
    account any holidays that might fall within that time period and days designated as
    working from home (WFH).

    If show_workdays is set to True, a report with the work days is generated instead of
    the four day weekend dates.

    Args:
        start_month (int, optional): Month to start. Defaults to 8.
        paid_time_off (int, optional): Paid vacation days
        year (int, optional): Year to calculate, defaults to current year
        show_workdays (bool, optional): Enables work day report. Defaults to False.

    Raises:
        ValueError: ERROR_MSG
    """
    if len(args) > 0:
        raise ValueError(ERROR_MSG)

    if show_workdays == False:
        # generate weekend report

        # get number of weekends to subtract because holiday of US holidays for year

        holidays = list()

        # for hol in holidays.UnitedStates(years=year).items():
        for i, hol in enumerate(FEDERAL_HOLIDAYS):
            print(hol, calendar.day_name[hol.weekday()])
            if calendar.day_name[hol.weekday()] in ('Friday', 'Monday'):
                holidays.append(hol)

        print(holidays)

        # get number of weekends left in year from start_month
        weekends = list()

        # day_range = calendar.monthrange(year, start_month)
        start_date = date(year, start_month, 1)
        end_date = date(year,12,31)

        for i in range((end_date - start_date).days):
            if calendar.day_name[(start_date + timedelta(days=i)).weekday()] in ('Friday', 'Monday'):
                weekends.append(start_date + timedelta(days=i))

        if calendar.day_name[weekends[0].weekday()] == 'Monday':
            weekends = weekends[1:]

        if calendar.day_name[weekends[-1].weekday()] == 'Friday':
            weekends = weekends[:-1]

        print(weekends)

    else:
        print('weekday report')


def main():
    print("thank you for looking after my mama...")


if __name__ == "__main__":
    four_day_weekends()
    main()
