from typing import Union, List


BLOSUM62 = """#  Matrix made by matblas from blosum62.iij
#  * column uses minimum score
#  BLOSUM Clustered Scoring Matrix in 1/2 Bit Units
#  Blocks Database = /data/blocks_5.0/blocks.dat
#  Cluster Percentage: >= 62
#  Entropy =   0.6979, Expected =  -0.5209
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V  B  Z  X  *
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0 -2 -1  0 -4
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3 -1  0 -1 -4
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  3  0 -1 -4
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  4  1 -1 -4
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1 -3 -3 -2 -4
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0  3 -1 -4
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3 -1 -2 -1 -4
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0  0 -1 -4
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3 -3 -3 -1 -4
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1 -4 -3 -1 -4
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0  1 -1 -4
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1 -3 -1 -1 -4
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1 -3 -3 -1 -4
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2 -2 -1 -2 -4
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0  0  0 -4
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0 -1 -1  0 -4
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3 -4 -3 -2 -4
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1 -3 -2 -1 -4
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4 -3 -2 -1 -4
B -2 -1  3  4 -3  0  1 -1  0 -3 -4  0 -3 -3 -2  0 -1 -4 -3 -3  4  1 -1 -4
Z -1  0  0  1 -3  3  4 -2  0 -3 -3  1 -1 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
X  0 -1 -1 -1 -2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2  0  0 -2 -1 -1 -1 -1 -1 -4
* -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4  1 """


class Error(Exception):
    """Base class for other exceptions"""
    pass


class AminoAcidNotFoundError(KeyError):
    """Raised when the input value is too small"""
    pass


def process_matrix(matrix_str: str) -> List[str]:
    return [l for l in matrix_str.split('\n') if not l.startswith("#")]


def matrix_score(sequence1: str, sequence2: str, matrix_str: str = BLOSUM62) -> int:
    """
    Receives two proteins sequences and a matrix table
    Returns the score of two proteins according to the supplied matrix table
    """

    sequences = list(zip(sequence1, sequence2))
    # print(sequences)

    scores = list()

    for s in sequences:
        # find index of amino in seq1 from col header row in similarity matrix
        a1_i = process_matrix(matrix_str)[0].find(s[0].upper())
        line = [l for l in process_matrix(matrix_str) if l.startswith(s[1].upper())]

        if line:
            score = int(line[0][a1_i - 2:a1_i + 1].strip())
            scores.append(score)
        else:
            raise AminoAcidNotFoundError(
                "Scoring matrix does not support scoring for: ('{}', '{}')".format(s[0].upper(), s[1].upper()))

        # print(s[0], a1_i, line, score)

    return sum(scores)


def closest_match(
        reference_sequence: str, query_sequences: List[str], matrix_str: str = BLOSUM62
) -> Union[str, List, None]:
    """
    Receives a reference sequence, a list of query sequences and a matrix table
    Returns the closest matching sequence(s) or None
    """
    if not query_sequences:
        return None

    closest_matches = [0]

    high_score = matrix_score(reference_sequence, query_sequences[0], matrix_str)

    for i, s in enumerate(query_sequences[1:]):
        score = matrix_score(reference_sequence, s, matrix_str)

        if score == high_score:
            # closest_matches.pop()
            closest_matches.append(i + 1)

        if score > high_score:
            closest_matches.clear()
            closest_matches.append(i + 1)
            high_score = score

        # print(s, score, high_score)

    if len(closest_matches) == 1:
        return query_sequences[closest_matches[0]]
    else:
        return [query_sequences[i] for i in closest_matches]


# if __name__ == "__main__":
#     main()
#
#
# def main():
#     print("thank you for everything you have given me...")
#
#     seq1 = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
#     seq2 = "mIlwmrllpllallalwgpdpaaaDvnqhlcgshlvealylvcgergDDytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
#
#     # print(matrix_score(seq1, seq2, PAM70))
#
#     # print(closest_match(HUMAN_INSULIN, INSULIN_VARIANTS_NO_TIE, BLOSUM62))
#     # print(closest_match(HUMAN_INSULIN, INSULIN_VARIANTS_NO_TIE, PAM70))
#     #
#     # print(closest_match(HUMAN_INSULIN, INSULIN_VARIANTS_TIES, PAM70))
#     # print(closest_match(HUMAN_INSULIN, INSULIN_VARIANTS_TIES, PAM70))
#
#     print(closest_match("MAAAAG", ["MAAAAO"], PAM70))
