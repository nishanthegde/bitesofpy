VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str: str) -> bool:
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(c.lower() in VOWELS for c in input_str)


def contains_any_py_chars(input_str: str) -> bool:
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(c.lower() in PYTHON for c in input_str)


def contains_digits(input_str: str) -> bool:
    """Receives input string and checks if it contains
       one or more digits."""
    return any(c.isdigit() for c in input_str)


# def main():
#     print('thank you for the waves...')

#     # print(contains_only_vowels('aioue'))
#     # print(contains_only_vowels('EoUia'))
#     # print(contains_only_vowels('aaAiIee'))
#     # print(contains_only_vowels('AEIOU'))
#     # print(contains_only_vowels('aaeeouu'))
#     # print(contains_only_vowels('abcde'))
#     # print(contains_only_vowels('AE123'))
#     # print(contains_only_vowels('AiOuef'))

#     # print(contains_any_py_chars('Python'))
#     # print(contains_any_py_chars('pycharm'))
#     # print(contains_any_py_chars('PYTHON'))
#     # print(contains_any_py_chars('teaser'))
#     # print(contains_any_py_chars('bob'))
#     # print(contains_any_py_chars('julian'))
#     # print(contains_any_py_chars('yes'))
#     # print(contains_any_py_chars('no'))
#     # print(contains_any_py_chars('america'))
#     # print(contains_any_py_chars('B@b'))
#     # print(contains_any_py_chars('Jules'))
#     # print(contains_any_py_chars('agua'))
#     # print(contains_any_py_chars('123'))
#     # print(contains_any_py_chars(''))

#     print(contains_digits('yes1'))
#     print(contains_digits('123'))
#     print(contains_digits('hello2'))
#     print(contains_digits('up2date'))
#     print(contains_digits('yes'))
#     print(contains_digits('hello'))
#     print(contains_digits(''))


# if __name__ == '__main__':
#     main()
