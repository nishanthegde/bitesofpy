from pathlib import Path
from urllib.request import urlretrieve

from dateutil.parser import parse

# get the data
tmp = Path('/tmp')
base_url = 'https://bites-data.s3.us-east-2.amazonaws.com/'

fathers_days_countries = tmp / 'fathers-day-countries.txt'
fathers_days_recurring = tmp / 'fathers-day-recurring.txt'

for file_ in (fathers_days_countries, fathers_days_recurring):
    if not file_.exists():
        urlretrieve(base_url + file_.name, file_)


def _parse_father_days_per_country(year, filename=fathers_days_countries):
    """Helper to parse fathers_days_countries"""


def _parse_recurring_father_days(filename=fathers_days_recurring):
    """Helper to parse fathers_days_recurring"""


def get_father_days(year=2020):
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    pass


def generate_father_day_planning(father_days=None):
    """Prints all father days in order, example in tests and
       Bite description
    """
    if father_days is None:
        father_days = get_father_days()

    # you code