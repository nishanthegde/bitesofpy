from typing import List

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
