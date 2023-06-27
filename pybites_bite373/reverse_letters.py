def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    lstring = list(string)
    na_pos = []
    for i in range(len(lstring)):
        if not lstring[i].isalpha():
            na_pos.append(i)

    rev_lstring = [i for i in lstring if i.isalpha()][::-1]

    for p in na_pos:
        rev_lstring.insert(p, lstring[p])

    return "".join(rev_lstring)


if __name__ == "__main__":
    reverse_letters()
