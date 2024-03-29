def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    if n > 0:
        return string[n:] + string[:n]
    elif n < 0:
        return string[n:] + string[: len(string) + n]
