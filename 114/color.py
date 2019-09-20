import os
import sys
import urllib.request

# local = os.getcwd()
local = '/tmp'
# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join(local, 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append(local)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper())

    @classmethod
    def hex2rgb(self, h):
        """Class method that converts a hex value into an rgb one"""
        h = h.lstrip('#')
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    @classmethod
    def rgb2hex(self, rgb):
        """Class method that converts an rgb value into a hex one"""
        if rgb in COLOR_NAMES.values():
            r, g, b = rgb
            return '#{:02x}{:02x}{:02x}'.format(r, g, b)
        else:
            raise ValueError('bad value')

    def __repr__(self):
        """Returns the repl of the object"""
        return "Color('{}')".format(self.color)

    def __str__(self):
        """Returns the string value of the color object"""
        return '{}'.format(self.rgb)


# def main():
#     print('here')
#     # print(len(COLOR_NAMES))

#     c = Color('white')
#     print(c.rgb)

#     c = Color('test')
#     print(c.rgb)

#     c = Color('red')
#     print(c.rgb)
#     # print(rgb2hex(c))
#     print(Color.rgb2hex((255, 0, 0)))
#     # print(Color.hex2rgb("puke"))

#     color = Color("brown")
#     assert repr(color) == "Color('brown')"
#     test = str(color)
#     print(test)


# if __name__ == '__main__':
#     main()
