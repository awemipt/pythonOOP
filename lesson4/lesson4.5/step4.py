class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    id_ = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__class__.id_
        self.__class__.id_ += 1

    def get_id(self):
        return self.__id

print(ShopItem(1,2,3).get_id())
print(ShopItem(1,2,3).get_id())