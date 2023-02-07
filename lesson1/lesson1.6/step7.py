class SingletonFive:
    amount = 0
    prev = None

    def __new__(cls, *args, **kwargs):
        if cls.amount < 5:
            cls.prev = super().__new__(cls)
            cls.amount += 1
            return cls.prev
        else:
            return cls.prev

    def __init__(self, name):
        self.name = name
        self.amount += 1



objs = [SingletonFive(str(n)) for n in range(10)]
print(*(x.amount for x in objs))
print()