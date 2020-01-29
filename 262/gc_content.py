from collections import Counter
import re


def calculate_gc_content(sequence: str) -> float:
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """

    sequence = re.sub(r'[.!?/, \n]', '', sequence)

    # print(sequence)
    c = Counter(sequence.upper())
    return round(((c['G'] + c['C']) / len(sequence)) * 100, 2)


def main():
    print("please let haydee be well...")
    dna = ("gtttttttgttcctggtctcgctctggctgcttgg"
           "tcgctgctgtgtttgggttgcgtgtccttgctgctttt"
           "tttctggcgggccgggcgccgctcggttgttgctttcggct"
           "ggcgtttttcgtgttcttgggtcggggtcggggctttcttttct"
           "gcgtttcgctcctcttgcttccttcttgtctccgtcc"
           "tctggcttttgctctttttctcctttcctgccggtcttcttgggg"
           "tctctggcgcttctgtgctgcgcgcgtcctgtttttttccgttttgg"
           "tcgccggttgttcccgcgtGGtcctgctttcctttcgtg"
           "tttccgtcgccgcttttctttccttccgtttcttggtgctcc"
           "gccttgggcggttccgccctttcttcggttttgtgttggctccgggg"
           "ggttcctcccgtctcgtctctctcgctgttttttctgcttctggc"
           "tggttgggtgcggctgccgcttcctttggttgcgcttcgtc"
           "tttctgtggttgtccggttttgcttttctcgttccttctttgtcc"
           "gtgtgttttctttcgggCtgcttttgttcctgcgttcgcgt")

    dna_with_spaces = "".join([base + "\n" for base in dna])

    print(calculate_gc_content(dna_with_spaces))


if __name__ == "__main__":
    main()
