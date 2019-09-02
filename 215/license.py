import re
from string import ascii_uppercase, digits
import random

ALPHABET = ascii_uppercase + digits


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    key_reg = re.compile(r'^PB(-[0-9A-Z]{8}){4}$')

    if key_reg.search(key):
        return True

    return False


# def _create_license():
#     return 'PB-' + '-'.join(
#         [''.join(random.sample(ALPHABET, 8))
#          for _ in range(4)]
#     )


# def main():

#     for _ in range(10):
#         key = _create_license()
#         # print(validate_license(key))
#         assert validate_license(key)

#     pool = [_create_license() for _ in range(5)]
#     # print(pool)
#     lcase_key = pool[0].lower()
#     assert not validate_license(lcase_key)
#     # print(validate_license('test this out'))
#     shorter_key = pool[1][:-2]
#     assert not validate_license(shorter_key)
#     longer_key = pool[2] + 'A'
#     assert not validate_license(longer_key)
#     # print(longer_key)
#     wrong_prefix = 'AB-' + pool[3][3:]
#     assert not validate_license(wrong_prefix)
#     empty_key = ''
#     assert not validate_license(empty_key)
#     key_reversed = pool[4][::-1]
#     assert not validate_license(key_reversed)


# if __name__ == '__main__':
#     main()
