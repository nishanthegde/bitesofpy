from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

import re

# local = os.getcwd()
local = '/tmp'
commits = os.path.join(local, 'commits')

urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """

    with open(commit_log, "r") as log:
        data = log.read()

    year_month_changes = {}

    pattern = re.compile(r'^Date:\s+(.*)\s+\|.*?,\s(\d+)(.*?,\s(\d+))?', re.MULTILINE)

    for match in pattern.finditer(data):
        change1 = 0
        change2 = 0

        yr = parse(match.group(1)).year
        mo = parse(match.group(1)).month
        key = YEAR_MONTH.format(y=yr, m=mo)

        if match.group(2):
            change1 = int(match.group(2))
        if match.group(4):
            change2 = int(match.group(4))

        tot_changes = change1 + change2

        if key not in year_month_changes:
            year_month_changes[key] = tot_changes
        else:
            year_month_changes[key] += tot_changes

    if year:
        year_month_changes = {k: v for k, v in year_month_changes.items() if k[:4] == str(year)}

    least_active_month = min(year_month_changes, key=year_month_changes.get)
    most_active_month = max(year_month_changes, key=year_month_changes.get)

    return (least_active_month, most_active_month)


# def main():
#     print('here!')
#     print(type(get_min_max_amount_of_commits(year=2019)))
#     print(get_min_max_amount_of_commits(year=2019))


# if __name__ == '__main__':
#     main()
