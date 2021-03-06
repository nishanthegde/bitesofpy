import os
import urllib.request as ur

# PREWORK
curr_path = os.getcwd()
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
ur.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U")   , (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

LETTER_SCORES = {letter: score for score, letters in scrabble_scores for letter in letters.split()}


def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    words = []

    f = open(DICTIONARY, 'r')
    words = f.readlines()
    f.close()

    #take out newlines
    words = [w[:-1] for w in words]

    return words


def calc_word_value(word=None):
    """given a word calculate its value using LETTER_SCORES"""
    #list to hold letter score for the word
    if word:
        letter_score = [LETTER_SCORES[l.upper()] if l.upper() in LETTER_SCORES else 0 for l in word] #list to hold letter scores for word

        return sum(letter_score)

    pass

def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    #list to hold word score for the list of words
    if words:
        word_score = [calc_word_value(w) for w in words]

        idx_max = word_score.index(max(word_score))

        return words[idx_max]

    pass







