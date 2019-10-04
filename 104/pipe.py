message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    msg_split = message.split('\n')
    return "|".join(msg_split)


# def main():
#     print('here...')

#     expected = ('Hello world!|We hope that you are learning a lot of Python.|'
#                 'Have fun with our Bites of Py.|Keep calm and code in Python!'
#                 '|Become a PyBites ninja!')

#     actual = split_in_columns()
#     assert actual == expected

#     expected = 'Hello world:|I am coding in Python :)|How awesome!'

#     message = 'Hello world:\nI am coding in Python :)\nHow awesome!'
#     actual = split_in_columns(message)


# if __name__ == '__main__':
#     main()
