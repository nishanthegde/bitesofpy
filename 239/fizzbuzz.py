def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


def main():
    print('thank you for everything you have given me...')
    print(fizzbuzz(15))
    print(fizzbuzz(5))
    print(fizzbuzz(3))
    # print(fizzbuzz('test'))
    print(fizzbuzz(True))


if __name__ == '__main__':
    main()
