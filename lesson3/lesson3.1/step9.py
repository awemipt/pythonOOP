# class descipter:
#     def __set_name__(self, owner, name):
#         self.name = '__' + name
#
#     def __set__(self, instance, value):
#         if instance.MIN_DIMENSION <= value  <= instance.MAX_DIMENSION:
#             setattr(instance, self.name, value)
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    # a = descipter()
    # b = descipter()
    # c = descipter()
    @classmethod
    def check_value(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.check_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.check_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.check_value(value):
            self.__c = value

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ['MIN_DIMENSION', 'MAX_DIMENSION']:
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super(Dimensions, self).__setattr__(key, value)


d = Dimensions(100.5, 20.1, 30)
d.a = 8000
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
print(a, b, c)
