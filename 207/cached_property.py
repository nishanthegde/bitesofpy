from random import random
from time import sleep
from time import perf_counter


def cached_property(method):
    """decorator used to cache expensive object attribute lookup"""
    prop_name = '_{}'.format(method.__name__)

    def wrapped_func(self, *args, **kwargs):
        # print(self)
        if not hasattr(self, prop_name):
            setattr(self, prop_name, method(self, *args, **kwargs))
        return getattr(self, prop_name)

    return property(wrapped_func)
    # return prop_name


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color
        # self._mass = None

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    @cached_property
    def mass(self):
        print('setting mass')
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        return self._mass

    # @mass.setter
    # def mass(self, value):
    #     self._mass = value

    @cached_property
    def something(self):
        print('accessing')
        return 981978


# def main():

#     print('here ...')

#     blue = Planet('blue')
#     # print(blue.something)
#     # print(blue.something)

#     # print(blue.mass)
#     # print(blue.mass)
#     # print(blue.something)

#     start_time = perf_counter()
#     for _ in range(5):
#         blue.mass
#         # print(blue.mass)
#     end_time = perf_counter()
#     elapsed_time = end_time - start_time
#     # print(elapsed_time)

#     assert elapsed_time < .5
#     # print(blue.something)
#     # print(blue.something)

#     masses = [blue.mass for _ in range(10)]
#     initial_mass = masses[0]
#     assert all(m == initial_mass for m in masses)

#     blue.mass = 11


# if __name__ == '__main__':
#     main()
