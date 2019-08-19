scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


CONGRATS_MSG = ('Congrats, you earned {score} points '
                'obtaining the PyBites Ninja {rank} Belt')
NEW_SCORE_MSG = 'Set new score to {score}'


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        # get all belt scores in BELTS that are lower
        levels = [i for i in BELTS if i <= new_score]
        if levels:
            # get the highest belt
            _new_belt = BELTS[max(levels)]
            # check if new belt is different
            if self._last_earned_belt != _new_belt:
                self._last_earned_belt = _new_belt
                return CONGRATS_MSG.format(score=self.score, rank=_new_belt.capitalize())

        return NEW_SCORE_MSG.format(score=self.score)

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError("score must be int")

        if new_score < self.score:
            raise ValueError("score must be higher than current score. Current score is {}".format(self.score))

        self._score = new_score
        print(self._get_belt(self.score))

    score = property(_get_score, _set_score)


# def main():
#     """
#         Make sure it can only be assigned an integer,
#         It can not be assigned a score lower than the current score,
#         It checks in BELTS if a new belt was earned (for example going from 49 to 50 you earn the yellow belt), if so it stores it in self._last_earned_belt.
#         For each new score print a message:
#         If a new badge was earned: Congrats, you earned {score} points obtaining the PyBites Ninja {rank} Belt
#         Else just the new score: Set new score to {score}
#     """
#     print("dance!")
#     # print(BELTS)
#     ninja = NinjaBelt()

#     assert ninja.score == 0
#     assert ninja._last_earned_belt is None

#     ninja.score = 20
#     ninja.score = 49

#     # ninja.score = 'a'
#     # ninja.score = 40

#     ninja.score = 50
#     ninja.score = 177

#     assert ninja._last_earned_belt.lower() == 'green'


# if __name__ == '__main__':
#     main()
