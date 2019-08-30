import re


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""

    score = 0

    # up_low_reg = re.compile(r'.*[A-Z].*[a-z].*'))

    # if up_low_reg.search(password):
    # score += 1

    if (any(char.isupper() for char in password) and any(char.islower() for char in password)):
        # print('here1')
        score += 1

    if (any(char.isdigit() for char in password) and any(char.isalpha() for char in password)):
        # print('here2')
        score += 1

    sp_char_reg_ex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if sp_char_reg_ex.search(password):
        # print('here3')
        score += 1

    rep_regex = re.compile('(.)\\1{1,}')
    if len(password) >= 8:
        # print('here4')
        score += 1
        # print(rep_regex.search(password))
        if not rep_regex.search(password):
            # print('here5')
            score += 1

    return score


# def main():
#     """
#         Password has both lower- and uppercase letters,
#         Password contains one or more numbers in addition to one or more characters,
#         Password has one or more special characters,
#         Password has a minimum length of 8 characters,
#         Password starting 8 chars ("long enough") that doesn't have repeating characters ('1234abcd' = good, '1234abbd' = bad)
#     """
#     tests = ['abc', 'ABC', '123', 'abc1', 'ABC1', '@', 'aA@', 'aA1@', 'aA1@1224', 'aA1@1234', 'aaaabbbbc', 'abcdabcd', 'Abcdabcd', 'Abcdabc$',
#              'Abcdab1$', 'Abcdaac$', '123$abc', '123$abC', '123$abcd', '123$abC1', '123$abb1', '123$Abb1', '123$Abc1', '@@@@@@@@@@',
#              '@$@$@$@$@$'
#              ]
#     for password in tests:
#         print(password, password_complexity(password))

#     # password = '@$@$@$@$@$'
#     # print(password, password_complexity(password))


# if __name__ == '__main__':
#     main()
