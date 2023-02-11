class StringValue:

    def validate(self, value):
        return type(value) is str and self.__min_length <= len(value) <= self.__max_length

    def __init__(self, min_length=3, max_length=50):
        self.__min_length = min_length
        self.__max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class PriceValue:
    def validate(self, value):
        return type(value) is int and value <= self.__max_value

    def __init__(self, max_value=10_000):
        self.__max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.goods = []
        self.name = name

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
