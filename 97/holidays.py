from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

# local = os.getcwd()
local = '/tmp'
# prep data
holidays_page = os.path.join(local, 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = Soup(content, 'html.parser')

    table = soup.find('table', attrs={'class': 'list-table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        holidays[cols[1][5:7]].append(cols[3])

    return holidays


# def main():
#     print('here ...')
#     ret = get_us_bank_holidays()
#     # print(type(ret))
#     print(ret.get("11"))


# if __name__ == '__main__':
#     main()
