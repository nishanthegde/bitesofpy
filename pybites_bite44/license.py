import random
import string


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    key = ''
    for _ in range(parts):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=chars_per_part))
        key += part + '-'

    return key[:-1]
