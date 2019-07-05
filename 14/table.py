import random
# import re
# random.seed(205)

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def int_to_str(l):
    # return (str(i) if isinstance(i, int) and not isinstance(i, bool) else i for i in l)
    return (str(i) if isinstance(i, int) else i for i in l)

def generate_table(*args):

    """
        Function that receives one or more sequences and returns a table (list of strings) where the columns are the sequences (example below).
        >>> generate_table(names, aliases)
        ['Julian | Pythonista', 'Bob | Nerd', 'PyBites | Coder',
         'Dante | Pythonista', 'Martin | Nerd', 'Rodolfo | Coder']

        bonus: use a generator to build up the table rows.

    """
    arg_list = []
    for a in args:
        arg_list.append(list(int_to_str(a)))

    # print(list(x for x in zip(*arg_list)))
    # print(list(SEPARATOR.join(x) for x in zip(*arg_list)))

    if len(arg_list) > 0: # check if params is given
        if len(arg_list) == 1:
            gen = (x[0] for x in zip(*arg_list))
        else:
            # gen = (SEPARATOR.join(x) for x in zip(arg_list))
            gen = (SEPARATOR.join(x) for x in zip(*arg_list))
    else:
        gen = None

    return gen

# def main():

#     table0 = generate_table()
#     table1 = list(generate_table(names))
#     table2 = list(generate_table(names, aliases))
#     table3 = list(generate_table(names, aliases, points))
#     table4 = list(generate_table(names, aliases, points, awake))

#     print(table0)
#     print(table1)
#     print(table2)
#     print(table3)
#     print(table4)

#     # generate_table(names)
#     # generate_table(names, aliases)
#     # generate_table(names, aliases, points)
#     # generate_table(names, aliases, points, awake)
#     print(re.match(r'\d+', table3[2].split(SEPARATOR)[2]))
#     print(table4[3].split(SEPARATOR)[3])
# if __name__ == "__main__":
#     main()
