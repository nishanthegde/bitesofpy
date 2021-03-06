import json
from dateutil.tz import gettz
from datetime import date, timedelta, tzinfo, datetime
from pathlib import Path
from typing import Tuple, Optional, List
import os
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile

DATA_FILE_NAME = "test4.json"
local = os.getcwd()
# TMP = Path(os.getenv("TMP", "/tmp"))
TMP = Path(os.getenv("TMP", local))
DATA_PATH = TMP / DATA_FILE_NAME
from_zone = gettz('UTC')
MY_TZ = gettz("America/New York")
UTC = gettz("UTC")
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"

RESULTS = [
    (date(2019, 10, 10), date(2019, 10, 11)),
    (date(2019, 10, 13), date(2019, 10, 14)),
    None,
    (date(2019, 10, 1), date(2019, 10, 1)),
]

RESULTS_UTC = [
    (date(2019, 10, 9), date(2019, 10, 13)),
    (date(2019, 10, 9), date(2019, 10, 14)),
    None,
    (date(2019, 10, 2), date(2019, 10, 2)),
]
PATHS = [TMP / f"test{x}.json" for x in range(1, 5)]


def longest_streak(
        data_file: Path = DATA_PATH, my_tz: Optional[tzinfo] = MY_TZ
) -> Optional[Tuple[date, date]]:
    """Retrieve datetime strings of passed commits and calculate the longest
    streak from the user's data

    Note: The datetime strings will need to be used to create aware datetime objects

    All datetimes are in UTC, and the timezone of the user is part of the context
    for calculating a streak. Ex: 2019-10-14 01:58:48.129585+00:00 is 2019-10-13 in
    New York City. You will need to convert datetimes from UTC into the supplied timezone.

    The tests show an example of how a streak can change based on the timezone used.

    If the dataset has two or more streaks of the same length as longest, provide
    only the most recent streak.

    Return a tuple containing start and end date for the longest streak
    or None
    """
    with open(data_file) as f:
        data = json.load(f)

    # You code from here
    commit_dates = [datetime.strptime(c['date'].strip(), "%Y-%m-%d %H:%M:%S.%f%z").replace(tzinfo=from_zone) for c in
                    data['commits'] if c['passed'] == True]
    commit_dates = [d.astimezone(MY_TZ).date() for d in commit_dates]

    unique_dates = sorted(list(set(commit_dates)))

    i = 0
    max_days = 0
    day_count = 0

    if unique_dates:
        prev_date = unique_dates[0]
        for curr_date in unique_dates:

            if (curr_date - prev_date).days == 1:
                day_count += 1
            else:
                day_count = 0

            if day_count >= max_days:
                max_days = day_count
                end_date = curr_date
            prev_date = curr_date

        start_idx = unique_dates.index(end_date) - max_days
        end_idx = unique_dates.index(end_date)

        return unique_dates[start_idx], unique_dates[end_idx]


if __name__ == "__main__":
    print("thank you for looking after my mama...")
    # print(f"My longest streak went from {streak[0]} through {streak[1]}")
    # print(f"The streak lasted {(streak[1] - streak[0]).days + 1} days")
    # data_zipfile = 'bite328_test_data.zip'
    # urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    # ZipFile(TMP / data_zipfile).extractall(TMP)
