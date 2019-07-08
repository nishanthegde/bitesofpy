import numpy as np

class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""

        #initialize 2d np array
        a = np.ones((length, length))

        #populate array
        for i in range(length):
            a[i] = [x*(i+1) for x in list(range(1,length+1))]

        self._table = a.astype(int)

    def __len__(self):
        """Returns the area of the table (len x*len y)"""
        return self._table.shape[0] * self._table.shape[1]

    def __str__(self):
        """Returns a string representation of the table"""
        res = ''
        for i in range(self._table.shape[0]):
            res += ' | '.join(map(str, self._table[i])) + '\n'

        return res

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        return self._table[x-1,y-1]


# def main():
#     """
#     Complete the MultiplicationTable class below implementing the following methods:

#     Use __init__ (constructor) to store the (x,y) coordinates and their multiplication result in a data structure (say in self._table).
#     __len__ should return the area of the table (len x* len y)
#     __str__ should give a visual representation of the table, for example a 3x3 length table should return this str:

#      1 | 2 | 3
#      2 | 4 | 6
#      3 | 6 | 9

#     The calc_cell method should take a x and y coordinate and return the result multiplying them. If x/y are out of range, raise an IndexError.
#     """

#     a = MultiplicationTable(3)
#     print(len(a))
#     print(a._table)
#     print(type(a._table))

#     # print(' | '.join(map(str, a._table[0])))

#     # a = MultiplicationTable(2)
#     # print(len(a))

#     # a = MultiplicationTable(1)
#     # print(len(a))

#     # a = MultiplicationTable(100)
#     # print(len(a))

#     op = str(a)
#     print('1 | 2 | 3' in op)
#     print('2 | 4 | 6' in op)
#     print('3 | 6 | 9' in op)


#     res = a.calc_cell(7,6)
#     print(res)
#     print(type(res))

# if __name__ == "__main__":
#     main()
