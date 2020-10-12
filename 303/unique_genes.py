import gzip
import os
from Bio import SeqIO, SeqRecord  # Recommended
from urllib.request import urlretrieve
from itertools import groupby


def make_fasta_from_tuple(content):
    """
    Creates a FASTA text from tuples
    """
    return_text = ""
    for header, seq in content:
        return_text += f"{header}\n{seq}\n"
    return return_text


def write_test_file(filename, content, zip=False):
    """
    Writes the contents of a FASTA fie into a physical file
    """
    if not os.path.isfile(filename):
        if not zip:
            with open(filename, "w") as f:
                f.write(make_fasta_from_tuple(content))
        else:
            with gzip.open(filename, "wt") as f:
                f.write(make_fasta_from_tuple(content))


def convert_to_unique_genes(filename_in, filename_out):
    """
    Takes a standard FASTA file or gzipped FASTA file,
    de-duplicates the file, sorts by number of occurrences and
    outputs the result in a standard FASTA file

    filename_in: str Filename of FASTA file containing duplicated genes
    filename_out: str Filename of FASTA file to output reduced file

    returns None
    """
    return_str = ''

    with open(filename_in, "r") as f:
        all_lines = f.readlines()

    genes = [l.strip() for l in all_lines[::2]]
    # print(genes)

    fastas = [l.strip() for l in all_lines[1::2]]
    # print(fastas)

    groups = [i for i, j in groupby(fastas)]
    # print(groups)

    group_indices = []
    for g in groups:
        group_indices = [i for i, val in enumerate(fastas) if val == g]
        if len(group_indices) == 1:
            return_str += '{}\n{}\n'.format(genes[group_indices[0]], g)
        else:
            # multi index group
            gene_comb_str = genes[group_indices[0]].split(']')[0].replace('tag','tags')
            for i in group_indices[1:]:
                gene_comb_str += ',{}'.format(genes[group_indices[i]].split('=')[1].replace(']', ''))
            gene_comb_str += ']'
            return_str += '{}\n{}\n'.format(gene_comb_str, g)

    with open(filename_out, "w") as f:
        f.write(return_str)


def main():
    print("thank you for looking after my mama!")

    local = os.getcwd()
    NARI_URL = "https://bites-data.s3.us-east-2.amazonaws.com/narI.fna"
    directory = "fastas"

    if not os.path.exists(directory):
        os.makedirs(directory)

    local = os.path.join(local, directory)
    p = os.path.join(local, 'order_data.fasta')

    if not os.path.isfile(p):
        urlretrieve(NARI_URL, p)

    # mimic fasta_dir function from test_unique_genes.py
    simple_fasta = [
        (">gene [locus_tag=AA11]", "AAAAAA"),
        (">gene [locus_tag=BB22]", "AAAAAA"),
        (">gene [locus_tag=CC33]", "AAAAAA"),
        (">gene [locus_tag=DD44]", "GAAAAC"),
    ]

    # print(simple_fasta)

    # Regular 2-line FASTA file (1 line header, one line sequence)
    filename = os.path.join(local, 'simple_test.fasta')
    filename_o = os.path.join(local, 'output.fasta')
    write_test_file(filename, simple_fasta)
    convert_to_unique_genes(filename, filename_o)


if __name__ == "__main__":
    main()
