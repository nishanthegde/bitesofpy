import json
from dateutil.tz import gettz
from datetime import date, timedelta, tzinfo, datetime
from pathlib import Path
from typing import Tuple, Optional, List
import os
from dateutil.parser import parse

from urllib.request import urlretrieve
from zipfile import ZipFile

S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
data_zipfile = 'bite328_test_data.zip'

DATA_FILE_NAME = "test1.json"
TMP = Path(os.getenv("TMP", "/tmp"))
# TMP = Path(os.getenv("TMP", os.getcwd()))
DATA_PATH = TMP / DATA_FILE_NAME
MY_TZ = gettz("America/New York")
UTC = gettz("UTC")


def download_test_files():
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)


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

    download_test_files()

    with open(data_file) as f:
        data = json.load(f)

    passes = sorted([datetime.strptime(b['date'], '%Y-%m-%d %H:%M:%S.%f%z') for b in data['commits'] if b['passed']])
    passes = [datetime.date(p.astimezone(my_tz)) for p in passes]

    if not passes:
        return None
    elif len(passes) == 1:
        return (passes[0], passes[0])
    else:
        streaks = []

        start_date = passes[0]
        end_date = None
        for idx in range(1, len(passes)):
            if (passes[idx] - passes[idx - 1]).days > 1:
                start_date = passes[idx]
            else:
                end_date = passes[idx]
                streaks.append((start_date, end_date, (end_date - start_date).days))

        return sorted(streaks, key=lambda x: (x[2], x[1]), reverse=True)[0][0], \
               sorted(streaks, key=lambda x: (x[2], x[1]), reverse=True)[0][1]


if __name__ == "__main__":
    streak = longest_streak()
    print(f"My longest streak went from {streak[0]} through {streak[1]}")
    print(f"The streak lasted {(streak[1]-streak[0]   ).days + 1} days")
