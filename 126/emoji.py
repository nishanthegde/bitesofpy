import sys
import unicodedata
import os

from pathlib import Path
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as Soup


START_EMOJI_RANGE = 100000  # estimate

# out_dir = os.getcwd()
out_dir = "/tmp"
html_file = f"{out_dir}/emoji.html"

HTML_FILE = Path(html_file)
URL = "https://apps.timwhitlock.info/emoji/tables/unicode#"


def what_means_emoji(emoji):
  """Receives emoji and returns its meaning,
     in case of a TypeError return 'Not found'"""
  try:
    return unicodedata.name(emoji)
  except TypeError:
    return 'Not found'


def _make_emoji_mapping():
  """Helper to make a mapping of all possible emojis:
     - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
     - return dict with keys=emojis, values=names"""

  all_byte_strings = [chr(c).encode('utf-8') for c in range(START_EMOJI_RANGE, sys.maxunicode + 1)]
  # return ['U+{:X}'.format(c) for c in range(START_EMOJI_RANGE, START_EMOJI_RANGE + 10)]
  soup = get_soup()
  emoji_byte_strings = get_emoji_byte_strings(soup)

  emoji_keys = [e.decode('utf-8') for e in all_byte_strings if e in emoji_byte_strings]

  emoji_mapping = {k: what_means_emoji(k).lower() for k in emoji_keys}

  return emoji_mapping


def find_emoji(term):
  """Return emojis and their texts that match (case insensitive)
     term, print matches to console"""
  term = term.lower()

  emoji_mapping = _make_emoji_mapping()

  emoji_hits = {k: v for k, v in emoji_mapping.items() if term in v}

  if emoji_hits:
    max_buffer = max([len(name) for name in emoji_hits.values()]) + 5
    for k, v in emoji_hits.items():
      name = v
      name_buffer = ' ' * (max_buffer - len(v))
      emoji = k
      print("{}{}| {}".format(name, name_buffer, emoji))
    return emoji_hits
  else:
    print("no matches")


def get_soup(file=HTML_FILE):
  """Retrieves/takes source HTML and returns a BeautifulSoup object"""
  if isinstance(file, Path):
    if not HTML_FILE.is_file():
      urlretrieve(URL, HTML_FILE)

    with file.open() as html_source:
      soup = Soup(html_source, "html.parser")
  else:
    soup = Soup(file, "html.parser")

  return soup


def get_emoji_byte_strings(soup=get_soup()):

  emoji_byte_strings = []

  soup.prettify()

  tables = soup.find_all("table")

  for t in tables:

    bodies = t.find_all("tbody")

    for b in bodies:

      rows = b.find_all("tr")
      for r in rows:
        cols = r.find_all('td')

        byte_str = cols[7].text

        emoji_byte_strings.append(byte_str.encode().decode('unicode-escape').encode('latin-1'))

  return emoji_byte_strings


def main():
  # print('dance!')

  what_means_emoji('🐶').lower() == 'dog face'
  what_means_emoji('🏋').lower() == 'weight lifter'
  what_means_emoji('🌇').lower() == 'sunset over buildings'

  assert what_means_emoji('aaa').lower() == 'not found'

  # emoji_mapping = _make_emoji_mapping()
  # print(emoji_mapping)

  ret = find_emoji('test')
  print(ret)

  # output = """sunrise over mountains           | 🌄
  #           sunrise                          | 🌅
  #           sunset over buildings            | 🌇
  #           sun with face                    | 🌞
  #           sunflower                        | 🌻
  #           smiling face with sunglasses     | 😎"""

  # assert 'sunrise' in output
  # assert '🌅' in output
  # assert 'sunset over buildings' in output
  # assert '🌇' in output
  # assert 'sun with face' in output
  # assert '🌻' in output


if __name__ == '__main__':
  main()
