import numpy as np

from decorators import check_matching


class Matrix():
    def __init__(self, data=None):
        self.data = self.numpy_data(data)

    def numpy_data(self, data):
        matrix = np.matrix(data)
        return matrix


class Operations():
    @staticmethod
    @check_matching
    def mult(m1, m2):
        return m1.dot(m2)

    @staticmethod
    @check_matching
    def summ(m1, m2):
        return m1 + m2


m1 = Matrix()
m2 = Matrix()
o = Operations()

first_m = m1.numpy_data([[1, 2, 3], [4, 5, 6]])
second_m = m2.numpy_data([[1, 2, 3], [0, 8, 9], [12, 45, 2]])

print(o.mult(first_m, second_m))
