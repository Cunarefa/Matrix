import numpy as np


class NumpyMixin:
    def numpy_matrix(self, matrix1, matrix2):
        self.matrix1 = np.matrix(matrix1)
        self.matrix2 = np.matrix(matrix2)

    def summ1(self):
        return self.matrix1 + self.matrix2

    def min(self):
        return self.matrix1 - self.matrix2

    def mult(self):
        return self.matrix1.dot(self.matrix2)
