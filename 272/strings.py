from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    sentence1_set = set([w.lower() for w in sentence1])
    sentence2_set = set([w.lower() for w in sentence2])

    common = list(sentence1_set.intersection(sentence2_set))

    return sorted(common, key=len)
