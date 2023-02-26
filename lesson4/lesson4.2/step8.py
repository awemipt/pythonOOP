class IteratorAttrs:
    def __iter__(self):
        self.iter = iter(list(self.__dict__))
        return self

    def __next__(self):
        key = next(self.iter)
        return key, self.__dict__[key]

class SmartPhone(IteratorAttrs):
    def __init__(self, name, size, memory):
        self.name = name
        self.size = size
        self.memory = memory


phone = SmartPhone('a', 10,100)
for attr, value in phone:
    print(attr, value)
a = iter(phone)
print(next(a))
print(next(a))
print(next(a))
print(next(a))