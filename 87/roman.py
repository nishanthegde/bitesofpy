def romanize(decimal_number: int) -> str:
    """Takes a decimal number int and converts its Roman Numeral str"""

    roman = ''

    if not isinstance(decimal_number, int) or decimal_number <= 0 or decimal_number >= 4000:
        raise ValueError('please provide an int')

    symbols = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    while decimal_number > 0:
        base = max(k for k in symbols.keys() if k <= decimal_number)
        quotient = decimal_number // base
        remainder = decimal_number % base
        # print(decimal_number, base, quotient, remainder)
        decimal_number = remainder
        roman += quotient * symbols[base]

    return roman


# def main():
#     print('thank you for everything ...')
#     # print(romanize(3549))
#     print(romanize(177))
#     # print(romanize(549))
#     # print(romanize(49))
#     # print(romanize(9))


# if __name__ == '__main__':
#     main()
