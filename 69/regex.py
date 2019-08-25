import re


def has_timestamp(text):
  """Return True if text has a timestamp of this format:
     2014-07-03T23:30:37"""
  ts_regex = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')
  ts = ts_regex.search(text)

  if ts:
    return True

  return False


def is_integer(number):
  """Return True if number is an integer"""
  int_regex = re.compile(r'^[-+]?[0-9]+$')
  inte = int_regex.search(str(number))

  if inte:
    return True

  return False


def has_word_with_dashes(text):
  """Returns True if text has one or more words with dashes"""
  hyph_regex = re.compile(r'\w+-\w+')
  hyph = hyph_regex.search(text)

  if hyph:
    return True

  return False


def remove_all_parenthesis_words(text):
  """Return text but without any words or phrases in parenthesis:
     'Good morning (afternoon)' -> 'Good morning' (so don't forget
     leading spaces)"""

  # take out paranthesis words
  str1 = re.sub(r'\(\S+\)', '', text)

  # take out white space before punctuation
  str2 = re.sub(r'\s+([^0-9a-zA-Z])', r'\1', str1)

  return str2


def split_string_on_punctuation(text):
  """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
     ['hi', 'how are you doing', 'blabla']
     (make sure you strip trailing spaces)"""
  # take out ?!.,;
  # lst = re.sub(r'([?!.,;])', ' ', text).split()

  lst = re.split(r'([?!.,;])', text)
  lst_filt = list(filter(lambda x: re.findall('[\w]+', x), lst))

  return [thing.strip() for thing in lst_filt]


def remove_duplicate_spacing(text):
  """Replace multiple spaces by one space"""
  return re.sub(r'\s+', ' ', text)


def has_three_consecutive_vowels(word):
  """Returns True if word has at least 3 consecutive vowels"""
  threevow_regex = re.compile(r'[aeiou]{3,}')
  threevow = threevow_regex.search(word)

  if threevow:
    return True

  return False


def convert_emea_date_to_amer_date(date):
  """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
     (AMER date format)"""
  date_regex = re.compile(r'\d{2}\/\d{2}/\d{4}')
  dt = date_regex.search(date)

  if dt:
    return re.sub(r'^(\d{2})\/(\d{2})', r'\g<2>/\g<1>', date)

  return date


# def main():

#   assert has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.')
#   assert has_timestamp('INFO 2014-06-01T13:28:51 Shutdown initiated.')
#   assert not has_timestamp('INFO 2014-7-3T23:27:51 Shutdown initiated.')
#   assert not has_timestamp('INFO 2014-07-03t23:27:1 Shutdown initiated.')

#   assert is_integer(1)
#   assert is_integer(-1)
#   assert not is_integer('str')
#   assert not is_integer(1.1)

#   assert has_word_with_dashes('this Bite is self-contained')
#   assert has_word_with_dashes('the match ended in 1-1')
#   assert not has_word_with_dashes('this Bite is not selfcontained')
#   assert not has_word_with_dashes('the match ended in 1- 1')

#   input_string = 'good morning (afternoon), how are you?'
#   expected = 'good morning, how are you?'

#   assert remove_all_parenthesis_words(input_string) == expected

#   input_string = 'math (8.6) and science (9.1) where his strengths'
#   expected = 'math and science where his strengths'
#   assert remove_all_parenthesis_words(input_string) == expected

#   input_string = 'hi, how are you doing? blabla'
#   expected = ['hi', 'how are you doing', 'blabla']
#   # print(expected)
#   # print(split_string_on_punctuation(input_string))
#   assert split_string_on_punctuation(input_string) == expected

#   input_string = ';String. with. punctuation characters!'
#   expected = ['String', 'with', 'punctuation characters']
#   # print(expected)
#   # print(split_string_on_punctuation(input_string))
#   assert split_string_on_punctuation(input_string) == expected

#   input_string = 'This is a   string with  too    much spacing'
#   expected = 'This is a string with too much spacing'
#   assert remove_duplicate_spacing(input_string) == expected

#   assert has_three_consecutive_vowels('beautiful')
#   assert has_three_consecutive_vowels('queueing')
#   assert not has_timestamp('mountain')
#   assert not has_timestamp('house')

#   assert convert_emea_date_to_amer_date('31/03/2018') == '03/31/2018'
#   assert convert_emea_date_to_amer_date('none') == 'none'

# if __name__ == "__main__":
#   main()
