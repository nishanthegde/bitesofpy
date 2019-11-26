NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if isinstance(name, str):
        g3_ages = [a for n, a in group3.items() if n.lower() == name.lower()]
        g2_ages = [a for n, a in group2.items() if n.lower() == name.lower()]
        g1_ages = [a for n, a in group1.items() if n.lower() == name.lower()]

        if g3_ages:
            return g3_ages[0]
        elif g2_ages:
            return g2_ages[0]
        elif g1_ages:
            return g1_ages[0]
        else:
            return NOT_FOUND

    return NOT_FOUND

# def main():
#     print('thank you for everything you have given me...')
#     assert get_person_age('tim') == 30
#     assert get_person_age('helen') == 26
#     assert get_person_age('otto') == 44

#     assert get_person_age('Tim') == 30
#     assert get_person_age('BOB') == 17
#     assert get_person_age('BrEnDa') == 17

#     assert get_person_age('timothy') == NOT_FOUND
#     assert get_person_age(None) == NOT_FOUND
#     assert get_person_age(False) == NOT_FOUND
#     assert get_person_age(-1) == NOT_FOUND

#     assert get_person_age('thomas') == 46
#     assert get_person_age('ana') == 26


# if __name__ == '__main__':
#     main()
