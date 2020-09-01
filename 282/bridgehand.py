from enum import Enum
import typing
from collections import namedtuple, defaultdict
from collections.abc import Sequence
import random

suits = list("SHDC")
ranks = list("AKQJT98765432")
Suit = Enum("Suit", suits)
Rank = Enum("Rank", ranks)
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: typing.Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError("BridgeHand object must be initiated with card sequence")
        elif len(cards) != 13:
            raise ValueError("Card sequence must have 13 cards")
        elif not all(isinstance(x, Card) for x in cards):
            raise ValueError("Card sequence can have only card objects")
        else:
            self.cards = cards

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        ret = ''
        ret_dict = defaultdict(list)

        for c in self.cards:
            ret_dict[str(c.suit.name)].append(str(c.rank.name))

        for s in sorted(ret_dict, key=lambda x: Suit[x].value):
            ret += "{}:{} ".format(s, ''.join(sorted(ret_dict[s], key=lambda x: Rank[x].value)))

        return "{}".format(ret.strip())

    # @property
    # def hcp(self) -> int:
    #     """ Return the number of high card points contained in this hand """
    #
    # @property
    # def doubletons(self) -> int:
    #     """ Return the number of doubletons contained in this hand """
    #
    # @property
    # def singletons(self) -> int:
    #     """ Return the number of singletons contained in this hand """
    #
    # @property
    # def voids(self) -> int:
    #     """ Return the number of voids (missing suits) contained in
    #         this hand
    #     """
    #
    # @property
    # def ssp(self) -> int:
    #     """ Return the number of short suit points in this hand.
    #         Doubletons are worth one point, singletons two points,
    #         voids 3 points
    #     """
    #
    # @property
    # def total_points(self) -> int:
    #     """ Return the total points (hcp and ssp) contained in this hand """
    #
    # @property
    # def ltc(self) -> int:
    #     """ Return the losing trick count for this hand - see bite description
    #         for the procedure
    #     """


def main():
    print("please look after my mom...")

    cards = list()
    random.seed(9878)
    for i in range(13):
        suit = Suit[random.choice(suits)]
        rank = Rank[random.choice(ranks)]
        cards.append(Card(suit, rank))

    # print([c for c in cards][0])
    hand = BridgeHand(cards)
    print(str(hand))


if __name__ == "__main__":
    main()
