expected = '''10
9
8
7
6
5
4
3
2
1
time is up
'''

expected_other_start_arg = '''13
12
11
'''

expected_other_start_arg += expected


def countdown_for(start: int=10) -> str:
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start: int=10) -> str:
    if start < 1:
        print('time is up')
        return True
    else:
        print('{}'.format(start))

    start -= 1
    countdown_recursive(start)


# def main():
#     print('thank you for the waves ...')
#     # countdown_for()

#     countdown_recursive(13)
#     # print(expected_other_start_arg)


# if __name__ == '__main__':
#     main()
