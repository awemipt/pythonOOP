import sys


class ShopItem:
    def __init__(self, name: str, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


# здесь объявляйте классы

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
shop_items ={}
for line in lst_in:
    tmp = line.split(': ')
    name = tmp[0]
    weight, price = tmp[1].split()
    obj = ShopItem(name, weight, price)
    if obj not in shop_items:
        shop_items[obj] = [obj,0]
    shop_items[obj][1] += 1

print(shop_items)