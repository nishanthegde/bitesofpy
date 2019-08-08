import re
import itertools

# expected = [
#     r"^My house is small",
#     r"^but cosy."
# ]

# expected = [
#     r"^My house is small\s+It has a white\s+I have a very\s+My mornings are",
#     r"^but cosy\.\s+kitchen and an empty\s+comfortable couch,\s+filled with coffee",
#     r".*fridge\.\s+people love to sit\s+and reading, if only",
#     r".*on it\.\s+I had a garden",
# ]

COL_WIDTH = 20
# text = """My house is small but cosy. Lets test this out with more text so that we know that
#             this is working better."""

# text = """My house is small but cosy."""

# text = """My house is small but cosy.

#     It has a white kitchen and an empty fridge."""


# text = """My house is small but cosy.

#     It has a white kitchen and an empty fridge.

#     I have a very comfortable couch, people love to sit on it."""

# text = """I have a very comfortable couch, people love to sit on it."""

# text = """My house is small but cosy.

#     It has a white kitchen and an empty fridge.

#     I have a very comfortable couch, people love to sit on it.

#     My mornings are filled with coffee and reading, if only I had a garden"""

# text = """My mornings are filled with coffee and reading, if only I had a garden"""


def build_cols(text):
    running_width = 0
    output = []
    for line in text.split('\n'):
        if line:
            for word in line.split():
                # print(word)
                running_width += len(word) + 1
                if running_width <= COL_WIDTH + 1:
                    output.append(word)
                    # print(output)
                    # print(running_width)
                else:
                    output.append('\n')
                    running_width = len(word) + 1
                    output.append(word)
                    # print(output)
                    # print(running_width)

    output = (' '.join(output).replace(' \n ', '\n'))  # take out extra spaces
    return output


def compile_cols(all_out):

    all_out_split = {k: v.split('\n') for k, v in all_out.items()}

    # print(all_out_split)
    # a = ['My house is small', 'but cosy.']
    # b = ['It has a white', 'kitchen and an empty', 'fridge.']
    # c = ['I have a very', 'comfortable couch,', 'people love to sit', 'on it.']
    # d = ['My mornings are', 'filled with coffee', 'and reading, if only', 'I had a garden']

    # print([v for v in all_out_split.values()])

    return list(itertools.zip_longest(*[v for v in all_out_split.values()], fillvalue=''))


def _get_buffered_line(s):
    return s + ' ' * (COL_WIDTH - len(s))


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    # num_cols = text.count('\n\n') + 1

    all_out = {}

    line = text.split('\n\n')

    for i, l in enumerate(line):
        all_out[i] = build_cols(l.strip())

    all_out_compiled = compile_cols(all_out)

    return '\n'.join([' '.join(tuple(map(_get_buffered_line, e))) for e in all_out_compiled])


# def main():
#     what = text_to_columns(text)
#     print(what)
# #     # print([len(w) for w in what.split('\n')])

# #     output = text_to_columns(text).split("\n")
# #     for line, match in zip(output, expected):
# #         assert re.search(match, line)

# #     # test = [('My house is small', 'It has a white'), ('but cosy.', 'kitchen and an empty'), ('', 'fridge.')]
# #     # print([' '.join(tuple(map(_get_buffered_line, e))) for e in test])
# #     # # test_alt = [' '.join(thing[i]) for thing in test for i in range(0, len(thing))]
# #     # print(test)

# #     # test_alt = []

# #     # print([(' '.join(str(i) for i in e)) for e in test])

# #     # for i in range(0, len(test)):
# #     #     for j in range(0, len(test[i])):
# #     #         test_alt.append(' '.join(test[i][j] + ' ' * (COL_WIDTH - len(test[i][j]))))
# #     #     # test_alt.append(' '.join(thing))

# #     # print(test_alt)


# if __name__ == '__main__':
#     main()
