def _valid_range(val):
    return isinstance(val, int) and val >= 0 and val <= 255


def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if all(_valid_range(x) for x in rgb):
        return "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])
    else:
        raise ValueError("invalid rgb value")


# def main():
#     print('here!')
#     print(rgb_to_hex(((0, 0, 0))))
#     print(rgb_to_hex((255, 255, 255)))
#     print(rgb_to_hex((0, 128, 0)))
#     print(rgb_to_hex((192, 192, 192)))

#     # print(rgb_to_hex((-1, 'test', 100)))

#     # print(_valid_range(255))


# if __name__ == '__main__':
#     main()
