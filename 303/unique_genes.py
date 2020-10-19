import gzip
import os
from Bio import SeqIO, SeqRecord  # Recommended
from urllib.request import urlretrieve
from itertools import groupby
import binascii

def is_gz_file(filepath):
    with open(filepath, 'rb') as test_f:
        return binascii.hexlify(test_f.read(2)) == b'1f8b'

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

    if is_gz_file(filename_in):
        with gzip.open(filename_in, 'rt') as f:
            all_lines = f.readlines()
    else:
        with open(filename_in, "r") as f:
            all_lines = f.readlines()


    if all_lines[0][0:5].strip().replace('>', '').lower() == 'gene':

        for i in range(len(all_lines) - 2, -1, -1):
            curr_gene = all_lines[i][0:5].strip().replace('>', '').lower()
            next_gene = all_lines[i + 1][0:5].strip().replace('>', '').lower()

            if (curr_gene != 'gene' and next_gene != 'gene'):
                all_lines[i] = all_lines[i].strip() + all_lines.pop(i + 1).strip()

    if all_lines[0][0:5].strip().replace('>', '').lower() == 'nari':

        for i in range(len(all_lines) - 2, -1, -1):
            curr_gene = all_lines[i][0:5].strip().replace('>', '').lower()
            next_gene = all_lines[i + 1][0:5].strip().replace('>', '').lower()

            if (curr_gene != 'nari' and next_gene != 'nari'):
                all_lines[i] = all_lines[i].strip() + all_lines.pop(i + 1).strip()

    # print(all_lines[::2])
    genes = [l.strip() for l in all_lines[::2]]

    fastas = [l.strip().upper() for l in all_lines[1::2]]

    for i, g in enumerate(genes):
        if not g.startswith('>'):
            genes.pop(i)
            fastas.pop(i)

    # print(genes)
    # print(fastas)

    # check for multiple genes
    genes_splits = [g.split(' [')[0].lower() for g in genes]
    gene_groups = [i for i, j in groupby(genes_splits)]

    s = ""

    for gg in gene_groups:
        s += "'{}' vs. ".format(gg[1:].strip())

    s = s[:-5]

    if len(gene_groups) > 1:
        raise NameError('Gene names differ between entries: {}'.format(s))

    # groups = [i for i, j in groupby(fastas)]
    groups = list(dict.fromkeys(fastas))
    # print(mylist)
    # print(groups)


    group_indices = []
    for g in groups:
        group_indices = [i for i, val in enumerate(fastas) if val == g]
        if len(group_indices) == 1:
            return_str += '{}\n{}\n'.format(genes[group_indices[0]], g)
        else:
            # multi index group
            gene_comb_str = genes[group_indices[0]].split(']')[0].replace('tag', 'tags')
            # print(gene_comb_str)
            # print(group_indices)
            for i in group_indices[1:]:
                # print(i)
                # print(genes[i])
                # gene_comb_str += ',{}'.format(genes[group_indices[i]].split('=')[1].replace(']', ''))
                gene_comb_str += ',{}'.format(genes[i].split('=')[1].replace(']', ''))
            gene_comb_str += ']'
            return_str += '{}\n{}\n'.format(gene_comb_str, g)

    genes2 = [l.strip() for l in return_str.split('\n')[::2] if l]
    genes2_srt = sorted(genes2, key=lambda k: len(k), reverse=True)
    genes3 = [genes2.index(g) for g in genes2_srt]

    fastas2 = [l.strip() for l in return_str.split('\n')[1::2] if l]
    fastas3 = [fastas2[i] for i in genes3]

    res = [(i+'\n'+j) for i, j in zip(genes2_srt, fastas3)]

    return_str = ''
    return_str = '\n'.join(res)

    if filename_out[-3:] == '.gz':
        with gzip.open(filename_out, "wt") as f:
            f.write(return_str)
    else:
        with open(filename_out, "w") as f:
            f.write(return_str)


