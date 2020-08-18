import string


def convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """
    try:
        assert isinstance(number, int)
    except:
        raise TypeError

    try:
        assert (1 < base < 37)
    except:
        raise ValueError

    r = ''
    while number > 0:
        r = string.printable[number % base] + r
        number //= base
    return r.upper()
