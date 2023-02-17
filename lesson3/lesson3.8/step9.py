class Thing:
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name


class Bag:
    def __init__(self, max_weigth):
        self.maxWeight = max_weigth
        self.things = []
        self.weight = 0

    def add_thing(self, thing: Thing):
        if self.weight + thing.weight > self.maxWeight:
            raise ValueError('превышен суммарный вес предметов')
        self.things.append(thing)
        self.weight += thing.weight

    def __check_indx(self, indx):
        if indx < 0 or indx >= len(self.things):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_indx(item)
        return self.things[item]

    def __setitem__(self, key, value):
        self.__check_indx(key)
        self.weight -= self.things[key].weight
        if self.weight + value.weight > self.maxWeight:
            raise  ValueError('превышен суммарный вес предметов')
        self.things[key] = value
        self.weight += value.weight

    def __delitem__(self, key):
        self.__check_indx(key)
        del self.things[key]


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name)  # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name)  # платок
del bag[0]
print(bag[0].name)  # платок
# t = bag[4]  # генерируется исключение IndexError
