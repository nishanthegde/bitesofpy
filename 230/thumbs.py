THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:

    def __mul__(self, other):
        if other > 0:
            if other <= 3:
                return THUMBS_UP * int(other)
            else:
                return "{} ({}x)".format(THUMBS_UP, int(other))
        elif other < 0:
            if other >= -3:
                return THUMBS_DOWN * -int(other)
            else:
                return "{} ({}x)".format(THUMBS_DOWN, int(-other))
        else:
            raise ValueError('Specify a number')

    def __rmul__(self, other):
        if other > 0:
            if other <= 3:
                return THUMBS_UP * int(other)
            else:
                return "{} ({}x)".format(THUMBS_UP, int(other))
        elif other < 0:
            if other >= -3:
                return THUMBS_DOWN * -int(other)
            else:
                return "{} ({}x)".format(THUMBS_DOWN, int(-other))
        else:
            raise ValueError('Specify a number')


def main():
    print('thank you for everything... ')
    th = Thumbs()
    print(th * 3)
    print(th * 2.1)
    # print(0 * th)
    print(th * -2)


if __name__ == '__main__':
    main()
