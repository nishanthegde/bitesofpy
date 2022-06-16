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
    hands_used = []

    for letter in word:
        if letter.upper() in LEFT_HAND_CHARS:
            hands_used.append(Hand.LEFT.value)
        else:
            hands_used.append(Hand.RIGHT.value)

    if hands_used:
        if all(x == 'left' for x in hands_used):
            return Hand.LEFT
        elif all(x == 'right' for x in hands_used):
            return Hand.RIGHT
        else:
            return Hand.BOTH