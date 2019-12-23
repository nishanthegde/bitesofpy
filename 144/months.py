from datetime import datetime, date

from dateutil.relativedelta import relativedelta

START_DATE = date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH = 10
MONTHS_PER_YEAR = 12


def calc_months_passed(year: int, month: int, day: int) -> int:
  """Construct a date object from the passed in arguments.
     If this fails due to bad inputs reraise the exception.
     Also if the new date is < START_DATE raise a ValueError.

     Then calculate how many months have passed since the
     START_DATE constant. We suggest using dateutil.relativedelta!

     One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
     days in, it counts as an extra  month.

     For example:
     date(2018, 11, 10) = 9 days in => 0 months
     date(2018, 11, 11) = 10 days in => 1 month
     date(2018, 12, 11) = 1 month + 10 days in => 2 months
     date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
     etc.

     See the tests for more examples.

     Return the number of months passed int.
  """
  new_date = date(year, month, day)

  if new_date < START_DATE:
    raise ValueError('date must be after start')
  else:
    r = relativedelta(new_date, START_DATE)

  # if r.days >= MIN_DAYS_TO_COUNT_AS_MONTH:
  #   return r.months + 1

  # if new_date.month > START_DATE.month andnew_date.day >= MIN_DAYS_TO_COUNT_AS_MONTH:
  if r.days >= MIN_DAYS_TO_COUNT_AS_MONTH:
    return r.years * MONTHS_PER_YEAR + r.months + 1

  return r.years * MONTHS_PER_YEAR + r.months


# def main():
#   print('thank you for my mom ...')
#   # print(calc_months_passed(2019, 12, 11))
#   # print(type(calc_months_passed('a', 12, 11)))
#   # print(type(calc_months_passed(2018, 10, 'c')))
#   # print(calc_months_passed(-1000, 11, 1))
#   # print(calc_months_passed(2018, 11, 34))
#   # print(calc_months_passed(2018, 13, 1))
#   # print(calc_months_passed(2018, 10, 1))
#   # print(calc_months_passed(2018, 11, 11))
#   print(calc_months_passed(2018, 11, 10))
#   print(calc_months_passed(2018, 11, 11))
#   print(calc_months_passed(2018, 12, 11))
#   print(calc_months_passed(2019, 12, 11))

#   print(calc_months_passed(2018, 11, 1))
#   print(calc_months_passed(2018, 11, 10))
#   print(calc_months_passed(2018, 11, 11))
#   print(calc_months_passed(2018, 12, 10))
#   print(calc_months_passed(2018, 12, 11))
#   print(calc_months_passed(2019, 12, 10))
#   print(calc_months_passed(2019, 12, 11))


# if __name__ == '__main__':
#   main()
