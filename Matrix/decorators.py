from functools import wraps
from Matrix.exceptions import MyError


def check_summ_conditions(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        try:
            if len(args[0].data) == len(args[1].data) and args[0].data.shape[1] == args[1].data.shape[1]:
                return fun(*args, **kwargs)
            raise MyError(f"Entity size is not matched with other entity size: {args[0].data.shape} and {args[1].data.shape}")
        except MyError as err:
            print(err)
        except Exception as ex:
            print(ex)

    return decorated


def check_mult_conditions(fun):
    @wraps(fun)
    def wrapped(*args, **kwargs):
        try:
            if args[0].data.shape[1] == args[1].data.shape[0]:
                return fun(*args, **kwargs)
            raise MyError(f"Entity size is not matched with other entity size: {args[0].data.shape} and {args[1].data.shape}")
        except MyError as err:
            print(err)
        except Exception as ex:
            print(ex)

    return wrapped
