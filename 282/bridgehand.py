from enum import Enum
import typing
from dataclasses import dataclass, field
from collections import namedtuple, defaultdict
from collections.abc import Sequence
import random
from typing import List
from random import shuffle

suits = list("SHDC")
ranks = list("AKQJT98765432")
Suit = Enum("Suit", suits)
Rank = Enum("Rank", ranks)
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


@dataclass
class TestHand:
    card_string: str
    doubletons: int
    singletons: int
    voids: int
    hcp: int
    ssp: int
    total_points: int
    ltc: int
    card_list: List[Card] = field(init=False)

    def __post_init__(self):
        """ Generate actual list of Card instances from card_string """
        self.card_list = []
        for suit_holding in self.card_string.split():
            suit = Suit[suit_holding[0]]
            for rank in suit_holding[2:]:
                card = Card(suit, Rank[rank])
                self.card_list.append(card)
        shuffle(self.card_list)


test_hands = [
    TestHand("S:AKJ H:QJT9 D:5432 C:AK", 1, 0, 0, 18, 1, 19, 6),
    TestHand("S:A76 H:KT75 D:KQ2 C:AK8", 0, 0, 0, 19, 0, 19, 6),
    TestHand("S:AKQJT98765432", 0, 0, 3, 10, 9, 19, 0),
    TestHand("S:5432 H:5432 D:543 C:32", 1, 0, 0, 0, 1, 1, 11),
    TestHand("S:K642 H:Q985 D:AT64 C:4", 0, 1, 0, 9, 2, 11, 7),
    TestHand("S:KQ3 H:Q76 D:J43 C:J987", 0, 0, 0, 9, 0, 9, 9),
    TestHand("S:A64 H:72 D:KJ8542 C:AJ", 2, 0, 0, 13, 2, 15, 7),
    TestHand("S:AT4 H:86 D:A984 C:AKT7", 1, 0, 0, 15, 1, 16, 7),
    TestHand("S:J972 H:9 D:98742 C:T54", 0, 1, 0, 1, 2, 3, 10),
    TestHand("S:9854 H:K43 D:Q5 C:9873", 1, 0, 0, 5, 1, 6, 10),
    TestHand("S:KT943 H:T63 D:JT5 C:97", 1, 0, 0, 4, 1, 5, 10),
    TestHand("S:T9732 H:J86 D:K93 C:86", 1, 0, 0, 4, 1, 5, 10),
    TestHand("S:KT8 H:94 D:AJT4 C:6532", 1, 0, 0, 8, 1, 9, 9),
    TestHand("S:AQT92 H:J763 D:763 C:6", 0, 1, 0, 7, 2, 9, 8),
    TestHand("S:AK94 H:K743 D:AKT C:72", 1, 0, 0, 17, 1, 18, 6),
    TestHand("S:A974 D:AK94 C:QJ932", 0, 0, 1, 14, 3, 17, 5),
    TestHand("S:J873 H:KJ62 D:A96 C:K8", 1, 0, 0, 12, 1, 13, 8),
    TestHand("S:T732 H:T2 D:JT8 C:AK96", 1, 0, 0, 8, 1, 9, 9),
    TestHand("S:KT H:AK975 D:QJT2 C:KJ", 2, 0, 0, 17, 2, 19, 5),
    TestHand("S:KJT97 H:AQ843 D:86 C:5", 1, 1, 0, 10, 3, 13, 6)
]


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

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        hcp = 0
        for suit_holding in self.__str__().split():
            for c in suit_holding.strip().split(':')[1]:
                if c == 'A':
                    hcp += 4
                if c == 'K':
                    hcp += 3
                if c == 'Q':
                    hcp += 2
                if c == 'J':
                    hcp += 1

        return hcp

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        doubletons = 0
        for suit_holding in self.__str__().split():
            if len(suit_holding.strip().split(':')[1]) == 2:
                doubletons += 1

        return doubletons

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        singletons = 0
        for suit_holding in self.__str__().split():
            if len(suit_holding.strip().split(':')[1]) == 1:
                singletons += 1

        return singletons

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        non_voids = 0
        for suit_holding in self.__str__().split():
            non_voids += 1

        return 4 - non_voids

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        return self.doubletons * 1 + self.singletons * 2 + self.voids * 3

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        ltc = 0

        for suit_holding in self.__str__().split():

            #  singletons
            if len(suit_holding.strip().split(':')[1]) == 1:
                for c in suit_holding.strip().split(':')[1]:
                    if c == 'A':
                        ltc += 0
                    else:
                        ltc += 1

            # doubletons
            if len(suit_holding.strip().split(':')[1]) == 2:
                d_cards = suit_holding.strip().split(':')[1]

                if d_cards == 'AK':
                    ltc += 0
                elif d_cards[0] == 'A' or d_cards[0] == 'K':
                    ltc += 1
                elif d_cards[0] == 'Q':
                    ltc += 2
                else:
                    ltc += 2

            # 3 card suit
            if len(suit_holding.strip().split(':')[1]) >= 3:
                t_cards = suit_holding.strip().split(':')[1][:3]

                if t_cards == 'AKQ':
                    ltc += 0
                elif t_cards[:2] == 'AK' or t_cards[:2] == 'AQ' or t_cards[:2] == 'KQ':
                    ltc += 1
                elif t_cards[0] == 'A' or t_cards[0] == 'K' or t_cards[0] == 'Q':
                    ltc += 2
                else:
                    ltc += 3

        return ltc

