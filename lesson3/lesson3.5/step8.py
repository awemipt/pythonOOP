class MoneyR:
    name = 'rub'

    def __init__(self, value=0):
        self.__volume = value
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def checkRegister(cls):
        if cls.cb is None:
            raise ValueError("Неизвестен курс валют.")

    def todollars(self):
        rate = self.cb.rates[self.name]
        return self.volume / rate

    def __lt__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return d1 < d2

    def __le__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return d1 <= d2

    def __eq__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return abs(d1 - d2) <= 0.1


class MoneyD:
    name = 'dollar'

    def __init__(self, value=0):
        self.__volume = value
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def checkRegister(cls):
        if cls.cb is None:
            raise ValueError("Неизвестен курс валют.")

    def todollars(self):
        rate = self.cb.rates[self.name]
        return round(self.volume / rate, 1)

    def __lt__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return d1 < d2

    def __le__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return d1 <= d2

    def __eq__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return abs(d1 - d2) <= 0.1


class MoneyE:
    name = 'euro'

    def __init__(self, value=0):
        self.__volume = value
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value


    def checkRegister(self):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют.")

    def todollars(self):
        rate = self.cb.rates[self.name]
        return round(self.volume / rate, 1)

    def __lt__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return d1 < d2

    def __le__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return d1 <= d2

    def __eq__(self, other):
        self.checkRegister()
        d1 = self.todollars()
        d2 = other.todollars()
        return abs(d1 - d2) <= 0.1


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    def __new__(cls, *args, **kwargs):
        return
    @classmethod
    def register(cls, money):
        money.cb = cls


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)
e = MoneyE(900)

CentralBank.register(r)
CentralBank.register(d)
# CentralBank.register(e)
if r > e:
    print("неплохо")
else:
    print("нужно поднажать")
