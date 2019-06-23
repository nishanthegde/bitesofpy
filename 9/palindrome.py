"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request as ur
import re


local = '/tmp'
# local = os.getcwd()
DICTIONARY = os.path.join(local, 'dictionary_m_words.txt')
ur.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)

def prep_word(word):
    """Prep the word for the palindrome test
      1. case insensitive
      3. strip /n
      2. remove non-alpha numeric
      """
    word = word.strip().casefold()
    word = re.sub(r'[^a-zA-Z0-9]','',word)

    return word

def load_dictionary():
    """Load dictionary (sample)
    and return as generator (done)"""
    with open(DICTIONARY,'r') as f:
      return [prep_word(w) for w in f.readlines()]

def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    is_palindrome = False
    if prep_word(word) == prep_word(word[::-1]):
        is_palindrome = True

    return is_palindrome

def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words == None:
      words = load_dictionary()

    pal = [p for p in words if is_palindrome(p)]
    m = max([len(p) for p in pal])

    max_words = [p for p in pal if len(p) == m]
    max_words = sorted(max_words)

    return max_words[0]

# def main():
#     """ main program entry point"""
#     p = get_longest_palindrome()
#     print(p)

# if __name__=="__main__":
#   main()
