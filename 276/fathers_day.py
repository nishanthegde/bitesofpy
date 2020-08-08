from pathlib import Path
from urllib.request import urlretrieve
from dateutil.parser import parse
import os
from collections import defaultdict

CALENDAR_OUTPUT = """February 23
- Russia

March 19
- Andora
- Bolivia
- Honduras
- Italy
- Liechtenstein
- Portugal
- Spain

May 10
- Romania

May 21
- Germany

June 7
- Austria
- Belgium

June 14
- U.S.
- Canada
- U.K.

June 17
- El Salvador
- Guatemala

June 21
- Egypt
- Jordan
- Lebanon
- Syria
- Uganda

June 23
- Nicaragua
- Poland

August 9
- Samoa
- Brazil

September 6
- Fiji
- New Guinea
- Australia
- New Zealand

November 8
- Estonia
- Finland
- Iceland
- Norway
- Sweden"""

# get the data
tmp = Path('/tmp')
# tmp = Path(os.getcwd())
base_url = 'https://bites-data.s3.us-east-2.amazonaws.com/'

fathers_days_countries = tmp / 'fathers-day-countries.txt'
fathers_days_recurring = tmp / 'fathers-day-recurring.txt'

for file_ in (fathers_days_countries, fathers_days_recurring):
    if not file_.exists():
        urlretrieve(base_url + file_.name, file_)


def _parse_father_days_per_country(year, filename=fathers_days_countries):
    """Helper to parse fathers_days_countries"""
    f_days = {}
    with open(filename) as f:
        for line in f:
            if '* ' in line:
                l = [li.replace('*', '').replace('and ', '').strip() for li in line.split(',')]
            if '{}: '.format(str(year)) in line:
                d = line.split(':')[1].strip()
                if d in f_days.keys():
                    f_days[d] += l
                else:
                    f_days[d] = l

    return f_days


def _parse_recurring_father_days(filename=fathers_days_recurring):
    """Helper to parse fathers_days_recurring"""
    f_days = defaultdict(list)
    with open(filename) as f:
        for line in f:
            if '* ' in line:
                d = line.split('*')[1].strip()
            if line[0].isupper():
                f_days[d].append(line.strip())

    return dict(f_days)


def get_father_days(year=2020):
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    d1 = _parse_father_days_per_country(year)
    d2 = _parse_recurring_father_days()

    return {**d1, **d2}


def generate_father_day_planning(father_days=None):
    if father_days is None:
        father_days = get_father_days()
    i = 0
    for k, v in sorted(father_days.items(), key=lambda t: parse(t[0])):
        if i == 0:
            print('{}'.format(k))
        else:
            print('\n{}'.format(k))
        for elem in v:
            print('- {}'.format(elem))
        i+=1


def main():
    father_days = get_father_days(year=2022)
    # print(father_days)
    generate_father_day_planning()


if __name__ == "__main__":
    main()
