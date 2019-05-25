VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""

    while True:
        color = input('Enter a color or ''quit'' to exit: ')
        color = color.lower()

        if color == 'quit':
            print('bye')
            break
        else:
            if color not in [c.lower() for c in VALID_COLORS]:
                print('Not a valid color')
                continue
            else:
                print(f'{color}')


