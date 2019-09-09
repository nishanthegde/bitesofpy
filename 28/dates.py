import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/dates/'
RSS_FEED = 'all.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'

# TMP = os.getcwd()


def _get_dates():
  """Downloads PyBites feed and parses out all pub dates returning
     a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
     'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
  remote = os.path.join(BASE_URL, RSS_FEED)
  local = os.path.join(TMP, RSS_FEED)
  urlretrieve(remote, local)

  with open(local) as f:
    return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str):
  """Receives a date str and convert it into a datetime object"""

  date_dt = datetime.strptime(date_str[:-6].strip(), '%a, %d %b %Y %H:%M:%S')
  # print(date_dt)

  return date_dt


def get_month_most_posts(dates):
  """Receives a list of datetimes and returns the month (format YYYY-MM)
     that occurs most"""
  posts = [d.strftime('%Y-%m') for d in dates]

  return max(set(posts), key=posts.count)


# def main():

#   date_strings = ['Thu, 04 May 2017 20:46:00 +0200', 'Wed, 22 Mar 2017 12:42:00 +0100',
#                   'Mon, 20 Feb 2017 00:01:00 +0100', 'Sun, 07 Jan 2018 12:00:00 +0100',
#                   'Sat, 15 Apr 2017 01:00:00 +0200']

#   date_dts = [datetime(2017, 5, 4, 20, 46), datetime(2017, 3, 22, 12, 42), datetime(2017, 2, 20, 0, 1),
#               datetime(2018, 1, 7, 12, 0), datetime(2017, 4, 15, 1, 0)]

#   actuals = [convert_to_datetime(d) for d in date_strings]

#   for i in range(0, len(date_dts)):
#     assert actuals[i] == date_dts[i]

#   dates = _get_dates()
#   converted_dates = [convert_to_datetime(d) for d in dates]
#   assert get_month_most_posts(converted_dates) == '2017-01'

#   for _ in range(25):
#     dates.append('Sun, 07 Jan 2018 12:00:00 +0100')

#   converted_dates = [convert_to_datetime(d) for d in dates]
#   assert get_month_most_posts(converted_dates) == '2018-01'


# if __name__ == '__main__':
#   main()
