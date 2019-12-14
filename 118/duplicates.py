def get_duplicate_indices(words: list) -> list:
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return [words.index(k) for k in counts if counts[k] > 1]


# def main():
#     print('thank you for everything...')
#     print(get_duplicate_indices(['is', 'it', 'true', 'or', 'is', 'it', 'not?']))
#     print(get_duplicate_indices(['this', 'is', 'a', 'new', 'bite', 'I', 'hope', 'this', 'bite', 'will', 'teach', 'you', 'something', 'new']))

#     words = ('List comprehensions provide a concise way to create '
#              'lists. Common applications are to make new lists where '
#              'each element is the result of some operations applied '
#              'to each member of another sequence or iterable, or to '
#              'create a subsequence of those elements that satisfy a '
#              'certain condition').split()
#     print(get_duplicate_indices(words))


# if __name__ == '__main__':
#     main()
