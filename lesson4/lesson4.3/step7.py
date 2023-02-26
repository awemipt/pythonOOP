# здесь объявляйте функцию-декоратор
def integer_params_decorated(v):
    # print(v)
    def wrapper(*args, **kwargs):
        for x in args[1:]:
            if type(x) is not int:
                raise TypeError("аргументы должны быть целыми числами")
        if not all(type(x) is int for x in kwargs.values()):
            raise TypeError("аргументы должны быть целыми числами")


        return v(*args, **kwargs)
    return wrapper
    pass


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    # print(methods)
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
        pass
    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
# vector[1] = 20.4  # TypeError
vector.set_coords(1, 2, reverse=False)
print(vector[1])
