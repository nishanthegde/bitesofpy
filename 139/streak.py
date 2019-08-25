from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)


def extract_dates(data):
  """Extract unique dates from DB table representation as shown in Bite"""
  dates = []

  date_regex = re.compile(r'(\d+-\d+-\d+)', re.MULTILINE)

  for match in date_regex.finditer(data):
    dates.append(datetime.strptime(match.group(1), '%Y-%m-%d').date())

  return sorted(list(set(dates)), reverse=True)
  # return sorted(list(set(dates)))


def calculate_streak(dates):
  """Receives sequence (set) of dates and returns number of days
     on coding streak.

     Note that a coding streak is defined as consecutive days coded
     since yesterday, because today is not over yet, however if today
     was coded, it counts too of course.

     So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
     the table makes for a 3 days coding streak.

     See the tests for more examples that will be used to pass your code.
  """
  yesterday = TODAY + timedelta(days=-1)
  streak = []

  for i, d in enumerate(dates):

    if i == 0 and (d == TODAY or d == yesterday):
      current_date = d
      # print(i, d)
      streak.append(d)
      continue
    else:
      if i != 0 and d == current_date + timedelta(days=-1):
        current_date = d
        # print(i, d)
        streak.append(d)
        continue
      else:
        break

  return len(streak)


# def main():
#   """
#     Here is what you need to do:

#     Complete extract_dates to extract date (not datetime) objects.
#     Complete calculate_streak that takes those date objects and returns the streak in (int) days.
#     Calculate back from TODAY that is set to date(2018, 11, 12). Note that a streak can be > 0 if today or yesterday is in the date range.
#     This is because we don't assume today to be over yet, so if yesterday was coded that is a valid continuation of a streak.
#     If today was coded that counts towards the streak too of course.
#   """

#   dates = extract_dates(data)

#   # assert len(dates) == 8  # one less = deduped 2018-09-18
#   # assert date(2018, 9, 18) in dates
#   # assert date(2018, 10, 23) in dates
#   # assert date(2018, 11, 9) in dates

#   # dates = extract_dates(data)
#   # streak = calculate_streak(dates)
#   # assert streak == 0

#   dates = extract_dates(data)
#   streak = calculate_streak(dates)
#   assert streak == 5


# if __name__ == "__main__":
#   main()
