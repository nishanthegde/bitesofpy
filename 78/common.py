def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""

    set_list = [set(lang) for lang in programmers.values()]
    return set.intersection(*map(set,set_list))

# def main():
#     """{'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
#         'paul': ['C++', 'JS', 'Python'],
#         'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
#         'tim': ['Python', 'Haskell', 'C++', 'JS']}
#         Complete the common_languages function that receives a dict of this format and returns the languages that ALL devs have in common, so in this case it would return Python and JS. Under TESTS we test your code against a few more scenarios. Have fun!
#     """
#     programmers =  dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
#                             tim=['Python', 'Haskell', 'C++', 'JS'],
#                             sara=['Perl', 'C', 'Java', 'Python', 'JS'],
#                             paul=['C++', 'JS', 'Python'])
#     print(sorted(list(common_languages(programmers))))

#     # programmers['sue'] = ['Scala', 'Python']
#     # print(sorted(list(common_languages(programmers))))

#     # programmers['fabio'] = ['PHP']
#     # print(sorted(list(common_languages(programmers))))

#     programmers['bob'].append('C++')
#     programmers['sara'].append('C++')
#     print(sorted(list(common_languages(programmers))))

# if __name__ == "__main__":
#     main()
