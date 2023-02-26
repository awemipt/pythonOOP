vector_log = []


def decorated(v, vector_log):
    def wrapper(*args, **kwargs):
        f = v(*args, **kwargs)
        vector_log.append(v.__name__)
        return f

    return wrapper


def class_log(vector_log):
    def wrapper(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, decorated(v, vector_log))
        return cls
    return wrapper


class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

Vector = class_log(vector_log)(Vector)
v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)