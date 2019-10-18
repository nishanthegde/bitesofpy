PYBITES = "pybites"


def _in_pybites(c):
    return c.lower() in PYBITES


def _swap_case(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    ret = []
    for c in text:
        # ret.append(c)
        if _in_pybites(c):
            ret.append(_swap_case(c))
        else:
            ret.append(c)

    return ''.join(ret)


# def main():
#     print('here ...')
#     what = convert_pybites_chars('Imperdiet sed euismod nisi porta lorem mollis aliquam')
#     print(what)


# if __name__ == '__main__':
#     main()
