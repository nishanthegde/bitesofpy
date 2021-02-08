from typing import List

sentence1 = ['To', 'be', 'or', 'not', 'to', 'be',
             'that', 'is', 'a', 'question']
sentence2 = ['To', 'strive', 'to', 'seek', 'to',
             'find', 'and', 'not', 'to', 'yield']
sentence3 = ['No', 'two', 'persons', 'ever', 'to',
             'read', 'the', 'same', 'book', 'You', 'said']
sentence4 = ['The', 'more', 'read', 'the',
             'more', 'things', 'will', 'know']
sentence5 = ['be', 'a', 'good', 'man']


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase
            words are treated as the same word.

            If there are duplicate words in the results, just choose one word.
            Returned words should be sorted by word's length.
    """
    ret = set([w.lower() for w in sentence1]) & set([w.lower() for w in sentence2])
    return sorted(ret, key=lambda k: sentence1.index(k), reverse=True)


# def main():
#     print('thank you for looking after my mama!')
#     S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything']
#     T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']
#
#     print(common_words(S, T))
#     print(common_words(sentence1, sentence2))
#
#
# if __name__ == "__main__":
#     main()
