import os
from datetime import date, timedelta, datetime
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
import json

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
local = os.getcwd()
# local =  "/tmp"
TMP = Path(os.getenv("TMP", local))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    st_date = start_date
    end_date = end_date

    return [st_date + timedelta(days=d) for d in range((end_date - st_date).days + 1)]


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    return_value: Dict[str, str] = dict()

    date_keys = [datetime.strptime(k, '%Y-%m-%d').date() for k in daily_rates.keys()]

    base_date = get_all_days(start, end)[0]

    for d in get_all_days(start, end):
        if d in date_keys:
            return_value[d] = d
            base_date = d
        else:
            return_value[d] = base_date

    return return_value

def exchange_rates(
        start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    pass


def main():
    print("thank you for looking after my mama...")
    start = date(2020, 1, 1)
    end = date(2020, 9, 1)
    # print(len(get_all_days(start, end)))
    # print(get_all_days(start, end))

    daily_rates = json.loads(RATES_FILE.read_text())["rates"]

    m = match_daily_rates(start, end, daily_rates)
    print(m[date(2020, 5, 3)])


if __name__ == "__main__":
    main()
