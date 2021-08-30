from functools import wraps


def check_matching(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        if args[0].shape[1] == args[1].shape[0]:
            return fun(*args, **kwargs)
        elif args[0].shape[0] == args[1].shape[0] and args[0].shape[1] == args[1].shape[1] and args[0].shape[1] != \
                args[1].shape[0]:
            return fun(*args, **kwargs)
        else:
            raise ValueError("Wrong length of elements list")

    return decorated
