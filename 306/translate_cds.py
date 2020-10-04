from Bio.Seq import Seq
from Bio.Data import CodonTable
import re


def translate_cds(cds: str, translation_table: str) -> str:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """

    pattern = re.compile(r'\s+')

    gene = Seq(re.sub(pattern, '', cds))
    table = CodonTable.ambiguous_generic_by_name[translation_table]

    return str(gene.translate(table=table, cds=True))

