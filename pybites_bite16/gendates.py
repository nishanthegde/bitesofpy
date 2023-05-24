from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates(loops=10):
    new_date = PYBITES_BORN
    for i in range(loops):
        new_date = new_date + timedelta(days=100)
        yield new_date
