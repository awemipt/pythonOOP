class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    @staticmethod
    def __check_type(key):
        if type(key) is not Thing:
            raise TypeError('ключами могут быть только объекты класса Thing')
    def __init__(self, things={}):
        if type(things) is not dict:
            raise TypeError('аргумент должен быть словарем')

        for x in things:
            self.__check_type(x)
        super().__init__(things)
    
    def __setitem__(self, key, value):
        self.__check_type(key)
        super(DictShop, self).__setitem__(key, value)

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

# dict_things[1] = th_1 # исключение TypeError`