from typing import List

# sentence1 = ['To', 'be', 'or', 'not', 'to', 'be',
#              'that', 'is', 'a', 'question']
# sentence2 = ['To', 'strive', 'to', 'seek', 'to',
#              'find', 'and', 'not', 'to', 'yield']
# sentence3 = ['No', 'two', 'persons', 'ever', 'to',
#              'read', 'the', 'same', 'book', 'You', 'said']
# sentence4 = ['The', 'more', 'read', 'the',
#              'more', 'things', 'will', 'know']
# sentence5 = ['be', 'a', 'good', 'man']


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase
            words are treated as the same word.

            If there are duplicate words in the results, just choose one word.
            Returned words should be sorted by word's length.
    """

    common = set([w.lower() for w in sentence1]) & set([w.lower() for w in sentence2])

    return sorted(common, key=lambda k: len(k))


# def main():
#     print('thank your for everything... ')
#     print(common_words(sentence1, sentence2))


# if __name__ == '__main__':
#     main()
