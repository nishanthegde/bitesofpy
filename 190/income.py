from pathlib import Path
from urllib.request import urlretrieve

# import the countries xml file
tmp = Path('/tmp')
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
    pass