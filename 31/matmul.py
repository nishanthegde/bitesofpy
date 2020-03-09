class Matrix(object):

    def __init__(self, values):
        if not isinstance(values, list):
            raise ValueError("<Matrix object must be a list of lists>")
        else:
            for sub_list in values:
                for i in sub_list:
                    if not isinstance(i, int):
                        raise ValueError("<Matrix object must be a list of lists of ints>")
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        """
            check for matrix multiplication criteria
            for A to be able to be multiplied by B
            number of columns in A should be equal to number of rows in B
        """
        product_matrix = []
        if len(self.values) > 0:
            if len(self.values[0]) == len(other.values):
                # matrices can be multiplied
                # return self.values[0][0] * other.values[0][0]
                for idx_row_m1, row_m1 in enumerate(self.values):  # for each row in matrix1
                    # for idx_col_m1 in range(0, len(self.values[0])):  # for each col in matrix1
                    # print(idx_row_m1, row_m1)
                    product_row = []
                    for idx_col_m2 in range(0, len(other.values[0])):  # for each col in matrix2
                        col_m2 = []
                        for row_m2 in other.values:  # for each row in matrix2
                            col_m2.append(row_m2[idx_col_m2])
                        # multiply row_m1 and col_m2
                        product = 0
                        for i in range(0, len(row_m1)):
                            product += row_m1[i] * col_m2[i]
                        product_row.append(product)
                    product_matrix.append(product_row)
                return Matrix(product_matrix)
            else:
                raise ValueError("<Matrix multiplication criteria not met>")


def main():
    print("thank you for the waves...")
    A = [[1, 2], [3, 4]]
    B = [[11, 12], [13, 14]]
    # B = 3
    # B = [['', 12], [13, 14]]
    mat1 = Matrix(A)
    mat2 = Matrix(B)
    mat3 = mat1 @ mat2
    print(mat3.values)
    mat3 = mat2 @ mat1
    print(mat3.values)


if __name__ == "__main__":
    main()
