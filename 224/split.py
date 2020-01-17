import re
from typing import List

TEXT = """
PyBites was founded 19th of December 2016. That means that today,
14th of October 2019 we are 1029 days old. Time flies when you code
in Python. Anyways, good luck with this Bite. What is your favorite editor?
"""


TEXT_WITH_DOTS = """
We are looking forward attending the next Pycon in the U.S.A.
in 2020. Hope you do so too. There is no better Python networking
event than Pycon. Meet awesome people and get inspired. Btw this
dot (.) should not end this sentence, the next one should. Have fun!
"""


def get_sentences(text: str) -> List:
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    sentences = []
    # pattern_regex = re.compile(r'([A-Z][^\.!?]*[.?!])', re.MULTILINE | re.DOTALL)

    # for match in pattern_regex.finditer(text):
    #     sentences.append(match.group(0).replace('\n', ' '))

    # return sentences
    text = text.strip() + ' '
    pattern = re.compile(r'([\.!?] )')
    matches = pattern.split(text)

    for i, m in enumerate(matches):
        if m.strip() == '?' or m.strip() == '!' or m.strip() == '.':
            # print(m, i)
            sentences.append(matches[i - 1].strip() + m.strip())

    return [s.replace('\n', ' ') for s in sentences]


def main():
    print('thank you for everything...')
    print(get_sentences(TEXT))
    print(get_sentences(TEXT_WITH_DOTS))


if __name__ == '__main__':
    main()
