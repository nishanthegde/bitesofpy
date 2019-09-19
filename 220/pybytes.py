from collections import namedtuple, Counter
import re
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'http://projects.bobbelderbos.com/pcc/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


REAL_PYTHON = "realpython.com"
PYBITES = 'pybit.es'


def get_sec(dur_str):
  """Get Seconds from time."""
  h, m, s = dur_str.split(':')
  return int(h) * 3600 + int(m) * 60 + int(s)


def get_mean_list(lst):
  return sum(lst) / len(lst)


def get_ts_str(secs):
  m, s = divmod(secs, 60)
  h, m = divmod(m, 60)

  return ('{:02d}:{:02d}:{:02d}'.format(h, m, s))


class PythonBytes:

  def __init__(self, url=URL):
    """Load the feed url into self.entries using the feedparser module."""
    d = feedparser.parse(url)
    self.entries = d['entries']

  def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
    """Return a list of episode IDs (itunes_episode attribute) of the
       episodes the pass in domain was mentioned in.
    """
    return [e.itunes_episode for e in self.entries if domain in e.description]

  def get_most_mentioned_domain_names(self, n: int = 15) -> list:
    """Get the most mentioned domain domains. We match a domain using
       regex: "https?://[^/]+" - make sure you only count a domain once per
       episode and ignore domains in IGNORE_DOMAINS.
       Return a list of (domain, count) tuples (use Counter).
    """
    all_domains = []

    for e in self.entries:
      entry_domains = []
      desc = e.description
      # matches = re.findall(r'"(https?://[^/]*)/', desc, re.MULTILINE)
      matches = re.findall(r'https?://[^/]+', desc, re.MULTILINE)

      for m in matches:
        if m not in IGNORE_DOMAINS:
          entry_domains.append(m)

      for d in list(set(entry_domains)):
        all_domains.append(d)

    return Counter(all_domains).most_common(n)

  def number_episodes_with_special_guest(self) -> int:
    """Return the number of episodes that had one of more special guests
       featured (use SPECIAL_GUEST).
    """
    sp_guest_eps = [e.title for e in self.entries if SPECIAL_GUEST in e.description]

    if sp_guest_eps:
      return len(sp_guest_eps)

  def get_average_duration_episode_in_seconds(self) -> NamedTuple:
    """Return the average duration in seconds of a Python Bytes episode, as
       well as the shortest and longest episode in hh:mm:ss notation.
       Return the results using the Duration namedtuple.
    """
    ep_dur_secs = [get_sec(e.itunes_duration) for e in self.entries]

    min_ep_dur_str = get_ts_str(min(ep_dur_secs))
    max_ep_dur_str = get_ts_str(max(ep_dur_secs))

    mean_ep_dur_secs = int(get_mean_list([get_sec(e.itunes_duration) for e in self.entries]))

    return Duration(mean_ep_dur_secs, max_ep_dur_str, min_ep_dur_str)


# def main():
#   print('here!')

#   pb = PythonBytes(URL)

#   actual = pb.get_episode_numbers_for_mentioned_domain(PYBITES)
#   expected = ['106', '98', '34', '26', '14']
#   assert sorted(actual) == sorted(expected)

#   actual = pb.get_episode_numbers_for_mentioned_domain(REAL_PYTHON)
#   expected = ['143', '134', '123', '119', '118', '114', '110', '102',
#               '100', '97', '88', '86', '85', '84', '83', '82', '80', '76',
#               '75', '71', '66', '56', '37', '20', '7']
#   assert sorted(actual) == sorted(expected)

#   actual = pb.get_most_mentioned_domain_names()
#   expected = [('https://github.com', 120),
#               ('https://www.youtube.com', 50),
#               ('https://medium.com', 38),
#               ('https://www.python.org', 26),
#               ('https://www.reddit.com', 26),
#               ('https://docs.python.org', 25),
#               ('https://realpython.com', 24),
#               ('https://hackernoon.com', 22),
#               ('https://pypi.python.org', 20),
#               ('https://pypi.org', 16),
#               ('https://en.wikipedia.org', 14),
#               ('https://pragprog.com', 13),
#               ('https://docs.pytest.org', 11),
#               ('http://rollbar.com', 11),
#               ('https://dbader.org', 9)]
#   assert actual == expected

#   actual = pb.get_most_mentioned_domain_names(n=5)
#   expected = [('https://github.com', 120),
#               ('https://www.youtube.com', 50),
#               ('https://medium.com', 38),
#               ('https://www.python.org', 26),
#               ('https://www.reddit.com', 26)]
#   assert actual == expected

#   actual = pb.number_episodes_with_special_guest()
#   expected = 17
#   assert actual == expected

#   org_entries = pb.entries
#   pb.entries = pb.entries[:20]
#   actual = pb.number_episodes_with_special_guest()
#   expected = 7
#   pb.entries = org_entries  # pb is module scope so restore entries
#   assert actual == expected

#   actual = pb.get_average_duration_episode_in_seconds()
#   max_, min_ = '00:56:54', '00:15:27'
#   expected = Duration(avg=1439, max_=max_, min_=min_)
#   # depending the way mean is calculated, results might differ
#   expected_alt = Duration(avg=1442, max_=max_, min_=min_)
#   assert actual in (expected, expected_alt)

#   num_half_episodes = int(len(pb.entries) / 2)
#   org_entries = pb.entries
#   pb.entries = pb.entries[:num_half_episodes]
#   actual = pb.get_average_duration_episode_in_seconds()
#   # print(actual)
#   max_, min_ = '00:56:54', '00:16:40'
#   expected = Duration(avg=1606, max_=max_, min_=min_)
#   # depending the way mean is calculated, results might differ
#   expected_alt = Duration(avg=1607, max_=max_, min_=min_)
#   pb.entries = org_entries  # pb is module scope so restore entries
#   assert actual in (expected, expected_alt)


# if __name__ == '__main__':
#   main()
