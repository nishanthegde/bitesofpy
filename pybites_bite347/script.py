from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    hands = []  # 0 left, 1 right
    for letter in word:
        if letter.upper() in LEFT_HAND_CHARS:
            hands.append(Hand("left").value)
        elif letter.upper() in RIGHT_HAND_CHARS:
            hands.append(Hand("right").value)

    if len(set(hands)) == 1:
        return hands[0]
    else:
        return Hand("both").value
