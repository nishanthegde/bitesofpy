import re


def count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """
    ret = 0
    regex = r'((\w)\2{' + re.escape(str(n)) + ',})'

    match = re.findall(regex, text)
    # print(match)
    ret = len(match)
    if match:
        for m in match:
            ret += count_n_repetitions(m[0][1:],n)

    return ret


def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """


def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """


def main():
    print('please look after my mama. i love her very much...')
    # print(count_n_repetitions('3444553333', 2))
    # print(count_n_repetitions('333', 1))
    print(count_n_repetitions('', 1))
    print(count_n_repetitions('111', 2))
    print(count_n_repetitions('1122', 2))
    print(count_n_repetitions('1112345', 2))



if __name__ == '__main__':
    main()
