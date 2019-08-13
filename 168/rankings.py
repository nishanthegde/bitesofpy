from dataclasses import dataclass
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    def __init__(self, name, bites):
        self.name = name
        self.bites = int(bites)

    def __str__(self):
        return "[{}] {}".format(self.bites, self.name)

    def __eq__(self, other):
        if isinstance(other, Ninja):
            return self.bites == other.bites
        return False

    def __gt__(self, other):
        if isinstance(other, Ninja):
            return self.bites > other.bites
        return False

    def __lt__(self, other):
        if isinstance(other, Ninja):
            return self.bites < other.bites
        return False


@dataclass
class Rankings:

    def __init__(self, rankings=None):
        self.rankings = []

    def __len__(self):
        return len(self.rankings)

    def add(self, ninja):
        if isinstance(ninja, Ninja):
            self.rankings.append(ninja)

    def sort_rankings(self, rev=False):
        return sorted(self.rankings, key=lambda x: x.bites, reverse=rev)

    def dump(self):
        self.sort_rankings(True)
        if self.rankings:
            return self.rankings.pop()

    def highest(self, n=1):
        self.rankings = self.sort_rankings(True)
        if self.rankings:
            return sorted(self.rankings[:n], key=lambda x: x.bites, reverse=True)

    def lowest(self, n=1):
        self.rankings = self.sort_rankings(True)
        if self.rankings:
            return sorted(self.rankings[-n:], key=lambda x: x.bites)

    def pair_up(self, n=3):
        self.rankings = self.sort_rankings(True)

        highs = self.rankings[:n]
        lows = self.rankings[-n:][::-1]

        return [(high, low) for high, low in zip(highs, lows)]


# def main():

#     # print("dance")

#     n = Ninja('nishant', 168)
#     FIRST_NINJAS = [Ninja(*ninja) for ninja in zip(names, bites)]

#     ninja1 = Ninja("snow", 283)
#     ninja2 = Ninja("natalia", 282)
#     ninja3 = Ninja("okken", 70)

#     assert ninja1 in FIRST_NINJAS
#     assert ninja2 in FIRST_NINJAS
#     assert ninja3 not in FIRST_NINJAS

#     # print(FIRST_NINJAS[1])
#     # print(FIRST_NINJAS[3])

#     ranking = Rankings()

#     for ninja in FIRST_NINJAS:
#         ranking.add(ninja)

#     assert len(ranking) == 11

#     # print(len(ranking))

#     actual = ranking.dump()
#     expected = Ninja(name="sam", bites=195)
#     assert actual == expected
#     # print(len(ranking))
#     assert len(ranking) == 10

#     actual = ranking.highest()
#     expected = [Ninja(name="snow", bites=283)]
#     assert actual == expected

#     actual = ranking.lowest()
#     expected = [Ninja(name="sara", bites=196)]
#     assert actual == expected

#     actual = ranking.lowest(3)
#     expected = [
#         Ninja(name="sara", bites=196),
#         Ninja(name="james", bites=197),
#         Ninja(name="fred", bites=204),
#     ]
#     assert actual == expected

#     ranking.add(Ninja(name="sam", bites=195))
#     assert len(ranking) == 11

#     actual = ranking.lowest(3)
#     expected = [
#         Ninja(name="sam", bites=195),
#         Ninja(name="sara", bites=196),
#         Ninja(name="james", bites=197),
#     ]
#     assert actual == expected

#     SECOND_NINJAS = [Ninja(*ninja) for ninja in more_names]

#     # now add the ninjas of first_ninja_ranks
#     for ninja in SECOND_NINJAS:
#         ranking.add(ninja)

#     # print(len(ranking))

#     actual = ranking.highest(3)

#     expected = [
#         Ninja(name="noah", bites=470),
#         Ninja(name="doug", bites=469),
#         Ninja(name="steve", bites=468),
#     ]
#     assert actual == expected

#     # for ninja in ranking.rankings:
#     #     print(ninja)

#     actual = ranking.pair_up()
#     assert len(actual) == 3
#     # print(actual)

#     expected = (Ninja(name="doug", bites=469), Ninja(name="sara", bites=196))
#     assert actual[1] == expected

#     actual = ranking.pair_up(5)
#     assert len(actual) == 5

#     # for n in actual[0]:
#     #     print(n)
#     expected = (Ninja(name="noah", bites=470),
#                 Ninja(name="sam", bites=195))
#     assert actual[0] == expected

#     expected = (Ninja(name="valentine", bites=441),
#                 Ninja(name="kenneth", bites=216))
#     assert actual[-1] == expected


# if __name__ == '__main__':
#     main()
