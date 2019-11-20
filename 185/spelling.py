from difflib import SequenceMatcher
from os import path
from urllib.request import urlretrieve
import os
import string
import operator

# local = os.getcwd()
local = '/tmp'


DICTIONARY = path.join(local, 'dictionary.txt')
if not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


def a_words():
    """Get only a[abcdefghijklm]-words to speed up tests"""
    words = load_words()
    return {word for word in words if word.startswith('a') and len(word) > 1 and word[1] in string.ascii_letters[:13]}


def load_words() -> set:
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        # print(f.readlines())
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""

    ratios = {}

    if words is None:
        words = load_words()

    ratios = {w: SequenceMatcher(None, misspelled_word.lower(), w).ratio() for w in words}

    return max(ratios.items(), key=operator.itemgetter(1))[0]


# def main():
#     print('thank you for the people I know...')
#     # print(type(load_words()))
#     # print(a_words())
#     print(suggest_word('accidentaly', words=a_words()))


# if __name__ == '__main__':
#     main()
