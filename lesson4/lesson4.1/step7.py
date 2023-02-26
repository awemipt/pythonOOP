class Singleton:
    entity = None

    def __new__(cls, *args, **kwargs):
        if cls.entity is None:
            cls.entity = super().__new__(cls)
        return cls.entity


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


a = Game('a')
b = Game('b')
print(b.name)
