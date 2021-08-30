# mat1.dot(mat2) - умножение


import numpy as np

from decorators import check_matching
from mixins import NumpyMixin


class Matrix(NumpyMixin):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    @check_matching
    def multiple(self):
        sums_of_elem = [sum(elem) for elem in self.matrix2]
        if any(sums_of_elem) > 0:
            self.numpy_matrix(self.matrix1, self.matrix2)
            return self.mult()
        else:
            return np.matrix(self.matrix2)

    @check_matching
    def summ(self):
        self.numpy_matrix(self.matrix1, self.matrix2)
        return self.summ1()

    @check_matching
    def minus(self):
        self.numpy_matrix(self.matrix1, self.matrix2)
        return self.min()


zero_lists = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
two_lists = [[1, 2, 3], [4, 5, 6]]
three_lists = [[4, 28, 5], [8, 87, 19], [3, 29, 4]]
three_lists2 = [[7, 8, 9], [3, 6, 9], [38, 2, 85]]
four_lists = [[7, 8, 9], [38, 2, 85], [3, 6, 9], [3, 3, 3]]

mult = Matrix(two_lists, three_lists)
summ = Matrix(three_lists2, three_lists)
zero_mult = Matrix(two_lists, zero_lists)

print(mult.multiple())
print()
print(summ.summ())
