from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    # move these into an Enum:
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return '{} => {}'.format(str(self.name), str(self.value * THUMBS_UP))

    @classmethod
    def average(cls):
        vals = []
        for s in cls:
            vals.append(s.value)

        return sum(vals) / len(vals)


# def main():
#     print('thank you for everything...')
#     # print(list(Score))
#     assert list(Score) == [Score.BEGINNER, Score.INTERMEDIATE,
#                            Score.ADVANCED, Score.CHEATED]
#     # print(repr(Score.BEGINNER))
#     # print(Score.BEGINNER.name)
#     # print(Score.BEGINNER.value)

#     assert Score.BEGINNER is Score.BEGINNER
#     assert Score.INTERMEDIATE is not Score.ADVANCED

#     # print(str(Score.BEGINNER))
#     # print(str(Score.INTERMEDIATE))
#     # print(str(Score.ADVANCED))
#     # print(str(Score.CHEATED))

#     assert str(Score.BEGINNER) == 'BEGINNER => 👍👍'
#     assert str(Score.INTERMEDIATE) == 'INTERMEDIATE => 👍👍👍'
#     assert str(Score.ADVANCED) == 'ADVANCED => 👍👍👍👍'
#     assert str(Score.CHEATED) == 'CHEATED => 👍'

#     print(Score.average())


# if __name__ == '__main__':
#     main()
