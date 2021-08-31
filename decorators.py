from functools import wraps


def check_summ_conditions(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        if args[0].shape[0] == args[1].shape[0] and args[0].shape[1] == args[1].shape[1]:
            return fun(*args, **kwargs)
        else:
            raise ValueError("Wrong length of elements list")

    return decorated


def check_mult_conditions(fun):
    @wraps(fun)
    def wrapped(*args, **kwargs):
        if args[0].shape[1] == args[1].shape[0]:
            return fun(*args, **kwargs)
        raise ValueError("Wrong length of elements list")

    return wrapped
