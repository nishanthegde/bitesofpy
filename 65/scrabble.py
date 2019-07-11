import itertools
import os
import urllib.request

# PREWORK
local = os.getcwd()
local = '/tmp'
# DICTIONARY = os.path.join(local, 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY, 'r') as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

# dict_list = list(dictionary)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                                for letter in letters.split()}

def calc_word_score(word):
    """
        calculate word score based on LETTER_SCORES
    """
    return sum(LETTER_SCORES.get(letter.upper(),0)for letter in word)

def max_word(words):
    # return max(words, key=calc_word_score)
    max_score = max([calc_word_score(w) for w in words])
    high = [w for w in words if calc_word_score(w)==max_score]

    return high


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary
    """
    words = set(_get_permutations_draw(draw))
    # valid_words = [w for w in words if w in dict_list]
    return list(words.intersection(dictionary))

def _get_permutations_draw(draw):
    """
        Helper to get all permutations of a draw (list of letters), hint:
        use itertools.permutations (order of letters matters)
    """
    words = []

    for i in range(len(draw), 0, -1):
        perms = list(itertools.permutations(draw,i))

        for i in range(0, len(perms)):
            words.append(''.join(perms[i]).strip().lower())

    return words

# def main():
#     """
#         this bite focusses on the use of itertools... to that extent you complete
#         get_possible_dict_words and _get_permutations_draw to get all valid dictionary words for a random draw of 7 letters.

#         This is fed into the tests that calculate the word with maximum value (work previously done for Bite 3) and there you go: you have a Scrabble cheat tool (Scrabble fans, pay attention or maybe skip this Bite!).

#         For example a draw of letters G, A, R, Y, T, E, V would give highest valued word GARVEY (13 points).
#     """

#     # print(type(dictionary))
#     # print(len(dictionary))


#     # print(type(scrabble_scores))
#     # print(scrabble_scores)

#     # print(type(LETTER_SCORES))
#     # print(LETTER_SCORES)


#     draw = 'E, P, A, E, I, O, A'
#     draw = draw.split(', ')

#     # words = _get_permutations_draw(draw)
#     # print(len(words))
#     # # print(type(words))

#     valid_words = get_possible_dict_words(draw)
#     print(valid_words)
#     """
#     {'E': 1, 'A': 1, 'O': 1, 'I': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}
#     """

#     # test = ['nishant', 'z98989', 'se2e098790987']
#     w = max_word(valid_words)
#     # score = calc_word_score()
#     print(type(w))
#     print('peai' in w)
#     print('apio' in w)
#     print(w)

# if __name__ == "__main__":
#     main()
