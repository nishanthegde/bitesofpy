from pathlib import Path
from urllib.request import urlretrieve
import os
from collections import defaultdict

import xml.etree.ElementTree as ET

EXPECTED = {'High income': ['Aruba',
                            'Argentina',
                            'Antigua and Barbuda',
                            'Bahamas, The',
                            'Barbados',
                            'Chile',
                            'Curacao',
                            'Cayman Islands',
                            'St. Kitts and Nevis',
                            'St. Martin (French part)',
                            'Panama',
                            'Puerto Rico',
                            'Sint Maarten (Dutch part)',
                            'Turks and Caicos Islands',
                            'Trinidad and Tobago',
                            'Uruguay',
                            'British Virgin Islands',
                            'Virgin Islands (U.S.)'],
            'Low income': ['Haiti'],
            'Lower middle income': ['Bolivia',
                                    'Honduras',
                                    'Nicaragua',
                                    'El Salvador'],
            'Upper middle income': ['Belize',
                                    'Brazil',
                                    'Colombia',
                                    'Costa Rica',
                                    'Cuba',
                                    'Dominica',
                                    'Dominican Republic',
                                    'Ecuador',
                                    'Grenada',
                                    'Guatemala',
                                    'Guyana',
                                    'Jamaica',
                                    'St. Lucia',
                                    'Mexico',
                                    'Peru',
                                    'Paraguay',
                                    'Suriname',
                                    'St. Vincent and the Grenadines',
                                    'Venezuela, RB']}

# import the countries xml file
# local = os.getcwd()
local = '/tmp'
tmp = Path(local)
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """

    incomes = []
    names = []

    ret = dict()

    tree = ET.parse(xml)
    root = tree.getroot()

    # tags = [elem.tag for elem in root.iter()]

    for x in root.iter():
        if 'incomeLevel' in x.tag:
            incomes.append(x.text)

        if 'name' in x.tag:
            names.append(x.text)

    zipped = list(zip(incomes, names))

    [ret[t[0]].append(t[1]) if t[0] in list(ret.keys()) else ret.update({t[0]: [t[1]]}) for t in zipped]

    return ret


# def main():
#     # print('here')
#     actual = get_income_distribution()

#     for income, countries in EXPECTED.items():
#         print(countries)
#         assert income in actual
#         assert sorted(actual[income]) == sorted(countries)
#     # print(get_income_distribution())


# if __name__ == '__main__':
#     main()
