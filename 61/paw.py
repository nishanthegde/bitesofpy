from collections import namedtuple, Counter
import random

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


def divide_chunks(l, n):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


def assign_actions(actions):

    chunked = list(divide_chunks(actions, len(NUMBERS)))

    if len(chunked) >= len(NUMBERS):  # used when n is >= NUMBERS eg n=8 and NUMBERS=4
        actions_left = {k: int(len(chunked) / len(NUMBERS)) for k in ACTIONS}
        # print(actions_left)
        # print('-' * 50)
        for c in chunked:
            idx = random.randint(0, len(NUMBERS) - 1)
            # print(c)
            actions_keys_gtr0 = [a for a in actions_left.keys() if actions_left[a] > 0]
            prev_choice = ''
            if actions_keys_gtr0:
                choice = random.choice(actions_keys_gtr0)
                # print(choice)
                actions_left[choice] -= 1
                # print(actions_left)
                c[idx] = choice
                # print(c)
            else:
                # eg n=17 and NUMBERS=4 last 2 iterations
                choice = random.choice([a for a in ACTIONS if a != prev_choice])
                c[idx] = choice
                prev_choice = choice
                # print(c)
    # print(actions_left)

    else:  # eg n=2 and NUMBERS=4
        prev_choice = ''
        for c in chunked:
            idx = random.randint(0, len(NUMBERS) - 1)
            choice = random.choice([a for a in ACTIONS if a != prev_choice])
            c[idx] = choice
            prev_choice = choice

    return chunked


def create_paw_deck(n=8):

    try:
        if int(n) > 0 and int(n) < 27:
            # print(ord("A"))
            # Create alphabet list of uppercase letters
            letters = []
            for letter in range(65, 65 + n):
                letters.append(chr(letter))

            # create list of lettter numbers
            let_num = [let + str(num) for let in letters for num in NUMBERS]

            # initialize list for actions
            actions = [None] * len(letters) * len(NUMBERS)

            chunked_actions = assign_actions(actions)
            flat_actions = [item for c in chunked_actions for item in c]

            # print(flat_actions)

            deck = []
            for item in zip(let_num, flat_actions):
                deck.append(PawCard(*item))
        else:
            raise ValueError

        return deck

    except ValueError:
        raise
    # except ValueError:
    #     # print('Invalid arg!')
    #     pass


# def main():
#     """The Paw Patrol card deck consists of 32 cards ranging A1-A2..B1-B2..C..G..H3-H4. 8 of
#         these cards have an action associated: 2x draw_card, 2x play_again, 2x interchange_cards, 2x change_turn_direction which are defined in ACTIONS. So for each 4 cards one gets an action assigned. For this exercise you will assign them randomly. For this Bite complete create_paw_deck generating the deck.

#         To make it a bit more challenging it will receive an input argument n which determines the letters used in the deck:

#         the default is 8 l`etters (card range A1-H4),
#         n=16 would give you card range A1..P4,
#         n=26 gives you card range A1..Z4,
#         if n > 26 raise a ValueError.
#         as you see the number part of the card is always 1..4 (NUMBERS).
#         The function returns a list of PawCard namedtuple objects. Make sure that the right amount of actions get assigned to the cards (again the ratio = 1/4) and that they are randomly distributed. The tests check for this.
# """
#     small_deck = create_paw_deck(26)
#     # print(len(ret))

#     # assert sum(1 for card in deck if card.action is not None) == 8
#     # assert sum(1 for card in deck if card.action is None) == 24

#     # cards = [card.action for card in small_deck if card.action is not None]
#     # assert sum(Counter(cards).values()) == 4

#     # for i in range(1, 3):
#     #     deck = list(create_paw_deck(i))
#     #     # assert sum(1 for card in deck if int(card.card[1:]) == 1) == i

#     # print(deck)


# if __name__ == "__main__":
#     main()
