from os import path
import statistics as st
from urllib.request import urlretrieve
import os

# local = os.getcwd()
local = '/tmp'
STATS = path.join(local, 'testfiles_number_loc.txt')

if not path.isfile(STATS):
    urlretrieve('https://bit.ly/2Jp5CUt', STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""


def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file

    with open(data, 'r') as f:
        return [int(l.split()[0].strip()) for l in f.readlines()]


def create_stats_report(data=None):
    if data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())

    # taking a sample for the last section
    sample = list(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = dict(count=len(data),
                 min_=min(data),
                 max_=max(data),
                 mean=round(st.mean(data), 2),
                 pstdev=round(st.pstdev(data), 2),
                 pvariance=round(st.pvariance(data), 2),
                 sample_count=round(len(sample), 2),
                 sample_stdev=round(st.stdev(sample), 2),
                 sample_variance=round(st.variance(sample), 2),
                 )

    return STATS_OUTPUT.format(**stats)


# def main():

#     print('here ...')
#     counts = list(get_all_line_counts())
#     assert len(counts) == 186
#     assert all(isinstance(c, int) for c in counts)
#     assert sum(counts) == 8135
#     # print(get_all_line_counts())
#     # print(len(get_all_line_counts()))

#     print(create_stats_report())


# if __name__ == '__main__':
#     main()
