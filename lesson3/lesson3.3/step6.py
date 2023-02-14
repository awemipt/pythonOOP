class Complex:
    @classmethod
    def check_value(cls, value):
        if type(value) not in (float, int):
            raise ValueError("Неверный тип данных.")

    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.check_value(value)
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.check_value(value)
        self.__img = value

    def __abs__(self):
        return (self.real ** 2 + self.img ** 2) ** .5

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)