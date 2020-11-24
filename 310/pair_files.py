def pair_files(filenames):
    """
    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    valid_filenames = [f for f in filenames if f.lower().strip().endswith('fastq.gz')]

    # parse through each file name and separate into R1 files and R2 files
    r1_files = [f for f in valid_filenames if f.split('_')[len(f.split('_')) - 2].lower() == 'r1']
    r2_files = [f for f in valid_filenames if f.split('_')[len(f.split('_')) - 2].lower() == 'r2']

    # loop through r1 files to find match in r2
    # for f in r1_files:
    #     for i, element in enumerate(reversed(f.split('_'))):
    #         if i<=3:
    #
    #         print(i, element)

    print(r1_files, r2_files)

    for f in r1_files:
        print(split_filename(f))

    # for f in valid_filenames:
    #     print(f.split('_')[len(f.split('_'))-2])

    # return valid_filenames


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


def main():
    print("Thank you for looking after my Mama!")


# Set up for your convenience during testing
if __name__ == "__main__":
    main()
    # filenames = [
    #     "Sample1_S1_L001_R1_001.FASTQ.GZ",
    #     "Sample1_S1_L001_R2_001.fastq.gz",
    #     "Sample2_S2_L001_R1_001.fastq.gz",
    #     "sample2_s2_l001_r2_001.fastq.gz",
    # ]
    # filenames = [
    #     "NCTC8325_S1_L001_R1_001.fastq.gz",
    #     "NCTC8325_S1_L001_R2_001.fastq.gz",
    #     "E.coliK12_S2_L001_R1_001.fastq.gz",
    #     "E.coliK12_S2_L001_R2_001.fastq.gz",
    #     "C.elegans_S3_L001_R1_001.fastq.gz",
    #     "C.elegans_S3_L001_R2_001.fastq.gz",
    # ]
    # filenames = [
    #     "folder/NCTC8325_S1_L001_R1_001.FASTQ.GZ",
    #     "folder/NCTC8325_S1_L001_R2_001.FASTQ.GZ",
    #     "folder/E.coliK12_S2_L001_R1_001.fastq.gz",
    #     "folder/E.coliK12_S2_L001_R2_001.FASTQ.GZ",
    #     "folder/C.elegans_S3_L001_R1_001.fastq.GZ",
    #     "folder/C.elegans_S3_L001_R2_001.FASTQ.gz",
    # ]
    # filenames = [
    #         "NCTC8325_S1_L001_R1_001.fastq.gz",
    #         "NCTC8325_S1_L001_R1_001.md5.gz",
    #         "NCTC8325_S1_L001_R2_001.md5.gz",
    #         "NCTC8325_S1_L001_R2_001.fastq.gz",
    #         "C.elegans_S3_L001_R1_001.md5.gz",
    #         "C.elegans_S3_L001_R2_001.md5.gz",
    #     ]

    filenames = [
                    "NCTC_8325_S1_L001_R1_001.fastq.gz",
                    "NCTC_8325_S1_L001_R2_001.fastq.gz",
                    "C._ele_gans_1_S3_L001_R1_001.fastq.gz",
                    "C._ele_gans_1_S3_L001_R2_001.fastq.gz",
                ]
    # # ('Sample1_S1_L001_R1_001.FASTQ.GZ', 'Sample1_S1_L001_R2_001.fastq.gz')
    # # ('Sample2_S2_L001_R1_001.fastq.gz', 'sample2_s2_l001_r2_001.fastq.gz')

    print(pair_files(filenames))

    # for pair in pair_files(filenames):
    #     print(pair)
