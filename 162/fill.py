HTML_SPACE = '&nbsp;'
DIFF_FILL = 'x'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    return '{}{}'.format(fill_char * (column_length - len(str(value))), value)


# def main():
#     print('thank you for everything ...')
#     print(prefill_with_character(1239, 4, HTML_SPACE))
#     # print(f'{HTML_SPACE*3}1')
#     # assert prefill_with_character(1) == f'{HTML_SPACE*3}1'


# if __name__ == '__main__':
#     main()
