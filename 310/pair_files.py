import collections


def pair_files(filenames):
    """
    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    ret = []

    valid_filenames = [f for f in filenames if f.lower().strip().endswith('fastq.gz')]

    # parse through each file name and separate into R1 files and R2 files
    r1_files = [f for f in valid_filenames if f.split('_')[len(f.split('_')) - 2].lower() == 'r1']
    r2_files = [f for f in valid_filenames if f.split('_')[len(f.split('_')) - 2].lower() == 'r2']

    r1_split_files = [split_filename(f) for f in r1_files]
    r2_split_files = [split_filename(f) for f in r2_files]

    # print(r1_split_files, r2_split_files)

    for f in r1_split_files:
        if len(f) != 5:
            return retr
        if len(f[-1]) != 12:
            return ret
        if len(f[2]) != 4:
            return ret
        if len(f[1]) != 2:
            return ret

    for f in r2_split_files:
        if len(f) != 5:
            return retr
        if len(f[-1]) != 12:
            return ret
        if len(f[2]) != 4:
            return ret
        if len(f[1]) != 2:
            return ret

    # find matches from r1 to r2
    for i, f1 in enumerate(r1_split_files):
        for j, f2 in enumerate(r2_split_files):
            if collections.Counter([e.lower() for e in f1]) == collections.Counter(
                    ['r1' if e.lower() == 'r2' else e.lower() for e in f2]):
                ret.append((r1_files[i], r2_files[j]))

    # for f in valid_filenames:
    #     print(f.split('_')[len(f.split('_'))-2])

    return ret


def split_filename(filename: str) -> list:
    filename_split = []
    sample_name = []

    for i, element in enumerate(reversed(filename.split('_'))):
        if i <= 3:
            filename_split.append(element)
        else:
            sample_name.append(element)

    filename_split.append('_'.join(reversed(sample_name)))

    return list(reversed(filename_split))


# if __name__ == "__main__":
#     main()
#     # filenames = [
#     #     "Sample1_S1_L001_R1_001.FASTQ.GZ",
#     #     "Sample1_S1_L001_R2_001.fastq.gz",
#     #     "Sample2_S2_L001_R1_001.fastq.gz",
#     #     "sample2_s2_l001_r2_001.fastq.gz",
#     # ]
#     # filenames = [
#     #     "NCTC8325_S1_L001_R1_001.fastq.gz",
#     #     "NCTC8325_S1_L001_R2_001.fastq.gz",
#     #     "E.coliK12_S2_L001_R1_001.fastq.gz",
#     #     "E.coliK12_S2_L001_R2_001.fastq.gz",
#     #     "C.elegans_S3_L001_R1_001.fastq.gz",
#     #     "C.elegans_S3_L001_R2_001.fastq.gz",
#     # ]
#     # filenames = [
#     #     "folder/NCTC8325_S1_L001_R1_001.FASTQ.GZ",
#     #     "folder/NCTC8325_S1_L001_R2_001.FASTQ.GZ",
#     #     "folder/E.coliK12_S2_L001_R1_001.fastq.gz",
#     #     "folder/E.coliK12_S2_L001_R2_001.FASTQ.GZ",
#     #     "folder/C.elegans_S3_L001_R1_001.fastq.GZ",
#     #     "folder/C.elegans_S3_L001_R2_001.FASTQ.gz",
#     # ]
#     # filenames = [
#     #         "NCTC8325_S1_L001_R1_001.fastq.gz",
#     #         "NCTC8325_S1_L001_R1_001.md5.gz",
#     #         "NCTC8325_S1_L001_R2_001.md5.gz",
#     #         "NCTC8325_S1_L001_R2_001.fastq.gz",
#     #         "C.elegans_S3_L001_R1_001.md5.gz",
#     #         "C.elegans_S3_L001_R2_001.md5.gz",
#     #     ]
#
#     # filenames = [
#     #     "NCTC_8325_S1_L001_R1_001.fastq.gz",
#     #     "NCTC_8325_S1_L001_R2_001.fastq.gz",
#     #     "C._ele_gans_1_S3_L001_R1_001.fastq.gz",
#     #     "C._ele_gans_1_S3_L001_R2_001.fastq.gz",
#     # ]
#
#     filenames = [
#             "NCTC8325_S1_L001_r1_001.fastq.gz",
#             "NCTC8325_S1_L001_r2_001.fastq.gz",
#             "E.coliK12_S2_l001_R1_001.fastq.gz",
#             "E.coliK12_S2_l001_r2_001.fastq.gz",
#             "C.elegans_s3_L001_r1_001.fastq.gz",
#             "C.elegans_s3_L001_R2_001.fastq.gz",
#         ]
#
#     # filenames = [
#     #     "NCTC8325_S1_L001_R1_001.fastq.gz.fastq.gz",
#     #     "NCTC8325_S1_L001_R2_001.fastq.gz.fastq.gz",
#     # ]
#
#     # filenames = [
#     #     "NCTC8325_S_L001_R1_001.fastq.gz",
#     #     "NCTC8325_S_L001_R2_001.fastq.gz",
#     # ]
#
#     print(pair_files(filenames))
#
#
# # Set up for your convenience during testing
# def main():
#     print("Thank you for looking after my Mama!")

