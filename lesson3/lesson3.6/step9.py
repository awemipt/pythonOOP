class Dimensions:
    @classmethod
    def __check_value(cls, value):
        if value <= 0:
            raise  ValueError("габаритные размеры должны быть положительными числами")



    def __init__(self, a, b, c):
        self.__check_value(a)
        self.__check_value(b)
        self.__check_value(c)
        self.a = a

        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

lst_dims = [Dimensions(*map(float, vals.split())) for vals in input().split(';')]
lst_dims.sort(key=lambda x: hash(x))
print([hash(x) for x in lst_dims])