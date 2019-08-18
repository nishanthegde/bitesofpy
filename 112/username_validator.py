# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re
from typing.re import Pattern

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can Contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can coNtain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string(inp=social_platforms):
  """Convert the social_platforms string above into a dict where
     keys = social platforms name and values = validator namedtuples"""

  #  take out line feeds and strip white space
  inp = inp.replace('\n\n', '\n').strip()

  # dict to return
  platforms = {}

  # extract platform names
  platform_names = []

  pf_matches = re.findall(r'^[\S]*\n', inp, re.MULTILINE)

  for plat in pf_matches:
    platform_names.append(plat.replace('\n', '').lower())

  # extract mins for ranges
  mins = []
  mins_regex = re.compile(r'^\s+Min:\s+([0-9]+)\n', re.MULTILINE)

  for match in mins_regex.finditer(inp):
    min_val = int(match.group(1))
    mins.append(min_val)

  # extract maxs for ranges
  maxs = []
  maxs_regex = re.compile(r'^\s+Max:\s+([0-9]+)\n', re.MULTILINE)

  for match in maxs_regex.finditer(inp):
    max_val = int(match.group(1)) + 1
    maxs.append(max_val)

  ranges = [range(min, max) for min, max in zip(mins, maxs)]

  # extract patterns for username validation
  patterns = []
  pattern_regex = re.compile(r'^\s+can contain:\s+(.*)$', re.IGNORECASE | re.MULTILINE)

  for match in pattern_regex.finditer(inp):
    patterns.append(match.group(1).replace(' ', ''))

  # create regex compile objects from patterns
  validation = [re.compile(r'^[' + s + ']+$') for s in patterns]

  # create validator named tuples from ranges and reg ex compile objects
  # print(platform_names)
  # print(ranges)
  # print(validation)

  tups = [Validator(r, v) for r, v in zip(ranges, validation)]

  # print(tups)

  for i in range(0, len(platform_names)):
    platforms[platform_names[i].capitalize()] = tups[i]

  # return {k.capitalize(): v for k in platform_names for v in tups}

  return(platforms)


def validate_username(platform, username):
  """Receives platforms(Twitter, Facebook or Reddit) and username string,
     raise a ValueError if the wrong platform is passed in,
     return True/False if username is valid for entered platform"""
  platform = platform.lower().capitalize()
  all_validators = parse_social_platforms_string()

  if platform not in all_validators:
    raise ValueError('Platform not identified!')

  validator = all_validators.get(platform)

  # validate length of username
  if len(username) < min(validator.range):
    return False

  if len(username) > max(validator.range):
    return False

  pattern = validator.regex

  if not pattern.match(username):
    return False

  return True


# def main():
#   platforms = parse_social_platforms_string()
#   # print(platforms)
#   assert len(platforms) == 3
#   assert all([type(nw) == Validator for nw in platforms.values()])

#   twitter = platforms.get('Twitter')
#   assert type(twitter.range) == range
#   assert isinstance(twitter.regex, Pattern)

#   # validate_username('Github', 'bob')

#   assert validate_username('Twitter', 'a')
#   assert not validate_username('Twitter', '')
#   assert not validate_username('Twitter', 'a' * 16)
#   assert validate_username('Twitter', 'nhegde')

#   assert validate_username('Twitter', 'bob')
#   assert validate_username('Twitter', 'boB123')
#   assert validate_username('Twitter', 'bo__89A')
#   assert not validate_username('Twitter', 'bob-123')
#   assert not validate_username('Twitter', 'bob@PyBites')
#   assert not validate_username('Twitter', 'bob.')

#   assert validate_username('Facebook', 'abc123')
#   assert not validate_username('Facebook', 'bob')
#   assert not validate_username('Facebook', 'a' * 51)

#   assert validate_username('Facebook', 'bobb.')
#   assert validate_username('Facebook', 'bob.PyBites')
#   assert validate_username('Facebook', 'aAbB123')
#   assert not validate_username('Facebook', 'bobb,')
#   assert not validate_username('Facebook', 'bob$56')
#   assert not validate_username('Facebook', 'bob123_')

#   assert validate_username('Reddit', 'abc')
#   assert not validate_username('Reddit', 'ab')
#   assert not validate_username('Reddit', 'a' * 21)

#   assert validate_username('Reddit', 'bob_PyBites')
#   assert validate_username('Reddit', '-123ABC')
#   assert validate_username('Reddit', '123-abc__')
#   assert not validate_username('Reddit', 'bobb.')
#   assert not validate_username('Reddit', 'bob@PyBites')
#   assert not validate_username('Reddit', 'bob$56')


# if __name__ == '__main__':
#   main()
