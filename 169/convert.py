def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError('value must be int or float')

    if fmt.lower() not in ['cm', 'in']:
        raise ValueError('fmt must be in or cm')

    if fmt.lower() == 'cm':
        return round(value * 2.54, 4)
    else:
        return round(value * 0.393701, 4)


# def main():
#     print('thank you for everything...')
#     # convert(-153.67, "cm")
#     # convert(300, "cm")
#     print(convert(60.5, "CM"))
#     print(convert(83, "CM"))
#     print(convert(91, "IN"))

# if __name__ == '__main__':
#     main()
