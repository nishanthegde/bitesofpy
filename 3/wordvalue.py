import os
import urllib.request as ur

# PREWORK
curr_path = os.getcwd()
DICTIONARY = os.path.join(curr_path, 'dictionary.txt')
ur.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

letter_scores = {letter: score for score, letters in scrabble_scores for letter in letters.split()}

# print(curr_path)
# print(os.listdir(curr_path))
# print(DICTIONARY)
# print(os.path.expanduser('~'))

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    words = []

    f = open('dictionary.txt', 'r')
    words = f.readlines()
    f.close()

    #take out newlines
    words = [w[:-1] for w in words]

    return words


def calc_word_value(word=None):
    """given a word calculate its value using LETTER_SCORES"""
    #list to hold letter score for the word
    if word:
        letter_score = [letter_scores[l.upper()] if l.upper() in letter_scores else 0 for l in word] #list to hold letter scores for word

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

# words = load_words()
# print(words[20000:21000])
# print(len(words))
# print(words[0])
# print(words[-1:])
# print(' ' in ''.join(words))

# print(type(scrabble_scores))
# print(letter_scores)
# print(calc_word_value('bob'))
# print(calc_word_value('PyBites'))

# test_words = ('bob', 'barbeque', 'julian', 'pybites', 'quit')
# print(max_word_value(test_words))
# print(max_word_value(words[20000:21000]))
# print(max_word_value(["a", "B", "Z"]))
# print(max_word_value(["a", "åäö"]))
# print(type(test_words))
# print(max_word_value())








