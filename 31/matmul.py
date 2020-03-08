class Matrix(object):

    def __init__(self, values):
        if not isinstance(values, list):
            raise ValueError("<Matrix object must be a list of lists of ints>")

        # if (all(isinstance(item, int) for item in sub_list) for sub_list in values):
        #     raise ValueError("<Matrix object must be a list of lists of ints>")
        else:
            print([(item for item in sub_list) for sub_list in values])
            self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        """
            check for matrix multiplication criteria
            for A to be able to be multiplied by B
            number of columns in A should be equal to number of rows in B
        """
        if len(self.values) > 0:
            if len(self.values[0]) == len(other.values):
                # return f'<Matrices can be multiplied">'
                return self.values[0][0] * other.values[0][0]
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
    print(mat3)


if __name__ == "__main__":
    main()
