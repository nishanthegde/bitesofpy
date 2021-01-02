from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    if cols <= 0:
        raise ValueError('number of columns must be a positive integer')

    line = ''
    go_to_new_line = cols
    remainder = len(names) % cols

    for name in names:
        filler = ' ' * (10 - len(name))
        if go_to_new_line != 1:
            line += f'| {name}{filler}'
            go_to_new_line -= 1
        else:
            line += f'| {name}{filler}'
            print(line)
            line = ''
            go_to_new_line = cols

    if remainder > 0:
        line = ''
        for name in names[-remainder:]:
            filler = ' ' * (10 - len(name))
            line += f'| {name}{filler}'
        print(line)
