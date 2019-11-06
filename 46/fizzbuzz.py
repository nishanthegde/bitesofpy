def fizzbuzz(num: int):

    ret = []

    if num % 3 == 0 and num != 0:
        ret.append('Fizz')

    if num % 5 == 0 and num != 0:
        ret.append('Buzz')

    if ret:
        return ' '.join(ret)
    else:
        return num


# def main():
#     # print('thank you...')
#     for i in range(0, 17):
#         print(fizzbuzz(i))


# if __name__ == '__main__':
#     main()
