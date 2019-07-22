from collections import namedtuple
from datetime import datetime, date
import time

import feedparser

# import os

# local = os.getcwd()
# file = os.path.join(local, 'py_feed.txt')

FEED = 'http://projects.bobbelderbos.com/pcc/all.rss.xml'
Entry = namedtuple('Entry', 'date title link tags')

class AttrDict(dict):
    """feedparser lets you access dict keys as attributes, hence a bit of
       mocking, got this from https://stackoverflow.com/a/14620633"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

dt1 = datetime(2018, 2, 18, 19, 52, 0).timetuple()
dt2 = datetime(2017, 1, 6, 11, 0, 0).timetuple()

MOCK_ENTRIES = AttrDict({'entries':
                [AttrDict({'author': 'PyBites',
                           'link':
                           'https://pybit.es/twitter_digest_201808.html',  # noqa E501
                           'published': 'Sun, 18 Feb 2018 20:52:00 +0100',  # noqa E501
                           'published_parsed': dt1,
                           'summary': 'Every weekend we share ...',
                           'tags': [AttrDict({'term': 'twitter'}),
                                    AttrDict({'term': 'Flask'}),
                                    AttrDict({'term': 'Python'}),
                                    AttrDict({'term': 'Regex'})],
                           'title': 'Twitter Digest 2018 Week 08'}),
                 AttrDict({'author': 'Julian',
                           'link': 'https://pybit.es/pyperclip.html',
                           'published': 'Fri, 06 Jan 2017 12:00:00 +0100',  # noqa E501
                           'published_parsed': dt2,
                           'summary': 'Use the Pyperclip module to ...',
                           'tags': [AttrDict({'term': 'python'}),
                                    AttrDict({'term': 'tips'}),
                                    AttrDict({'term': 'tricks'}),
                                    AttrDict({'term': 'code'}),
                                    AttrDict({'term': 'pybites'})],
                           'title': 'Copy and Paste with Pyperclip'})]})




def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(stime.tm_year, stime.tm_mon, stime.tm_mday)


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
        Return a list of Entry namedtuples (date = date, drop time part)
    """

    feed = feedparser.parse(feed)

    #initiate list to return Entry = namedtuple('Entry', 'date title link tags') namedtuples
    entries = []

    try:
    #loop through entries list
      for i in range(0,len(feed['entries'])):
        dt = _convert_struct_time_to_dt(feed['entries'][i]['published_parsed'])
        title = feed['entries'][i]['title']
        link = feed['entries'][i]['link']
        #list of tags
        tags = [feed['entries'][i]['tags'][t]['term'].lower() for t in range(0, len(feed['entries'][i]['tags']))]
        entries.append(Entry(date=dt, title=title, link=link, tags=tags))

      return entries

    except TypeError:
      print ('invalid argument type')

def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    if "&" in search:
      return all(x.lower() in getattr(entry, "tags") for x in search.split('&'))
    elif "|" in search:
      return any(x.lower() in getattr(entry, "tags") for x in search.split('|'))
    else:
      return search.lower() in getattr(entry, "tags")

    return False

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries **
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date desc
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """

    entries  = get_feed_entries()

    term = ''
    while True:
      term = input('Search for (q for exit): ')

      if term == '':
        print('Please provide a search term\n')

      if term.lower() == 'q':
        print('Bye')
        break

      if term:
        hits = sorted([(entry.date.strftime("%Y-%m-%d"), entry.title, entry.link) for entry in entries if filter_entries_by_tag(term.lower(), entry)], key=lambda x:x[0])

        for h in hits:
          print("{} | {} | {}".format(h[0], h[1], h[2]))

        if len(hits) == 1:
          print('\n{} entry matched "{}"\n'.format(len(hits),term))
        else:
          print('\n{} entries matched "{}"\n'.format(len(hits),term))

    # entry = Entry(date=date(2016, 12, 22),
    #               title='2016 py articles and useful books',
    #               link='https://pybit.es/py-articles-books2016.html',
    #               tags={'pythonic', 'data science',
    #                     'tips', 'tricks', 'matplotlib',
    #                     'pandas', 'books', 'collections'})
    # arg = 'TRICKS'
    # print(filter_entries_by_tag(arg, entry))

if __name__ == '__main__':
    main()
