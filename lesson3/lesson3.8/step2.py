class Record:
    def __init__(self, **kwargs):
        self.keys = kwargs
        self.__dict__.update(kwargs)

    def __getitem__(self, item):
        if type(item) != int or item < 0 or item >= len(self.keys):
            raise IndexError('неверный индекс поля')
        return getattr(self, list(self.keys.keys())[item])

    def __setitem__(self, key, value):
        if type(key) != int or key < 0 or key >= len(self.keys):
            raise IndexError('неверный индекс поля')
        setattr(self, list(self.keys.keys())[key], value)


r = Record(pk=1, title='a', author='b')
r[0] = 2
print(r[0], r[1])
