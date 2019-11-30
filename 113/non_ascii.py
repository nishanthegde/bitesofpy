def _is_ascii(s: str)-> bool:
    return all(ord(c) < 128 for c in s)


def extract_non_ascii_words(text: str) -> list:
    """Filter a text returning a list of non-ascii words"""
    words = text.split()
    return [w for w in words if not _is_ascii(w)]


# def main():
#     print('thank you for everything ...')
#     # print(_is_ascii('saber'))
#     print(extract_non_ascii_words('This string only contains ascii words'))
#     print(extract_non_ascii_words('Sí ... habrá que saber algo de Unicode, ¿no?'))
#     print(extract_non_ascii_words('Over \u0e55\u0e57 57 flavours'))


# if __name__ == '__main__':
#     main()
