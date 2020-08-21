import csv
from typing import List

YEAR = '2020'


def class_rosters(input_file: str) -> List[str]:
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    ret = list()

    try:
        with open(input_file) as f:
            for line in f.readlines():
                student_id = line.strip().split(',')[0]
                classes = [c.strip().split(' - ')[0] for c in line.strip().split(',')[3:] if c]
                if classes:
                    for c in classes:
                        out_str = c + ',' + YEAR + ',' + student_id
                        ret.append(out_str)

                # print(student_id, classes)
        return ret
    except:
        print('File not found!')
