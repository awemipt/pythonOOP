class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    @classmethod
    def __check_value(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__check_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__check_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__check_value(value):
            self.__c = value

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __volume(self):
        return self.a * self.b * self.c

    def __lt__(self, other):
        return self.__volume() < other.__volume()

    def __le__(self, other):
        return self.__volume() <= other.__volume()

    def __str__(self):
        return f'{self.__volume()}'


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim
    def __repr__(self):
        return f'{self.dim}'
    # def __str__(self):
    #     return f'{self.dim}'


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40_000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
print(*lst_shop_sorted)
