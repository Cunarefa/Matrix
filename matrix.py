import numpy as np

from decorators import check_summ_conditions, check_mult_conditions


class Matrix():
    def __init__(self, data=None):
        self.data = self.numpy_data(data)

    def numpy_data(self, data):
        matrix = np.matrix(data)
        return matrix


class Operations():
    @staticmethod
    @check_mult_conditions
    def mult(m1, m2):
        sums_of_elem = [sum(elem) for elem in m2.tolist()]
        if any(sums_of_elem) > 0:
            return m1.dot(m2)
        return m2

    @staticmethod
    @check_summ_conditions
    def summ(m1, m2):
        return m1 + m2


m1 = Matrix()
m2 = Matrix()
o = Operations()

list_a = [[1, 2, 3], [4, 5, 6]]
list_b = [[1, 2, 3], [0, 8, 9], [12, 45, 2]]
zero_list = np.full(6, 0).reshape(2, 3)

first_m = m1.numpy_data(list_a)
second_m = m2.numpy_data(list_b)

print(o.mult(first_m, second_m))
