def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""

    word1 = str(word1.lower().strip().replace(' ', ''))
    word2 = str(word2.lower().replace(' ', ''))

    l1 = len(word1)
    l2 = len(word2)

    if l1 != l2:
        return False

    w1 = sorted(word1)
    w2 = sorted(word2)

    for i in range(0, l1):
        if w1[i] != w2[i]:
            return False

    return True


# def main():

#     print('here ... ')
#     print(is_anagram("rail safety", "fairy tales"))
#     print(is_anagram("roast beef", "eat for BSE"))
#     print(is_anagram("restful", "fluster"))
#     print(is_anagram("funeral", "real fun"))
#     print(is_anagram("adultery", "true lady"))
#     print(is_anagram("customers", "store scum"))
#     print(is_anagram("forty five", "over fifty"))

#     print(is_anagram("William Shakespeare", "I am a weakish speller"))
#     print(is_anagram("Madam Curie", "Radium came"))

#     print(is_anagram("rail safety", "fairy fun"))
#     print(is_anagram("roast beef", "eat for ME"))
#     print(is_anagram("restful", "fluester"))
#     print(is_anagram("funeral", "real funny"))
#     print(is_anagram("adultery", "true ladie"))
#     print(is_anagram("customers", "store scam"))
#     print(is_anagram("forty five", "over fifty1"))
#     print(is_anagram("William Shakespeare", "I am a strong speller"))
#     print(is_anagram("Madam Curie", "Radium come"))


# if __name__ == '__main__':
#     main()
