from typing import Tuple
import re
from collections import Counter

sample_text = '''It is a truth universally acknowledged, that a single man in
                    possession of a good fortune, must be in want of a wife.'''
with_numbers_text = '''20,000 Leagues Under the Sea is a 1954 American
                    Technicolor science fiction-adventure film...'''
emoji_text = 'emoji like 😃😃😃😃 are not letters'
accents_text = 'Société Générale est une des principales banques françaises'
mixed_case_text = 'Short Plays By Lady Gregory The Knickerbocker Press 1916'
hyphenated_word_text = 'six-feet-two in height'
compound_character_text = 'der Schloß is riesig'
no_repeat_characters_text = 'the quick brown fox jumped over the lazy dog'
non_ascii_symbols_text = '«¿Tiene sentido la TV pública?»'
apostrophe_in_word_text = "but we've been there already!!!"
underscore_torture_text = '"____".isalpha() is True, thus this test text'
digit_text = '99abc99 __abc__ --abc-- digits _ and - are not letters'
repeat_words_text = 'test test test test test correct-answer.'
no_words_in_text = '1, 2, 3'
empty_text = ''


def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    # >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    # >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """

    return_value = ('', '', 0)

    regex = re.compile('[«¿\"#!@$%%&*()0-9._]')
    regex1 = re.compile(r'[^ \nA-Za-zÀ-ÖØ-öø-ÿ/]+')

    if not isinstance(text, str):
        raise ValueError
    else:
        words_orig = [regex.sub('', w) for w in text.split()]
        words = [regex1.sub('', w.casefold()) for w in text.split()]

        for i, word in enumerate(words):
            if word:
                # print(word)
                cnt = Counter(word).most_common()[0]
                # print(cnt)
                if i == 0:  # initiate
                    return_value = (words_orig[i], cnt[0], cnt[1])
                else:
                    if cnt[1] > return_value[2]:
                        return_value = (words_orig[i], cnt[0], cnt[1])
            # else:
            #     break

    return return_value

