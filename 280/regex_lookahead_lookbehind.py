import re


def count_n_repetitions(text, n=1):
    ret = 0
    regex = r'((.)\2{' + re.escape(str(n)) + ',})'

    text = re.sub(r"\n", " ", text)
    match = re.findall(regex, text)

    # print(match)

    ret = len(match)
    if match:
        for m in match:
            ret += count_n_repetitions(m[0][1:], n)

    return ret


def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """

    # first count n repetitions
    ret = count_n_repetitions(text, n)

    if char:
        # print(char)
        regex = r'(.)(' + re.escape(char) + '{' + re.escape(str(n)) + '})'
        match = re.findall(regex, text)
        # print(regex)
        if match:
            for m in match:
                if m[0][:1] != m[1][:1]:
                    ret += 1

    return ret


def check_surrounding_chars(text, surrounding_chars):
    print(text)
    ret = 0
    surrounding = '|'.join([re.escape(c) for c in surrounding_chars])
    regex = r'(?<=' + surrounding + ')(\w)(?=' + surrounding + ')'
    print(regex)
    match = re.findall(regex, text)
    if match:
        for m in match:
            ret += 1

    return ret

