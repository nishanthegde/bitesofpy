from typing import Union, List

sequence_pairs = [
    (
        "MSIQHFRVALIPFFAAFCLPVFAHPETLVKVKDAEDKLGARVGYIELDLNSGKILESFRPEERFPMMSTFKVLLCGAVLSRVDAG",
        "MSIaHFRVALIPFFAAFCLPVFAHPETLVKVKiAEDKLGARVGYIELDLNSGKILESFRPgERFPMMSTFKVLLCGAVLSRVDAG",
    ),
    (
        "QEQLGRRIHYSQNDLVEYSPVTEKHLTDGMTVRELCSAAITMSDNTAANLLLTTIGGPKELTAFLHNMGDHVTRLDRWEPELNEA",
        "QEaLGRRIHiSQNDLVEYpPVTEKHLTsGMTVRngCSAAITMSDNTppNLaaTTIGGlKELTAFLHNMGhHVTRLhRWEPELNiA",
    ),
    ("IPNDERDTTMPAAMATTLRKLLTGELLTLASRQQ", "IPNfnRDppMPppMpppLRKaaTGELgTLtSRdQ"),
    (
        "LIDWMEADKVAGPLLRSALPAGWFIADKSGAGERGSRGIIAALGPDGKPSRIVVIYTTGSQATMDERNRQIAEIGASLIKHW",
        "LIDWMsADKpGaqLLRSALPaAfFIADKdGgGfeGSRGggppLGPDGKPSRIttIYTTGSQpTiDEpNReIAEIGASLIKHW",
    ),
]

# Grabbed matrix from from
# https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
# Fixed width of 3

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

PAM70 = """#
# This matrix was produced by "pam" Version 1.0.6 [28-Jul-93]
#
# PAM 70 substitution matrix, scale = ln(2)/2 = 0.346574
#
# Expected score = -2.77, Entropy = 1.60 bits
#
# Lowest score = -11, Highest score = 13
#
    A   R   N   D   C   Q   E   G   H   I   L   K   M   F   P   S   T   W   Y   V   B   Z   X   *
A   5  -4  -2  -1  -4  -2  -1   0  -4  -2  -4  -4  -3  -6   0   1   1  -9  -5  -1  -1  -1  -2 -11
R  -4   8  -3  -6  -5   0  -5  -6   0  -3  -6   2  -2  -7  -2  -1  -4   0  -7  -5  -4  -2  -3 -11
N  -2  -3   6   3  -7  -1   0  -1   1  -3  -5   0  -5  -6  -3   1   0  -6  -3  -5   5  -1  -2 -11
D  -1  -6   3   6  -9   0   3  -1  -1  -5  -8  -2  -7 -10  -4  -1  -2 -10  -7  -5   5   2  -3 -11
C  -4  -5  -7  -9   9  -9  -9  -6  -5  -4 -10  -9  -9  -8  -5  -1  -5 -11  -2  -4  -8  -9  -6 -11
Q  -2   0  -1   0  -9   7   2  -4   2  -5  -3  -1  -2  -9  -1  -3  -3  -8  -8  -4  -1   5  -2 -11
E  -1  -5   0   3  -9   2   6  -2  -2  -4  -6  -2  -4  -9  -3  -2  -3 -11  -6  -4   2   5  -3 -11
G   0  -6  -1  -1  -6  -4  -2   6  -6  -6  -7  -5  -6  -7  -3   0  -3 -10  -9  -3  -1  -3  -3 -11
H  -4   0   1  -1  -5   2  -2  -6   8  -6  -4  -3  -6  -4  -2  -3  -4  -5  -1  -4   0   1  -3 -11
I  -2  -3  -3  -5  -4  -5  -4  -6  -6   7   1  -4   1   0  -5  -4  -1  -9  -4   3  -4  -4  -3 -11
L  -4  -6  -5  -8 -10  -3  -6  -7  -4   1   6  -5   2  -1  -5  -6  -4  -4  -4   0  -6  -4  -4 -11
K  -4   2   0  -2  -9  -1  -2  -5  -3  -4  -5   6   0  -9  -4  -2  -1  -7  -7  -6  -1  -2  -3 -11
M  -3  -2  -5  -7  -9  -2  -4  -6  -6   1   2   0  10  -2  -5  -3  -2  -8  -7   0  -6  -3  -3 -11
F  -6  -7  -6 -10  -8  -9  -9  -7  -4   0  -1  -9  -2   8  -7  -4  -6  -2   4  -5  -7  -9  -5 -11
P   0  -2  -3  -4  -5  -1  -3  -3  -2  -5  -5  -4  -5  -7   7   0  -2  -9  -9  -3  -4  -2  -3 -11
S   1  -1   1  -1  -1  -3  -2   0  -3  -4  -6  -2  -3  -4   0   5   2  -3  -5  -3   0  -2  -1 -11
T   1  -4   0  -2  -5  -3  -3  -3  -4  -1  -4  -1  -2  -6  -2   2   6  -8  -4  -1  -1  -3  -2 -11
W  -9   0  -6 -10 -11  -8 -11 -10  -5  -9  -4  -7  -8  -2  -9  -3  -8  13  -3 -10  -7 -10  -7 -11
Y  -5  -7  -3  -7  -2  -8  -6  -9  -1  -4  -4  -7  -7   4  -9  -5  -4  -3   9  -5  -4  -7  -5 -11
V  -1  -5  -5  -5  -4  -4  -4  -3  -4   3   0  -6   0  -5  -3  -3  -1 -10  -5   6  -5  -4  -2 -11
B  -1  -4   5   5  -8  -1   2  -1   0  -4  -6  -1  -6  -7  -4   0  -1  -7  -4  -5   5   1  -2 -11
Z  -1  -2  -1   2  -9   5   5  -3   1  -4  -4  -2  -3  -9  -2  -2  -3 -10  -7  -4   1   5  -3 -11
X  -2  -3  -2  -3  -6  -2  -3  -3  -3  -3  -4  -3  -3  -5  -3  -1  -2  -7  -5  -2  -2  -3  -3 -11
* -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11 -11   1"""

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
            raise AminoAcidNotFoundError("Scoring matrix does not support scoring for: ('{}', '{}')".format(s[0].upper(), s[1].upper()))

        # print(s[0], a1_i, line, score)

    return sum(scores)


def closest_match(
        reference_sequence: str, query_sequences: List[str], matrix_str: str = BLOSUM62
) -> Union[str, List, None]:
    """
    Receives a reference sequence, a list of query sequences and a matrix table
    Returns the closest matching sequence(s) or None
    """

    # TODO: Complete function


def main():
    print("thank you for everything you have given me...")

    seq1 = "MAAAAG"
    seq2 = "MAAAAO"

    print(matrix_score(seq1, seq2, PAM70))


if __name__ == "__main__":
    main()
