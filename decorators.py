from functools import wraps


def check_matching(fun):
    @wraps(fun)
    def decorated(self, *args, **kwargs):
        if len(self.matrix1[0]) == len(self.matrix2):
            return fun(self, *args, **kwargs)
        elif len(self.matrix1) == len(self.matrix2) and len(self.matrix1[0]) == len(self.matrix2[0]) and len(
                self.matrix1[0]) != len(self.matrix2):
            return fun(self, *args, **kwargs)
        else:
            raise ValueError("Wrong length of elements list")

    return decorated
