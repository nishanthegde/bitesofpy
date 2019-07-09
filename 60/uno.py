from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')

def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""

    # one 0 card for each suit
    deck = [UnoCard(suit, name=0) for suit in SUITS]
    # for each suit
    # two 1 cards, two 2s, 3s, 4s, 5s, 6s, 7s, 8s and 9s, two Draw Two cards; two Skip cards; and two Reverse cards
    for suit in SUITS:
        for i in range(1,10):
            deck.append(UnoCard(suit, i))
            deck.append(UnoCard(suit, i))

        deck.append(UnoCard(suit, name='Draw Two'))
        deck.append(UnoCard(suit, name='Draw Two'))
        deck.append(UnoCard(suit, name='Skip'))
        deck.append(UnoCard(suit, name='Skip'))
        deck.append(UnoCard(suit, name='Reverse'))
        deck.append(UnoCard(suit, name='Reverse'))

    # four Wild cards and four Wild Draw Four cards
    deck.append(UnoCard(suit=None, name='Wild'))
    deck.append(UnoCard(suit=None, name='Wild'))
    deck.append(UnoCard(suit=None, name='Wild'))
    deck.append(UnoCard(suit=None, name='Wild'))

    deck.append(UnoCard(suit=None, name='Wild Draw Four'))
    deck.append(UnoCard(suit=None, name='Wild Draw Four'))
    deck.append(UnoCard(suit=None, name='Wild Draw Four'))
    deck.append(UnoCard(suit=None, name='Wild Draw Four'))

    return deck

# def main():
#     """
#         There are 108 cards in a Uno deck. There are four suits, Red, Green, Yellow and Blue, each consisting of one 0 card, two 1 cards, two 2s, 3s, 4s, 5s, 6s, 7s, 8s and 9s; two Draw Two cards; two Skip cards; and two Reverse cards. In addition there are four Wild cards and four Wild Draw Four cards.
#     """
#     # print(SUITS)
#     # print(type(SUITS))

#     deck = create_uno_deck()
#     # print(type(deck))
#     print(all(type(card) == UnoCard for card in deck))
#     # print(len(deck))
#     # print(deck)

#     # chk = sum(1 for card in deck if card.suit == None
#     #            and str(card.name) == 'Wild Draw Four')
#     # print(chk)

# if __name__ == "__main__":
#     main()
