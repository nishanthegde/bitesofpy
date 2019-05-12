NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# NUMBERS = [0, 8, 1, 2, 3, 0, 8, 3, 2]

# print(f'Original list: {NAMES}\n')
# print(f'\nOriginal list: {NUMBERS}')

# def dedup_and_title_case_names(ip_list, sort=False):
#     """Should return a list of names that are title cased, each name appears only once"""
#     unique_list = []

#     for i in ip_list:
#         if i not in unique_list:
#             unique_list.append(i)

#     if sort:
#         unique_list.sort()



#     unique_list = [x.title() if isinstance(x,str) else x for x in unique_list]

#     return unique_list

#     pass

def dedup_and_title_case_names(ip_list):
    """Should return a list of names that are title cased, each name appears only once"""
    unique_list = []

    for i in ip_list:
        if i not in unique_list:
            unique_list.append(i)

    unique_list = [x.title() if isinstance(x,str) else x for x in unique_list]

    return unique_list

    pass

# test for function
# names = dedup_and_title_case_names(NAMES)
# print(names.count('Bob Belderbos'))
# print(names.count('julian sequeira'))
# print(names.count('Brad Pitt'))
# print(len(names))

# deduped = dedup_and_title_case_names(NAMES, True)
# deduped = dedup_and_title_case_names(NUMBERS, True)

# print(f'Deduped list: {deduped}')

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # surnames = [n.split()[1] if len(n.split()) > 1 else n for n in names]
    surname_sorted = sorted(names, key=lambda x: x.split()[-1], reverse=True)

    return surname_sorted

# tests for function
# names = sort_by_surname_desc(NAMES)
# print(f'{names}')

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_names = [n.split()[0] for n in names]
    shortest_first_name = min(first_names, key=len)

    return shortest_first_name

# test for function
# shortest = shortest_first_name(NAMES)
# print(shortest)



