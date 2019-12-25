STAR = "+"
LEAF = "*"
TRUNK = "|"

default_tree = """
         +
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
    |||||||||||
    |||||||||||
"""
smaller_tree = """
  +
  *
 ***
*****
 |||
 |||
"""


def generate_improved_xmas_tree(rows: int=10) -> str:
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""

    tree = ''

    num = 1
    max_leaf = rows * 2 - 1
    for r in range(rows):
        if num % 2 != 0:
            leaf_space_buffer = (max_leaf - num) // 2
            if num == 1:
                tree += "{}{}\n".format(leaf_space_buffer * " ", num * STAR)
            # print(num, leaf_space_buffer)
            tree += "{}{}\n".format(leaf_space_buffer * " ", num * LEAF)
            # print("{}{}\n".format(leaf_space_buffer * " ", num * LEAF,))
        num += 2

    num_trunks = round(max_leaf / 2 + .5)
    if (max_leaf - num_trunks) % 2 != 0:
        num_trunks += 1

    trunk_space_buffer = (max_leaf - num_trunks) // 2
    tree += "{}{}\n".format(trunk_space_buffer * " ", num_trunks * TRUNK)
    tree += "{}{}".format(trunk_space_buffer * " ", num_trunks * TRUNK)

    return tree


# def main():
#     print('thank you for everything you have given me...')
#     # print(generate_improved_xmas_tree(3).strip("\n").split("\n"))
#     # print(len(generate_improved_xmas_tree(20).rstrip().splitlines()))
#     # print(generate_improved_xmas_tree(3))
#     # print(generate_improved_xmas_tree(20))
#     # print(generate_improved_xmas_tree(20).count("*"))
#     # print(generate_improved_xmas_tree(20).count("+"))
#     # print(len(default_tree.rstrip().splitlines()))

#     # actual_tree = generate_improved_xmas_tree(3).strip("\n").split("\n")
#     # expected_tree = default_tree.strip("\n").split("\n")
#     # expected_tree = smaller_tree.strip("\n").split("\n")

#     # for i, j in zip(actual_tree, expected_tree):
#     #     assert i.rstrip() == j.rstrip()

#     actual_tree = generate_improved_xmas_tree(3).strip("\n").split("\n")
#     expected_tree = smaller_tree.strip("\n").split("\n")
#     for i, j in zip(actual_tree, expected_tree):
#         assert i.rstrip() == j.rstrip()


# if __name__ == '__main__':
#     main()
