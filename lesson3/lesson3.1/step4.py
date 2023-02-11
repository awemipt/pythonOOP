class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)
    pass


class Product:
    uid = 1

    def __init__(self, name, weight, price):
        self.uid = Product.uid
        Product.uid += 1
        self.name = name
        self.weight = weight
        self.price = price

    def __delattr__(self, item):
        if item == 'uid':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            super().__delattr__(item)

    def __setattr__(self, key, value):
        if key == 'uid':
            if not type(value) is int:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key in ['weight', 'price']:
            if not type(value) in [int, float] or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'name':
            if not type(value) is str:
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.uid},{p.name}, {p.weight}, {p.price}")

print(book.__dict__)