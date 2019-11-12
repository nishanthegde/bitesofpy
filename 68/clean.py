import string

exclude = set(string.punctuation)


def remove_punctuation(input_string: str)->str:
    """Return a str with punctuation chars stripped out"""
    # table = str.maketrans(dict.fromkeys(string.punctuation))
    return ''.join(c for c in input_string if c not in exclude)


# def main():
#     print('thank you for everything ...')
#     print(remove_punctuation("Some other (chars) |:-^, let's delete them"))


# if __name__ == '__main__':
#     main()
