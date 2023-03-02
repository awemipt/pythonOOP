class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []
        self._weight = 0

    def add_thing(self, obj):
        if self._weight + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj[0])
        self._weight += obj[1]


class BoxDefender:
    def __init__(self, box):
        self.box = box

    def __enter__(self):
        self.__temp = Box(self.box._name, self.box._max_weight)

        self.__temp._things = self.box._things[:]
        self.__temp._weight = self.box._weight

        return self.__temp
    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type is None:
            self.box._things = self.__temp._things[:]
            self.box._weight = self.__temp._weight



box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 1000))
    # print(b._things)
# print(b._things)
print(box._things)
