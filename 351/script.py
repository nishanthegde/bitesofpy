from typing import List, NamedTuple

from textblob import Word

MIN_CONFIDENCE = 0.5


class SuggestedWord(NamedTuple):
    word: str
    confidence: float


def get_spelling_suggestions(
        word: str, min_confidence: float = MIN_CONFIDENCE
) -> List[SuggestedWord]:
    """
    Find spelling suggestions with at least minimum confidence score
    Use textblob.Word (check out the docs)
    """
    suggestions = []
    w = Word(word)

    for s in w.spellcheck():
        if s[1] >= min_confidence:
            word = s[0]
            confidence = s[1]
            suggestions.append(SuggestedWord(word, confidence))

    return suggestions
