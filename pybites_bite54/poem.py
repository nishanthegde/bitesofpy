INDENTS = 4

TEXT = """                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand"""

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


def print_hanging_indents(poem):
    poem_lst = poem.split("\n")
    poem_lst_fmt = list()
    indent_next = False

    for i, line in enumerate(poem_lst):
        if indent_next:
            poem_lst_fmt.append(" " * 4 + line.strip())
        else:
            poem_lst_fmt.append(line.strip())

        if line.strip() != "":
            indent_next = True
        else:
            indent_next = False

    print("\n".join([li for li in poem_lst_fmt if li != " " * 4]).strip())
