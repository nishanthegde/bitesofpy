WHITE, BLACK = ' ', '#'


def create_chessboard(size: int=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    num_pieces = int(size / 2)
    num_lines = size

    for i in range(0, num_lines):
        if i % 2 == 0:
            print('{}{}'.format(WHITE, num_pieces * BLACK))
        else:
            print('{}'.format(num_pieces * BLACK))


# def main():
#     print('thank you for the poeple that you have given me in my life ...')
#     create_chessboard(8)


# if __name__ == '__main__':
#     main()
