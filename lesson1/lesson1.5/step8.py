class Cart:
    def __init__(self, cart:list=None):
        if cart is None:
            self.goods = []
        else:
            self.goods = cart

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        lst = []
        for gd in self.goods:
            lst.append(f'{gd.name}: {gd.price}')
        return lst


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('tv1', 1000))
cart.add(TV('tv2', 10000))
cart.add(Table('lsef', 1000))
cart.add(Notebook('json', 100))
cart.add(Notebook('dkj', 100))
cart.add(Cup('mu', 10))
