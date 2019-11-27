default_tree = """
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
"""

smaller_tree = """
  *
 ***
*****
"""


def generate_xmas_tree(rows: int =10) ->str:
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    lines = []
    pad = rows - 1
    for i in range(1, rows + 1):
        stars = i * 2 - 1
        lines.append('{}{}'.format(pad * ' ', stars * '*'))
        pad -= 1

    return '\n'.join(lines)


# def main():

#     print('thank you for everything ...')

#     expected_tree = default_tree.strip('\n').split('\n')
#     expected_tree = smaller_tree.strip('\n').split('\n')
#     print(expected_tree)

#     actual = generate_xmas_tree()
#     print(actual)

#     assert len(generate_xmas_tree().split('\n')) == 10  # default arg
#     assert len(generate_xmas_tree(5).split('\n')) == 5
#     assert len(generate_xmas_tree(20).split('\n')) == 20

#     assert generate_xmas_tree(3).count('*') == 9
#     assert generate_xmas_tree(5).count('*') == 25
#     assert generate_xmas_tree(20).count('*') == 400

#     actual_tree = generate_xmas_tree().strip('\n').split('\n')
#     expected_tree = default_tree.strip('\n').split('\n')
#     for i, j in zip(actual_tree, expected_tree):
#         assert i.rstrip() == j.rstrip()

#     actual_tree = generate_xmas_tree(3).strip('\n').split('\n')
#     expected_tree = smaller_tree.strip('\n').split('\n')
#     for i, j in zip(actual_tree, expected_tree):
#         assert i.rstrip() == j.rstrip()


# if __name__ == '__main__':
#     main()
