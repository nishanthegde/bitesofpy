from dataclasses import dataclass, astuple, replace, field


@dataclass
class Bite:
    number: int
    title: str
    level: str = 'Beginner'

    def __post_init__(self):
        self.title = self.title.capitalize()

    def __lt__(self, other):
        return self.number < other.number


# def main():

#     b1 = Bite(number=1, title="sum of numbers")
#     b2 = Bite(number=2, title="a second bite", level="Intermediate")
#     b3 = Bite(number=3, title="a hard bite", level="Advanced")
#     bites = [b1, b2, b3]

#     # print(bites)

#     assert Bite.__annotations__ == {'number': int, 'title': str, 'level': str}

#     expected = Bite(number=1, title='Sum of numbers', level='Beginner')
#     assert bites[0] == expected

#     assert bites[0].level == 'Beginner'

#     assert bites[1].number == 2
#     # title should get capitalized (use the __post_init__ method)
#     assert bites[1].title == 'A second bite'
#     assert bites[1].level == 'Intermediate'

#     b3 = bites[-1]
#     assert b3.level == 'Advanced'
#     # named tuples are immutable so would not allow this:
#     b3 = replace(b3, level='super hard')
#     assert b3.level == 'super hard'

#     # print(bites)
#     sorted_bites = sorted(bites, reverse=True)
#     # print(sorted_bites)

#     assert sorted_bites[0].number == 3
#     assert sorted_bites[-1].number == 1

#     # set(bites)
#     # number, title, level = bites[0]
#     number, title, level = astuple(bites[0])

#     assert number == 1
#     assert level == 'Beginner'
#     print(title)


# if __name__ == '__main__':
#     main()
