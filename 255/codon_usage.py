import os
from urllib.request import urlretrieve
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


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    # local = os.getcwd()
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    # filename = os.path.join(os.getenv("TMP", local), "NC_009641.txt")

    if not os.path.isfile(filename):
        urlretrieve(url, filename)

    with open(filename, "r") as f:
        return f.readlines()



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

    # String to return usage table
    usage_table_str = ""

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

    # Calculate total codon count for per-1000 frequency
    total_codon_count = sum(codon_count.values())

    # Convert translation table to list
    transl_list = [t for t in TRANSL_TABLE_11.splitlines() if t]
    # print(transl_list)

    usage_table_str = "|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |\n"
    usage_table_str += "-" * 105

    # Get counts for ordered codons with translated AA
    codon_usage_list = []
    for codon in all_codons:
        # Lookup AA value from translation table
        for i, letter in enumerate(codon.replace('U', 'T')):
            # Search for first letter in Base 1 in Translation List
            if i == 0:  # First letter in codon
                scnd_letter_start_idx = transl_list[i + 2].index(letter, 0)
                # print(codon, letter, i, transl_list[i+2].index(letter,0))
            elif i == 1:  # Second letter in the codon
                third_letter_start_idx = transl_list[i + 2].index(letter, scnd_letter_start_idx)
                # print(codon, letter, i, transl_list[i + 2].index(letter, scnd_letter_start_idx))
            else:  # third letter in the codon
                aa_idx = transl_list[i + 2].index(letter, third_letter_start_idx)
                # print(codon, letter, i, transl_list[i + 2].index(letter, third_letter_start_idx))

        frequency = round((codon_count.get(codon) / sum(codon_count.values()) * 1000), 1)
        codon_usage_list.append((codon, transl_list[0][aa_idx], frequency, codon_count.get(codon)))

    for chunk in [codon_usage_list[i:i + 16] for i in range(0, len(codon_usage_list), 16)]:
        for i in range(0, 4):
            codon_row_list = chunk[i::4]
            # print(codon_row_list)
            table_row_str = ''
            for c in codon_row_list:
                freq_str = " " * (4 - len(str(c[2]))) + str(c[2])
                cnt_str = " " * (5 - len(str(c[3]))) + str(c[3])
                # print(len(str(c[2])))
                # print(" " * (4 - len(str(c[2]))) + str(c[2]))
                table_row_str += '|  {}:  {}   {}  {}  '.format(c[0], c[1], freq_str, cnt_str)

            table_row_str += '|'
            usage_table_str += '\n' + table_row_str
        usage_table_str += "\n"+"-" * 105
    return usage_table_str

# def main():
#     print('thank you for the waves this morning and for looking after my family')
#     print(return_codon_usage_table())


if __name__ == "__main__":
    print(return_codon_usage_table())
