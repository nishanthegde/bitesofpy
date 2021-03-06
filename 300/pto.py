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
    # get number of weekends to subtract because holiday of US holidays for year

    holidays = list()

    # for hol in holidays.UnitedStates(years=year).items():
    for i, hol in enumerate(FEDERAL_HOLIDAYS):
        # print(hol, calendar.day_name[hol.weekday()])
        if calendar.day_name[hol.weekday()] in ('Friday', 'Monday'):
            holidays.append(hol)

    # print(holidays)

    # get number of weekends left in year from start_month
    weekends = list()

    # day_range = calendar.monthrange(year, start_month)
    start_date = date(year, start_month, 1)
    end_date = date(year, 12, 31)

    for i in range((end_date - start_date).days + 1):
        if calendar.day_name[(start_date + timedelta(days=i)).weekday()] in ('Friday', 'Monday'):
            weekends.append(start_date + timedelta(days=i))

    if calendar.day_name[weekends[0].weekday()] == 'Monday':
        weekends = weekends[1:]

    if calendar.day_name[weekends[-1].weekday()] == 'Friday':
        weekends = weekends[:-1]

    # print(weekends)

    take_out_days = list()

    for i, w in enumerate(weekends):
        if w in holidays:
            if (w - weekends[i - 1]).days == 3:
                take_out_days.append(weekends[i - 1])
                take_out_days.append(w)
            if (weekends[i + 1] - w).days == 3:
                take_out_days.append(w)
                take_out_days.append(weekends[i + 1])
            # print(w, weekends[i - 1], (w - weekends[i - 1]).days, weekends[i + 1], (weekends[i + 1]-w).days)

    # print(take_out_days)
    # print(AT_HOME)

    four_day_weekends = [w for w in weekends if w not in take_out_days]

    if (paid_time_off // 8) + 1 < len(four_day_weekends):
        ast = four_day_weekends[:(-paid_time_off // 8) + 1][-1]
    else:
        ast = None

    if show_workdays == False:
        # print(ast)
        print("  {} Four-Day Weekends".format(len(four_day_weekends) // 2))
        print("========================")
        print("    PTO: {} ({} days)".format(paid_time_off, paid_time_off // 8))
        print("    BALANCE: {} ({} days)".format(paid_time_off - (len(four_day_weekends) * 8),
                                                 abs((paid_time_off - (len(four_day_weekends) * 8)) // 8)))
        print()
        it = iter(four_day_weekends)
        for x in it:
            next_date = next(it)
            if ast and ast in (x, next_date):
                print('{} - {} *'.format(x, next_date))
            else:
                print('{} - {}'.format(x, next_date))
    else:
        work_days = list()
        for i in range((end_date - start_date).days + 1):
            if (start_date + timedelta(days=i)).weekday() not in AT_HOME and start_date + timedelta(
                    days=i) not in four_day_weekends and start_date + timedelta(
                days=i) not in holidays and start_date + timedelta(
                days=i) not in FEDERAL_HOLIDAYS:
                work_days.append(start_date + timedelta(days=i))
        # print(work_days)
        work_days_remaining = len(work_days)
        print("Remaining Work Days: {} ({} days)".format(work_days_remaining * 8, work_days_remaining))
        it = iter(work_days)
        for x in it:
            print(x)


if __name__ == "__main__":
    four_day_weekends()
