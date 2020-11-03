import os
from urllib.request import urlretrieve
import re
from collections import Counter
from itertools import combinations

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA

TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]

EXPECTED = """
|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |
---------------------------------------------------------------------------------------------------------
|  UUU:  F   32.7  26200  |  UCU:  S   12.9  10309  |  UAU:  Y   30.4  24332  |  UGU:  C    4.9   3919  |
|  UUC:  F   12.1   9716  |  UCC:  S    1.6   1310  |  UAC:  Y    8.6   6887  |  UGC:  C    1.2    992  |
|  UUA:  L   53.8  43053  |  UCA:  S   20.3  16267  |  UAA:  *    2.4   1909  |  UGA:  *    0.4    299  |
|  UUG:  L   13.5  10801  |  UCG:  S    4.0   3172  |  UAG:  *    0.5    405  |  UGG:  W    7.6   6055  |
---------------------------------------------------------------------------------------------------------
|  CUU:  L   10.6   8462  |  CCU:  P   10.8   8642  |  CAU:  H   18.2  14550  |  CGU:  R   13.2  10569  |
|  CUC:  L    1.9   1560  |  CCC:  P    1.0    773  |  CAC:  H    4.5   3625  |  CGC:  R    3.1   2512  |
|  CUA:  L    8.5   6808  |  CCA:  P   16.3  13009  |  CAA:  Q   36.3  29048  |  CGA:  R    4.9   3914  |
|  CUG:  L    2.3   1826  |  CCG:  P    4.1   3262  |  CAG:  Q    5.0   3977  |  CGG:  R    0.4    348  |
---------------------------------------------------------------------------------------------------------
|  AUU:  I   52.0  41646  |  ACU:  T   16.8  13481  |  AAU:  N   43.0  34398  |  AGU:  S   16.7  13345  |
|  AUC:  I   14.9  11905  |  ACC:  T    2.6   2077  |  AAC:  N   13.9  11135  |  AGC:  S    5.2   4152  |
|  AUA:  I   18.8  15063  |  ACA:  T   28.9  23134  |  AAA:  K   61.1  48950  |  AGA:  R   11.7   9372  |
|  AUG:  M   25.9  20717  |  ACG:  T    9.5   7638  |  AAG:  K   14.3  11428  |  AGG:  R    1.5   1217  |
---------------------------------------------------------------------------------------------------------
|  GUU:  V   27.4  21938  |  GCU:  A   20.4  16291  |  GAU:  D   45.6  36531  |  GGU:  G   32.6  26104  |
|  GUC:  V    7.3   5873  |  GCC:  A    4.4   3507  |  GAC:  D   12.8  10229  |  GGC:  G    9.4   7525  |
|  GUA:  V   22.8  18270  |  GCA:  A   29.9  23954  |  GAA:  E   54.6  43675  |  GGA:  G   14.2  11399  |
|  GUG:  V    9.5   7584  |  GCG:  A    9.4   7550  |  GAG:  E   10.6   8458  |  GGG:  G    4.4   3483  |
---------------------------------------------------------------------------------------------------------
""".strip()


def get_table_bars(table):
    """
    Receives a results table
    Returns a list of bars/pipes (|) per line
    """
    return [len(re.findall(r"\|", line)) for line in table.split("\n")]


def get_table_dividers(table):
    """
    Receives a results table
    Returns a list of divider rows (------)
    """
    return [len(re.findall(r"^-{3,}$", line)) for line in table.split("\n")]


def get_codons(table):
    """
    Get field "codons" from table
    Receives a results table
    Returns a list of queried field
    """
    return get_field(table, 0)


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    local = os.getcwd()
    # filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    filename = os.path.join(os.getenv("TMP", local), "NC_009641.txt")

    if not os.path.isfile(filename):
        urlretrieve(url, filename)

    with open(filename, "r") as f:
        return f.readlines()


def get_whole_table(table):
    """
    Receives a results table
    Returns all results in a list of lists with whitespace removed
    """
    return [
        entry.strip().split()
        for line in table.strip().split("\n")
        for entry in line.split("|")
        if entry.replace("-", "") != "" and entry.strip() != ""
    ]


def return_codon_usage_table(
        sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    # Regex to search for start and stop codons
    pattern = re.compile(r'(AUG)(.*)(UAG|UAA|UGA])')

    # List for valid coding sequences only
    valid_sequences = [sequence.strip() for sequence in sequences if len(sequence.strip()) % 3 == 0]

    # Loop through valid sequences and block codons into 3 character blocks
    codons = []
    for sequence in valid_sequences:
        codons.append([sequence[i:i + 3] for i in range(0, len(sequence), 3)])

    blocked_sequences = [item for codon in codons for item in codon]
    codon_count = dict(Counter(blocked_sequences))

    # Construct all 3 base combinations of codons based on  order
    all_codons = []
    for i in BASE_ORDER:
        for j in BASE_ORDER:
            for k in BASE_ORDER:
                all_codons.append('{}{}{}'.format(i, j, k))

    # Get counts for ordered codons
    for codon in all_codons:
        print(codon, codon_count.get(codon))

    return all_codons


def main():
    print('thank you for the waves this morning and for looking after my family')
    return_codon_usage_table()


if __name__ == "__main__":
    main()
