from statistics import median
from decimal import Decimal
import collections


class IntList(list):

    @property
    def mean(self):
        if self:
            return sum(self) / len(self)

    @property
    def median(self):
        if self:
            return median(self)

    def append(self, item):

        if isinstance(item, collections.Sequence):
            for i in item:
                if not rep_int(i):
                    raise TypeError
                super(IntList, self).append(int(i))
        else:
            if not rep_int(item):
                raise TypeError
            super(IntList, self).append(int(item))

    def __add__(self, other):
        return self.append(other)

    def __iadd__(self, other):
        self.append(other)
        return self


def rep_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# def main():
#     list1 = IntList([5, 1, 3])
#     list2 = IntList([2, 3, 4, 5, 7])
#     assert list1.mean == 3
#     assert list1.median == 3

#     list1.append(7)
#     assert list1.mean == 4
#     assert list1.median == 4

#     assert list2.mean == 4.2
#     assert list2.median == 4

#     list2.append(9.0)
#     list2.append(Decimal(11))
#     assert round(list2.mean, 2) == 5.86
#     assert list2.median == 5

#     # list1.append('a')
#     # list1.append(['a'])
#     # list1.append({'a': 1})

#     # print(list1)
#     # list1.append([9.0, Decimal(10)])
#     # print(list1)
#     # list1 += [1, 2, 3]
#     # list1 + [2, 'a']
#     # list1 += ['a']
#     # print(list1)
#     # print(list1)
#     list1 += [1, Decimal(10)]
#     print(list1)


# if __name__ == "__main__":
#     main()
