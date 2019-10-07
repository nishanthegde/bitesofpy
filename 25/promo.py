import random

BITES = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}

BITES_TEST = {6: 'PyBites Die Hard',
              10: 'Practice exceptions',
              16: 'Special PyBites date generator',
              18: 'Find the most common word',
              21: 'Query a nested data structure'}

bites_done = {6, 10, 16, 18, 21}

BITES_AVAILABLE = len(BITES) - len(bites_done)


class NoBitesAvailable(Exception):
    pass


class Promo:

    def __init__(self, bites_done=bites_done):

        self.bites_done = bites_done

    def _pick_random_bite(self):

        if not [k for k in list(BITES.keys()) if k not in self.bites_done]:
            raise NoBitesAvailable("No more bites available")
        else:
            return random.choice([k for k in list(BITES.keys()) if k not in self.bites_done])

    def new_bite(self):
        nb = self._pick_random_bite()
        self.bites_done.add(nb)
        return nb


def grab_bites(promo, amount=BITES_AVAILABLE):
    # _ is a throw-away variable (just want a loop)
    for _ in range(amount):
        promo.new_bite()


def main():
    print('here ...')
    # print(type(BITES))

    promo = Promo(bites_done=bites_done.copy())

    assert len(BITES) == 15
    assert len(promo.bites_done) == 5

    for _ in range(10):
        bite = promo._pick_random_bite()
        # print(bite)
        assert type(bite) == int
        assert bite in BITES
        assert bite not in promo.bites_done

    # assert len(promo.bites_done) == 5
    # grab_bites(promo, amount=7)
    # # bites_done incremented with 7
    # assert len(promo.bites_done) == 12
    # # print(promo.bites_done)

    assert len(promo.bites_done) == 5
    grab_bites(promo)
    # promo._pick_random_bite()
    # exhausted bites
    # with pytest.raises(NoBitesAvailable):
    #     promo._pick_random_bite()

    # grab_bites(promo)
    # exhausted bites
    # with pytest.raises(NoBitesAvailable):
    #     promo._pick_random_bite()

    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)
    # p.new_bite()
    # print(p.bites_done)


if __name__ == '__main__':
    main()
