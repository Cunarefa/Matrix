import numpy as np

from decorators import check_summ_conditions, check_mult_conditions


class Matrix(object):
    def __init__(self, data=None):
        self.data = np.matrix(data)

    @check_mult_conditions
    def __mul__(self, other):
        sums_of_elem = [sum(elem) for elem in other.data.tolist()]
        if any(sums_of_elem) > 0:
            return self.data * other.data
        return other.data

    @check_summ_conditions
    def __add__(self, other):
        return self.data + other.data

    @check_summ_conditions
    def __sub__(self, other):
        return self.data - other.data


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[1, 2, 3], [0, 8, 9], [4, 9, 3]])

zero = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

m1 + m2
