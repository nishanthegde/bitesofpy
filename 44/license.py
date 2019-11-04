import re
import random
import string

default_key = re.compile(r'^([A-Z0-9]{8}-){3}[A-Z0-9]{8}$')
shorter_key = re.compile(r'^([A-Z0-9]{4}-){2}[A-Z0-9]{4}$')
longer_key = re.compile(r'^([A-Z0-9]{10}-){9}[A-Z0-9]{10}$')


def gen_key(parts: int=4, chars_per_part: int=8) -> str:
    key = ''
    choices = string.ascii_uppercase + string.digits
    for p in range(parts):
        key += ''.join(random.choice(choices) for i in range(chars_per_part)) + '-'

    return key[:-1]


# def main():
#     print('thank you... start writing... it like water')
#     assert default_key.match(gen_key())
#     assert shorter_key.match(gen_key(parts=3, chars_per_part=4))
#     assert longer_key.match(gen_key(parts=10, chars_per_part=10))


# if __name__ == '__main__':
#     main()
