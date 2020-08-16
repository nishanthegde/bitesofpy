import os
import urllib
from Bio import SeqIO

# local = os.getcwd()
local = "/tmp"
# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)
# TODO: UPLOAD FILE to S3
URL = "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE = os.path.join(os.getenv("TMP", local), "fasta_genes.fasta")

if not os.path.isfile(FASTA_FILE):
    urllib.request.urlretrieve(URL, FASTA_FILE)


def fasta_to_2line_fasta(fasta_file: str, fasta_2line_file: str) -> int:
    """
    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """

    with open(fasta_file, "r") as f:
        raw_lines = f.readlines()
        raw_lines = [l.replace('\n', '') if not l.strip().startswith('>') else l for l in raw_lines]
        seq_indices = []
        parsed_lines = list()

        for cntr, l in enumerate(raw_lines):
            if l.strip().startswith('>'):
                seq_indices.append(cntr)
        seq_indices.append(len(raw_lines))

        for cntr, index in enumerate(seq_indices):
            if index < len(raw_lines):
                parsed_lines.append(''.join(raw_lines[seq_indices[cntr]:seq_indices[cntr + 1]]))

    with open(fasta_2line_file, "w") as f:
        f.writelines(['{}\n'.format(ele) for ele in parsed_lines])

    return len(parsed_lines)


if __name__ == "__main__":
    fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")