# def main():
#     print("thank you for looking after my mama!")
#
#     local = os.getcwd()
#     NARI_URL = "https://bites-data.s3.us-east-2.amazonaws.com/narI.fna"
#     directory = "fastas"
#
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     local = os.path.join(local, directory)
#     p = os.path.join(local, 'narI.fasta')
#
#     if not os.path.isfile(p):
#         urlretrieve(url=NARI_URL, filename=p)
#
#     # mimic fasta_dir function from test_unique_genes.py
#     simple_fasta = [
#         (">gene [locus_tag=AA11]", "AAAAAA"),
#         (">gene [locus_tag=BB22]", "AAAAAA"),
#         (">gene [locus_tag=CC33]", "AAAAAA"),
#         (">gene [locus_tag=DD44]", "GAAAAC"),
#     ]
#
#     # print(simple_fasta)
#
#     # Regular 2-line FASTA file (1 line header, one line sequence)
#     # filename = os.path.join(local, 'simple_test.fasta')
#     filename = os.path.join(local, 'simple_test.fasta.gz')
#     filename_o = os.path.join(local, 'output.fasta.gz')
#     write_test_file(filename, simple_fasta, zip=True)
#     # write_test_file(filename, simple_fasta)
#     convert_to_unique_genes(filename, filename_o)
#
#     with gzip.open(filename_o, "rt") as f:
#         assert (
#             f.readlines()[0].strip().upper()
#             == ">gene [locus_tags=AA11,BB22,CC33]".upper()
#         )
#
#
#     # FASTA File where the sequence is spread over more than one line
#     # simple_multi_fasta = simple_fasta.copy()
#     # simple_multi_fasta[0] = (">gene [locus_tag=AA11]", "AAA\nAAA")
#     # filename = os.path.join(local, 'simple_multi_fasta.fasta')
#     # filename_o = os.path.join(local, 'output1.fasta')
#     # # write_test_file(filename, simple_multi_fasta)
#     # convert_to_unique_genes(filename, filename_o)
#
#     # FASTA with upper and lower case variation in sequence
#     # seq_case_variation = simple_fasta.copy()
#     # seq_case_variation[0] = (">gene [locus_tag=AA11]", "AaAaAa")
#     # print(seq_case_variation)
#     # filename = os.path.join(local, 'seq_case_variation.fasta')
#     # write_test_file(filename, seq_case_variation)
#     # filename_o = os.path.join(local, 'output2.fasta')
#     # convert_to_unique_genes(filename, filename_o)
#
#     # FASTA File with first header missing
#     # missing_header = simple_fasta.copy()
#     # missing_header[0] = ("gene [locus_tag=AA11]", "AAAAAA")
#     # # print(missing_header)
#     # filename = os.path.join(local, 'first_header_missing.fasta')
#     # write_test_file(filename, missing_header)
#     # filename_o = os.path.join(local, 'output3.fasta')
#     # convert_to_unique_genes(filename, filename_o)
#
#     # FASTA file with more than one gene
#     # two_different_genes = simple_fasta.copy()
#     # two_different_genes[0] = (">gene2 [locus_tag=AA11]", "AAAAAA")
#     # print(two_different_genes)
#     # filename = os.path.join(local, 'two_gene_names.fasta')
#     # write_test_file(filename, two_different_genes)
#     # filename_o = os.path.join(local, 'output4.fasta')
#     # convert_to_unique_genes(filename, filename_o)
#
#     # filename = os.path.join(local, 'narI.fasta')
#     # filename_o = os.path.join(local, 'output5.fasta')
#     # convert_to_unique_genes(filename, filename_o)
#     #
#     # with open(filename_o, "r") as f:
#     #     all_lines = f.readlines()
#     #
#     # print(sum([1 for line in all_lines if line[0] == ">"]))
#     # print(all_lines[0].strip().upper())
#
#
# if __name__ == "__main__":
#     main()
