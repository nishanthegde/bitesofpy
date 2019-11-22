import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    iter = re.finditer(IS_EMOJI, text)
    return [m.start(0) for m in iter]


# def main():
#     print('thank you for everything ...')
#     text = "We see more and more 🐍 Python 🥋 ninjas, keep it up 💪"
#     text = 'Books can be boring 😴, better to code 💪❗'

#     print(get_emoji_indices(text))


# if __name__ == '__main__':
#     main()
