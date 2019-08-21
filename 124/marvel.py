from collections import namedtuple
from itertools import groupby
import csv
import re

from collections import defaultdict

import requests

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')

# csv parsing code provided so this Bite can focus on the parsing


def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


data = list(load_data())

# start coding


def most_popular_characters(top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)"""
    appeared = [x for x in data if x.appearances]
    # print(len(appeared))
    appeared = sorted(appeared, key=lambda x: int(x.appearances), reverse=True)

    return [a.name for a in appeared][:top]


def max_and_min_years_new_characters():
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)"""
    with_years = [(x.year, x.name) for x in data if x.year]

    # for key, group in groupby(with_years, key=lambda x: x.year):
    #     print(key, [j for j in group])

    years = defaultdict(list)

    for year, name in with_years:
        years[year].append(name)

    years = {k: len(v) for k, v in years.items()}
    years_sorted = sorted(years.items(), key=lambda x: x[1], reverse=True)

    return (years_sorted[:1][0][0], years_sorted[-1:][0][0])


def percentage_female():
    """Get the percentage of female characters as percentage of all characters, rounded to 2 digits"""
    all_chars = len(data)
    fem_chars = len([c for c in data if c.sex == 'Female Characters'])

    return round((fem_chars / all_chars) * 100, 2)


# def main():
#     # print(data[:5])
#     actual = most_popular_characters()
#     # print(actual)
#     expected = ['Spider-Man', 'Captain America', 'Wolverine', 'Iron Man', 'Thor']
#     # print(expected)
#     assert actual == expected

#     ret = max_and_min_years_new_characters()
#     # print(ret)
#     expected = ('1993', '1958')
#     # print(expected)
#     assert ret == expected

#     assert percentage_female() == 23.43


# if __name__ == "__main__":
#     main()
