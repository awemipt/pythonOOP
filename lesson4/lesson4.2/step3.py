class ListInteger(list):
    def __init__(self, data):
        if any(map(lambda x: type(x) is not int, data)):
            raise TypeError('можно передавать только целочисленные значения')
        super().__init__(data)

    def append(self, __object) -> None:
        if type(__object) is not int:
            raise TypeError('можно передавать только целочисленные значения')
        super().append(__object)

    def __setitem__(self, key, value):
        if type(value) is not int:
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5 # TypeError