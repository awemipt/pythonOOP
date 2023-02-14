class Triangle:
    @classmethod
    def __checkValue(cls, value):
        if value <= 0:
            raise  ValueError("длины сторон треугольника должны быть положительными числами")

    def __checkTriangle(self, a, b, c):
        lst = sorted([a, b ,c])
        if lst[0] + lst[1] <= lst[2]:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
    def __init__(self, a, b ,c):
        self.__checkValue(a)
        self.__checkValue(b)
        self.__checkValue(c)
        self.__checkTriangle(a, b ,c)
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return self.a + self.b + self.c

    def __call__(self):
        p = len(self)/2
        return (p*(p-self.a)*(p-self.b)*(p- self.c)) ** .5

print(Triangle(3,4, 5)())
print(len(Triangle(3,4, 5)))

