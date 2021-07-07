import json
from dateutil.tz import gettz
from datetime import date, timedelta, tzinfo
from pathlib import Path
from typing import Tuple, Optional, List
import os
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile

DATA_FILE_NAME = "test1.json"
local = os.getcwd()
# TMP = Path(os.getenv("TMP", "/tmp"))
TMP = Path(os.getenv("TMP", local))
DATA_PATH = TMP / DATA_FILE_NAME
MY_TZ = gettz("America/New York")
UTC = gettz("UTC")
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


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
    pass


if __name__ == "__main__":
    # streak = longest_streak()
    # print(f"My longest streak went from {streak[0]} through {streak[1]}")
    # print(f"The streak lasted {(streak[1] - streak[0]).days + 1} days")

    print("thank you for looking after my loved ones...")
    data_zipfile = 'bite328_test_data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
