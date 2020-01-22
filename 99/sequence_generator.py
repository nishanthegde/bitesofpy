from itertools import islice, cycle
from string import ascii_uppercase


def sequence_generator() -> list:

    number = 1
    letters = cycle(ascii_uppercase)
    loop_cntr = 1
    while 1:
        if number > 26:
            number = 1
        if loop_cntr % 2 == 0:
            yield next(letters)
        else:
            yield number
            number += 1
        loop_cntr += 1


def main():

    print('thank you for everything yoou have given me...')

    actual = list(islice(sequence_generator(), 10))
    actual = list(islice(sequence_generator(), 52, 62))
    print(actual)


if __name__ == "__main__":
    main()
