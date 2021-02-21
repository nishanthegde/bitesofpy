from dataclasses import dataclass
import enum
from typing import List  # TODO: can remove >= 3.9
import operator
from ordered_enum import ValueOrderedEnum

NUMBERS = [101, 1, 97, 2]
TITLES = 'f-string,sum numbers,scrape holidays,regex fun'.split(',')


# 1. make a BiteLevel enum class
# keys = INTRO BEGINNER INTERMEDIATE ADVANCED
# values = 1 2 3 4
# make sure they can be sorted by int value

class EnumMetaSubClass(enum.EnumMeta):

    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value


# class BiteLevel(ValueOrderedEnum, metaclass=EnumMetaSubClass):
class BiteLevel(enum.Enum):
    INTRO = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4

    def __getattribute__(self, name):
        ob = object.__getattribute__(self, name)
        print(type(ob))
        return ob

    # def __str__(self):
    #     return str(self.value)

    # def __repr__(self):
    #     return str(self._value_)

# 2. make a dataclass that can be ordered
# attributes: number (int), title (str), level (BiteLevel)

@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: BiteLevel


# 3. complete the function below

def create_bites(numbers: List[int], titles: List[str],
                 levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    # return create_bites(numbers[0], titles[0], list(levels))
    # bite_levels = list(levels)
    # for (a, b, c) in zip(numbers, titles, levels):
    #     yield Bite(a, b, c)
    for i in range(len(numbers)):
        yield Bite(numbers[i], titles[i], list(levels)[i].value)


def main():
    print('thank you for looking after my mama :-)')

    some_bites = create_bites(NUMBERS, TITLES, BiteLevel.__members__.values())
    # print(list(some_bites))
    print(list(zip(BiteLevel.__members__.keys(), range(1, 5))))
    print(getattr(BiteLevel, 'INTERMEDIATE'))
    # assert getattr(BiteLevel, 'INTRO').value == 1

    # first, *_, last = sorted(some_bites,  key=operator.attrgetter('level'), reverse=True)
    # print(first.level, BiteLevel.ADVANCED)
    # assert str(4) == 4
    # print(BiteLevel.INTRO >= BiteLevel.INTERMEDIATE)
    # a = Bite(1, 'a', list(BiteLevel.__members__.values())[0])
    # b = Bite(1, 'b', list(BiteLevel.__members__.values())[1])
    # print(a, b, a > b)


if __name__ == '__main__':
    main()
