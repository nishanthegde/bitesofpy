def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    add = number % base

    if number <= 1:
        if number == 0:
            return ''
        return str(number)

    else:
        return int(str(dec_to_base(number // base, base)) + str(add))


def main():
    print(dec_to_base(256, 8))


if __name__ == "__main__":
    main()
