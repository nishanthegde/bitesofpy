def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    if n >= 0:
        str1 = string[n:]
        str2 = string[:n]
    else:
        str1 = string[n:]
        str2 = string[:n]

    return str1 + str2


# def main():

#     assert rotate('hello', 2) == 'llohe'
#     assert rotate('hello', -2) == 'lohel'

#     string = 'bob and julian love pybites!'
#     expected = 'love pybites!bob and julian '
#     assert rotate(string, 15) == expected

#     string = expected = 'julian and bob!'
#     assert rotate(string, len(string)) == expected

#     string = 'pybites loves julian and bob!'
#     expected = 'julian and bob!pybites loves '
#     assert rotate(string, -15) == expected

#     string = 'julian and bob!'
#     expected_solution1 = 'julian and bob!'
#     expected_solution2 = ' bob!julian and'  # ;)
#     assert rotate(string, 100) in (expected_solution1,
#                                    expected_solution2)

#     mod = 100 % len(string)  # 10
#     assert rotate(string, mod) in (expected_solution1,
#                                    expected_solution2)


# if __name__ == "__main__":
#     main()
