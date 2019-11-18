def count_indents(text: str) -> int:
    """Takes a string and counts leading white spaces, return int count"""
    return len(text) - len(text.lstrip(' '))


# def main():
#     print('thank you for everything...')
#     print(count_indents('    string'))


# if __name__ == '__main__':
#     main()
