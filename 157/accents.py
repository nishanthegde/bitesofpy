
# -*- coding: utf-8 -*-


def isEnglish(s):

    try:
        s.encode(encoding='utf-8').decode('ascii')

    except UnicodeDecodeError:
        return False
    else:
        return True


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return sorted(list(set(c for c in text.lower() if not isEnglish(c))))

# def main():
#     print('here...')
#     # print(texts[0])
#     actual = filter_accents(texts[3])
#     expected = ['à', 'â', 'ç', 'è', 'é', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü']
#     assert actual == expected
#     # print(len(actual))
#     # print(len(expected))


# if __name__ == '__main__':
#     main()
