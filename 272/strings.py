from typing import List

sentence1 = ['To', 'be', 'or', 'not', 'to', 'be',
             'that', 'is', 'a', 'question']
sentence2 = ['To', 'strive', 'to', 'seek', 'to',
             'find', 'and', 'not', 'to', 'yield']


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    s1 = set([word.lower() for word in sentence1])
    s2 = set([word.lower() for word in sentence2])

    both = list(s1.intersection(s2))

    return sorted(both, key=len)
