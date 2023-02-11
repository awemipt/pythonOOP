import time


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            super(Mechanical, self).__setattr__(key, value)
        else:
            return


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            super().__setattr__(key, value)
        else:
            return


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            super().__setattr__(key, value)
        else:
            return


a = Mechanical(10)
print(a.date)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    suit = {0: Mechanical, 1: Aragon, 2: Calcium}

    def __init__(self):
        self.slots = [None] * 3

    def add_filter(self, slot_num, filter):
        slot_num -= 1
        if type(filter) == self.suit[slot_num]:
            self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        slot_num -= 1
        self.slots[slot_num] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return all(
            [not (filter is None) and 0 <= time.time() - filter.date <= self.MAX_DATE_FILTER for filter in self.slots])


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
