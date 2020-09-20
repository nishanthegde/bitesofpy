import os
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve

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
    pass


def exchange_rates(
        start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    pass


def main():
    print("thank you for looking after my mama...")
    start = date(2020, 1, 1)
    end = date(2020, 9, 1)
    print(get_all_days(start, end))


if __name__ == "__main__":
    main()
