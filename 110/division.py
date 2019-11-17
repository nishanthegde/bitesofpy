def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        n = int(numerator)
        d = int(denominator)
    except ValueError:
        print('Caught ValueError Exception')
        raise ValueError('args must be convertable to int')
    else:
        try:
            return n / d
        except ZeroDivisionError:
            print('Caught ZeroDivisionError Exception')
            return 0


# def main():
#     print('thank you for the ocean ...')
#     print(divide_numbers(10, 0))


# if __name__ == '__main__':
#     main()
