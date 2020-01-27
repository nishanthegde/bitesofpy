import test_reverse_complement as trc


# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base   Complementary Base
 A  T
 T  A
 G  C
 C  G
"""


# Recommended helper function
def _clean_sequence(sequence: str, str_table: str) -> str:
    """
    Receives a DNA sequence and all str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """

    lookup_dict = _create_dna_dict(str_table)

    return "".join(c.upper() for c in sequence if c.upper() in lookup_dict)


def _create_dna_dict(str_table: str) -> dict:
    """
    Receives a DNA sequence str_table that defines valid
    (and complementary) bases and returns dict -> key:base, value:complementary base
    """
    dna = dict()
    str_lines = str_table.splitlines()
    for i in range(2, len(str_lines)):
        dna[str_lines[i].strip()[0]] = str_lines[i].strip()[-1]

    return dna


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    return _clean_sequence(sequence, str_table)[::-1]


def complement(sequence: str, str_table: str=SIMPLE_COMPLEMENTS_STR) -> str:
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    complement = ""
    lookup_dict = _create_dna_dict(str_table)

    for i in _clean_sequence(sequence, str_table):
        complement += lookup_dict.get(i.upper())

    return complement


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    return complement(reverse(sequence, str_table), str_table)


def main():
    print("thank you for everything you have given me...")

    # print(_create_dna_dict(SIMPLE_COMPLEMENTS_STR))
    # print(trc.COMPLEMENTS_STR)
    # print(_create_dna_dict(trc.COMPLEMENTS_STR))

    # print(complement('TTTAAAGGGCCC'))
    # print(_clean_sequence('t!t%ttttAACCG', SIMPLE_COMPLEMENTS_STR))

    print(reverse_complement('TTTAAAGGGCCC'))


if __name__ == "__main__":
    main()
