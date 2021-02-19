from dataclasses import dataclass
import enum
from typing import List  # TODO: can remove >= 3.9

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


class BiteLevel(enum.Enum, metaclass=EnumMetaSubClass):
    INTRO = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4


# 2. make a dataclass that can be ordered
# attributes: number (int), title (str), level (BiteLevel)

@dataclass
class Bite:
    number: int
    title: str
    level: BiteLevel


# 3. complete the function below

def create_bites(numbers: List[int], titles: List[str],
                 levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    # return create_bites(numbers[0], titles[0], list(levels))
    bite_levels = list(levels)
    for (a, b, c) in zip(numbers, titles, levels):
        yield Bite(a, b, c)


def main():
    print('thank you for looking after my mama :-)')
    # print(list(BiteLevel.__members__.values())[0].name)
    # print(list(create_bites(NUMBERS, TITLES, BiteLevel.__members__.values())))
    print(BiteLevel.__members__.keys())
    print(getattr(BiteLevel, 'INTRO'))


if __name__ == '__main__':
    main()
